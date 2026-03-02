# The Trapezoidal Rule in MPI

=====================================

### Overview

The trapezoidal rule is a numerical integration method that approximates a definite integral by dividing the area under a curve into trapezoids. In MPI, the integration interval [a, b] is decomposed among processes, each computes a local integral, and results are aggregated using MPI_Reduce. This is a classic example of parallelizing embarrassingly parallel computations.

### Key Points

- **Trapezoidal Formula:** Integral[a,b] f(x)dx ~ (h/2)[f(x0) + 2f(x1) + ... + 2f(x_{n-1}) + f(xn)], where h = (b-a)/n
- **Domain Decomposition:** Each process gets local_a = a + rank*(b-a)/p and local_b = a + (rank+1)*(b-a)/p
- **Local Computation:** Each process computes trapezoidal rule on its subinterval independently
- **MPI_Bcast:** Broadcasts input parameters (a, b, n) from root to all processes
- **MPI_Reduce with MPI_SUM:** Aggregates local integrals into a global result at root
- **Error Term:** O(h^2); doubling n reduces error by a factor of 4
- **Parallel Time Complexity:** O(n/p + log p) where p is the number of processes

### Important Concepts

- local_n = n / num_procs handles subinterval count per process
- When n is not evenly divisible by p, extra subintervals are distributed to the first (n % p) processes
- MPI_Bcast distributes parameters; MPI_Reduce combines results -- these are the key communication steps
- Comparison: Trapezoidal O(h^2) vs Simpson's O(h^4) vs Monte Carlo O(1/sqrt(n))

### Notes

- Floating-point precision errors can accumulate; use double precision
- Ensure local boundaries are calculated precisely to avoid gaps or overlaps
- The communication overhead (Bcast + Reduce) is minimal compared to computation for large n
- Be able to write the complete MPI trapezoidal rule program from scratch for exams
