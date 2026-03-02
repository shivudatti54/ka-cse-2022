# Deadlock Characterization - Summary

## Key Definitions
- **Deadlock**: A state where two or more processes are waiting indefinitely for resources held by each other, forming a circular wait
- **Resource**: Any system component (CPU, memory, I/O device, lock, semaphore) that a process requires to complete execution
- **Safe State**: A system state where there exists at least one safe sequence allowing all processes to complete without deadlock
- **Unsafe State**: A system state where no safe sequence exists, indicating possibility of deadlock
- **Resource Allocation Graph (RAG)**: A directed bipartite graph representing current resource allocation and request states

## Important Formulas
- **Available Resources**: Available = Total Allocated - Sum of All Allocations
- **Need Matrix**: Need[i][j] = Maximum[i][j] - Allocation[i][j]
- **Safety Algorithm**: Work = Available; find process with Need ≤ Work; if all processes can finish, state is safe

## Key Points
- Deadlock requires all four Coffman conditions: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait
- The resource allocation graph is a visual tool for deadlock characterization—cycles indicate potential deadlock
- A cycle in RAG with single-instance resources always indicates deadlock
- A cycle in RAG with multi-instance resources indicates potential deadlock requiring further analysis
- No cycle in RAG guarantees no deadlock exists
- Safe states are a subset of all deadlock-free states; unsafe states may or may not lead to deadlock
- The hold-and-wait condition can be eliminated by requiring processes to request all resources at once
- Circular wait can be prevented by establishing a total ordering of resource types

## Common Mistakes
- Confusing necessary with sufficient conditions—Coffman conditions are necessary but not sufficient for deadlock
- Assuming all cycles in RAG indicate definite deadlock—multi-instance resources require additional analysis
- Concluding unsafe states always lead to deadlock—unsafe only means deadlock is possible, not certain
- Drawing RAG edges in wrong direction—request edges go from process to resource, assignment edges from resource to process
- Forgetting that multiple instances of a resource type can exist, fundamentally changing deadlock analysis