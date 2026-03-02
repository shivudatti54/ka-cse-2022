# The Trapezoidal Rule in OpenMP

=====================================

### Overview

The trapezoidal rule approximates a definite integral by dividing the area under a curve into trapezoids. In OpenMP, this embarrassingly parallel computation is parallelized using `#pragma omp parallel for reduction(+:integral)`, where each thread independently evaluates function values and the reduction clause combines partial sums.

### Key Points

- **Formula:** Integral[a,b] f(x)dx ~ h \* [f(x0)/2 + f(x1) + f(x2) + ... + f(x_{n-1}) + f(xn)/2], h = (b-a)/n
- **Reduction Approach (Best):** `#pragma omp parallel for reduction(+:integral)` -- compiler-optimized, no explicit locks
- **Critical Approach (Worst):** `#pragma omp critical` per iteration serializes accumulation, kills performance
- **Manual Approach (Good):** Thread-local sum + single critical section at end reduces contention
- **Speedup:** S(p) = T_sequential / T_parallel(p); near-linear for large n
- **Efficiency:** E(p) = S(p) / p; reduction clause has O(log p) overhead
- **Error:** O(h^2); doubling n reduces error by factor of 4; parallelization does not affect accuracy

### Important Concepts

- Variable scoping: a, b, n, h are shared; integral is reduction; i and x_i are private
- Loop index i is automatically private in `#pragma omp for`
- Variables declared inside the loop body are private by default
- Compile with: `gcc -fopenmp -o trap trap.c -lm`

### Notes

- Always use `reduction(+:integral)` as the preferred approach for the trapezoidal rule
- Floating-point ordering may cause tiny differences between serial and parallel results -- this is expected
- Be prepared to write and compare all three approaches: reduction, critical, and manual decomposition
- The error is O(h^2) regardless of the number of threads used
