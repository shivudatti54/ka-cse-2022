# **Parallel Computing**

## **Module: 21102024**

## **Topic: Thread 1 : Iterations 2 −− 3 3 Write a OpenMP program to calculate n Fibonacci numbers using tasks**

## **Table of Contents**

1. [Definition and Overview](#definition-and-overview)
2. [OpenMP and Tasks](#openmp-and-tasks)
3. [Fibonacci Sequence](#fibonacci-sequence)
4. [OpenMP Program to Calculate n Fibonacci Numbers Using Tasks](#openmp-program-to-calculate-n-fibonacci-numbers-using-tasks)
5. [Example Use Case](#example-use-case)

## **Definition and Overview**

Parallel computing is a technique that uses multiple processing units to solve a problem by dividing the workload into smaller sub-problems and distributing them among the processors. OpenMP (Open Multi-Processing) is a set of APIs and programming models that allow developers to easily write parallel programs for a variety of architectures.

## **OpenMP and Tasks**

OpenMP provides several parallelization constructs, including:

- **Parallel regions**: Allow developers to specify a block of code that is executed in parallel.
- **Parallel loops**: Allow developers to specify a loop that is executed in parallel.
- **Tasks**: Allow developers to specify a block of code that is executed asynchronously.

## **Fibonacci Sequence**

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers, usually starting with 0 and 1. The sequence is often used to model population growth, finance, and other real-world phenomena.

## **OpenMP Program to Calculate n Fibonacci Numbers Using Tasks**

The following program uses OpenMP tasks to calculate the first `n` Fibonacci numbers.

```c
#include <stdio.h>
#include <omp.h>

// Function to calculate the Fibonacci sequence using recursive function calls
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Function to calculate the Fibonacci sequence using tasks
void fibonacciTask(int n, int numTasks, int start, int end) {
    if (start == end - 1) {
        printf("%d ", fibonacci(start));
    } else {
        // Divide the work among tasks
        int mid = (start + end) / 2;
        fibonacciTask(n, numTasks, start, mid);
        fibonacciTask(n, numTasks, mid, end);
    }
}

int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);

    // Create a task group
    #pragma omp parallel for num_threads(4) // Create 4 threads
    for (int i = 1; i <= n; i++) {
        // Create a task for each iteration
        int numTasks = n / 4;
        int start = (i - 1) * numTasks + 1;
        int end = start + numTasks;
        if (i == n) {
            end = n;
        }
        fibonacciTask(n, numTasks, start, end);
    }

    return 0;
}
```

## **Example Use Case**

To run the program, save it to a file named `fibonacci_tasks.c` and compile it using the following command:

```bash
gcc -o fibonacci_tasks fibonacci_tasks.c -fopenmp
```

Then, run the program and enter a value for `n` when prompted:

```bash
./fibonacci_tasks
```

The program will output the first `n` Fibonacci numbers.

## **Key Concepts**

- **Parallel computing**: A technique that uses multiple processing units to solve a problem by dividing the workload into smaller sub-problems and distributing them among the processors.
- **OpenMP**: A set of APIs and programming models that allow developers to easily write parallel programs for a variety of architectures.
- **Tasks**: A parallelization construct in OpenMP that allows developers to specify a block of code that is executed asynchronously.
- **Fibonacci sequence**: A series of numbers in which each number is the sum of the two preceding numbers, usually starting with 0 and 1.
