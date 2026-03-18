import numpy as np
import matplotlib.pyplot as plt

TOL = 1e-8
MAX_ITER = 1000

n = int(input("Enter dimension n: "))

print("Enter matrix A (row-wise):")
A = []
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)
A = np.array(A)

print("Enter vector b:")
b = np.array(list(map(float, input().split())))

print("Enter initial guess x:")
x = np.array(list(map(float, input().split())))

def f(x):
    return 0.5 * x @ A @ x - b @ x

def grad_f(x):
    return A @ x - b

points = [x.copy()]

print("\nx-------------Iteration details-------------x\n")

for k in range(MAX_ITER):

    grad = grad_f(x)
    p = -grad
    grad_norm = np.linalg.norm(p)

    print(f"Iteration {k}")
    print("current x =", x)
    print("f(x) =", f(x))
    print("||p|| =", grad_norm)
    print()

    if grad_norm < TOL:
        break

    alpha = (p @ p) / (p @ A @ p)
    x = x + alpha * p
    points.append(x.copy())

points = np.array(points)

print("Converged to:", x)
print("Minimum value:", f(x))

if n == 2:
    x_vals = np.linspace(-20, 20, 1000)
    y_vals = np.linspace(-20, 20, 1000)
    X, Y = np.meshgrid(x_vals, y_vals)

    Z = 0.5*(A[0,0]*X**2 + 2*A[0,1]*X*Y + A[1,1]*Y**2) - (b[0]*X + b[1]*Y)

    plt.figure()
    plt.contour(X, Y, Z, cmap='gray', levels=50)

    plt.plot(points[:,0], points[:,1], marker='o', color='green')
    plt.scatter(points[0,0], points[0,1], s=100, label="Start")
    plt.scatter(points[-1,0], points[-1,1], s=100, label="End")

    plt.title("Steepest Descent for Ax = b")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()

    plt.savefig('steepest_descent_Ax_eq_b.png')
    plt.show()