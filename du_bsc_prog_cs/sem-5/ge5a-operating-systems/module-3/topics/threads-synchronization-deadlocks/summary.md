# Threads Synchronization & Deadlocks

## Introduction

In multi-threaded applications, multiple threads execute concurrently while sharing resources like memory, files, and variables. This concurrent execution introduces critical challenges: **race conditions** (when multiple threads access shared data simultaneously) and **deadlocks** (when threads wait indefinitely for resources held by each other). Proper synchronization is essential for maintaining data consistency and system stability.

---

## Thread Synchronization

### Why Synchronization is Needed
- Threads share memory space and system resources
- Uncoordinated access leads to **race conditions**
- Results in inconsistent or corrupted data

### Synchronization Mechanisms

- **Mutual Exclusion (Mutex)**
  - Ensures only one thread accesses critical section at a time
  - Lock/unlock operations protect shared resources

- **Semaphores**
  - Integer-based counter for resource management
  - **Binary semaphore**: like mutex (0 or 1)
  - **Counting semaphore**: manages multiple identical resources

- **Monitors**
  - High-level synchronization construct
  - Encapsulates shared data with operations and condition variables

- **Condition Variables**
  - Allow threads to wait until a specific condition is true
  - Used with mutexes for complex synchronization patterns

- **Spinlocks**
  - Lock that repeatedly checks for lock availability
  - Useful for short wait times

---

## Deadlocks

### Definition
A deadlock occurs when two or more threads are permanently blocked, each waiting for a resource held by another.

### Four Necessary Conditions (Coffman Conditions)
- **Mutual Exclusion**: At least one resource must be non-shareable
- **Hold and Wait**: Threads hold resources while waiting for others
- **No Preemption**: Resources cannot be forcibly taken
- **Circular Wait**: Circular chain of waiting threads

### Handling Deadlocks

| Strategy | Description |
|----------|-------------|
| **Prevention** | Eliminate one of the four conditions |
| **Avoidance** | Use algorithms (e.g., Banker's Algorithm) to safely allocate resources |
| **Detection** | Periodically check for deadlock existence |
| **Recovery** | Terminate threads or preempt resources |

### Banker's Algorithm
- Used for deadlock avoidance
- Requires knowledge of maximum resource needs
- Ensures safe state before resource allocation

### Resource Allocation Graph (RAG)
- **Representation**: Processes (circles) → Resources (rectangles)
- **Request edge**: Process → Resource
- **Assignment edge**: Resource → Process
- **Cycle without resource**: Implies deadlock

---

## Important Patterns to Remember

- **Producer-Consumer Problem**: Bounded buffer synchronization
- **Readers-Writers Problem**: Multiple readers OR single writer access
- **Dining Philosophers Problem**: Classic deadlock demonstration

---

## Conclusion

Thread synchronization is fundamental to operating system design. While synchronization mechanisms prevent data inconsistencies, they can lead to deadlocks if improperly designed. Understanding the conditions for deadlock and employing appropriate prevention/avoidance strategies ensures efficient multi-threaded program execution. For exams, remember the four Coffman conditions and Banker's algorithm as key concepts.

*Reference: Delhi University BSc (Hons) CS - Operating Systems Syllabus, NEP 2024*