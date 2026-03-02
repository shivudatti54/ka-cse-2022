# Generating Functions: A Powerful Tool for Solving Recurrences

## 1. Introduction to Generating Functions

A **Generating Function** is a formal power series whose coefficients encode information about a sequence of numbers, $a_0, a_1, a_2, a_3, \dots$. It is a powerful algebraic tool that transforms problems about sequences into problems about functions, which are often easier to solve.

The **Ordinary Generating Function (OGF)** for the sequence $\{a_n\}$ is defined as:
$$ G(x) = a*0 + a_1x + a_2x^2 + a_3x^3 + \dots = \sum*{n=0}^{\infty} a_n x^n $$

Think of the variable $x$ as a placeholder. We are not concerned with its convergence in a classical sense; we treat it as a formal power series. The coefficient of $x^n$ "holds" the value of the $n$-th term of the sequence.

**Why are they useful?**

1.  **Solving Recurrences:** They can transform a recurrence relation into an algebraic equation, which is simpler to manipulate.
2.  **Combinatorial Enumeration:** They are indispensable for counting complex combinatorial structures.
3.  **Closed-Form Formulas:** They provide a method to find closed-form expressions for sequences defined recursively.

## 2. Building Blocks: Common Generating Functions

Before solving recurrences, it's crucial to know the generating functions for some fundamental sequences. These serve as our "algebraic toolkit".

| Sequence                                                    | Closed Form                | Generating Function (Series Expansion)                        |
| :---------------------------------------------------------- | :------------------------- | :------------------------------------------------------------ |
| Constant $1, 1, 1, 1, \dots$                                | $a_n = 1$                  | $\sum_{n=0}^{\infty} x^n = \frac{1}{1-x}$                     |
| Geometric $1, c, c^2, c^3, \dots$                           | $a_n = c^n$                | $\sum_{n=0}^{\infty} c^nx^n = \frac{1}{1-cx}$                 |
| Binomial Coefficients ${m \choose 0}, {m \choose 1}, \dots$ | $a_n = {m \choose n}$      | $\sum_{n=0}^{m} {m \choose n} x^n = (1+x)^m$                  |
| Generalized Binomial ${\alpha \choose n}$                   | $a_n = {\alpha \choose n}$ | $\sum_{n=0}^{\infty} {\alpha \choose n} x^n = (1+x)^{\alpha}$ |

The last one is particularly important and is known as the **Generalized Binomial Theorem**.

## 3. The Process: Solving Recurrence Relations with Generating Functions

The general strategy involves a series of algebraic steps:

1.  **Define the Generating Function:** Write down the generating function $G(x)$ for your sequence.
2.  **Multiply by Powers and Sum:** Manipulate the recurrence relation by multiplying by $x^n$ and summing over all $n$ for which the recurrence holds. This transforms the recurrence into an equation involving $G(x)$.
3.  **Solve for $G(x)$:** Solve the resulting algebraic equation to find a closed-form expression for the generating function $G(x)$.
4.  **Find the Series Expansion (Closed Form):** Express $G(x)$ as a power series again. The coefficient of $x^n$ in this expansion is the closed-form solution $a_n$ to your original recurrence.

Let's illustrate this with a detailed example.

### 3.1. Example: Solving a Linear Homogeneous Recurrence

**Problem:** Solve the recurrence relation:
$$ a*n = 3a*{n-1} + 2, \quad \text{for } n \geq 1 $$
with the initial condition $a_0 = 1$.

**Step 1: Define the Generating Function**
$$ G(x) = a*0 + a_1x + a_2x^2 + a_3x^3 + \dots = \sum*{n=0}^{\infty} a_n x^n $$

**Step 2: Multiply and Sum**
The recurrence is valid for $n \geq 1$. Multiply both sides by $x^n$ and sum over all $n \geq 1$.
$$ \sum*{n=1}^{\infty} a_n x^n = \sum*{n=1}^{\infty} (3a\_{n-1} + 2) x^n $$

The left side is almost $G(x)$, but it's missing the $n=0$ term.
$$ \sum\_{n=1}^{\infty} a_n x^n = G(x) - a_0 = G(x) - 1 $$

Now, let's break apart the right side:
$$ \sum*{n=1}^{\infty} (3a*{n-1} + 2) x^n = 3\sum*{n=1}^{\infty} a*{n-1}x^n + 2\sum\_{n=1}^{\infty} x^n $$

We adjust the indices to match the form of $G(x)$.
For the first sum, let $k = n-1$. When $n=1$, $k=0$.
$$ 3\sum*{n=1}^{\infty} a*{n-1}x^n = 3x\sum\_{k=0}^{\infty} a_k x^k = 3x G(x) $$

The second sum is a standard geometric series starting at $n=1$.
$$ 2\sum\_{n=1}^{\infty} x^n = 2(\frac{1}{1-x} - 1) = \frac{2x}{1-x} $$

Now we can put it all together into an equation:
$$ G(x) - 1 = 3x G(x) + \frac{2x}{1-x} $$

**Step 3: Solve for G(x)**
This is now an algebraic equation. Solve for $G(x)$.
$$ G(x) - 3x G(x) = 1 + \frac{2x}{1-x} $$
$$ G(x)(1 - 3x) = \frac{(1-x) + 2x}{1-x} = \frac{1 + x}{1-x} $$
$$ G(x) = \frac{1 + x}{(1-x)(1-3x)} $$

**Step 4: Find the Closed Form (Series Expansion)**
We now have $G(x)$, but we need the coefficients. We use the method of **Partial Fractions**.

We want to find constants $A$ and $B$ such that:
$$ \frac{1 + x}{(1-x)(1-3x)} = \frac{A}{1-x} + \frac{B}{1-3x} $$

Multiply both sides by $(1-x)(1-3x)$:
$$ 1 + x = A(1-3x) + B(1-x) $$
$$ 1 + x = (A + B) + (-3A - B)x $$

This gives us a system of equations:

1.  $A + B = 1$
2.  $-3A - B = 1$

Solving this system:
From (1): $B = 1 - A$
Substitute into (2): $-3A - (1 - A) = 1$ => $-3A -1 + A = 1$ => $-2A = 2$ => $A = -1$
Then $B = 1 - (-1) = 2$

So,
$$ G(x) = \frac{-1}{1-x} + \frac{2}{1-3x} $$

We recognize these as generating functions for known sequences:
$$ G(x) = -\sum*{n=0}^{\infty} x^n + 2\sum*{n=0}^{\infty} (3x)^n = \sum\_{n=0}^{\infty} ( -1 + 2 \cdot 3^n ) x^n $$

Therefore, the coefficient of $x^n$ is our solution:
$$ a_n = -1 + 2 \cdot 3^n $$

We can verify this with our initial condition: $a_0 = -1 + 2 \cdot 1 = 1$, which matches.

## 4. A More Complex Example: Fibonacci Sequence

The Fibonacci sequence is defined by:
$$ F*n = F*{n-1} + F\_{n-2}, \quad \text{for } n \geq 2 $$
with $F_0 = 0$ and $F_1 = 1$.

**Step 1: Define the Generating Function**
$$ G(x) = F*0 + F_1x + F_2x^2 + F_3x^3 + \dots = \sum*{n=0}^{\infty} F_n x^n $$

**Step 2: Multiply and Sum**
Multiply the recurrence by $x^n$ and sum over $n \geq 2$:
$$ \sum*{n=2}^{\infty} F_n x^n = \sum*{n=2}^{\infty} F*{n-1} x^n + \sum*{n=2}^{\infty} F\_{n-2} x^n $$

The left side is $G(x) - F_0 - F_1x = G(x) - 0 - x = G(x) - x$.

Adjust the indices on the right side:
Let $k = n-1$ for the first sum: $\sum_{n=2}^{\infty} F_{n-1} x^n = x\sum_{k=1}^{\infty} F_k x^k = x(G(x) - F_0) = xG(x)$
Let $m = n-2$ for the second sum: $\sum_{n=2}^{\infty} F_{n-2} x^n = x^2\sum_{m=0}^{\infty} F_m x^m = x^2 G(x)$

Putting it all together:
$$ G(x) - x = xG(x) + x^2 G(x) $$

**Step 3: Solve for G(x)**
$$ G(x) - xG(x) - x^2G(x) = x $$
$$ G(x)(1 - x - x^2) = x $$
$$ G(x) = \frac{x}{1 - x - x^2} $$

**Step 4: Find the Closed Form**
We use partial fractions on $G(x) = \frac{x}{1 - x - x^2}$. First, factor the denominator. The roots of $1 - x - x^2 = 0$ are:
$$ x = \frac{1 \pm \sqrt{1 + 4}}{2(-1)} = \frac{1 \pm \sqrt{5}}{-2} $$
Let $\phi = \frac{1+\sqrt{5}}{2}$ (the golden ratio) and $\hat{\phi} = \frac{1-\sqrt{5}}{2}$. Notice that $1 - x - x^2 = -(x^2 + x - 1) = -(x-\phi)(x-\hat{\phi})$.

We want to find $A$ and $B$ such that:
$$ \frac{x}{1 - x - x^2} = \frac{A}{1 - \alpha x} + \frac{B}{1 - \beta x} $$
It can be shown that $\alpha = \phi$ and $\beta = \hat{\phi}$. Solving the partial fractions yields:
$$ G(x) = \frac{1}{\sqrt{5}} \left( \frac{1}{1-\phi x} - \frac{1}{1-\hat{\phi} x} \right) $$

Now, we write this as a geometric series:
$$ G(x) = \frac{1}{\sqrt{5}} \left( \sum*{n=0}^{\infty} (\phi x)^n - \sum*{n=0}^{\infty} (\hat{\phi} x)^n \right) = \sum\_{n=0}^{\infty} \frac{1}{\sqrt{5}} (\phi^n - \hat{\phi}^n) x^n $$

Therefore, the coefficient of $x^n$ gives us Binet's formula:
$$ F_n = \frac{\phi^n - \hat{\phi}^n}{\sqrt{5}} $$

## 5. Key Properties and Operations

Generating functions can be manipulated using standard algebraic operations, which correspond to operations on the underlying sequence.

| Operation on Generating Function                    | Effect on Sequence $\{a_n\}$                           |
| :-------------------------------------------------- | :----------------------------------------------------- |
| **Scaling:** $c \cdot G(x)$                         | $\{c \cdot a_n\}$                                      |
| **Addition:** $G(x) + H(x)$                         | $\{a_n + b_n\}$                                        |
| **Right Shift (Mult. by x):** $x^k G(x)$            | $a_n \rightarrow a_{n-k}$ (with $a_{-1}=...=a_{-k}=0$) |
| **Left Shift (Derivative):** $G(x) - a_0 - ...}{x}$ | $a_n \rightarrow a_{n+1}$                              |
| **Convolution (Mult.):** $G(x) \cdot H(x)$          | $\{ \sum_{k=0}^{n} a_k b_{n-k} \}$                     |

## 6. Exam Tips

1.  **Memorize the Common GFs:** Know $\frac{1}{1-x}$, $\frac{1}{1-cx}$, and $(1+x)^m$ like the back of your hand. They are the building blocks.
2.  **Practice Index Shifting:** This is the most common point of error. Be meticulous when changing the index of summation. Write out the first few terms if you get stuck.
3.  **Master Partial Fractions:** Most solutions will require decomposing a rational function into simpler fractions. Be comfortable with solving the resulting system of equations.
4.  **Always Verify:** Check your closed-form solution against the initial conditions and the first few terms generated by the recurrence itself.
5.  **Show Your Work:** The process of setting up the generating function equation is worth significant marks, even if the algebraic manipulation becomes complex.
