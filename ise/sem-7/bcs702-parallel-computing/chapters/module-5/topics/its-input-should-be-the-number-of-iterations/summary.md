# **Revision Notes: "Its input should be the number of iterations"**

**Definition:**

- The input to a parallel computing algorithm should be the number of iterations, not the size of the input data.

**Key Points:**

- **Data-parallel vs task-parallel computing:**
  - Data-parallel computing: Divide data into smaller chunks and process each chunk in parallel.
  - Task-parallel computing: Divide the algorithm into smaller tasks and process each task in parallel.
- **Why iterations matter:**
  - Number of iterations determines the number of tasks to be executed in parallel.
  - Increasing iterations can lead to improved parallelization, but also increases computational complexity.
- **Important Formulas:**
  - Number of tasks = Number of processors x Number of iterations
  - Computational complexity = O(n x p x c), where n is input size, p is number of processors, and c is number of iterations.

**Theorems:**

- **Master-Theorem:**
  - Gives a way to solve recurrence relations for algorithms with a small number of recursive calls.
  - Can be used to analyze the time complexity of parallel algorithms.

**Key Concepts:**

- **Synchronization:**
  - Coordinating the execution of tasks to ensure correct results.
- **Communication:**
  - Exchanging data between processors to achieve a common goal.
- **Load balancing:**
  - Distributing tasks evenly among processors to minimize idle time.

**Important Terms:**

- **Parallelism:**
  - The ability to execute multiple tasks simultaneously.
- **Concurrent execution:**
  - The ability to execute multiple tasks at the same time.
- **Data locality:**
  - The tendency of data to be stored in nearby memory locations.
