# Collective Communication in MPI

=====================================

### Overview

Collective communication in MPI involves coordinated communication among all processes in a communicator group, unlike point-to-point communication between two processes. These operations are essential for distributing data, gathering results, and synchronizing processes in parallel programs. All processes must call the collective routine, and these calls are blocking.

### Key Points

- **MPI_Barrier:** Synchronizes all processes; each blocks until all reach the barrier
- **MPI_Bcast:** Broadcasts data from root process to all other processes
- **MPI_Scatter:** Distributes chunks of data from root to all processes
- **MPI_Gather:** Collects data from all processes and stores at root
- **MPI_Reduce:** Combines data from all processes using an operation (SUM, MAX, MIN, etc.) and stores result at root
- **MPI_Allgather:** Gathers data and distributes the result to all processes (not just root)
- **MPI_Allreduce:** Reduces data and distributes the combined result to all processes
- **Reduction Operators:** MPI_SUM, MPI_PROD, MPI_MAX, MPI_MIN, MPI_LAND, MPI_LOR, MPI_BAND, MPI_BOR

### Important Concepts

- All processes in the communicator must call collective operations with compatible parameters
- Collective operations are generally more efficient than equivalent point-to-point implementations
- MPI_Reduce stores result only at root; MPI_Allreduce stores result at all processes
- Communication costs include latency, bandwidth, and synchronization overhead

### Notes

- Always match parameter types, counts, and root process across all calling processes to avoid deadlocks
- Use collective operations over multiple point-to-point calls for better performance and readability
- Know the function signatures: buffer, count, datatype, root, communicator pattern is common
- Practice tracing data movement in Scatter, Gather, and Reduce operations for exam questions
