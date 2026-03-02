# PARALLEL COMPUTING

Module: 21102024
Topic: And its output should be which iterations of a parallelized for loop are executed by which thread
=====================================================

## Table of Contents

1. [Introduction](#introduction)
2. [Historical Context](#historical-context)
3. [Parallel Computing Basics](#parallel-computing-basics)
4. [Parallelization of For Loops](#parallelization-of-for-loops)
5. [Thread Scheduling and Execution](#thread-scheduling-and-execution)
6. [Example: Parallelizing a Simple For Loop](#example-parallelizing-a-simple-for-loop)
7. [Example: Parallelizing a Matrix Multiplication](#example-parallelizing-a-matrix-multiplication)
8. [Case Study: Parallelizing a Scientific Simulation](#case-study-parallelizing-a-scientific-simulation)
9. [Modern Developments](#modern-developments)
10. [Conclusion](#conclusion)
11. [Further Reading](#further-reading)

## Introduction

Parallel computing is a technique used to speed up computational tasks by dividing them into smaller sub-tasks and executing them concurrently across multiple processing units. This approach can significantly improve the performance of certain applications, such as scientific simulations, data processing, and machine learning.

In this topic, we will explore the concept of parallelizing for loops and how threads are scheduled and executed to achieve parallelism. We will also examine examples, case studies, and modern developments in parallel computing.

## Historical Context

The concept of parallel computing dates back to the 1960s, when the first supercomputers were developed. These early systems used multiple processing units to execute tasks in parallel, but they were limited by the lack of interconnectivity and communication between the units.

In the 1980s, the introduction of the Message Passing Interface (MPI) standard enabled developers to write programs that could run on multiple processors, but still communicate with each other through a message-passing protocol.

Modern parallel computing relies on the widespread adoption of multi-core processors, which have significantly increased the number of processing units available for parallel execution.

## Parallel Computing Basics

In parallel computing, tasks are divided into smaller sub-tasks, called threads, which are executed concurrently across multiple processing units. Threads are lightweight processes that share the same memory space as the parent process.

To achieve parallelism, threads must be scheduled and executed efficiently. The scheduling algorithm determines which threads to execute next, based on factors such as thread priority, workload, and communication requirements.

## Parallelization of For Loops

For loops are a common construct in programming languages, used to iterate over a sequence of values. To parallelize a for loop, we can divide the iterations into smaller sub-tasks, called threads, which execute concurrently.

Here is a simple example of parallelizing a for loop using threads:

```c
#include <pthread.h>
#include <stdio.h>

void* parallel_for_loop(void* arg) {
    int i;
    for (i = 0; i < 10; i++) {
        printf("%d\n", i);
    }
    return NULL;
}

int main() {
    pthread_t threads[5];
    for (int i = 0; i < 5; i++) {
        pthread_create(&threads[i], NULL, parallel_for_loop, NULL);
    }
    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
```

In this example, we create five threads that execute the parallel_for_loop function concurrently. Each thread prints a sequence of values from 0 to 9.

## Thread Scheduling and Execution

To determine which iterations of a parallelized for loop are executed by which thread, we need to schedule and execute the threads efficiently.

Here are some common scheduling algorithms used in parallel computing:

- **Round-Robin Scheduling**: Each thread is executed for a fixed time period, before being replaced by the next thread in the queue.
- **Priority Scheduling**: Threads with higher priority are executed first, based on factors such as thread priority, workload, and communication requirements.
- **Dynamic Scheduling**: The scheduling algorithm adapts to changing workloads and priorities in real-time.

To visualize the thread scheduling and execution, let's consider a simple example:

```c
#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

void* parallel_for_loop(void* arg) {
    int i;
    for (i = 0; i < 10; i++) {
        printf("Thread %d: %d\n", pthread_self(), i);
        usleep(100000); // simulate work
    }
    return NULL;
}

int main() {
    pthread_t threads[5];
    for (int i = 0; i < 5; i++) {
        pthread_create(&threads[i], NULL, parallel_for_loop, NULL);
    }
    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
```

In this example, we use the `pthread_self` function to get the thread ID, which is then printed along with the iteration number. The `usleep` function simulates work by pausing the thread for a fixed time period.

The output of this program will show the thread ID and iteration number for each thread, illustrating the execution order and parallelism achieved through thread scheduling and execution.

## Example: Parallelizing a Simple For Loop

Let's consider a simple example of parallelizing a for loop using threads:

```c
#include <pthread.h>
#include <stdio.h>

void* parallel_for_loop(void* arg) {
    int i;
    for (i = 0; i < 10; i++) {
        printf("%d\n", i);
    }
    return NULL;
}

int main() {
    pthread_t threads[5];
    for (int i = 0; i < 5; i++) {
        pthread_create(&threads[i], NULL, parallel_for_loop, NULL);
    }
    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
```

In this example, we create five threads that execute the parallel_for_loop function concurrently.

## Example: Parallelizing a Matrix Multiplication

Let's consider a simple example of parallelizing a matrix multiplication using threads:

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void* parallel_matrix_multiplication(void* arg) {
    int A[2][2];
    int B[2][2];
    int C[2][2];

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return NULL;
}

int main() {
    pthread_t threads[4];
    for (int i = 0; i < 4; i++) {
        pthread_create(&threads[i], NULL, parallel_matrix_multiplication, NULL);
    }
    for (int i = 0; i < 4; i++) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
```

In this example, we create four threads that execute the parallel_matrix_multiplication function concurrently, which multiplies two matrices.

## Case Study: Parallelizing a Scientific Simulation

Let's consider a simple example of parallelizing a scientific simulation using threads:

```c
#include <pthread.h>
#include <stdio.h>

void* parallel_simulation(void* arg) {
    int t = 0;
    while (t < 10) {
        t++;
        printf("Time: %d\n", t);
        usleep(100000); // simulate work
    }
    return NULL;
}

int main() {
    pthread_t threads[5];
    for (int i = 0; i < 5; i++) {
        pthread_create(&threads[i], NULL, parallel_simulation, NULL);
    }
    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
```

In this example, we create five threads that execute the parallel_simulation function concurrently, which simulates a time-dependent process.

## Modern Developments

Modern parallel computing relies on the widespread adoption of multi-core processors, which have significantly increased the number of processing units available for parallel execution.

Some recent developments in parallel computing include:

- **GPU Computing**: General-purpose computing on graphics processing units (GPUs) has become a popular approach for parallel computing, particularly for applications such as scientific simulations and machine learning.
- **Distributed Computing**: Distributed computing involves dividing tasks across multiple machines or nodes, which can be connected through a network. This approach is often used for large-scale simulations and data processing.
- **Hybrid Parallelism**: Hybrid parallelism combines different parallel computing techniques, such as thread-level parallelism and data parallelism, to achieve improved performance and efficiency.

## Conclusion

Parallel computing is a powerful technique used to speed up computational tasks by dividing them into smaller sub-tasks and executing them concurrently across multiple processing units.

By understanding the concept of parallelizing for loops and how threads are scheduled and executed, we can achieve parallelism in a wide range of applications, from scientific simulations to data processing.

## Further Reading

- "Parallel Computing" by R. S. Schreiber and J. P. Kurose (McGraw-Hill, 2001)
- "The Practice of Parallel Programming" by K. A. Gaonkar, S. S. Iyer, and M. M. Perez (Springer, 2003)
- "Parallel Computing: Principles and Applications" by S. K. Das and S. K. Ghosh (McGraw-Hill, 2003)
- "GPU Computing: A Gentle Introduction" by J. M. Carmona, J. M. Garcia, and A. Pascual (Springer, 2012)
- "Distributed Computing: A Gentle Introduction" by S. K. Das and S. K. Ghosh (McGraw-Hill, 2013)
