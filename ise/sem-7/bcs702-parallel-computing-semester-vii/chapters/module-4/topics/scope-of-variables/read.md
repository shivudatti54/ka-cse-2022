# Scope of Variables in OpenMP

## Introduction to Variable Scope in Parallel Programming

In shared memory programming with OpenMP, understanding variable scope is fundamental to writing correct, efficient, and thread-safe parallel programs. The **scope** of a variable determines which threads can access it and whether that access is shared or private. Incorrectly scoped variables are a primary source of errors in OpenMP programs, including race conditions, data corruption, and incorrect results.

When a parallel region is encountered (e.g., with `#pragma omp parallel`), the master thread forks into a team of threads. Variables declared outside this parallel region have a storage duration that persists across the region. How these variables are treated *inside* the parallel region is governed by OpenMP's data-sharing attribute rules.

## Key Concepts: Shared vs. Private Variables

### Shared Variables
A **shared** variable exists in only one memory location. All threads in the team read from and write to this single location. This is the default behavior for variables declared *outside* the parallel region (e.g., global variables, static variables, or variables in the `main` function).

**Characteristics:**
*   **Single Storage:** One copy in memory.
*   **Global Access:** All threads access the same memory address.
*   **Synchronization Needed:** Requires careful use of critical sections or atomic operations to avoid race conditions when multiple threads write to it.

**Example:**
```c
#include <stdio.h>
#include <omp.h>

int main() {
    int shared_var = 0; // Declared outside parallel region -> shared by default

    #pragma omp parallel
    {
        // All threads increment the SAME variable
        shared_var++;
        printf("Thread %d: shared_var = %d\n", omp_get_thread_num(), shared_var);
    }

    printf("Final value of shared_var: %d\n", shared_var);
    return 0;
}
```
**Possible Output (Due to Race Condition):**
```
Thread 1: shared_var = 1
Thread 2: shared_var = 2
Thread 0: shared_var = 3
Final value of shared_var: 3
```
*Or, if threads read the value simultaneously before incrementing:*
```
Thread 0: shared_var = 1
Thread 2: shared_var = 1
Thread 1: shared_var = 1
Final value of shared_var: 1 // Incorrect result due to race condition
```

### Private Variables
A **private** variable creates a separate, independent copy for each thread in the team. The value of the original variable before the parallel region is undefined inside the region, and the value of the private copy after the region is undefined in the master thread. Variables declared *inside* the parallel region are private by default.

**Characteristics:**
*   **Multiple Storage:** Each thread has its own copy.
*   **Independent Access:** Threads operate on their local copies without interference.
*   **No Synchronization Needed:** Eliminates race conditions for that variable.

**Example:**
```c
#include <stdio.h>
#include <omp.h>

int main() {
    int private_var; // Original variable

    #pragma omp parallel private(private_var)
    {
        // Each thread has its OWN COPY of private_var
        private_var = omp_get_thread_num(); // Initialize local copy
        printf("Thread %d: private_var = %d\n", omp_get_thread_num(), private_var);
    }

    // Value of the original private_var here is undefined
    printf("Original variable after parallel region: %d\n", private_var);
    return 0;
}
```
**Possible Output:**
```
Thread 0: private_var = 0
Thread 2: private_var = 2
Thread 1: private_var = 1
Original variable after parallel region: 32767 // Garbage value
```

## Data-Sharing Attribute Clauses

OpenMP provides clauses to explicitly control the scope of variables, overriding the default rules. These clauses are used with directives like `parallel`, `for`, and `sections`.

### 1. The `private` Clause
Explicitly declares a variable to be private to each thread.
```c
int a = 10;
#pragma omp parallel private(a)
{
    // 'a' inside here is uninitialized for each thread
    a = omp_get_thread_num();
    // Original 'a' (value 10) is unchanged
}
// Value of original 'a' is still 10
```

### 2. The `firstprivate` Clause
A special case of `private` that **initializes** each thread's private copy with the value of the original variable from before the parallel region.
```c
int a = 42;
#pragma omp parallel firstprivate(a)
{
    // Each thread's 'a' starts with the value 42
    a += omp_get_thread_num();
    // Modify local copy
}
// Value of original 'a' is still 42
```

### 3. The `lastprivate` Clause
A special case of `private` that **updates** the original variable after the parallel region with the value from the sequentially last iteration (in a loop construct) or the last section (in a sections construct).
```c
int a;
#pragma omp parallel for lastprivate(a)
for (int i = 0; i < 10; i++) {
    a = i; // Each thread updates its private 'a'
}
// Original 'a' now has the value from the last iteration (i=9)
printf("a = %d\n", a); // Output: a = 9
```

### 4. The `shared` Clause
Explicitly declares a variable as shared. This is often used for clarity, even though it might be the default.
```c
int counter = 0;
#pragma omp parallel shared(counter)
{
    #pragma omp critical
    counter++; // Need critical section to avoid race condition
}
```

### 5. The `default` Clause
Forces a specific default scope for variables not explicitly listed in other data-sharing clauses. `default(none)` is a crucial tool for writing safe code, as it forces the programmer to explicitly specify the scope for every variable, preventing errors from implicit defaults.
```c
int a, b, c;
#pragma omp parallel default(none) shared(a, b) private(c)
{
    // Compiler will error if 'c' is not handled explicitly.
    // Forgetting to list 'a' or 'b' would also cause an error.
    c = omp_get_thread_num();
    // ... use a, b, c
}
```

## Default Scoping Rules

OpenMP defines default scoping rules based on the construct and where the variable is declared.

| Construct Type                  | Variables declared outside construct (e.g., global, in `main`) | Variables declared inside construct (e.g., loop index) |
| ------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------ |
| `parallel`, `teams`             | **SHARED**                                                    | **PRIVATE**                                            |
| `for`, `simd`, `sections`, `task` | **SHARED** (unless iteration variable)                       | **PRIVATE**                                            |
| `task`                          | **FIRSTPRIVATE** (by default in OpenMP 3.0+)                 | **PRIVATE**                                            |

*Table 1: Summary of Default Data-Sharing Attributes*

**Loop Iteration Variables:** The index variable of a loop worksharing construct (`#pragma omp for`) is automatically made private, even if it was declared outside the parallel region.

## The Reduction Clause: A Special Case

The `reduction` clause combines the benefits of private and shared variables. It performs a specific operation (e.g., `+`, `*`, `max`) on a variable.

**How it works:**
1.  **Private Copy:** OpenMP creates a private copy of the variable for each thread and initializes it based on the operation (e.g., 0 for `+`, 1 for `*`).
2.  **Local Computation:** Each thread performs its computation on its local private copy.
3.  **Combination:** At the end of the parallel region, all local results are combined (reduced) into the original shared variable using the specified operation. This combination is done atomically to avoid race conditions.

**Syntax:** `reduction(operator: variable_list)`

**Example: Calculating a sum safely without a critical section.**
```c
#include <stdio.h>
#include <omp.h>

int main() {
    int sum = 0;
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < 100; i++) {
        sum += i; // Each thread adds to its PRIVATE copy of 'sum'
    }
    // All private 'sum's are reduced (added) into the shared 'sum'
    printf("Sum = %d\n", sum); // Correct output: 4950
    return 0;
}
```
**Visualization of Reduction:**
```
Thread 0 Private Sum: 2450
Thread 1 Private Sum: 4950  ->  Combined via '+' ->  Global Sum: 4950
Thread 2 Private Sum: 7450
```

## Common Pitfalls and How to Avoid Them

1.  **Race Conditions:** Occur when multiple threads write to a shared variable without synchronization.
    *   **Solution:** Use `critical`, `atomic`, `reduction`, or make the variable `private`.

2.  **Uninitialized Private Variables:** A `private` variable inside a parallel region does not inherit the value of the original variable.
    *   **Solution:** Use `firstprivate` if you need the initial value.

3.  **Forgetting `lastprivate`:** If you need the last value from a parallel loop to be available afterwards, you must use `lastprivate`.
    *   **Solution:** Remember to use `lastprivate(clause)`.

4.  **Implicit Defaults Leading to Errors:** Relying on default sharing rules can cause subtle bugs, especially in complex code.
    *   **Solution:** **Always use `default(none)`** and explicitly specify the scope of all variables. This is a best practice.

## ASCII Diagram: Variable Scoping in a Parallel Region

```
MASTER THREAD MEMORY (BEFORE)
+------------------------+
| shared_var (value = 5) |<-----+
| private_var (value = 2) |      |
+------------------------+      |
                                | SHARED
                                | (One memory location)
PARALLEL REGION STARTS          |
Thread 0 Memory      |          |
+------------------------+      |
| private_var (UNDEFINED)|      |
+------------------------+      |
                                |
Thread 1 Memory      |          |
+------------------------+      |
| private_var (UNDEFINED)|      |
+------------------------+      |
                                |
Thread 2 Memory      |          V
+------------------------+      +-----------------------+
| private_var (UNDEFINED)|      | shared_var (value = 5)|<-- All threads
+------------------------+      +-----------------------+    read/write here
```

## Exam Tips

*   **Memorize the Defaults:** Know that variables declared outside a `parallel` region are `shared` by default, and variables declared inside are `private`.
*   **`firstprivate` vs. `lastprivate`:** `firstprivate` is about initialization at the start, `lastprivate` is about updating at the end.
*   **Reduction is Your Friend:** Remember that `reduction` is the standard, efficient way to handle operations like sum, product, min, and max across threads. It avoids the overhead of critical sections.
*   **`default(none)` is a Best Practice:** Explicitly stating your intent for every variable's scope prevents countless errors. Expect questions that use this clause.
*   **Spot the Race Condition:** Exam questions often present code snippets with a shared variable being written to without protection. Your first instinct should be to identify this race condition.
*   **Loop Index is Special:** Remember that the loop index in an OpenMP `for` directive is always private, regardless of its original declaration.