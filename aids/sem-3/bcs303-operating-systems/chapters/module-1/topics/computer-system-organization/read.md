# Computer System Organization

## Introduction to Computer System Architecture

A computer system consists of hardware components that work together to execute programs and process data. Understanding this organization is fundamental to grasping how operating systems manage resources efficiently.

At its core, a computer system can be broken down into four main structural components:

- **Central Processing Unit (CPU)**: The brain that executes instructions
- **Main Memory (RAM)**: Temporary storage for programs and data
- **Input/Output (I/O) Devices**: Components that communicate with the external world
- **System Bus**: The communication pathway connecting all components

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   CPU          |<----->|   Main Memory  |<----->|   I/O Devices  |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
        ^                         ^                         ^
        |                         |                         |
        +------------+------------+------------+-----------+
                     |                         |
                     v                         v
               +-----------+             +-----------+
               |           |             |           |
               | System Bus|             |Controller |
               |           |             |           |
               +-----------+             +-----------+
```

## The CPU and Its Operation

The Central Processing Unit is responsible for executing program instructions. It consists of:

- **Control Unit**: Coordinates all activities within the CPU
- **Arithmetic Logic Unit (ALU)**: Performs mathematical and logical operations
- **Registers**: Small, high-speed storage locations within the CPU

```
+-------------------------------+
|            CPU                 |
|  +-------------------------+  |
|  |      Control Unit        |  |
|  +-------------------------+  |
|  +-------------------------+  |
|  |          ALU            |  |
|  +-------------------------+  |
|  +-------------------------+  |
|  |       Registers         |  |
|  |  - Program Counter (PC) |  |
|  |  - Instruction Register |  |
|  |  - Accumulator          |  |
|  +-------------------------+  |
+-------------------------------+
```

The CPU operates in a cycle known as the **fetch-decode-execute cycle**:

1. **Fetch**: Retrieve instruction from memory (address in PC)
2. **Decode**: Interpret the instruction
3. **Execute**: Perform the operation
4. **Update**: Increment PC to next instruction

## Memory Hierarchy

Computer systems use a memory hierarchy to balance speed, cost, and capacity:

```
+---------------------+
|                     |  Smallest, Fastest, Most Expensive
|      Registers      |
|                     |
+---------------------+
|                     |
|     Cache Memory    |
|                     |
+---------------------+
|                     |
|    Main Memory      |
|      (RAM/ROM)      |
|                     |
+---------------------+
|                     |
| Secondary Storage   |  Largest, Slowest, Least Expensive
|   (HDD/SSD)         |
|                     |
+---------------------+
```

**Characteristics of Memory Types:**

| Memory Type | Speed     | Capacity  | Cost     | Volatility   | Purpose              |
| ----------- | --------- | --------- | -------- | ------------ | -------------------- |
| Registers   | Fastest   | Few bytes | Highest  | Volatile     | CPU operations       |
| Cache       | Very Fast | KBs-MBs   | High     | Volatile     | Frequently used data |
| RAM         | Fast      | GBs       | Moderate | Volatile     | Active programs/data |
| ROM         | Moderate  | MBs       | Low      | Non-volatile | Firmware/BIOS        |
| Secondary   | Slowest   | TBs       | Lowest   | Non-volatile | Long-term storage    |

## I/O System Organization

Input/Output devices allow communication between the computer and external world. These include:

- Storage devices (hard drives, SSDs)
- User interface devices (keyboard, mouse, display)
- Network interfaces
- Peripheral devices (printers, scanners)

I/O operations are handled through:

- **Programmed I/O**: CPU directly controls data transfer
- **Interrupt-driven I/O**: Devices signal CPU when ready
- **Direct Memory Access (DMA)**: Special controller handles transfers without CPU involvement

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|      CPU       |<---->|     Memory     |<---->|   DMA Controller|
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       ^                         ^                      |
       |                         |                      |
       |                         |                      v
       |                         |             +----------------+
       +-------------------------+------------->|   I/O Device   |
                                                +----------------+
```

## Interrupts and Their Handling

Interrupts are signals that alert the CPU to important events requiring attention. Types of interrupts include:

- **Hardware interrupts**: From external devices (I/O completion, errors)
- **Software interrupts**: From programs (system calls, exceptions)
- **Traps**: Error conditions (division by zero, page fault)

**Interrupt Handling Process:**

1. Device sends interrupt signal to CPU
2. CPU finishes current instruction
3. CPU saves current state (registers, program counter)
4. CPU jumps to interrupt service routine (ISR)
5. ISR processes the interrupt
6. CPU restores saved state and resumes execution

## Storage Device Structure

Secondary storage devices have different organizational structures:

**Magnetic Disks:**

- Organized into tracks, sectors, and cylinders
- Data accessed through seek, rotation, and transfer times

```
          +-----------------------+
          |      Disk Platter     |
          |                       |
          |  +-----------------+  |
          |  |      Track      |  |
          |  |  +-----------+  |  |
          |  |  |  Sector   |  |  |
          |  |  +-----------+  |  |
          |  +-----------------+  |
          |                       |
          +-----------------------+
```

**Solid State Drives (SSDs):**

- Use flash memory with no moving parts
- Organized into blocks and pages
- Faster access but with write limitations

## Computer System Operation

When a computer starts up, it goes through a boot process:

1. **Power-on**: Hardware components receive power
2. **POST (Power-On Self-Test)**: Hardware diagnostics
3. **Bootstrap loader**: Loads initial program from ROM
4. **Kernel loading**: OS kernel loaded into memory
5. **System initialization**: OS starts services and drivers
6. **User authentication**: Login prompt appears

## Symmetric Multiprocessing (SMP)

Modern systems often use multiple processors that share resources:

```
+-------------------------------------------------+
|                                                 |
|                 Shared Memory                   |
|                                                 |
+-------------------------------------------------+
         ^                  ^                 ^
         |                  |                 |
+----------------+   +----------------+   +----------------+
|                |   |                |   |                |
|     CPU 1      |   |     CPU 2      |   |     CPU N      |
|                |   |                |   |                |
+----------------+   +----------------+   +----------------+
```

Advantages of SMP:

- Increased throughput (parallel processing)
- Improved reliability (fault tolerance)
- Economical (shared resources)

## Clustered Systems

Multiple systems work together as a single cohesive unit:

- **Asymmetric clustering**: One machine in hot-standby mode
- **Symmetric clustering**: All machines run applications and monitor each other

## Operating System's Role in System Organization

The OS acts as an intermediary between hardware and applications, providing:

1. **Resource Allocation**: Manages CPU time, memory space, file storage
2. **Control Program**: Manages execution of programs
3. **Kernel**: Core component that remains in memory

```
+-----------------------+
|                       |
|   Application Program |
|                       |
+-----------------------+
|                       |
|   Operating System    |
|                       |
+-----------------------+
|                       |
|       Hardware        |
|                       |
+-----------------------+
```

## Exam Tips

1. **Understand the fetch-decode-execute cycle** thoroughly as it's fundamental to CPU operation
2. **Memorize the memory hierarchy** and characteristics of each level
3. **Differentiate between interrupt types** and understand the interrupt handling process
4. **Know the advantages of multiprocessor systems** and how they differ from single-processor systems
5. **Practice drawing diagrams** of computer organization - visual representations often earn more marks
6. **Focus on the role of the OS** in managing each hardware component
7. **Understand storage device structures** especially the difference between magnetic disks and SSDs
