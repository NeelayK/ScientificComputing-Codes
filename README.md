# Scientific Computing Lab Codes

**Course:** DSC 412 – Scientific Computing Lab
**Author:** Neelay Kamat
**Roll No:** IMS23174
**Program:** BS-MS Data Science (2023)
**Date:** March 21, 2026

---

## Overview

This repository contains implementations and analysis of fundamental **numerical linear algebra algorithms**. The focus is on:

* Mathematical understanding
* Manual implementation (without external solvers)
* Computational complexity and convergence behavior

---

##  Contents

1. Gauss Elimination
2. LU Factorization
3. QR Decomposition
4. Singular Value Decomposition (SVD)
5. Image Compression using SVD
6. Steepest Descent Method
7. Conjugate Gradient Method

---

### 1. Gauss Elimination

* Solves linear systems using row operations
* Converts matrix to upper triangular form
* Uses back-substitution to obtain solution
* **Complexity:** O(n³)

---

### 2. LU Factorization

* Decomposes matrix: **A = LU**
* Efficient for solving multiple systems with same matrix
* Uses forward & backward substitution
* **Advantage:** Reusable factorization

---

### 3. QR Decomposition

* Factorizes matrix: **A = QR**
* Q: Orthogonal matrix
* R: Upper triangular matrix
* **Application:** Least Squares Problems

---

### 4. Singular Value Decomposition (SVD)

* Factorizes matrix: **A = UΣVᵀ**
* Useful for:

  * Dimensionality reduction
  * Pseudo-inverse
  * Data compression

---

### 5. Image Compression using SVD

* Treats image as matrix
* Keeps top **k singular values**
* Reduces storage while preserving structure

**Compression Ratio:**

```
ρ = mn / (k(m + n + 1))
```

---

### 6. Steepest Descent Method

* Iterative optimization method
* Minimizes quadratic function:

```
f(x) = 1/2 xᵀAx − bᵀx
```

* Works for **symmetric positive definite (SPD)** matrices
* **Limitation:** Slow convergence

---

### 7. Conjugate Gradient Method

* Improved iterative solver for SPD systems
* Uses conjugate directions
* Much faster than steepest descent
* Ideal for large sparse systems

---

## 📊 Comparative Summary

| Algorithm          | Matrix Type | Complexity | Key Feature                 |
| ------------------ | ----------- | ---------- | --------------------------- |
| Gauss Elimination  | General     | O(n³)      | Universal method            |
| LU Factorization   | General     | O(n³)      | Reusable decomposition      |
| QR Decomposition   | Any (m×n)   | O(mn²)     | Least squares               |
| SVD                | Any (m×n)   | O(mn²)     | Low-rank approximation      |
| Steepest Descent   | SPD         | O(n²)/iter | Simple but slow             |
| Conjugate Gradient | SPD         | O(kn)      | Efficient for large systems |

---

## ⭐ If you found this useful

Consider giving the repo a star!
