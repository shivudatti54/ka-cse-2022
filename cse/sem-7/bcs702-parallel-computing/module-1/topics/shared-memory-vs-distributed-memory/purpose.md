# Learning Purpose: Shared-Memory vs Distributed-Memory

**1. Why this topic matters**
The distinction between shared-memory and distributed-memory architectures is one of the most fundamental concepts in parallel computing, as it determines which programming model, communication strategy, and synchronization approach a developer must use. Choosing the wrong approach for a given architecture leads to poor performance or incorrect programs. This comparison is essential for selecting the right tools for any parallel computing task.

**2. What you will learn**
You will learn the architectural differences between shared-memory systems (UMA, NUMA) and distributed-memory systems (clusters, MPPs), including how processors access data in each model. You will understand the advantages and disadvantages of each in terms of scalability, programming complexity, and cost, and learn how to match the appropriate programming model (OpenMP vs MPI) to each architecture.

**3. How it connects to other topics**
This comparison ties together the hardware concepts from Module 1 and motivates the two major programming paradigms in this course: OpenMP for shared memory (Module 4) and MPI for distributed memory (Module 3). It also introduces the rationale for hybrid programming (MPI + OpenMP) that combines both approaches for large-scale systems.

**4. Real-world relevance**
Modern HPC systems are almost always hybrid, with shared-memory nodes connected via a distributed-memory network. Understanding both paradigms is essential for programming supercomputers, cloud computing clusters, and even multi-socket server systems used in enterprise applications and large-scale data processing.
