# Module 5: Optimization Techniques in Linear Algebra

## Introduction

For  Engineering Students, Semester IV

Linear Algebra is far more than just solving systems of equations; it is the foundational language for modeling and optimizing real-world engineering problems. This module bridges the gap between abstract vector spaces and practical applications in fields like Machine Learning, Operations Research, and Signal Processing. Optimization techniques using linear algebra allow us to find the _best_ possible solution—be it minimizing cost, maximizing profit, or achieving the most efficient design—all within a structured, mathematical framework.

## Core Concepts

### 1. Formulating an Optimization Problem

Most linear optimization problems can be stated in the **standard form**:

**Maximize (or Minimize):**
$c_1x_1 + c_2x_2 + ... + c_nx_n$

**Subject to (Constraints):**
$a_{11}x_1 + a_{12}x_2 + ... + a_{1n}x_n \leq b_1$
$a_{21}x_1 + a_{22}x_2 + ... + a_{2n}x_n \leq b_2$
...
$a_{m1}x_1 + a_{m2}x_2 + ... + a_{mn}x_n \leq b_m$

**And:**
$x_1, x_2, ..., x_n \geq 0$ **(Non-negativity constraint)**

Here:

- The expression $c^Tx$ (where $c$ and $x$ are vectors) is the **objective function** to be optimized.
- The inequalities $Ax \leq b$ (where $A$ is a matrix) represent the **constraints**.
- The solution vector $x$ contains the **decision variables**.

### 2. The Feasible Region and Optimal Solution

The constraints, being linear inequalities, define a convex polytope in n-dimensional space called the **feasible region**. This is the set of all possible solutions that satisfy the constraints. A fundamental theorem of Linear Programming states that the optimal solution (if it exists) always lies at a **vertex** (or corner point) of this feasible region.

### 3. The Simplex Method

The Simplex Method, developed by George Dantzig, is a classic algorithm for solving Linear Programming problems. It is an iterative procedure that intelligently moves from one vertex of the feasible region to an adjacent vertex, improving the value of the objective function each time, until the optimal vertex is found.

**Key steps (simplified):**

1.  **Start** with a basic feasible solution (a vertex).
2.  **Check Optimality:** If the current vertex cannot be improved upon, stop; it is optimal.
3.  **Pivot:** If not optimal, move to an adjacent vertex that gives a better objective value.
4.  **Repeat** steps 2 and 3 until the optimal solution is found.

### 4. Duality

Every linear programming problem (called the **Primal**) has a corresponding related problem called the **Dual**. The dual problem flips the objective function and constraints. For a primal _maximization_ problem with $\leq$ constraints, its dual is a _minimization_ problem with $\geq$ constraints.

The **Duality Theorem** states that if both problems have feasible solutions, then the optimal value of the primal objective function equals the optimal value of the dual objective function. Understanding duality provides deep economic interpretation (e.g., shadow prices) and can sometimes simplify complex problems.

## Example: A Production Optimization Problem

**Problem:** A company manufactures two products, A and B. Product A gives a profit of ₹5 per unit, and Product B gives ₹4 per unit. Manufacturing requires time on two machines:

- Product A requires 2 hours on Machine 1 and 1 hour on Machine 2.
- Product B requires 1 hour on Machine 1 and 2 hours on Machine 2.
  Machine 1 is available for at most 10 hours per day, and Machine 2 for 8 hours. How many of each product should be made to maximize profit?

**Formulation:**

- Let $x_1 =$ number of Product A units.
- Let $x_2 =$ number of Product B units.

**Objective Function (Maximize):** $Z = 5x_1 + 4x_2$

**Constraints:**

- Machine 1: $2x_1 + x_2 \leq 10$
- Machine 2: $x_1 + 2x_2 \leq 8$
- Non-negativity: $x_1 \geq 0, x_2 \geq 0$

**Solution (Graphical Method):**
Plot the constraints. The feasible region is a polygon with vertices at (0,0), (5,0), (0,4), and (4,2). Evaluating Z at each vertex:

- At (0,0): Z = 0
- At (5,0): Z = 25
- At (0,4): Z = 16
- At (4,2): Z = 5*4 + 4*2 = 20 + 8 = **28**

The **maximum profit is ₹28**, achieved by producing **4 units of Product A** and **2 units of Product B**. This confirms the optimal solution lies at a vertex.

## Key Points & Summary

- **Foundation:** Linear Algebra provides the tools (vectors, matrices, systems of equations) to model and solve optimization problems efficiently.
- **Standard Form:** Linear Programming problems are defined by an objective function and linear constraints, often with non-negative variables.
- **Geometric Insight:** The optimal solution lies at a corner point of the feasible region defined by the constraints.
- **Simplex Method:** A powerful and widely used algorithm that navigates these corner points to find the optimum.
- **Duality:** A profound theoretical concept that creates a paired problem, offering economic insights and alternative solution methods.
- **Engineering Applications:** These techniques are crucial in resource allocation, network flows, scheduling, portfolio optimization, and the foundational algorithms behind machine learning (e.g., Support Vector Machines).
