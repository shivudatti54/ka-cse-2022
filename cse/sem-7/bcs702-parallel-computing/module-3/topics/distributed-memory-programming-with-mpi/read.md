# Distributed Memory Programming with MPI

## 1. Introduction to Distributed Memory Systems

In parallel computing, **distributed memory systems** constitute a fundamental architectural paradigm where multiple processors or compute nodes are interconnected through a high-speed communication network. Each processing node possesses its own private memory space, and data exchange between nodes occurs exclusively through explicit **message passing** protocols. This architectural approach enables scalable parallel computing, as computational resources can be expanded by adding nodes to handle increasingly complex problems.

### 1.1 Fundamental Characteristics

Unlike shared memory architectures where all processors access a common memory address space, distributed memory systems enforce strict memory isolation. This architectural constraint necessitates explicit communication mechanisms but provides several compelling advantages:

- **Linear Scalability**: Architectural design permits scaling to thousands or millions of processors without inherent memory contention
- **Absence of Memory Contention**: Each processor maintains dedicated memory, eliminating synchronization overhead associated with shared data structures
- **Economic Efficiency**: Implementation leverages commodity hardware interconnected via standard networking technologies
- **Fault Isolation**: Memory faults remain localized to individual nodes, enhancing system reliability

### 1.2 Communication Topology

The network topology connecting compute nodes significantly impacts parallel algorithm performance. Common topologies include:

- **Mesh**: Two-dimensional grid connectivity
- **Hypercube**: Logarithmic diameter connectivity
- **Torus**: Wrapped-around mesh topology
- **Tree**: Hierarchical communication patterns

## 2. MPI (Message Passing Interface) Specification

### 2.1 Standards and Implementations

MPI represents a standardized library specification for message passing in parallel computing, defined by the MPI Forum. The specification provides a portable, efficient, and flexible standard for inter-process communication across distributed memory systems.

**Key Implementations:**

- **OpenMPI**: Open-source implementation supporting hybrid architectures
- **MPICH**: Reference implementation emphasizing portability
- **Intel MPI**: Optimized for Intel architectures
- **IBM MPI**: Specialized for IBM supercomputing systems

### 2.2 Core Programming Model

MPI adopts the **Single Program Multiple Data (SPMD)** programming model where identical program instances execute concurrently, with process identification enabling differentiated behavior.

```c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
    int rank, size;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    printf("Process %d of %d\n", rank, size);

    MPI_Finalize();
    return 0;
}
```

## 3. Fundamental MPI Concepts

### 3.1 Process Model

An MPI **process** constitutes an independent execution context with the following attributes:

- Private memory address space
- Distinct program counter
- Local variable storage
- Unique rank identifier within communicator

**Critical Property**: Processes possess no shared memory; communication occurs exclusively through message passing.

### 3.2 Communicators and Groups

A **communicator** defines a collection of processes capable of mutual communication, establishing the communication scope for collective operations.

**Predefined Communicators:**

- `MPI_COMM_WORLD`: Encompasses all processes in the MPI execution
- `MPI_COMM_SELF`: Contains only the calling process

**Custom Communicator Creation:**

```c
MPI_Comm_split(MPI_COMM_WORLD, color, key, &new_comm);
```

### 3.3 Process Ranking

A **rank** serves as a unique integer identifier [0, size-1] assigned to each process within a communicator. Ranks enable:

- Addressing specific destination processes
- Determining process roles in collective operations
- Implementing algorithmic differentiation via rank-based logic

## 4. Point-to-Point Communication

### 4.1 Blocking Communication Primitives

Point-to-point communication involves direct data transfer between exactly two processes.

#### MPI_Send - Blocking Send Operation

```c
int MPI_Send(void* buf, int count, MPI_Datatype datatype,
             int dest, int tag, MPI_Comm comm);
```

**Parameter Semantics:**

- `buf`: Initial address of send buffer
- `count`: Number of elements in buffer
- `datatype`: MPI datatype (MPI_INT, MPI_FLOAT, MPI_DOUBLE, MPI_CHAR)
- `dest`: Rank of destination process
- `tag`: Message envelope identifier (non-negative integer)
- `comm`: Intracommunicator

**Blocking Semantics**: Function returns only after the send buffer is available for reuse.

#### MPI_Recv - Blocking Receive Operation

```c
int MPI_Recv(void* buf, int count, MPI_Datatype datatype,
             int source, int tag, MPI_Comm comm, MPI_Status* status);
```

**Parameter Semantics:**

- `source`: Source rank or `MPI_ANY_SOURCE` for wildcard matching
- `tag`: Message tag or `MPI_ANY_TAG` for wildcard matching
- `status`: Status object containing source, tag, and error code

### 4.2 Communication Modes

MPI supports four communication modes:

| Mode            | Behavior                                                |
| --------------- | ------------------------------------------------------- |
| **Standard**    | Implementation determines buffering                     |
| **Buffered**    | User-provided buffer guarantees asynchronous completion |
| **Synchronous** | Sender blocks until matching receive initiates          |
| **Ready**       | Assumes matching receive already posted                 |

### 4.3 Deadlock Considerations

**Deadlock** occurs when two or more processes mutually wait for communication that neither initiates. Common deadlock scenarios include:

```c
// DEADLOCK: Both processes wait indefinitely
if (rank == 0) {
    MPI_Send(buf1, 100, MPI_CHAR, 1, 0, MPI_COMM_WORLD);
    MPI_Recv(buf2, 100, MPI_CHAR, 1, 0, MPI_COMM_WORLD, &status);
} else {
    MPI_Send(buf1, 100, MPI_CHAR, 0, 0, MPI_COMM_WORLD);
    MPI_Recv(buf2, 100, MPI_CHAR, 0, 0, MPI_COMM_WORLD, &status);
}
```

**Resolution Strategies:**

- Order communications consistently across processes
- Use non-blocking operations for communication hiding
- Employ buffered communication modes

### 4.4 Non-Blocking Communication

Non-blocking operations enable computation-communication overlap:

```c
MPI_Request request;
MPI_Status status;

// Post non-blocking send
MPI_Isend(sendbuf, count, MPI_DOUBLE, dest, tag, MPI_COMM_WORLD, &request);

// Perform independent computation
compute_local_data();

// Wait for communication completion
MPI_Wait(&request, &status);
```

**Advantages:**

- Reduces idle time through computation-communication overlap
- Enables pipeline parallelism
- Essential for optimizing distributed algorithms

## 5. Collective Communication

Collective operations require participation from all processes within a communicator.

### 5.1 Broadcast (MPI_Bcast)

Distributes data from root process to all processes:

```c
MPI_Bcast(void* buffer, int count, MPI_Datatype datatype,
          int root, MPI_Comm comm);
```

**Communication Cost**: T(log P) where P denotes process count.

### 5.2 Scatter (MPI_Send)

Distributes distinct data segments from root to all processes:

```c
MPI_Scatter(void* sendbuf, int sendcount, MPI_Datatype sendtype,
            void* recvbuf, int recvcount, MPI_Datatype recvtype,
            int root, MPI_Comm comm);
```

### 5.3 Gather (MPI_Gather)

Collects data from all processes to root:

```c
MPI_Gather(void* sendbuf, int sendcount, MPI_Datatype sendtype,
           void* recvbuf, int recvcount, MPI_Datatype recvtype,
           int root, MPI_Comm comm);
```

### 5.4 Reduction Operations (MPI_Reduce)

Applies reduction operation across all processes:

```c
MPI_Reduce(void* sendbuf, void* recvbuf, int count,
           MPI_Datatype datatype, MPI_Op op, int root, MPI_Comm comm);
```

**Standard Reduction Operations:**

- `MPI_SUM`: Global summation
- `MPI_PROD`: Global product
- `MPI_MAX`: Maximum value
- `MPI_MIN`: Minimum value
- `MPI_LAND`: Logical AND

### 5.5 Allreduce

All processes receive reduction results:

```c
MPI_Allreduce(void* sendbuf, void* recvbuf, int count,
              MPI_Datatype datatype, MPI_Op op, MPI_Comm comm);
```

### 5.6 Barrier Synchronization (MPI_Barrier)

Ensures all processes reach synchronization point:

```c
MPI_Barrier(MPI_Comm comm);
```

## 6. Practical Parallel Algorithms

### 6.1 Parallel Summation

```c
double parallel_sum(double local_val) {
    double total;
    MPI_Reduce(&local_val, &total, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
    return total;
}
```

**Performance Analysis**: Logarithmic reduction depth yields O(log P) communication cost.

### 6.2 Parallel Prefix (Scan) Algorithm

Parallel prefix computes cumulative operations across distributed data:

```c
void parallel_prefix_scan(double* local_data, int local_n, MPI_Comm comm) {
    int rank, size;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);

    double* recvbuf = (double*)malloc(local_n * sizeof(double));

    for (int stride = 1; stride < size; stride *= 2) {
        if (rank >= stride) {
            MPI_Send(local_data, local_n, MPI_DOUBLE, rank - stride, 0, comm);
            MPI_Recv(recvbuf, local_n, MPI_DOUBLE, rank - stride, 0, comm, MPI_STATUS_IGNORE);
            for (int i = 0; i < local_n; i++)
                local_data[i] += recvbuf[i];
        }
        MPI_Barrier(comm);
    }
    free(recvbuf);
}
```

### 6.3 Domain Decomposition

Decomposing computational domains across processes:

```c
void distribute_domain(int N, int rank, int size, int* start, int* end) {
    int chunk = N / size;
    int remainder = N % size;

    *start = rank * chunk + (rank < remainder ? rank : remainder);
    *end = *start + chunk + (rank < remainder ? 1 : 0);
}
```

## 7. Performance Considerations

### 7.1 Communication Cost Model

Communication latency comprises:

- **Startup time (t_s)**: Protocol initiation overhead
- **Per-byte transfer time (t_w)**: Bandwidth-dependent cost
- **Per-hop cost**: Network topology influence

**Simple Model**: T_comm = t_s + (n × t_w)

### 7.2 Optimization Strategies

- Minimize message frequency through buffering
- Employ collective operations for regular communication patterns
- Overlap communication with computation using non-blocking primitives
- Optimize data layout to reduce communication volume
- Consider network topology in algorithm design

## 8. Derived Datatypes

MPI supports structured data transmission through derived datatypes:

```c
// Contiguous datatype
MPI_Type_contiguous(count, oldtype, &newtype);

// Vector datatype (strided access)
MPI_Type_vector(count, blocklen, stride, oldtype, &newtype);

// Struct datatype (heterogeneous structures)
MPI_Type_create_struct(count, blocklens, offsets, oldtypes, &newtype);

MPI_Type_commit(&newtype);
```

---

# Assessment Questions

## Multiple Choice Questions

### Question 1

In an MPI program with 4 processes, process 0 executes:

```c
MPI_Send(sendbuf, 100, MPI_CHAR, 1, 10, MPI_COMM_WORLD);
MPI_Recv(recvbuf, 100, MPI_CHAR, 1, 20, MPI_COMM_WORLD, &status);
```

Process 1 executes:

```c
MPI_Recv(recvbuf, 100, MPI_CHAR, 0, 10, MPI_COMM_WORLD, &status);
MPI_Send(sendbuf, 100, MPI_CHAR, 0, 20, MPI_COMM_WORLD);
```

What is the correct characterization of this communication pattern?

A) This program will execute without deadlock because MPI automatically buffers messages
B) This program will deadlock because both processes block on receive before sending
C) This program will execute correctly because message tags differ (10 vs 20)
D) This program exhibits race condition due to non-deterministic message ordering

**Answer: B**

**Explanation**: This demonstrates classic **deadlock** arising from **blocking receive** operations. Process 0 blocks on receive waiting for tag 20, while Process 1 blocks on receive waiting for tag 10. Neither can proceed to execute their send operation. MPI does not automatically buffer standard mode sends—the implementation may buffer internally, but this behavior is not guaranteed. Message tags being different is irrelevant since receives specify exact tags, creating mutual waiting.

---

### Question 2

Consider parallel summation of N elements across P processes using the following code executed by each process:

```c
double local_sum = compute_local_sum();
double result;

for (int stride = 1; stride < P; stride *= 2) {
    if (rank % (2*stride) == 0) {
        if (rank + stride < P) {
            MPI_Recv(&local_sum, 1, MPI_DOUBLE, rank + stride, 0,
                     MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            local_sum += result;
        }
    } else if (rank % (2*stride) == stride) {
        MPI_Send(&local_sum, 1, MPI_DOUBLE, rank - stride, 0, MPI_COMM_WORLD);
    }
    MPI_Barrier(MPI_COMM_WORLD);
}
```

What is the time complexity of this algorithm (excluding barrier costs)?

A) O(N/P) computation, O(P) communication
B) O(N/P) computation, O(log P) communication
C) O(N) computation, O(P) communication
D) O(N/P) computation, O(P log P) communication

**Answer: B**

**Explanation**: This implements **parallel reduction** using a **pairwise exchange** algorithm. Each iteration doubles the stride, resulting in log₂P iterations. In iteration k (stride = 2^k), approximately P/2^{k+1} processes participate in send/receive pairs. Total communication operations: P/2 + P/4 + P/8 + ... = P(1/2 + 1/4 + 1/8 + ...) = P. However, each iteration completes in constant time (local send/receive), yielding O(log P) parallel time complexity. Local computation is O(N/P), making total complexity O(N/P + log P).

---

### Question 3

Three MPI processes execute the following code simultaneously:

```c
MPI_Comm_rank(MPI_COMM_WORLD, &rank);
if (rank == 0)
    MPI_Bcast(buffer, 100, MPI_INT, 0, MPI_COMM_WORLD);
else if (rank == 1)
    MPI_Bcast(buffer, 100, MPI_INT, 1, MPI_COMM_WORLD);
else
    MPI_Bcast(buffer, 100, MPI_INT, 2, MPI_COMM_WORLD);
```

Which statement correctly describes the execution?

A) All processes participate in a single broadcast with rank 0 as root
B) Each process becomes root of its own broadcast, causing undefined behavior
C) Process 0 and process 1 participate in broadcasts; process 2 waits indefinitely
D) MPI will automatically select a valid root and complete the broadcast

**Answer: B**

**Explanation**: This code violates MPI semantics. The **root parameter** must be identical across **all** participating processes in a collective operation. Here, each process specifies a different root (0, 1, 2 respectively). MPI implementations are not required to detect this error—behavior is undefined. Depending on the implementation, this may cause deadlock, incorrect data, or process crashes. Correct usage requires consistent root specification: `MPI_Bcast(buffer, 100, MPI_INT, 0, MPI_COMM_WORLD);` for all processes.

---

### Question 4

A parallel application uses MPI_Scatter to distribute an array of 1000 integers across 10 processes. Each process receives 100 integers. If the latency parameter t_s = 10 μs and per-word transfer time t_w = 0.01 μs, what is the estimated communication time using the simple latency model?

A) 10 μs
B) 20 μs
C) 110 μs
D) 1000 μs

**Answer: B**

**Explanation**: The simple communication cost model: **T = t_s + n × t_w**, where n is the number of words transferred.

For MPI_Scatter with 1000 integers (assuming 4-byte integers = 4000 bytes = 1000 words):

- **t_s** = 10 μs (latency)
- **n × t_w** = 1000 × 0.01 = 10 μs

Total: 10 + 10 = **20 μs**

Note: This assumes the simple model where scatter cost equals send cost to one process. More accurate models account for the tree-based implementation typically used, yielding T = t_s + (n/P) × t_w × log₂P, but the simple model suffices here.
