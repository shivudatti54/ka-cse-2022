# Methods for Handling Deadlocks

## Overview

Operating systems handle deadlocks using four approaches: prevention (negate necessary condition), avoidance (safe state before allocation), detection and recovery (periodic checking), or ignoring (ostrich algorithm). Each method has different complexity, overhead, and effectiveness trade-offs.

## Key Points

- **Deadlock Prevention**: Negate at least one of four necessary conditions, restricts resource requests, reduces system concurrency
- **Deadlock Avoidance**: Requires advance information about resource needs, uses Banker's Algorithm to ensure safe state
- **Deadlock Detection**: Allows deadlocks to occur, periodically invokes detection algorithm, uses resource allocation graph or matrix
- **Deadlock Recovery**: Process termination (abort all or one at a time) or resource preemption (select victim, rollback, starvation)
- **Ignore Deadlocks**: Ostrich algorithm, assume deadlocks rare, system restart if deadlock detected, used by UNIX, Windows
- **Banker's Algorithm**: Maintains safe state by granting requests only if resulting state is safe
- **Safe State**: System can allocate resources to each process in some order without deadlock

## Important Concepts

- Prevention most restrictive, avoidance requires advance knowledge, detection allows occurrence
- Banker's Algorithm checks if granting request leaves system in safe state
- Detection frequency trade-off: frequent (low deadlock duration, high overhead), infrequent (reverse)
- Recovery by termination loses work, recovery by preemption may cause starvation

## Notes

- Understand when to use each method based on system requirements
- Know Banker's Algorithm steps: request → check safety → grant or deny
- Practice safe sequence calculations for avoidance
- Remember most OS ignore deadlocks (ostrich algorithm) due to rarity
