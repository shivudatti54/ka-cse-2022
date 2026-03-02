# **Recurrence Relations: First Order Linear Recurrence Relation**

### Definitions and Notations

- A **recurrence relation** is an equation that defines a sequence recursively.
- A **first-order linear recurrence relation** is of the form:
  - $a_n = r_1a_{n-1} + r_2a_{n-2} + \ldots + r_k a_{n-k} + f(n)$
  - where $a_n$ is the nth term of the sequence, $r_i$ are constants, and $f(n)$ is a non-negative integer.

### Important Formulas and Theorems

- **Master Theorem**: A fundamental result for solving recurrence relations. It states that the solution to a recurrence relation of the form $T(n) = aT(n/b) + f(n)$ is $T(n) = O(f(n) \log(n/b) + n^d)$, where $d$ is the degree of the polynomial in the recurrence relation.
- **Casework**: A technique for solving recurrence relations by considering different cases.

### Key Points

- **Solution methods**:
  - **Analytical solutions**: Finding an explicit formula for the sequence.
  - **Numerical solutions**: Approximating the sequence using numerical methods.
- **Properties of first-order linear recurrence relations**:
  - **Periodicity**: The sequence repeats after a certain number of terms.
  - **Convergence**: The sequence converges to a limit.
- **Examples**:
  - **Fibonacci sequence**: A classic example of a first-order linear recurrence relation.
  - **Exponential functions**: The solution to recurrence relations involving exponential functions.

### Important Theorems

- **Poincaré recurrence theorem**: States that for a sequence defined by a first-order linear recurrence relation, the sequence will eventually repeat with probability 1.
- **Birkhoff ergodic theorem**: Provides a condition for the recurrence relation to have a periodic solution.
