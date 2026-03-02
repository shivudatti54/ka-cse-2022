Of course. Here is a comprehensive educational note on the Least Squares Problem and Least Square Error for  Engineering Students.

# Module 4: Inner Product Spaces

## Topic: Least Squares Problem and Least Square Error

### 1. Introduction

In engineering and data science, we often encounter systems of linear equations $A\vec{x} = \vec{b}$ that are **inconsistent**—meaning they have no exact solution. This happens when the vector $\vec{b}$ is not in the column space of the matrix $A$ (e.g., when we have more equations than unknowns).

The **Least Squares Method** provides a powerful workaround. Instead of finding an exact solution (which doesn't exist), we find the "best possible" approximate solution, $\hat{\vec{x}}$, by minimizing the **sum of the squares of the errors** (the differences between $A\hat{\vec{x}}$ and the actual vector $\vec{b}$). This is fundamental for regression analysis, curve fitting, signal processing, and control systems.

---

### 2. Core Concepts

#### The Problem Statement

Given an $m \times n$ matrix $A$ and a vector $\vec{b}$ in $\mathbb{R}^m$, the least squares problem is to find a vector $\hat{\vec{x}}$ in $\mathbb{R}^n$ that minimizes the quantity
$||\vec{b} - A\vec{x}||^2$.
This quantity is the squared Euclidean norm of the **error vector** $\vec{e} = \vec{b} - A\vec{x}$.

#### The Key Idea: Orthogonal Projection

The minimized error $||\vec{b} - A\hat{\vec{x}}||$ is achieved when the vector $A\hat{\vec{x}}$ is the **orthogonal projection** of $\vec{b}$ onto the column space of $A$, denoted as Col $A$.

This means the error vector $\vec{e} = \vec{b} - A\hat{\vec{x}}$ must be **orthogonal** to every vector in Col $A$. In other words, it is orthogonal to every column of $A$. This orthogonality condition gives us the formal mathematical setup:

$A\hat{\vec{x}}$ is the projection of $\vec{b}$ onto Col $A$ **if and only if**
$(\vec{b} - A\hat{\vec{x}}) \perp \text{Col } A$.

#### The Normal Equations

The orthogonality condition leads directly to the most important equation for solving least squares problems. If $\vec{e}$ is orthogonal to Col $A$, it is orthogonal to every column of $A$. This can be written as:
$A^T(\vec{b} - A\hat{\vec{x}}) = \vec{0}$.

Rearranging this gives the **Normal Equations**:
$A^TA\hat{\vec{x}} = A^T\vec{b}$.

The matrix $A^TA$ is an $n \times n$ symmetric matrix. If the columns of $A$ are linearly independent, then $A^TA$ is invertible, and the unique least squares solution is:
$\hat{\vec{x}} = (A^TA)^{-1}A^T\vec{b}$.

#### The Least Square Error

Once we have found the least squares solution $\hat{\vec{x}}$, we can calculate the **least square error**. This is the minimum value of $||\vec{b} - A\vec{x}||$ achievable. It is given by:
$\text{Least Square Error} = ||\vec{b} - A\hat{\vec{x}}||$.

This value quantifies how well our approximate solution $A\hat{\vec{x}}$ fits the actual data $\vec{b}$. A smaller error indicates a better fit.

---

### 3. Example

Let's find the least squares solution for the inconsistent system:
$
\begin{aligned}
x_1 + x_2 &= 3 \\
2x_1 - x_2 &= 1 \\
x_1 + 2x_2 &= 8 \\
\end{aligned}
$

**Step 1: Write in Matrix Form**
$A\vec{x} = \vec{b}$, where
$A = \begin{bmatrix} 1 & 1 \\ 2 & -1 \\ 1 & 2 \end{bmatrix}$, $\vec{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$, $\vec{b} = \begin{bmatrix} 3 \\ 1 \\ 8 \end{bmatrix}$.

**Step 2: Form the Normal Equations**
First, compute $A^TA$ and $A^T\vec{b}$.

$A^TA = \begin{bmatrix} 1 & 2 & 1 \\ 1 & -1 & 2 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 2 & -1 \\ 1 & 2 \end{bmatrix} = \begin{bmatrix} 1+4+1 & 1-2+2 \\ 1-2+2 & 1+1+4 \end{bmatrix} = \begin{bmatrix} 6 & 1 \\ 1 & 6 \end{bmatrix}$

$A^T\vec{b} = \begin{bmatrix} 1 & 2 & 1 \\ 1 & -1 & 2 \end{bmatrix} \begin{bmatrix} 3 \\ 1 \\ 8 \end{bmatrix} = \begin{bmatrix} 3+2+8 \\ 3-1+16 \end{bmatrix} = \begin{bmatrix} 13 \\ 18 \end{bmatrix}$

So, the normal equations are:
$\begin{bmatrix} 6 & 1 \\ 1 & 6 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 13 \\ 18 \end{bmatrix}$.

**Step 3: Solve for $\hat{\vec{x}}$**
We solve this $2 \times 2$ system:
$
\begin{aligned}
6x_1 + x_2 &= 13 \\
x_1 + 6x_2 &= 18 \\
\end{aligned}
$

Solving (e.g., by elimination), we get the least squares solution:
$\hat{\vec{x}} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} \frac{12}{7} \\ \frac{19}{7} \end{bmatrix} \approx \begin{bmatrix} 1.714 \\ 2.714 \end{bmatrix}$.

**Step 4: Compute the Least Square Error**
First, find $A\hat{\vec{x}}$:
$A\hat{\vec{x}} = \begin{bmatrix} 1 & 1 \\ 2 & -1 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} \frac{12}{7} \\ \frac{19}{7} \end{bmatrix} = \begin{bmatrix} \frac{31}{7} \\ \frac{5}{7} \\ \frac{50}{7} \end{bmatrix}$.

Now, find the error vector and its norm:
$\vec{e} = \vec{b} - A\hat{\vec{x}} = \begin{bmatrix} 3 \\ 1 \\ 8 \end{bmatrix} - \begin{bmatrix} \frac{31}{7} \\ \frac{5}{7} \\ \frac{50}{7} \end{bmatrix} = \begin{bmatrix} -\frac{10}{7} \\ \frac{2}{7} \\ \frac{6}{7} \end{bmatrix}$.

$||\vec{e}|| = \sqrt{ \left(-\frac{10}{7}\right)^2 + \left(\frac{2}{7}\right)^2 + \left(\frac{6}{7}\right)^2 } = \sqrt{ \frac{100+4+36}{49} } = \sqrt{ \frac{140}{49} } = \sqrt{\frac{20}{7}} \approx 1.69$.

This is the minimum possible error for any choice of $x_1$ and $x_2$.

---

### 4. Key Points & Summary

- **Purpose:** To find an approximate solution $\hat{\vec{x}}$ to an inconsistent system $A\vec{x} = \vec{b}$.
- **Method:** Minimize the sum of squared errors, $||\vec{b} - A\vec{x}||^2$.
- **Geometric Interpretation:** The best approximation, $A\hat{\vec{x}}$, is the orthogonal projection of $\vec{b}$ onto the column space of $A$.
- **Key Equation:** The solution is found by solving the **Normal Equations**:
  $A^TA\hat{\vec{x}} = A^T\vec{b}$.
- **Uniqueness:** If the columns of $A$ are linearly independent, $A^TA$ is invertible and $\hat{\vec{x}} = (A^TA)^{-1}A^T\vec{b}$ is unique.
- **Error:** The **Least Square Error** $||\vec{b} - A\hat{\vec{x}}||$ measures the quality of the fit. It is the distance from $\vec{b}$ to the column space of $A$.
