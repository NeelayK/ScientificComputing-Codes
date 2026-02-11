import numpy as np

def qr_decomposition(A):
    A = np.array(A, dtype=float)
    m, n = A.shape

    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j]

        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]

        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]

    return Q, R


m = int(input("Row Count:"))
n = int(input("Column Count: "))

aug = np.zeros((m, n))
for i in range(m):
    print(f"Enter elements of row {i + 1}:")
    aug[i] = list(map(float, input().split()))




Q, R = qr_decomposition(aug)

print("Orthogonal matrix Q:\n", Q)
print("Matrix R:\n", R)

print("A reconstructed from QR:\n", Q @ R)

print("\n\nA original:\n", aug)
