# Deadlock Avoidance - Summary

## Key Definitions and Concepts

- DEADLOCK AVOIDANCE: A strategy that allows all deadlock conditions to exist but makes intelligent allocation decisions to prevent the system from entering unsafe states where deadlock becomes inevitable.

- SAFE STATE: A system state where there exists a sequence of process executions (safe sequence) that allows all processes to complete without deadlock, even if they request maximum resources simultaneously.

- UNSAFE STATE: A state where no safe sequence exists; deadlock is possible but not certain.

- BANKER'S ALGORITHM: A deadlock avoidance algorithm requiring processes to declare maximum resource needs in advance. It allocates resources only if the resulting state remains safe.

- RESOURCE ALLOCATION GRAPH (RAG): A directed graph representing processes and resource types. A cycle indicates potential deadlock. The variant with claim edges helps avoid deadlock in single-instance systems.

## Important Formulas and Theorems

- NEED[i][j] = MAXIMUM[i][j] - ALLOCATION[i][j]
- AVAILABLE = TOTAL RESOURCES - SUM OF ALLOCATION for each type
- SAFETY ALGORITHM: Iteratively find process P with Need ≤ Work, allocate its resources, add to Work, repeat until all processes finish or no such process exists.

## Key Points

- DEADLOCK AVOIDANCE REQUIRES ADVANCE KNOWLEDGE of maximum resource needs for all processes.
- THE SYSTEM REMAINS IN SAFE STATE BY GUARANTEEING that resource requests do not lead to unsafe states.
- BANKER'S ALGORITHM IS CONSERVATIVE—it may deny requests that would actually be safe but cannot be proven safe.
- FOR MULTIPLE RESOURCE INSTANCES, USE BANKER'S ALGORITHM; FOR SINGLE INSTANCES, RESOURCE ALLOCATION GRAPH suffices.
- SAFE STATE ≠ DEADLOCK WILL NOT OCCUR; UNSAFE STATE ≠ DEADLOCK WILL OCCUR.
- THE FOUR CONDITIONS FOR DEADLOCK ARE: mutual exclusion, hold and wait, no preemption, circular wait.
- DEADLOCK PREVENTION REMOVES ONE CONDITION; DEADLOCK AVOIDANCE MAKES SMART DECISIONS.

## Common Mistakes to Avoid

- CONFUSING DEADLOCK PREVENTION WITH AVOIDANCE—prevention removes conditions, avoidance makes smart allocation choices.
- SKIPPING THE VALIDATION CHECK: Request ≤ Need AND Request ≤ Available before attempting safety analysis.
- ASSUMING UNSAFE STATE MEANS DEADLOCK IS CERTAIN—unsafe only means deadlock is possible.
- FORGETTING TO RESTORE ORIGINAL STATE when a request is denied in the Banker's Algorithm.

## Revision Tips

- PRACTICE DRAWING AND SOLVING AT LEAST THREE BANKER'S ALGORITHM PROBLEMS with different resource configurations.
- MEMORIZE THE DATA STRUCTURES: Available, Maximum, Allocation, Need and their relationships.
- UNDERSTAND THE SAFETY ALGORITHM FLOW: Find process → Check Need ≤ Work → Allocate → Release → Repeat.
- REMEMBER THAT THE BANKER'S ALGORITHM NAMES ARE METAPHORICAL—banks don't actually run the algorithm; it's named for how a bank might manage loans.