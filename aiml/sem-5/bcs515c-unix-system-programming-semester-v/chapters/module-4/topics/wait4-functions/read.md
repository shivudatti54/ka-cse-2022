# Distributed Memory Programming with MPI: Functions and Basics

## Introduction to MPI

The **Message Passing Interface (MPI)** is a standardized and portable message-passing standard designed to function on parallel computing architectures. It enables processes running on multiple computers (nodes) in a cluster to communicate with each other by passing messages. Unlike shared memory models (like OpenMP), MPI is designed for distributed memory systems, where each processor has its own private memory.

MPI is not a programming language but a library specification with bindings for Fortran, C, C++, and other languages. Its primary goals are:
*   **Portability:** MPI programs can run on any system that implements the standard.
*   **Performance:** Vendor implementations are highly optimized for their specific hardware.
*   **Functionality:** It provides a rich set of routines for various communication patterns.

## Core MPI Concepts

### 1. Communicators and Groups
An MPI **communicator** defines a communication context and a group of processes. The most important communicator is `MPI_COMM_WORLD`, which includes all processes launched when the program starts. Processes within a communicator are ordered and assigned a unique **rank**, an integer identifier starting from 0.

```
Process View of MPI_COMM_WORLD (Size = 4)
+----------------+    +----------------+    +----------------+    +----------------+
|   Process 0    |    |   Process 1    |    |   Process 2    |    |   Process 3    |
|   Rank: 0      |    |   Rank: 1      |    |   Rank: 2      |    |   Rank: 3      |
|   Local Memory |    |   Local Memory |    |   Local Memory |    |   Local Memory |
+----------------+    +----------------+    +----------------+    +----------------+
```

### 2. Point-to-Point Communication
This involves communication between two specific processes: a sender and a receiver.

**Key Functions:**
*   `MPI_Send(void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm)`
    *   `buf`: Pointer to the data to send.
    *   `count`: Number of elements to send.
    *   `datatype`: MPI data type (e.g., `MPI_INT`, `MPI_FLOAT`).
    *   `dest`: Rank of the destination process.
    *   `tag`: Message tag (integer) to distinguish message types.
    *   `comm`: Communicator.

*   `MPI_Recv(void *buf, int count, MPI_Datatype datatype, int source, int tag, MPI_Comm comm, MPI_Status *status)`
    *   `source`: Rank of the source process (`MPI_ANY_SOURCE` wildcard).
    *   `status`: Object containing information about the received message (e.g., actual source, tag).

**Blocking vs. Non-blocking:**
The standard `MPI_Send` and `MPI_Recv` are **blocking**. This means `MPI_Send` may not return until the message buffer is safe to be reused (though the message may not have been received yet). `MPI_Recv` blocks until the matching message is received. MPI also provides non-blocking versions (`MPI_Isend`, `MPI_Irecv`) which return immediately, allowing computation and communication to overlap.

**Example: Sending an Integer**
```c
// Process 1
int number = 42;
MPI_Send(&number, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);

// Process 0
int received_number;
MPI_Status status;
MPI_Recv(&received_number, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, &status);
// received_number is now 42
```

### 3. Collective Communication
Collective operations involve all processes within a communicator. They are often more optimized and easier to use than implementing the same logic with multiple point-to-point calls.

**Common Collective Operations:**

| Function | Purpose | Description |
| :--- | :--- | :--- |
| `MPI_Bcast` | Broadcast | One process (the root) sends the same data to all others. |
| `MPI_Scatter` | Scatter | The root process sends distinct chunks of an array to all processes. |
| `MPI_Gather` | Gather | The root process collects distinct chunks from all processes into an array. |
| `MPI_Reduce` | Reduction | Performs a global operation (e.g., sum, max, min) on data from all processes and stores the result on the root. |
| `MPI_Allreduce` | All-Reduction | Like `MPI_Reduce`, but the result is distributed to all processes. |
| `MPI_Barrier` | Synchronization | Blocks until all processes in the communicator have reached this call. |

**Diagram of Collective Operations:**
```
Bcast: Root sends same data to all
    Root (P0)
      | \
      |  \
      |   \
     P1   P2   P3   ...   Pn

Scatter: Root sends chunks of an array
    Root [a,b,c,d]
      |   |  |  |
      a   b  c  d
     P0  P1 P2 P3   (P0 also gets a chunk)

Gather: Inverse of Scatter
    P0  P1 P2 P3
     a   b  c  d
      \   \  \  \
       \   \  \  \
        [a,b,c,d] Root

Reduce: Global operation (e.g., SUM)
    P0:5  P1:3  P2:7  P3:1
        \   |   /   /
         \  |  /   /
          SUM=16 -> Root
```

**Example: Global Sum with MPI_Reduce**
```c
int my_value = ...; // Each process computes its local value
int global_sum;

// Sum all my_value from all processes, store result in global_sum on process 0
MPI_Reduce(&my_value, &global_sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
```

### 4. MPI Derived Datatypes
Basic datatypes (`MPI_INT`, `MPI_CHAR`, etc.) are often insufficient for sending complex data structures like structs or non-contiguous memory blocks (e.g., a column of a matrix). **Derived datatypes** allow you to create custom data layouts for communication.

**Common Functions:**
*   `MPI_Type_contiguous(int count, MPI_Datatype oldtype, MPI_Datatype *newtype)`: Creates a type representing `count` contiguous elements.
*   `MPI_Type_vector(int count, int blocklength, int stride, MPI_Datatype oldtype, MPI_Datatype *newtype)`: Creates a type for regularly spaced blocks (e.g., a row of a matrix with padding).
*   `MPI_Type_create_struct(int count, int array_of_blocklengths[], MPI_Aint array_of_displacements[], MPI_Datatype array_of_types[], MPI_Datatype *newtype)`: Creates a type from arbitrary data elements (e.g., a C struct).

**Process:**
1.  Create the new datatype.
2.  Commit it with `MPI_Type_commit(MPI_Datatype *datatype)` to make it ready for use.
3.  Use it in communication calls.
4.  Free it with `MPI_Type_free(MPI_Datatype *datatype)` when done.

## A Complete Example: Trapezoidal Rule in MPI

This is a classic example of data parallelism using MPI. The goal is to approximate the integral of a function `f(x)` from `a` to `b` using the trapezoidal rule by dividing the work among processes.

**Algorithm:**
1.  **Initialization:** Each process gets its rank and the total number of processes (`comm_sz`).
2.  **Data Distribution:** Process 0 (the root) reads the integration limits (`a`, `b`) and the number of trapezoids (`n`). It then broadcasts `a`, `b`, and `n` to all other processes.
3.  **Local Calculation:** Each process calculates the width `h = (b-a)/n`. Each process determines its specific segment of the integration range.
    *   `local_n = n / comm_sz` (number of trapezoids per process)
    *   `local_a = a + my_rank * local_n * h`
    *   `local_b = local_a + local_n * h`
    *   Each process calculates its local integral `local_int` over `[local_a, local_b]`.
4.  **Result Aggregation:** All processes use `MPI_Reduce` with the `MPI_SUM` operation to sum their `local_int` into a `total_int` on process 0.
5.  **Output:** Process 0 prints the result.

```c
#include <stdio.h>
#include <mpi.h>

double f(double x) { return x*x; } // Function to integrate

double Trap(double left_end, double right_end, int trap_count, double h) {
    double estimate, x;
    int i;
    estimate = (f(left_end) + f(right_end)) / 2.0;
    for (i = 1; i < trap_count; i++) {
        x = left_end + i * h;
        estimate += f(x);
    }
    estimate = estimate * h;
    return estimate;
}

int main(void) {
    int my_rank, comm_sz, n = 1024, local_n;
    double a = 0.0, b = 3.0, h, local_a, local_b;
    double local_int, total_int;

    MPI_Init(NULL, NULL);
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &comm_sz);

    h = (b-a)/n;
    local_n = n / comm_sz;

    local_a = a + my_rank * local_n * h;
    local_b = local_a + local_n * h;
    local_int = Trap(local_a, local_b, local_n, h);

    // Sum all local integrals into total_int on process 0
    MPI_Reduce(&local_int, &total_int, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    if (my_rank == 0) {
        printf("With n = %d trapezoids, our estimate\n", n);
        printf("of the integral from %f to %f = %.15e\n", a, b, total_int);
    }

    MPI_Finalize();
    return 0;
}
```

## Performance Evaluation and Timing

Measuring the performance of an MPI program is crucial. The `MPI_Wtime()` function returns a floating-point number of seconds, representing elapsed wall-clock time since some arbitrary point in the past.

**How to Time a Section of Code:**
```c
double start_time, end_time;

start_time = MPI_Wtime(); // Start timer
// ... Code to be timed ...
end_time = MPI_Wtime();   // End timer

if (my_rank == 0) {
    printf("Elapsed time = %f seconds\n", end_time - start_time);
}
```
It's important to synchronize processes using `MPI_Barrier()` before timing to ensure all processes start the timed section at roughly the same time.

## Exam Tips

1.  **Know the Core Functions:** Be able to write the signatures and explain the parameters for `MPI_Send`, `MPI_Recv`, `MPI_Bcast`, `MPI_Reduce`, `MPI_Scatter`, and `MPI_Gather` without hesitation.
2.  **Understand Blocking Semantics:** Explain what it means for `MPI_Send` and `MPI_Recv` to be blocking. Be able to trace code and identify potential deadlocks caused by improper ordering of blocking calls.
3.  **Collective vs. Point-to-Point:** Know when to use a collective operation versus multiple point-to-point operations. Collective operations are almost always preferred for their simplicity and performance for global patterns.
4.  **Rank and Size:** Remember that the behavior of an MPI program almost always depends on `my_rank` and `comm_sz`. Process 0 often acts as the "master" or "root."
5.  **Trapezoidal Rule:** Be prepared to explain the steps of the parallel trapezoidal rule algorithm, including how the problem is decomposed and how the results are combined. You might be asked to write pseudocode for it.
6.  **Derived Datatypes:** Understand the *purpose* of derived datatypes (to handle non-contiguous data) and be familiar with the general process of creating, committing, using, and freeing them.
7.  **Timing:** Know how to use `MPI_Wtime()` correctly to measure parallel execution time.