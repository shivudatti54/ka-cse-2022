# Storage Management in Operating Systems - Summary

## Key Definitions

- **Seek Time**: The time required to move the disk read/write head to the correct track, typically ranging from 3-12 milliseconds in modern disks.

- **Rotational Latency**: The time waiting for the desired sector to rotate under the read/write head, equal to half the rotation time at average case.

- **Disk Scheduling**: The process of determining the order in which pending I/O requests are serviced to minimize total head movement.

- **External Fragmentation**: Occurs when free storage space is fragmented into small non-contiguous blocks, making it impossible to allocate large contiguous regions.

- **Internal Fragmentation**: Wasted space within allocated blocks due to fixed block sizes or indexing overhead.

- **File System**: The component of an operating system that provides named file access, hierarchical directory organization, and persistent storage management.

## Important Formulas

- **Average Rotational Latency** = (1/2) × (60 seconds / RPM)

- **Average Access Time** = Average Seek Time + Average Rotational Latency + Transfer Time

- **Transfer Time** = (Number of bytes requested) / (Transfer Rate)

- **Maximum File Size (Indexed Allocation)** = Number of pointers per index block × Size of each data block

- **Total Head Movement (FCFS)** = Σ |request_i - request_{i-1}|

## Key Points

1. Disk scheduling algorithms aim to minimize seek time, which is typically the largest component of disk I/O latency.

2. FCFS is simple and fair but performs poorly with scattered requests; SSTF provides better performance but may cause starvation.

3. SCAN (elevator algorithm) moves the head in one direction, servicing all requests, then reverses—providing bounded wait times and preventing starvation.

4. C-SCAN provides uniform response times by servicing requests in only one direction, making it suitable for systems requiring fair access.

5. Free space can be managed using bit vectors (fast but requires memory), linked lists (simple but slow for searching), grouping (for multiple blocks), or counting (for contiguous regions).

6. Contiguous allocation provides excellent sequential access but suffers from external fragmentation and difficulty in file expansion.

7. Linked allocation eliminates external fragmentation but has poor random access performance and reliability issues.

8. Indexed allocation supports direct access but requires extra I/O operations and has overhead for small files.

9. Modern operating systems use hierarchical directories with support for symbolic links to create flexible file organization.

10. The choice of disk scheduling algorithm depends on the workload characteristics, with SCAN/LOOK preferred for high-load systems and SSTF for moderate loads.

## Common Mistakes

1. **Confusing SCAN and C-SCAN**: Remember that SCAN services requests in both directions while C-SCAN only services in one direction and jumps back to the beginning.

2. **Ignoring rotational latency**: Students often focus solely on seek time and forget that rotational latency also significantly impacts disk performance.

3. **Forgetting that SSTF can cause starvation**: While SSTF minimizes head movement, it can permanently delay far-away requests if nearby requests keep arriving.

4. **Confusing internal and external fragmentation**: Internal fragmentation is wasted space within allocated blocks; external fragmentation is free space scattered throughout the disk.

5. **Overlooking the need for index blocks**: When calculating maximum file size in indexed allocation, remember that the index blocks themselves occupy disk space and are not available for user data.