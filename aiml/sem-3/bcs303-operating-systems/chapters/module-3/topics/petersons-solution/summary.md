# Peterson's Solution

## Revision Notes

### Operating Systems Module: 8 Hours

### Key Points:

- Peterson's Solution is a synchronization algorithm used to protect common variables in a multi-process environment.
- It involves two processes, P1 and P2, that take turns accessing a common variable.
- The algorithm uses two resources (R1 and R2) to ensure mutual exclusion.

### Important Formulas, Definitions, Theorems:

- **Peterson's Solution Algorithm:**
  ```markdown
  while (true) {
  if (P1[R1] == 0) {
  P1[R1] = P1[R1] + 1;
  P2[R2] = P2[R2] + 1;
  yield;
  } else if (P2[R2] == 0) {
  P2[R2] = P2[R2] + 1;
  P1[R1] = P1[R1] + 1;
  yield;
  }
  }
  ```
- **Definition of a Yield Statement:** A yield statement in a coroutine is used to pause the execution of the coroutine and return control to the caller.

### Notable Theorems:

- **Peterson's Theorem:** Peterson's solution is a solution to the problem of synchronization in a multi-process environment, and it works correctly even in the presence of a malicious process.

### Key Concepts:

- **Mutual Exclusion:** A fundamental concept in synchronization, where one process must have exclusive access to a shared resource.
- **Synchronization:** The process of coordinating the actions of multiple processes to achieve a common goal.

### Revision Tips:

- Focus on understanding the algorithm and its implementation.
- Practice solving problems related to synchronization and mutual exclusion.
