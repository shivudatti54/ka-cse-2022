# Deadlocks - Summary

## Key Definitions and Concepts

- **Deadlock**: A situation where two or more processes are permanently blocked, each waiting for a resource held by another.
- **Safe State**: A system state where there exists a sequence of process execution (safe sequence) that allows all processes to complete without deadlock.
- **Safe Sequence**: An ordering of processes such that if each process requests resources up to its maximum need, all can complete.
- **Resource Allocation Graph**: A directed graph showing resource allocation and requests, used for deadlock analysis.
- **Need Matrix**: The remaining resource requirement of each process, calculated as Need = Maximum - Allocation.

## Important Formulas and Theorems

- **Need Calculation**: Need[i][j] = Maximum[i][j] - Allocation[i][j]
- **Banker's Algorithm Safety Check**: Available + Allocation of completed process ≥ Need of next process in sequence
- **Deadlock Conditions Theorem**: All four conditions (mutual exclusion, hold and wait, no preemption, circular wait) must hold simultaneously for deadlock
- **RAG Cycle Theorem**: Cycle implies possible deadlock; if each resource type has exactly one instance, cycle guarantees deadlock

## Key Points

1. Four necessary conditions for deadlock: Mutual exclusion, hold and wait, no preemption, circular wait
2. Deadlock prevention attacks one of the four conditions; deadlock avoidance dynamically maintains safe states
3. Banker's Algorithm requires advance knowledge of maximum resource needs
4. Safe state means at least one safe sequence exists; unsafe state may lead to deadlock
5. Resource allocation graph: cycle ≠ always deadlock (depends on resource instances)
6. Detection algorithms can identify actual deadlocks; frequency of detection involves trade-off
7. Recovery options: terminate all deadlocked processes, terminate one at a time, or preempt resources
8. Resource ordering prevents circular wait by enforcing strict increasing request order
9. Most mainstream OS use "ignorance" approach due to overhead of other methods
10. Banker's Algorithm time complexity is O(m × n²) where m = resource types, n = processes

## Common Mistakes to Avoid

1. Confusing deadlock prevention with avoidance—they are fundamentally different approaches
2. Forgetting that circular wait requires all four conditions; attacking one prevents deadlock
3. Assuming every cycle in RAG means deadlock (only true for single-instance resources)
4. Not recalculating Available after each process completes in safety algorithms
5. Thinking safe state means no deadlock will occur—it only means deadlock can be avoided

## Revision Tips

1. Practice Banker's Algorithm numerical problems multiple times until comfortable with Need calculations
2. Memorize the four deadlock conditions and think about how each prevention strategy attacks them
3. Draw resource allocation graphs for various scenarios to build intuition
4. Remember that safe state ≠ no deadlock, but rather "can avoid deadlock"
5. Review past DU examination questions on deadlocks to understand the expected answer format
6. Create a comparison table of all four handling methods with pros and cons