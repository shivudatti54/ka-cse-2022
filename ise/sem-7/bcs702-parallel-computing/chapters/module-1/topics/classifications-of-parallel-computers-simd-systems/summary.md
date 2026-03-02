# **Classifications of Parallel Computers, SIMD Systems, MIMD Systems, Interconnection Networks, Cache Coherence, Shared-Memory vs**

## **I. Classifications of Parallel Computers**

- **Parallel Computer**: A computer that consists of multiple processing units connected together to increase processing speed and efficiency.
- **MIMD (Multiple Instruction, Multiple Data)**: A parallel computer architecture where multiple processors execute different instructions on different data.
- **SIMD (Same Instruction, Multiple Data)**: A parallel computer architecture where a single processor executes the same instruction on multiple data.

## **II. SIMD Systems**

- **SIMD Architecture**: A parallel processing architecture where a single processor executes the same instruction on multiple data elements.
- **Examples**: Vector Processors (e.g. SIMD-8, VLSI-8), Graphics Processing Units (GPUs), Field-Programmable Gate Arrays (FPGAs)
- **Key Characteristics**: Single instruction, multiple data, data parallelism

## **III. MIMD Systems**

- **MIMD Architecture**: A parallel processing architecture where multiple processors execute different instructions on different data.
- **Examples**: Multi-Processor Systems, Distributed Memory Architectures
- **Key Characteristics**: Multiple instructions, multiple data, instruction parallelism

## **IV. Interconnection Networks**

- **Interconnection Network**: A network that connects processors or nodes in a parallel computer system to enable communication and data exchange.
- **Types**: Bus-Based, Switch-Based, Mesh-Based, Hypercube-Based

## **V. Cache Coherence**

- **Cache Coherence**: A mechanism to ensure that data is consistent across multiple processors in a parallel computer system.
- **Types**: Strong Consistency, Weak Consistency, Casual Consistency

## **VI. Shared-Memory vs Distributed-Memory**

- **Shared-Memory Architecture**: A parallel computer architecture where all processors share a common memory space.
- **Distributed-Memory Architecture**: A parallel computer architecture where each processor has its own memory space.
- **Key Characteristics**: Shared memory, distributed memory

## **Important Formulas and Definitions**

- **Amdahl's Law**: A measure of the theoretical speedup of a parallel program.
- **Gotoh's Law**: A measure of the maximum theoretical speedup of a parallel program.
- **Parnas' Law**: A measure of the maximum theoretical speedup of a parallel program.

## **Theorems**

- **Amdahl's Law Theorem**: A theoretical bound on the speedup of a parallel program.
- **Gotoh's Law Theorem**: A theoretical bound on the speedup of a parallel program.
