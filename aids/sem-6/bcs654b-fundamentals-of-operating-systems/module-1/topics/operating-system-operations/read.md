# Operating System Operations


## Table of Contents

- [Operating System Operations](#operating-system-operations)
- [Introduction](#introduction)
- [Core Operating System Operations](#core-operating-system-operations)
  - [1. Process Management Operations](#1-process-management-operations)
  - [2. Memory Management Operations](#2-memory-management-operations)
  - [3. File System Operations](#3-file-system-operations)
  - [4. I/O Device Management Operations](#4-io-device-management-operations)
  - [5. Protection and Security Operations](#5-protection-and-security-operations)
  - [6. System Monitoring and Accounting](#6-system-monitoring-and-accounting)
- [Dual-Mode Operation](#dual-mode-operation)
  - [User Mode vs Kernel Mode](#user-mode-vs-kernel-mode)
- [Timer Operations](#timer-operations)
  - [Purpose of System Timer](#purpose-of-system-timer)
  - [Timer Mechanism](#timer-mechanism)
- [Error Handling](#error-handling)
  - [Types of Errors](#types-of-errors)
  - [Error Handling Operations](#error-handling-operations)
- [Boot Operations](#boot-operations)
  - [System Startup](#system-startup)
- [Exam Tips](#exam-tips)

## Introduction

Operating System Operations refer to the various activities and services performed by an OS to manage computer hardware and software resources effectively. These operations ensure smooth functioning of the system and provide a platform for application programs to execute.

## Core Operating System Operations

### 1. Process Management Operations

#### A. Process Creation

**How Processes are Created:**

1. **System Initialization**: When OS boots, it creates several processes

- Foreground processes (user interaction)
- Background processes (daemons/services)

2. **User Request**: User starts a program

- Double-click an icon
- Type a command in terminal

3. **Process Spawning**: Existing process creates new process

- Using system calls like `fork()` in Unix/Linux

**Process Creation Steps:**

```
1. Allocate unique Process ID (PID)
2. Allocate memory for process
3. Load program into memory
4. Create Process Control Block (PCB)
5. Set up process state to "Ready"
6. Add to ready queue
```

**Example (Unix/Linux):**

```c
#include <unistd.h>
#include <stdio.h>

int main() {
 pid_t pid = fork(); // Create child process

 if (pid == 0) {
 printf("Child process (PID: %d)\n", getpid());
 } else if (pid > 0) {
 printf("Parent process (PID: %d), Child PID: %d\n", getpid(), pid);
 }
 return 0;
}
```

#### B. Process Scheduling

**Purpose:** Determine which process runs on CPU and for how long.

**Scheduling Queues:**

1. **Job Queue**: All processes in the system
2. **Ready Queue**: Processes ready to execute
3. **Device Queues**: Processes waiting for I/O

**Scheduling Algorithms:**

- First-Come-First-Served (FCFS)
- Shortest Job First (SJF)
- Round Robin (RR)
- Priority Scheduling
- Multilevel Queue Scheduling

**Process States:**

```
 +-------+
 | New |
 +-------+
 ↓
 +-------+
 +--->| Ready |<---+
 | +-------+ |
 | ↓ |
 | +-------+ |
 +----| Running|---+
 +-------+
 ↓
 +-------+
 |Waiting|
 +-------+
 ↓
 +-------+
 |Terminated|
 +-------+
```

#### C. Process Termination

**Reasons for Termination:**

1. Normal exit (voluntary)
2. Error exit (voluntary)
3. Fatal error (involuntary)
4. Killed by another process (involuntary)

**Termination Steps:**

1. Release allocated resources
2. Close open files
3. Remove from process table
4. Notify parent process
5. Return exit status

#### D. Inter-Process Communication (IPC)

**Why IPC?**

- Information sharing
- Computation speedup
- Modularity
- Convenience

**IPC Mechanisms:**

1. **Shared Memory**

```c
// Create shared memory
int shmid = shmget(IPC_PRIVATE, 1024, IPC_CREAT | 0666);
// Attach to process
char *shm = (char*) shmat(shmid, NULL, 0);
```

2. **Message Passing**

```c
// Send message
msgsnd(msgid, &message, sizeof(message), 0);
// Receive message
msgrcv(msgid, &message, sizeof(message), 1, 0);
```

3. **Pipes**
4. **Sockets**
5. **Signals**

### 2. Memory Management Operations

#### A. Memory Allocation

**Purpose:** Allocate memory to processes efficiently.

**Allocation Methods:**

1. **Contiguous Allocation**

- **Fixed Partitioning**: Memory divided into fixed-size partitions
- **Dynamic Partitioning**: Memory divided as needed

2. **Non-Contiguous Allocation**

- **Paging**: Memory divided into fixed-size pages
- **Segmentation**: Memory divided into variable-size segments

**Operations:**

```
Allocate(process_id, size)
├─ Check available memory
├─ Find suitable block
├─ Allocate memory
└─ Update memory map
```

#### B. Memory Deallocation

**When to Deallocate:**

- Process terminates
- Process releases memory explicitly
- System needs to reclaim memory

**Operation:**

```
Deallocate(process_id)
├─ Free allocated memory
├─ Update memory map
├─ Merge free blocks (compaction)
└─ Add to free memory pool
```

#### C. Virtual Memory Operations

**Purpose:** Allow execution of processes larger than physical memory.

**Key Operations:**

1. **Page Fault Handling**

```
Page Fault Occurs
├─ 1. Trap to OS
├─ 2. Save process state
├─ 3. Determine location on disk
├─ 4. Read page from disk to memory
├─ 5. Update page table
└─ 6. Resume process
```

2. **Page Replacement**

- When memory is full, decide which page to replace
- Algorithms: FIFO, LRU, Optimal

3. **Swapping**

- Swap out: Move process from RAM to disk
- Swap in: Move process from disk to RAM

#### D. Memory Protection

**Mechanisms:**

- Base and limit registers
- Page table protection bits
- Segmentation with protection

### 3. File System Operations

#### A. File Operations

**1. Create**

```c
int fd = creat("file.txt", 0644);
```

**2. Open**

```c
int fd = open("file.txt", O_RDWR);
```

**3. Read**

```c
read(fd, buffer, size);
```

**4. Write**

```c
write(fd, data, size);
```

**5. Close**

```c
close(fd);
```

**6. Delete**

```c
unlink("file.txt");
```

#### B. Directory Operations

**1. Create Directory**

```c
mkdir("mydir", 0755);
```

**2. Remove Directory**

```c
rmdir("mydir");
```

**3. List Directory**

```c
DIR *dir = opendir(".");
struct dirent *entry;
while ((entry = readdir(dir)) != NULL) {
 printf("%s\n", entry->d_name);
}
closedir(dir);
```

#### C. File System Maintenance

**Operations:**

- Disk defragmentation
- Backup and recovery
- Consistency checking (fsck, chkdsk)
- Quota management

### 4. I/O Device Management Operations

#### A. Device Operations

**1. Request I/O**

```
Application → System Call → Kernel → Device Driver → Device
```

**2. Buffering**

- **Purpose**: Cope with speed mismatch between devices
- **Types**: Single buffer, Double buffer, Circular buffer

**3. Spooling (Simultaneous Peripheral Operations Online)**

- Used for devices that can't accept interleaved data streams
- Example: Printer spooling

```
Multiple print jobs → Spool directory → One at a time to printer
```

#### B. Interrupt Handling

**Interrupt Processing:**

```
1. Device sends interrupt signal
2. CPU saves current state
3. CPU jumps to interrupt handler
4. Execute interrupt service routine (ISR)
5. Restore CPU state
6. Resume interrupted process
```

**Types of Interrupts:**

- **Hardware Interrupts**: From devices (keyboard, mouse, disk)
- **Software Interrupts**: From programs (system calls, exceptions)

### 5. Protection and Security Operations

#### A. Authentication

**Methods:**

1. **Password-based**: Username and password
2. **Biometric**: Fingerprint, face recognition
3. **Token-based**: Smart cards, security keys
4. **Multi-factor**: Combination of above

#### B. Authorization

**Access Control:**

1. **Access Control Lists (ACL)**

```
File: document.txt
User Alice: Read, Write
User Bob: Read
Group Staff: Read
```

2. **Capability Lists**

- Each process has list of resources it can access

3. **Permission Bits** (Unix/Linux)

```
-rwxr-xr--
│││││││││└─ Others: Read
││││││││└── Others: No Write
│││││││└─── Others: No Execute
││││││└──── Group: Read
│││││└───── Group: No Write
││││└────── Group: Execute
│││└─────── Owner: Read
││└──────── Owner: Write
│└───────── Owner: Execute
└────────── Regular file
```

#### C. Encryption

**Purpose:** Protect data confidentiality

**Types:**

- **Symmetric**: Same key for encryption and decryption
- **Asymmetric**: Public-private key pair

### 6. System Monitoring and Accounting

#### A. Performance Monitoring

**Metrics:**

- CPU utilization
- Memory usage
- Disk I/O
- Network traffic
- Process statistics

**Tools:**

- Windows: Task Manager, Performance Monitor
- Linux: top, htop, vmstat, iostat

#### B. Resource Accounting

**Purpose:** Track resource usage by users and processes

**Information Tracked:**

- CPU time used
- Memory consumption
- Disk space used
- Network bandwidth used
- Login/logout times

#### C. Logging

**System Logs:**

- **Event Logs** (Windows): System, Application, Security
- **Syslog** (Linux): /var/log/syslog, /var/log/messages

**Log Information:**

- Timestamps
- Event types
- Error messages
- User activities

## Dual-Mode Operation

### User Mode vs Kernel Mode

**Purpose:** Protect OS and critical resources from user programs

```
+------------------+
| User Mode | Limited privileges
| (User programs) | Cannot execute privileged instructions
+------------------+
 ↕ System Call
+------------------+
| Kernel Mode | Full privileges
| (OS kernel) | Can execute all instructions
+------------------+
```

**Mode Bit:**

- 0 = Kernel mode
- 1 = User mode

**Privileged Instructions:**

- I/O control
- Timer management
- Interrupt management
- Memory management

**Mode Switching:**

```
User Mode → System Call → Kernel Mode → Return → User Mode
User Mode → Interrupt → Kernel Mode → Return → User Mode
```

## Timer Operations

### Purpose of System Timer

1. **Prevent infinite loops** from taking over CPU
2. **Implement time-sharing**
3. **Track system time**

### Timer Mechanism

```
1. Set timer to interrupt after X milliseconds
2. Process runs
3. Timer decrements
4. When timer reaches 0:
 ├─ Generate interrupt
 ├─ Transfer control to OS
 └─ OS decides next process
```

## Error Handling

### Types of Errors

1. **Hardware Errors**

- Memory errors
- Disk failures
- Network errors

2. **Software Errors**

- Arithmetic overflow
- Invalid memory access
- Illegal instruction

### Error Handling Operations

```
Error Occurs
├─ Detect error
├─ Log error
├─ Notify user/process
├─ Take corrective action:
│ ├─ Retry operation
│ ├─ Terminate process
│ ├─ Ignore error
│ └─ Return error code
└─ Continue or halt system
```

## Boot Operations

### System Startup

**Boot Process:**

```
1. Power On
2. BIOS/UEFI initialization
3. Boot loader loads OS kernel
4. Kernel initializes
5. Hardware detection
6. Device drivers loaded
7. System services started
8. User login
```

**Bootstrap Program:**

- Stored in ROM/EEPROM
- Initializes all aspects of system
- Loads OS kernel into memory

## Exam Tips

1. **Understand process operations**: Creation, scheduling, termination
2. **Know memory operations**: Allocation, deallocation, virtual memory
3. **Master file operations**: Create, read, write, delete
4. **Understand I/O operations**: Buffering, spooling, interrupts
5. **Know dual-mode operation**: User mode vs kernel mode
6. **Understand system calls** and their role
7. **Remember IPC mechanisms** and their uses
8. **Know protection mechanisms**: Authentication, authorization
9. **Understand timer operations** and their importance
10. **Be able to explain error handling** procedures
11. **Draw diagrams** for process states, mode switching
12. **Practice examples** of system calls and operations
