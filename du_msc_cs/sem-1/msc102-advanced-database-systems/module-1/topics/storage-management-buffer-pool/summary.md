# Storage Management & Buffer Pool - Summary

## Key Definitions and Concepts
- Buffer Pool: Volatile cache for database pages
- Dirty Page: Modified page not yet written to disk
- Locality of Reference: Temporal vs spatial access patterns
- Flush Policy: Criteria for writing dirty pages to disk
- Working Set: Actively used pages in current transaction mix

## Important Formulas and Theorems
- Hit Ratio (HR) = (Logical Reads - Physical Reads) / Logical Reads
- Effective Access Time: HR*T_mem + (1-HR)*T_disk
- LRU-K Cost Function: C(p) = 1 / (t_current - t_{k-th last access})
- Bélády's Theorem: Optimal replacement requires future knowledge

## Key Points
- Clock algorithm variants dominate practical implementations
- Write-optimized buffers require careful crash recovery integration
- Buffer pool sizing follows 80/20 rule (80% of gains from 20% memory)
- Column stores use vertical partitioning in buffer pools
- Modern SSDs require different replacement heuristics than HDDs
- Machine learning models need lightweight inference (<1μs/page)
- NUMA architectures demand page placement awareness

## Common Mistakes to Avoid
- Assuming LRU is always optimal for all workloads
- Ignoring pin counts in concurrency control
- Overlooking page size alignment with storage blocks
- Treating buffer pool as independent of query planner
- Neglecting memory bandwidth in throughput calculations

## Revision Tips
1. Practice drawing buffer states for replacement algorithms
2. Memorize 3 key metrics from PostgreSQL's pg_buffercache
3. Compare 2 recent papers on ML-based buffer management
4. Use Linux perf to analyze real buffer pool behavior
5. Create cheat sheet for algorithm tradeoffs (space/time complexity)

Length: 650 words