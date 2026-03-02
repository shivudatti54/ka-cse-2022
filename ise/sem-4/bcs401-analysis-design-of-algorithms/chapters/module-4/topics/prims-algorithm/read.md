# Banker's Algorithm

## Overview

The **Banker's Algorithm** is a deadlock avoidance algorithm that tests for safety by simulating allocation of maximum possible amounts of all resources, then checks if the system can complete all processes.

Named after banking analogy: Bank never allocates cash that prevents satisfying all customers.

## Data Structures

| Structure  | Size  | Description                          |
| ---------- | ----- | ------------------------------------ |
| Available  | m     | Available instances of each resource |
| Max        | n × m | Maximum demand of each process       |
| Allocation | n × m | Currently allocated resources        |
| Need       | n × m | Remaining need (Max - Allocation)    |

Where: n = processes, m = resource types

## Safety Algorithm

Determines if current state is safe.

```
1. Initialize:
   Work = Available
   Finish[i] = false for all i

2. Find process i such that:
   Finish[i] = false AND Need[i] ≤ Work

3. If found:
   Work = Work + Allocation[i]
   Finish[i] = true
   Go to step 2

4. If all Finish[i] = true:
   System is in SAFE state
   Return safe sequence
```

## Resource Request Algorithm

When process Pi requests resources Request[i]:

```
1. If Request[i] > Need[i]:
   Error! Exceeded max claim

2. If Request[i] > Available:
   Process must wait

3. Pretend to allocate:
   Available = Available - Request[i]
   Allocation[i] = Allocation[i] + Request[i]
   Need[i] = Need[i] - Request[i]

4. Run Safety Algorithm:
   If safe: Grant request
   If unsafe: Restore old state, deny request
```

## Complete Example

### Initial State

**Resources**: A=10, B=5, C=7

| Process | Allocation | Max   | Need  |
| ------- | ---------- | ----- | ----- |
| P0      | 0 1 0      | 7 5 3 | 7 4 3 |
| P1      | 2 0 0      | 3 2 2 | 1 2 2 |
| P2      | 3 0 2      | 9 0 2 | 6 0 0 |
| P3      | 2 1 1      | 2 2 2 | 0 1 1 |
| P4      | 0 0 2      | 4 3 3 | 4 3 1 |

**Available**: [3, 3, 2]

### Safety Check

1. Work = [3, 3, 2]
2. P1: Need[1,2,2] ≤ Work[3,3,2]? Yes
   - Work = [3,3,2] + [2,0,0] = [5, 3, 2]
3. P3: Need[0,1,1] ≤ Work[5,3,2]? Yes
   - Work = [5,3,2] + [2,1,1] = [7, 4, 3]
4. P4: Need[4,3,1] ≤ Work[7,4,3]? Yes
   - Work = [7,4,3] + [0,0,2] = [7, 4, 5]
5. P2: Need[6,0,0] ≤ Work[7,4,5]? Yes
   - Work = [7,4,5] + [3,0,2] = [10, 4, 7]
6. P0: Need[7,4,3] ≤ Work[10,4,7]? Yes
   - Work = [10,4,7] + [0,1,0] = [10, 5, 7]

**Safe Sequence**: <P1, P3, P4, P2, P0>

### Resource Request Example

P1 requests (1, 0, 2):

1. Check: (1,0,2) ≤ Need[1]=(1,2,2)? Yes
2. Check: (1,0,2) ≤ Available=(3,3,2)? Yes
3. Pretend allocate:
   - Available = [2, 3, 0]
   - Allocation[1] = [3, 0, 2]
   - Need[1] = [0, 2, 0]
4. Safety check with new state → Safe
5. **Grant request**

## Limitations

1. **Max claim required**: Processes must declare maximum needs upfront
2. **Fixed resources**: Number of resources must be fixed
3. **Fixed processes**: Number of processes must be fixed
4. **Overhead**: Safety check on every request
5. **Conservative**: May deny safe requests

## Time Complexity

- Safety Algorithm: O(m × n²)
- Resource Request: O(m × n²) (includes safety check)
