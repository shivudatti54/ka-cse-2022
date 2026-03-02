# Cache Memories – Mapping Functions

### Definitions and Theorems

- **Cache Memory**: A small, fast memory that stores frequently accessed data or instructions.
- **Mapping Function**: A relationship between the cache addresses and the main memory addresses.
- **Direct Mapping**: A mapping function that maps each cache address to a main memory address.
- **Indirect Mapping**: A mapping function that maps each cache address to a main memory address through a tag.
- **Set-Associative Mapping**: A mapping function that divides the cache into sets, each with its own set of tags.

### Key Formulas

- **Cache Hit**: A successful access to a cache line that is in the cache.
- **Cache Miss**: An unsuccessful access to a cache line that is not in the cache.
- **Cache Hit Rate**: The ratio of cache hits to total accesses.
- **Cache Miss Rate**: The ratio of cache misses to total accesses.
- **Cache Replacement Policy**: The algorithm used to replace a cache line when it is replaced.

### Important Formulas

- **Cache Hit Rate = (H / (H + M)) \* 100**, where H is the number of cache hits and M is the number of cache misses.
- **Cache Miss Rate = (M / (H + M)) \* 100**, where H is the number of cache hits and M is the number of cache misses.
- **Hit Rate = (H / (H + M))**, where H is the number of cache hits and M is the number of cache misses.

### Key Points

- Cache memories are used to improve system performance by reducing the time it takes to access data and instructions.
- Mapping functions are used to map cache addresses to main memory addresses.
- Direct mapping, indirect mapping, and set-associative mapping are common types of mapping functions.
- The cache hit rate and cache miss rate are important metrics used to evaluate cache performance.
- Cache replacement policies, such as LRU and FIFO, are used to replace cache lines when they are replaced.
