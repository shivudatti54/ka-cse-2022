# Dealing with I/O in Parallel Computing

=====================================

### Overview

I/O is a critical bottleneck in parallel computing due to the vast performance gap between processor speeds and storage device speeds. When multiple processors simultaneously access a shared storage device, congestion negates parallelism gains. Efficient I/O handling must be considered at the design phase of parallel applications, not as an afterthought.

### Key Points

- **I/O Bottleneck (I/O Wall):** CPUs perform billions of operations per second while storage devices are orders of magnitude slower
- **Serial I/O:** A single master process handles all I/O, creating a massive serial bottleneck that is highly unscalable
- **Parallel File Systems:** Systems like Lustre, GPFS, and PVFS2 stripe data across multiple Object Storage Targets (OSTs) for concurrent access
- **MPI-IO:** A standardized API within MPI for performing I/O operations in parallel, simplifying concurrent file access
- **Collective I/O:** Combines small I/O requests from multiple processes into fewer, larger, efficient operations
- **Data Chunking:** I/O strategy should mirror the computational data decomposition pattern
- **File Views:** Each process specifies which portion of the file is visible to it using MPI-IO file views

### Important Concepts

- Data striping distributes file data across multiple physical storage devices for concurrent access
- `MPI_File_read_all` is a collective function where all processes cooperate to read a file
- Decomposition alignment ensures each process reads only the data it needs, minimizing contention
- Parallel I/O bandwidth scales with the number of storage targets

### Notes

- I/O must be planned at the initial design phase of a parallel application
- Match the I/O pattern to the computational decomposition (block decomposition implies block I/O)
- Collective I/O operations are preferred over independent I/O for performance
- Serial I/O is the simplest but least scalable approach -- avoid for large-scale programs
