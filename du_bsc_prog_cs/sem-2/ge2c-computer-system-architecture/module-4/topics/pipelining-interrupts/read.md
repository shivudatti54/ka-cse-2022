# Pipelining Interrupts: Comprehensive Study Material

## Subject: Ge2C Computer System Architecture
### BSc Physical Science (CS) — Delhi University, NEP 2024

---

## Table of Contents
1. [Introduction to Pipelining and Interrupts](#introduction)
2. [Pipelining Fundamentals](#pipelining-fundamentals)
3. [Pipeline Hazards](#pipeline-hazards)
4. [Interrupt Handling Mechanisms](#interrupt-handling-mechanisms)
5. [Types of Interrupts](#types-of-interrupts)
6. [Interrupt Handling in Pipelined Processors](#interrupt-handling-in-pipelined-processors)
7. [Direct Memory Access (DMA)](#direct-memory-access-dma)
8. [Concrete Examples](#concrete-examples)
9. [Key Takeaways](#key-takeaways)
10. [Practice Questions (MCQs)](#practice-questions-mcqs)
11. [Flashcards](#flashcards)

---

## 1. Introduction to Pipelining and Interrupts {#introduction}

### What is Pipelining?

**Pipelining** is a fundamental technique in computer architecture that improves instruction throughput by overlapping the execution of multiple instructions. Just like an assembly line in a factory where different stages work on different products simultaneously, a processor pipeline allows multiple instructions to be in various stages of execution at the same time.

### Real-World Relevance

Consider a **laundry washing machine** with three stages: wash, dry, and fold. Without pipelining, you would complete one load entirely before starting the next. With pipelining, while the first load is drying, you can wash the second load—dramatically improving throughput.

In modern computing, pipelining is essential for:
- **Smartphone processors** (Qualcomm Snapdragon, Apple A-series) - enabling efficient multitasking
- **Desktop CPUs** (Intel Core, AMD Ryzen) - achieving high clock speeds
- **Embedded systems** - maximizing performance within power constraints

### What are Interrupts?

An **interrupt** is a signal to the CPU indicating an event that requires immediate attention. When an interrupt occurs, the CPU suspends its current execution, saves its state, and executes an **Interrupt Service Routine (ISR)** to handle the event.

### Why This Topic Matters for Delhi University Students

This topic aligns with the **Ge2C Computer System Architecture** syllabus under NEP 2024, covering the intersection of two critical concepts: processor optimization (pipelining) and I/O handling (interrupts). Understanding how these mechanisms work together is essential for system programming and embedded development.

---

## 2. Pipelining Fundamentals {#pipelining-fundamentals}

### Basic Pipeline Stages

A classic RISC pipeline consists of five stages:

| Stage | Name | Function |
|-------|------|----------|
| IF | Instruction Fetch | Fetch instruction from memory |
| ID | Instruction Decode | Decode instruction, read registers |
| EX | Execute | Perform arithmetic/logical operations |
| MEM | Memory Access | Read/write data to memory |
| WB | Write Back | Write result back to register file |

### How Pipeline Works

```
Time →    T1    T2    T3    T4    T5    T6    T7
Inst 1:   IF    ID    EX    MEM   WB
Inst 2:        IF    ID    EX    MEM   WB
Inst 3:             IF    ID    EX    MEM   WB
Inst 4:                  IF    ID    EX    MEM   WB
```

Without pipeline: 5 cycles per instruction × 4 instructions = 20 cycles
With pipeline: 5 cycles (startup) + 4 × 1 = 9 cycles (81% improvement)

### Pipeline Performance Metrics

- **Speedup**: Ratio of non-pipelined to pipelined execution time
- **Throughput**: Number of instructions completed per unit time
- **Latency**: Time to complete a single instruction

---

## 3. Pipeline Hazards {#pipeline-hazards}

Pipeline hazards are situations where the next instruction cannot execute in the intended clock cycle. There are three main types:

### 3.1 Structural Hazards

**Definition**: Occur when hardware cannot support all combinations of instructions in the pipeline simultaneously.

**Example**: Single memory for both instructions and data (von Neumann bottleneck)

```
Without Structural Hazard Mitigation:
Clock:    1    2    3    4    5
Inst A:   IF   ID   EX   MEM  WB
Inst B:   -    IF   ID   EX   MEM  WB  ← Structural hazard (memory conflict)

With Dual-Port Memory:
Clock:    1    2    3    4    5
Inst A:   IF   ID   EX   MEM  WB
Inst B:   IF   ID   EX   MEM   WB  ← No conflict
```

**Solution**: Duplicate hardware resources (e.g., separate instruction and data caches)

### 3.2 Data Hazards

**Definition**: Occur when instructions depend on the results of previous instructions still in the pipeline.

#### Types of Data Hazards:

1. **Read After Write (RAW)** - True Dependency
   ```
   ADD R1, R2, R3    ; R1 = R2 + R3
   SUB R4, R1, R5    ; R4 = R1 - R5 (depends on R1)
   ```

2. **Write After Read (WAR)** - Anti-dependency
   ```
   ADD R1, R2, R3    ; R1 = R2 + R3
   SUB R2, R4, R5    ; R2 = R4 - R5 (overwrites R2 before it's read)
   ```

3. **Write After Write (WAW)** - Output dependency
   ```
   ADD R1, R2, R3    ; R1 = R2 + R3
   SUB R1, R4, R5    ; R1 = R4 - R5 (result order matters)
   ```

**Solutions**:
- **Data Forwarding**: Pass results directly from EX/MEM stages to next instruction
- **Pipeline Stalling**: Insert bubble (NOP) cycles
- **Register Renaming**: Eliminate false dependencies

#### Code Example: Data Hazard Resolution

```mips
# MIPS Assembly demonstrating data forwarding

# Without forwarding (stalls):
    add $t0, $t1, $t2    # Cycle 1-5: Execute
    sub $t3, $t0, $t4    # Would need stall until $t0 is written back

# With forwarding (no stalls):
    add $t0, $t1, $t2    # Cycle 1-5
    sub $t3, $t0, $t4    # Cycle 3: Forward $t0 from EX/MEM of add
                          # to ID of sub
```

### 3.3 Control Hazards

**Definition**: Occur due to branch instructions that alter the program counter.

**Example**:
```
    beq $t0, $t1, label  # Branch to label if $t0 == $t1
    add $t2, $t3, $t4    # This instruction might be fetched incorrectly
```

**Solutions**:

1. **Branch Delay Slots**: Execute instruction after branch regardless of outcome
   ```mips
       beq $t0, $t1, loop
       add $t2, $t3, $t4    # This ALWAYS executes (delay slot)
   loop:
       sub $t5, $t6, $t7
   ```

2. **Branch Prediction**: 
   - Static: Always predict taken/not taken
   - Dynamic: Use history (2-bit saturating counter)

3. **Flush Pipeline**: Clear wrong-path instructions on misprediction

---

## 4. Interrupt Handling Mechanisms {#interrupt-handling-mechanisms}

### 4.1 Interrupt Processing Steps

When an interrupt occurs, the CPU follows this sequence:

```
1. Interrupt Request (IRQ) received
2. CPU completes current instruction
3. Save processor state (PC, status register, etc.)
4. Identify interrupt source (interrupt vector)
5. Jump to Interrupt Service Routine (ISR)
6. Handle the interrupt event
7. Restore processor state
8. Resume normal execution
```

### 4.2 Interrupt Vector Table

An **interrupt vector table** is a data structure that maps interrupt requests to their corresponding ISR addresses.

**Example: 8086 Interrupt Vector Table**

```c
// Interrupt Vector Table structure (8086)
// Each vector is 4 bytes (2 bytes offset, 2 bytes segment)

#define NUM_INTERRUPTS 256

// Interrupt Vector Table entry
struct IVTEntry {
    uint16_t offset;      // IP offset
    uint16_t segment;     // CS segment
};

// The IVT is located at linear address 0x00000
extern struct IVTEntry _interrupt_vector_table[NUM_INTERRUPTS];

// Example: Timer interrupt (IRQ0) - vector number 0x20
void timer_isr(void);
void setup_timer_interrupt(void) {
    // Install ISR at timer interrupt vector
    _interrupt_vector_table[0x20].offset = (uint16_t)timer_isr;
    _interrupt_vector_table[0x20].segment = 0x0000;  // Code segment
}
```

### 4.3 Polling vs. Vectored Interrupts

| Method | Description | Advantages | Disadvantages |
|--------|-------------|------------|---------------|
| **Polling** | CPU checks each device sequentially | Simple, low hardware cost | Slow, wastes CPU cycles |
| **Vectored** | Device provides vector number | Fast, efficient | More hardware complexity |

---

## 5. Types of Interrupts {#types-of-interrupts}

### 5.1 Maskable vs. Non-Maskable Interrupts (NMI)

| Type | Description | Can be Delayed? | Examples |
|------|-------------|-----------------|----------|
| **Maskable (IRQ)** | Can be enabled/disabled by CPU | Yes | Keyboard, mouse, disk I/O |
| **Non-Maskable (NMI)** | Cannot be ignored by CPU | No | Power failure, hardware fault, memory parity error |

```c
// Example: ARM Cortex-M interrupt control

// Enable maskable interrupts
__enable_irq();    // Set PRIMASK, allow IRQ

// Disable maskable interrupts  
__disable_irq();   // Clear PRIMASK, block IRQ

// Example: NMI handler in ARM Cortex-M
void NMI_Handler(void) {
    // NMI cannot be masked - handle critical error
    // Possible causes: clock failure, voltage drop
    while(1) {
        // Flash error LED or log to backup memory
    }
}
```

### 5.2 Hardware vs. Software Interrupts

- **Hardware Interrupts**: Generated by external devices (keyboard, timer, disk)
- **Software Interrupts**: Generated by programs using `INT` instruction (system calls)

```mips
# MIPS software interrupt (system call)
    li $v0, 1      # syscall number 1 = print integer
    li $a0, 42     # argument = 42
    syscall        # triggers software interrupt
```

### 5.3 Vectored Interrupts

In vectored interrupts, the interrupting device provides an identifier that the CPU uses to directly locate the appropriate ISR.

**Example: PIC (Programmable Interrupt Controller) 8259A**

```
External Device → PIC → CPU (with vector)
                          ↓
              Interrupt Vector Table
                          ↓
                    ISR Address
```

---

## 6. Interrupt Handling in Pipelined Processors {#interrupt-handling-in-pipelined-processors}

Handling interrupts in a pipelined processor is complex because multiple instructions are in various stages of execution simultaneously.

### 6.1 Challenges

1. **Precise Interrupts**: All instructions before the interrupt point must complete; all after must not execute
2. **State Preservation**: Must save/restore pipeline state
3. **Restartability**: Must be able to resume execution after ISR

### 6.2 Pipeline Flush on Interrupt

When an interrupt occurs:
1. Complete all instructions before the interrupting instruction
2. Discard all instructions after the interrupting instruction
3. Save PC of the interrupted instruction
4. Branch to ISR

```
Normal:    IF  ID  EX  MEM  WB
Interrupt at EX stage:
           IF  ID  EX  --FLUSH--  ISR
                    ↑
           Instructions after EX are discarded
```

### 6.3 Handling Interrupts with In-Flight Instructions

```c
// Pseudo-code for precise interrupt handling in pipeline

void handle_interrupt(uint32_t interrupt_id) {
    // 1. Complete current instruction in EX stage
    complete_current_instruction();
    
    // 2. Squash all instructions in IF, ID stages
    squash_pipeline();
    
    // 3. Save PC (point to interrupted instruction)
    uint32_t saved_pc = get_current_pc();
    save_to_stack(saved_pc);
    save_csr_to_stack();  // Control/Status Registers
    
    // 4. Load ISR address from vector table
    void (*isr_addr)() = interrupt_vector_table[interrupt_id];
    
    // 5. Jump to ISR
    jump_to_isr(isr_addr);
}
```

---

## 7. Direct Memory Access (DMA) {#direct-memory-access-dma}

### What is DMA?

**Direct Memory Access (DMA)** is a method where data is transferred directly between I/O devices and memory without CPU intervention, significantly improving system performance.

### How DMA Works

```
Without DMA:
CPU → Read from disk → CPU → Write to memory → CPU

With DMA:
CPU → Setup DMA transfer → DMA Controller → Direct memory transfer
                    CPU can do other work simultaneously
```

### DMA Transfer Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| **Single Transfer** | One data word per request | Low-bandwidth devices |
| **Block Transfer** | Multiple words in one sequence | Disk, tape drives |
| **Demand Transfer** | Device requests transfer when ready | High-speed devices |
| **Cascade Mode** | DMA controller acts as proxy | Chaining controllers |

### DMA and Interrupts

DMA controllers typically generate interrupts to notify the CPU when:
- Transfer is complete
- Error occurs
- Buffer threshold reached

```c
// Example: DMA transfer with interrupt handling

// DMA configuration structure
typedef struct {
    volatile uint32_t SRC_ADDR;    // Source address
    volatile uint32_t DEST_ADDR;   // Destination address
    volatile uint32_t TRANSFER_COUNT;
    volatile uint32_t CONTROL;     // Control register
} DMA_Channel_t;

#define DMA_CHANNEL_0 ((DMA_Channel_t *)0x40026000)

// DMA transfer complete ISR
void DMA0_IRQHandler(void) {
    // Clear transfer complete flag
    DMA_CHANNEL_0->CONTROL |= (1 << 3);  // Clear TC flag
    
    // Notify application
    transfer_complete = true;
    
    // Optional: Trigger another software interrupt
    NVIC_SetPendingIRQ(APP_TASK_IRQ);
}

// Setup DMA transfer
void setup_dma_transfer(uint32_t *src, uint32_t *dest, uint32_t count) {
    DMA_CHANNEL_0->SRC_ADDR = (uint32_t)src;
    DMA_CHANNEL_0->DEST_ADDR = (uint32_t)dest;
    DMA_CHANNEL_0->TRANSFER_COUNT = count;
    DMA_CHANNEL_0->CONTROL = (1 << 0)   // Enable DMA
                           | (1 << 1)   // Source increment
                           | (1 << 2)   // Dest increment
                           | (1 << 4)   // Interrupt on complete
                           | (0x3 << 8); // 32-bit transfer size
    
    transfer_complete = false;
}
```

---

## 8. Concrete Examples {#concrete-examples}

### Example 1: MIPS Pipeline with Data Hazard and Forwarding

```mips
# MIPS Pipeline Simulation with Data Forwarding
# File: pipeline_example.asm

# Initialize registers
    ori $t0, $zero, 10      # $t0 = 10
    ori $t1, $zero, 20      # $t1 = 20

# Instruction sequence with RAW hazard
    add $t2, $t0, $t1       # $t2 = 10 + 20 = 30  (EX stage)
    sub $t3, $t2, $t1       # $t3 = 30 - 20 = 10  (needs $t2 from add)
    and $t4, $t2, $t0       # $t4 = 30 & 10 = 10  (needs $t2 from add)
    or  $t5, $t3, $t1       # $t5 = 10 | 20 = 30  (needs $t3 from sub)

# Pipeline Timeline WITH Forwarding:
# Cycle:  1    2    3    4    5    6    7    8
# add:    IF   ID   EX   MEM  WB
# sub:         IF   ID   EX*  MEM  WB    *Forwards $t2 from add's MEM
# and:              IF   ID*  EX   MEM  WB  *Forwards $t2 from add's WB
# or:                   IF   ID   EX   MEM  WB

# Pipeline Timeline WITHOUT Forwarding:
# Cycle:  1    2    3    4    5    6    7    8    9   10
# add:    IF   ID   EX   MEM  WB
# sub:         IF   ID   EX   MEM  WB    # Stalled for 1 cycle
# and:              IF   ID   NOP  NOP   EX   MEM  WB  # Stalled for 2 cycles
# or:                        IF   ID   EX   MEM  WB
```

### Example 2: Interrupt-Driven I/O in Embedded Systems

```c
/*
 * Example: UART interrupt-driven communication
 * Demonstrates interrupt handling in embedded system
 */

#include <stdint.h>

// UART Registers (example addresses)
#define UART_DATA_REG     (*(volatile uint32_t *)0x4000C000)
#define UART_STATUS_REG   (*(volatile uint32_t *)0x4000C004)
#define UART_CONTROL_REG  (*(volatile uint32_t *)0x4000C008)
#define UART_BAUD_REG     (*(volatile uint32_t *)0x4000C00C)

// Status register bits
#define UART_RX_READY     (1 << 0)
#define UART_TX_EMPTY     (1 << 1)

// Ring buffer for received data
#define BUFFER_SIZE 256
volatile uint8_t rx_buffer[BUFFER_SIZE];
volatile uint32_t rx_head = 0;
volatile uint32_t rx_tail = 0;

// Interrupt Service Routine for UART RX
void UART0_IRQHandler(void) {
    // Check if receive data interrupt
    if (UART_STATUS_REG & UART_RX_READY) {
        // Read data from UART
        uint8_t data = (uint8_t)UART_DATA_REG;
        
        // Add to ring buffer
        uint32_t next_head = (rx_head + 1) % BUFFER_SIZE;
        
        if (next_head != rx_tail) {
            rx_buffer[rx_head] = data;
            rx_head = next_head;
        } else {
            // Buffer overflow - discard data
            // In real system, set overflow flag
        }
    }
    
    // Check if transmit interrupt
    if (UART_STATUS_REG & UART_TX_EMPTY) {
        // More data to transmit
        if (tx_head != tx_tail) {
            UART_DATA_REG = tx_buffer[tx_tail];
            tx_tail = (tx_tail + 1) % BUFFER_SIZE;
        } else {
            // Disable TX interrupt when done
            UART_CONTROL_REG &= ~(1 << 1);
        }
    }
}

// Initialize UART with interrupts
void uart_init(void) {
    // Set baud rate (assuming 16MHz clock)
    UART_BAUD_REG = 16000000 / (16 * 115200);
    
    // Enable RX interrupt, disable TX interrupt initially
    UART_CONTROL_REG = (1 << 0)   // RX interrupt enable
                     | (0 << 1);  // TX interrupt disable
    
    // Enable UART interrupt in NVIC
    // (architecture-specific, simplified)
    *((volatile uint32_t *)0xE000E100) = (1 << 6);  // Enable IRQ6
}

// Main function demonstrating interrupt-driven I/O
int main(void) {
    uart_init();
    
    while (1) {
        // Process received data in main loop
        if (rx_head != rx_tail) {
            uint8_t data = rx_buffer[rx_tail];
            rx_tail = (rx_tail + 1) % BUFFER_SIZE;
            
            // Echo back (using interrupt-driven TX)
            uart_send_byte(data);
        }
        
        // Do other work while I/O is interrupt-driven
        // CPU is free to perform other tasks
    }
    
    return 0;
}
```

---

## 9. Key Takeaways {#key-takeaways}

### Pipelining Fundamentals
- **Pipelining** improves throughput by overlapping instruction execution across multiple stages
- A classic 5-stage pipeline (IF, ID, EX, MEM, WB) can significantly speed up program execution
- Pipeline depth and clock frequency are key performance factors

### Pipeline Hazards
1. **Structural Hazards**: Hardware limitations causing conflicts → Solved by duplicating resources
2. **Data Hazards**: Instruction dependencies (RAW, WAR, WAW) → Solved by forwarding, stalling, renaming
3. **Control Hazards**: Branch mispredictions → Solved by delay slots, prediction, flushing

### Interrupt Handling
- **Interrupts** allow external devices to gain CPU attention asynchronously
- **Maskable interrupts (IRQ)** can be enabled/disabled; **NMIs** cannot be delayed
- **Interrupt Vector Table** maps interrupt sources to ISR addresses
- **Precise interrupts** ensure all previous instructions complete before ISR execution

### DMA
- **Direct Memory Access** enables high-speed data transfer without CPU involvement
- DMA controllers generate interrupts to signal transfer completion
- Critical for disk I/O, audio/video streaming, and data acquisition

### Delhi University NEP 2024 Context
This topic connects:
- Processor architecture (pipelining)
- I/O handling (interrupts)
- System optimization (hazards, DMA)
- Embedded systems programming

---

## 10. Practice Questions (MCQs) {#practice-questions-mcqs}

### Multiple Choice Questions

**Q1. In a 5-stage MIPS pipeline, how many cycles are needed to execute 100 instructions?**

A) 100  
B) 104  
C) 500  
D) 95  

**Answer: B (104 = 5 cycles for first instruction + 99 × 1 cycle for rest)**

---

**Q2. Which type of hazard is resolved by data forwarding?**

A) Structural hazard  
B) Control hazard  
C) Data hazard (RAW)  
D) All of the above  

**Answer: C**

---

**Q3. A non-maskable interrupt (NMI) can be:**

A) Delayed by the CPU  
B) Enabled/disabled by software  
C) Generated by external hardware only  
D) None of the above  

**Answer: C**

---

**Q4. In a pipelined processor, when an interrupt occurs at the EX stage, what happens to instructions in IF and ID stages?**

A) They complete normally  
B) They are squashed (flushed)  
C) They are paused  
D) They are forwarded to next cycle  

**Answer: B**

---

**Q5. DMA stands for:**

A) Direct Memory Access  
B) Data Memory Access  
C) Dual Memory Architecture  
D) Dynamic Memory Allocation  

**Answer: A**

---

**Q6. Which interrupt handling mechanism provides faster response?**

A) Polling  
B) Vectored interrupts  
C) Software interrupts  
D) All equally fast  

**Answer: B**

---

**Q7. The Read-After-Write (RAW) hazard is also known as:**

A) Anti-dependency  
B) Output dependency  
C) True dependency  
D) False dependency  

**Answer: C**

---

**Q8. What is the purpose of a branch delay slot?**

A) To speed up branch execution  
B) To execute an instruction regardless of branch outcome  
C) To reduce power consumption  
D) To handle exceptions  

**Answer: B**

---

## 11. Flashcards {#flashcards}

### Flashcard Set

| Term | Definition |
|------|-------------|
| **Pipeline** | Instruction execution overlap technique with multiple stages |
| **Structural Hazard** | Hardware cannot support instruction combination |
| **RAW Hazard** | Read After Write - true data dependency |
| **Control Hazard** | Caused by branch/jump instructions |
| **Interrupt** | Signal requiring CPU attention from external/internal source |
| **NMI** | Non-Maskable Interrupt - cannot be ignored or delayed |
| **ISR** | Interrupt Service Routine - code handling the interrupt |
| **Vectored Interrupt** | Interrupt where device provides vector number to find ISR |
| **DMA** | Direct Memory Access - data transfer without CPU intervention |
| **Pipeline Flush** | Discarding in-flight instructions on exception/interrupt |
| **Forwarding** | Passing results directly from one pipeline stage to another |
| **Precise Interrupt** | Interrupt where all previous instructions complete, later ones don't |

---

## References and Further Reading

1. **Computer Organization and Design** - David A. Patterson, John L. Hennessy
2. **Computer Architecture: A Quantitative Approach** - John L. Hennessy, David A. Patterson
3. **Microprocessors and Microcontrollers** - N. Senthil Kumar
4. **Delhi University NEP 2024 - Ge2C Syllabus**
5. **MIPS Architecture Documentation**
6. **ARM Cortex-M Programming Guide**

---

*Document prepared for BSc Physical Science (CS), Delhi University, NEP 2024*