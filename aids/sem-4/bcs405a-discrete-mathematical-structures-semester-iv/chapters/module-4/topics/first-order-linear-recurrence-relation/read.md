# Module 4: First Order Linear Recurrence Relations

## Introduction

A recurrence relation defines a sequence where each term is expressed as a function of its preceding terms. They are fundamental in computer science for analyzing the time complexity of recursive algorithms (like the ones you study in Data Structures), modeling population growth, and solving combinatorial problems. The simplest type is the **First Order Linear Recurrence Relation**, which depends only on the immediately previous term.

## Core Concepts

A first order linear recurrence relation has the following form:
$$
a_n = c \cdot a_{n-1} + f(n)
$$
for $n \ge 1$, with a given initial condition $a_0 = d$.

*   **First Order:** The current term $a_n$ depends only on the **one** previous term $a_{n-1}$.
*   **Linear:** The term $a_{n-1}$ appears to the first power (no expressions like $a_{n-1}^2$ or $\sin(a_{n-1})$).
*   **Constant Coefficient:** `c` is a constant real number.
*   **Inhomogeneous Term:** $f(n)$ is a function that depends only on `n`. If $f(n) = 0$ for all `n`, the relation is called **homogeneous**.

### 1. Solving the Homogeneous Case ($f(n) = 0$)

The relation simplifies to:
$$
a_n = c \cdot a_{n-1}
$$
This is a geometric sequence. The solution is found by iterating:
$a_1 = c \cdot a_0$
$a_2 = c \cdot a_1 = c \cdot (c \cdot a_0) = c^2 a_0$
$a_3 = c \cdot a_2 = c \cdot (c^2 a_0) = c^3 a_0$
...
The closed-form solution is:
$$
a_n = a_0 \cdot c^n
$$

### 2. Solving the Non-Homogeneous Case ($f(n) \neq 0$)

The general solution is the sum of the **homogeneous solution** and a **particular solution**.
$$
a_n = a_n^{(h)} + a_n^{(p)}
$$

1.  **Find the Homogeneous Solution ($a_n^{(h)}$):** Solve as if $f(n)=0$.
    $a_n^{(h)} = A \cdot c^n$ (where $A$ is a constant to be determined later).

2.  **Find a Particular Solution ($a_n^{(p)}$):** "Guess" a solution based on the form of $f(n)$. This requires observation.

    | Form of $f(n)$               | Trial Particular Solution      |
    | ---------------------------- | ------------------------------ |
    | A constant (e.g., $k$)       | A constant (e.g., $B$)         |
    | A polynomial of degree `m`   | A polynomial of degree `m`      |
    | An exponential (e.g., $r^n$) | $B \cdot r^n$ **(if $r \neq c$)** |

    **Important:** If your guess for $a_n^{(p)}$ has the same form as $a_n^{(h)}$, you must multiply your guess by `n`.

3.  **Combine and Apply Initial Condition:** Substitute $a_n^{(h)} + a_n^{(p)}$ into the original recurrence to solve for any constants in your particular solution. Then, use the initial condition $a_0$ to solve for the final constant (like $A$).

## Example

Solve the recurrence relation: $a_n = 3a_{n-1} + 2$, for $n \ge 1$, with $a_0 = 1$.

**1. Homogeneous Solution:**
The homogeneous equation is $a_n = 3a_{n-1}$.
$a_n^{(h)} = A \cdot 3^n$

**2. Particular Solution:**
$f(n) = 2$, which is a constant. Our trial solution is a constant, $a_n^{(p)} = B$.
Substitute this trial into the original recurrence:
$B = 3B + 2$
Solve for $B$:
$B - 3B = 2$
$-2B = 2$
$B = -1$
So, $a_n^{(p)} = -1$

**3. General Solution:**
$a_n = a_n^{(h)} + a_n^{(p)} = A \cdot 3^n - 1$

**4. Apply Initial Condition:**
Use $a_0 = 1$:
$a_0 = A \cdot 3^0 - 1 = A - 1 = 1$
Therefore, $A = 2$.

**5. Final Closed-Form Solution:**
$$
a_n = 2 \cdot 3^n - 1
$$

You can verify this solution by checking the first few terms against the original recurrence.
*   $a_0 = 2\cdot1 - 1 = 1$ ✔️
*   $a_1 = 2\cdot3 - 1 = 5$. Check recurrence: $a_1 = 3(1) + 2 = 5$ ✔️
*   $a_2 = 2\cdot9 - 1 = 17$. Check recurrence: $a_2 = 3(5) + 2 = 17$ ✔️

## Key Points & Summary

*   **Definition:** A first order linear recurrence relates a term $a_n$ to its previous term $a_{n-1}$ in the form $a_n = c \cdot a_{n-1} + f(n)$.
*   **Homogeneous Solution:** Always has the form $A \cdot c^n$.
*   **General Solution:** Is the sum of the homogeneous and a particular solution: $a_n = a_n^{(h)} + a_n^{(p)}$.
*   **Particular Solution:** The form is guessed from $f(n)$. If the guess matches the homogeneous form, multiply by `n`.
*   **Application:** Crucial for calculating the computational complexity of algorithms (e.g., `T(n) = T(n-1) + n` has a complexity of $O(n^2)$).
*   **Process:** 1) Find $a_n^{(h)}$, 2) Find $a_n^{(p)}$, 3) Combine and use initial conditions to solve for constants.