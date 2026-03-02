# Deadlock Avoidance

## Overview

Deadlock avoidance dynamically examines resource allocation state to ensure system never enters unsafe state. The Banker's Algorithm is the primary avoidance technique, requiring advance knowledge of maximum resource needs and granting requests only when resulting state remains safe.

## Key Points

- **Safe State**: System can allocate resources to each process in some order (safe sequence) without deadlock
- **Unsafe State**: No safe sequence exists, may lead to deadlock but doesn't guarantee it
- **Banker's Algorithm**: Simulates resource allocation, grants request only if system remains in safe state
- **Resource Request Algorithm**: Check if request ≤ need, check if request ≤ available, simulate allocation, run safety algorithm
- **Safety Algorithm**: Find process with need ≤ available, mark as finished, add its resources to available, repeat until all finished
- **Safe Sequence**: Order of process execution where each can get needed resources from available + allocated to finished processes
- **Single Instance**: Resource allocation graph with claim edges, grant if no cycle created
- **Multiple Instances**: Use Banker's Algorithm with available, maximum, allocation, and need matrices

## Important Concepts

- Safe state guarantees no deadlock, unsafe state may or may not lead to deadlock
- Avoidance requires advance knowledge of maximum resource requirements
- Banker's Algorithm conservative: may deny requests even if no deadlock would occur
- Safety check overhead: O(m × n²) where m=resources, n=processes

## Notes

- Practice safety algorithm step-by-step with example matrices
- Understand difference between safe and unsafe states
- Know Banker's Algorithm request handling steps
- Remember avoidance requires knowing maximum resource needs in advance
