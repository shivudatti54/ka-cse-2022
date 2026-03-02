# Disk Scheduling - Summary

## Key Definitions

- **Disk Scheduling**: The process of ordering I/O requests to minimize seek time and improve disk throughput
- **Seek Time**: Time required to move the disk arm to the correct cylinder/track
- **Rotational Latency**: Time waiting for the desired sector to rotate under the read/write head
- **Starvation**: A condition where some requests may wait indefinitely due to continuous arrival of "closer" requests
- **Track (Cylinder)**: A circular path on the disk surface where data is stored

## Important Formulas

- **Total Seek Distance**: Sum of absolute differences between consecutive head positions
- Total Seek = Σ |request*i - request*{i-1}|

- **Average Seek Time**: Approximately one-third of maximum seek time for randomly distributed requests

- **Rotational Latency**: (1/2) × (60 / RPM) seconds, typically 4-8 ms for 7200 RPM drives

## Key Points

1. Seek time is the dominant component of disk access time (50-80% of total), making disk scheduling crucial for I/O performance.

2. **FCFS** is simple and fair but provides poor performance due to excessive head movement.

3. **SSTF** minimizes arm movement by servicing closest request first but can cause starvation for distant requests.

4. **SCAN (Elevator)** moves in one direction, servicing all requests, then reverses—provides good performance with relatively fair wait times.

5. **C-SCAN** provides uniform service times by servicing requests in one direction only and wrapping around, making it suitable for systems requiring predictable response.

6. **LOOK and C-LOOK** are optimized versions that reverse at the last request rather than the disk edge, avoiding unnecessary head movement.

7. Algorithm selection depends on request distribution: SSTF works well with clustered requests; SCAN/LOOK perform better with distributed requests.

8. Modern operating systems may use more advanced techniques like FCFS-EDF (Earliest Deadline First) that combine request deadlines with spatial locality.

## Common Mistakes

1. **Confusing SCAN and C-SCAN**: SCAN reverses direction at the end; C-SCAN returns to the beginning without servicing requests during return.

2. **Forgetting initial head position**: Always start calculating seek distance from the current head position, not from zero.

3. **Ignoring starvation in SSTF**: While efficient, SSTF can cause indefinite waiting for distant requests.

4. **Assuming all algorithms are always better**: Performance varies with request patterns; FCFS may be preferred in real-time systems for fairness guarantees.

5. **Not considering physical disk layout**: In reality, factors like controller queuing, disk cache, and command queuing (NCQ) affect actual performance significantly.
