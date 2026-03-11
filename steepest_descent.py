import numpy as np
import matplotlib.pyplot as plt

TOL = 1e-8
MAX_ITER = 1000

def f(x):
    x1, x2 = x
    return x1**2 + (x2**2)/4

def grad_f(x):
    x1, x2 = x
    return np.array([2*x1, x2/2])

A = np.array([
    [2, 0],
    [0, 0.5]
])

x1 = float(input("x1: "))
x2 = float(input("x2: "))
x = np.array([x1, x2])

points = [x.copy()]

print("\nx-------------Iteration details-------------x\n")

for k in range(MAX_ITER):

    p = -grad_f(x)
    grad_norm = np.linalg.norm(p)

    print(f"Iteration {k}")
    print("current position (x1,x2) =", x)
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
print("Mimimum value:", f(x))

x_vals = np.linspace(-20, 20, 1000)
y_vals = np.linspace(-20, 20, 1000)
X, Y = np.meshgrid(x_vals, y_vals)
Z = X**2 + Y**2/4
plt.figure()
plt.contour(X, Y, Z, cmap='gray', levels=50)


plt.plot(points[:,0], points[:,1], marker='o',color='green')

plt.scatter(points[0,0], points[0,1], s=100)
plt.scatter(0, 0, s=100)

plt.title("Steepest Descent Convergence")
plt.xlabel("x1")
plt.ylabel("x2")
plt.savefig('steepest_descent_convergence.png') #
plt.show()
