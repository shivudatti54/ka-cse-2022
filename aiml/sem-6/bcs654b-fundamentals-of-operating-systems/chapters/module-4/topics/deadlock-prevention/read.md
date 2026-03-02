# Deadlock Prevention

## Strategy

Ensure at least ONE of the four necessary conditions cannot hold.

## Breaking Each Condition

### 1. Mutual Exclusion

**Cannot break for non-shareable resources** (printers, tape drives).
Can use spooling to make resource appear shareable.

### 2. Hold and Wait

**Solution A**: Request all resources at once before execution.

```
acquire(R1, R2, R3);  // All or none
// Use resources
release_all();
```

**Problem**: Low resource utilization, starvation possible.

**Solution B**: Release all before requesting more.

```
release_all();
request(new_resources);
```

### 3. No Preemption

**Solution**: If request fails, release all held resources.

```
if (request(R3) fails):
    release(R1, R2);
    retry_later();
```

**Works for**: CPU, memory (can save/restore state).
**Doesn't work for**: Printers, tape drives.

### 4. Circular Wait

**Solution**: Impose ordering on resources. Request in increasing order.

```
Resources ordered: R1 < R2 < R3 < R4
Process must request R1 before R2, etc.
```

**Why it works**: If P1 holds Ri and waits for Rj where j > i, and P2 holds Rj, P2 cannot be waiting for Ri (would violate ordering).

## Comparison

| Condition        | Prevention Method   | Drawback              |
| ---------------- | ------------------- | --------------------- |
| Mutual Exclusion | Spooling            | Limited applicability |
| Hold and Wait    | Request all at once | Low utilization       |
| No Preemption    | Release if denied   | Not always possible   |
| Circular Wait    | Resource ordering   | Inconvenient          |

## Most Common: Circular Wait Prevention

Resource ordering is practical and widely used.
