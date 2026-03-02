# Deadlock Avoidance - Banker's Algorithm

## Concept

Before granting a resource request, check if the resulting state is **safe**. Only grant if safe.

## Safe State

A state is safe if there exists a sequence of processes that can all complete.

## Banker's Algorithm Data Structures

Given: n processes, m resource types

| Matrix     | Dimensions | Description                          |
| ---------- | ---------- | ------------------------------------ |
| Available  | [m]        | Available instances of each resource |
| Max        | [n×m]      | Maximum demand of each process       |
| Allocation | [n×m]      | Currently allocated to each          |
| Need       | [n×m]      | Remaining need (Max - Allocation)    |

## Safety Algorithm

```
1. Work = Available
 Finish[i] = false for all i

2. Find i such that:
 - Finish[i] = false
 - Need[i] <= Work

 If no such i, go to step 4

3. Work = Work + Allocation[i]
 Finish[i] = true
 Go to step 2

4. If Finish[i] = true for all i:
 System is in SAFE state
 Else: UNSAFE
```

## Resource Request Algorithm

Process Pi requests Request[i]:

```
1. If Request[i] > Need[i]: ERROR (requested more than declared)

2. If Request[i] > Available: Wait (not enough resources)

3. Pretend to allocate:
 Available = Available - Request[i]
 Allocation[i] = Allocation[i] + Request[i]
 Need[i] = Need[i] - Request[i]

4. Run Safety Algorithm:
 If safe: Grant request
 If unsafe: Restore old state, make process wait
```

## Example

```
Processes: P0, P1, P2, P3, P4
Resources: A(10), B(5), C(7)

Allocation Max Need
 A B C A B C A B C
P0 0 1 0 7 5 3 7 4 3
P1 2 0 0 3 2 2 1 2 2
P2 3 0 2 9 0 2 6 0 0
P3 2 1 1 2 2 2 0 1 1
P4 0 0 2 4 3 3 4 3 1

Available: 3 3 2

Safe sequence: P1 → P3 → P4 → P2 → P0
```

## Limitations

1. Processes must declare max needs in advance
2. Number of resources fixed
3. Overhead of safety check for each request
