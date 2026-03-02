# Deadlock Avoidance - Summary

## Key Definitions

- **Deadlock Avoidance**: A proactive approach that ensures the system never enters an unsafe state by carefully examining resource allocation requests before granting them
- **Safe State**: A system state in which there exists at least one safe sequence of process execution that allows all processes to complete without deadlock
- **Safe Sequence**: An ordering of processes such that if resources are allocated in that order, each process can complete using only the available resources plus those allocated to earlier processes in the sequence
- **Unsafe State**: A state where no safe sequence exists; deadlock is possible but not guaranteed
- **Banker's Algorithm**: A deadlock avoidance algorithm for systems with multiple instances of each resource type, developed by Edsger Dijkstra

## Important Formulas

- **Need Matrix**: Need[i][j] = Maximum[i][j] - Allocation[i][j]
- **Safety Check Condition**: Process Pi can complete if Need[i] ≤ Work (available resources)
- **New Available after allocation**: Available = Available - Request
- **New Available after process completion**: Available = Available + Allocation[i]

## Key Points

1. Deadlock avoidance allows all four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, circular wait) to remain intact
2. The Banker's Algorithm requires each process to declare its maximum resource needs in advance
3. A system is safe if it can find a sequence where all processes can complete with available resources
4. The Safety Algorithm iteratively finds processes whose needs can be satisfied and simulates their completion
5. Before granting any resource request, the system simulates the allocation and checks if the resulting state is safe
6. For single-instance resources, cycles in the Resource Allocation Graph indicate potential deadlock
7. Deadlock avoidance has higher overhead but prevents deadlock rather than dealing with its consequences
8. The algorithm assumes a fixed number of processes and known maximum resource requirements

## Common Mistakes

1. **Confusing safe and unsafe states**: Students often assume unsafe states always lead to deadlock, but they only indicate the *possibility* of deadlock
2. **Forgetting to update matrices correctly**: When checking resource requests, Need must be recalculated as Maximum minus the *new* Allocation
3. **Not pretending before committing**: Students sometimes grant requests without first simulating the safety check
4. **Incorrect Work calculation**: After granting resources to a process in the safety algorithm, Work becomes Work + Allocation, not Work + Need
5. **Mixing up prevention and avoidance**: Prevention eliminates one of the four necessary conditions; avoidance allows all conditions but controls resource allocation