# Scope of Variables in OpenMP

=====================================

### Overview

Variable scope in OpenMP determines which threads can access a variable and whether access is shared or private. Incorrectly scoped variables are a primary source of race conditions and data corruption. OpenMP provides clauses like shared, private, firstprivate, lastprivate, and reduction to explicitly control variable scope.

### Key Points

- **Shared Variables:** Single memory location accessed by all threads; default for variables declared outside parallel region
- **Private Variables:** Each thread gets an independent copy; default for variables declared inside parallel region
- **firstprivate:** Private copy initialized with the original variable's value before the parallel region
- **lastprivate:** Updates the original variable with the value from the sequentially last iteration after the region
- **reduction:** Creates private copies, computes locally, then combines results using the specified operator
- **default(none):** Forces explicit specification of all variable scopes -- a best practice to prevent bugs
- **Loop Index:** Automatically made private in `#pragma omp for` regardless of original declaration

### Important Concepts

- Syntax: `#pragma omp parallel shared(a) private(b) firstprivate(c) lastprivate(d) reduction(+:e)`
- Private variables inside a parallel region are uninitialized (use firstprivate if initial value needed)
- The original variable's value after a parallel region is undefined for private variables
- Reduction initialization: 0 for +, 1 for \*, min type max for min, max type min for max

### Notes

- Always use `default(none)` and explicitly declare every variable's scope
- Race conditions occur when shared variables are written without synchronization
- Use reduction instead of critical sections for accumulation operations -- it is more efficient
- The loop index in `#pragma omp for` is always private, even if declared outside the region
