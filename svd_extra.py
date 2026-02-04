import numpy as np

def svd(A, reduced=False):
    A = np.array(A, dtype=float)
    m, n = A.shape

    ATA = A.T @ A
    eigenvalues, V = np.linalg.eigh(ATA)

    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    V = V[:, idx]

    # Singular values
    singular_values = np.sqrt(np.clip(eigenvalues, 0, None))

    r = min(m, n)
    R = np.linalg.matrix_rank(A)

    U = np.zeros((m, r))
    for i in range(r):
        if singular_values[i] > 1e-10:
            U[:, i] = (A @ V[:, i]) / singular_values[i]

    if reduced:
        S = np.diag(singular_values[:r])
        Vt = V[:, :r].T
    else:
        S = np.zeros((m, n))
        for i in range(r):
            S[i, i] = singular_values[i]
        Vt = V.T

        if m > r:
            U_full = np.zeros((m, m))
            U_full[:, :r] = U
            U = U_full

    return np.round(U, 4), np.round(S, 4), np.round(Vt, 4),R



choice = input("Do you want full or reduced SVD (f/r): ").strip().lower()
reduced = (choice == 'r')

m = int(input("Row Count: "))
n = int(input("Column Count: "))

A = []
for i in range(m):
    print(f"Enter elements of row {i + 1}:")
    A.append(list(map(float, input().split())))


U, S, Vt,r = svd(A, reduced=reduced)

if(reduced):
	print("\nU:")
	print(U[:,:r])

	print("\nS:")
	print(S[:r,:r])

	print("\nVt:")
	print(Vt[:r,:])
	
else:
	print("\nU:")
	print(U)

	print("\nS:")
	print(S)

	print("\nVt:")
	print(Vt)

