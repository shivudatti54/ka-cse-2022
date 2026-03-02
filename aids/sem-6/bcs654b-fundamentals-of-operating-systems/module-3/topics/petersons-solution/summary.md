# Peterson’s Solution - Summary

## Key Definitions and Concepts

- **Critical Section**: Code segment accessing shared resources requiring mutual exclusion
- **Mutual Exclusion**: Ensuring only one process executes in its critical section at a time
- **Progress**: No process not in its critical section should block others wanting to enter
- **Bounded Waiting**: Bound on number of times others can enter CS before current process
- **Peterson's Algorithm**: Software-based solution for mutual exclusion between **two processes**

## Important Formulas and Theorems

```markdown
1. Entry Section Code:
   flag[i] = True # Process i wants to enter CS
   turn = j # Give priority to other process
   while (flag[j] && turn == j): # Busy wait

2. Exit Section Code:
   flag[i] = False # Release CS
```

## Key Points

- Solves critical section problem for **exactly two processes**
- Uses two shared variables: `flag[2]` (boolean array) and `turn`
- Combines **mutual exclusion** with **busy waiting** (spinlock)
- Satisfies all three requirements: Mutual Exclusion, Progress, Bounded Waiting
- Process flow:

1.  Declare intention to enter CS (`flag[i] = True`)
2.  Give priority to other process (`turn = j`)
3.  Wait while other process wants to enter AND has priority

- Not used in modern OS due to busy waiting, but important theoretical foundation
- Limited to two processes (doesn't scale to N processes)
- Pure software solution (no special hardware instructions)

## Common Mistakes to Avoid

1. Confusing with **Dekker's Algorithm** (similar but more complex two-process solution)
2. Assuming it works for N > 2 processes (only valid for two processes)
3. Forgetting to set `turn` variable before busy wait
4. Implementing flags as single variable instead of array for each process

## Revision Tips

1. **Visualize the algorithm flow** using process state diagrams
2. Practice writing pseudocode from memory with proper entry/exit sections
3. Compare with hardware solutions (TestAndSet, Swap) for mutual exclusion
4. Remember key limitations: Busy waiting, 2-process restriction, no fairness guarantee
