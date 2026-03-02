# Deadlock Prevention

## Overview

Deadlock prevention ensures at least one of the four necessary conditions (mutual exclusion, hold and wait, no preemption, circular wait) cannot hold, thereby preventing deadlocks. Each strategy has trade-offs affecting system performance and resource utilization.

## Key Points

- **Negate Mutual Exclusion**: Make resources sharable when possible (read-only files), not feasible for inherently exclusive resources (printers)
- **Negate Hold and Wait**: Require process to request all resources at once before execution or release all held resources before requesting new ones
- **Negate No Preemption**: Allow forcible resource preemption - if process requests unavailable resource, preempt its currently held resources
- **Negate Circular Wait**: Impose total ordering on resource types, processes must request resources in increasing order of enumeration
- **Resource Ordering**: Assign unique number to each resource type, request in ascending order prevents circular wait
- **Disadvantages**: Low device utilization, reduced system throughput, starvation possible (hold and wait prevention)

## Important Concepts

- Preventing circular wait most practical approach using resource ordering
- Hold and wait prevention requires knowing all needed resources in advance (impractical)
- Preemption strategy applicable only to resources whose state can be easily saved/restored (CPU, memory)
- Each prevention method restricts resource request/usage, reducing concurrency

## Notes

- Know all four necessary conditions and how to negate each
- Understand trade-offs: prevention guarantees no deadlock but reduces efficiency
- Resource ordering example: tape drives=1, disk drives=5, printers=12
- Remember prevention is restrictive, avoidance is less restrictive alternative
