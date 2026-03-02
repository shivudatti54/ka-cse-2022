# GPU Programming: Architecture and Implementation

## 1. Introduction and Foundational Concepts

Graphics Processing Units (GPUs) have undergone a fundamental transformation from specialized graphics rendering engines to general-purpose parallel computing accelerators. This evolution, precipitated by the inherent data-level parallelism inherent in graphics operations, has fundamentally restructured high-performance computing paradigms across scientific simulation, computational engineering, and machine learning domains. GPU programming leverages the massively parallel architecture of these devices to achieve computational throughput levels unattainable through conventional sequential processor architectures.

### 1.1 Fundamental Architectural Philosophy

The architectural distinction between Central Processing Units (CPUs) and Graphics Processing Units (GPUs) represents a fundamental trade-off between latency optimization and throughput optimization. CPUs employ sophisticated architectural techniques to minimize instruction latency, including deep instruction pipelines, branch prediction mechanisms, out-of-order execution engines, and substantial on-chip cache hierarchies. These features enable efficient execution of serial code with complex control flow dependencies.

GPUs, conversely, embrace a throughput-oriented design philosophy predicated on massive thread-level parallelism. Modern GPUs incorporate thousands of execution units capable of simultaneously processing data-parallel operations. The GPU accepts latency not by minimizing it, but by concealing it through concurrent execution of numerous threads—while some threads encounter memory stalls, other threads progress toward completion.

## 2. GPU Architecture: SIMT Execution Model

### 2.1 Streaming Multiprocessor Organization

Modern GPUs implement the Single Instruction, Multiple Thread (SIMT) execution model, wherein groups of threads execute synchronously in lockstep formation on streaming multiprocessors (SMs). This model generalizes the traditional SIMD approach by permitting individual threads to follow independent execution paths while maintaining efficiency through warp-level synchronization.

**Definition 2.1 (Warp)**: A warp comprises a group of 32 threads that execute in lockstep on a streaming multiprocessor, simultaneously processing the same instruction but operating on distinct data elements.

**Definition 2.2 (Streaming Multiprocessor)**: A streaming multiprocessor (SM) constitutes the fundamental execution unit containing multiple warp schedulers, instruction units, arithmetic logic units, and a private memory hierarchy including shared memory and L1 cache.

### 2.2 Theoretical Throughput Analysis

The theoretical peak throughput of a GPU can be derived from its architectural parameters. For a GPU possessing $N_{SM}$ streaming multiprocessors, each capable of concurrently executing $N_{warps}$ warps:

$$Peak\ Throughput = N_{SM} \times N_{warps} \times 32 \times Clock\ Frequency$$

The factor of 32 represents the thread count per warp. Consider a contemporary GPU architecture with 80 SMs, 32 warps per SM, and a 1.5 GHz core frequency:

$$Peak\ Throughput = 80 \times 32 \times 32 \times 1.5 \times 10^9 \approx 122.88\ GFLOPS$$

This theoretical peak substantially exceeds CPU capabilities for workloads exhibiting sufficient data-level parallelism.

### 2.3 Latency Hiding Mechanism

GPU architectures achieve effective utilization through latency hiding, a technique wherein thread switching amortizes memory access latency across concurrent warp execution.

**Theorem 2.1 (Latency Hiding Condition)**: For a GPU with $N_{active\_warps}$ active warps per SM and memory latency $L_{mem}$ cycles, effective utilization approaches 100% when:

$$N_{active\_warps} \geq \frac{L_{mem}}{N_{cycles\_per\_instruction}}$$

**Proof**: Each warp requires $N_{cycles\_per\_instruction}$ cycles to complete a memory instruction. During these cycles, the warp scheduler can issue instructions from other warps. With sufficient active warps, the SM maintains continuous throughput despite individual memory stalls. ∎

## 3. GPU Memory Hierarchy

### 3.1 Hierarchical Memory Organization

GPUs implement a sophisticated multi-level memory hierarchy with distinct latency, bandwidth, and scope characteristics:

| Memory Type     | Scope      | Latency              | Bandwidth     | Capacity   |
| --------------- | ---------- | -------------------- | ------------- | ---------- |
| Global Memory   | All SMs    | ~400-800 cycles      | 400-1600 GB/s | 8-80 GB    |
| Shared Memory   | Per SM     | ~1-2 cycles          | ~10 TB/s      | 48-128 KB  |
| Constant Memory | All SMs    | ~1-2 cycles (cached) | ~10 TB/s      | 64 KB      |
| Registers       | Per Thread | 0 cycles             | ~32 TB/s      | 65,536/SM  |
| L1 Cache        | Per SM     | ~1-2 cycles          | ~10 TB/s      | 128-256 KB |

### 3.2 Memory Coalescing Theory

Optimal global memory access patterns require coalescing, wherein consecutive threads access consecutive memory addresses. This technique minimizes memory transaction count and maximizes bandwidth utilization.

**Theorem 3.1 (Coalesced Access Efficiency)**: For a warp of 32 threads accessing global memory with element size $B$ bytes and stride pattern $S$, the number of memory transactions $T$ is:

$$T = \begin{cases} 1 & \text{if } S \times 32 \times B \leq 128 \text{ bytes} \\ \lceil \frac{S \times 32 \times B}{128} \rceil & \text{otherwise} \end{cases}$$

**Proof**: GPU memory controllers issue 128-byte transactions. When $S \times 32 \times B \leq 128$, all 32 threads' accesses fall within a single 128-byte boundary, requiring one transaction. Otherwise, the access spans $\lceil S \times 32 \times B / 128 \rceil$ 128-byte segments. ∎

**Corollary 3.1.1**: The coalescing efficiency $\eta_{coalesce}$ is defined as:

$$\eta_{coalesce} = \frac{32 \times B}{T \times 128}$$

Perfectly coalesced access yields $\eta_{coalesce} = 1$.

## 4. CUDA Programming Model

### 4.1 Thread Organization Hierarchy

CUDA (Compute Unified Device Architecture) organizes threads in a three-level hierarchy:

- **Grid**: A collection of thread blocks executing the same kernel
- **Block**: A group of threads (up to 1024) executing concurrently on an SM, capable of synchronization and shared memory access
- **Thread**: The fundamental execution unit with unique coordinates (blockIdx, threadIdx)

```
Thread Hierarchy Structure:

Grid
├── Block(0,0) ─── Thread(0,0), Thread(1,0), ..., Thread(1023,0)
├── Block(1,0) ─── Thread(0,0), Thread(1,0), ..., Thread(1023,0)
├── Block(2,0) ─── Thread(0,0), Thread(1,0), ..., Thread(1023,0)
└── ... (N blocks)
```

### 4.2 Kernel Execution Model

A CUDA kernel represents a function executed in parallel by multiple threads on the GPU. The execution configuration specifies grid and block dimensions:

```cuda
__global__ void vectorAdd(float* A, float* B, float* C, int N) {
    int tid = blockIdx.x * blockDim.x + threadIdx.x;
    if (tid < N) {
        C[tid] = A[tid] + B[tid];
    }
}

// Kernel launch: 256 threads per block, N/256 blocks
vectorAdd<<<(N+255)/256, 256>>>(d_A, d_B, d_C, N);
```

### 4.3 Memory Type Specifications

CUDA provides distinct memory spaces with different performance characteristics:

| Memory Space | Declaration         | Access Scope  | Persistence      |
| ------------ | ------------------- | ------------- | ---------------- |
| Global       | `__device__`        | All threads   | Kernel duration  |
| Shared       | `__shared__`        | Block threads | Block duration   |
| Constant     | `__constant__`      | All threads   | Program duration |
| Register     | Automatic variables | Thread        | Instruction      |

### 4.4 Synchronization Primitives

**Definition 4.1 (Barrier Synchronization)**: `__syncthreads()` creates an explicit synchronization point where all threads in a block must arrive before any thread proceeds.

**Definition 4.2 (Memory Fence)**: `__threadfence()` guarantees visibility of memory writes to other threads, while `__threadfence_block()` provides fence operations scoped to the block.

## 5. Performance Optimization Principles

### 5.1 Occupancy Calculation

GPU occupancy, defined as the ratio of active warps to maximum warps per SM, critically influences performance.

$$Occupancy = \frac{N_{active\_warps}}{N_{max\_warps}} \times 100\%$$

**Theorem 5.1 (Occupancy Constraints)**: Maximum occupancy is constrained by:

1. **Register Limitation**: $N_{blocks} \times N_{registers\_per\_thread} \leq N_{registers\_per\_SM}$
2. **Shared Memory Limitation**: $N_{blocks} \times N_{shared\_memory\_per\_block} \leq N_{shared\_memory\_per\_SM}$
3. **Thread Count Limitation**: $N_{blocks} \times N_{threads\_per\_block} \leq N_{max\_threads\_per\_SM}$

### 5.2 Warp Divergence Analysis

When threads within a warp follow different execution paths due to conditional statements, warp divergence occurs, degrading performance.

**Theorem 5.2 (Divergence Penalty)**: For a warp with $P$ threads on path A and $32-P$ threads on path B, the effective execution time is:

$$T_{divergent} = T_A + T_B$$

Whereas with non-divergent execution: $T_{non\_divergent} = \max(T_A, T_B)$

The divergence overhead increases proportionally to the number of divergent paths taken.

## 6. Assessment

### 6.1 Multiple Choice Questions

1. **A GPU with 64 streaming multiprocessors, each supporting 32 active warps, operates at 1.4 GHz. What is the theoretical peak throughput in GFLOPS assuming one FLOP per clock cycle per thread?**
   - (a) 68.2 GFLOPS
   - (b) 137.2 GFLOPS
   - (c) 274.4 GFLOPS
   - (d) 548.8 GFLOPS

2. **For a warp accessing float arrays (4 bytes each) with stride 4, how many 128-byte memory transactions are required?**
   - (a) 1 transaction
   - (b) 2 transactions
   - (c) 4 transactions
   - (d) 8 transactions

3. **Which memory type provides the lowest latency but is only accessible by threads within the same block?**
   - (a) Global memory
   - (b) Constant memory
   - (c) Shared memory
   - (d) Register memory

4. **Given a GPU with 128 KB shared memory per SM and a kernel using 32 KB shared memory per block, what is the maximum number of blocks that can simultaneously execute on one SM (assuming other resources are unlimited)?**
   - (a) 2
   - (b) 4
   - (c) 8
   - (d) 16

5. **In CUDA, which function ensures all threads in a block reach a specific point before any thread continues execution?**
   - (a) `__threadfence()`
   - (b) `__syncthreads()`
   - (c) `__threadfence_block()`
   - (d) `__threadfence_system()`

### 6.2 Numerical Problem

**Problem**: A CUDA kernel processes 1 million elements using 256 threads per block. Each thread uses 20 registers and 2 KB of shared memory. Given a GPU with 65,536 registers per SM, 48 KB shared memory per SM, and maximum 1024 threads per SM:

- (a) Calculate the maximum number of blocks per SM
- (b) Determine the achievable occupancy percentage

**Solution**:

- (a) Register constraint: $65,536 / (256 \times 20) = 12.8$, so 12 blocks
  Shared memory constraint: $48 / 2 = 24$ blocks
  Thread constraint: $1024 / 256 = 4$ blocks
  Maximum blocks: min(12, 24, 4) = **4 blocks**
- (b) Active threads: $4 \times 256 = 1024$ threads
  Occupancy: $1024 / 1024 \times 100\% = **100%\***
