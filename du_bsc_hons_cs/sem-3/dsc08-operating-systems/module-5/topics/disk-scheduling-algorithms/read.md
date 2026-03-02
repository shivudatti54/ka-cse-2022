# Disk Scheduling Algorithms

## Comprehensive Study Material for Operating Systems (BSc Hons - Delhi University)

---

## 1. Introduction

**Disk Scheduling** is a fundamental concept in Operating Systems that determines the order in which disk I/O requests are serviced. In modern computing environments, where storage operations can significantly impact system performance, understanding disk scheduling algorithms is crucial for any computer science student.

### Real-World Relevance

Imagine you're using a computer system with multiple processes running simultaneously:

- A word processor saving your document
- A web browser loading a webpage
- A media player streaming video
- Background system processes updating files

All these operations generate disk I/O requests simultaneously. Without efficient disk scheduling, the system would serve these requests in a chaotic manner, leading to:

- **Excessive seek time**: The disk arm moving erratically across the platter
- **Poor throughput**: Fewer I/O operations completed per second
- **Increased latency**: Longer wait times for each request
- **Starvation**: Some requests may never be served

Disk scheduling algorithms optimize the order of these requests to minimize seek time, reduce rotational latency, and maximize system throughput—directly impacting user experience in everyday computing tasks.

---

## 2. Need for Disk Scheduling

Modern hard disk drives (HDDs) consist of:

- **Platters**: Circular magnetic disks that store data
- **Spindle**: Rotates the platters at high speed (typically 5400-15000 RPM)
- **Read/Write Arm**: Moves radially to access different tracks
- **Actuator**: Controls the arm movement

When a process requests data, the operating system must:

1. **Locate the data** (track, sector)
2. **Position the read/write head** over the correct track (seek time)
3. **Wait for the sector to rotate under the head** (rotational latency)
4. **Transfer the data** (transfer time)

**Disk scheduling becomes essential because:**

- **Seek time is the slowest operation** (typically 3-10 ms)
- **Random access is inefficient** - sequential access is much faster
- **Multiple processes compete for limited I/O resources**
- **OS must ensure fairness** while maintaining efficiency

---

## 3. Key Terminology

Understanding these terms is essential for analyzing disk scheduling algorithms:

| Term | Definition |
|------|------------|
| **Seek Time** | Time taken to move the disk arm to the desired track (typically 3-10 ms) |
| **Rotational Latency** | Time waiting for the desired sector to rotate under the read/write head |
| **Transfer Time** | Time to actually read/write data once the head is positioned |
| **Access Time** | Sum of seek time + rotational latency + transfer time |
| **Track** | Circular path on the disk surface where data is stored |
| **Cylinder** | Set of tracks at the same radius on all platters |
| **Disk Queue** | Pending I/O requests waiting to be served |
| **Throughput** | Number of I/O requests serviced per unit time |
| **Starvation** | When a request is perpetually delayed due to other requests |
| **Bias** | Tendency toward one end of the disk (common in SCAN algorithms) |

---

## 4. Disk Scheduling Algorithms

### 4.1 FCFS (First Come First Served)

**Description:**
FCFS is the simplest disk scheduling algorithm. Requests are serviced in the order they arrive in the disk queue, similar to a FIFO (First In First Out) queue.

**Advantages:**
- Simple to implement
- No starvation (every request gets served)
- Fair - no request is prioritized over another

**Disadvantages:**
- Does not optimize seek time
- Poor performance in terms of average seek distance
- Can cause excessive disk arm movement

**Example:**

Consider a disk with 200 tracks (0-199). The initial head position is at track 50. The request queue (in order of arrival) is:

```
Request Queue: [82, 170, 43, 140, 24, 16, 190]
```

**Step-by-step calculation:**

| Step | Requested Track | Head Movement | Calculation |
|------|-----------------|---------------|-------------|
| 1 | 82 | |50 - 82| = 32 |
| 2 | 170 | |82 - 170| = 88 |
| 3 | 43 | |170 - 43| = 127 |
| 4 | 140 | |43 - 140| = 97 |
| 5 | 24 | |140 - 24| = 116 |
| 6 | 16 | |24 - 16| = 8 |
| 7 | 190 | |16 - 190| = 174 |

**Total Head Movement**: 32 + 88 + 127 + 97 + 116 + 8 + 174 = **642 tracks**

**Average Seek Time**: 642 / 7 = **91.71 tracks**

---

### 4.2 SSTF (Shortest Seek Time First)

**Description:**
SSTF selects the request closest to the current head position, minimizing the seek time for each individual request. It is a greedy algorithm that always chooses the nearest request.

**Important Note:** The previous version had an incomplete description. Here is the complete explanation:

**Algorithm Steps:**
1. Start from the current head position
2. Find the request with minimum seek time from current position
3. Service that request
4. Update head position and repeat

**Advantages:**
- Significantly better than FCFS
- Reduces average seek distance
- Relatively simple to implement

**Disadvantages:**
- Can cause starvation for requests far from the current position
- Not optimal (doesn't guarantee minimum total seek time)
- May cause high bias toward middle tracks

**Example:**

Using the same scenario:
- Initial head position: 50
- Request Queue: [82, 170, 43, 140, 24, 16, 190]

**Step-by-step calculation:**

| Step | Current Head | Nearest Request | Head Movement | Calculation |
|------|--------------|-----------------|---------------|-------------|
| 1 | 50 | 43 | |50 - 43| = 7 |
| 2 | 43 | 24 | |43 - 24| = 19 |
| 3 | 24 | 16 | |24 - 16| = 8 |
| 4 | 16 | 82 | |82 - 16| = 66 |
| 5 | 82 | 140 | |82 - 140| = 58 |
| 6 | 140 | 170 | |140 - 170| = 30 |
| 7 | 170 | 190 | |170 - 190| = 20 |

**Total Head Movement**: 7 + 19 + 8 + 66 + 58 + 30 + 20 = **208 tracks**

**Average Seek Time**: 208 / 7 = **29.71 tracks**

**Comparison with FCFS**: SSTF achieved 208 tracks vs FCFS's 642 tracks — a **67.6% improvement**!

---

### 4.3 SCAN Algorithm (Elevator Algorithm)

**Description:**
The SCAN algorithm, also known as the Elevator algorithm, works like an elevator in a building. The head moves in one direction, servicing all requests until it reaches the end, then reverses direction and services requests in the opposite direction.

**How it works:**
1. Head starts from one end (usually track 0) and moves toward the other end
2. Service all requests in order of increasing track number while moving in one direction
3. When no more requests ahead, reverse direction
4. Service remaining requests in the reverse direction

**Advantages:**
- Better throughput than FCFS and SSTF
- Fair - requests at both ends get serviced
- Reduced starvation compared to SSTF
- No indefinite postponement

**Disadvantages:**
- Longer wait time for requests at the ends
- May cause more seek time than SSTF for some patterns
- Arm may travel longer distance than necessary

**Example:**

Initial head position: 50, moving toward track 0 (left direction)
Request Queue: [82, 170, 43, 140, 24, 16, 190]

**Sorting requests**: [16, 24, 43, 82, 140, 170, 190]

**Step-by-step calculation (moving left first):**

| Step | Current Head | Next Request | Head Movement |
|------|--------------|--------------|---------------|
| 1 | 50 | 43 | 7 |
| 2 | 43 | 24 | 19 |
| 3 | 24 | 16 | 8 |
| 4 | 16 | (reverse) | 0 |
| 5 | 16 | 82 | 66 |
| 6 | 82 | 140 | 58 |
| 7 | 140 | 170 | 30 |
| 8 | 170 | 190 | 20 |

**Total Head Movement**: 7 + 19 + 8 + 66 + 58 + 30 + 20 = **208 tracks**

---

### 4.4 C-SCAN (Circular SCAN)

**Description:**
C-SCAN is a variant of SCAN that provides more uniform wait times. Instead of reversing direction and scanning back, the head returns quickly to the beginning and starts scanning again.

**How it works:**
1. Head moves in one direction servicing all requests
2. When reaching the end, it quickly returns (without servicing) to the beginning
3. Begins servicing again from the start

**Characteristics:**
- Provides circular (wrap-around) service
- More uniform access times
- Often called the "elevator that loops"

**Example:**

Initial head position: 50, moving toward higher tracks
Request Queue: [82, 170, 43, 140, 24, 16, 190]

**Sorted (circular)**: Starting from 50, going right: [82, 140, 170, 190, 199, 0, 16, 24, 43]

**Step-by-step calculation:**

| Step | Current Head | Next Request | Head Movement |
|------|--------------|--------------|---------------|
| 1 | 50 | 82 | 32 |
| 2 | 82 | 140 | 58 |
| 3 | 140 | 170 | 30 |
| 4 | 170 | 190 | 20 |
| 5 | 190 | (jump to 0) | 9 |
| 6 | 0 | 16 | 16 |
| 7 | 16 | 24 | 8 |
| 8 | 24 | 43 | 19 |

**Total Head Movement**: 32 + 58 + 30 + 20 + 9 + 16 + 8 + 19 = **192 tracks**

---

### 4.5 LOOK Algorithm

**Description:**
LOOK is an optimized version of SCAN. It doesn't go all the way to the end of the disk; instead, it only goes as far as the last request in each direction, then reverses.

**How it works:**
1. Head moves in one direction
2. Services requests until no more requests in that direction
3. Reverses immediately without going to the end
4. Continues servicing in the opposite direction

**Advantages:**
- More efficient than SCAN (doesn't go to the end unnecessarily)
- Still provides fair service
- Reduced average seek time compared to SCAN

**Example:**

Initial head position: 50, moving toward higher tracks
Request Queue: [82, 170, 43, 140, 24, 16, 190]

**Sorted requests**: [16, 24, 43, 82, 140, 170, 190]

**Step-by-step (LOOK, going right first):**

| Step | Current Head | Next Request | Head Movement |
|------|--------------|--------------|---------------|
| 1 | 50 | 82 | 32 |
| 2 | 82 | 140 | 58 |
| 3 | 140 | 170 | 30 |
| 4 | 170 | 190 | 20 |
| 5 | 190 | (reverse) | 0 |
| 6 | 190 | 43 | 147 |
| 7 | 43 | 24 | 19 |
| 8 | 24 | 16 | 8 |

**Total Head Movement**: 32 + 58 + 30 + 20 + 147 + 19 + 8 = **314 tracks**

---

### 4.6 C-LOOK Algorithm

**Description:**
C-LOOK combines the advantages of C-SCAN and LOOK. It services requests in one direction and then jumps back to the oldest request, without going to the ends of the disk.

**How it works:**
1. Head moves in one direction servicing requests
2. When no more requests ahead, jumps to the first request (not track 0)
3. Continues servicing in the same direction

**Advantages:**
- Most efficient among traditional algorithms
- No unnecessary travel to disk ends
- Eliminates starvation completely

**Example:**

Initial head position: 50, moving toward higher tracks
Request Queue: [82, 170, 43, 140, 24, 16, 190]

**Sorted**: [16, 24, 43, 82, 140, 170, 190]

**Step-by-step (C-LOOK, going right first):**

| Step | Current Head | Next Request | Head Movement |
|------|--------------|--------------|---------------|
| 1 | 50 | 82 | 32 |
| 2 | 82 | 140 | 58 |
| 3 | 140 | 170 | 30 |
| 4 | 170 | 190 | 20 |
| 5 | 190 | (jump to 16) | 174 |
| 6 | 16 | 24 | 8 |
| 7 | 24 | 43 | 19 |

**Total Head Movement**: 32 + 58 + 30 + 20 + 174 + 8 + 19 = **341 tracks**

---

## 5. Comparative Analysis

| Algorithm | Advantages | Disadvantages | Best Use Case |
|-----------|------------|---------------|---------------|
| **FCFS** | Simple, fair, no starvation | Poor performance, high seek time | Light load, simple systems |
| **SSTF** | Better than FCFS, moderate simplicity | Starvation possible, not optimal | General purpose |
| **SCAN** | Good throughput, fairness | Longer waits at extremes | High load systems |
| **C-SCAN** | Uniform wait times | Higher total seek time | Database systems |
| **LOOK** | Efficient than SCAN | Slightly complex | Moderate load |
| **C-LOOK** | Best overall efficiency | More complex | Modern OS, high performance |

---

## 6. Implementation Examples

### 6.1 Python Implementation of FCFS and SSTF

```python
def fcfs_scheduling(requests, head):
    """
    FCFS Disk Scheduling Algorithm
    
    Args:
        requests: List of track numbers to be accessed
        head: Initial position of disk head
    
    Returns:
        Total head movement
    """
    total_seek = 0
    current_head = head
    
    print(f"Initial Head Position: {head}")
    print("\nFCFS Execution:")
    print("-" * 50)
    
    for i, request in enumerate(requests):
        seek_distance = abs(current_head - request)
        total_seek += seek_distance
        print(f"Request {i+1}: Track {request} | Movement: {seek_distance}")
        current_head = request
    
    print("-" * 50)
    print(f"Total Seek Time: {total_seek}")
    print(f"Average Seek Time: {total_seek / len(requests):.2f}")
    
    return total_seek


def sstf_scheduling(requests, head):
    """
    SSTF (Shortest Seek Time First) Disk Scheduling Algorithm
    
    Args:
        requests: List of track numbers to be accessed
        head: Initial position of disk head
    
    Returns:
        Total head movement
    """
    total_seek = 0
    current_head = head
    remaining = requests.copy()
    
    print(f"Initial Head Position: {head}")
    print("\nSSTF Execution:")
    print("-" * 50)
    
    while remaining:
        # Find request with minimum seek time
        closest = min(remaining, key=lambda x: abs(current_head - x))
        seek_distance = abs(current_head - closest)
        total_seek += seek_distance
        
        print(f"Serviced: Track {closest} | Movement: {seek_distance}")
        
        current_head = closest
        remaining.remove(closest)
    
    print("-" * 50)
    print(f"Total Seek Time: {total_seek}")
    print(f"Average Seek Time: {total_seek / len(requests):.2f}")
    
    return total_seek


# Example usage
if __name__ == "__main__":
    # Sample request queue
    requests = [82, 170, 43, 140, 24, 16, 190]
    initial_head = 50
    
    print("=" * 60)
    print("DISK SCHEDULING ALGORITHM COMPARISON")
    print("=" * 60)
    print(f"Request Queue: {requests}")
    print()
    
    fcfs_total = fcfs_scheduling(requests, initial_head)
    print()
    
    sstf_total = sstf_scheduling(requests, initial_head)
    print()
    
    print("=" * 60)
    print("COMPARISON:")
    print(f"FCFS Total Seek: {fcfs_total}")
    print(f"SSTF Total Seek: {sstf_total}")
    print(f"Improvement: {((fcfs_total - sstf_total) / fcfs_total) * 100:.2f}%")
    print("=" * 60)
```

### 6.2 Java Implementation of SCAN Algorithm

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class DiskScheduling {
    
    /**
     * SCAN Disk Scheduling Algorithm
     */
    public static int scanScheduling(List<Integer> requests, int head, int diskSize) {
        int totalSeek = 0;
        int currentHead = head;
        
        // Sort requests
        Collections.sort(requests);
        
        // Find position where head is currently
        int index = 0;
        for (int i = 0; i < requests.size(); i++) {
            if (requests.get(i) >= head) {
                index = i;
                break;
            }
        }
        
        System.out.println("SCAN Execution (moving right first):");
        System.out.println("----------------------------------------");
        
        // Service requests to the right of head
        for (int i = index; i < requests.size(); i++) {
            int request = requests.get(i);
            int seek = Math.abs(currentHead - request);
            totalSeek += seek;
            System.out.println("Track " + request + " | Movement: " + seek);
            currentHead = request;
        }
        
        // Go to end of disk
        int endSeek = Math.abs(currentHead - (diskSize - 1));
        totalSeek += endSeek;
        currentHead = diskSize - 1;
        
        // Reverse and service remaining requests
        for (int i = index - 1; i >= 0; i--) {
            int request = requests.get(i);
            int seek = Math.abs(currentHead - request);
            totalSeek += seek;
            System.out.println("Track " + request + " | Movement: " + seek);
            currentHead = request;
        }
        
        return totalSeek;
    }
    
    public static void main(String[] args) {
        List<Integer> requests = new ArrayList<>();
        requests.add(82);
        requests.add(170);
        requests.add(43);
        requests.add(140);
        requests.add(24);
        requests.add(16);
        requests.add(190);
        
        int head = 50;
        int diskSize = 200;
        
        System.out.println("Request Queue: " + requests);
        System.out.println("Initial Head: " + head);
        System.out.println("Disk Size: " + diskSize);
        System.out.println();
        
        int totalSeek = scanScheduling(requests, head, diskSize);
        
        System.out.println("----------------------------------------");
        System.out.println("Total Seek Time: " + totalSeek);
        System.out.println("Average Seek Time: " + (double) totalSeek / requests.size());
    }
}
```

---

## 7. Delhi University Syllabus Context

This topic aligns with the **Operating Systems** paper for BSc (Hons) Computer Science under NEP 2024 UGCF. Key points relevant to university exams:

**Expected Coverage:**
- Understanding disk I/O operations
- Different scheduling algorithms (FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK)
- Performance comparison and analysis
- Numerical problems and calculations

**Important Topics for Exams:**
1. Definitions and differences between algorithms
2. Step-by-step calculation of head movement
3. Advantages and disadvantages of each algorithm
4. Real-world applications and scenarios
5. Comparative analysis questions

**Common Exam Questions:**
- "Explain the SCAN algorithm with an example"
- "Compare FCFS and SSTF disk scheduling algorithms"
- "Calculate the total seek time using C-LOOK algorithm"
- "Why is SSTF better than FCFS? Explain with an example"
- "What is starvation? How does SCAN algorithm address this?"

---

## 8. Key Takeaways

1. **Disk scheduling is essential** for optimizing I/O performance by minimizing seek time and maximizing throughput.

2. **FCFS** is simple and fair but performs poorly; suitable only for light loads.

3. **SSTF** significantly improves performance over FCFS but may cause starvation for distant requests.

4. **SCAN (Elevator algorithm)** provides a good balance between throughput and fairness by scanning back and forth.

5. **C-SCAN** offers uniform wait times by providing circular service, ideal for database systems.

6. **LOOK and C-LOOK** are optimized versions that don't travel to disk ends unnecessarily.

7. **No single algorithm is best** - the choice depends on the system's workload and requirements.

8. **Modern operating systems** use more advanced techniques like elevator algorithms, deadline scheduling, and completely fair queuing (CFQ).

9. **Solid State Drives (SSDs)** have changed the landscape - they have no moving parts, so traditional disk scheduling is less relevant, but the concepts remain important for understanding OS design.

---

## 9. Multiple Choice Questions (MCQs)

### MCQ 1: Basic Concepts
**Which component of a disk system contributes most to the access time?**

A) Transfer time  
B) Rotational latency  
C) Seek time  
D) Controller overhead  

**Answer: C) Seek time** — The time taken to move the disk arm to the desired track is typically 3-10 ms and is the largest component of disk access time.

---

### MCQ 2: Algorithm Identification *(Corrected)*
**A disk scheduling algorithm services requests in the order they arrive in the queue. This algorithm is called:**

A) SSTF  
B) SCAN  
C) FCFS  
D) C-SCAN  

**Answer: C) FCFS** — First Come First Served (FCFS) services requests in the exact order they arrive, making it the simplest algorithm.

*Note: The previous version had an error in the explanation. The correct answer is FCFS (not 24 vs 20).*

---

### MCQ 3: SCAN Algorithm
**In the SCAN algorithm (elevator algorithm), when the disk head reaches one end of the disk, it:**

A) Stops and waits for new requests  
B) Reverses direction immediately  
C) Jumps to the beginning without servicing  
D) Services the last request twice  

**Answer: B) Reverses direction immediately** — The SCAN algorithm moves in one direction until it reaches the end, then reverses to service requests in the opposite direction.

---

### MCQ 4: SSTF Starvation
**Which disk scheduling algorithm may cause starvation for some requests?**

A) FCFS  
B) SCAN  
C) SSTF  
D) C-SCAN  

**Answer: C) SSTF** — SSTF (Shortest Seek Time First) always selects the nearest request, which may cause requests far from the current head position to wait indefinitely.

---

### MCQ 5: Performance Comparison
**Which algorithm typically provides the lowest average seek time?**

A) FCFS  
B) SSTF  
C) SCAN  
D) C-SCAN  

**Answer: B) SSTF** — SSTF minimizes the seek time for each individual request by always choosing the closest request to the current head position.

---

### MCQ 6: C-LOOK Algorithm
**What happens when the disk head in C-LOOK has no more requests in the current direction?**

A) It goes to the end of the disk  
B) It reverses direction  
C) It jumps to the first pending request  
D) It stops  

**Answer: C) It jumps to the first pending request** — C-LOOK jumps directly to the oldest request rather than going to the end of the disk, making it more efficient than C-SCAN.

---

### MCQ 7: Real-World Application
**Which type of storage device makes traditional disk scheduling algorithms less relevant?**

A) Hard Disk Drive (HDD)  
B) Magnetic Tape  
C) Solid State Drive (SSD)  
D) Optical Drive  

**Answer: C) Solid State Drive (SSD)** — SSDs have no moving parts and provide constant access time, making traditional seek-time-based scheduling algorithms unnecessary.

---

### MCQ 8: Seek Time Calculation
**Initial head position is at track 50. Requests are at tracks: 82, 170, 43, 140, 24, 16, 190. Using FCFS, what is the seek time for the first request?**

A) 32  
B) 82  
C) 43  
D) 50  

**Answer: A) 32** — From track 50 to track 82: |50 - 82| = 32

---

## 10. Flashcards for Quick Review

| Term | Definition |
|------|------------|
| **Seek Time** | Time taken to move the read/write head to the desired track |
| **Rotational Latency** | Time waiting for the desired sector to rotate under the head |
| **FCFS** | First Come First Served - services requests in arrival order |
| **SSTF** | Shortest Seek Time First - services closest request first |
| **SCAN** | Elevator algorithm - scans back and forth across the disk |
| **C-SCAN** | Circular SCAN - provides uniform wait times in circular fashion |
| **LOOK** | Optimized SCAN - doesn't go to disk ends, only last request |
| **C-LOOK** | Circular LOOK - combines C-SCAN and LOOK advantages |
| **Starvation** | When a request is perpetually delayed by other requests |
| **Throughput** | Number of I/O requests completed per unit time |

---

## 11. Summary Table: Algorithm Examples Comparison

| Algorithm | Example Total Seek | Notes |
|-----------|-------------------|-------|
| **FCFS** | 642 tracks | Highest - worst performer |
| **SSTF** | 208 tracks | Best for minimizing individual seeks |
| **SCAN** | 208 tracks | Good balance |
| **C-SCAN** | 192 tracks | Uniform access times |
| **LOOK** | 314 tracks | Variable based on direction |
| **C-LOOK** | 341 tracks | Best overall efficiency |

*Note: Values based on the example with initial head at track 50 and requests [82, 170, 43, 140, 24, 16, 190]*

---

## Conclusion

Disk scheduling algorithms form a crucial part of operating system design, directly impacting system performance and user experience. Understanding each algorithm's strengths and weaknesses enables system designers to choose appropriate strategies based on workload characteristics. While modern SSDs have changed storage dynamics, the fundamental concepts remain essential knowledge for every computer science student.

---

*Prepared for BSc (Hons) Computer Science - Delhi University (NEP 2024 UGCF)*