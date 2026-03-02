# Accessing I/O Devices

## 1. Introduction

Input/Output (I/O) devices constitute essential peripheral components that enable communication between a computer system and the external environment. The mechanisms employed for accessing I/O devices significantly influence system performance, CPU utilization, and overall architectural complexity. Understanding these access methods is fundamental to computer organization and operating system design.

## 2. Classification of I/O Devices

### 2.1 Input Devices

Devices that transmit data to the CPU include keyboards, mice, scanners, microphones, and various sensors.

### 2.2 Output Devices

Devices that receive data from the CPU include monitors, printers, speakers, and actuators.

### 2.3 Storage Devices

Devices providing persistent data storage include Hard Disk Drives (HDD), Solid State Drives (SSD), and USB flash drives.

### 2.4 Communication Devices

Devices facilitating data exchange with remote systems include Network Interface Cards (NIC) and modems.

## 3. Fundamental Differences: I/O vs Memory Access

| Aspect              | Memory Access                   | I/O Device Access                       |
| ------------------- | ------------------------------- | --------------------------------------- |
| **Access Time**     | Fast (nanoseconds)              | Variable (microseconds to milliseconds) |
| **Synchronization** | Synchronous                     | Often asynchronous                      |
| **Error Rates**     | Minimal                         | Frequent due to external factors        |
| **Addressing**      | Simple linear addressing        | Complex protocol-based addressing       |
| **Data Transfer**   | Block-oriented or word-oriented | Stream or packet-oriented               |

## 4. I/O Interface Architecture

An I/O interface provides the necessary hardware components to connect peripheral devices to the system bus:

### 4.1 Interface Components

1. **Data Register**: Temporary storage for data being transferred between CPU and device
2. **Status Register**: Contains flags indicating device state (READY, BUSY, ERROR, DONE)
3. **Control Register**: Specifies operation mode, direction, and enable signals
4. **Address Decoder**: Translates CPU address signals to select specific device registers

### 4.2 Handshaking Protocol

The fundamental handshaking sequence between CPU and I/O device involves:

1. CPU writes command to control register
2. Device sets BUSY flag in status register
3. Device performs operation
4. Device sets DONE flag and clears BUSY
5. CPU reads status and acknowledges completion

## 5. I/O Addressing Schemes

### 5.1 Memory-Mapped I/O (MMIO)

In memory-mapped I/O, I/O devices share the same physical address space as system memory. Device registers are assigned unique memory addresses, and standard load/store instructions access I/O registers.

**Mathematical Representation:**

```
Physical Address Space = [0, M) ∪ [I/O Base, I/O Base + N)
Where M = Main Memory Size
 N = I/O Device Register Space
```

**Advantages:**

- Utilizes complete instruction set for I/O operations
- No dedicated I/O instructions required
- Simplified CPU design (single addressing unit)

**Disadvantages:**

- Reduces available memory address space
- Slower access for simple I/O operations
- No protection mechanism for I/O addresses

### 5.2 Isolated I/O (Port-Mapped I/O)

Isolated I/O maintains separate address spaces for memory and I/O devices, requiring dedicated IN and OUT instructions.

**Address Decoding:**

```
if (M/IO# pin = 1) → Memory Space
if (M/IO# pin = 0) → I/O Space
```

**Advantages:**

- Preserves full memory address space
- Explicit distinction between I/O and memory operations
- Simpler device address decoding

**Disadvantages:**

- Limited instruction set for I/O operations
- Additional CPU pin and control logic required

## 6. Methods of I/O Access

### 6.1 Programmed I/O (Polling)

In programmed I/O, the CPU executes a continuous loop to monitor device status before initiating data transfer.

#### 6.1.1 Operational Algorithm

```
1. CPU writes command to device control register
2. repeat
 status ← READ(status_register)
 until (status.READY = TRUE)
3. CPU reads/writes data from/to data register
4. Repeat steps 1-3 for subsequent operations
```

#### 6.1.2 Performance Analysis

**Time Wasted in Polling:**

Let Tₚ be the time to poll once, D be the device service time, and N be the number of polls required:

$$T_{total} = N \cdot T_p + D$$

The polling overhead ratio is:

$$\eta = \frac{N \cdot T_p}{N \cdot T_p + D} = \frac{T_p}{T_p + \frac{D}{N}}$$

When D ≫ N·Tₚ, polling becomes efficient. However, for slow devices where D ≈ N·Tₚ, significant CPU time is wasted.

**Example Calculation:**
If Tₚ = 10μs, D = 100μs, and N = 50:
$$T_{total} = 50 \times 10\mu s + 100\mu s = 600\mu s$$
$$\eta = \frac{500}{600} = 83.3\% \text{ overhead}$$

#### 6.1.3 Pseudocode Implementation

```c
#define STATUS_REG (*(volatile uint32_t*)0x40001000)
#define DATA_REG (*(volatile uint32_t*)0x40001004)
#define CTRL_REG (*(volatile uint32_t*)0x40001008)

#define STATUS_READY 0x01
#define STATUS_ERROR 0x02

int read_device(uint32_t *data) {
 // Initiate read operation
 CTRL_REG = 0x01;

 // Poll until ready or error
 while (1) {
 uint32_t status = STATUS_REG;
 if (status & STATUS_ERROR) return -1;
 if (status & STATUS_READY) break;
 }

 *data = DATA_REG;
 return 0;
}
```

### 6.2 Interrupt-Driven I/O

Interrupt-driven I/O enables asynchronous communication between CPU and devices, allowing the CPU to execute other tasks while waiting for I/O completion.

#### 6.2.1 Interrupt Processing Sequence

1. **Interrupt Request (IRQ)**: Device raises interrupt request line
2. **Interrupt Recognition**: CPU completes current instruction
3. **Interrupt Acknowledgment**: CPU sends acknowledgment, obtains interrupt vector
4. **Context Save**: Push PC, PSW, and registers onto stack
5. **ISR Execution**: Transfer control to Interrupt Service Routine
6. **Context Restore**: Pop saved state from stack
7. **Resume Execution**: Return to interrupted program

#### 6.2.2 Interrupt Latency Analysis

Total interrupt latency L comprises:
$$L = L_d + L_c + L_h + L_s$$

Where:

- L_d = Detection delay (time from IRQ to CPU recognition)
- L_c = Context save time
- L_h = Handler invocation time
- L_s = Stack operation time

For a system with T-cycle instruction time:
$$L_c = n \times T \quad \text{(n = number of registers saved)}$$

#### 6.2.3 Interrupt Priority Mechanisms

**Daisy Chain Priority:**

```
Device 1 → Device 2 → Device 3 → CPU
(Priority: Device 1 > Device 2 > Device 3)
```

**Parallel Priority Encoding:**
Hardware priority encoder determines highest-priority requesting device.

#### 6.2.4 Pseudocode: Interrupt Handler

```c
// Interrupt Service Routine for serial device
void serial_isr(void) {
 // Save additional context if needed
 uint32_t status = *((volatile uint32_t*)0x40002000);

 if (status & RX_READY) {
 char c = *((volatile char*)0x40002004);
 circular_buffer_put(&rx_buffer, c);
 }

 if (status & TX_READY) {
 if (!circular_buffer_empty(&tx_buffer)) {
 char c = circular_buffer_get(&tx_buffer);
 *((volatile char*)0x40002004) = c;
 }
 }

 // Clear interrupt flags
 *((volatile uint32_t*)0x40002000) = 0;
}
```

### 6.3 Direct Memory Access (DMA)

DMA enables direct data transfer between I/O devices and memory without CPU intervention, significantly improving throughput for large transfers.

#### 6.3.1 DMA Controller Architecture

**Key Registers:**

- **Source Address Register**: Starting memory address for read operations
- **Destination Address Register**: Target memory address for write operations
- **Word Count Register**: Number of data units to transfer
- **Control Register**: Transfer mode, direction, and enable bits
- **Status Register**: Transfer progress and error flags

#### 6.3.2 DMA Transfer Cycle

```
1. CPU programs DMA controller:
 - Set source/destination addresses
 - Configure word count and transfer mode
 - Enable DMA channel

2. CPU continues execution; DMA controller operates autonomously

3. For each data unit:
 a. DMA requests bus control via HRQ signal
 b. CPU acknowledges via HLDA, releases bus
 c. DMA performs single memory-I/O transfer
 d. DMA releases bus (cycle stealing) or retains (burst)

4. Transfer complete: DMA sends interrupt to CPU
```

#### 6.3.3 DMA Transfer Modes

**Burst Mode (Block Transfer):**

- Acquires bus and transfers entire data block
- CPU blocked during transfer duration
- Formula: T_burst = (N × T_cycle), where N = word count
- Maximum throughput, minimum transfer time

**Cycle Stealing Mode:**

- Transfers single data unit per bus cycle
- CPU executes between stolen cycles
- Formula: T_stealed = N × (T_cycle + T_cpu)
- Lower throughput, CPU remains partially active

**Transparent Mode:**

- DMA transfers only when CPU is idle
- Requires bus idle detection
- Formula: T_transparent ≥ T_burst (depends on CPU bus usage)
- Slowest transfer, zero CPU impact

#### 6.3.4 Performance Comparison

**Time Comparison for N-word Transfer:**

| Method         | Transfer Time         | CPU Block Time |
| -------------- | --------------------- | -------------- |
| Programmed I/O | N × (T_poll + T_io)   | N × T_poll     |
| Interrupt I/O  | N × T_io + O(1)       | Near zero      |
| DMA (Burst)    | N × T_cycle           | N × T_cycle    |
| DMA (Steal)    | N × (T_cycle + T_cpu) | Zero           |

**Proof of DMA Efficiency:**

For large transfers (N >> 1):

- Programmed I/O: CPU time = N × T_poll
- DMA: CPU time ≈ 0

Therefore, DMA provides O(N) reduction in CPU overhead for large N.

## 7. Comparative Analysis

| Criterion               | Programmed I/O       | Interrupt I/O | DMA          |
| ----------------------- | -------------------- | ------------- | ------------ |
| **CPU Involvement**     | Continuous           | Minimal       | None         |
| **Hardware Complexity** | Low                  | Medium        | High         |
| **Throughput**          | Low                  | Medium        | High         |
| **Latency**             | Deterministic        | Variable      | Low          |
| **Suitable For**        | Simple, fast devices | Moderate data | Large blocks |

## 8. Summary

This module covered the three fundamental methods of I/O access: programmed I/O (polling), interrupt-driven I/O, and Direct Memory Access (DMA). We examined the architectural differences between memory-mapped and port-mapped I/O addressing schemes, analyzed performance characteristics through mathematical models, and explored the trade-offs between implementation complexity and system efficiency. The selection of appropriate I/O access methodology depends on device characteristics, data transfer volume, and real-time requirements.
