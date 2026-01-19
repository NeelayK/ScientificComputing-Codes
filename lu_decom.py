def lu_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for k in range(i, n):
            s = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - s


        L[i][i] = 1.0
        for k in range(i + 1, n):
            if U[i][i] == 0:
                raise ZeroDivisionError("LU decomposition not possible")
            s = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (A[k][i] - s) / U[i][i]

    return L, U


def forward_substitution(L, b):
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
    return y


def back_substitution(U, y):
    n = len(U)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        if U[i][i] == 0:
            raise ZeroDivisionError("Zero pivot in U")
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
    return x

n = int(input("Enter number of variables: "))

print("\nEnter matrix A (row by row):")
A = []
for i in range(n):
    row = list(map(float, input(f"Row {i + 1}: ").split()))
    if len(row) != n:
        raise ValueError("Each row must have exactly", n, "elements")
    A.append(row)

print("\nEnter vector b:")
b = list(map(float, input().split()))
if len(b) != n:
    raise ValueError("Vector b must have", n, "elements")

L, U = lu_decomposition(A)
y = forward_substitution(L, b)
x = back_substitution(U, y)

print("\nL Matrix:")
for row in L:
    print(row)

print("\nU Matrix:")
for row in U:
    print(row)

print("\nSolution Vector x:")
for i in range(n):
    print(f"x{i + 1} = {x[i]}")
