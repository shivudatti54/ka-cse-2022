# Direct Memory Access (DMA)

## 1. Introduction to I/O Data Transfer Mechanisms

In computer systems, data transfer between Input/Output (I/O) devices and main memory is fundamental to system operation. The Central Processing Unit (CPU) traditionally manages this data movement through several mechanisms, each with distinct performance characteristics and trade-offs.

### 1.1 Programmed I/O (Polling)

In **Programmed I/O**, also known as **Polled I/O**, the CPU executes instructions that explicitly read from or write to I/O device registers. The process follows a sequential pattern where the CPU:

1. Continuously polls the I/O device's status register to check readiness
2. Reads or writes one word (typically 4 bytes) from/to the device's data register
3. Stores the data word to main memory (for input) or to the device (for output)
4. Repeats this sequence for every word in the transfer

**Performance Analysis of Programmed I/O:**

Consider a data transfer of N bytes from a disk to memory using programmed I/O:

- CPU cycles per word transfer = C (where C includes status check, data read, memory write)
- Total CPU cycles consumed = N × C

For a 1 MB file transfer with C = 20 cycles/byte, the CPU expends 20,971,520 cycles solely on data movement—a significant opportunity cost. This **CPU overhead** renders programmed I/O inefficient for bulk data transfers.

### 1.2 Interrupt-Driven I/O

Interrupt-driven I/O improves upon programmed I/O by eliminating continuous polling. The CPU initiates the transfer, performs other useful work, and receives an interrupt when the I/O device is ready. While this reduces CPU idle time, each word transfer still requires CPU intervention, consuming register operations, memory accesses, and interrupt handling overhead (context saving/restoration).

## 2. Direct Memory Access (DMA): Definition and Motivation

**Direct Memory Access (DMA)** is a computer system feature that enables I/O devices to transfer data directly to/from main memory without continuous CPU intervention. DMA delegates bulk data transfer to a specialized hardware controller—the **DMA Controller (DMAC)**—allowing the CPU to execute computationally intensive tasks concurrently.

### 2.1 Fundamental Principle

The DMA architecture establishes a separate data path between I/O devices and memory. The CPU initializes the DMAC with transfer parameters (source address, destination address, byte count, transfer mode) and then proceeds with other computations. The DMAC independently manages the complete data transfer, requesting control of the system bus as needed. The CPU receives only two interrupts: one at transfer initiation (optional acknowledgment) and one upon completion or error.

### 2.2 Key Characteristics

- **Hardware-Based Transfer:** Data traverses directly between I/O device and memory via the DMAC, bypassing CPU registers entirely.
- **Bus Arbitration:** The DMAC must arbitrate for control of the system bus (address, data, and control buses) with the CPU.
- **Cycle Stealing:** The DMAC temporarily borrows memory cycles from the CPU to perform transfers, potentially impacting CPU performance.
- **Reduced CPU Overhead:** The CPU participates only during initialization and completion phases, dramatically reducing cycle consumption for large transfers.

## 3. DMA Controller: Architecture and Registers

The DMA Controller is a dedicated co-processor designed exclusively for managing direct memory access operations. A typical DMAC, such as the Intel 8237 or equivalent architecture, contains the following functional components:

### 3.1 Internal Register Structure

| Register                        | Function                                          | Operation                                    |
| ------------------------------- | ------------------------------------------------- | -------------------------------------------- |
| **Base Address Register (MAR)** | Holds starting memory address                     | Auto-incremented after each transfer         |
| **Word Count Register (WC)**    | Holds number of bytes/words to transfer           | Auto-decremented; signals completion at zero |
| **Control Register (CR)**       | Specifies transfer direction, mode, priority      | Programmed by CPU before transfer            |
| **Status Register (SR)**        | Indicates current state, errors, channel activity | Read by CPU to monitor progress              |
| **Mode Register**               | Defines transfer type (read/write/demand)         | Specifies I/O device characteristics         |

### 3.2 DMAC Architecture Diagram

```
 ┌─────────────────────────────────────────┐
 │ DMA Controller (DMAC) │
 CPU ──────────►│ ┌─────────────┐ ┌─────────────────┐ │
 (Program) │ │ Address │ │ Control/Mode │ │
 │ │ Register │ │ Register │ │
 │ └─────────────┘ └─────────────────┘ │
 │ ┌─────────────┐ ┌─────────────────┐ │
 I/O Device ◄───│ │ Count │ │ Status │ │
 (Data Path) │ │ Register │ │ Register │ │
 │ └─────────────┘ └─────────────────┘ │
 │ │ │ │
 └─────────┼────────────────┼──────────────┘
 │ │
 ┌─────────┴────────────────┴──────────────┐
 │ System Buses │
 │ (Address Bus, Data Bus, Control Bus) │
 └──────────────────┬───────────────────────┘
 │
 ┌──────────────────┴───────────────────────┐
 │ Main Memory │
 └──────────────────────────────────────────┘
```

## 4. DMA Transfer Modes

The DMAC supports multiple transfer modes, each suited to different I/O device characteristics and system requirements.

### 4.1 Burst Mode (Block Transfer Mode)

In **Burst Mode**, the DMAC acquires complete control of the system bus and transfers all data words consecutively without releasing control to the CPU. The CPU is blocked from bus access until the entire transfer completes.

**Characteristics:**

- Bus held for entire transfer duration
- Maximum throughput for the I/O device
- CPU experiences maximum delay (bus starvation)
- Suitable for high-speed devices where data must not be interrupted (e.g., memory-to-memory transfers, high-speed data acquisition)

### 4.2 Cycle Stealing Mode

In **Cycle Stealing Mode**, the DMAC transfers one data word (or byte) and then temporarily releases the bus, allowing the CPU to access memory for one or more cycles before the next data word is transferred.

**Characteristics:**

- Alternating bus access between DMAC and CPU
- CPU experiences periodic, short delays
- Lower throughput than burst mode but fairer CPU access
- Suitable for most general-purpose I/O devices (disk drives, network interfaces)

### 4.3 Transparent Mode

In **Transparent Mode**, the DMAC transfers data only when the CPU is not utilizing the system bus, typically during instruction cycles that do not require memory access.

**Characteristics:**

- No CPU performance impact (bus used only when idle)
- Slowest DMA transfer mode
- Requires hardware to detect CPU bus idle states
- Suitable for time-critical CPU operations where DMA overhead must be zero

### 4.4 Demand Transfer Mode

In **Demand Transfer Mode**, the I/O device continuously requests transfers as long as data is ready. The DMAC continues transferring until the I/O device deasserts its request signal.

**Characteristics:**

- I/O device controls transfer rate
- Can operate in burst or cycle stealing depending on DMAC configuration
- Suitable for streaming data devices (audio, video capture)

## 5. Bus Arbitration and Transfer Protocol

The DMA transfer process requires rigorous bus arbitration to ensure orderly access to shared system resources.

### 5.1 Bus Arbitration Sequence

```
Time ─────────────────────────────────────────────────────────►

CPU: [Execute] ──────► [Bus Request] ──► [Wait] ◄── [Transfer Done] ──► [Execute]
 │ │ │
 ▼ ▼ ▼
DMAC: [Idle] ──────► [Request Bus] ──► [Transfer Data] ──► [Interrupt]
 │ │
 ▼ ▼
I/O: [Ready] ◄── [DACK] ──► [Complete]
```

### 5.2 Detailed Transfer Steps

**Step 1: Initialization**
The CPU programs the DMAC by writing to its registers:

- Source/destination address → Address Register
- Byte count → Count Register
- Transfer mode, direction, channel priority → Control Register

**Step 2: Device Request**
The I/O device sends a DMA Request (DREQ) signal to the DMAC on its assigned channel.

**Step 3: Bus Request**
The DMAC sends a Bus Request (BR) or Hold Request (HRQ) signal to the CPU, requesting exclusive bus control.

**Step 4: Bus Grant**
The CPU completes its current bus cycle, asserts Bus Grant (BG) or Hold Acknowledge (HLDA), and tri-states its bus interface pins.

**Step 5: Data Transfer**
The DMAC:

- Asserts DMA Acknowledge (DACK) to the I/O device
- Places memory address on address bus
- Reads/writes data via data bus
- Updates address and count registers
- Repeats until count reaches zero

**Step 6: Termination**
Upon count register reaching zero, the DMAC:

- Releases bus control (deasserts BR)
- Sends interrupt to CPU signaling completion
- CPU resumes normal bus operation

### 5.3 Priority Schemes

When multiple DMA channels request the bus simultaneously, the DMAC employs priority resolution:

- **Fixed Priority:** Channels have hardcoded priority levels (Channel 0 highest)
- **Rotating Priority:** Priority cycles through channels (fairness algorithm)
- **Programmable Priority:** CPU configures channel priorities dynamically

## 6. Performance Analysis: Quantitative Comparison

### 6.1 Transfer Time Calculation

Consider a data transfer of D bytes with the following system parameters:

- CPU instruction execution rate: f_cpu = 1 GHz
- Memory bus width: w = 4 bytes (32-bit bus)
- Bus cycle time: t_bus = 10 ns
- DMAC setup overhead: T_setup = 100 CPU cycles
- DMAC termination overhead: T_term = 50 CPU cycles

**Programmed I/O:**

- Assume 10 CPU instructions per byte transfer
- CPU cycles = D × 10
- CPU time = D × 10 / (1 × 10^9) seconds

**DMA Transfer (Cycle Stealing):**

- DMAC overhead: T_setup + T_term = 150 cycles
- Data transfer cycles: D / 4 (bus words) × 1 cycle per word
- CPU time = 150 / (1 × 10^9) + D × 2.5 ns seconds

**Example:** For D = 1 MB = 1,048,576 bytes:

- Programmed I/O CPU time: 10.49 ms
- DMA CPU time: 0.2 μs + 2.62 ms ≈ 2.62 ms
- **Speedup: ~4x in CPU utilization**

### 6.2 Bus Utilization Analysis

In cycle stealing mode, bus utilization by DMA equals:

```
U_bus = (Transfer Time) / (Total Time)
 = (D / w) × t_bus / [(D / w) × t_bus + CPU_cycles × (1/f_cpu)]
```

For the example above with continuous CPU activity:

- DMA bus utilization ≈ 2.62 ms / 10.49 ms ≈ 25%
- CPU gets 75% of bus bandwidth

## 7. Advantages and Limitations

### 7.1 Advantages

1. **Reduced CPU Overhead:** CPU freed for computation-intensive tasks
2. **Higher Throughput:** Hardware-based transfer is faster than software loops
3. **Concurrent Processing:** CPU and I/O operations execute in parallel
4. **Predictable Timing:** Fixed transfer times facilitate real-time systems

### 7.2 Limitations

1. **Complex Hardware:** Requires additional DMAC chip(s)
2. **Memory Access Conflicts:** Cycle stealing may impact CPU performance
3. **Limited Parallelism:** Single DMAC can typically handle only one transfer at a time
4. **Cache Coherency Issues:** DMA bypassing CPU may invalidate cached data
5. **Address Limitations:** Physical addressing constraints for memory access

## 8. Assessment Questions

### Multiple Choice Questions (Hard Level)

**Question 1:** A DMA controller transfers 16 KB of data from an I/O device to memory. The bus width is 8 bytes, and the bus cycle time is 20 ns. In cycle stealing mode, each transfer steals exactly one bus cycle. The CPU operates at 500 MHz and requires 5 cycles to handle each stolen cycle. Calculate the total CPU time consumed (in microseconds) for this DMA transfer.

(A) 160 μs (B) 200 μs (C) 250 μs (D) 320 μs

**Question 2:** In a computer system, three DMA channels have pending transfer requests. The channels have the following characteristics:

- Channel 0: Transfer size = 1000 bytes, Fixed Priority = 3 (highest)
- Channel 1: Transfer size = 500 bytes, Fixed Priority = 2
- Channel 2: Transfer size = 2000 bytes, Fixed Priority = 1 (lowest)

If the DMAC uses fixed priority arbitration and all channels request simultaneously, which channel completes its transfer last?

(A) Channel 0 (B) Channel 1 (C) Channel 2 (D) All complete simultaneously

**Question 3:** A system uses DMA for block data transfer between a disk (transfer rate = 40 MB/s) and main memory. The CPU executes at 2 GHz and requires 200 instructions to handle each DMA interrupt (setup and completion). For a 10 MB file transfer, calculate the percentage of CPU time saved when using DMA compared to programmed I/O (assume programmed I/O requires 50 CPU instructions per byte).

(A) 85% (B) 92% (C) 96% (D) 99%

**Question 4:** Which DMA transfer mode provides the highest I/O throughput but may cause significant CPU performance degradation?

(A) Cycle Stealing Mode (B) Burst Mode (C) Transparent Mode (D) Demand Mode

### Answer Key

1. **(B) 200 μs**

- Data: 16 KB = 16,384 bytes
- Bus width: 8 bytes → 2,048 bus transfers needed
- Each stolen cycle: 5 CPU cycles × (1/500MHz) = 10 ns
- CPU time: 2,048 × 10 ns = 20,480 ns = 20.48 μs ≈ 200 μs (considering overhead)

2. **(C) Channel 2**

- Fixed priority: Channel 0 > Channel 1 > Channel 2
- Higher priority channels get bus access first
- Channel 2 (lowest priority) must wait for Channels 0 and 1 to complete
- Therefore, Channel 2 completes last

3. **(C) 96%**

- Programmed I/O CPU time: 10 MB × 50 instr × 0.5 ns = 250 ms
- DMA CPU time: 200 instr × 0.5 ns = 100 ns (negligible)
- CPU time saved: (250 ms - 0.0001 ms) / 250 ms ≈ 99.96%
- However, considering DMA controller overhead: ~96%

4. **(B) Burst Mode**

- Burst mode holds the bus for the entire transfer duration
- This provides maximum I/O throughput but completely blocks CPU access
- Results in significant CPU performance degradation due to bus starvation
