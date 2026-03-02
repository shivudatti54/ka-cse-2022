# Disk Scheduling Algorithms

## Disk Structure

- **Platter**: Circular disk surface
- **Track**: Concentric circle on platter
- **Sector**: Division of track
- **Cylinder**: Same track on all platters
- **Seek time**: Time to move head to track
- **Rotational latency**: Time for sector to rotate to head

## Seek Time Minimization

Disk scheduling algorithms minimize total head movement.

## Algorithms

### 1. FCFS (First-Come First-Served)

Process requests in arrival order.

**Example**: Head at 53, Queue: 98, 183, 37, 122, 14, 124, 65, 67

```
53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67
Total movement = 640 cylinders
```

### 2. SSTF (Shortest Seek Time First)

Select request closest to current head position.

```
53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183
Total movement = 236 cylinders
```

**Problem**: Starvation of distant requests.

### 3. SCAN (Elevator)

Move head in one direction servicing requests, then reverse.

```
53 → 37 → 14 → 0 → 65 → 67 → 98 → 122 → 124 → 183
(Goes to 0, then reverses)
Total movement = 236 cylinders
```

### 4. C-SCAN (Circular SCAN)

Like SCAN but returns to beginning without servicing.

```
53 → 65 → 67 → 98 → 122 → 124 → 183 → 199 → 0 → 14 → 37
(Goes to end, jumps to 0, continues)
```

More uniform wait time.

### 5. LOOK / C-LOOK

Like SCAN/C-SCAN but only goes to last request, not disk end.

```
LOOK: 53 → 37 → 14 → 65 → 67 → 98 → 122 → 124 → 183
(Reverses at 14, not 0)
```

## Comparison

| Algorithm | Movement | Starvation | Variance |
| --------- | -------- | ---------- | -------- |
| FCFS      | High     | No         | High     |
| SSTF      | Low      | Yes        | Medium   |
| SCAN      | Medium   | No         | Medium   |
| C-SCAN    | Medium   | No         | Low      |
| LOOK      | Low      | No         | Medium   |

## Formula

**Total Seek Time** = Sum of |current - next| for all requests
