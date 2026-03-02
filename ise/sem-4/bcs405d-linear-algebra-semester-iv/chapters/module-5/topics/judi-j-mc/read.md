Of course. Here is a comprehensive educational note on the requested topic, tailored for  Engineering students.

# Module 5: Optimization Techniques in Linear Algebra

## Topic: The Simplex Method

### 1. Introduction

In engineering, we often face problems of maximizing or minimizing a linear function (like profit, efficiency, or cost) subject to a set of linear constraints (like resource limitations, physical laws, or capacity). These are called **Linear Programming Problems (LPP)**. The **Simplex Method**, developed by George Dantzig, is the most powerful and widely used algorithm for solving such problems. It is an iterative procedure that systematically examines the corner points (vertices) of the feasible region defined by the constraints, moving from one vertex to an adjacent one that improves the value of the objective function, until an optimal solution is found.

### 2. Core Concepts

The Simplex Method operates on a problem formulated in **Standard Form**. A maximization LPP is in standard form if:

- The objective function is to be maximized.
- All constraints (except non-negativity) are equations (`=`), not inequalities (`≤` or `≥`).
- All variables are non-negative (`x₁, x₂, ..., xₙ ≥ 0`).
- The right-hand side constants (`bᵢ`) of the constraints are non-negative.

**Key Components of the Simplex Tableau:**

To convert inequalities into equations, we introduce **slack variables**. For a `≤` constraint, a slack variable represents the unused resource and is added to the left-hand side.

1.  **Slack Variables:** For a constraint like `2x₁ + 3x₂ ≤ 100`, we add a slack variable `s₁` to get `2x₁ + 3x₂ + s₁ = 100`, where `s₁ ≥ 0`.
2.  **Basic and Non-Basic Variables:** In any simplex tableau, the variables are split into:
    - **Basic Variables (BV):** Variables that have a coefficient of 1 in one equation and 0 in all others. They form the basis for the current solution.
    - **Non-Basic Variables (NBV):** Variables set to zero.
3.  **Initial Basic Feasible Solution (BFS):** Initially, the slack variables are chosen as the basic variables. This gives the trivial starting point, often the origin (`x₁=0, x₂=0`).
4.  **Simplex Tableau:** A tabular arrangement of the coefficients of the problem. It includes:
    - Coefficient matrix for all variables (decision and slack).
    - The right-hand side (RHS) values.
    - The bottom row, called the **Cj - Zj row** or the **net evaluation row**, which indicates whether the current solution can be improved.

**The Iterative Steps:**

The method proceeds through a series of iterative steps:

1.  **Optimality Test:** If all entries in the `Cj - Zj` row are `≤ 0` (for a maximization problem), the current solution is optimal. **STOP.**
2.  **Entering Variable:** If not optimal, choose the **non-basic variable** with the _most positive_ `Cj - Zj` value (for max). This variable will enter the basis to improve the objective function.
3.  **Departing Variable (Minimum Ratio Test):** For the pivot column (entering variable's column), calculate the ratio `(RHS / Coefficient)` for each row (ignore rows with `coefficient ≤ 0`). The row with the **smallest non-negative ratio** is the pivot row. The basic variable in that row will leave the basis.
4.  **Pivoting:** Perform row operations to convert the pivot element to 1 and all other elements in the pivot column to 0. This creates a new simplex tableau and a new Basic Feasible Solution.
5.  **Repeat** steps 1-4 until the optimality condition is met.

### 3. Example (Simplified)

Maximize `Z = 3x₁ + 5x₂`
Subject to:
`x₁ ≤ 4`
`2x₂ ≤ 12`
`3x₁ + 2x₂ ≤ 18`
`x₁, x₂ ≥ 0`

**Step 1: Convert to Standard Form.** Add slack variables `s₁, s₂, s₃`.
Maximize `Z = 3x₁ + 5x₂ + 0s₁ + 0s₂ + 0s₃`
Subject to:
`x₁ + s₁ = 4`
`2x₂ + s₂ = 12`
`3x₁ + 2x₂ + s₃ = 18`
`x₁, x₂, s₁, s₂, s₃ ≥ 0`

**Step 2: Initial Tableau (Origin is BFS: `x₁=0, x₂=0`, `Z=0`)**
| | Cj | 3 | 5 | 0 | 0 | 0 | |
| :---- | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **BV** | | x₁ | x₂ | s₁ | s₂ | s₃ | RHS |
| s₁ | 0 | 1 | 0 | 1 | 0 | 0 | 4 |
| s₂ | 0 | 0 | 2 | 0 | 1 | 0 | 12 |
| s₃ | 0 | 3 | 2 | 0 | 0 | 1 | 18 |
| | Zj | 0 | 0 | 0 | 0 | 0 | 0 |
| | Cj-Zj | **3** | **5** | 0 | 0 | 0 | |

- **Entering Variable:** `x₂` (most positive `Cj-Zj = 5`).
- **Departing Variable:** Min Ratio Test: `s₁: 4/0 = ∞` (ignore), `s₂: 12/2 = 6`, `s₃: 18/2 = 9`. Min is 6, so `s₂` leaves.
- **Pivot:** On the element `2` (intersection of `x₂` column and `s₂` row).

After pivoting, the new tableau will have `x₂` as a basic variable. The process repeats until all `Cj-Zj ≤ 0`. The final solution will be `x₁=2, x₂=6` yielding `Z = 3(2) + 5(6) = 36`.

### 4. Key Points & Summary

- **Purpose:** The Simplex Method is an algorithm for solving Linear Programming Problems (maximization or minimization).
- **Process:** It's an iterative process that moves from one corner point (Basic Feasible Solution) of the feasible region to an adjacent, better one.
- **Requirements:** The problem must be converted into standard form using slack/surplus/artificial variables.
- **Mechanism:** The algorithm uses a tabular format (the simplex tableau) and key steps—the optimality test, selection of entering and departing variables via the minimum ratio test, and pivoting.
- **Optimality:** The solution is optimal when the net evaluation row (`Cj - Zj`) has no positive elements (for maximization).
- **Engineering Application:** This is fundamental in Operations Research for optimization in areas like supply chain management, network flows, production planning, and resource allocation.
