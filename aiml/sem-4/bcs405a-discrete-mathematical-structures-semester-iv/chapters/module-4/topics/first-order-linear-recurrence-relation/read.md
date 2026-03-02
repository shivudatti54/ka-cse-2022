# Module 4: The Principle of Inclusion and Exclusion
## Topic: First Order Linear Recurrence Relations

### 1. Introduction

A recurrence relation defines a sequence where each term is expressed as a function of its preceding terms. They are fundamental in computer science for analyzing the complexity of recursive algorithms (like those in `DSA`), modeling population growth, and solving combinatorial problems. A **First Order Linear Recurrence Relation** is the simplest type, where a term depends *only* on its immediate predecessor in a linear fashion. Understanding how to solve these relations is a key skill for engineers, providing a closed-form formula to compute any term without knowing all previous ones.

### 2. Core Concepts

A first order linear recurrence relation has the following standard form:

$$
a_n = c \cdot a_{n-1} + f(n) \quad \text{for } n \geq 1
$$

with an **initial condition** $a_0 = d$.

Where:
*   $a_n$ is the term we want to find.
*   $a_{n-1}$ is the previous term.
*   $c$ is a constant coefficient.
*   $f(n)$ is a function of $n$ (called the *non-homogeneous* part). If $f(n) = 0$, the relation is called **homogeneous**.
*   $d$ is the given initial value.

The goal is to find a **closed-form solution** (or *closed-form expression*), which is a non-recursive formula that calculates $a_n$ directly based only on $n$ and the initial condition.

#### Method of Solution: Iteration (Telescoping)

The most intuitive method for solving first order relations is **iteration**. We repeatedly substitute the recurrence relation into itself, creating a pattern that "telescopes" down to the initial condition.

**General Steps:**
1.  **Write the recurrence** for $a_n$, $a_{n-1}$, $a_{n-2}$, ..., down to $a_1$.
2.  **Substitute** each equation into the one above it.
3.  **Identify the pattern** that emerges. This will typically involve a summation.
4.  **Express $a_n$** in terms of $n$, the constant $c$, the initial condition $a_0$, and a summation of $f(k)$.
5.  **Simplify** the resulting expression, especially the summation, if possible.

### 3. Examples

#### Example 1: Homogeneous Case ($f(n)=0$)

Solve: $a_n = 3a_{n-1}$ for $n \geq 1$, with $a_0 = 5$.

**Solution via Iteration:**
$a_n = 3a_{n-1}$
$\quad = 3(3a_{n-2}) = 3^2 a_{n-2}$
$\quad = 3^2(3a_{n-3}) = 3^3 a_{n-3}$
$\quad \vdots$
$\quad = 3^k a_{n-k}$

We continue this pattern until we reach the initial condition. Let $k = n$:
$a_n = 3^n a_{n-n} = 3^n a_0$

**Final Answer:** Substitute the initial condition $a_0 = 5$:
$$a_n = 5 \cdot 3^n$$

This is the closed-form solution. To find the 10th term, we compute $5 \cdot 3^{10}$ instead of doing 10 recursive steps.

#### Example 2: Non-Homogeneous Case ($f(n) \neq 0$)

Solve: $a_n = 2a_{n-1} + 3$ for $n \geq 1$, with $a_0 = 1$.

**Solution via Iteration:**
$a_n = 2a_{n-1} + 3$
Substitute for $a_{n-1}$: $a_n = 2(2a_{n-2} + 3) + 3 = 2^2a_{n-2} + 2 \cdot 3 + 3$
Substitute for $a_{n-2}$: $a_n = 2^2(2a_{n-3} + 3) + 2\cdot3 + 3 = 2^3a_{n-3} + 2^2\cdot3 + 2\cdot3 + 3$
A clear pattern emerges. After $n$ steps:
$a_n = 2^n a_0 + 3(2^{n-1} + 2^{n-2} + ... + 2^1 + 2^0)$
The term in parentheses is a geometric series.
$a_n = 2^n \cdot 1 + 3 \left( \frac{2^n - 1}{2 - 1} \right)$
**Final Answer:**
$$a_n = 2^n + 3(2^n - 1) = 4 \cdot 2^n - 3 = 2^{n+2} - 3$$

Verify for $n=2$: $a_2 = 2^{4} - 3 = 16 - 3 = 13$. Using the original recurrence: $a_1 = 2(1)+3=5$; $a_2=2(5)+3=13$. It checks out.

### 4. Key Points & Summary

| Aspect | Description |
| :--- | :--- |
| **Definition** | A relation of the form $a_n = c \cdot a_{n-1} + f(n)$ with initial condition $a_0 = d$. |
| **Order** | **First Order** because $a_n$ depends only on the **first** previous term, $a_{n-1}$. |
| **Linearity** | **Linear** because the terms ($a_n$, $a_{n-1}$) appear to the first power and are not multiplied together. |
| **Solution Method** | The **Iteration (Telescoping) Method** is powerful and straightforward for first order relations. |
| **Homogeneous Solution** | The solution when $f(n)=0$ is always $a_n = a_0 \cdot c^n$. |
| **Application** | Crucial for calculating the time complexity of algorithms (e.g., `T(n) = T(n-1) + n`). |

**Summary:** A first order linear recurrence relation provides a recursive definition of a sequence. Solving it means finding a direct, closed-form formula. The iterative method involves unwinding the recurrence until a pattern emerges, which is then expressed using geometric series summations. Mastering this topic is essential for analyzing the efficiency of recursive processes in engineering applications.