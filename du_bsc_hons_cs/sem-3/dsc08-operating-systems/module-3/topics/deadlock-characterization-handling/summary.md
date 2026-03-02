# Deadlock: Characterization and Handling - Summary

## Key Definitions and Concepts

- **Deadlock**: A permanent blocking of processes where each process waits for a resource held by another process in the set
- **Coffman Conditions**: Four necessary conditions for deadlock—Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait
- **Resource Allocation Graph (RAG)**: A directed graph representing resource allocation with process vertices (circles) and resource vertices (squares)
- **Safe State**: A system state where there exists a sequence allowing all processes to complete without deadlock
- **Unsafe State**: A state where no safe sequence exists—deadlock may occur but is not certain

## Important Formulas and Theorems

- **Need Matrix**: Need[i][j] = Maximum[i][j] - Allocation[i][j]
- **Safety Algorithm**: Work = Available; find process where Need ≤ Work, complete it, update Work, repeat
- **RAG Theorem**: No cycle = no deadlock; Cycle with single-instance resources = definite deadlock

## Key Points

- All four Coffman conditions must hold simultaneously for deadlock to occur
- Deadlock prevention ensures at least one condition cannot hold
- Deadlock avoidance (Banker's Algorithm) maintains safe states during resource allocation
- Banker's Algorithm requires knowledge of maximum resource needs in advance
- Deadlock detection identifies existing deadlocks but doesn't prevent them
- Recovery options include process termination and resource preemption
- The order of resource request can prevent circular wait condition
- Multiple instances of resources require more complex analysis than single instances

## Common Mistakes to Avoid

- Confusing deadlock prevention with avoidance—they are fundamentally different strategies
- Forgetting that a safe state doesn't mean deadlock is occurring; it means deadlock can be avoided
- Incorrectly calculating the Need matrix (Maximum - Allocation)
- Assuming circular wait always leads to deadlock (only true for single-instance resources)
- Mixing up request edges and assignment edges in RAG diagrams

## Revision Tips

1. Memorize the four Coffman conditions in order and understand how each can be violated
2. Practice at least 5 Banker's Algorithm problems to master safe sequence calculation
3. Remember: prevention attacks conditions, avoidance checks safety, detection finds existing deadlock
4. For RAG, practice drawing graphs with both request and assignment edges
5. Review the difference between preemptible and non-preemptible resources—deadlocks involve non-preemptible resources