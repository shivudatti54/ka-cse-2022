# Introduction to Operating Systems


## Table of Contents

- [Introduction to Operating Systems](#introduction-to-operating-systems)
- [What is an Operating System?](#what-is-an-operating-system)
- [Goals of an Operating System](#goals-of-an-operating-system)
  - [1. Primary Goals](#1-primary-goals)
  - [2. Secondary Goals](#2-secondary-goals)
- [Functions of an Operating System](#functions-of-an-operating-system)
  - [1. Process Management](#1-process-management)
  - [2. Memory Management](#2-memory-management)
  - [3. File System Management](#3-file-system-management)
  - [4. I/O Device Management](#4-io-device-management)
  - [5. Security and Protection](#5-security-and-protection)
  - [6. Command Interpretation](#6-command-interpretation)
- [Types of Operating Systems](#types-of-operating-systems)
  - [1. Batch Operating System](#1-batch-operating-system)
  - [2. Time-Sharing Operating System (Multitasking)](#2-time-sharing-operating-system-multitasking)
  - [3. Distributed Operating System](#3-distributed-operating-system)
  - [4. Real-Time Operating System (RTOS)](#4-real-time-operating-system-rtos)
  - [5. Network Operating System](#5-network-operating-system)
  - [6. Mobile Operating System](#6-mobile-operating-system)
- [Operating System Services](#operating-system-services)
  - [1. User Services](#1-user-services)
  - [2. System Services](#2-system-services)
- [Operating System Structure](#operating-system-structure)
  - [Components:](#components)
- [System Calls](#system-calls)
- [Operating System Structures](#operating-system-structures)
  - [1. Simple Structure (MS-DOS)](#1-simple-structure-ms-dos)
  - [2. Layered Approach](#2-layered-approach)
  - [3. Microkernel](#3-microkernel)
  - [4. Modular Approach](#4-modular-approach)
- [Evolution of Operating Systems](#evolution-of-operating-systems)
- [Examples of Operating Systems](#examples-of-operating-systems)
- [User View vs System View](#user-view-vs-system-view)
  - [User View (Top-Down)](#user-view-top-down)
  - [System View (Bottom-Up)](#system-view-bottom-up)
- [Exam Tips](#exam-tips)

## What is an Operating System?

An **Operating System (OS)** is system software that manages computer hardware and software resources and provides common services for computer programs. It acts as an intermediary between users and the computer hardware, making the computer system convenient and efficient to use.

**Definition:** An operating system is a program that manages a computer's hardware and provides a basis for application programs, acting as an intermediary between the computer user and the computer hardware.

## Goals of an Operating System

### 1. Primary Goals

**Convenience:**

- Make the computer system easy to use
- Hide complexity of hardware from users
- Provide user-friendly interface
- Enable efficient application development

**Efficiency:**

- Maximize resource utilization
- Minimize idle time of hardware components
- Optimize CPU usage, memory management
- Ensure fair resource allocation

### 2. Secondary Goals

- **Reliability**: System should be dependable and error-free
- **Maintainability**: Easy to update and maintain
- **Security**: Protect data and resources from unauthorized access
- **Portability**: Ability to run on different hardware platforms

## Functions of an Operating System

### 1. Process Management

**What is a Process?**
A program in execution is called a process.

**Functions:**

- Process creation and deletion
- Process scheduling (deciding which process runs when)
- Process synchronization
- Inter-process communication
- Deadlock handling

**Example:**
When you open a web browser, the OS creates a process for it, allocates resources, and schedules CPU time.

### 2. Memory Management

**Purpose:** Efficiently manage the computer's main memory (RAM)

**Functions:**

- Memory allocation and deallocation
- Keep track of which memory is in use
- Decide which processes to load into memory
- Implement virtual memory
- Memory protection

**Example:**
When you run multiple applications, the OS ensures each gets sufficient memory without interfering with others.

### 3. File System Management

**Purpose:** Organize and store data on storage devices

**Functions:**

- File creation, deletion, reading, writing
- Directory structure management
- File access control and permissions
- File backup and recovery
- Disk space management

**Example:**
When you save a document, the OS manages where on the disk it's stored and how to retrieve it.

### 4. I/O Device Management

**Purpose:** Manage input/output devices efficiently

**Functions:**

- Device driver management
- Buffering and caching
- Spooling (simultaneous peripheral operations online)
- Device allocation and deallocation

**Example:**
When you print a document, the OS uses the printer driver to communicate with the printer.

### 5. Security and Protection

**Security:** Defending system from external and internal attacks
**Protection:** Controlling access to system resources

**Functions:**

- User authentication (login/password)
- Access control (file permissions)
- Encryption
- Firewall management
- Malware protection

### 6. Command Interpretation

**Purpose:** Interface between user and system

**Types:**

- **CLI (Command Line Interface)**: Text-based commands (e.g., Terminal, Command Prompt)
- **GUI (Graphical User Interface)**: Visual interface with windows and icons

## Types of Operating Systems

### 1. Batch Operating System

**Characteristics:**

- Jobs are grouped into batches
- No direct interaction with user
- Jobs are executed one after another
- Used in mainframe computers

**Advantages:**

- Less idle time
- High efficiency for repetitive tasks
- Suitable for large-scale data processing

**Disadvantages:**

- No user interaction during execution
- Difficult to debug
- Long turnaround time

**Examples:** IBM OS/360, Payroll processing systems

### 2. Time-Sharing Operating System (Multitasking)

**Characteristics:**

- Multiple users share system simultaneously
- CPU time is divided into time slices (quantum)
- Each user gets a turn
- Appears simultaneous to users

**Advantages:**

- Multiple users can work simultaneously
- Reduced idle time
- Better response time
- Increased productivity

**Disadvantages:**

- Security concerns
- Data communication overhead
- Requires scheduling algorithms

**Examples:** Unix, Linux, Windows (modern versions)

### 3. Distributed Operating System

**Characteristics:**

- Multiple autonomous computers connected via network
- Appears as single system to users
- Resources are shared across network
- Processes can run on different machines

**Advantages:**

- Resource sharing
- Faster computation
- Reliability (if one fails, others continue)
- Scalability

**Disadvantages:**

- Complex implementation
- Network dependency
- Security challenges

**Examples:** Google's distributed systems, LOCUS

### 4. Real-Time Operating System (RTOS)

**Characteristics:**

- Time-critical applications
- Deterministic response time
- Must meet strict deadlines
- Used in embedded systems

**Types:**

- **Hard Real-Time**: Missing deadline is catastrophic (airbag systems, pacemakers)
- **Soft Real-Time**: Missing occasional deadline is tolerable (video streaming, gaming)

**Advantages:**

- Predictable response time
- High reliability
- Efficient for time-critical tasks

**Disadvantages:**

- Limited flexibility
- Complex design
- Expensive

**Examples:** VxWorks, QNX, FreeRTOS

### 5. Network Operating System

**Characteristics:**

- Manages network resources
- Provides services to clients
- Handles file sharing, printer sharing
- Centralized administration

**Examples:** Novell NetWare, Windows Server

### 6. Mobile Operating System

**Characteristics:**

- Designed for mobile devices
- Touch-based interface
- Power management crucial
- Support for wireless connectivity

**Examples:** Android, iOS, Windows Phone

## Operating System Services

### 1. User Services

- **Program Execution**: Load and run programs
- **I/O Operations**: Access to I/O devices
- **File System Manipulation**: Read, write, create, delete files
- **Communications**: Inter-process communication
- **Error Detection**: Detect and handle errors

### 2. System Services

- **Resource Allocation**: Allocate resources to processes
- **Accounting**: Track resource usage
- **Protection**: Control access to resources
- **Security**: Authenticate users and protect system

## Operating System Structure

```
+----------------------------------+
| User Applications |
+----------------------------------+
| System Programs |
+----------------------------------+
| Operating System Services |
| (File Mgmt, Process Mgmt, etc.) |
+----------------------------------+
| System Calls |
+----------------------------------+
| Kernel |
+----------------------------------+
| Hardware |
+----------------------------------+
```

### Components:

1. **Kernel**: Core of OS, manages resources
2. **System Calls**: Interface between user programs and OS
3. **System Programs**: Utilities provided by OS
4. **User Applications**: Programs run by users

## System Calls

**Definition:** Programming interface to services provided by the OS.

**Types:**

1. **Process Control**: fork(), exit(), wait()
2. **File Management**: open(), read(), write(), close()
3. **Device Management**: ioctl(), read(), write()
4. **Information Maintenance**: getpid(), time()
5. **Communication**: pipe(), shmget(), mmap()

**Example in C:**

```c
#include <unistd.h>
int main() {
 pid_t pid = fork(); // System call to create process
 return 0;
}
```

## Operating System Structures

### 1. Simple Structure (MS-DOS)

- No modularity
- Application can access hardware directly
- Not well-layered

### 2. Layered Approach

- OS divided into layers
- Each layer uses services of lower layer
- Example: Layer 0 (Hardware), Layer 1 (CPU scheduling), etc.

### 3. Microkernel

- Minimal kernel
- Most services in user space
- Communication via message passing
- Example: Mach, QNX

### 4. Modular Approach

- Kernel has core components
- Other services loaded as modules
- Example: Modern Linux, Solaris

## Evolution of Operating Systems

```
1940s: No OS (Manual operation)
 ↓
1950s: Batch Systems
 ↓
1960s: Multiprogramming, Time-sharing
 ↓
1970s: Personal computers, Unix
 ↓
1980s: GUIs, Networks
 ↓
1990s: Internet, Mobile OS
 ↓
2000s: Virtualization, Cloud
 ↓
2010s-2020s: Mobile-first, IoT, Distributed systems
```

## Examples of Operating Systems

| OS       | Type                 | Usage                       |
| -------- | -------------------- | --------------------------- |
| Windows  | Time-sharing         | Personal computers, servers |
| Linux    | Time-sharing, Server | Servers, embedded, mobile   |
| macOS    | Time-sharing         | Apple computers             |
| Android  | Mobile               | Smartphones, tablets        |
| iOS      | Mobile               | iPhone, iPad                |
| Unix     | Time-sharing         | Servers, workstations       |
| VxWorks  | Real-time            | Embedded systems            |
| FreeRTOS | Real-time            | IoT devices                 |

## User View vs System View

### User View (Top-Down)

- Ease of use
- Performance
- Good response time
- User interface

### System View (Bottom-Up)

- Resource allocation
- Control and management
- Efficiency
- Protection and security

## Exam Tips

1. **Understand the definition** of OS and be able to explain it clearly
2. **Know all functions** of OS with examples
3. **Differentiate between types** of OS (batch, time-sharing, real-time, distributed)
4. **Remember characteristics** of each OS type
5. **Understand goals**: Convenience vs Efficiency
6. **Know system calls** and their categories
7. **Understand OS structure** and different architectural approaches
8. **Remember examples** of each type of OS
9. **Be able to draw diagrams** showing OS structure and layers
10. **Understand evolution** of operating systems
11. **Practice scenarios**: Which OS for which application?
12. **Know the difference** between hard and soft real-time systems
