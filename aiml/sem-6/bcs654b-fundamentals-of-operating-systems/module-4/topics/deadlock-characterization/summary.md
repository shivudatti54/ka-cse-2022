# Deadlock Characterization

## Overview

Deadlocks are characterized by four necessary conditions that must all be true simultaneously: mutual exclusion, hold and wait, no preemption, and circular wait. Resource allocation graphs visualize system state and help identify deadlocks through cycle detection.

## Key Points

- **Mutual Exclusion**: At least one resource must be held in non-sharable mode, only one process can use resource at a time
- **Hold and Wait**: Process holds at least one resource while waiting to acquire additional resources held by other processes
- **No Preemption**: Resources cannot be forcibly removed, must be voluntarily released by holding process
- **Circular Wait**: Set of waiting processes P0, P1, ..., Pn where P0 waits for P1, P1 waits for P2, ..., Pn waits for P0
- **Resource Allocation Graph**: Vertices (processes, resources), edges (request process→resource, assignment resource→process)
- **Cycle in Graph**: If graph contains no cycles, no deadlock; if cycle exists with single instance per type, deadlock exists
- **Multiple Instances**: Cycle necessary but not sufficient condition for deadlock with multiple instances per type

## Important Concepts

- All four conditions must hold simultaneously for deadlock to possibly occur
- Resource allocation graph provides visual representation of system state
- Cycle detection algorithm determines if deadlock exists (single instance per type)
- Safety algorithm needed for multiple instances per type (Banker's Algorithm)

## Notes

- Memorize all four necessary conditions with examples
- Practice drawing and analyzing resource allocation graphs
- Understand cycle detection: DFS or matrix-based algorithms
- Remember cycle + single instance = deadlock, cycle + multiple instances = maybe deadlock
