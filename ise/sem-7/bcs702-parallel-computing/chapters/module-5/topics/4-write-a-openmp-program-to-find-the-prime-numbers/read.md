# **Parallel Computing**

**Module:** 21102024
**Topic:** 4 Write a OpenMP program to find the prime numbers from 1 to n employing parallel for directive

## **Table of Contents**

1. [Introduction](#introduction)
2. [What are Prime Numbers](#what-are-prime-numbers)
3. [OpenMP and Parallel Computing](#openmp-and-parallel-computing)
4. [Example OpenMP Program](#example-openmp-program)
5. [Code](#code)

## **Introduction**

Parallel computing is a technique that allows us to solve problems by dividing them into smaller sub-problems and solving them simultaneously. OpenMP (Open Multi-Processing) is a library that allows us to write parallel programs in C, C++, and Fortran.

## **What are Prime Numbers**

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, and 7 are prime numbers.

## **OpenMP and Parallel Computing**

OpenMP provides a set of directives that allow us to specify which parts of the program should be executed in parallel. The `#pragma omp parallel for` directive is used to parallelize a loop.

## **Example OpenMP Program**

The following program finds the prime numbers from 1 to n using OpenMP.

```markdown
// PrimeNumbersOpenMP.c
#include <stdio.h>
#include <omp.h>

// Function to check if a number is prime
int isPrime(int num) {
if (num <= 1) {
return 0;
}
for (int i = 2; i \* i <= num; i++) {
if (num % i == 0) {
return 0;
}
}
return 1;
}

int main(int argc, char\*\* argv) {
int n;
if (argc != 2) {
printf("Usage: %s <n>\n", argv[0]);
return 1;
}
n = atoi(argv[1]);

    // Create a task array to store the number of iterations for each thread
    int taskSize = n / omp_get_max_threads();
    int* tasks = (int*)malloc(n * sizeof(int));

    // Initialize the task array
    for (int i = 0; i < n; i++) {
        tasks[i] = 1;
    }

    // Parallelize the loop
    #pragma omp parallel for
    for (int i = 0; i < n; i++) {
        // Assign task to the current thread
        int taskId = omp_get_thread_num() * taskSize;
        if (i >= taskId && i < taskId + taskSize) {
            tasks[i]++;
        }
    }

    // Count the number of prime numbers
    int primeCount = 0;
    for (int i = 0; i < n; i++) {
        if (isPrime(i) && tasks[i] == 1) {
            primeCount++;
        }
    }

    printf("Number of prime numbers from 1 to %d: %d\n", n, primeCount);

    free(tasks);
    return 0;

}
```

## **Code**

To compile the program, use the following command:

```bash
gcc PrimeNumbersOpenMP.c -fopenmp -o PrimeNumbersOpenMP
```

To run the program, use the following command:

```bash
./PrimeNumbersOpenMP <n>
```

Replace `<n>` with the desired number.

## **Key Concepts**

- OpenMP is a library that allows us to write parallel programs in C, C++, and Fortran.
- The `#pragma omp parallel for` directive is used to parallelize a loop.
- The task array is used to distribute the work among threads.
- The `omp_get_max_threads()` function returns the maximum number of threads that can be used.
- The `omp_get_thread_num()` function returns the number of the current thread.

## **Tips and Variations**

- Use `omp_set_num_threads()` to specify the number of threads to use.
- Use `omp_get_thread_num()` to get the number of the current thread.
- Use `omp_get_max_active_devices()` to get the maximum number of active devices.
- Use `omp_set_dynamic_device_assignment()` to dynamically assign devices to threads.
- Use `omp_set_num_threads()` to specify the number of threads to use.
