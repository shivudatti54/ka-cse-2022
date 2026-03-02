# Record Both Serial and Parallel Execution Times

## **What is Parallel Computing?**

Parallel computing is the practice of using multiple processing units to solve a problem by dividing the work among them. This approach can significantly speed up the execution time of a program compared to running it on a single processor.

## **Serial Execution Time**

Serial execution time refers to the time it takes for a program to run on a single processor. It is the time it takes for the program to execute one instruction after another, without any overlap or simultaneous execution of other instructions.

## **Parallel Execution Time**

Parallel execution time, on the other hand, refers to the time it takes for a program to run on multiple processors. It is the time it takes for multiple processors to execute different instructions simultaneously, resulting in faster execution time.

## **Recording Parallel Execution Times**

Recording parallel execution times involves measuring the time it takes for a program to run on multiple processors. This can be done using various methods, including:

- **Profiling tools**: Profiling tools, such as gprof or Intel VTune Amplifier, can be used to measure the execution time of a program on multiple processors.
- **Benchmarking tools**: Benchmarking tools, such as OpenMP or MPICH, can be used to measure the execution time of a program on multiple processors.
- **Manual timing**: Manual timing can be used to measure the execution time of a program on multiple processors by using a stopwatch or a timing library.

## **Key Concepts**

- **Synchronization**: Synchronization is the process of coordinating the execution of multiple processors to ensure that they execute instructions in the correct order.
- **Barriers**: Barriers are synchronization points that allow processors to wait for each other to finish executing instructions before proceeding.
- **Load balancing**: Load balancing is the process of dividing the workload among multiple processors to ensure that each processor has an equal amount of work to do.

## **Example: Measuring Parallel Execution Time using OpenMP**

Here is an example of how to measure parallel execution time using OpenMP:

```c
#include <omp.h>

void parallel_execution_time() {
    int num_threads = omp_get_max_threads();
    double serial_time = 0.0;
    double parallel_time = 0.0;

    // Create a serial execution time
    for (int i = 0; i < 1000000; i++) {
        serial_time += 1.0;
    }

    // Create a parallel execution time using OpenMP
    #pragma omp parallel for reduction(+:parallel_time)
    for (int i = 0; i < 1000000; i++) {
        parallel_time += 1.0;
    }

    printf("Serial execution time: %f seconds\n", serial_time);
    printf("Parallel execution time: %f seconds\n", parallel_time);
}

int main() {
    parallel_execution_time();
    return 0;
}
```

In this example, the `parallel_execution_time` function measures the serial execution time by executing a loop 1,000,000 times. It then measures the parallel execution time by executing the same loop using OpenMP, which creates multiple threads to execute the loop.

## **Best Practices**

- **Use profiling tools**: Profiling tools can help identify performance bottlenecks in a program and guide optimization efforts.
- **Use benchmarking tools**: Benchmarking tools can help measure the execution time of a program on multiple processors.
- **Optimize for load balancing**: Optimizing for load balancing can help ensure that each processor has an equal amount of work to do.

By following these best practices and using the right tools, developers can effectively record both serial and parallel execution times to optimize the performance of their parallel programs.
