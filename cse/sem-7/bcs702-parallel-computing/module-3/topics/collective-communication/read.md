# Collective Communication in MPI

## Introduction to Collective Communication

In distributed memory programming using MPI (Message Passing Interface), communication between processes can be categorized into two types: point-to-point communication and collective communication. While point-to-point communication involves communication between exactly two processes (a sender and a receiver), collective communication involves coordinated communication among all processes in a communicator group.

**Collective communication** refers to operations where all processes in a communicator (typically `MPI_COMM_WORLD`) must participate. These operations are essential for coordinating work, distributing data, and gathering results across multiple processes in a parallel program.

### Key Characteristics of Collective Operations:

- All processes in the communicator must call the collective routine
- Collective calls are blocking - they don't return until the operation is complete
- They provide optimized implementations for common communication patterns
- They often lead to more readable and efficient code compared to multiple point-to-point calls

## Types of Collective Communication Operations

MPI collective operations can be categorized into several types based on their functionality:

### 1. Synchronization Operations

```c
MPI_Barrier(MPI_Comm communicator);
```

The barrier operation synchronizes all processes in the communicator. Each process blocks until all processes in the communicator have reached the barrier call.

```
Process 0: -------| Barrier |--------
Process 1: -------| Barrier |--------
Process 2: -------| Barrier |--------
Process 3: -------| Barrier |--------
 Time
```

### 2. Broadcast Operations

```c
MPI_Bcast(void* buffer, int count, MPI_Datatype datatype,
 int root, MPI_Comm communicator);
```

Broadcast sends data from one process (the root) to all other processes in the communicator.

```
Root Process (0): [Data] → → → →
 ↓
Process 1: [Data]
Process 2: [Data]
Process 3: [Data]
```

### 3. Gather Operations

```c
MPI_Gather(void* sendbuf, int sendcount, MPI_Datatype sendtype,
 void* recvbuf, int recvcount, MPI_Datatype recvtype,
 int root, MPI_Comm communicator);
```

Gather collects data from all processes and stores it at the root process.

```
Process 0: [Data0] →
Process 1: [Data1] → → Root Process: [Data0, Data1, Data2, Data3]
Process 2: [Data2] →
Process 3: [Data3] →
```

### 4. Scatter Operations

```c
MPI_Scatter(void* sendbuf, int sendcount, MPI_Datatype sendtype,
 void* recvbuf, int recvcount, MPI_Datatype recvtype,
 int root, MPI_Comm communicator);
```

Scatter distributes data from the root process to all other processes.

```
Root Process: [Data0, Data1, Data2, Data3] → → →
 ↓ ↓ ↓ ↓
Process 0: [Data0] [Data1] [Data2] [Data3]
Process 1: [Data0] [Data1] [Data2] [Data3]
Process 2: [Data0] [Data1] [Data2] [Data3]
Process 3: [Data0] [Data1] [Data2] [Data3]
```

### 5. Reduction Operations

```c
MPI_Reduce(void* sendbuf, void* recvbuf, int count,
 MPI_Datatype datatype, MPI_Op op, int root,
 MPI_Comm communicator);
```

Reduction operations combine data from all processes using a specified operation (sum, max, min, etc.) and store the result at the root process.

```
Process 0: [Value0] →
Process 1: [Value1] → → Root Process: [Value0 + Value1 + Value2 + Value3]
Process 2: [Value2] →
Process 3: [Value3] →
```

### 6. All-versus-All Operations

```c
MPI_Allgather(void* sendbuf, int sendcount, MPI_Datatype sendtype,
 void* recvbuf, int recvcount, MPI_Datatype recvtype,
 MPI_Comm communicator);

MPI_Allreduce(void* sendbuf, void* recvbuf, int count,
 MPI_Datatype datatype, MPI_Op op,
 MPI_Comm communicator);
```

These variants distribute results to all processes rather than just the root.

## Comparison of Collective Communication Operations

| Operation     | Purpose                        | Root Process | Other Processes | Result Location |
| ------------- | ------------------------------ | ------------ | --------------- | --------------- |
| MPI_Bcast     | Distribute data                | Sender       | Receiver        | All processes   |
| MPI_Scatter   | Distribute chunks of data      | Sender       | Receiver        | All processes   |
| MPI_Gather    | Collect data                   | Receiver     | Sender          | Root only       |
| MPI_Reduce    | Combine data with operation    | Receiver     | Sender          | Root only       |
| MPI_Allgather | Collect and distribute data    | Participant  | Participant     | All processes   |
| MPI_Allreduce | Combine and distribute results | Participant  | Participant     | All processes   |
| MPI_Barrier   | Synchronize                    | Participant  | Participant     | None            |

## Common MPI Reduction Operations

| Operation   | MPI Constant | Description               |
| ----------- | ------------ | ------------------------- |
| Sum         | MPI_SUM      | Sum of all values         |
| Product     | MPI_PROD     | Product of all values     |
| Maximum     | MPI_MAX      | Maximum value             |
| Minimum     | MPI_MIN      | Minimum value             |
| Logical AND | MPI_LAND     | Logical AND of all values |
| Logical OR  | MPI_LOR      | Logical OR of all values  |
| Bitwise AND | MPI_BAND     | Bitwise AND of all values |
| Bitwise OR  | MPI_BOR      | Bitwise OR of all values  |

## Implementation Examples

### Example 1: Calculating Global Sum

```c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
 MPI_Init(&argc, &argv);

 int world_rank, world_size;
 MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
 MPI_Comm_size(MPI_COMM_WORLD, &world_size);

 int local_value = world_rank + 1; // Each process has a different value
 int global_sum;

 // Reduce all local values to global sum at root process 0
 MPI_Reduce(&local_value, &global_sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

 if (world_rank == 0) {
 printf("Global sum: %d\n", global_sum);
 }

 MPI_Finalize();
 return 0;
}
```

### Example 2: Matrix-Vector Multiplication Using Collective Operations

```c
void matrix_vector_multiply(double* matrix, double* vector, double* result,
 int rows, int cols, MPI_Comm comm) {
 int rank, size;
 MPI_Comm_rank(comm, &rank);
 MPI_Comm_size(comm, &size);

 // Scatter matrix rows to different processes
 int local_rows = rows / size;
 double* local_matrix = malloc(local_rows * cols * sizeof(double));
 double* local_result = malloc(local_rows * sizeof(double));

 MPI_Scatter(matrix, local_rows * cols, MPI_DOUBLE,
 local_matrix, local_rows * cols, MPI_DOUBLE,
 0, comm);

 // Broadcast the vector to all processes
 MPI_Bcast(vector, cols, MPI_DOUBLE, 0, comm);

 // Each process computes its portion
 for (int i = 0; i < local_rows; i++) {
 local_result[i] = 0.0;
 for (int j = 0; j < cols; j++) {
 local_result[i] += local_matrix[i * cols + j] * vector[j];
 }
 }

 // Gather results back to root
 MPI_Gather(local_result, local_rows, MPI_DOUBLE,
 result, local_rows, MPI_DOUBLE,
 0, comm);

 free(local_matrix);
 free(local_result);
}
```

## Performance Considerations

### 1. Communication Costs

Collective operations are typically optimized by the MPI implementation but still incur communication costs:

- Latency: Time to initiate communication
- Bandwidth: Data transfer rate
- Synchronization: Time spent waiting for other processes

### 2. Algorithm Selection

Choose the appropriate collective operation based on:

- Data distribution pattern
- Result requirements (root-only vs all-processes)
- Operation complexity (simple transfer vs reduction)

### 3. Buffer Management

Proper buffer management is crucial:

- Ensure send and receive buffers are correctly allocated
- Match data types and counts precisely
- Avoid buffer overflows and memory leaks

## Common Pitfalls and Best Practices

### Pitfalls:

1. **Mismatched calls**: All processes must call the collective operation with compatible parameters
2. **Buffer size errors**: Incorrect counts or data types can cause crashes or incorrect results
3. **Deadlocks**: Improper use of collective operations with point-to-point operations

### Best Practices:

1. **Use collective operations** instead of multiple point-to-point calls when appropriate
2. **Choose the right operation** for your communication pattern
3. **Test with different process counts** to ensure scalability
4. **Profile communication** to identify bottlenecks

## Exam Tips

1. **Remember the blocking nature**: Collective operations don't return until all processes in the communicator have called them
2. **Know the root parameter**: For operations like Broadcast, Scatter, Gather, and Reduce, identify which process is the root
3. **Understand data distribution**: Be able to trace how data moves in Scatter, Gather, and Alltoall operations
4. **Practice common patterns**: Reduction operations with MPI_SUM, MPI_MAX, etc., are frequently tested
5. **Watch for parameter order**: MPI function parameters follow consistent patterns - practice writing the signatures
6. **Consider performance implications**: Collective operations are generally more efficient than implementing the same pattern with point-to-point operations
