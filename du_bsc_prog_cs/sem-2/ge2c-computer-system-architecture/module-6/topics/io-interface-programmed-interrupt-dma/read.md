# IO Interface: Programmed Interrupt DMA

## Comprehensive Study Material for BSc Physical Science (CS) - Delhi University NEP 2024

---

## 1. Introduction and Real-World Relevance

In modern computer systems, the efficient transfer of data between the CPU and peripheral devices is crucial for system performance. The **I/O Interface** refers to the mechanisms and protocols that enable communication between the central processing unit (CPU) and external devices such as keyboards, mice, printers, hard drives, and network cards.

This topic covers three fundamental methods of I/O data transfer:

1. **Programmed I/O (Polling)** - CPU actively monitors devices
2. **Interrupt-Driven I/O** - Devices notify CPU when ready
3. **Direct Memory Access (DMA)** - Devices transfer data directly to memory

### Real-World Relevance

Consider these everyday scenarios:

- **Loading a game from a hard drive**: Without efficient I/O, games would take minutes to load
- **Streaming video online**: DMA ensures smooth playback by transferring data directly to memory
- **Typing in a text editor**: Interrupt-driven I/O provides responsive typing without constant polling
- **File transfers**: DMA enables high-speed transfers without CPU overhead

For Delhi University students, understanding these concepts is essential as they form the foundation of computer architecture and system programming.

---

## 2. I/O Interface Fundamentals

### 2.1 What is an I/O Interface?

An I/O interface consists of:

- **I/O Devices**: Hardware components that perform input or output functions
- **Device Controllers**: Hardware that manages communication between CPU and devices
- **System Bus**: The pathway for data transfer
- **Device Drivers**: Software that allows OS to communicate with hardware

### 2.2 I/O Addressing Methods

There are two primary methods for addressing I/O devices:

| Method | Description | Example |
|--------|-------------|---------|
| **Memory-Mapped I/O** | Devices are mapped to memory addresses | x86 architecture |
| **Isolated I/O** | Separate address space for I/O | x86 IN/OUT instructions |

---

## 3. Programmed I/O (Polling)

### 3.1 Concept and Working

In **Programmed I/O**, also known as **Polling**, the CPU continuously checks the status of I/O devices to determine if they are ready for data transfer. The CPU executes a loop that repeatedly reads the device's status register until it indicates that data is ready or the device is ready to accept data.

### 3.2 How It Works

1. CPU writes to device control registers to initiate I/O
2. CPU continuously reads the status register in a loop
3. When status indicates "ready," CPU reads/writes data
4. CPU processes the data and continues

### 3.3 Implementation Details

```
Status Register Bits:
- bit 0: Ready (1 = ready, 0 = not ready)
- bit 1: Error (1 = error occurred)
- bit 2: Busy (1 = device busy)
```

### 3.4 Example: Keyboard Input with Programmed I/O

```c
// Programmed I/O Example: Reading from Keyboard
// Assumptions: Status register at port 0x64, Data register at port 0x60

#include <stdio.h>

// Pseudo-code for illustration
#define KEYBOARD_STATUS 0x64
#define KEYBOARD_DATA   0x60
#define STATUS_READY    0x01

unsigned char inport(unsigned short port) {
    // Assembly code to read from I/O port
    unsigned char ret;
    asm volatile ("inb %1, %0" : "=a"(ret) : "dN"(port));
    return ret;
}

void read_keyboard_programmed() {
    unsigned char status, data;
    
    // Polling loop - CPU keeps checking until key is pressed
    while (1) {
        status = inport(KEYBOARD_STATUS);
        
        // Check if data is ready (bit 0)
        if (status & STATUS_READY) {
            data = inport(KEYBOARD_DATA);
            printf("Key pressed: %c\n", data);
            
            // Break on ESC key (key code 27)
            if (data == 27) break;
        }
        // CPU is busy waiting here - wasting cycles
    }
}

int main() {
    printf("Programmed I/O Example - Press any key (ESC to quit)\n");
    read_keyboard_programmed();
    return 0;
}
```

### 3.5 Advantages of Programmed I/O

- **Simple implementation**: Easy to understand and code
- **No special hardware**: Works with basic device controllers
- **Predictable timing**: CPU checks at known intervals
- **Low latency for fast devices**: Immediate response for quick operations

### 3.6 Disadvantages of Programmed I/O

- **CPU inefficiency**: CPU wastes cycles polling idle devices
- **Poor scalability**: Multiple devices create conflicts
- **High power consumption**: Continuous polling keeps CPU active
- **Not suitable for slow devices**: Wastes time waiting
- **No real-time response guarantee**: Depends on polling frequency

---

## 4. Interrupt-Driven I/O

### 4.1 Concept and Working

**Interrupt-Driven I/O** is a method where the CPU performs other tasks while waiting for I/O operations. When an I/O device needs attention, it sends an **interrupt signal** to the CPU, which then pauses its current work to handle the device.

### 4.2 How Interrupts Work

1. **Device Ready**: I/O device completes its task or needs attention
2. **Interrupt Request (IRQ)**: Device raises an interrupt request line
3. **Interrupt Acknowledgment**: CPU finishes current instruction
4. **Save State**: CPU saves current context (registers, program counter)
5. **Interrupt Service Routine (ISR)**: CPU executes the appropriate handler
6. **Restore State**: CPU resumes previous task

### 4.3 Types of Interrupts

| Type | Description | Examples |
|------|-------------|----------|
| **Hardware Interrupts** | Generated by external devices | Keyboard, mouse, timer |
| **Software Interrupts** | Generated by CPU instructions | System calls, divide by zero |
| **Maskable Interrupts** | Can be ignored by CPU | Most I/O devices |
| **Non-Maskable Interrupts (NMI)** | Cannot be ignored | Critical errors, power failure |

### 4.4 Interrupt Priority and Vector Table

```
Interrupt Vector Table (Typical x86):
- IRQ 0: Timer
- IRQ 1: Keyboard
- IRQ 2: Cascade (IRQ 8-15)
- IRQ 3: COM2
- IRQ 4: COM1
- IRQ 6: Floppy Disk
- IRQ 12: Mouse
- IRQ 13: Math Coprocessor
- IRQ 14: Primary IDE
- IRQ 15: Secondary IDE
```

### 4.5 Example: Keyboard Input with Interrupt-Driven I/O

```c
// Interrupt-Driven I/O Example: Keyboard Handler
// This demonstrates how an ISR works

#include <stdio.h>
#include <signal.h>

// Define interrupt handler function
// In real systems, this would be registered with the OS
volatile int key_pressed = 0;
volatile unsigned char key_code = 0;

// Interrupt Service Routine (ISR) for keyboard
void keyboard_isr(void) {
    // In real hardware, read from keyboard data port
    // unsigned char data = inport(0x60);
    
    key_pressed = 1;
    key_code = 0x1E; // Example: 'A' key
    
    // Acknowledge interrupt (tell device we're handling it)
    // outport(0x20, 0x20); // Send End of Interrupt (EOI)
}

// Main program demonstrating interrupt-driven approach
int main() {
    printf("Interrupt-Driven I/O Example\n");
    printf("Press any key (this simulates interrupt handling)\n");
    
    // In actual implementation:
    // 1. Register ISR: signal(SIGINT, keyboard_isr)
    // 2. Enable interrupts: asm volatile ("sti")
    // 3. CPU can do other work while waiting
    
    // Simulated main work - CPU can do other tasks
    for (int i = 0; i < 10; i++) {
        printf("Main program doing useful work... iteration %d\n", i);
        
        // In real system, CPU would NOT check keyboard here
        // It would be interrupted when key is pressed
        
        // Simulated delay
        // sleep(1);
    }
    
    // When interrupt occurs, ISR runs automatically
    // Then control returns here
    
    if (key_pressed) {
        printf("Interrupt occurred! Key code: 0x%02X\n", key_code);
    }
    
    return 0;
}

/*
 * FLOW IN ACTUAL INTERRUPT-DRIVEN I/O:
 * 
 * 1. User presses key → Keyboard hardware generates IRQ1
 * 2. CPU finishes current instruction → Checks interrupt flag
 * 3. CPU saves context → Pushes flags, CS, IP to stack
 * 4. CPU looks up interrupt vector → Gets address of keyboard ISR
 * 5. CPU executes ISR → Reads key from keyboard port
 * 6. ISR acknowledges interrupt → Sends EOI to PIC
 * 7. CPU restores context → Returns to main program
 * 8. Main program continues → Never had to poll!
 */
```

### 4.6 Advantages of Interrupt-Driven I/O

- **CPU efficiency**: CPU can perform useful work while waiting
- **Better responsiveness**: Immediate attention to devices
- **Scalable**: Can handle many devices simultaneously
- **Suitable for slow devices**: No wasted CPU cycles

### 4.7 Disadvantages of Interrupt-Driven I/O

- **Complex implementation**: Requires interrupt handling code
- **Overhead**: Context saving/restoring takes time
- **Race conditions**: May require synchronization
- **Priority inversion**: High-priority tasks may wait

---

## 5. Direct Memory Access (DMA)

### 5.1 Concept and Working

**Direct Memory Access (DMA)** is a method that allows I/O devices to transfer data directly to/from system memory without CPU intervention. A special hardware component called a **DMA Controller** manages these transfers.

### 5.2 How DMA Works

1. **CPU programs DMA controller**: Sets source, destination, transfer length
2. **CPU continues other work**: No longer involved in data transfer
3. **DMA controller manages transfer**: Reads from device, writes to memory
4. **Device sends request**: DRQ (DMA Request) signal
5. **DMA controller arbitrates**: Gets control of bus
6. **Transfer occurs**: Data goes directly device ↔ memory
7. **Completion interrupt**: DMA controller notifies CPU when done

### 5.3 DMA Controller Architecture

```
DMA Controller (8237A style):
├── Channel 0: System DRAM refresh
├── Channel 1: Reserved (often used for sound)
├── Channel 2: Floppy Disk
├── Channel 3: Reserved
├── Channel 4: Cascade (master/slave)
├── Channel 5: Hard Disk
├── Channel 6: Reserved
└── Channel 7: Reserved
```

### 5.4 DMA Transfer Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| **Single Transfer** | One byte/word per request | Slow devices |
| **Block Transfer** | Multiple bytes in one go | Disk I/O |
| **Demand Transfer** | Continuous while device requests | High-speed devices |
| **Cascade Mode** | Chains to another DMA controller | Expansion |

### 5.5 Example: DMA Transfer for Hard Disk Read

```c
// DMA Example: Pseudo-code for disk read operation
// This demonstrates how DMA eliminates CPU involvement

#include <stdio.h>

// DMA Controller Registers (ISA bus example)
#define DMA_BASE        0x00
#define DMA_COMMAND     (DMA_BASE + 0x08)
#define DMA_MASK        (DMA_BASE + 0x0A)
#define DMA_MODE        (DMA_BASE + 0x0B)
#define DMA_CLEAR_FF    (DMA_BASE + 0x0C)
#define DMA_START       (DMA_BASE + 0x04)  // Channel 2

// Physical memory addresses (for real DMA)
typedef unsigned int phys_addr_t;

// DMA Transfer Structure
typedef struct {
    unsigned char channel;        // DMA channel (0-7)
    phys_addr_t buffer_physical;  // Physical address of buffer
    unsigned int transfer_count;  // Number of bytes
    unsigned char transfer_mode;  // Read/Write mode
} dma_transfer_t;

// DMA Mode bits
#define DMA_MODE_READ   0x44  // Device to memory
#define DMA_MODE_WRITE  0x48  // Memory to device
#define DMA_MODE_SINGLE 0x40  // Single transfer mode

void outportb(unsigned short port, unsigned char value);
unsigned char inportb(unsigned short port);

int setup_dma_transfer(dma_transfer_t *dma) {
    // Step 1: Disable the DMA channel
    outportb(DMA_MASK, (dma->channel & 0x03) | 0x04);
    
    // Step 2: Clear byte flip-flop (sets low byte first)
    outportb(DMA_CLEAR_FF, 0xFF);
    
    // Step 3: Set transfer mode (read from device, single mode)
    outportb(DMA_MODE, DMA_MODE_READ | dma->channel);
    
    // Step 4: Set the physical address (low 16 bits)
    outportb(DMA_START, dma->buffer_physical & 0xFF);
    outportb(DMA_START, (dma->buffer_physical >> 8) & 0xFF);
    
    // Step 5: Set transfer count (number of bytes - 1)
    outportb(DMA_START + 2, dma->transfer_count & 0xFF);
    outportb(DMA_START + 2, (dma->transfer_count >> 8) & 0xFF);
    
    // Step 6: Enable the DMA channel
    outportb(DMA_MASK, dma->channel & 0x03);
    
    return 0;
}

int main() {
    // Example: Read 1024 bytes from disk using DMA
    char buffer[1024];  // Must be aligned for DMA!
    
    dma_transfer_t dma = {
        .channel = 2,           // Floppy disk channel
        .buffer_physical = 0x00100000,  // Physical address
        .transfer_count = 1023, // Bytes - 1
        .transfer_mode = DMA_MODE_READ
    };
    
    printf("Setting up DMA transfer...\n");
    setup_dma_transfer(&dma);
    
    printf("DMA configured. CPU can now do other work!\n");
    printf("Transfer will complete with interrupt when done.\n");
    
    // CPU is FREE to do other tasks while DMA transfers data!
    for (int i = 0; i < 5; i++) {
        printf("CPU performing useful computation: %d\n", i);
    }
    
    // In real system, wait for DMA completion interrupt
    printf("Waiting for DMA completion...\n");
    
    return 0;
}

/*
 * DMA ADVANTAGE DEMONSTRATION:
 * 
 * WITHOUT DMA (Programmed I/O):
 *   for (i = 0; i < 1024; i++)
 *       buffer[i] = read_from_disk();  // CPU busy the whole time
 * 
 * WITH DMA:
 *   setup_dma_transfer(&dma);
 *   // CPU can do OTHER WORK here
 *   do_other_tasks();
 *   // DMA completion interrupt wakes us up
 * 
 * RESULT: CPU utilization dramatically improved!
 */
```

### 5.6 Bus Arbitration

DMA controllers must request control of the system bus:

```
Bus Arbitration Priority (from highest to lowest):
1. CPU (when needs bus)
2. Refresh (memory refresh)
3. DMA (high priority)
4. DMA (low priority)
5. Other devices
```

### 5.7 Advantages of DMA

- **CPU liberation**: CPU can perform other computations
- **High throughput**: Efficient for bulk data transfers
- **Lower CPU overhead**: Dramatically reduces CPU involvement
- **Better system performance**: Enables concurrent operations

### 5.8 Disadvantages of DMA

- **Complex hardware**: Requires DMA controller
- **Memory constraints**: Buffers must be physically contiguous
- **Cache coherency**: Must invalidate/invalidate cache
- **Limited channels**: Few DMA channels available
- **Cost**: Additional hardware complexity

---

## 6. Comparative Analysis

### 6.1 Comparison Table

| Aspect | Programmed I/O | Interrupt-Driven I/O | DMA |
|--------|---------------|---------------------|-----|
| **CPU Involvement** | Constant | Minimal (only ISR) | None during transfer |
| **Speed** | Slow for slow devices | Good | Excellent for bulk |
| **Complexity** | Simple | Moderate | Complex |
| **Hardware** | Basic | Interrupt controller | DMA controller |
| **Suitable For** | Fast devices | Variable rate | Bulk transfers |
| **Efficiency** | Poor | Good | Excellent |
| **Latency** | Polling interval | Interrupt overhead | Setup + transfer |
| **Power Consumption** | High | Moderate | Low |

### 6.2 When to Use Each Method

```
DECISION TREE:

Is the device fast (keyboard, mouse)?
├── YES → Interrupt-Driven I/O
└── NO → Is data transfer bulk (disk, network)?
    ├── YES → Is DMA available?
    │   ├── YES → Use DMA
    │   └── NO → Interrupt-Driven
    └── NO → Programmed I/O (if simple) or Interrupt-Driven
```

---

## 7. Multiple Choice Questions

### Easy Level

1. **In Programmed I/O, the CPU:**
   - a) Waits in a loop for device readiness
   - b) Immediately handles the device
   - c) Uses DMA for transfer
   - d) Ignores the device until interrupted
   
   **Answer: a)**

2. **Which I/O method requires the most CPU intervention?**
   - a) Interrupt-Driven I/O
   - b) DMA
   - c) Programmed I/O
   - d) Memory-Mapped I/O
   
   **Answer: c)**

3. **DMA stands for:**
   - a) Direct Memory Access
   - b) Data Memory Allocation
   - c) Digital Media Adapter
   - d) Dynamic Memory Access
   
   **Answer: a)**

### Medium Level

4. **An Interrupt Service Routine (ISR) is:**
   - a) A program that runs when the CPU starts
   - b) A function called when an interrupt occurs
   - c) A type of device driver
   - d) A memory management routine
   
   **Answer: b)**

5. **The main advantage of Interrupt-Driven I/O over Programmed I/O is:**
   - a) Simpler programming
   - b) CPU doesn't waste cycles polling
   - c) Faster data transfer
   - d) Works with all devices
   
   **Answer: b)**

6. **In a DMA transfer, who controls the system bus?**
   - a) CPU
   - b) Device Controller
   - c) DMA Controller
   - d) Operating System
   
   **Answer: c)**

### Hard Level

7. **A DMA controller typically uses how many channels on a standard PC?**
   - a) 4
   - b) 8
   - c) 16
   - d) 32
   
   **Answer: b)** (8 channels in 8237A controller)

8. **Cache coherency issues in DMA occur because:**
   - a) DMA uses virtual addresses
   - b) CPU cache may hold stale data while DMA writes to memory
   - c) DMA controllers have cache
   - d) The OS manages cache incorrectly
   
   **Answer: b)**

### Scenario-Based Questions

9. **Scenario: A real-time system needs to capture data from a high-speed sensor at 10,000 samples per second. Which I/O method is most suitable?**
   - a) Programmed I/O - Simple to implement
   - b) Interrupt-Driven I/O - But may miss samples
   - c) DMA - Can handle high-speed continuous transfer
   - d) Memory-Mapped I/O - Fastest access
   
   **Answer: c)** - DMA is ideal for high-speed, continuous data transfer where missing samples is unacceptable.

10. **Scenario: You are designing an embedded system with limited hardware (no DMA controller). The system has a slow temperature sensor that reports every 5 seconds. Which I/O method would you choose?**
    - a) DMA - Not available
    - b) Interrupt-Driven I/O - CPU can do other work between interrupts
    - c) Programmed I/O - Wasteful but simple
    - d) Memory-Mapped I/O - Not relevant to choice
    
    **Answer: b)** - Interrupt-Driven I/O is appropriate: the sensor is slow, but we don't want to waste CPU cycles polling when it can do other useful work.

---

## 8. Flashcards

### Flashcard 1
**Term:** Programmed I/O (Polling)

**Definition:** An I/O method where the CPU continuously checks the status of devices by reading their status registers in a loop until they indicate readiness for data transfer.

**Key Point:** CPU is busy-waiting, inefficient for slow devices.

---

### Flashcard 2
**Term:** Interrupt-Driven I/O

**Definition:** An I/O method where devices notify the CPU by sending an interrupt signal when they need attention, allowing the CPU to execute an Interrupt Service Routine (ISR).

**Key Point:** CPU efficiency improved; can perform other tasks while waiting.

---

### Flashcard 3
**Term:** Direct Memory Access (DMA)

**Definition:** A method allowing I/O devices to transfer data directly to/from memory without CPU intervention, managed by a DMA controller.

**Key Point:** CPU is completely freed for other computations during bulk transfers.

---

### Flashcard 4
**Term:** Interrupt Service Routine (ISR)

**Definition:** A special function executed in response to a hardware interrupt, responsible for handling the interrupt and performing necessary device operations.

**Key Point:** Must be short and efficient; saves/restores CPU state.

---

### Flashcard 5
**Term:** DMA Controller

**Definition:** Specialized hardware (e.g., 8237A) that manages direct data transfers between I/O devices and memory, handling bus arbitration and transfer timing.

**Key Point:** Contains multiple channels, each assigned to a specific device.

---

### Flashcard 6
**Term:** Bus Arbitration

**Definition:** The process by which the DMA controller gains control of the system bus from the CPU to perform memory transfers.

**Key Point:** DMA must request bus access; CPU has priority but can be released.

---

### Flashcard 7
**Term:** Interrupt Vector Table

**Definition:** A data structure that maps interrupt request numbers to the addresses of corresponding Interrupt Service Routines.

**Key Point:** CPU uses this to determine which ISR to execute when an interrupt occurs.

---

### Flashcard 8
**Term:** End of Interrupt (EOI)

**Definition:** A signal sent to the Programmable Interrupt Controller (PIC) to acknowledge that the interrupt handler has finished processing.

**Key Point:** Required to allow subsequent interrupts to be processed.

---

## 9. Key Takeaways

### Summary of I/O Methods

1. **Programmed I/O (Polling)**
   - CPU actively monitors device status in a loop
   - Simple but inefficient - CPU wastes cycles
   - Suitable only for very fast devices or simple systems
   - Example: Reading keyboard in early computer systems

2. **Interrupt-Driven I/O**
   - Device notifies CPU via interrupt when ready
   - CPU can perform other tasks while waiting
   - Requires interrupt controller and ISR implementation
   - Standard approach for most modern I/O operations

3. **Direct Memory Access (DMA)**
   - Data transfers directly between device and memory
   - CPU completely freed during transfer
   - Requires DMA controller hardware
   - Essential for high-performance storage and network operations

### Delhi University Syllabus Context

This content aligns with the **Ge2C Computer System Architecture** paper under NEP 2024, covering:
- I/O interface concepts
- Programmed, Interrupt, and DMA transfer modes
- Comparative analysis of I/O methods
- Practical implementation considerations

### Important Concepts to Remember

- **CPU involvement decreases**: Programmed → Interrupt → DMA
- **Efficiency increases**: With each method
- **Hardware complexity increases**: With each method
- **Real-world systems combine**: All three methods depending on device needs

### Exam Tips

- Understand when to use each I/O method
- Know the advantages and disadvantages of each
- Be able to trace through operation sequences
- Remember the components involved in each method
- Practice comparing methods using the comparison table

---

## References

1. Computer Organization and Architecture by William Stallings
2. Computer System Architecture by M. Morris Mano
3. Delhi University NEP 2024 Syllabus - Ge2C Computer System Architecture
4. Intel 8237A DMA Controller Documentation
5. x86 Interrupt Architecture Documentation

---

*This study material is designed for BSc Physical Science (CS) students at Delhi University under NEP 2024. Total coverage: ~2000 words.*