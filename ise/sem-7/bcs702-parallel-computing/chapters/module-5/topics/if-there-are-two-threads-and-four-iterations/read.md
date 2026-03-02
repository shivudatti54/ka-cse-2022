# **Parallel Computing**

## **Module: 21102024**

## **Topic: If there are two threads and four iterations**

## **Introduction**

Parallel computing is a technique where multiple computations are performed simultaneously, improving the overall speed and efficiency of a program. In this topic, we will explore the concept of multiple threads and iterations in parallel computing.

## **Threads**

A thread is a separate flow of execution within a program. Each thread has its own program counter, stack, and local variables. Threads can share data with each other, but each thread has its own memory space.

## **Iterations**

An iteration refers to the number of times a loop is executed. In parallel computing, iterations are executed simultaneously by multiple threads.

## **Problem Statement**

Let's consider a problem where we have two threads and four iterations. We need to calculate the sum of two arrays using parallel computing.

## **Example**

Suppose we have two threads, T1 and T2, and two arrays, A and B, each with four elements. We need to calculate the sum of corresponding elements in A and B.

| Element in A | Element in B |
| ------------ | ------------ |
| 1            | 2            |
| 2            | 3            |
| 3            | 4            |
| 4            | 5            |

Thread T1 will iterate over the first two elements of array A and calculate the sum with the corresponding elements in array B.

| Iteration | Element in A | Element in B | Sum |
| --------- | ------------ | ------------ | --- |
| 1         | 1            | 2            | 3   |
| 2         | 2            | 3            | 5   |

Thread T2 will iterate over the last two elements of array A and calculate the sum with the corresponding elements in array B.

| Iteration | Element in A | Element in B | Sum |
| --------- | ------------ | ------------ | --- |
| 3         | 3            | 4            | 7   |
| 4         | 4            | 5            | 9   |

## **Solution**

To solve this problem, we can use the following steps:

1. Create two threads, T1 and T2.
2. Initialize two arrays, A and B, with four elements each.
3. Use a loop to iterate over the elements of array A and calculate the sum with the corresponding elements in array B.
4. In each iteration, assign the sum to a shared variable, sum.
5. After all iterations, return the final sum.

## **Code**

```c
#include <stdio.h>
#include <pthread.h>

#define NUM_ITERATIONS 4

// Shared variable to store the sum
int sum = 0;

// Function for thread T1
void* threadT1(void* arg) {
    int i;
    for (i = 0; i < NUM_ITERATIONS / 2; i++) {
        sum += arg[(i * 2) + 1] + arg[(i * 2) + 2];
    }
    return NULL;
}

// Function for thread T2
void* threadT2(void* arg) {
    int i;
    for (i = NUM_ITERATIONS / 2; i < NUM_ITERATIONS; i++) {
        sum += arg[(i * 2) + 1] + arg[(i * 2) + 2];
    }
    return NULL;
}

int main() {
    int arrA[] = {1, 2, 3, 4};
    int arrB[] = {2, 3, 4, 5};

    pthread_t threadT1, threadT2;
    pthread_create(&threadT1, NULL, threadT1, arrA);
    pthread_create(&threadT2, NULL, threadT2, arrB);

    pthread_join(threadT1, NULL);
    pthread_join(threadT2, NULL);

    printf("Sum: %d\n", sum);

    return 0;
}
```

## **Key Concepts**

- Multiple threads can execute simultaneously to improve the speed and efficiency of a program.
- Iterations can be executed simultaneously by multiple threads to improve the speed and efficiency of a program.
- Shared variables can be used to store results calculated by multiple threads.
- Threads can share data with each other, but each thread has its own memory space.

## **Best Practices**

- Use multiple threads to execute computationally intensive tasks to improve the speed and efficiency of a program.
- Use shared variables to store results calculated by multiple threads.
- Use synchronization mechanisms to ensure that threads access shared variables safely and efficiently.

By following these best practices and using parallel computing techniques, you can improve the speed and efficiency of your programs and solve complex computational problems efficiently.
