# Introduction to Operating Systems

## What is an Operating System?

An **Operating System (OS)** is system software that acts as an intermediary between the computer user and the computer hardware. It manages hardware resources and provides services for the execution of application programs.

> **Definition (Silberschatz):** An operating system is a program that manages a computer's hardware, provides a basis for application programs, and acts as an intermediary between the computer user and the computer hardware.

There is no universally accepted definition of an operating system. A common definition is: "Everything a vendor ships when you order an operating system." The one program running at all times on the computer is the **kernel**. Everything else is either a system program or an application program.

## Goals of an Operating System

An operating system has three primary goals:

| Goal                  | Description                                                                                                                |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Convenience**       | Make the computer system convenient and easy to use for the user                                                           |
| **Efficiency**        | Ensure that computer hardware resources are used in an efficient manner                                                    |
| **Ability to Evolve** | Permit effective development, testing, and introduction of new system functions without interfering with existing services |

### Convenience

- Provides a user-friendly interface (CLI, GUI)
- Hides the complexity of hardware from the user
- Offers high-level abstractions (files instead of disk sectors)

### Efficiency

- Maximizes CPU utilization
- Manages memory to avoid waste
- Schedules I/O operations for optimal throughput
- Balances resource allocation among competing processes

### Ability to Evolve

- Supports hardware upgrades and new hardware types
- Allows bug fixes and patches without system redesign
- Provides modular design for adding new services

## Views of an Operating System

### OS as a Resource Manager

The computer system has many resources (CPU time, memory space, storage, I/O devices). The OS acts as a **resource manager** (or resource allocator) that:

- Decides how to allocate resources to specific programs and users
- Manages conflicting requests for resources fairly and efficiently
- Controls the execution of programs to prevent errors and improper use

```
 +----------------------------+
 | USERS |
 | User 1 User 2 User 3 |
 +----------------------------+
 |
 +----------------------------+
 | APPLICATION PROGRAMS |
 | Compiler Editor Browser |
 +----------------------------+
 |
 +----------------------------+
 | OPERATING SYSTEM |
 | (Resource Manager) |
 +----------------------------+
 |
 +----------------------------+
 | COMPUTER HARDWARE |
 | CPU Memory I/O Devices |
 +----------------------------+
```

### OS as an Extended Machine (Virtual Machine)

The OS provides an **abstraction layer** over the raw hardware, presenting a simpler, cleaner interface to application programs. Instead of dealing with low-level hardware details (disk controller registers, interrupt vectors), programs interact with high-level abstractions like files, processes, and sockets.

**Example:** A program calls `write("file.txt", data)` instead of manually programming the disk controller, positioning the head, waiting for rotation, transferring data, and checking for errors.

## Components of a Computer System

A computer system can be divided into four components:

```
+----------------------------------------------------------+
| |
| Users |
| (People, machines, other computers) |
| |
+----------------------------------------------------------+
| |
| Application Programs |
| (Word processors, compilers, web browsers, games) |
| |
+----------------------------------------------------------+
| |
| Operating System |
| (Controls and coordinates use of hardware) |
| |
+----------------------------------------------------------+
| |
| Computer Hardware |
| (CPU, memory, I/O devices, storage) |
| |
+----------------------------------------------------------+
```

### 1. Hardware

Provides the basic computing resources: CPU, memory (RAM), I/O devices (disk drives, keyboard, display, network interfaces).

### 2. Operating System

Controls the hardware and coordinates its use among the various application programs for the various users.

### 3. Application Programs

Define the ways in which hardware resources are used to solve user computing problems. Examples: word processors, spreadsheets, compilers, web browsers, database systems.

### 4. Users

People, machines, or other computers that interact with the computer system.

## History and Evolution of Operating Systems

### Generation 1: No Operating System (1940s-1950s)

- Computers were enormous machines (vacuum tubes)
- Programming done in machine language using plugboards
- No operating system; the programmer was also the operator
- One job at a time, completely manual operation
- Extremely slow setup and turnaround times

### Generation 2: Batch Systems (1955-1965)

- Introduction of **transistors** made computers more reliable
- Jobs were submitted on punch cards, grouped into **batches**
- A **resident monitor** (early OS) automatically loaded and ran jobs sequentially
- No interaction between user and the job during execution

```
Job Flow in Batch System:
+-----------+ +-----------+ +-----------+ +-----------+
| Submit | --> | Job Queue | --> | Execute | --> | Output |
| Job Cards | | (Batch) | | (One at | | Results |
+-----------+ +-----------+ | a time) | +-----------+
 +-----------+
```

**Problem:** CPU remained idle during I/O operations, wasting expensive computing resources.

### Generation 3: Multiprogramming and Time-Sharing (1965-1980)

- Introduction of **Integrated Circuits (ICs)**
- **Multiprogramming:** Multiple jobs kept in memory simultaneously. When one job waits for I/O, the CPU switches to another job, improving CPU utilization.

```
Multiprogramming:
+------------------+
| Memory |
| +------------+ |
| | OS | |
| +------------+ |
| | Job 1 | | CPU switches between
| +------------+ | jobs to maximize
| | Job 2 | | utilization
| +------------+ |
| | Job 3 | |
| +------------+ |
+------------------+
```

- **Time-Sharing (Multitasking):** A logical extension of multiprogramming where the CPU switches between jobs so frequently that users can interact with each program while it is running. Each user gets a small time slice (quantum).

| Feature          | Batch System | Multiprogramming | Time-Sharing  |
| ---------------- | ------------ | ---------------- | ------------- |
| User interaction | None         | None             | Interactive   |
| Response time    | Hours/Days   | Hours            | Seconds       |
| CPU utilization  | Low          | High             | High          |
| Number of users  | Single       | Single           | Multiple      |
| Example OS       | FMS, IBSYS   | OS/360           | MULTICS, UNIX |

### Generation 4: Personal Computers and Beyond (1980-Present)

- **LSI/VLSI** circuits made personal computers affordable
- Emergence of **MS-DOS**, **Windows**, **macOS**, **Linux**
- Focus shifted from CPU efficiency to user convenience
- **Networked** and **distributed** operating systems
- **Mobile OS**: Android, iOS
- **Real-Time OS**: VxWorks, QNX (for embedded systems)
- **Cloud OS**: Systems managing virtualized environments

## Types of Operating Systems

| Type                    | Description                                           | Example       |
| ----------------------- | ----------------------------------------------------- | ------------- |
| **Batch OS**            | Jobs processed in batches without user interaction    | FMS, IBSYS    |
| **Multiprogramming OS** | Multiple programs in memory, CPU switches on I/O wait | OS/360        |
| **Time-Sharing OS**     | Interactive, rapid CPU switching among users          | UNIX, MULTICS |
| **Real-Time OS**        | Strict timing guarantees for critical tasks           | VxWorks, QNX  |
| **Distributed OS**      | Manages a collection of networked computers as one    | Amoeba        |
| **Embedded OS**         | Designed for embedded devices with limited resources  | FreeRTOS      |
| **Mobile OS**           | Designed for smartphones and tablets                  | Android, iOS  |

## Key Concepts Summary

```
+-----------------------------------------------------+
| OPERATING SYSTEM = Resource Manager + Extended Machine |
+-----------------------------------------------------+
| |
| GOALS: Convenience | Efficiency | Ability to Evolve |
| |
| EVOLUTION: |
| No OS --> Batch --> Multiprogramming --> Time-Sharing |
| --> Personal Computers --> Mobile/Cloud |
| |
| COMPONENTS: Hardware <-> OS <-> Apps <-> Users |
+-----------------------------------------------------+
```

## Exam Tips

1. **Definition is frequently asked:** Memorize Silberschatz's definition of an OS as an intermediary between user and hardware.
2. **Three goals of OS** (Convenience, Efficiency, Ability to Evolve) -- commonly asked as a short-answer question.
3. **Four components of a computer system** (Hardware, OS, Application programs, Users) -- draw the layered diagram.
4. **Evolution of OS:** Know the progression from batch systems to multiprogramming to time-sharing. Understand WHY each was developed (to solve limitations of the previous generation).
5. **Resource Manager vs Extended Machine:** Understand both views of the OS. Resource manager allocates and controls; extended machine provides abstractions.
6. **Multiprogramming vs Time-Sharing:** This is a very common comparison question. Key difference: time-sharing is interactive with rapid context switching, while multiprogramming focuses on CPU utilization without user interaction.
7. ** frequently asks:** "Explain the evolution of operating systems" or "Distinguish between multiprogramming and time-sharing systems" -- prepare well-structured answers with examples.
