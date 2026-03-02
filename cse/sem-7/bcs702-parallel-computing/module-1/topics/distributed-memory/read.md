# Distributed Memory Systems

## Introduction

Distributed memory systems represent a fundamental paradigm in parallel computing where each processing element possesses its own private memory space, and communication between processors occurs exclusively through message passing over an interconnection network. Unlike shared memory architectures where all processors access a common address space, distributed memory systems enforce strict memory isolation, requiring explicit data movement between processor local memories. This architectural choice, while introducing programming complexity, offers superior scalability characteristics that have made it the dominant paradigm for large-scale parallel computing systems. The design philosophy behind distributed memory stems from the physical limitations of bus-based shared memory systems, which become bandwidth-constrained as processor counts increase.

The conceptual foundation of distributed memory computing rests on the principle of locality—both spatial and temporal. Each processor primarily operates on data stored in its local memory, minimizing the need for expensive remote memory accesses. When data from another processor's memory is required, explicit communication must be initiated, introducing latency that must be carefully managed in parallel algorithm design. This model naturally maps to problems with structured data distributions, such as grid-based computations in scientific simulations, where data dependencies follow regular patterns that can be efficiently communicated along network paths. The evolution of distributed memory systems from early message-passing supercomputers to modern cloud computing infrastructure demonstrates the enduring importance of this architectural approach.

## Key Concepts

### Architectural Components

A distributed memory system comprises multiple compute nodes, each consisting of a processor, local memory, and a network interface card (NIC) connected through an internal bus. The processors within a node may themselves be multi-core, but the fundamental memory model remains distributed at the node level. The interconnection network provides the communication substrate, with characteristics including topology, bandwidth, and latency that fundamentally determine system performance. Modern systems employ various network technologies including InfiniBand, Ethernet, and proprietary interconnects, each offering different trade-offs between cost, bandwidth, and latency.

The absence of a shared address space means that programmers must explicitly manage data distribution across processors. This requirement for explicit data movement distinguishes distributed memory programming from shared memory approaches and necessitates careful attention to communication patterns, data layout, and load balancing. The distributed nature of memory also implies that synchronization must be achieved through message passing rather than through shared variables, typically employing primitives such as barriers and collective operations that coordinate the actions of multiple processors.

### Message Passing Model

The message passing paradigm provides the fundamental abstraction for inter-process communication in distributed memory systems. Under this model, processes execute independently with their own address spaces, and data transfer occurs through explicit send and receive operations. The send operation copies data from the sender's local buffer to the network, while the receive operation copies data from the network to the receiver's local buffer. This communication model requires careful attention to synchronization—processes must coordinate to ensure that sends and receives match, preventing deadlock situations where processes wait indefinitely for communications that never complete.

Message passing interfaces have been standardized through the Message Passing Interface (MPI), which defines a portable library specification adopted widely in parallel computing. MPI provides point-to-point communication primitives for direct processor-to-processor messaging, as well as collective operations that involve groups of processes. Collective operations include broadcast (one process sending data to all others), gather (collecting data from all processes to one), scatter (distributing data from one process to all others), and reduction (combining data from all processes using an associative operator). These abstractions enable efficient implementation of common communication patterns while providing portability across different hardware platforms.

### Interconnection Network Topologies

The interconnection network topology critically impacts the performance characteristics of distributed memory systems. Common topologies include bus, ring, mesh, hypercube, and tree structures, each offering different trade-offs in terms of diameter (maximum distance between any two nodes), bisection bandwidth (the bandwidth across a minimum cut separating the network into two equal halves), and implementation complexity. The diameter of a network determines the maximum number of hops a message must traverse, directly affecting worst-case communication latency.

A **d-dimensional hypercube** connects N = 2^d nodes such that each node has d neighbors, with the diameter equal to d. This topology provides logarithmic diameter and excellent connectivity, though the number of links per node grows with log₂N, potentially limiting scalability. A **k-ary d-mesh** organizes nodes in a d-dimensional grid with k nodes along each dimension, offering regular structure that maps naturally to grid-based problems. The torus variation wraps connections at mesh boundaries, reducing diameter and improving path diversity. Mathematical analysis shows that the diameter of a d-dimensional mesh with k nodes per dimension equals d × (k-1), while a hypercube achieves diameter d = log₂N with only log₂N links per node.

### Communication Cost Models

Quantitative analysis of distributed memory systems employs formal cost models that capture the time required for message communication. The basic **latency-bandwidth model** expresses communication time T as: T = α + nβ, where α represents the latency (startup cost), β represents the per-byte transfer time, and n represents the message size in bytes. This model captures the fundamental trade-off between message size and communication efficiency—larger messages achieve better bandwidth utilization but incur greater absolute latency.

For network topologies with multiple paths, contention effects complicate the basic model. The **store-and-forward** model charges the full latency cost per hop, while **cut-through** routing allows messages to proceed to the next node before complete reception, reducing effective latency for multi-hop communication. Performance analysis of parallel algorithms requires combining computation costs with communication costs, considering both the volume of data transferred and the pattern of communication. The **isoefficiency** metric measures how problem size must scale with processor count to maintain constant efficiency, providing a formal framework for analyzing scalability.

### Distributed Shared Memory

Distributed Shared Memory (DSM) systems represent a hybrid approach that provides the abstraction of shared memory on distributed hardware. Under DSM, multiple machines collectively maintain a single logical address space, with hardware or software mechanisms transparently migrating data between local memories as needed. This approach combines the programming convenience of shared memory with the scalability of distributed architectures, though it introduces overhead for coherence maintenance and may exhibit performance variability depending on access patterns. Implementation strategies include page-based DSM (where memory pages are migrated between nodes) and object-based DSM (where finer-grained data items are managed), each offering different trade-offs between overhead and flexibility.

## Examples

### Matrix-Vector Multiplication

Consider parallel matrix-vector multiplication y = Ax where A is an N×N matrix distributed across P processors. Under a row-block distribution, processor i owns rows iN/P through (i+1)N/P - 1. Each processor initially stores its local portion of A and a copy of the complete vector x. For optimal performance, we can pipeline the vector broadcast while computing: as soon as processor j needs element x[k], it requests this value rather than storing the entire vector. The communication volume per processor equals N/P elements received from the vector, while computation involves approximately 2N²/P floating-point operations. The communication-to-computation ratio decreases as N increases, explaining why this algorithm exhibits good strong scaling properties.

### Message Passing Code Structure

```c
// Distributed memory matrix multiplication with block distribution
void parallel_matrix_multiply(double *A, double *B, double *C,
                              int N, int rank, int size) {
    int block_size = N / size;
    double *local_A = malloc(block_size * N * sizeof(double));
    double *local_B = malloc(N * block_size * sizeof(double));
    double *local_C = malloc(block_size * block_size * sizeof(double));

    // Scatter columns of B to all processes
    MPI_Scatter(B, N * block_size, MPI_DOUBLE,
                local_B, N * block_size, MPI_DOUBLE, 0, MPI_COMM_WORLD);

    // Broadcast rows of A to all processes (or use pipeline)
    MPI_Bcast(A + rank * block_size * N, block_size * N,
              MPI_DOUBLE, rank, MPI_COMM_WORLD);

    // Local computation: local_C = local_A * local_B
    for (int i = 0; i < block_size; i++)
        for (int j = 0; j < block_size; j++)
            for (int k = 0; k < N; k++)
                local_C[i * block_size + j] += local_A[i * N + k] *
                                               local_B[k * block_size + j];

    // Gather results to root process
    MPI_Gather(local_C, block_size * block_size, MPI_DOUBLE,
               C, block_size * block_size, MPI_DOUBLE, 0, MPI_COMM_WORLD);
}
```

### Communication Cost Analysis

For a hypercube network with N = 2^d processors, the time to broadcast a message of size m from one processor to all others equals: T_broadcast = α + (d-1)β + mβ(d-1) under store-and-forward routing, or approximately α + mβ under cut-through routing. This analysis demonstrates why collective communication algorithms are designed to minimize the number of communication steps while maximizing bandwidth utilization. The logarithmic dependence on processor count explains the excellent scalability characteristics of hypercube-connected systems for collective operations.

## Exam Tips

1. **Remember the fundamental distinction**: In distributed memory, processors have private memories and communicate via messages; in shared memory, processors share a common address space and communicate through reads/writes to shared variables.

2. **Master the communication cost formula**: T = α + nβ, understanding that latency α dominates for small messages while bandwidth (1/β) determines throughput for large messages.

3. **Know key topologies and their properties**: Hypercube has diameter log₂N and degree log₂N; mesh has diameter O(N^(1/d)) with degree 2d; torus improves mesh by wrapping boundaries.

4. **Understand scalability metrics**: Isoefficiency analysis determines how problem size must grow with processor count to maintain constant parallel efficiency; strong scaling fixes problem size while weak scaling fixes per-problem size.

5. **MPI collective operations**: Remember that collectives involve all processes in a communicator and provide synchronization implicitly; distinguish between broadcast, gather, scatter, and reduction.

6. **Deadlock prevention**: In message passing, ensure that receive operations are posted before corresponding sends, or use non-blocking communication (MPI_Isend/MPI_Irecv) to avoid circular wait dependencies.

7. **Network bisection bandwidth**: This metric measures the minimum bandwidth across any cut dividing the network in half; it determines the rate at which data can move between halves during collective operations.
