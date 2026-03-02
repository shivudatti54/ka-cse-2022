# Methods For Handling Deadlocks - Summary

## Key Definitions
- **Deadlock**: A condition where two or more processes are blocked, each waiting for resources held by the other
- **Safe State**: A state where there exists a sequence of process execution that allows all processes to complete without deadlock
- **Unsafe State**: A state where no sequence of process execution can guarantee that all processes will complete without deadlock
- **Wait-For Graph**: A directed graph representing which processes are waiting for resources held by other processes
- **Resource Allocation Graph**: A graph showing which resources are allocated to which processes and which processes are requesting which resources

## Important Formulas
- **Banker's Algorithm Safety Check**: Available ≥ Need of selected process → Allocate → Release → Repeat for all processes
- **Need Matrix**: Need[i][j] = Maximum[i][j] - Allocation[i][j]
- **Safe Sequence**: An ordering of processes such that each process's maximum need can be satisfied using available resources plus resources released by preceding processes

## Key Points
1. Deadlock handling can be approached through Prevention, Avoidance, Detection, and Recovery methods
2. Deadlock Prevention eliminates one of the four necessary conditions (Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait)
3. Deadlock Avoidance (e.g., Banker's Algorithm) ensures the system never enters an unsafe state
4. Deadlock Detection periodically checks system state for cycles in resource allocation/wait-for graphs
5. Recovery options include process termination (partial or total) and resource preemption
6. The choice of method depends on system characteristics, resource types, and performance requirements
7. Single-instance resources allow simpler detection via cycle finding in graphs
8. Multiple-instance resources require more sophisticated detection algorithms
9. Avoidance requires advance knowledge of maximum resource demands, which may not be available
10. Recovery through partial termination is generally preferred over total system termination

## Common Mistakes
1. Confusing deadlock prevention with avoidance - prevention eliminates conditions structurally, avoidance checks states dynamically
2. Forgetting that deadlock detection only identifies deadlocks but does not prevent them
3. Overlooking that the Banker's Algorithm requires prior knowledge of maximum resource needs
4. Applying single-instance detection algorithms to multiple-instance resource systems (will not work correctly)