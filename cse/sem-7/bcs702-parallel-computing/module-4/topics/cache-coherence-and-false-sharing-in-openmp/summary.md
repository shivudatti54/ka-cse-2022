# Cache Coherence and False Sharing in OpenMP - Summary

## Key Definitions

- **Cache Line**: The fundamental unit of data transfer between cache and main memory, typically 64 bytes on modern processors.

- **Cache Coherence**: The property ensuring that multiple caches have a consistent view of memory—for any memory location, all caches see the same data at any given time.

- **MESI Protocol**: A cache coherence protocol with four states—Modified, Exclusive, Shared, and Invalid—that tracks the status of each cache line.

- **False Sharing**: A performance phenomenon where threads modifying different variables that share the same cache line cause unnecessary cache invalidations, even when there is no actual data dependency.

- **Cache Line Padding**: Adding unused bytes between variables to ensure they occupy different cache lines.

## Important Formulas

- **Cache line alignment formula**: For a cache line of size L bytes, a variable should be placed at address A where (A mod L) = 0.

- **Padding calculation**: If variable size is S bytes and cache line size is L, padding needed = (L - (S mod L)) bytes to reach next cache line boundary.

## Key Points

1. Cache coherence is maintained at the hardware level through protocols like MESI, which use invalidation messages to ensure consistency.

2. False sharing is a performance bug—not a functional bug—that occurs when independent data shares the same cache line.

3. Adjacent array elements in OpenMP parallel loops are prime candidates for false sharing when each thread writes to its own element.

4. The MESI protocol transitions cache lines through Modified, Exclusive, Shared, and Invalid states based on read/write operations.

5. OpenMP's reduction clause naturally avoids false sharing by using private copies combined only at the end of the parallel region.

6. Padding structures to cache line size (typically 64 bytes) prevents false sharing by ensuring independent variables are on different lines.

7. Thread-local accumulation followed by a single atomic update or critical section is an effective pattern for avoiding false sharing.

8. Performance tools like Intel VTune or OpenMP profiling can identify false sharing by showing high cache miss rates.

## Common Mistakes

1. **Assuming array elements are independent**: Using `#pragma omp for` with an array where each thread writes to its own element still causes false sharing due to cache line sharing.

2. **Using padding incorrectly**: Adding only a few bytes (e.g., `char pad[8]`) instead of full cache line size (64 bytes) may not prevent false sharing on all systems.

3. **Forgetting that atomic operations still suffer from false sharing**: Each `#pragma omp atomic` update may involve cache line transfers between cores.

4. **Over-padding**: Using excessive padding wastes memory bandwidth and cache space, potentially degrading overall performance.