# Parallel Computing

### Introduction

Parallel computing is a technique that uses multiple processing units to perform computations in parallel, improving processing speed and efficiency.

### Key Concepts

- **Parallelized For Loop**: A for loop that is divided among multiple threads to perform computations in parallel.
- **Thread**: A separate flow of execution within a process, each with its own program counter, stack, and local variables.
- **Synchronization**: Coordinating the execution of multiple threads to ensure correct and efficient results.

### Scheduling of Parallelized For Loop Iterations

- **Critical Section**: A section of code that is shared among multiple threads and requires synchronization to prevent data corruption.
- **Lock**: A mechanism to ensure exclusive access to a critical section.
- **Barriers**: A synchronization point where threads wait until all threads have reached a certain point.

### Important Formulas and Definitions

- **Amdahl's Law**: A bound on the maximum speedup that can be achieved by parallel processing, taking into account the fraction of the program that cannot be parallelized.
- **Goto Parallelism**: A technique that uses conditional statements to determine which iterations of a parallelized for loop to execute.

### Theorems

- **Total Parallelism Theorem**: A theorem that states that the maximum parallelism that can be achieved is limited by the fraction of the program that cannot be parallelized.
- **Conservative Parallelism Theorem**: A theorem that states that the actual parallelism achieved will be less than the maximum possible parallelism due to synchronization overhead.

### Revision Notes

- Understand the importance of synchronization in parallel computing.
- Know how to divide a parallelized for loop among multiple threads.
- Understand the limitations of parallelism imposed by Amdahl's Law and the Total Parallelism Theorem.
- Be aware of the need to use locks and barriers to ensure correct results.
- Familiarize yourself with Goto Parallelism and its limitations.
