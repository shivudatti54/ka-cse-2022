# Peterson's Solution

## Fundamentals of Operating Systems

### Overview

Peterson's solution is a synchronization algorithm for two processes accessing shared resources. It ensures mutual exclusion and prevents deadlocks.

### Key Points

- **Problem Statement**: Two processes, P1 and P2, need to access a shared resource, but both want to access it simultaneously.
- **Goal**: Ensure that only one process can access the shared resource at a time, preventing deadlocks.
- **Peterson's Solution**:
  - Two processes, P1 and P2, each have a flag variable `f` and a counter variable `c`.
  - The process with the value 0 is considered the owner of the resource.
  - The process with the value 1 is considered the non-owner.

### Important Formulas and Definitions

- **Peterson's Condition**: The condition for two processes to access the shared resource is given by `c1 == 0 && (c2 == 1 || f2 == 0)`.
- **Peterson's Loop**:
  1.  If the current process is the owner, set `f` to 1 and increment `c`.
  2.  If the current process is the non-owner, set `f` to 1 and wait until the Peterson's condition is true.

### Important Theorems

- **Peterson's Theorem**: Peterson's solution ensures mutual exclusion and prevents deadlocks for two processes accessing a shared resource.
- **Safety**: Peterson's solution ensures that the shared resource is accessed safely, without violating any constraints.

### Important Concepts

- **Mutual Exclusion**: Peterson's solution ensures that only one process can access the shared resource at a time.
- **Deadlock Prevention**: Peterson's solution prevents deadlocks by ensuring that the Peterson's condition is always true.
- **Token Passing**: Peterson's solution uses a token passing approach to synchronize the access to the shared resource.
