# Deadlock Detection and Prevention - Summary

## Key Definitions and Concepts
- **Deadlock**: Permanent blocking of process set waiting for resources
- **Safe State**: Exists if system can allocate resources without deadlock
- **Livelock**: Processes keep changing state but make no progress
- **Starvation**: Infinite resource postponement (not deadlock)

## Important Formulas and Theorems
- **Safety Algorithm**: Σ Allocation + Available ≥ Max for all processes
- **Resource Ordering**: ∀ resources r_i, r_j: i < j → request order r_i before r_j
- **Wait-For Graph**: Cycle detection via depth-first search

## Key Points
- Deadlocks require all four Coffman conditions
- Detection uses periodic graph analysis (O(n²) complexity)
- Prevention eliminates ≥1 condition during system design
- Banker's Algorithm requires prior knowledge of max needs
- Distributed systems use timestamp-based detection
- Recovery methods: Process termination, resource preemption
- Real-world systems often combine detection and prevention

## Common Mistakes to Avoid
- Confusing deadlock prevention with avoidance
- Ignoring resource types in allocation graphs
- Forgetting to update Available matrix in Banker's Algorithm
- Assuming all resources are single-instance

## Revision Tips
1. Practice Banker's Algorithm with varying Available resources
2. Memorize Coffman conditions using acronym "MuHNoC"
3. Compare WFG cycle detection in single vs multi-instance resources
4. Study real-world cases: Database deadlocks, thread synchronization
5. Create flowcharts for detection and prevention algorithms