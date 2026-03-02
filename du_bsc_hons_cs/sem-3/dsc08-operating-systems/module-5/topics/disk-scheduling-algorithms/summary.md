# Disk Scheduling Algorithms

## Introduction
Disk scheduling is a fundamental concept in Operating Systems that manages the order in which disk I/O requests are served. Since disk access involves mechanical operations (seek time and rotational delay), efficient scheduling significantly impacts system performance. This summary covers all major algorithms as per the Delhi University BSc (Hons) CS syllabus.

## Disk Access Time Components
- **Seek Time**: Time taken to move the read/write head to the correct cylinder
- **Rotational Delay**: Time waiting for the desired sector to rotate under the head
- **Transfer Time**: Time actually transferring data

**Total Access Time = Seek Time + Rotational Delay + Transfer Time**

## Key Algorithms

### 1. FCFS (First Come First Served)
- Serves requests in the order they arrive
- Simple but inefficient; high average seek time

### 2. SSTF (Shortest Seek Time First)
- Selects the request closest to the current head position
- Reduces average seek time; may cause starvation

### 3. SCAN (Elevator Algorithm)
- Head moves in one direction servicing all requests until end
- Then reverses direction
- Fairer than SSTF; reduces starvation

### 4. C-SCAN (Circular SCAN)
- Head moves in one direction servicing requests
- Returns to beginning without servicing on the return trip
- Provides uniform wait time; more uniform service

### 5. LOOK
- Similar to SCAN but doesn't go to the end of the disk
- Head reverses at the last request

### 6. C-LOOK
- Circular version of LOOK
- Head jumps to beginning after reaching last request

## Performance Metrics
- **Throughput**: Requests served per unit time
- **Average Seek Time**: Mean distance head travels
- **Response Time**: Time from request to first service
- **Starvation**: When some requests are never served

## Conclusion
Disk scheduling algorithms balance efficiency, fairness, and throughput. While FCFS is simplest, SSTF offers better performance. SCAN and its variants (C-SCAN, LOOK, C-LOOK) are widely used in real systems due to their predictable behavior and reduced starvation. Understanding these algorithms is essential for optimizing I/O operations in operating systems.

*For exam: Remember the differences, advantages, disadvantages, and which algorithm best suits different scenarios.*