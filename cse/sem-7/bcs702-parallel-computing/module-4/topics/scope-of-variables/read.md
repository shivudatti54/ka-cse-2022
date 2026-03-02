# Scope of Variables in OpenMP

## Introduction

In shared-memory parallel programming with OpenMP, variable scope represents one of the most critical design decisions a programmer must make. The **scope** (or **data-sharing attribute**) of a variable determines three fundamental properties: (1) which threads can access the variable, (2) whether accesses occur to a single memory location or to thread-local copies, and (3) whether synchronization is required to ensure correctness.

Incorrect specification of variable scope constitutes the primary source of bugs in OpenMP programs, manifesting as **race conditions**, **data corruption**, **non-deterministic results**, or **undefined behavior**. Understanding the OpenMP memory model and formal data-sharing rules is therefore essential for developing correct parallel applications.

## The OpenMP Memory Model

OpenMP employs a **shared-memory consistency model** where the memory hierarchy typically consists of a shared main memory accessible by all threads, with each thread possessing private caches. The consistency model guarantees that:

1. At a **synchronization point**, all threads observe a consistent view of shared variables.
2. Between synchronization points, reads and writes to shared variables may be reordered by the compiler and hardware, leading to **data races** if multiple threads access the same memory location without synchronization, and at least one access is a write.

### Definition: Data Race

According to the OpenMP specification, a **data race** occurs when two threads simultaneously access the same memory location, where at least one access is a write, and no synchronization mechanism (critical section, atomic operation, or explicit barrier) orders these accesses. The behavior of a program containing a data race is **undefined**—the program may produce different results across executions, platforms, or optimization levels.

**Theorem (Correctness of Synchronized Access)**: If all accesses to a shared variable $V$ are protected by synchronization primitives (critical sections, atomic operations, or barriers), then the program produces deterministic results independent of thread scheduling.

_Proof_: Synchronization primitives establish a **happens-before** relationship between conflicting accesses. By the OpenMP memory model, this total ordering ensures that each read observes either the initial value or a value written by a preceding write, eliminating conflicting concurrent modifications. $\square$

## Classification of Variable Scope

### 1. Shared Variables

A **shared** variable resides at a single memory address accessible by all threads in the team. All reads and writes operate on this identical location, requiring explicit synchronization for write operations.

**Formal Definition**: A variable $V$ is shared if $\forall$ threads $t_i, t_j \in T$, the address $\&V_{t_i} = \&V_{t_j}$ (identical memory address).

**Characteristics**:

- Single storage location in memory
- All threads access the same physical address
- Write accesses require synchronization (critical, atomic, or ordered constructs)
- Default for variables declared outside parallel regions

**Example with Race Condition Analysis**:

```c
#include <stdio.h>
#include <omp.h>

int main() {
    int counter = 0;

    #pragma omp parallel num_threads(4)
    {
        // UNSAFE: Multiple threads execute this simultaneously
        counter = counter + 1;  // Read-modify-write without synchronization
    }

    printf("Final counter: %d\n", counter);
    return 0;
}
```

**Timing Diagram (Demonstrating Race Condition)**:

```
Thread 0:    READ(counter=0) → COMPUTE(1) → WRITE(counter=1)
Thread 1:    READ(counter=0) → COMPUTE(1) → WRITE(counter=1)  [race!]
Thread 2:    READ(counter=1) → COMPUTE(2) → WRITE(counter=2)
Thread 3:    READ(counter=2) → COMPUTE(3) → WRITE(counter=3)
```

In the worst case, the final value may be 1, 2, 3, or 4 depending on thread interleaving—demonstrating **non-deterministic behavior** due to the data race.

### 2. Private Variables

A **private** variable creates an independent copy for each thread. The original variable's address is not accessible within the parallel region; instead, each thread operates on its private copy.

**Formal Definition**: A variable $V$ is private if $\forall$ threads $t_i, t_j \in T$, $t_i \neq t_j \implies \&V_{t_i} \neq \&V_{t_j}$ (distinct memory addresses), where $V_{t_i}$ denotes thread $t_i$'s private copy.

**Characteristics**:

- Separate storage per thread (typically in thread-local storage or stack)
- No synchronization required—each thread has exclusive access
- Initial value of private copies is **undefined** (unless firstprivate is used)
- Value of original variable after region is **undefined** (unless lastprivate is used)
- Default for variables declared inside parallel regions

**Example**:

```c
#include <stdio.h>
#include <omp.h>

int main() {
    int local_id;

    #pragma omp parallel private(local_id)
    {
        local_id = omp_get_thread_num();  // Each thread writes to its private copy
        printf("Thread %d: local_id = %d\n", omp_get_thread_num(), local_id);
    }

    // Original local_id has undefined value here
    return 0;
}
```

### 3. Thread-Local Variables (threadprivate)

The `threadprivate` directive extends private storage across multiple parallel regions, maintaining the same private copy for a thread across the program's lifetime.

**Characteristics**:

- Storage persists across parallel regions
- Each thread retains its value between parallel sections
- Cannot be used inside parallel regions (unlike private)
- Performance implication: avoids re-initialization overhead

```c
#include <stdio.h>
#include <omp.h>

int counter;  // Global variable
#pragma omp threadprivate(counter)

int main() {
    #pragma omp parallel
    {
        counter = omp_get_thread_num();
        printf("Region 1 - Thread %d: counter = %d\n", omp_get_thread_num(), counter);
    }

    #pragma omp parallel
    {
        // Each thread retains its previous value
        printf("Region 2 - Thread %d: counter = %d\n", omp_get_thread_num(), counter);
    }
    return 0;
}
```

## Data-Sharing Attribute Clauses

OpenMP provides explicit clauses to override default scoping rules.

### Syntax Overview

```c
#pragma omp parallel [clauses]
{
    // parallel region
}
```

Where clauses include: `shared(list)`, `private(list)`, `firstprivate(list)`, `lastprivate(list)`, `default(none | shared)`, `reduction(operator:list)`

### Detailed Clause Specifications

#### (a) `private(list)`

Creates thread-local copies of listed variables. The initial value of private copies is **indeterminate** (garbage values).

```c
int x = 10;
#pragma omp parallel private(x)
{
    x = omp_get_thread_num();  // Private copy initialized to undefined value
    printf("Thread %d: x = %d\n", omp_get_thread_num(), x);
}
// Original x remains 10 (unchanged)
```

**Use Case**: Variables that accumulate intermediate results within a parallel region.

#### (b) `firstprivate(list)`

Identical to `private` except each thread's copy is initialized with the value of the original variable from the enclosing context.

```c
int x = 42;
#pragma omp parallel firstprivate(x)
{
    x += omp_get_thread_num();  // Each thread's x starts at 42
    printf("Thread %d: x = %d\n", omp_get_thread_num(), x);
}
// Original x remains 42
```

**Mathematical Specification**: $\forall$ thread $t$, $x_t^{initial} = x^{original}$

#### (c) `lastprivate(list)`

Variables in `lastprivate` maintain private copies during execution, and the original variable is updated with the value from the **last iteration** (in `for` constructs) or **last section** (in `sections` constructs).

```c
int result;
#pragma omp parallel for lastprivate(result)
for (int i = 0; i < 10; i++) {
    result = i;  // Each iteration updates its private copy
}
// result = 9 (value from i=9, the last iteration)
```

**Theorem (Lastprivate Correctness)**: For a loop with iterations $I = \{i_0, i_1, ..., i_{n-1}\}$ executed sequentially, if $V_{last}$ is the value of variable $V$ at iteration $i_{n-1}$, then after the parallel for construct, the original variable $V$ equals $V_{last}$.

#### (d) `shared(list)`

Explicitly declares variables as shared. Primarily used for documentation clarity, as this is the default for outer-scope variables.

```c
int buffer[1000];
#pragma omp parallel shared(buffer)
{
    int tid = omp_get_thread_num();
    // ... operations on shared buffer
}
```

#### (e) `default(none | shared)`

The `default` clause controls implicit scoping:

- `default(shared)`: Variables outside the parallel region are shared (default behavior)
- `default(none)`: **Forces explicit specification** for every variable used within the parallel region

```c
int a = 5, b = 10, c;
#pragma omp parallel default(none) shared(a, b) private(c)
{
    c = a + b + omp_get_thread_num();  // Compiler error if any variable unspecified
}
```

**Best Practice**: Use `default(none)` to prevent inadvertent sharing bugs. This forces the programmer to consciously decide the scope of each variable.

#### (f) `reduction(operator:list)`

The **reduction** clause provides a thread-safe mechanism for combining results from all threads. Each thread maintains a private copy initialized to the **identity value**, and private copies are combined using the specified operator at a synchronization point.

| Operator | Identity Value  | Operator | Identity Value |
| -------- | --------------- | -------- | -------------- | --- |
| `+`      | 0               | `*`      | 1              |
| `-`      | 0               | `min`    | INFINITY       |
| `&`      | ~0 (all bits 1) | `        | `              | 0   |
| `^`      | 0               | `&&`     | 1              |

```c
#include <stdio.h>
#include <omp.h>

int main() {
    int sum = 0;

    #pragma omp parallel for reduction(+:sum)
    for (int i = 1; i <= 100; i++) {
        sum += i;  // Each thread has private sum, initialized to 0
    }

    printf("Sum = %d\n", sum);  // Correct result: 5050
    return 0;
}
```

**Reduction Execution Model**:

1. Initialize private copy with identity value (0 for +)
2. Each thread performs independent updates to its private copy
3. At loop end, combine all private copies: $sum = \sum_{t} sum_t$

## Default Scoping Rules

OpenMP defines explicit default behaviors based on variable declaration location:

| Variable Declaration Location | Default Data-Sharing Attribute |
| ----------------------------- | ------------------------------ |
| Outside any parallel region   | `shared`                       |
| Inside parallel region        | `private`                      |
| In loop iteration variable    | `private` (implicit)           |
| Static variables              | `shared`                       |
| Global variables              | `shared`                       |

## Performance Implications: False Sharing

When multiple threads modify variables that reside on the same **cache line** (typically 64 bytes), the hardware cache coherence protocol forces invalidation and reload, degrading performance—this phenomenon is **false sharing**.

**Example**:

```c
int array[4];

#pragma omp parallel
{
    int tid = omp_get_thread_num();
    array[tid]++;  // Each thread modifies different array element
}
```

If `array[0]`, `array[1]`, etc. reside on the same cache line, each write invalidates the cache line for other threads, causing severe performance degradation despite having no data race.

**Mitigation Strategies**:

1. Pad variables to cache line boundaries using `alignas(64)`
2. Restructure data layout to separate frequently-written fields
3. Use thread-local accumulation with final reduction

## Comparison of Data-Sharing Attributes

| Clause          | Storage Duration        | Initial Value  | Final Value            | Use Case                  |
| --------------- | ----------------------- | -------------- | ---------------------- | ------------------------- |
| `shared`        | Single location         | Original value | Original (modified)    | Global data, accumulators |
| `private`       | Per-thread              | Undefined      | Undefined              | Temporary computation     |
| `firstprivate`  | Per-thread              | Original value | Undefined              | Passing initial state     |
| `lastprivate`   | Per-thread              | Undefined      | Last iteration/section | Collecting loop results   |
| `threadprivate` | Per-thread (persistent) | Original value | Original value         | Thread-local statistics   |
| `reduction`     | Per-thread              | Identity value | Combined result        | Accumulation operations   |

## Summary of Key Principles

1. **Default Rules**: Variables outside parallel regions are shared by default; variables inside are private by default.

2. **Explicit is Safer**: Always use `default(none)` and explicitly specify scope for every variable.

3. **Synchronization for Shared Writes**: All writes to shared variables must be protected using `critical`, `atomic`, or `reduction`.

4. **Private Initialization**: Use `firstprivate` when initial values must be preserved; otherwise, private variables start with undefined values.

5. **Last Value Propagation**: Use `lastprivate` to propagate results from parallel loops to serial code.

6. **Avoid False Sharing**: Consider cache line alignment when multiple threads write adjacent memory locations.

---

## Assessment Questions

### Question 1 (Analysis)

Consider the following OpenMP code:

```c
int x = 10;
#pragma omp parallel num_threads(4) firstprivate(x)
{
    x = x + omp_get_thread_num();
    #pragma omp critical
    printf("Thread %d: x = %d\n", omp_get_thread_num(), x);
}
printf("x = %d\n", x);
```

What are the possible output values of the final `printf` statement? Explain your reasoning.

### Question 2 (Application)

Given the following code with a data race, identify the race condition and propose two different solutions using OpenMP clauses to fix it:

```c
int sum = 0;
#pragma omp parallel for
for (int i = 0; i < 1000; i++) {
    sum = sum + i;  // Data race here
}
```

### Question 3 (Evaluation)

For each variable in the following code, identify its data-sharing attribute and explain why:

```c
int global_var = 5;

void compute(int param) {
    static int static_var = 10;
    int local_var = 15;

    #pragma omp parallel default(none) shared(global_var) private(local_var)
    {
        int thread_local;
        // ... code using global_var, static_var, local_var, thread_local
    }
}
```

### Question 4 (Analysis)

What is false sharing, and how does it affect performance? Provide a code example that demonstrates false sharing and explain how you would modify it to avoid the issue.

### Question 5 (Application)

Write an OpenMP parallel program that computes both the sum and maximum of an integer array using a single parallel loop with appropriate reduction clauses. Explain how the reduction mechanism ensures correctness.
