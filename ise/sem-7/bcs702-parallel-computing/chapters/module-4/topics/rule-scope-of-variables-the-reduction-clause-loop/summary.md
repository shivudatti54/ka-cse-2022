# **Rule, Scope of Variables, Reduction Clause, Loop Carried Dependency, Scheduling, Producers and Consumers, Caches, Cache Coherence, and False Sharing**

### Rule

- Rule for variable reduction: Multiple assignments to the same variable are allowed if the assignments are independent.
- Rule for variable scope: Variables are scoped to the block they are declared in, unless explicitly changed.

### Reduction Clause

- Reduction clause: `reduction(+:var_name)`: Specifies that the variable `var_name` should be reduced (i.e., its final value is the sum of its initial values).
- Formula: `reduction(+:var_name) = var_name[0] + var_name[1] + ... + var_name[n]`

### Loop Carried Dependency

- Loop carried dependency: A dependency that propagates from one iteration of a loop to the next.
- Formula: `D(i) = f(D(i-1))`, where `D(i)` is the dependency at iteration `i`.

### Scheduling

- Scheduling: The order in which tasks are executed by the processor.
- Types of scheduling:
  - Immediate scheduling: Tasks are executed in the order they are scheduled.
  - Deferred scheduling: Tasks are executed in a different order than specified.
  - Parallel scheduling: Multiple tasks are executed concurrently.

### Producers and Consumers

- Producers: Tasks that produce data that is consumed by other tasks.
- Consumers: Tasks that consume data produced by producers.
- Deadlock: A situation where two or more tasks are waiting for each other to release resources.

### Caches

- Cache: A small, fast memory that stores frequently accessed data.
- Cache coherence: Ensures that data is consistent across different processors.
- False sharing: A situation where multiple tasks share the same cache line, leading to reduced performance.

### Cache Coherence and False Sharing

- Cache coherence protocols:
  - MESI (Modified, Exclusive, Shared, Invalid)
  - MSI (Modified, Shared, Invalid)
- False sharing formula: `s = (t \* p) / c`, where `s` is the false sharing factor, `t` is the number of tasks, `p` is the number of threads per task, and `c` is the number of cache lines.
