# Write Policy: Write-Back or Write-Through - Summary

## Key Definitions and Concepts

- **Write Policy**: Determines how data updates are handled when the processor writes to memory locations that may be present in cache
- **Write-Through**: Updates both cache and main memory simultaneously on every write operation
- **Write-Back**: Updates cache first, writes to main memory only when the cache block is evicted
- **Dirty Bit**: A status flag indicating whether a cache line has been modified and differs from main memory
- **Write Miss**: Occurs when the data to be written is not present in the cache
- **Write-Allocate**: Loads the block into cache on a write miss before updating
- **No-Write-Allocate**: Writes directly to main memory without loading into cache

## Important Formulas and Theorems

- **Write-Through Memory Writes**: Total writes = Number of processor writes (always equal, assuming write-allocate)
- **Write-Back Memory Writes**: Can be much less than total writes, depends on dirty block eviction frequency
- **Hit Rate Impact**: Write-back benefit increases with higher write hit rates (reusing same location)

## Key Points

- Write-Through ensures data consistency but incurs a main memory write on every store operation
- Write-Back reduces memory traffic by deferring writes until cache eviction, improving performance
- The dirty bit in write-back caches tracks modified data requiring write-back to memory
- Write-back caches are more complex but offer better performance for write-intensive workloads
- Write-through caches are simpler to implement and maintain coherence in multiprocessor systems
- Modern microcontrollers often use write-back policies to minimize power consumption
- Write buffers in write-back systems hide memory write latency from the processor

## Common Mistakes to Avoid

- Confusing write-back with no-write-allocate (they are different concepts)
- Thinking write-back never writes to memory (it does, just deferred)
- Ignoring the dirty bit status when analyzing write-back cache behavior
- Assuming write-through always performs worse (simpler coherence can be advantageous)

## Revision Tips

1. Create a comparison table of Write-Through vs Write-Back covering: operation, performance, consistency, complexity, power usage
2. Practice tracing through write sequences for both policies with a simple example
3. Remember that write-back is preferred in modern processors due to performance benefits
4. Understand that embedded/IoT systems favor write-back for power efficiency
5. Review the dirty bit state machine: clean → dirty on write, dirty → clean on write-back
