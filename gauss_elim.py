m = int(input("Equations Count: "))
n = int(input("Variable Count: "))

aug = []
for i in range(m):
    print(f"Enter elements of row {i + 1}:")
    aug.append(list(map(float, input().split())))

row = 0

for col in range(n):
    if row >= m:
        break

    pivot = row
    while pivot < m and aug[pivot][col] == 0:
        pivot += 1

    if pivot == m:
        continue

    aug[row], aug[pivot] = aug[pivot], aug[row]

    pval = aug[row][col]
    for j in range(col, n + 1):
        aug[row][j] /= pval

    for i in range(row + 1, m):
        factor = aug[i][col]
        for j in range(col, n + 1):
            aug[i][j] -= factor * aug[row][j]

    row += 1

x = [0] * n
for i in range(n - 1, -1, -1):
    x[i] = aug[i][n]
    for j in range(i + 1, n):
        x[i] -= aug[i][j] * x[j]

for i in range(n):
    print(f"x{i + 1} = {x[i]}")
