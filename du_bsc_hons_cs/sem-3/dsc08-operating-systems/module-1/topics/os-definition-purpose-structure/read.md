# Operating Systems: Definition, Purpose, and Structure

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

An operating system (OS) is the foundational software that bridges the gap between computer hardware and user applications. Every interaction you have with a computer—whether you're browsing the web, editing a document, or playing a game—relies on the operating system managing resources and providing services behind the scenes.

### Why This Topic Matters

For Delhi University BSc (Hons) Computer Science students, understanding operating systems is crucial because:

- **Core Curriculum Requirement**: This topic aligns with the Operating Systems paper in Semester IV/V under NEP 2024 UGCF
- **System Programming Foundation**: Knowledge of OS concepts is essential for system programming, embedded systems, and software development
- **Competitive Examinations**: Questions on OS fundamentals frequently appear in GATE, UGC NET, and placement interviews
- **Real-World Applications**: From smartphones to supercomputers, every computing device runs an operating system

---

## 2. Definition of Operating System

### 2.1 Classical Definitions

An operating system is a **system software** that acts as an **interface between the user and the computer hardware**. It manages hardware resources and provides services to application programs.

**Key Definitions from Textbook Perspectives:**

| Perspective | Definition |
|-------------|------------|
| **User View** | A program that makes computers easy to use |
| **System View** | A resource allocator managing hardware and software resources |
| **Kernel View** | The core program that controls all system resources and operations |

### 2.2 Modern Definition

> **Operating System**: A collection of system programs that controls and coordinates the execution of application programs and acts as an interface between the user of a computer and the computer hardware.

**According to Silberschatz et al.**, "An operating system is a program that acts as an interface between the user and the computer hardware."

---

## 3. Purpose and Objectives of Operating System

The primary purposes of an operating system can be categorized into several key objectives:

### 3.1 Convenience and User Interface

- Provides a user-friendly interface (CLI or GUI)
- Simplifies complex hardware operations for users
- Enables users to interact with computers without knowing hardware details

### 3.2 Efficiency and Resource Management

The OS efficiently manages computer resources:

- **CPU Scheduling**: Allocates processor time to multiple processes
- **Memory Management**: Controls RAM allocation and virtual memory
- **I/O Management**: Handles input/output operations efficiently
- **Disk Management**: Manages file storage and retrieval

### 3.3 Protection and Security

- Prevents unauthorized access to system resources
- Implements user authentication and access control
- Protects data integrity and confidentiality

### 3.4 Abstraction and Virtualization

- Provides logical view of physical resources
- Creates abstractions like files, processes, and virtual memory
- Enables program execution without hardware complexity

---

## 4. Operating System Structure

The structure of an operating system defines how its components are organized and interact. Understanding OS structure is essential for Delhi University students as this topic appears frequently in examinations.

### 4.1 Simple/Batch Systems

- Users submit jobs in batches
- No interactive user communication
- Simple resource management
- Examples: Early IBM systems, CDC 6600

### 4.2 Monolithic Structure

The **monolithic kernel** architecture is the simplest and oldest OS structure where the entire operating system runs in a single address space (kernel mode).

**Characteristics:**
- All OS services (process management, memory management, file system, device drivers) reside in the kernel
- No protection between kernel components
- Direct function calls between modules
- High performance due to minimal overhead

**Advantages:**
- Fast execution (no message passing overhead)
- Simple to design and implement for small systems

**Disadvantages:**
- Difficult to maintain and extend
- Any bug can crash the entire system
- Not scalable for large systems

**Real-World Examples:**
- Linux (traditional monolithic)
- UNIX (original design)
- MS-DOS

**Code Example: Simple Monolithic System Structure in C**

```c
// Simplified monolithic kernel structure (conceptual)
#include <stdio.h>

// Global kernel data structures
struct process_control_block {
    int pid;
    char state;
    int priority;
    void *memory_ptr;
};

// Kernel functions (all in single address space)
void schedule_process() {
    // CPU scheduling algorithm
}

void manage_memory(size_t size) {
    // Memory allocation/deallocation
}

void handle_interrupt(int irq_num) {
    // Interrupt handling
}

void read_write_file(const char *filename, char *buffer) {
    // File system operations
}

int main() {
    printf("Monolithic Kernel Initialized\n");
    // Boot sequence - initialize all subsystems
    schedule_process();
    return 0;
}
```

### 4.3 Microkernel Structure

The **microkernel** architecture minimizes the kernel by moving most services to user-space processes called **servers**.

**Characteristics:**
- Only essential services in kernel: basic IPC, scheduling, memory management
- User-space servers: file system, device drivers, networking, process management
- Communication via message passing

**Advantages:**
- High reliability (failure of one service doesn't crash system)
- Easy to extend and modify
- Better security through isolation
- Suitable for distributed systems

**Disadvantages:**
- Performance overhead (message passing between processes)
- Complex inter-process communication
- Higher memory requirements

**Real-World Examples:**
- **MINIX 3**: Educational microkernel OS
- **QNX**: Real-time microkernel OS
- **GNU Hurd**: GNU project's microkernel
- **macOS (XNU)**: Hybrid with microkernel elements

**Code Example: Microkernel Message Passing**

```c
// Conceptual microkernel message passing
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MSG_SIZE 256

// Message structure for IPC
struct ipc_message {
    int sender_pid;
    int receiver_pid;
    int message_type;
    char data[MSG_SIZE];
};

// Microkernel core functions (in kernel space)
int send_message(struct ipc_message *msg) {
    // Validate message
    // Route to destination server process
    // Return status
    return 0;
}

int receive_message(int receiver_pid, struct ipc_message *msg) {
    // Check message queue
    // Copy message to user buffer
    return 0;
}

// User-space server (File System Server)
int file_server_handler(struct ipc_message *request) {
    struct ipc_message response;
    
    if (request->message_type == FILE_OPEN) {
        // Perform file open operation
        strcpy(response.data, "File opened successfully");
    } else if (request->message_type == FILE_READ) {
        // Perform file read
    }
    
    send_message(&response);
    return 0;
}

// Client application
int main() {
    struct ipc_message msg;
    
    // Client requests file service via kernel
    msg.message_type = FILE_OPEN;
    msg.receiver_pid = FILE_SERVER_PID;
    strcpy(msg.data, "test.txt");
    
    send_message(&msg);
    printf("Request sent to file server\n");
    
    return 0;
}
```

### 4.4 Layered Structure

The **layered approach** organizes the OS into hierarchical layers, where each layer uses services only from the layer immediately below it.

**Typical Layer Organization:**

| Layer | Name | Functions |
|-------|------|-----------|
| Layer 5 | User Programs | Applications, editors, compilers |
| Layer 4 | User Interface | Command interpreter, shell |
| Layer 3 | Process Management | Process creation, scheduling, IPC |
| Layer 2 | Memory Management | Virtual memory, paging |
| Layer 1 | Device Drivers | Device-specific operations |
| Layer 0 | Hardware | Physical hardware, CPU, memory |

**Advantages:**
- Modular design - easy to implement and debug
- Each layer can be designed independently
- Changes in one layer don't affect others
- Clear abstraction between levels

**Disadvantages:**
- Performance overhead (layer traversal)
- Difficult to define clear layer boundaries
- Overhead in defining and enforcing layers

**Real-World Examples:**
- **THE OS** (Dijkstra) - First layered OS
- **MULTICS**
- **Windows NT** (hybrid layered architecture)
- **Traditional UNIX Systems**

### 4.5 Hybrid/Exokernel Structure

Modern operating systems often combine multiple approaches:

- **Linux**: Primarily monolithic with loadable kernel modules
- **Windows NT**: Hybrid of microkernel design with monolithic performance
- **macOS**: XNU kernel combining Mach microkernel with BSD components

---

## 5. Components of Operating System

### 5.1 Process Management

**Definition**: Process management involves creating, scheduling, and terminating processes.

**Key Concepts:**
- **Process**: A program in execution
- **Process Control Block (PCB)**: Data structure storing process information
- **Process States**: New, Ready, Running, Waiting, Terminated
- **CPU Scheduling**: Algorithms like FCFS, SJF, Round Robin, Priority Scheduling

### 5.2 Memory Management

**Definition**: Controls how computer memory is allocated and deallocated.

**Key Concepts:**
- **Contiguous Memory Allocation**
- **Paging**: Division of physical and logical memory into fixed-size frames
- **Segmentation**: Division into variable-sized segments
- **Virtual Memory**: Extends logical memory using disk space

### 5.3 File Management

**Definition**: Manages files on secondary storage devices.

**Key Concepts:**
- **File**: Collection of related information
- **Directory Structure**: Hierarchical, single-level, two-level
- **File Allocation Methods**: Contiguous, Linked, Indexed
- **File Protection**: Access control, authentication

### 5.4 Device Management

**Definition**: Controls and coordinates all hardware devices connected to the computer.

**Key Concepts:**

1. **Device Drivers**: Software components that allow OS to interact with hardware
2. **Buffering**: Temporary storage for data during I/O operations
3. **Spooling**: Sequential processing of I/O requests (print queue)
4. **Device Scheduling**: Managing access to shared devices
5. **Interrupt Handling**: Response to asynchronous events

**Device Types:**
- **Character Devices**: Keyboard, mouse (sequential access)
- **Block Devices**: Hard drives, USB (random access)
- **Network Devices**: Ethernet, Wi-Fi

### 5.5 Security and Protection

**Definition**: Ensures that resources are accessed only by authorized users and processes.

**Key Security Mechanisms:**

1. **Authentication**
   - Password-based authentication
   - Biometric authentication
   - Multi-factor authentication

2. **Authorization/Access Control**
   - **Discretionary Access Control (DAC)**: Owner controls access
   - **Mandatory Access Control (MAC)**: System enforces security policies
   - **Role-Based Access Control (RBAC)**: Access based on user roles

3. **Protection Mechanisms**
   - User IDs and Group IDs
   - File permissions (read, write, execute)
   - Capabilities and privileges
   - Security kernels

4. **Encryption**
   - Data at rest encryption
   - Secure communication protocols (TLS/SSL)

---

## 6. Examples with Code

### Example 1: Process Creation in UNIX (Fork System Call)

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid;
    
    printf("Parent Process: PID = %d\n", getpid());
    
    // Create child process
    pid = fork();
    
    if (pid < 0) {
        // Error in fork
        fprintf(stderr, "Fork Failed\n");
        return 1;
    }
    else if (pid == 0) {
        // Child process
        printf("Child Process: PID = %d, Parent PID = %d\n", 
               getpid(), getppid());
        execlp("/bin/ls", "ls", "-l", NULL);
    }
    else {
        // Parent process
        printf("Parent: Child created with PID = %d\n", pid);
        wait(NULL);  // Wait for child to complete
        printf("Child Process Completed\n");
    }
    
    return 0;
}
```

**Explanation:**
- `fork()` creates a new process (child) duplicating the parent
- `getpid()` returns current process ID
- `getppid()` returns parent process ID
- `execlp()` replaces child process image with new program
- `wait()` ensures parent waits for child completion

### Example 2: Memory Management Simulation (Paging)

```c
#include <stdio.h>
#include <stdlib.h>

#define PAGE_SIZE 256
#define FRAME_COUNT 4

// Page Table Entry structure
typedef struct {
    int frame_number;
    int valid_bit;
    int dirty_bit;
} PageTableEntry;

// Physical memory frames
char physical_memory[FRAME_COUNT][PAGE_SIZE];

// Initialize page table
void init_page_table(PageTableEntry *pt, int num_pages) {
    for (int i = 0; i < num_pages; i++) {
        pt[i].valid_bit = 0;
        pt[i].dirty_bit = 0;
    }
}

// Simulate page fault handling
int handle_page_fault(PageTableEntry *pt, int page_num) {
    printf("Page Fault: Page %d not in memory\n", page_num);
    
    // Simple replacement: find first free frame
    static int next_frame = 0;
    
    if (next_frame >= FRAME_COUNT) {
        // All frames occupied - need replacement
        printf("All frames occupied, using simple FIFO replacement\n");
        next_frame = 0;
    }
    
    pt[page_num].frame_number = next_frame;
    pt[page_num].valid_bit = 1;
    pt[page_num].dirty_bit = 0;
    
    printf("Loaded page %d into frame %d\n", page_num, next_frame);
    next_frame++;
    
    return pt[page_num].frame_number;
}

// Logical to physical address translation
void translate_address(PageTableEntry *pt, int logical_address, 
                       int *physical_addr, int *page_fault) {
    int page_num = logical_address / PAGE_SIZE;
    int offset = logical_address % PAGE_SIZE;
    
    *page_fault = 0;
    
    if (pt[page_num].valid_bit == 0) {
        // Page fault occurred
        *page_fault = 1;
        handle_page_fault(pt, page_num);
    }
    
    int frame = pt[page_num].frame_number;
    *physical_addr = (frame * PAGE_SIZE) + offset;
}

int main() {
    int num_pages = 8;
    PageTableEntry *page_table = malloc(num_pages * sizeof(PageTableEntry));
    
    init_page_table(page_table, num_pages);
    
    // Simulate accessing logical addresses
    int logical_addresses[] = {100, 300, 567, 900, 1200};
    
    for (int i = 0; i < 5; i++) {
        int physical_addr;
        int page_fault;
        
        translate_address(page_table, logical_addresses[i], 
                          &physical_addr, &page_fault);
        
        printf("Logical Addr: %d -> Physical Addr: %d %s\n",
               logical_addresses[i], physical_addr,
               page_fault ? "(Page Fault Handled)" : "");
    }
    
    free(page_table);
    return 0;
}
```

---

## 7. Key Takeaways

### Definition Summary
- An operating system is system software that acts as an interface between users and hardware
- It manages resources efficiently and provides services to application programs

### Purpose Summary
1. **Convenience**: Provides user-friendly interface
2. **Efficiency**: Manages CPU, memory, I/O resources
3. **Protection**: Secures data and resources
4. **Abstraction**: Simplifies hardware complexity

### Structure Summary
| Structure | Key Feature | Example |
|-----------|-------------|---------|
| Monolithic | Single kernel space | Linux, UNIX |
| Microkernel | Minimal kernel, servers | MINIX, QNX |
| Layered | Hierarchical layers | THE, Windows NT |
| Hybrid | Combination approaches | macOS, Linux with modules |

### Component Summary
- **Process Management**: Process scheduling, creation, termination
- **Memory Management**: Allocation, paging, virtual memory
- **File Management**: File operations, directories, protection
- **Device Management**: Drivers, buffering, interrupt handling
- **Security/Protection**: Authentication, access control, encryption

---

## 8. Multiple Choice Questions (MCQs)

### Level 1: Easy

**Q1. Which of the following is NOT a function of an Operating System?**
- (a) Memory Management
- (b) Process Management
- (c) Compilation of Programs
- (d) Device Management

**Answer**: (c) Compilation of Programs

---

**Q2. The main function of the operating system is:**
- (a) To make computer work efficiently
- (b) To provide user interface
- (c) To manage resources
- (d) All of the above

**Answer**: (d) All of the above

---

### Level 2: Medium

**Q3. In a microkernel architecture, which of the following is TRUE?**
- (a) All OS services run in kernel mode
- (b) Only essential services are in kernel; others run in user mode
- (c) No communication between processes is required
- (d) It provides maximum performance without any overhead

**Answer**: (b) Only essential services are in kernel; others run in user mode

---

**Q4. Which OS structure provides the BEST protection and reliability?**
- (a) Monolithic
- (b) Layered
- (c) Microkernel
- (d) Simple/Batch

**Answer**: (c) Microkernel

---

**Q5. The main difference between paging and segmentation is:**
- (a) Paging is visible to user; segmentation is not
- (b) Paging uses fixed-size blocks; segmentation uses variable-sized
- (c) Segmentation provides more protection than paging
- (d) Paging provides more flexibility than segmentation

**Answer**: (b) Paging uses fixed-size blocks; segmentation uses variable-sized

---

### Level 3: Hard

**Q6. In the context of Operating System security, DAC stands for:**
- (a) Direct Access Control
- (b) Dynamic Access Control
- (c) Discretionary Access Control
- (d) Distributed Access Control

**Answer**: (c) Discretionary Access Control

---

**Q7. Which of the following statements about virtual memory is INCORRECT?**
- (a) It allows execution of processes that may not be completely in memory
- (b) It increases the effective memory capacity of the system
- (c) It eliminates the need for physical memory completely
- (d) It uses swapping between disk and memory

**Answer**: (c) It eliminates the need for physical memory completely

---

**Q8. The hierarchical directory structure is implemented in:**
- (a) Single-level directory
- (b) Two-level directory
- (c) Tree-structured directory
- (d) All of the above

**Answer**: (c) Tree-structured directory

---

**Q9. A process is in the 'Ready' state when:**
- (a) It is waiting for I/O completion
- (b) It is waiting for CPU allocation
- (c) It is terminated
- (d) None of the above

**Answer**: (b) It is waiting for CPU allocation

---

**Q10. The operating system structure where all services run in the kernel space is called:**
- (a) Microkernel
- (b) Exokernel
- (c) Monolithic Kernel
- (d) Hybrid Kernel

**Answer**: (c) Monolithic Kernel

---

## References for Further Study

1. Silberschatz, Galvin, Gagne - *Operating System Concepts* (9th Edition)
2. Abraham Silberschatz - *Operating System Principles*
3. Delhi University B.Sc. (H) Computer Science Syllabus - NEP 2024 UGCF
4. Andrew S. Tanenbaum - *Operating Systems: Design and Implementation*

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University as per NEP 2024 UGCF curriculum.*