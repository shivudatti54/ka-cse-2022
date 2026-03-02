**Summary: Thread 1 - Iterations 2-3**

- **Fibonacci Sequence**: A series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1 (F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)).
- **Memoization**: A technique to store previously computed Fibonacci numbers to avoid redundant calculations.
- **OpenMP**: A parallel programming model that allows developers to write programs that can execute multiple threads or processes simultaneously.

**Important Formulas and Definitions:**

- Fibonacci recurrence relation: F(n) = F(n-1) + F(n-2)
- Binet's formula: F(n) = (φ^n - (1-φ)^n) / √5, where φ is the golden ratio (approximately 1.618)

**Theorems:**

- **Binet's Identity**: F(n) = (φ^n - (1-φ)^n) / √5
- **Matrix Exponentiation**: F(n) can be computed using matrix exponentiation, which reduces the time complexity from O(2^n) to O(n log n).

**Key Points for Revision:**

- OpenMP program to calculate n Fibonacci numbers using tasks:
  - Create a task to calculate the nth Fibonacci number
  - Use a work-sharing construct (e.g., parallel for) to distribute tasks among threads
  - Use a reduction construct (e.g., reduce) to combine the results from each task
- Benefits of using tasks:
  - Improved parallelism
  - Reduced overhead of thread creation and synchronization
  - Easier to write and manage parallel code
