import numpy as np
import matplotlib.pyplot as plt

MAX_ITER = 200
TOL = 1e-8
ALPHA_TOL = 1e-10
MAX_ALPHA_ITER = 50

def f(x):
    x1, x2 = x
    return x1**2 + x2**4

def grad_f(x):
    x1, x2 = x
    return np.array([2*x1, 4*x2**3])

def hessian_f(x):
    return np.array([
        [2, 0],
        [0, 12*x2**2]
    ])

def compute_alpha(x, p):
    alpha = 0.0

    for _ in range(MAX_ALPHA_ITER):

        x_new = x + alpha * p
        grad = grad_f(x_new)
        H = hessian_f(x_new)

        # φ'(α)
        phi_prime = grad @ p

        # φ''(α)
        phi_double_prime = p @ H @ p

        if abs(phi_prime) < ALPHA_TOL:
            break

        alpha = alpha - phi_prime / phi_double_prime

    return alpha


x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
x = np.array([x1, x2], dtype=float)

points = [x.copy()]

print("\n--- Modified Newton Method (2D) ---\n")

for k in range(MAX_ITER):

    grad = grad_f(x)
    grad_norm = np.linalg.norm(grad)

    print(f"Iteration {k}")
    print("x =", x)
    print("f(x) =", f(x))
    print("||grad|| =", grad_norm)

    if grad_norm < TOL:
        break

    H = hessian_f(x)
    p = -np.linalg.solve(H, grad)

    alpha = compute_alpha(x, p)

    print("alpha =", alpha)
    print()

    x = x + alpha * p
    points.append(x.copy())

points = np.array(points)

print("Converged to:", x)
print("Minimum value:", f(x))

x_vals = np.linspace(-10, 10, 1000)
y_vals = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x_vals, y_vals)
Z = X**2 + Y**4

plt.figure()
plt.contour(X, Y, Z, levels=50)

plt.plot(points[:,0], points[:,1], marker='o')

plt.scatter(points[0,0], points[0,1], s=100)
plt.scatter(0, 0, s=100)

plt.title("Modified Newton Method")
plt.xlabel("x")
plt.ylabel("y")

plt.savefig("modified_newton_2d.png")
plt.show()