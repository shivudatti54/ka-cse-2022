# Deadlock Characterization - Summary

## Key Definitions and Concepts

- DEADLOCK: A permanent blocking of processes where each process waits for a resource held by another process in a circular wait condition
- COFFMAN CONDITIONS: Four necessary conditions for deadlock—Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait
- RESOURCE ALLOCATION GRAPH (RAG): A directed graph with process nodes and resource nodes showing request and assignment edges
- SAFE STATE: A system state where a safe sequence exists allowing all processes to complete without deadlock
- UNSAFE STATE: A system state where no safe sequence exists—deadlock is possible but not certain

## Important Formulas and Theorems

- For RAG with single-instance resources: CYCLE = DEADLOCK
- For RAG with multiple-instance resources: CYCLE may NOT equal deadlock
- Banker's Algorithm Safety Test: Available ≥ Need of some process Pi, then add Pi's allocation to Available, repeat until all processes complete or no process can proceed

## Key Points

- ALL FOUR Coffman conditions must hold simultaneously for deadlock to occur
- A cycle in Resource Allocation Graph indicates potential deadlock only when resources in the cycle have single instances
- Safe state means the system CAN avoid deadlock; unsafe state means deadlock is POSSIBLE (not certain)
- Violating ANY ONE Coffman condition prevents deadlock—these are the foundations of deadlock prevention
- Deadlock characterization is about IDENTIFYING conditions that lead to deadlock, not about solving deadlocks

## Common Mistakes to Avoid

- CONFUSING unsafe states with deadlock states—unsafe does not mean deadlock has occurred
- ASSUMING a cycle in RAG always means deadlock—this is true only for single-instance resources
- FORGETTING that the four conditions are NECESSARY but not sufficient
- NOT understanding that resource preemption is only possible for preemptible resources

## Revision Tips

- Draw Resource Allocation Graphs for different scenarios and practice identifying cycles
- Memorize the four Coffman conditions using mnemonic M-H-N-C
- Practice determining safe sequences with the Banker's Algorithm
- Remember: Prevention avoids the conditions; Avoidance ensures safe states; Detection allows recovery after deadlock occurs