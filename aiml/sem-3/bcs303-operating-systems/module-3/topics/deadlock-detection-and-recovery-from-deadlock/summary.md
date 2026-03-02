# Deadlock Detection and Recovery from Deadlock - Summary

## Key Definitions

- **Deadlock Detection**: The process of periodically examining the system state to determine whether processes have entered a deadlock state.

- **Resource Allocation Graph (RAG)**: A directed graph representing the current state of resource allocation with process nodes and resource nodes, showing request and assignment edges.

- **Wait-For Graph**: A directed graph derived from RAG showing only process dependencies, where an edge Pi → Pj indicates Pi is waiting for a resource held by Pj.

- **Recovery**: The process of breaking an existing deadlock and returning the system to a normal operating state.

## Important Formulas

- **Single Instance Detection Time Complexity**: O(n²) where n is the number of processes

- **Multiple Instance Detection Time Complexity**: O(m × n²) where m is the number of resource types and n is the number of processes

- **Work Vector Update**: Work = Work + Allocation_i (when process i completes)

## Key Points

1. Detection algorithms identify deadlocks after they occur, unlike prevention/avoidance which stops them proactively.

2. For single-instance resources, a cycle in the wait-for graph guarantees deadlock.

3. For multiple-instance resources, the detection algorithm uses Available, Allocation, and Request matrices to determine if a safe sequence exists.

4. If all Finish[i] = true after detection algorithm, no deadlock exists; otherwise, processes with Finish[i] = false are deadlocked.

5. Process termination recovery can be all-or-one strategy, with selection based on priority, progress, and resource usage.

6. Resource preemption requires checkpointing and rollback mechanisms to be practical.

7. The frequency of detection execution involves a trade-off between overhead and responsiveness to deadlocks.

8. Recovery techniques may cause starvation if not designed carefully.

## Common Mistakes

1. Confusing resource allocation graph cycles with deadlock: In multiple-instance systems, a cycle doesn't guarantee deadlock.

2. Forgetting to update the Work vector after a process completes during detection.

3. Not considering that terminated processes may need to restart from the beginning, losing all progress.

4. Assuming resource preemption is always feasible without understanding the cost of rollback.

5. Applying single-instance detection logic to multiple-instance systems, leading to incorrect conclusions.