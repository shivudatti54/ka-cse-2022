# Tasking in OpenMP - Summary

## Key Definitions and Concepts

- **Task**: Independent unit of work created dynamically using `#pragma omp task`
- **Task Construct**: `#pragma omp task [clauses]` creates explicit parallel tasks
- **Taskwait**: `#pragma omp taskwait` ensures completion of all child tasks before proceeding
- **Task Dependencies**: Specified via `depend(in:var)`, `depend(out:var)`, `depend(inout:var)`
- **Task Scheduling**: Work-stealing algorithm used for load balancing
- **Task Granularity**: Balance between task size (coarse-grained) vs overhead (fine-grained)
- **Taskloop**: `#pragma omp taskloop` divides loop iterations into implicit tasks

## Important Formulas and Theorems

```cpp
// Basic task creation
#pragma omp parallel
#pragma omp single
{
  #pragma omp task
  { /* Task A */ }

  #pragma omp task depend(out: x)
  { x = compute(); }
}

// Taskwait synchronization
#pragma omp taskwait

// Taskloop implementation
#pragma omp taskloop grainsize(500)
for(int i=0; i<N; i++) { ... }
```

## Key Points

1. Tasks handle **irregular workloads** (trees, graphs) better than `parallel for`
2. Tasks are created **dynamically** during execution using `task` directives
3. Use `single` or `master` constructs when creating multiple tasks from parallel regions
4. `taskwait` ensures **parent task** waits for all child tasks to complete
5. Task dependencies create **execution order** constraints between tasks
6. OpenMP runtime uses **work-stealing** to balance tasks across threads
7. `taskloop` automatically divides loops into tasks with optional `grainsize`
8. Tasks can be **nested** to create hierarchical parallelism
9. **Mergeable** clause preserves thread-specific data across task generations
10. Real-world applications: Image processing pipelines, recursive algorithms, event-driven systems

## Common Mistakes to Avoid

1. Creating tasks without `single` in parallel region → Duplicate task generation
2. Forgetting `taskwait` → Premature exit from parallel region with unfinished tasks
3. Ignoring task dependencies → Race conditions in shared data access
4. Excessive task granularity → High scheduling overhead vs computation gain
5. Using `shared` variables without synchronization → Data corruption

## Revision Tips

1. **Practice Task Syntax**: Write code snippets for common patterns (task chains, nested tasks)
2. **Compare Constructs**: Create a table comparing `task`, `taskloop`, and `parallel for`
3. **Dependency Diagrams**: Draw dependency graphs for `depend(in/out/inout)` scenarios
4. **Exam Focus**: Memorize 3 key differences between task-based and loop-based parallelism
5. **Real-world Cases**: Study examples like Fibonacci recursion, parallel file processing
