# **Record both serial and parallel execution times**

### Key Points

- **Serial Execution Time**: The time taken to complete a task sequentially, without parallel processing.
- **Parallel Execution Time**: The time taken to complete a task using multiple processing units or cores simultaneously.
- **Speedup**: The ratio of parallel execution time to serial execution time, often denoted by `S = T_parallel / T_serial`.
- **Weak Scaling**: Increasing the number of processing units while reducing the amount of work per unit, resulting in a constant speedup.
- **Strong Scaling**: Increasing the number of processing units while increasing the amount of work per unit, resulting in a linear speedup.
- **Amdahl's Law**: The maximum theoretical speedup of a parallel algorithm, considering the fraction of the program that cannot be parallelized.
  - `S_max = 1 / (1 - P + P / N)`
  - where `P` is the fraction of the program parallelized and `N` is the number of processing units.

### Important Formulas and Definitions

- **Time Complexity**: A measure of the amount of time an algorithm takes to complete, often expressed in Big O notation (e.g., O(n) or O(n^2)).
- **Cache Hierarchy**: A system of caches that store frequently accessed data, reducing memory access latency.
- **Pipelining**: Breaking down a computation into stages, allowing for parallel processing and reducing overall execution time.

### Theorems

- **Gould's Law**: The minimum time required to perform a task on a parallel computer is proportional to the logarithm of the number of processing units.
  - `T_min = O(log N)`
- **Massey's Law**: The time taken to perform a task on a parallel computer is proportional to the logarithm of the number of processing units, with a constant factor.
  - `T = C * log N + O(1)`
