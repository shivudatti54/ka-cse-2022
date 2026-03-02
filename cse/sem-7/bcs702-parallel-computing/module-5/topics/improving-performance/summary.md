# Improving Performance in CUDA - Summary

## Key Definitions
- **Memory Coalescing**: Combining memory requests from threads in a warp into fewer transactions when accessing consecutive addresses
- **Bank Conflict**: Serialization of shared memory accesses when multiple threads access the same memory bank
- **Occupancy**: Ratio of active warps to maximum warps per streaming multiprocessor
- **Warp Divergence**: Different execution paths taken by threads within the same warp
- **Latency Hiding**: Technique of hiding memory/instruction latency by scheduling ready warps while others wait

## Important Formulas
- Coalesced access condition: `base_address % (threads_per_warp * element_size) == 0`
- Global memory transactions required: `ceil(accessed_bytes / transaction_size)`
- Effective bandwidth = `data_transferred / (time_elapsed)`
- Occupancy = `active_warps / max_warps_per_SM`

## Key Points
1. Coalesced global memory access can provide 10x+ speedup over non-coalesced access
2. Shared memory is 100x faster than global memory but requires careful bank access patterns
3. Padding shared memory arrays eliminates bank conflicts in column-wise access
4. Higher occupancy provides more warps for latency hiding but may reduce per-thread resources
5. Warp divergence should be minimized by restructuring code to keep threads on similar paths
6. Tiling with shared memory reduces global memory bandwidth requirements
7. Thread block size should be a multiple of 32 (warp size) for full efficiency
8. The optimal configuration depends on specific hardware and kernel characteristics

## Common Mistakes
1. Using 2D thread indexing without considering memory access patterns
2. Forgetting to call `__syncthreads()` after loading shared memory
3. Creating bank conflicts by accessing shared memory with strided patterns
4. Setting thread block sizes that are too small, reducing occupancy
5. Introducing warp divergence through poorly structured conditionals
6. Not padding shared memory arrays when accessing columns in 2D data
7. Optimizing without profiling — always measure before and after changes