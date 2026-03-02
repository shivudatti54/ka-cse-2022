# Parallel Computing Revision Notes

### Topic: If there are two threads and four iterations

**Definitions and Theorems**

- **Thread**: A separate flow of execution in a parallel program.
- **Iteration**: A single execution of a loop or a set of instructions.
- **Parallelism**: The ability to execute multiple threads simultaneously.

**Key Points**

- **Sequential Execution**: If two threads are executed sequentially, the total execution time is 8 iterations (2 threads x 4 iterations).
- **Parallel Execution**: If the two threads are executed in parallel, the total execution time is 4 iterations (2 threads x 2 iterations).
- **Ideal Parallelism**: The maximum theoretical parallelism that can be achieved, assuming all threads can execute in parallel.
- **Amdahl's Law**: A theorem that describes the maximum theoretical speedup that can be achieved in a parallel program.
- Formula: S = 1 / (1/p + (1 - p)), where S is the speedup and p is the fraction of the program that can be parallelized.

**Important Formulas**

- **Execution Time**: T = n \* t, where T is the total execution time, n is the number of threads, and t is the execution time of a single thread.
- **Speedup**: S = T / T', where T is the sequential execution time and T' is the parallel execution time.

**Key Concepts**

- **Thread Synchronization**: The ability of threads to coordinate their execution and access shared resources.
- **Locking Mechanisms**: Techniques used to synchronize threads and prevent data corruption.

### Quick Revision Tips

- Understand the definitions and theorems related to parallel computing.
- Practice calculating execution times and speedup using the formulas.
- Review key concepts, such as thread synchronization and locking mechanisms.
- Use Amdahl's Law to estimate the maximum theoretical speedup that can be achieved.
