# **Recurrence Relations: First Order Linear Recurrence Relation**

## **Key Definitions and Formulas**

- **Linear Recurrence Relation**: A recurrence relation of the form:
  - $a_n = a_{n-1} + c_1a_{n-2} + \ldots + c_{k-1}a_{n-k} + f(n)$
  - where $a_n$ is the $n^{th}$ term, $c_1, c_2, \ldots, c_{k-1}$ are constants, and $f(n)$ is a function of $n$
- **First Order Linear Recurrence Relation**: A recurrence relation of the form:
  - $a_n = a_{n-1} + c_1a_{n-2} + \ldots + c_1a_{n-k}$
- **Homogeneous Recurrence Relation**: A recurrence relation without the non-homogeneous term $f(n)$
- **Particular Solution**: A solution to the non-homogeneous recurrence relation
- **Homogeneous Solution**: A solution to the homogeneous recurrence relation
- **General Solution**: The sum of the homogeneous and particular solutions

## **Theorems**

- **Initial Value Theorem**: If $a_n$ is a solution to a recurrence relation with initial conditions $a_0, a_1, \ldots, a_{n-1}$, then
  - $a_n = a_{n-1} + c_1a_{n-2} + \ldots + c_1a_0 + \frac{1}{2!}\sum_{k=0}^{n-1} \frac{d^k}{dx^k} (a_k) + \ldots + \frac{1}{(n-1)!}\sum_{k=0}^{n-1} \frac{d^{n-1}}{dx^{n-1}} (a_k)$
- **Standard Form Theorem**: If $a_n$ is a solution to a homogeneous recurrence relation, then
  - $a_n = r^n$
  - where $r$ is the characteristic root

## **Important Concepts**

- **Characteristic Equation**: A polynomial equation obtained by substituting $a_n = r^n$ into the recurrence relation
- **Characteristic Roots**: The roots of the characteristic equation
- **Periodicity**: A sequence that repeats itself after a certain number of terms
