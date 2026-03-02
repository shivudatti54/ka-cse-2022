# Loop-Carried Dependencies in OpenMP

## 1. Introduction to Loop Parallelism

OpenMP (Open Multi-Processing) provides a directive-based API for shared-memory parallel programming in C/C++ and Fortran. The `#pragma omp parallel for` directive enables the distribution of loop iterations across multiple threads, facilitating concurrent execution and potential performance gains. However, the safe parallelization of loops requires careful analysis of data dependencies that may exist between iterations.

## 2. Theoretical Foundation of Loop-Carried Dependencies

### 2.1 Formal Definition

A **loop-carried dependency** exists in a loop when an iteration `i` (where `0 ≤ i < N`) accesses a memory location that was modified by some other iteration `j` (where `j ≠ i`), and at least one of these accesses is a write operation. This dependency creates a partial ordering constraint that must be preserved during execution.

**Mathematical Formulation:**

Let `S₁` and `S₂` be two statements within a loop, and let `I` and `J` represent iteration indices. A loop-carried dependency exists if and only if:

1. There exists a pair of iterations `(i, j)` such that `i` ≠ `j`
2. Both `S₁(i)` and `S₂(j)` access the same memory location `M`
3. At least one of these accesses is a write operation

### 2.2 Classification of Dependencies: Bernstein's Conditions

Bernstein's conditions provide a formal framework for determining whether two statements can execute in parallel. Let `R₁` and `W₁` denote the sets of memory locations read and written by statement `S₁` respectively, with similar notation for `S₂`.

**Bernstein's Conditions for Parallel Execution:**

Two statements `S₁` and `S₂` can execute in parallel (in either order) without interference if and only if:

- **Independence Condition:** `W₁ ∩ R₂ = ∅` (no flow dependency)
- **Anti-dependency Condition:** `R₁ ∩ W₂ = ∅` (no anti-dependency)
- **Output Dependency Condition:** `W₁ ∩ W₂ = ∅` (no output dependency)

If any of these conditions are violated, a dependency exists that prevents parallel execution.

### 2.3 Dependency Distance and Direction Vectors

The **dependency distance** `δ` is defined as the difference between the iteration indices: `δ = j - i`. The **dependency direction** characterizes the nature of this distance:

- **Forward dependency (flow):** `j < i` (iteration `j` must complete before iteration `i`)
- **Backward dependency:** `j > i` (iteration order must be reversed)
- **Loop-independent dependency:** `j = i` (dependency exists within the same iteration)

A loop is **parallelizable** if and only if all loop-carried dependencies have distance `δ = 0` (i.e., they are loop-independent).

## 3. Types of Dependencies in Loop Parallelization

### 3.1 Flow Dependency (Read-After-Write - RAW)

A flow dependency occurs when iteration `i` reads a value that was written by a previous iteration `j < i`. This represents a true data dependence that cannot be violated.

**Example: Recurrence Relation**

```c
for (int i = 1; i < N; i++) {
    a[i] = a[i-1] * 2 + b[i];  // a[i] depends on a[i-1]
}
```

**Proof of Non-Parallelizability:**

Assume parallel execution of iterations `i` and `i-1`. Let `a[i-1]` be updated at time `t₁` and `a[i]` be read at time `t₂`. If `t₂ < t₁`, the computation uses an stale value, producing incorrect results. Therefore, iteration `i` must wait for iteration `i-1` to complete, proving the loop cannot be parallelized.

### 3.2 Anti-Dependency (Write-After-Read - WAR)

An anti-dependency occurs when iteration `i` writes to a location that was previously read by iteration `j < i`. This is also known as a "write-after-read" hazard.

**Example:**

```c
for (int i = 0; i < N-1; i++) {
    x = a[i];       // Read phase
    a[i+1] = x + 1; // Write phase - depends on read in iteration i
}
```

### 3.3 Output Dependency (Write-After-Write - WAW)

An output dependency exists when multiple iterations write to the same memory location. The final value depends on the execution order of iterations.

**Example:**

```c
int result = 0;
for (int i = 0; i < N; i++) {
    result = compute(array[i]); // All iterations write to 'result'
    output[i] = result;
}
```

## 4. Dependency Analysis Techniques

### 4.1 The GCD Test for Affine Dependencies

For loops with affine array subscripts of the form `a[c₁*i + c₀]`, the **GCD (Greatest Common Divisor) test** provides a necessary condition for dependency existence.

**Theorem:** A loop-carried dependency exists between iterations `i` and `j` (i ≠ j) for array accesses `a[p*i + q]` and `a[r*j + s]` if and only if:

1. `p*i + q = r*j + s` (same memory location)
2. `GCD(r, p)` divides `(s - q)`

**Example Analysis:**

```c
for (int i = 0; i < N; i++) {
    a[2*i] = a[2*i + 1] + 1;
}
```

Here, `p = 2, q = 0` (write) and `r = 2, s = 1` (read). The GCD is `GCD(2, 2) = 2`. Since `2` does not divide `(1 - 0) = 1`, no dependency exists, and this loop is parallelizable.

## 5. Strategies for Resolving Loop-Carried Dependencies

### 5.1 The Reduction Clause

For accumulation patterns (WAW dependencies on reduction variables), OpenMP provides the `reduction` clause:

```c
int sum = 0;
#pragma omp parallel for reduction(+:sum)
for (int i = 0; i < N; i++) {
    sum += array[i];
}
```

**Implementation Mechanism:** The compiler creates a private copy of `sum` for each thread. Each thread performs local accumulation, and the partial results are combined using the specified operator (`+` in this case) at the end of the parallel region.

### 5.2 Privatization

Making shared variables private eliminates WAR and WAW dependencies:

```c
#pragma omp parallel for
for (int i = 0; i < N; i++) {
    int temp = array[i];  // Private variable
    // Computation using temp
}
```

### 5.3 Loop Distribution (Loop Splitting)

Separating independent statements into distinct loops:

```c
// Original: Cannot parallelize due to dependency
for (int i = 0; i < N; i++) {
    a[i] = b[i] * 2;
    c[i] = a[i-1] + 1;  // Depends on previous iteration
}

// Transformed: First loop parallelizable
#pragma omp parallel for
for (int i = 0; i < N; i++) {
    a[i] = b[i] * 2;
}

// Sequential loop (dependent)
for (int i = 0; i < N; i++) {
    c[i] = a[i-1] + 1;
}
```

### 5.4 Algorithmic Transformation: Parallel Prefix Sum

For recurrences like `a[i] = a[i-1] + b[i]`, use a parallel algorithm:

```c
// Sequential: O(N)
// Parallel (Hillis-Steele): O(log N) with N processors
void parallel_prefix_sum(int* a, int n) {
    int stride = 1;
    for (int k = 0; k < log2(n); k++) {
        #pragma omp parallel for
        for (int i = stride; i < n; i++) {
            a[i] += a[i - stride];
        }
        stride *= 2;
    }
}
```

### 5.5 The Ordered Construct

For loops requiring sequential execution of specific iterations:

```c
#pragma omp parallel for ordered
for (int i = 0; i < N; i++) {
    // Some parallel computation
    #pragma omp ordered
    {
        // Sequential execution ordered by i
        output[i] = process(data[i]);
    }
}
```

**Note:** The `ordered` construct significantly impacts performance and should be used sparingly.

## 6. Summary and Best Practices

Loop-carried dependencies represent the fundamental limitation on loop parallelization in OpenMP. The presence of flow, anti, or output dependencies creates ordering constraints that must be preserved. Key takeaways include:

1. **Identification:** Use Bernstein's conditions and the GCD test to formally analyze dependencies
2. **Transformation:** Apply techniques such as reduction, privatization, and loop distribution
3. **Algorithmic Change:** For complex dependencies, consider fundamentally different parallel algorithms
4. **Caution:** Synchronization mechanisms (`critical`, `atomic`, `ordered`) should be last resorts due to performance overhead

Understanding and properly handling loop-carried dependencies is essential for developing efficient parallel programs in OpenMP.
