# Multithreading Models - Summary

## Key Definitions and Concepts

- **Thread**: The smallest unit of CPU execution within a process, consisting of thread ID, program counter, register set, and stack, while sharing code and data sections with other threads in the same process
- **User-Level Threads**: Threads managed entirely by a thread library in user space without kernel involvement
- **Kernel-Level Threads**: Threads managed directly by the operating system kernel, which can schedule them on multiple processors
- **Multithreading Model**: The architectural pattern defining the relationship between user-level threads and kernel-level threads

## Important Formulas and Theorems

- Thread creation overhead: One-to-One requires kernel thread creation for each user thread, while Many-to-One creates threads entirely in user space
- Kernel thread stack memory: Typically 8KB-16KB per kernel thread, limiting the practical number of threads in One-to-One model
- Concurrency factor: Maximum parallel execution equals minimum of (number of CPU cores, number of kernel threads) in any model

## Key Points

- Many-to-One: Multiple user threads to single kernel thread; efficient but cannot utilize multiple processors; one blocking call blocks all threads
- One-to-One: One-to-one mapping between user and kernel threads; enables true parallelism; creation overhead limits thread count
- Many-to-Many: Multiplexes M user threads to N kernel threads; provides flexibility and true concurrency; best theoretical model
- Two-Level: Extension of Many-to-Many allowing direct binding of specific user threads to kernel threads for priority handling
- Modern operating systems primarily use One-to-One model through POSIX threads
- Thread pooling mitigates One-to-One creation overhead by reusing threads

## Common Mistakes to Avoid

- Confusing user-level threads with kernel-level threads; remember they operate at different privilege levels
- Thinking that creating more user threads in Many-to-One model automatically provides more parallelism
- Forgetting that blocking system calls in Many-to-One block all user threads in the process
- Underestimating thread creation overhead in One-to-One model for applications with many threads

## Revision Tips

- Draw diagrams showing the relationship between user threads and kernel threads for each model
- Memorize the key limitation of Each model: Many-to-One cannot use multiple CPUs; One-to-One limited by thread creation cost
- Focus on understanding why modern systems prefer One-to-One despite its limitations
- Practice comparing models using criteria: parallelism capability, thread creation overhead, portability, and blocking behavior