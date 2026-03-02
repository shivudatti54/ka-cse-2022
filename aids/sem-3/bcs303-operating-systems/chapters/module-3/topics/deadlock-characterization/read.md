# Deadlock Detection and Recovery

## Strategy

Allow deadlock to occur, detect it, then recover.

## Detection Algorithm

Similar to Banker's safety algorithm but uses Request instead of Need:

```
1. Work = Available
   Finish[i] = (Allocation[i] == 0)  // No resources held

2. Find i such that:
   - Finish[i] = false
   - Request[i] <= Work

   If no such i, go to step 4

3. Work = Work + Allocation[i]
   Finish[i] = true
   Go to step 2

4. If Finish[i] = false for any i:
   System is in DEADLOCK
   Deadlocked processes: {i | Finish[i] = false}
```

## When to Run Detection?

- On every resource request (high overhead)
- Periodically (e.g., every 5 minutes)
- When CPU utilization drops below threshold

## Recovery Methods

### 1. Process Termination

**Option A**: Abort ALL deadlocked processes

- Simple but expensive (loses all work)

**Option B**: Abort one at a time until deadlock breaks

- Re-run detection after each termination
- Which to terminate? Consider:
  - Priority
  - How long it has been running
  - How many resources it holds
  - How many more it needs
  - Is it interactive or batch?

### 2. Resource Preemption

Take resources from some processes, give to others.

**Issues**:

- **Selecting victim**: Which process to preempt?
- **Rollback**: How to restore safe state?
- **Starvation**: Same process may always be victim

### 3. Rollback

Roll back process to safe checkpoint and restart.
Requires periodic checkpointing.

## Comparison

| Method     | Overhead           | Resource Use       | Complexity |
| ---------- | ------------------ | ------------------ | ---------- |
| Prevention | Low                | Low (restrictions) | Low        |
| Avoidance  | Medium             | Medium             | Medium     |
| Detection  | High (if frequent) | High               | High       |
| Ignore     | None               | Highest            | None       |

## Example

```
5 processes, 3 resource types
Allocation    Request     Available
  A B C         A B C       A B C
P0 0 1 0       0 0 0       0 0 0
P1 2 0 0       2 0 2
P2 3 0 3       0 0 0
P3 2 1 1       1 0 0
P4 0 0 2       0 0 2

Sequence: P0, P2, P3, P1, P4 can finish → No deadlock
```
