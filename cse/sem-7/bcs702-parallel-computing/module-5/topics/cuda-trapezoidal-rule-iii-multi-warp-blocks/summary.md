# CUDA Trapezoidal Rule III: Blocks with More Than One Warp

=====================================

### Overview

When CUDA blocks contain more than 32 threads, they span multiple warps. Since threads within a warp execute in lockstep (SIMT), the last 5 iterations of tree reduction (strides 32 down to 1) do not need `__syncthreads()`. The optimized two-phase approach uses warp shuffle instructions (`__shfl_down_sync()`) for intra-warp reduction and shared memory only for inter-warp communication, reducing synchronization barriers from log2(blockDim.x) to just 1.

### Key Points

- **Warp = 32 threads** executing in lockstep; a 256-thread block has 8 warps
- **`__syncthreads()` needed between warps** but not within a single warp due to SIMT execution
- **volatile keyword:** Required pre-Volta to prevent compiler from caching shared memory values in registers when `__syncthreads()` is removed
- **`__shfl_down_sync(0xFFFFFFFF, val, delta)`:** Warp shuffle that lets thread i read thread i+delta's register value directly
- **Two-phase reduction:** Phase 1 reduces 32 values per warp using shuffles (no shared memory); Phase 2 reduces warp sums in shared memory
- **Shared memory savings:** From blockDim.x entries (2048 bytes for 256 doubles) down to 32 entries (256 bytes) for warp sums only
- **Only 1 `__syncthreads()` call** in the two-phase approach vs log2(blockDim.x) in the full tree

### Important Concepts

- Warp shuffle advantages: no shared memory needed, no bank conflicts, ~1 cycle latency vs ~5 cycles
- `warpReduceSum()` uses 5 shuffle-downs with deltas 16, 8, 4, 2, 1
- Lane = threadIdx.x % 32 (position within warp); warpId = threadIdx.x / 32
- On Volta+ (CC 7.0+), always use `_sync` variants; independent thread scheduling breaks the volatile approach
- Mask 0xFFFFFFFF means all 32 lanes participate in the shuffle

### Notes

- Version I (atomicAdd) is simplest but slowest; Version II (full tree) is fast; Version III (warp-optimized) is fastest
- Higher occupancy possible due to reduced shared memory usage per block
- Block size must be a multiple of 32 for clean warp boundaries
- The two-phase warp-shuffle reduction is the industry-standard pattern (used in CUB, Thrust)
