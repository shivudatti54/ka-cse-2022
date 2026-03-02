# Shared-Memory Programming with OpenMP – Pragmas and Directives

## 1. Introduction and Execution Model

OpenMP (Open Multi-Processing) is an application programming interface (API) that facilitates shared-memory parallel programming in C, C++, and Fortran. It employs compiler directives (pragmas) embedded within sequential code to specify parallel regions, enabling incremental parallelization without complete code restructuring. Given the ubiquity of multicore processors in contemporary computing environments, proficiency in OpenMP represents an essential skill for software developers seeking to harness thread-level parallelism.

The architecture of modern computational systems increasingly relies on symmetric multiprocessing (SMP) models where multiple processor cores share a common memory space. OpenMP is specifically designed for such shared-memory architectures, allowing threads to access global variables directly without the overhead of message passing.

### 1.1 The Fork-Join Parallel Execution Model

OpenMP implements the **fork-join** parallel execution model, which represents a fundamental paradigm in parallel computing:

- **Fork Phase**: When the master thread encounters a parallel region directive, it spawns a team of worker threads. The number of threads created may be predetermined or dynamically adjusted based on runtime configuration.

- **Parallel Execution Phase**: All threads in the team execute the code within the parallel region concurrently. Each thread possesses a unique thread identifier (`thread_num`) ranging from 0 to `num_threads-1`.

- **Join Phase**: Upon completion of the parallel region, all threads synchronize at an implicit barrier. Worker threads terminate or become idle, and execution returns to the master thread.

**Mathematical Representation**: If $T_1$ denotes the sequential execution time and $T_p$ denotes the parallel execution time with $p$ threads, the **speedup** $S$ is defined as:
$$S(p) = \frac{T_1}{T_p}$$

The **parallel efficiency** is given by:
$$E(p) = \frac{S(p)}{p} = \frac{T_1}{p \cdot T_p}$$

Ideally, for perfectly parallelizable workloads, we achieve linear speedup ($S(p) = p$) and efficiency $E(p) = 1$. In practice, efficiency is reduced by synchronization overhead, load imbalance, and memory contention.

---

## 2. Fundamental Pragmas and Directives

### 2.1 The Parallel Region Directive

The `#pragma omp parallel` directive creates a parallel region and spawns a team of threads:

```c
#pragma omp parallel [clause[[,] clause] ...]
{
    // Parallel region body executed by all threads
}
```

**Syntax of Clauses**:

- `num_threads(integer-expression)`: Specifies exact number of threads
- `default(shared | none)`: Defines default data sharing attribute
- `shared(list)`: Declares shared variables
- `private(list)`: Declares private variables
- `firstprivate(list)`: Like private but initializes with parent's value

**Example with Multiple Clauses**:

```c
int shared_var = 10;
int private_var = 5;

#pragma omp parallel default(none) shared(shared_var) private(private_var)
{
    int tid = omp_get_thread_num();
    private_var = tid * 2;  // Each thread has independent copy
    printf("Thread %d: private_var = %d, shared_var = %d\n",
           tid, private_var, shared_var);
}
```

### 2.2 Thread Identification Functions

```c
int omp_get_thread_num(void);  // Returns thread ID (0 to N-1)
int omp_get_num_threads(void); // Returns total thread count
```

---

## 3. Data Sharing Attributes

Understanding variable scope is critical for correct parallel programming. Variables may exhibit **shared** or **private** lifetime:

### 3.1 Shared Variables

By default, the following variables are shared:

- Global variables (file-scope)
- Static variables
- Heap-allocated memory (pointers)

All threads access the same memory location, requiring synchronization for write operations.

### 3.2 Private Variables

The `private` clause creates a new instance of each variable for each thread:

```c
int x = 10;

#pragma omp parallel for private(x)
for (int i = 0; i < N; i++) {
    x = i;  // Each thread has independent x
    result[i] = compute(x);
}
// Original x is undefined after parallel region (unspecified)
```

### 3.3 Firstprivate and Lastprivate

- **firstprivate**: Initializes private copies with the value from the master thread
- **lastprivate**: Copies the last iteration's value back to the original variable

```c
int counter = 100;

#pragma omp parallel for firstprivate(counter) lastprivate(counter)
for (int i = 0; i < 4; i++) {
    counter++;
    printf("Thread %d: counter = %d\n", omp_get_thread_num(), counter);
}
printf("Final counter = %d\n", counter);  //counter = 104 (with lastprivate)
```

---

## 4. Work-Sharing Constructs

### 4.1 The For Loop Directive

The `#pragma omp for` distributes loop iterations across threads:

```c
#pragma omp parallel
{
    #pragma omp for
    for (int i = 0; i < N; i++) {
        a[i] = b[i] + c[i];
    }
}
```

**Combined Parallel For**:

```c
#pragma omp parallel for
for (int i = 0; i < N; i++) {
    a[i] = b[i] + c[i];
}
```

### 4.2 The Sections Directive

For non-iterative work distribution:

```c
#pragma omp parallel sections
{
    #pragma omp section
    {
        task_a();
    }
    #pragma omp section
    {
        task_b();
    }
    #pragma omp section
    {
        task_c();
    }
}
```

Each section executes exactly once by one thread.

---

## 5. Scheduling Policies

The `schedule` clause determines how iterations are distributed:

### 5.1 Static Scheduling

```c
#pragma omp parallel for schedule(static, chunk_size)
```

- Iterations divided into equal chunks at compile time
- Minimal runtime overhead
- Optimal for balanced workloads

### 5.2 Dynamic Scheduling

```c
#pragma omp parallel for schedule(dynamic, chunk_size)
```

- Threads grab chunks at runtime
- Better for unbalanced workloads
- Higher overhead but improved load balancing

### 5.3 Guided Scheduling

```c
#pragma omp parallel for schedule(guided, chunk_size)
```

- Chunk size decreases exponentially
- Adaptive to workload characteristics

**Performance Analysis**: For a loop with $N$ iterations and $p$ threads:

- Static: $\lfloor N/p \rfloor$ iterations per thread (deterministic)
- Dynamic: Overhead of $O(N/chunk)$ synchronization points
- Guided: Combines benefits, reduces overhead for large $N$

---

## 6. The Reduction Clause

The reduction clause provides a thread-safe mechanism for accumulation operations:

### 6.1 Syntax and Semantics

```c
#pragma omp parallel for reduction(<operator>:variable-list)
for (int i = 0; i < N; i++) {
    sum += f(i);
}
```

**Formal Definition**: The reduction clause performs:

1. **Initialization**: Each thread receives a private copy initialized to the identity value
2. **Local Computation**: Each thread computes partial result
3. **Reduction**: Partial results are combined using the specified operator

**Supported Operators**: `+`, `-`, `*`, `&`, `|`, `^`, `&&`, `||`, `min`, `max`

### 6.2 Numerical Integration Example (Trapezoidal Rule)

```c
double trapezoidal(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.0;

    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < n; i++) {
        double x_i = a + i * h;
        double x_ip1 = a + (i + 1) * h;
        sum += (f(x_i) + f(x_ip1)) * h / 2.0;
    }
    return sum;
}
```

**Proof of Correctness**: The parallel reduction computes $\sum_{i=0}^{n-1} \frac{(f(x_i) + f(x_{i+1}))h}{2}$, which is mathematically equivalent to the sequential computation due to the associative property of floating-point addition (ignoring rounding errors).

### 6.3 Matrix Addition with Collapse

```c
void matrix_add(int n, double A[][], double B[][], double C[][]) {
    #pragma omp parallel for collapse(2)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
}
```

The `collapse(2)` clause flattens both loop dimensions, distributing $n^2$ iterations across threads.

---

## 7. Synchronization Directives

### 7.1 Critical Section

Ensures exclusive access to shared resources:

```c
#pragma omp critical
{
    shared_counter += local_value;
}
```

### 7.2 Atomic Directive

More efficient than critical for single updates:

```c
#pragma omp atomic
    counter++;
```

### 7.3 Barrier Directive

Explicit synchronization point:

```c
#pragma omp barrier
```

### 7.4 Nowait Clause

Removes implicit barrier:

```c
#pragma omp parallel
{
    #pragma omp for nowait
    for (int i = 0; i < N; i++) {
        process_a(i);
    }
    #pragma omp for
    for (int i = 0; i < M; i++) {
        process_b(i);
    }
}
```

---

## 8. Advanced Constructs

### 8.1 Tasking

Explicit task creation with dependencies:

```c
#pragma omp parallel
{
    #pragma omp single
    {
        #pragma omp task
        process_node(node->left);

        #pragma omp task
        process_node(node->right);
    }
}
```

### 8.2 Task Dependencies

```c
#pragma omp task depend(in: A) process_A();
#pragma omp task depend(in: B) process_B();
#pragma omp task depend(out: C) process_C();  // Waits for A and B
```

### 8.3 Threadprivate Directive

```c
static int thread_counter;

#pragma omp threadprivate(thread_counter)
```

---

## 9. Performance Considerations

### 9.1 False Sharing

When threads modify adjacent memory locations, cache line invalidation occurs:

**Solution**: Padding to cache line size (typically 64 bytes):

```c
struct padded_counter {
    long counter;
    char padding[64 - sizeof(long)];
};
```

### 9.2 Load Balancing

For irregular workloads, prefer dynamic or guided scheduling:

```c
// Unbalanced workload
#pragma omp parallel for schedule(dynamic, 10)
for (int i = 0; i < N; i++) {
    variable_work(i);
}
```

---

## 10. Environment Variables

| Variable          | Description                      |
| ----------------- | -------------------------------- |
| `OMP_NUM_THREADS` | Maximum thread count             |
| `OMP_SCHEDULE`    | Default scheduling policy        |
| `OMP_DYNAMIC`     | Enable dynamic thread adjustment |
| `OMP_NESTED`      | Enable nested parallelism        |

---

## 11. Comprehensive Examples

### Example 1: Parallel Hello World

```c
#include <omp.h>
#include <stdio.h>

int main() {
    #pragma omp parallel num_threads(4)
    {
        int tid = omp_get_thread_num();
        printf("Thread %d: Hello, World!\n", tid);
    }
    return 0;
}
```

### Example 2: Parallel Reduction for Dot Product

```c
double dot_product(double *a, double *b, int n) {
    double sum = 0.0;

    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < n; i++) {
        sum += a[i] * b[i];
    }
    return sum;
}
```

### Example 3: Mandelbrot Set Computation

```c
void compute_mandelbrot(int width, int height, int max_iter,
                        int output[width][height]) {
    #pragma omp parallel for collapse(2) schedule(dynamic)
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            output[y][x] = mandelbrot_point(x, y, max_iter);
        }
    }
}
```

---

## 12. Common Pitfalls and Best Practices

1. **Race Conditions**: Multiple threads writing to shared variables without synchronization
2. **Missing Synchronization**: Forgetting implicit barriers in work-sharing constructs
3. **Incorrect Data Sharing**: Using shared variables in private contexts inappropriately
4. **Excessive Parallelization**: Overhead exceeds benefits for small workloads
5. **Memory Contention**: Multiple threads accessing same memory location frequently

---
