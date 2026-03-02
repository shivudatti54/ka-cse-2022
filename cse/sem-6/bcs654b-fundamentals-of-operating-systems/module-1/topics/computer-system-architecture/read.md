# Computer System Architecture

## Introduction

Computer system architecture refers to the conceptual design and fundamental operational structure of a computer system. It defines how the computer's hardware components are organized, interconnected, and operate together to execute programs. Understanding computer system architecture is essential for operating system design, as the OS must efficiently manage and abstract the underlying hardware resources.

## 1. Basic Computer System Organization

### 1.1 Von Neumann Architecture

The most widely used computer architecture, proposed by John von Neumann in 1945.

**Key Characteristics:**

- **Stored Program Concept**: Instructions and data are stored in the same memory
- **Sequential Execution**: Instructions are executed one after another
- **Single Bus**: Data and instructions share the same communication path

**Components:**

```
+----------------+
| Input Unit |
+----------------+
 |
 v
+----------------+ +----------------+ +----------------+
| Control |<-->| Arithmetic |<-->| Memory |
| Unit | | Logic | | Unit |
| (CU) | | Unit (ALU) | | |
+----------------+ +----------------+ +----------------+
 ^
 |
+----------------+
| Output Unit |
+----------------+
```

**Von Neumann Bottleneck:**
The shared bus between memory and CPU creates a bottleneck, as only one operation (fetch instruction or data) can occur at a time.

### 1.2 Harvard Architecture

An alternative architecture with separate memory for instructions and data.

**Key Characteristics:**

- **Separate Memory**: Instructions and data stored in separate memory units
- **Dual Bus**: Independent paths for instruction and data access
- **Simultaneous Access**: Can fetch instruction and data simultaneously

**Advantages:**

- Higher performance due to parallel access
- Better suited for specialized applications

**Disadvantages:**

- More complex hardware
- Higher cost

**Modern Usage:**
Most modern processors use a Modified Harvard Architecture - separate caches for instructions and data, but unified main memory.

## 2. Computer System Components

### 2.1 Central Processing Unit (CPU)

The "brain" of the computer that executes instructions.

**CPU Components:**

**1. Arithmetic Logic Unit (ALU)**

- Performs arithmetic operations (add, subtract, multiply, divide)
- Performs logical operations (AND, OR, NOT, XOR)
- Performs comparison operations

**2. Control Unit (CU)**

- Fetches instructions from memory
- Decodes instructions
- Controls execution sequence
- Manages data flow between components

**3. Registers**

- Small, high-speed storage within CPU
- Store temporary data and instructions
- Types: Program Counter (PC), Instruction Register (IR), Accumulator, General Purpose Registers

**CPU Operation Cycle (Fetch-Decode-Execute):**

```
1. FETCH: Retrieve instruction from memory
 ↓
2. DECODE: Interpret the instruction
 ↓
3. EXECUTE: Perform the operation
 ↓
4. STORE: Write results back to memory/register
 ↓
 (Repeat)
```

### 2.2 Memory Hierarchy

Computer systems use multiple levels of memory with varying speeds and capacities.

**Memory Hierarchy (Fastest to Slowest):**

```
+------------------------+
| CPU Registers | <-- Fastest, Smallest
+------------------------+
| L1 Cache |
+------------------------+
| L2 Cache |
+------------------------+
| L3 Cache |
+------------------------+
| Main Memory (RAM) |
+------------------------+
| Secondary Storage |
| (SSD, HDD) |
+------------------------+
| Tertiary Storage | <-- Slowest, Largest
| (Tape, Cloud) |
+------------------------+
```

**Memory Characteristics:**

| Level         | Typical Size   | Access Time | Technology |
| ------------- | -------------- | ----------- | ---------- |
| **Registers** | 32-256 bytes   | < 1 ns      | SRAM       |
| **L1 Cache**  | 32-128 KB      | 1-2 ns      | SRAM       |
| **L2 Cache**  | 256 KB - 1 MB  | 3-10 ns     | SRAM       |
| **L3 Cache**  | 2-64 MB        | 10-20 ns    | SRAM       |
| **RAM**       | 4-128 GB       | 50-100 ns   | DRAM       |
| **SSD**       | 128 GB - 4 TB  | 50-150 μs   | Flash      |
| **HDD**       | 500 GB - 20 TB | 5-15 ms     | Magnetic   |

**Principle of Locality:**

- **Temporal Locality**: Recently accessed data likely to be accessed again soon
- **Spatial Locality**: Data near recently accessed data likely to be accessed soon

### 2.3 Input/Output (I/O) System

Components that allow the computer to interact with external devices.

**I/O Devices:**

- **Input**: Keyboard, mouse, scanner, microphone, sensors
- **Output**: Monitor, printer, speakers
- **Storage**: Hard drives, SSDs, USB drives
- **Network**: Network interface cards, modems

**I/O Controllers:**
Specialized hardware that manages communication between CPU and I/O devices.

## 3. System Buses

Buses are communication pathways that transfer data between components.

### 3.1 Types of Buses

**1. Data Bus**

- Carries actual data being processed
- Bidirectional (data flows both ways)
- Width determines data transfer capacity (32-bit, 64-bit)

**2. Address Bus**

- Carries memory addresses
- Unidirectional (CPU to memory)
- Width determines maximum addressable memory (2^n addresses)

**3. Control Bus**

- Carries control signals (read, write, interrupt)
- Manages coordination between components
- Includes timing signals

```
 CPU
 |
 +-----+-----+
 | | |
 Data Addr Ctrl
 Bus Bus Bus
 | | |
 +-----+-----+
 |
 +------+-------+------+
 | | | |
Memory I/O I/O I/O
 Dev1 Dev2 Dev3
```

## 4. Multiprocessor Systems

Modern systems often contain multiple processors for improved performance.

### 4.1 Types of Multiprocessor Systems

**1. Symmetric Multiprocessing (SMP)**

- All processors are equal
- Share same main memory
- Run same OS instance
- Example: Modern multi-core CPUs

```
+------+ +------+ +------+
| CPU | | CPU | | CPU |
| 0 | | 1 | | 2 |
+------+ +------+ +------+
 | | |
 +----Shared Bus-----+
 |
 +---------+
 | Memory |
 +---------+
```

**2. Asymmetric Multiprocessing (AMP)**

- Master-slave relationship
- Different processors perform different tasks
- Less common in modern systems

**3. Multicore Processors**

- Multiple CPU cores on single chip
- Shared cache levels
- Better power efficiency than separate CPUs

### 4.2 NUMA (Non-Uniform Memory Access)

Architecture where memory access time depends on memory location relative to processor.

**Characteristics:**

- Each processor has local memory (faster access)
- Can access other processors' memory (slower)
- Scalable to many processors

## 5. Storage Structure

### 5.1 Primary Storage (Main Memory)

**RAM (Random Access Memory):**

- Volatile (loses data when power off)
- Directly accessible by CPU
- Used for running programs and data

**ROM (Read-Only Memory):**

- Non-volatile (retains data when power off)
- Contains firmware and boot programs
- Cannot be easily modified

### 5.2 Secondary Storage

**Characteristics:**

- Non-volatile
- Large capacity
- Slower than main memory
- Used for long-term storage

**Types:**

- **Magnetic Disks (HDD)**: Rotating platters, mechanical
- **Solid State Drives (SSD)**: Flash memory, no moving parts
- **Optical Disks**: CD, DVD, Blu-ray
- **Magnetic Tape**: Archival storage

### 5.3 Caching

Storing copies of frequently accessed data in faster storage.

**Cache Levels:**

- **L1 Cache**: Integrated with CPU core, smallest and fastest
- **L2 Cache**: Larger, shared by one or few cores
- **L3 Cache**: Largest, shared by all cores on chip

**Cache Operations:**

- **Cache Hit**: Data found in cache (fast)
- **Cache Miss**: Data not in cache, must fetch from memory (slow)

## 6. Interrupt Handling

Mechanism for I/O devices to signal the CPU that they need attention.

### 6.1 Interrupt Process

```
1. Device generates interrupt signal
 ↓
2. CPU suspends current task
 ↓
3. CPU saves current state
 ↓
4. CPU executes interrupt handler
 ↓
5. Handler processes interrupt
 ↓
6. CPU restores saved state
 ↓
7. CPU resumes interrupted task
```

### 6.2 Types of Interrupts

**Hardware Interrupts:**

- Generated by devices (keyboard, disk, timer)
- Asynchronous (can occur anytime)

**Software Interrupts (Traps):**

- Generated by programs (system calls)
- Synchronous (occur at specific points)

**Exceptions:**

- Error conditions (divide by zero, page fault)
- Must be handled immediately

## 7. DMA (Direct Memory Access)

Allows I/O devices to transfer data directly to/from memory without CPU intervention.

**Benefits:**

- Frees CPU for other tasks
- Faster data transfer
- Reduced CPU overhead

**DMA Process:**

1. CPU initiates DMA transfer
2. DMA controller takes over bus
3. Data transferred directly between device and memory
4. DMA controller interrupts CPU when complete

## 8. Modern Architectural Trends

### 8.1 Pipelining

Overlapping execution of multiple instructions for better throughput.

### 8.2 Superscalar Architecture

Multiple execution units allowing parallel instruction execution.

### 8.3 RISC vs. CISC

| Feature          | RISC                 | CISC                     |
| ---------------- | -------------------- | ------------------------ |
| **Instructions** | Simple, fixed-length | Complex, variable-length |
| **Execution**    | Single cycle         | Multiple cycles          |
| **Registers**    | Many                 | Fewer                    |
| **Compiler**     | Complex              | Simpler                  |
| **Examples**     | ARM, RISC-V          | x86, x86-64              |

## 9. Exam Tips and Key Takeaways

1. **Understand Von Neumann Architecture**: Know the components and the bottleneck issue

2. **Memory Hierarchy**: Remember the order from fastest to slowest and the principle of locality

3. **CPU Components**: Understand ALU, Control Unit, and Registers

4. **Fetch-Decode-Execute Cycle**: Be able to draw and explain this fundamental operation

5. **Bus Types**: Know the difference between data, address, and control buses

6. **Interrupts**: Understand how interrupts work and their importance for I/O

7. **Multiprocessor Types**: Know SMP vs. NUMA architectures

8. **DMA**: Understand why DMA is important for efficient I/O

9. **Cache**: Understand cache levels and hit/miss concepts

10. **Real-World Examples**: Relate concepts to modern processors (Intel Core, AMD Ryzen, ARM)

### Further Reading

Refer to your prescribed textbook and official course materials.
