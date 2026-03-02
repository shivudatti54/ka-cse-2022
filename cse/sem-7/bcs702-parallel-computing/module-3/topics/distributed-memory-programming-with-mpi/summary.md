# Distributed Memory Programming with MPI - MPI Functions

=====================================

### Overview

MPI (Message Passing Interface) is a standardized library for distributed memory parallel programming. Processes communicate by explicitly sending and receiving messages. The core MPI functions provide initialization, communication, rank/size queries, and finalization to build parallel programs across multiple nodes.

### Key Points

- **MPI_Init:** Initializes the MPI execution environment; must be called before any other MPI function
- **MPI_Finalize:** Terminates the MPI execution environment; no MPI calls after this
- **MPI_Comm_rank:** Returns the rank (ID) of the calling process within a communicator
- **MPI_Comm_size:** Returns the total number of processes in a communicator
- **MPI_Send:** Blocking send of a message to a destination process with tag and communicator
- **MPI_Recv:** Blocking receive of a message from a source process with tag and communicator
- **MPI_COMM_WORLD:** Default communicator containing all processes
- **MPI_STATUS_IGNORE:** Used when status information from receive is not needed

### Important Concepts

- MPI_Send signature: `MPI_Send(buffer, count, datatype, dest, tag, comm)`
- MPI_Recv signature: `MPI_Recv(buffer, count, datatype, source, tag, comm, status)`
- Each process has a unique rank from 0 to size-1 within a communicator
- Tags allow differentiation of messages between the same sender-receiver pair
- Point-to-point communication involves exactly one sender and one receiver

### Notes

- Always call MPI_Init before any other MPI function and MPI_Finalize at the end
- Matching send/recv pairs must agree on datatype, tag, and communicator to avoid deadlocks
- The rank 0 process is commonly used as the master or root process
- Be able to write a basic MPI program skeleton: Init, Comm_rank, Comm_size, Send/Recv, Finalize
