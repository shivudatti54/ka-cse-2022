# Disk Scheduling Algorithms

## Introduction

Disk scheduling is a fundamental concept in operating systems that determines the order in which disk I/O requests are serviced. When multiple processes make simultaneous requests to read from or write to the disk, the operating system must decide the optimal sequence to minimize seek time—the time taken by the disk's read/write head to move to the correct track. This optimization is crucial because disk I/O is typically the slowest operation in a computer system, often becoming the bottleneck in overall system performance.

In the context of University of Delhi's Computer Science curriculum, understanding disk scheduling algorithms is essential for several reasons. First, these algorithms demonstrate how real-world systems balance efficiency, fairness, and complexity. Second, they appear frequently in university examinations, testing students' conceptual understanding and problem-solving abilities. Third, with the advent of modern storage systems including SSDs (which use different mechanisms but still benefit from these concepts), the fundamental principles of request scheduling remain highly relevant.

This topic builds upon your understanding of operating system fundamentals, particularly I/O management and the physical structure of magnetic disks. By mastering these algorithms, you will be able to analyze and compare different approaches to disk scheduling, understand trade-offs between throughput and response time, and apply these concepts to system design problems.

## Key Concepts

### Disk Structure and Terminology

Before diving into algorithms, it's essential to understand the physical characteristics of a disk. A magnetic disk consists of multiple concentric circles called **tracks**, and each track is divided into **sectors**. The **cylinder** refers to all tracks with the same radius across different platters. The **seek time** is the time taken for the disk arm to move to the desired cylinder, **rotational delay** is the time waiting for the correct sector to rotate under the read/write head, and **transfer time** is the time to actually read or write data. Disk scheduling algorithms primarily aim to minimize seek time.

### FCFS (First Come First Served)

FCFS is the simplest disk scheduling algorithm, processing requests in the exact order they arrive. While fair and easy to implement, it often results in poor performance because it ignores the physical location of requested blocks. If requests are scattered across the disk, the head must make extensive back-and-forth movements, leading to high average seek time.

### SSTF (Shortest Seek Time First)

SSTF selects the request closest to the current head position, minimizing the seek distance for each individual request. This greedy approach significantly reduces total seek time compared to FCFS. However, SSTF can cause **starvation**—requests far from the current position may never be serviced if new requests keep appearing closer to the head. It's important to note that SSTF is not optimal (unlike what students sometimes assume); it only provides a local optimization.

### SCAN Algorithm

The SCAN algorithm, also known as the **elevator algorithm**, moves the disk head in one direction servicing all requests until it reaches the end, then reverses direction. This back-and-forth pattern resembles how an elevator moves in a building. SCAN provides more uniform wait times than SSTF because requests at the ends of the disk are serviced as frequently as those in the middle. The head always moves in a predictable direction, making it suitable for systems where response time variance matters.

### C-SCAN (Circular SCAN)

C-SCAN is a variant that services requests in one direction only. When the head reaches the end of the disk, it returns to the beginning without servicing any requests on the return trip. This creates a more uniform waiting time because all requests are serviced in a single pass, providing a "carousel" effect. However, C-SCAN may result in slightly higher average seek time than SCAN because it doesn't exploit the opportunity to service requests while returning to the start.

### LOOK Algorithm

LOOK is essentially SCAN but without going to the extreme ends of the disk. Instead, the head only travels as far as the last request in each direction. This optimization avoids unnecessary seeks to empty portions of the disk, improving efficiency. In practice, most modern implementations use LOOK rather than pure SCAN.

### C-LOOK (Circular LOOK)

C-LOOK combines the concepts of C-SCAN and LOOK—the head services requests in one direction until the last request, then jumps back to service remaining requests from the beginning. This provides the benefits of both approaches: uniform wait times and avoiding unnecessary travel to disk edges.

### Evaluation Metrics

When comparing algorithms, consider: **throughput** (number of requests serviced per time unit), **average seek time** (mean distance the head travels), **response time** (time from request to service completion), and **fairness** (whether any request can suffer indefinite postponement). Different algorithms excel in different metrics, which is why modern operating systems often use more sophisticated approaches or combinations.

## Examples

### Example 1: FCFS Calculation

**Problem**: Consider a disk with 200 tracks (0-199). The read/write head currently at track 50 and the following requests arrive in order: 95, 180, 34, 119, 11, 66, 199. Calculate the total head movement and average seek time using FCFS.

**Solution**:

| Request | Head Position | Movement |
|---------|---------------|----------|
| Start   | 50            | -        |
| 95      | 50 → 95       | 45       |
| 180     | 95 → 180      | 85       |
| 34      | 180 → 34      | 146      |
| 119     | 34 → 119      | 85       |
| 11      | 119 → 11      | 108      |
| 199     | 11 → 199      | 188      |

Total head movement = 45 + 85 + 146 + 85 + 108 + 188 = 657 tracks

Average seek time = 657 / 7 = 93.86 tracks

### Example 2: SSTF Calculation

**Problem**: Using the same scenario, calculate using SSTF.

**Solution**: Starting at track 50, the closest request is 34 (distance 16), then 11 (distance 23), then 66 (distance 55), then 95 (distance 29), then 119 (distance 24), then 180 (distance 61), then 199.

| Request | Head Position | Movement |
|---------|---------------|----------|
| Start   | 50            | -        |
| 34      | 50 → 34       | 16       |
| 11      | 34 → 11       | 23       |
| 66      | 11 → 66       | 55       |
| 95      | 66 → 95       | 29       |
| 119     | 95 → 119      | 24       |
| 180     | 119 → 180     | 61       |
| 199     | 180 → 199     | 19       |

Total head movement = 16 + 23 + 55 + 29 + 24 + 61 + 19 = 227 tracks

Average seek time = 227 / 7 = 32.43 tracks

**Comparison**: SSTF reduces total movement from 657 to 227 tracks—a 65% improvement!

### Example 3: SCAN and C-SCAN

**Problem**: Using the same requests with the head starting at 50 and moving toward higher track numbers, calculate using SCAN and C-SCAN.

**Solution - SCAN**: Head moves from 50 toward 199, servicing requests at 95, 119, 180, 199, then reverses to service 66, 34, 11.

| Request | Head Position | Movement |
|---------|---------------|----------|
| Start   | 50            | -        |
| 95      | 50 → 95       | 45       |
| 119     | 95 → 119      | 24       |
| 180     | 119 → 180     | 61       |
| 199     | 180 → 199     | 19       |
| 66      | 199 → 66      | 133      |
| 34      | 66 → 34       | 32       |
| 11      | 34 → 11       | 23       |

Total = 45 + 24 + 61 + 19 + 133 + 32 + 23 = 337 tracks

**Solution - C-SCAN**: Head moves from 50 to 199, servicing all requests, then jumps back to beginning and services remaining.

| Request | Head Position | Movement |
|---------|---------------|----------|
| Start   | 50            | -        |
| 95      | 50 → 95       | 45       |
| 119     | 95 → 119      | 24       |
| 180     | 119 → 180     | 61       |
| 199     | 180 → 199     | 19       |
| 11      | 199 → 0 → 11  | 199 + 11 = 210 |
| 34      | 11 → 34       | 23       |
| 66      | 34 → 66       | 32       |

Total = 45 + 24 + 61 + 19 + 210 + 23 + 32 = 414 tracks

## Exam Tips

1. **Always specify the initial head direction** for SCAN/C-SCAN/LOOK algorithms—this significantly affects the answer.

2. **Calculate total head movement first**, then divide by number of requests for average seek time.

3. **Remember that FCFS has no starvation** but poor performance, while SSTF has potential starvation but better performance.

4. **SCAN vs C-SCAN**: SCAN generally has lower average seek time but C-SCAN provides more uniform waiting times.

5. **LOOK and C-LOOK are practical versions**—they don't go to the extreme ends, just to the last request.

6. **For numerical problems**, always list requests in order of servicing with track numbers and calculate movement between consecutive tracks.

7. **Understand the "elevator" analogy** for SCAN—it services requests as it passes by, like an elevator picking up passengers.

8. **Modern context**: While SSDs don't use mechanical seek time, these algorithms apply to virtual memory page scheduling and network request routing.

9. **Fairness consideration**: In exams, if a question asks about fairness, remember FCFS is the fairest algorithm.

10. **Common mistake**: Students often forget to include the head's initial position in calculations—there's no "movement" to the first request, only the distance from start position.