# Operating System as a Resource Manager

## Introduction

An Operating System (OS) serves as the fundamental interface between computer hardware and user applications. Among its many roles, the most critical function is **resource management** — the coordinated allocation, monitoring, and deallocation of physical and logical resources to ensure efficient, fair, and secure operation of the entire computing system.

In today's computing environment, where multiple processes run concurrently on a single machine, effective resource management is paramount. Consider a modern smartphone running multiple apps simultaneously: the OS must manage CPU time, memory, I/O devices, and network bandwidth across all applications without any single app monopolizing resources. Similarly, on a university computer lab server handling requests from dozens of students, the OS must ensure each student receives fair CPU time, memory allocation, and disk access.

This study material comprehensively covers the Operating System's role as a Resource Manager, aligned with the Delhi University NEP 2024 UGCF syllabus for BSc (Hons) Computer Science.

---

## 1. Understanding Resources in an Operating System

### 1.1 What is a Resource?

A **resource** is any component of the computer system that is required by processes to complete their execution. Resources can be classified into two categories:

| Resource Type | Examples | Characteristics |
|---------------|----------|-----------------|
| **Physical Resources** | CPU, RAM, Hard Disk, Printer, Keyboard, Display | Hardware components with finite capacity |
| **Logical Resources** | Files, Sockets, Semaphores, Locks, Process IDs | Abstract entities managed by the OS |

### 1.2 Why Resource Management is Essential

Without proper resource management, several problems arise:

- **Starvation**: Some processes never receive necessary resources
- **Deadlock**: Processes permanently block each other waiting for resources
- **Inefficiency**: Resources remain idle while others are overutilized
- **Security Vulnerabilities**: Unauthorized access to sensitive resources
- **System Instability**: Crash due to resource exhaustion

---

## 2. Core Functions of OS as Resource Manager

### 2.1 Resource Allocation and Deallocation

The OS must track which resources are currently in use, by which process, and ensure proper allocation and release.

**Allocation Strategies:**

1. **Static Allocation**: Resources assigned before process execution begins
2. **Dynamic Allocation**: Resources requested during execution

**Key Data Structures:**

```c
// Simple Resource Control Block structure
typedef struct {
    int resource_id;
    int total_instances;      // Total available
    int available_instances;  // Currently free
    int allocated_processes[MAX_PROCESSES]; // PIDs using this resource
    BOOL is_protected;        // Access control flag
} ResourceControlBlock;

// Process Control Block with resource information
typedef struct {
    int pid;
    int priority;
    int allocated_resources[MAX_RESOURCES];
    int needed_resources[MAX_RESOURCES];
    PCB_STATE state;
} PCB;
```

**Example: Memory Allocation in C**

```c
#include <stdio.h>
#include <stdlib.h>

// Simulating dynamic memory allocation (malloc)
int main() {
    // Requesting memory from OS heap
    int *array = (int*)malloc(10 * sizeof(int));
    
    if (array == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    
    // Using the allocated memory
    for (int i = 0; i < 10; i++) {
        array[i] = i * 10;
    }
    
    // OS reclaims memory when freed
    free(array);  // Deallocation
    
    return 0;
}
```

### 2.2 Resource Protection and Security

The OS must prevent unauthorized access to resources, ensuring isolation between processes and protecting critical system resources.

**Protection Mechanisms:**

1. **User Mode vs Kernel Mode**: Privileged operations restricted to kernel mode
2. **Memory Protection**: MMU (Memory Management Unit) enforces boundaries
3. **Access Control Lists (ACL)**: Define permissions for resources
4. **Capabilities**: Token-based access rights

**Example: File Permission System (Linux/Unix)**

```bash
# File permissions demonstrate OS resource protection
-rw-r--r--  1 student  student   1024 Jan 15 10:30 example.txt

# Breakdown:
# - : Regular file
# rw- : Owner (student) can read and write
# r-- : Group members can read only
# r-- : Others can read only
```

The OS enforces these permissions through system calls (`open()`, `read()`, `write()`), checking user credentials before granting access.

### 2.3 Resource Sharing

Modern OS must enable controlled sharing of resources among multiple processes efficiently.

**Types of Sharing:**

| Type | Description | Example |
|------|-------------|---------|
| **Time-Sharing** | Resources used by different processes at different times | CPU scheduling |
| **Space-Sharing** | Resources partitioned for simultaneous use | Memory partitioning |
| **Concurrent Access** | Multiple processes access simultaneously | File systems, databases |

**Example: Shared Memory (POSIX)**

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/shm.h>

int main() {
    key_t key = ftok("/tmp", 'R');  // Generate unique key
    int shmid = shmget(key, 1024, 0666 | IPC_CREAT);  // Create shared memory
    
    // Attach to shared memory
    char *str = (char*) shmat(shmid, (void*)0, 0);
    
    // Write to shared memory (Process A)
    strcpy(str, "Hello from OS Resource Manager!");
    
    printf("Data written to shared memory: %s\n", str);
    
    // Detach from shared memory
    shmdt(str);
    
    return 0;
}
```

### 2.4 Abstraction and Virtualization

The OS hides hardware complexity through abstraction, providing simple interfaces to complex hardware.

**Levels of Abstraction:**

1. **Physical to Logical**: Hardware → Device Drivers → OS APIs → Applications
2. **Virtual Memory**: Physical RAM → Virtual Address Space
3. **Virtual CPUs**: Multiple processes appear to have dedicated processors
4. **Virtual Machines**: Complete hardware simulation for OS isolation

**Example: Virtual Memory Concept**

```
Physical Memory (4GB):
┌─────────────────────────────────┐
│  Process 1 (Virtual 4GB)        │
│  ┌─────────────────────────┐    │
│  │ Maps to Physical: 0-1GB │    │
│  └─────────────────────────┘    │
├─────────────────────────────────┤
│  Process 2 (Virtual 4GB)        │
│  ┌─────────────────────────┐    │
│  │ Maps to Physical: 1-3GB │    │
│  └─────────────────────────┘    │
├─────────────────────────────────┤
│  Kernel Space                   │
└─────────────────────────────────┘

Each process believes it has exclusive access to 4GB memory!
```

---

## 3. CPU Scheduling — Core Resource Management

The CPU is the most precious resource. CPU scheduling determines which process gets CPU time and for how long.

### 3.1 Scheduling Criteria

- **CPU Utilization**: Keep CPU as busy as possible
- **Throughput**: Number of processes completed per unit time
- **Turnaround Time**: Time from submission to completion
- **Waiting Time**: Time spent in ready queue
- **Response Time**: Time from request to first response

### 3.2 Scheduling Algorithms

#### First-Come, First-Served (FCFS)

```c
// FCFS Scheduling Algorithm Simulation
#include <stdio.h>

typedef struct {
    int pid;
    int arrival_time;
    int burst_time;
    int waiting_time;
    int turnaround_time;
} Process;

void fcfs(Process processes[], int n) {
    int current_time = 0;
    float total_waiting = 0;
    
    printf("\nFCFS Scheduling:\n");
    printf("PID\tAT\tBT\tWT\tTAT\n");
    
    for (int i = 0; i < n; i++) {
        // Wait if process arrives later
        if (current_time < processes[i].arrival_time) {
            current_time = processes[i].arrival_time;
        }
        
        processes[i].waiting_time = current_time - processes[i].arrival_time];
        current_time += processes[i].burst_time;
        processes[i].turnaround_time = processes[i].waiting_time + processes[i].burst_time;
        
        total_waiting += processes[i].waiting_time;
        
        printf("%d\t%d\t%d\t%d\t%d\n", 
               processes[i].pid, 
               processes[i].arrival_time,
               processes[i].burst_time,
               processes[i].waiting_time,
               processes[i].turnaround_time);
    }
    
    printf("Average Waiting Time: %.2f\n", total_waiting / n);
}

int main() {
    Process processes[] = {{1, 0, 10}, {2, 1, 5}, {3, 2, 8}};
    fcfs(processes, 3);
    return 0;
}
```

#### Shortest Job First (SJF) — Non-Preemptive

```c
// SJF Scheduling
void sjf(Process processes[], int n) {
    // Sort by burst time (selection sort)
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (processes[j].burst_time < processes[min_idx].burst_time) {
                min_idx = j;
            }
        }
        // Swap
        Process temp = processes[i];
        processes[i] = processes[min_idx];
        processes[min_idx] = temp;
    }
    
    // Calculate waiting and turnaround times
    int current_time = 0;
    for (int i = 0; i < n; i++) {
        processes[i].waiting_time = current_time;
        current_time += processes[i].burst_time;
        processes[i].turnaround_time = processes[i].waiting_time + processes[i].burst_time;
    }
}
```

#### Round Robin (Preemptive)

```c
// Round Robin Scheduling (Simplified)
void roundRobin(Process processes[], int n, int quantum) {
    int remaining_bt[n];
    for (int i = 0; i < n; i++) remaining_bt[i] = processes[i].burst_time;
    
    int current_time = 0;
    int completed = 0;
    
    while (completed < n) {
        for (int i = 0; i < n; i++) {
            if (remaining_bt[i] > 0) {
                int time_slice = (remaining_bt[i] < quantum) ? 
                                  remaining_bt[i] : quantum;
                
                remaining_bt[i] -= time_slice;
                current_time += time_slice;
                
                if (remaining_bt[i] == 0) {
                    processes[i].turnaround_time = current_time;
                    processes[i].waiting_time = current_time - processes[i].burst_time;
                    completed++;
                }
            }
        }
    }
}
```

### 3.3 Comparison of Scheduling Algorithms

| Algorithm | Advantages | Disadvantages | Best For |
|-----------|------------|---------------|----------|
| FCFS | Simple, Fair | Long waiting for short processes | Batch systems |
| SJF | Minimum average waiting | Starvation, Requires burst time prediction | When burst times known |
| Round Robin | Good response time, Fair | High context switch overhead | Time-sharing systems |
| Priority | Important processes first | Starvation | Real-time systems |

---

## 4. Deadlock Handling

A **deadlock** occurs when two or more processes are waiting indefinitely for resources held by each other.

### 4.1 Conditions for Deadlock (Coffman Conditions)

1. **Mutual Exclusion**: Only one process can use a resource at a time
2. **Hold and Wait**: Process holds resources while waiting for others
3. **No Preemption**: Resources cannot be forcibly taken away
4. **Circular Wait**: Circular chain of processes waiting for resources

### 4.2 Deadlock Handling Strategies

| Strategy | Description | Overhead |
|----------|-------------|----------|
| **Detection** | Allow deadlocks, then detect and recover | High |
| **Prevention** | Ensure at least one condition cannot hold | Low |
| **Avoidance** | Banker's Algorithm to avoid unsafe states | Medium |
| **Ignorance** | Pretend deadlocks don't occur (UNIX approach) | Minimal |

### 4.3 Banker's Algorithm (Avoidance)

```c
// Banker's Algorithm Implementation
#include <stdio.h>

#define MAX_PROCESSES 5
#define MAX_RESOURCES 3

int available[MAX_RESOURCES];
int maximum[MAX_PROCESSES][MAX_RESOURCES];
int allocation[MAX_PROCESSES][MAX_RESOURCES];
int need[MAX_PROCESSES][MAX_RESOURCES];

// Initialize the system
void init() {
    // Available resources
    available[0] = 3; available[1] = 3; available[2] = 2;
    
    // Maximum demand
    int max[MAX_PROCESSES][MAX_RESOURCES] = {
        {7, 5, 3}, {3, 2, 2}, {9, 0, 2}, {2, 2, 2}, {4, 3, 3}
    };
    
    // Current allocation
    int alloc[MAX_PROCESSES][MAX_RESOURCES] = {
        {0, 1, 0}, {3, 0, 2}, {3, 0, 2}, {2, 1, 1}, {0, 0, 2}
    };
    
    for (int i = 0; i < MAX_PROCESSES; i++) {
        for (int j = 0; j < MAX_RESOURCES; j++) {
            maximum[i][j] = max[i][j];
            allocation[i][j] = alloc[i][j];
            need[i][j] = maximum[i][j] - allocation[i][j];
        }
    }
}

// Check if safe state exists
int isSafe() {
    int work[MAX_RESOURCES];
    int finish[MAX_PROCESSES] = {0};
    
    for (int i = 0; i < MAX_RESOURCES; i++) 
        work[i] = available[i];
    
    for (int count = 0; count < MAX_PROCESSES; count++) {
        int found = 0;
        for (int i = 0; i < MAX_PROCESSES; i++) {
            if (!finish[i]) {
                int can_allocate = 1;
                for (int j = 0; j < MAX_RESOURCES; j++) {
                    if (need[i][j] > work[j]) {
                        can_allocate = 0;
                        break;
                    }
                }
                
                if (can_allocate) {
                    for (int j = 0; j < MAX_RESOURCES; j++)
                        work[j] += allocation[i][j];
                    finish[i] = 1;
                    found = 1;
                }
            }
        }
        if (!found) break;
    }
    
    for (int i = 0; i < MAX_PROCESSES; i++) {
        if (!finish[i]) return 0;  // Unsafe
    }
    return 1;  // Safe
}

// Request resources
int requestResources(int process_id, int request[]) {
    for (int i = 0; i < MAX_RESOURCES; i++) {
        if (request[i] > need[process_id][i]) return -1;  // Error
        if (request[i] > available[i]) return 0;  // Must wait
    }
    
    // Pretend to allocate
    for (int i = 0; i < MAX_RESOURCES; i++) {
        available[i] -= request[i];
        allocation[process_id][i] += request[i];
        need[process_id][i] -= request[i];
    }
    
    if (isSafe()) {
        return 1;  // Request granted
    } else {
        // Rollback
        for (int i = 0; i < MAX_RESOURCES; i++) {
            available[i] += request[i];
            allocation[process_id][i] -= request[i];
            need[process_id][i] += request[i];
        }
        return 0;  // Request denied
    }
}

int main() {
    init();
    if (isSafe()) {
        printf("System is in SAFE state\n");
    } else {
        printf("System is in UNSAFE state\n");
    }
    return 0;
}
```

### 4.4 Resource Allocation Graph

```
    P1 ──────► R1 ──────► P2
    │                  │
    ▼                  ▼
    R2 ◄────── P3 ◄───── R3
    
P = Process, R = Resource
─► = Request, ◄── = Assignment
```

A cycle in the resource allocation graph indicates potential deadlock.

---

## 5. Memory Management

Memory is a critical resource requiring sophisticated management.

### 5.1 Memory Management Techniques

1. **Contiguous Allocation**: Single block per process
2. **Paging**: Fixed-size pages mapped to frames
3. **Segmentation**: Variable-sized segments with logical division
4. **Virtual Memory**: Swapping to disk extends available memory

### 5.2 Paging with TLB (Translation Lookaside Buffer)

The TLB is a hardware cache for virtual-to-physical address translation:

```c
// Conceptual TLB structure
typedef struct {
    unsigned int virtual_page;
    unsigned int physical_frame;
    int valid;
    int access_time;
} TLB_Entry;

TLB_Entry tlb[TLB_SIZE];
int tlb_index = 0;

// TLB Lookup
unsigned int translate_address(unsigned int virtual_addr) {
    unsigned int vpn = virtual_addr / PAGE_SIZE;
    unsigned int offset = virtual_addr % PAGE_SIZE;
    
    // Check TLB first
    for (int i = 0; i < TLB_SIZE; i++) {
        if (tlb[i].valid && tlb[i].virtual_page == vpn) {
            // TLB Hit
            return (tlb[i].physical_frame * PAGE_SIZE) + offset;
        }
    }
    
    // TLB Miss - page table lookup required
    unsigned int physical_frame = page_table[vpn];
    
    // Update TLB
    tlb[tlb_index].virtual_page = vpn;
    tlb[tlb_index].physical_frame = physical_frame;
    tlb[tlb_index].valid = 1;
    tlb_index = (tlb_index + 1) % TLB_SIZE;
    
    return (physical_frame * PAGE_SIZE) + offset;
}
```

---

## 6. I/O Device Management

The OS must manage diverse I/O devices efficiently:

- **Device Drivers**: Interface between OS and hardware
- **Buffering**: Temporary storage for data transfer
- **Spooling**: Queue management for shared devices (printers)
- **Caching**: Fast access to frequently used data

---

## Key Takeaways

1. **OS as Resource Manager**: The operating system serves as the central coordinator for all system resources, ensuring efficient, fair, and secure access to CPU, memory, I/O devices, and files.

2. **Core Functions**: Resource allocation, protection, sharing, and abstraction form the foundation of OS resource management.

3. **CPU Scheduling**: Various algorithms (FCFS, SJF, Round Robin, Priority) balance throughput, waiting time, and response time based on system requirements.

4. **Deadlock Handling**: Understanding the four Coffman conditions and employing prevention, avoidance, or detection strategies is crucial for system stability.

5. **Protection Mechanisms**: Memory management units (MMU), user/kernel mode separation, and access control lists prevent unauthorized resource access.

6. **Virtualization**: OS abstracts physical resources into logical entities (virtual memory, virtual CPUs), enabling better utilization and isolation.

7. **Practical Implementation**: Code examples demonstrate real-world implementations of scheduling algorithms, shared memory, and memory allocation.

---

## Delhi University NEP 2024 UGCF Alignment

This content covers the following modules from the Operating System syllabus:

- Unit I: Introduction to Operating Systems (Resource Management perspective)
- Unit II: Process Management (Scheduling, Deadlock)
- Unit III: Memory Management (Virtual memory, Paging, TLB)
- Unit IV: Device Management and File Systems

**Recommended References:**

- Silberschatz, Galvin, Gagne - "Operating System Concepts"
- Tanenbaum, Bos - "Modern Operating Systems"
- Delhi University Practical Lab Manual

---

*This study material provides comprehensive coverage of "OS as Resource Manager" for BSc (Hons) Computer Science students at Delhi University, addressing all key concepts required for the NEP 2024 UGCF curriculum.*