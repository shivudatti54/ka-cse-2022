# Trapezoidal Rule in OpenMP

## Introduction to Numerical Integration

Numerical integration (quadrature) is a fundamental technique in computational mathematics used to approximate definite integrals when an analytical solution is difficult or impossible to obtain. Numerical integration becomes essential when dealing with functions known only at discrete points, integrands without elementary antiderivatives, or experimental data. The trapezoidal rule represents one of the simplest and most widely used numerical integration methods, forming the foundation for more sophisticated quadrature techniques.

## Mathematical Foundation of the Trapezoidal Rule

### Derivation from Linear Interpolation

The trapezoidal rule derives from approximating the integrand f(x) by a linear function between consecutive points. Consider the interval [x_i, x_{i+1}] with width h = x*{i+1} - x_i. The area under f(x) over this subinterval is approximated by the area of the trapezoid formed by the points (x_i, 0), (x*{i+1}, 0), (x*{i+1}, f(x*{i+1})), and (x_i, f(x_i)):

```
Area = h × [f(x_i) + f(x_{i+1})] / 2
```

This geometric interpretation provides an intuitive understanding of why the method is termed the "trapezoidal rule." The approximation improves as the number of subintervals increases, as the linear approximation becomes increasingly accurate for well-behaved functions.

### Composite Trapezoidal Rule Formula

For a function f(x) defined on the interval [a, b] divided into n subintervals of equal width h = (b-a)/n, the composite trapezoidal rule approximates the integral as:

```
∫[a,b] f(x)dx ≈ h × [f(x₀)/2 + f(x₁) + f(x₂) + ... + f(x_{n-1}) + f(xₙ)/2]
```

where x_i = a + i×h for i = 0, 1, 2, ..., n. This formula can be rewritten more compactly as:

```
T_n = h × [f(a)/2 + Σ[i=1 to n-1] f(a + i×h) + f(b)/2]
```

The composite rule applies the simple trapezoidal approximation to each subinterval and sums all individual trapezoid areas to obtain the total approximation.

### Error Analysis and Proof

**Theorem (Trapezoidal Rule Error):** If f has a continuous second derivative on [a, b], then the error E_T in the composite trapezoidal rule satisfies:

```
E_T = -[(b-a)³ / (12n²)] × f''(ξ)
```

for some ξ ∈ [a, b].

**Proof:** Consider the simple trapezoidal rule on a single interval [x_i, x_{i+1}]. Using Taylor's theorem with remainder about the midpoint m = (x*i + x*{i+1})/2:

```
f(x) = f(m) + f'(m)(x-m) + f''(ξ_x)(x-m)²/2
```

Integrating this expansion over [x_i, x_{i+1}] and simplifying yields the local error term -h³f''(ξ)/12. Summing over n subintervals gives the global error formula above. The error is O(h²) = O(1/n²), indicating second-order convergence. ∎

### Convergence Analysis

The error bound demonstrates that as n → ∞ (or equivalently h → 0), the error E_T → 0, ensuring convergence of the trapezoidal rule for any twice-differentiable integrand. The second-order convergence rate means that doubling the number of subintervals reduces the error by approximately a factor of four, providing predictable accuracy improvement.

## Parallelizing the Trapezoidal Rule with OpenMP

### Why OpenMP is Ideal for This Problem

OpenMP represents an excellent choice for parallelizing the trapezoidal rule for several compelling reasons. First, the computation exhibits perfect embarrassingly parallel characteristics: each trapezoid area can be computed independently without any data dependencies between iterations. Second, OpenMP's shared memory model allows all threads to access common parameters (a, b, n, h) without explicit data distribution. Third, the natural accumulation pattern maps directly to OpenMP's reduction clause, enabling elegant and efficient parallelization. Finally, unlike MPI, no explicit message passing is required, simplifying implementation and reducing overhead.

### Sequential Implementation

Before parallelization, we present the sequential implementation to establish a baseline:

```c
#include <stdio.h>
#include <math.h>

double f(double x) {
    return x * x;  // Example: integrate x² from a to b
}

double trapezoidal_sequential(double a, double b, int n) {
    double h = (b - a) / n;
    double integral = (f(a) + f(b)) / 2.0;

    for (int i = 1; i < n; i++) {
        double x_i = a + i * h;
        integral += f(x_i);
    }

    integral *= h;
    return integral;
}
```

This implementation requires O(n) function evaluations and O(n) operations, making it suitable for parallelization when n is large.

### Parallel Implementation Using Reduction Clause

The most elegant and recommended OpenMP approach utilizes the reduction clause to handle the accumulation variable:

```c
#include <stdio.h>
#include <omp.h>
#include <math.h>

double f(double x) {
    return x * x;
}

double trapezoidal_reduction(double a, double b, int n, int thread_count) {
    double h = (b - a) / n;
    double integral = (f(a) + f(b)) / 2.0;

    #pragma omp parallel for num_threads(thread_count) reduction(+: integral)
    for (int i = 1; i < n; i++) {
        double x_i = a + i * h;
        integral += f(x_i);
    }

    integral *= h;
    return integral;
}

int main(int argc, char* argv[]) {
    double a = 0.0, b = 1.0;
    int n = 1000000;
    int thread_count = 4;

    double start = omp_get_wtime();
    double result = trapezoidal_reduction(a, b, n, thread_count);
    double end = omp_get_wtime();

    printf("Integral approximation: %.15f\n", result);
    printf("Time: %f seconds\n", end - start);
    return 0;
}
```

**Mechanism of the Reduction Clause:** The `#pragma omp parallel for reduction(+: integral)` directive creates a team of threads, each maintaining a private copy of `integral` initialized to zero. During the loop, each thread accumulates partial sums into its private copy. Upon loop completion, OpenMP automatically combines all private copies using the specified reduction operator (+) into the original `integral` variable. This approach eliminates race conditions while minimizing synchronization overhead compared to explicit critical sections.

### Alternative: Manual Thread-Based Decomposition

For educational purposes and scenarios requiring custom load balancing, manual decomposition provides greater control:

```c
double trapezoidal_manual(double a, double b, int n, int thread_count) {
    double h = (b - a) / n;
    double global_integral = (f(a) + f(b)) / 2.0;

    #pragma omp parallel num_threads(thread_count)
    {
        int my_rank = omp_get_thread_num();
        int total_threads = omp_get_num_threads();
        double local_sum = 0.0;

        // Block decomposition: thread i handles iterations i, i+p, i+2p, ...
        for (int i = my_rank + 1; i < n; i += total_threads) {
            double x_i = a + i * h;
            local_sum += f(x_i);
        }

        #pragma omp critical
        global_integral += local_sum;
    }

    global_integral *= h;
    return global_integral;
}
```

**Key Differences:** Each thread first accumulates into a private local variable, then performs a single critical section update. This approach reduces synchronization contention compared to per-iteration critical sections, as each thread updates the global sum only once.

### Performance Analysis

#### Speedup and Efficiency Metrics

The effectiveness of parallelization is quantified through speedup and efficiency:

- **Speedup S(p)**: S(p) = T_sequential / T_parallel(p), where p is the number of threads
- **Efficiency E(p)**: E(p) = S(p) / p, representing the fraction of ideal speedup achieved

For the trapezoidal rule with large n, near-linear speedup is achievable because the computation is embarrassingly parallel. However, overhead sources include thread creation and management, synchronization at the reduction combining phase (O(log p) complexity), and potential cache coherency traffic. The reduction operation's logarithmic overhead stems from the tree-based combination of partial results across threads.

#### False Sharing Considerations

False sharing occurs when multiple threads modify variables that reside on the same cache line, causing unnecessary invalidation traffic. In the manual decomposition approach, if `global_integral` is frequently updated, cache line ping-ponging between threads can degrade performance. The reduction clause mitigates this by using private accumulators during computation, minimizing shared data access patterns.

#### Scheduling Strategies

OpenMP supports various scheduling strategies affecting load distribution:

- **Static scheduling**: Iterations are divided equally before execution, suitable when work per iteration is uniform
- **Dynamic scheduling**: Iterations are distributed during execution, better for variable workloads
- **Guided scheduling**: Dynamic with decreasing chunk sizes, adaptive to runtime behavior

For the trapezoidal rule with uniform function evaluations, static scheduling typically performs best due to minimal overhead.

## Variable Scoping in OpenMP Parallel Regions

Correct understanding of variable scope is essential for correct parallel programs:

| Variable | Scope     | Justification                                          |
| -------- | --------- | ------------------------------------------------------ |
| a, b, n  | shared    | Input parameters, read-only, identical for all threads |
| h        | shared    | Computed once before parallel region                   |
| integral | reduction | Private copies created by reduction; combined at end   |
| i        | private   | Loop index automatically private in parallel for       |
| x_i      | private   | Declared inside loop body, automatic lifetime          |

Understanding these scoping rules prevents race conditions and ensures correct program behavior.

## Compilation and Execution

To compile an OpenMP program with GCC:

```bash
gcc -fopenmp -O2 -o trapezoidal trapezoidal.c -lm
```

To set thread count via environment variable:

```bash
export OMP_NUM_THREADS=4
./trapezoidal
```

The `-O2` optimization flag is recommended for accurate performance measurement.

## Comparison with Other Quadrature Methods

The trapezoidal rule provides O(n²) error convergence, making it suitable for general-purpose integration. Compared to Simpson's rule (O(n⁴) error), the trapezoidal rule requires more function evaluations for equivalent accuracy but parallelizes more naturally due to its simpler computation pattern. For highly oscillatory functions, specialized methods may be required, but the parallel structure of the trapezoidal rule makes it particularly amenable to parallel computing frameworks.

## Summary

The trapezoidal rule provides an excellent case study in parallel computing due to its inherent parallelism, predictable performance characteristics, and elegant mapping to OpenMP constructs. The reduction clause offers the simplest and most efficient parallel implementation for most use cases.
