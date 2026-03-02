# Peterson's Solution - Summary

## Key Definitions and Concepts

- **Critical Section**: The portion of code where shared resources are accessed and requires mutual exclusion to prevent race conditions.

- **Peterson's Solution**: A software-based algorithm developed by Gary Peterson in 1981 that provides mutual exclusion for two competing processes without hardware assistance.

- **Mutual Exclusion**: The requirement that no two processes can simultaneously execute within their critical sections.

- **Progress**: The requirement that processes not in their remainder section cannot prevent other processes from entering their critical sections.

- **Bounded Waiting**: The requirement that there exists a limit on the number of times other processes can enter their critical sections after a process has made a request.

## Important Formulas and Theorems

The entry section of Peterson's Solution for process i (where i is 0 or 1, and j is the other process) is:

```
flag[i] = true;
turn = j;
while (flag[j] && turn == j)
    ; // busy wait
```

The exit section is:

```
flag[i] = false;
```

## Key Points

- Peterson's Solution uses two shared variables: `turn` (an integer) and `flag[2]` (a Boolean array).

- The algorithm ensures mutual exclusion by requiring both conditions to be true for a process to wait: the other process must want to enter AND it must be the other process's turn.

- Progress is satisfied because if the other process is not interested (`flag[j] == false`), the waiting process enters immediately.

- Bounded waiting is guaranteed because the turn variable alternates or can only be changed by the other process.

- The solution assumes atomic reads and writes to shared variables, which requires hardware support in practice.

- The algorithm uses busy waiting (spinlock), which consumes CPU cycles while waiting.

- Peterson's Solution specifically handles only two processes and cannot be directly extended to N processes.

## Common Mistakes to Avoid

- Forgetting that both `turn` AND `flag[]` are necessary; using only one variable leads to incorrect solutions.

- Incorrectly setting `turn` to the current process instead of the other process, which breaks the progress requirement.

- Assuming the solution works for more than two processes without modification.

- Confusing the conditions in the while loop—the logical AND means BOTH conditions must be true for waiting.

- Overlooking the assumption of atomic operations, which is critical for correctness.

## Revision Tips

- Practice tracing through multiple execution scenarios with different interleavings of statements.

- Draw state diagrams showing process transitions between remainder, entry, critical, and exit sections.

- Memorize the algorithm structure but also understand why each line exists.

- Review the three requirements and be able to provide specific reasoning for each requirement's satisfaction.

- Compare with other synchronization solutions to understand the trade-offs.