import numpy as np

def svd(A):
    A = np.array(A, dtype=float)

    m, n = A.shape
    ATA = A.T @ A

    eigenvalues, V = np.linalg.eigh(ATA)
    print(f"Eigen Values for At-A  is {eigenvalues}. Eigen Vectors: {V}")
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    V = V[:, idx]

    singular_values = np.sqrt(np.clip(eigenvalues, 0, None))

    print(f"Sorted Eigen Values for At-A  is {eigenvalues}. Eigen Vectors: {V}")

    U = np.zeros((m, len(singular_values)))

    for i in range(len(singular_values)):
        if singular_values[i] > 1e-10:
            U[:, i] = (A @ V[:, i]) / singular_values[i]

    
    print(f"Sorted Eigen Values for A-At  is {eigenvalues}. Eigen Vectors: {V}")
    S = np.zeros((m, n))
    for i in range(min(m, n)):
        S[i, i] = singular_values[i]
    Vt = V.T

    return U, S, Vt


m = int(input("Row Count:"))
n = int(input("Column Count: "))

aug = []
for i in range(m):
    print(f"Enter elements of row {i + 1}:")
    aug.append(list(map(float, input().split())))

U, S, Vt = svd(aug)

print(f"\n\nU: {U}\n")
print(f"S: {S}\n")
print(f"Vt: {Vt}\n")
