# Trapezoidal Rule in MPI

## Introduction to Numerical Integration

Numerical integration, also called quadrature, is a fundamental technique in computational mathematics used to approximate definite integrals when an analytical solution is difficult or impossible to obtain. The trapezoidal rule is one of the simplest and most widely used numerical integration methods.

The trapezoidal rule approximates the area under a curve by dividing it into trapezoids rather than rectangles (as in the Riemann sum). For a function f(x) defined on the interval [a, b], the formula is:

```
∫[a,b] f(x)dx ≈ (b-a)/2n * [f(x₀) + 2f(x₁) + 2f(x₂) + ... + 2f(xₙ₋₁) + f(xₙ)]
```

where n is the number of subintervals and x₀ = a, x₁ = a + h, x₂ = a + 2h, ..., xₙ = b, with h = (b-a)/n.

## Parallelizing the Trapezoidal Rule with MPI

### Why Parallelize Numerical Integration?

Numerical integration often requires substantial computational resources, especially when:
- High precision is needed (large n)
- The function f(x) is computationally expensive to evaluate
- Multiple integrals need to be computed

MPI (Message Passing Interface) provides a standardized approach to parallelize such computations across distributed memory systems, allowing us to divide the work among multiple processes.

### Basic Parallelization Strategy

The parallelization strategy for the trapezoidal rule involves:

1. **Domain decomposition**: Dividing the integration interval [a, b] among available processes
2. **Local computation**: Each process computes its portion of the integral using the trapezoidal rule
3. **Result aggregation**: Combining partial results from all processes to get the final integral value

```
Process 0: [a, a + h]   → Compute local integral I₀
Process 1: [a + h, a + 2h] → Compute local integral I₁
...
Process p-1: [a + (p-1)h, b] → Compute local integral Iₙ₋₁
```

### MPI Implementation Details

#### Process Initialization

```c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    int my_rank, num_procs;
    
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);
```

#### Domain Decomposition

Each process calculates its local integration bounds:

```c
double local_a = a + my_rank * (b - a) / num_procs;
double local_b = a + (my_rank + 1) * (b - a) / num_procs;
```

#### Local Computation Function

```c
double trapezoidal_rule(double local_a, double local_b, int local_n, 
                       double (*f)(double)) {
    double h = (local_b - local_a) / local_n;
    double integral = (f(local_a) + f(local_b)) / 2.0;
    
    for (int i = 1; i < local_n; i++) {
        double x = local_a + i * h;
        integral += f(x);
    }
    
    integral *= h;
    return integral;
}
```

#### Collective Communication for Result Aggregation

```c
double local_integral = trapezoidal_rule(local_a, local_b, local_n, f);
double total_integral;

MPI_Reduce(&local_integral, &total_integral, 1, MPI_DOUBLE, 
           MPI_SUM, 0, MPI_COMM_WORLD);
```

#### Complete Program Structure

```c
if (my_rank == 0) {
    // Read input values: a, b, n
}

MPI_Bcast(&a, 1, MPI_DOUBLE, 0, MPI_COMM_WORLD);
MPI_Bcast(&b, 1, MPI_DOUBLE, 0, MPI_COMM_WORLD);
MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

// Each process computes its local integral
double local_integral = compute_local_integral(a, b, n, num_procs, my_rank, f);

// Reduce all local integrals to get the total
MPI_Reduce(&local_integral, &total_integral, 1, MPI_DOUBLE, 
           MPI_SUM, 0, MPI_COMM_WORLD);

if (my_rank == 0) {
    printf("Approximate integral: %.15f\n", total_integral);
}

MPI_Finalize();
```

## Advanced Considerations

### Load Balancing

For optimal performance, ensure each process has approximately the same amount of work:

```
Equal work distribution: Each process gets (b-a)/num_procs interval
```

### Error Analysis

The trapezoidal rule has an error term of O(h²), meaning that doubling the number of subintervals reduces the error by a factor of 4.

### Handling Uneven Divisions

When n is not evenly divisible by the number of processes:

```c
int local_n = n / num_procs;
int remainder = n % num_procs;

if (my_rank < remainder) {
    local_n++;
}
```

### Performance Optimization Techniques

1. **Vectorization**: Use SIMD instructions for function evaluations
2. **Overlapping computation and communication**: Use non-blocking operations
3. **Hybrid programming**: Combine MPI with OpenMP for intra-node parallelism

## Comparison of Integration Methods

| Method | Accuracy | Parallelizability | Implementation Complexity |
|--------|----------|-------------------|----------------------------|
| Trapezoidal Rule | O(h²) | Excellent | Low |
| Simpson's Rule | O(h⁴) | Good | Medium |
| Gaussian Quadrature | Very High | Poor | High |
| Monte Carlo | O(1/√n) | Excellent | Medium |

## Practical Example: Integrating f(x) = x²

Let's consider integrating f(x) = x² from 0 to 1 with 4 processes:

```
Exact solution: ∫[0,1] x² dx = 1/3 ≈ 0.333333

Process 0: [0, 0.25] → I₀ = 0.005208
Process 1: [0.25, 0.5] → I₁ = 0.036458
Process 2: [0.5, 0.75] → I₂ = 0.088542
Process 3: [0.75, 1.0] → I₃ = 0.161458

Total ≈ 0.291667 (with large error due to small n)
```

As n increases, the approximation improves significantly.

## ASCII Diagram: Parallel Trapezoidal Rule Execution

```
Master Process (Rank 0)
┌─────────────────────────────────────────────────┐
│ Initialize MPI                                  │
│ Read input parameters: a, b, n                 │
│ Broadcast parameters to all processes          │
│ Compute local integral for segment [0, 0.25]   │
│ Receive partial results from other processes   │
│ Sum all partial results                        │
│ Print final integral value                     │
│ Finalize MPI                                   │
└─────────────────────────────────────────────────┘
          ↑               ↑               ↑
          │               │               │
          ↓               ↓               ↓
Worker 1 (Rank 1)   Worker 2 (Rank 2)   Worker 3 (Rank 3)
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Receive a,b,n│     │ Receive a,b,n│     │ Receive a,b,n│
│ Compute [0.25,0.5]│ │ Compute [0.5,0.75]│ │ Compute [0.75,1.0] │
│ Send result to 0  │ │ Send result to 0  │ │ Send result to 0  │
└─────────────┘     └─────────────┘     └─────────────┘
```

## Common Pitfalls and Solutions

1. **Floating-point precision errors**: Use double precision and be mindful of cancellation errors
2. **Incorrect domain decomposition**: Ensure boundaries are calculated precisely
3. **Load imbalance**: Consider dynamic scheduling for irregular functions
4. **Communication overhead**: Minimize data transfer between processes

## Real-World Applications

1. **Physics**: Calculating work done, electric fields, gravitational potential
2. **Finance**: Option pricing, risk analysis
3. **Engineering**: Stress analysis, fluid dynamics
4. **Machine Learning**: Bayesian inference, expectation calculations

## Exam Tips

1. **Remember the formula**: The trapezoidal rule formula is essential for both implementation and error analysis
2. **Understand MPI collective operations**: MPI_Reduce and MPI_Bcast are crucial for this algorithm
3. **Consider edge cases**: What happens when n is not divisible by the number of processes?
4. **Analyze complexity**: The parallel time complexity is O(n/p + log p) where p is the number of processes
5. **Compare with other methods**: Be prepared to compare trapezoidal rule with Simpson's rule and other integration techniques
6. **Error analysis**: Understand how the error decreases as n increases and how parallelization affects accuracy