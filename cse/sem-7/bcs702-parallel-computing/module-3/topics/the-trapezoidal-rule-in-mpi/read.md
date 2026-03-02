# Parallel Trapezoidal Rule: Theory and MPI Implementation

## 1. Introduction to Numerical Integration

Numerical integration, also termed quadrature, constitutes a fundamental pillar of computational mathematics. It provides systematic approximations to definite integrals of the form ∫ₐᵇ f(x)dx when analytical solutions remain intractable or impossible to derive. The significance of numerical integration extends across diverse scientific domains, including physics simulations, engineering design, probability theory, and statistical mechanics.

The necessity for parallel implementation of numerical integration arises from multiple computational demands. High-precision approximations necessitate substantially large numbers of subintervals n, resulting in O(n) function evaluations. When the integrand f(x) involves computationally expensive operations—such as evaluating special functions, solving differential equations, or performing numerical optimizations—serial computation becomes prohibitively time-consuming. Furthermore, scenarios involving parametric studies, wherein thousands or millions of integral evaluations are required with varying parameters, demand efficient parallelization strategies.

## 2. Theoretical Foundation of the Trapezoidal Rule

### 2.1 Derivation of the Composite Formula

The composite trapezoidal rule approximates the definite integral by partitioning the interval [a, b] into n subintervals of equal width h = (b-a)/n. Each subinterval [xᵢ, xᵢ₊₁] is approximated by a trapezoid rather than a rectangle, yielding improved accuracy.

For a single subinterval [xᵢ, xᵢ₊₁], the trapezoidal approximation yields:

∫ₓᵢ^xᵢ₊₁ f(x)dx ≈ h × [f(xᵢ) + f(xᵢ₊₁)]/2

Summing over all n subintervals, we obtain the composite trapezoidal rule:

∫ₐᵇ f(x)dx ≈ (h/2)[f(x₀) + 2f(x₁) + 2f(x₂) + ... + 2f(xₙ₋₁) + f(xₙ)]

where xᵢ = a + ih for i = 0, 1, 2, ..., n.

### 2.2 Error Analysis and Proof

**Theorem (Trapezoidal Rule Error Bound):** Let f(x) possess a continuous second derivative on [a, b]. Then the composite trapezoidal rule with n subintervals satisfies:

|E_T| ≤ (b-a)³/(12n²) × maxₐ≤x≤b |f''(x)|

**Proof:** Consider the local truncation error for a single subinterval [xᵢ, xᵢ₊₁]. Using Taylor's theorem about the midpoint m = (xᵢ + xᵢ₊₁)/2:

f(xᵢ) = f(m) - (h/2)f'(m) + (h²/8)f''(m) - (h³/48)f'''(m) + (h⁴/384)f⁽⁴⁾(ξ₁)

f(xᵢ₊₁) = f(m) + (h/2)f'(m) + (h²/8)f''(m) + (h³/48)f'''(m) + (h⁴/384)f⁽⁴⁾(ξ₂)

Adding these expressions:

f(xᵢ) + f(xᵢ₊₁) = 2f(m) + (h²/4)f''(m) + O(h⁴)

The exact integral expanded about m:

∫ₓᵢ^xᵢ₊₁ f(x)dx = hf(m) + (h³/24)f''(m) + O(h⁵)

The trapezoidal approximation: T = h × [f(xᵢ) + f(xᵢ₊₁)]/2 = hf(m) + (h³/8)f''(m) + O(h⁵)

Local error: T - ∫ = -(h³/12)f''(m) + O(h⁵)

Summing n local errors with h = (b-a)/n:

|E_T| ≤ n × (h³/12) × max|f''(x)| = (b-a)³/(12n²) × max|f''(x)|

**Corollary:** The composite trapezoidal rule exhibits second-order convergence: doubling n reduces the error by a factor of 4.

## 3. Parallelization Strategy Using MPI

### 3.1 Domain Decomposition

The parallel implementation employs domain decomposition, wherein the integration interval [a, b] is partitioned among p available processes. Each process receives a contiguous subinterval and independently computes its local integral contribution.

Given p processes indexed by r = 0, 1, ..., p-1:

- Local interval: [a_r, b_r] = [a + rΔ, a + (r+1)Δ]
- Interval width: Δ = (b-a)/p
- Local subintervals: n_r = n/p (approximately)

### 3.2 Load Balancing Considerations

Optimal performance requires equitable workload distribution among processes. Two primary scenarios merit consideration:

**Case 1: n divisible by p**
Each process receives exactly n/p subintervals, achieving perfect load balance.

**Case 2: n not divisible by p**
Let n = qp + r, where 0 ≤ r < p. The first r processes receive (q+1) subintervals, while remaining processes receive q subintervals:

```c
int local_n = n / num_procs;
int remainder = n % num_procs;

if (my_rank < remainder) {
    local_n++;
    local_start = my_rank * (local_n);
} else {
    local_start = my_rank * local_n + remainder;
}
```

### 3.3 MPI Implementation

```c
#include <mpi.h>
#include <stdio.h>
#include <math.h>

double f(double x) {
    return x * x;  // Example: f(x) = x²
}

double trapezoidal_local(double local_a, double local_b, int local_n) {
    double h = (local_b - local_a) / local_n;
    double result = (f(local_a) + f(local_b)) / 2.0;

    for (int i = 1; i < local_n; i++) {
        double x = local_a + i * h;
        result += f(x);
    }

    result *= h;
    return result;
}

int main(int argc, char** argv) {
    int my_rank, num_procs;
    double a = 0.0, b = 1.0;
    int n = 1000;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

    // Broadcast input parameters from root process
    if (my_rank == 0) {
        printf("Enter a, b, n: ");
        scanf("%lf %lf %d", &a, &b, &n);
    }

    MPI_Bcast(&a, 1, MPI_DOUBLE, 0, MPI_COMM_WORLD);
    MPI_Bcast(&b, 1, MPI_DOUBLE, 0, MPI_COMM_WORLD);
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

    // Calculate local interval bounds
    double local_a = a + my_rank * (b - a) / num_procs;
    double local_b = a + (my_rank + 1) * (b - a) / num_procs;
    int local_n = n / num_procs;

    // Adjust for remainder
    int remainder = n % num_procs;
    if (my_rank < remainder) {
        local_n++;
        local_a = a + my_rank * (b - a) * local_n / n;
        local_b = a + (my_rank + 1) * (b - a) * local_n / n;
    }

    // Compute local integral
    double local_integral = trapezoidal_local(local_a, local_b, local_n);

    // Reduce all local integrals to obtain global result
    double global_integral;
    MPI_Reduce(&local_integral, &global_integral, 1, MPI_DOUBLE,
               MPI_SUM, 0, MPI_COMM_WORLD);

    // Output result
    if (my_rank == 0) {
        double exact = (b*b*b - a*a*a) / 3.0;
        printf("Approximate integral: %.15f\n", global_integral);
        printf("Exact value: %.15f\n", exact);
        printf("Absolute error: %.15e\n", fabs(global_integral - exact));
    }

    MPI_Finalize();
    return 0;
}
```

## 4. Performance Analysis

### 4.1 Speedup and Parallel Efficiency

Let T_s represent serial execution time and T_p represent parallel execution time with p processes.

**Speedup:** S(p) = T_s / T_p

**Parallel Efficiency:** E(p) = S(p) / p = T_s / (p × T_p)

For the trapezoidal rule, the computational complexity is O(n), while communication complexity involves O(log p) for the reduction operation. Assuming function evaluation dominates computation:

T_s ≈ n × τ, where τ represents time per function evaluation
T_p ≈ (n/p) × τ + T_comm, where T_comm represents communication overhead

Thus:
S(p) ≈ nτ / [(n/p)τ + T_comm] = p / [1 + (pT_comm)/(nτ)]

**Ideal Speedup:** Achieved when T_comm << (n/p)τ, yielding S(p) ≈ p

**Communication Overhead Impact:** When T_comm becomes significant relative to computation, speedup saturates and efficiency decreases. This motivates the use of larger n values and minimization of communication frequency.

### 4.2 Scalability Analysis

Strong scaling maintains constant problem size while increasing process count. Weak scaling maintains constant work per process. For trapezoidal rule:

- Strong scaling efficiency decreases due to fixed communication overhead
- Weak scaling maintains efficiency when work increases proportionally with p

## 5. Comparative Analysis of Quadrature Methods

| Method              | Order    | Error Term    | Parallelizability | Implementation Complexity |
| ------------------- | -------- | ------------- | ----------------- | ------------------------- |
| Trapezoidal Rule    | O(h²)    | O(n⁻²)        | Excellent         | Low                       |
| Simpson's Rule      | O(h⁴)    | O(n⁻⁴)        | Good              | Medium                    |
| Gaussian Quadrature | O(h²ᵏ⁺¹) | Very High     | Poor              | High                      |
| Monte Carlo         | O(n⁻¹ᐟ²) | Probabilistic | Excellent         | Medium                    |

The trapezoidal rule's excellent parallelizability stems from its embarrassingly parallel nature—each subinterval computation proceeds independently, requiring only a final reduction operation for result aggregation.

## 6. Practical Numerical Example

Consider f(x) = x² integrated over [0, 1] using 4 processes with n = 8 subintervals:

- Exact integral: ∫₀¹ x² dx = 1/3 ≈ 0.3333333333
- h = 1/8 = 0.125

Process 0: [0, 0.25], n₀ = 2 subintervals
I₀ = (0.125/2)[f(0) + 2f(0.125) + f(0.25)] = 0.015625

Process 1: [0.25, 0.5], n₁ = 2 subintervals  
I₁ = 0.046875

Process 2: [0.5, 0.75], n₂ = 2 subintervals
I₂ = 0.078125

Process 3: [0.75, 1.0], n₃ = 2 subintervals
I₃ = 0.109375

Total: I = 0.25 (error ≈ 0.0833 due to coarse discretization)

Increasing to n = 1000 yields error < 10⁻⁶, demonstrating rapid convergence.

## 7. Advanced Optimization Techniques

### 7.1 Vectorization

Modern processors support SIMD (Single Instruction Multiple Data) operations. Compiler directives such as `#pragma omp simd` enable automatic vectorization of the function evaluation loop, processing multiple points simultaneously.

### 7.2 Hybrid Parallelism

Combining MPI (inter-node) with OpenMP (intra-node) achieves optimal resource utilization:

```c
#pragma omp parallel for schedule(static)
for (int i = 1; i < local_n; i++) {
    // Parallel function evaluations within node
}
```

### 7.3 Non-blocking Communication

Overlapping computation with communication using MPI_Isend/MPI_Irecv improves pipeline efficiency in large-scale deployments.

## 8. Summary

The parallel implementation of the trapezoidal rule using MPI exemplifies the principles of domain decomposition in scientific computing. The method's embarrassingly parallel nature enables near-linear speedup for sufficiently large problem sizes. Key takeaways include: the error bound derivation establishing O(n⁻²) convergence; domain decomposition strategies ensuring load balance; performance analysis quantifying speedup limitations due to communication overhead; and comparative analysis positioning trapezoidal rule as the optimal choice when parallel efficiency is paramount.
