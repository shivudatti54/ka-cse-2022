# Bus Organization and Control Unit
## Ge2C Computer System Architecture - Delhi University NEP 2024

---

## 1. Introduction

In modern computer systems, the **bus** serves as the communication backbone that connects various hardware components including the CPU, memory, and input/output devices. The **Control Unit (CU)** orchestrates the flow of data and control signals across these buses, ensuring synchronized operation of all system components.

This topic is fundamental to understanding how computers execute instructions and manage data flow. For Delhi University students preparing for Ge2C Computer System Architecture under NEP 2024, mastering bus organization and control unit design is essential for comprehending microprocessor architecture, system integration, and performance optimization.

**Real-World Relevance:** When you use a smartphone, laptop, or desktop computer, the bus architecture determines how quickly data transfers between the processor and memory, affecting everything from application loading times to gaming performance. Understanding these concepts is crucial for system programmers, hardware engineers, and IT professionals.

---

## 2. Bus Organization

### 2.1 What is a Computer Bus?

A **bus** is a set of parallel wires that transmit data, addresses, and control signals between components. Think of it as a highway system for data—buses must be carefully designed to handle traffic efficiently without collisions.

### 2.2 Types of Buses in a Computer System

#### System Bus (CPU-Memory Bus)
- Connects CPU directly to main memory
- Highest speed bus in the system
- Carries address, data, and control signals
- Typically 32-bit or 64-bit wide in modern systems

#### I/O Bus
- Connects CPU to peripheral devices
- Examples: USB, PCI, ISA, SATA
- Longer distance than system bus
- Lower speed than system bus

#### Internal Bus (CPU Internal)
- Connects registers within the CPU
- Also called **CPU bus** or **internal data path**
- Very high speed, limited distance

### 2.3 Bus Lines and Their Functions

```
┌─────────────────────────────────────────────────────────────────┐
│                    SYSTEM BUS STRUCTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ADDRESS BUS (Unidirectional)                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ A0 ──► A1 ──► A2 ──► ... ──► An                        │   │
│  └─────────────────────────────────────────────────────────┘   │
│  CPU sends memory addresses to memory/IO devices               │
│                                                                 │
│  DATA BUS (Bidirectional)                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ D0 ◄────► D1 ◄────► D2 ◄────► ... ◄────► Dn            │   │
│  └─────────────────────────────────────────────────────────┘   │
│  Bidirectional data transfer between components                │
│                                                                 │
│  CONTROL BUS (Bidirectional/Mixed)                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ READ  ◄───► WRITE ◄───► MEM/IO ◄───► MREQ ◄───► IOR    │   │
│  └─────────────────────────────────────────────────────────┘   │
│  Control signals for coordination                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Key Control Signals:**
| Signal | Description |
|--------|-------------|
| **RD (Read)** | Indicates memory/I/O read operation |
| **WR (Write)** | Indicates memory/I/O write operation |
| **M/IO** | Distinguishes memory from I/O operations |
| **ALE** | Address Latch Enable (8085) |
| **INTR** | Interrupt request |
| **CLK** | System clock |

### 2.4 Bus Standards: PCI and ISA

#### ISA (Industry Standard Architecture)
- Introduced in 1981 for IBM PC
- 8-bit and 16-bit versions
- Maximum clock speed: 8 MHz
- Used in early IBM-compatible computers
- **Example:** Legacy sound cards, old network cards

#### PCI (Peripheral Component Interconnect)
- Introduced in 1992 by Intel
- 32-bit or 64-bit bus width
- Clock speeds: 33 MHz, 66 MHz, 133 MHz
- Plug-and-play (PnP) support
- **Example:** Modern graphics cards, network cards

```
┌────────────────────────────────────────────────────────────┐
│              EVOLUTION OF BUS STANDARDS                    │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ISA (1981)    ████████        8 MHz    16-bit           │
│       │                                                    │
│       ▼                                                    │
│  PCI  (1992)  ████████████     33 MHz   32-bit           │
│       │                                                    │
│       ▼                                                    │
│  AGP  (1997)  █████████████    66 MHz   32-bit           │
│       │                                                    │
│       ▼                                                    │
│  PCIe (2004)  ████████████████  100+ MHz 32-bit (lanes)   │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## 3. Bus Arbitration

### 3.1 Need for Arbitration

When multiple devices share a common bus, **bus arbitration** becomes necessary to prevent conflicts. Without arbitration, two devices might try to transmit simultaneously, causing **bus contention** and data corruption.

### 3.2 Centralized vs. Distributed Arbitration

#### Centralized Arbitration
- Single arbiter (bus controller) decides which device gets bus access
- **Advantages:** Simpler device design, guaranteed fairness
- **Disadvantages:** Bottleneck, single point of failure
- **Example:** PCI bus uses centralized arbitration

**Daisy-Chain Priority Method:**
```
CPU ──► Device 1 ──► Device 2 ──► Device 3
   │         │          │          │
   └─────────┴──────────┴──────────┘
   Bus Grant signals propagate down the chain
```

**Independent Request/Grant Method:**
```
        ┌────── Bus Arbiter ──────┐
        │                          │
   REQ1 ─┤                        ├── GRANT1
   REQ2 ─┤                        ├── GRANT2
   REQ3 ─┤                        ├── GRANT3
        └──────────────────────────┘
```

#### Distributed Arbitration
- No central controller; devices collaborate
- **Examples:** Ethernet (CSMA/CD), Token Ring
- **Advantages:** No single point of failure, scalable
- **Disadvantages:** More complex device logic

### 3.3 Arbitration Methods

| Method | Description | Priority |
|--------|-------------|----------|
| **Daisy Chain** | Devices wired in series; closer to CPU has higher priority | Fixed |
| **Polling** | Arbiter checks each device in sequence | Rotating |
| **Independent Request** | Each device has separate request/grant lines | Configurable |
| **Collision Detection** | Devices check if bus is busy before transmitting | Equal |

---

## 4. Bus Timing

### 4.1 Synchronous Bus Timing

In **synchronous buses**, all operations are synchronized by a clock signal. Every bus transaction takes an integer number of clock cycles.

**Timing Diagram - Synchronous Read:**
```
Clock:     ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐
           │   │   │   │   │   │   │   │   │   │   │   │
           ▼   │   ▼   │   ▼   │   ▼   │   ▼   │   ▼   │
              ──┘     ──┘     ──┘     ──┘     ──┘     ──┘
               
ADDR:      ═══════════════════════════════►
                 [Address Valid]

DATA:                    ════════════════►
                              [Data Valid]

RD:           ┌─────────────────────────────────────┘
              │   (Active Low)
              └────
```

**Advantages:**
- Simple to implement and control
- Predictable timing
- Lower cost

**Disadvantages:**
- Speed limited by slowest device
- Clock distribution overhead

### 4.2 Asynchronous Bus Timing

In **asynchronous buses**, no common clock exists. Devices use **handshaking signals** to coordinate transfers.

**Handshaking Protocol:**
```
Device A                          Device B
   │                                 │
   ├───── REQ (Request) ─────────────►│
   │                                 │
   │◄───── ACK (Acknowledge) ────────┤
   │                                 │
   ├───── DATA ─────────────────────►│
   │                                 │
   │◄───── ACK (Data Received) ──────┤
```

**Example 8085 Bus Timing (Synchronous Read Cycle):**

```assembly
; 8085 Microprocessor - Memory Read Operation
; This demonstrates the timing of a typical bus cycle

; Assuming: A register contains address, data goes to accumulator
LXI H, 2000H    ; Load address 2000H into HL pair
MOV A, M        ; Move data from memory to accumulator

; Bus Cycle Timing (3 T-states for memory read):
; T1: Address sent on address bus, ALE pulse, RD' signal goes low
; T2: Memory places data on data bus
; T3: Data latched into CPU, RD' goes high
```

### 4.3 Bus Cycle Examples

**8085 Bus Cycle Timing (Memory Read):**
```
T-State    Activity
─────────────────────────────────────────
T1         Address on AD7-AD0 and A15-A8
           ALE latches address
           S0=1, S1=1 (Write to memory)
           
T2         RD' goes LOW
           Data from memory appears on AD7-AD0
           
T3         Data latched into internal register
           RD' goes HIGH
```

---

## 5. Control Unit Design

### 5.1 Introduction to Control Unit

The **Control Unit (CU)** is the component of the CPU that directs the operation of the processor. It fetches instructions from memory, decodes them, and generates control signals to execute them.

**Main Functions:**
1. **Instruction Fetch** - Get instruction from memory
2. **Instruction Decode** - Determine what operation to perform
3. **Control Signal Generation** - Activate hardware components
4. **Sequencing** - Control the order of operations

### 5.2 Hardwired Control

In **hardwired control**, the control logic is implemented using combinational circuits (AND, OR, NOT gates, decoders, etc.). Control signals are generated directly from the instruction register and timing states.

**Block Diagram - Hardwired Control:**
```
┌─────────────────────────────────────────────────────────────────┐
│                    HARDWIRED CONTROL UNIT                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Instruction ──► ──► Instruction ──► Control          ──►      │
│  Register (IR)      Decoder              Logic         ──►      │
│                                              │         ──►      │
│                                              ▼                  │
│  Timing          ──► ──► Timing            Control      ──►      │
  Counter (TC)           Logic              Signals              │
│                                              │                  │
│                                              ▼                  │
│                                         Datapath               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Advantages:**
- Fast execution (no microinstruction fetch)
- Less overhead
- Suitable for RISC processors

**Disadvantages:**
- Complex circuit design
- Difficult to modify/extend
- Inflexible to new instructions

**Example - Control Signal Generation (Simplified):**
```verilog
// Verilog code for generating control signals in hardwired control
// Example for a simple processor

module control_unit (
    input [7:0] instruction,
    input [2:0] state,
    output reg mem_read,
    output reg mem_write,
    output reg alu_op,
    output reg reg_write
);

    // Decode instruction
    wire is_load, is_store, is_add;
    assign is_load  = (instruction[7:5] == 3'b000);
    assign is_store = (instruction[7:5] == 3'b001);
    assign is_add   = (instruction[7:5] == 3'b010);

    // Generate control signals based on instruction and state
    always @(*) begin
        mem_read = 1'b0;
        mem_write = 1'b0;
        alu_op = 1'b0;
        reg_write = 1'b0;
        
        case (state)
            3'b001: begin // Fetch state
                mem_read = 1'b1;
            end
            3'b010: begin // Decode state
                // No external signals
            end
            3'b011: begin // Execute state
                if (is_load) begin
                    mem_read = 1'b1;
                    reg_write = 1'b1;
                end
                else if (is_store) begin
                    mem_write = 1'b1;
                end
                else if (is_add) begin
                    alu_op = 1'b1;
                    reg_write = 1'b1;
                end
            end
        endcase
    end
endmodule
```

### 5.3 Microprogrammed Control

In **microprogrammed control**, control signals are stored in **control memory (ROM/PROM)** as microinstructions. Each instruction is executed as a sequence of microinstructions.

**Block Diagram - Microprogrammed Control:**
```
┌─────────────────────────────────────────────────────────────────┐
│                 MICROPROGRAMMED CONTROL UNIT                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Instruction ──► ──► Microinstruction ──► Control       ──►     │
│  Register (IR)      Address             Memory        ──►       │
│                     Generator                              │     │
│                                                 │        │       │
│                     ┌──────────────────────────┘        │       │
│                     ▼                                    ▼       │
│               Microprogram                   Control             │
│               (Control Memory)               Signals              │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Control Memory (ROM):                                    │  │
│  │  Address:  Microinstruction:                             │  │
│  │  0000      Fetch:  PC→MAR, MEM→IR, PC+1                  │  │
│  │  0001      Decode:  IR→Decoder                           │  │
│  │  0010      LDA:    IR[addr]→MAR, MEM→AC                  │  │
│  │  0011      STA:    IR[addr]→MAR, AC→MEM                  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Types of Microinstructions:**
1. **Horizontal** - Each bit controls one signal (wide, fast)
2. **Vertical** - Encoded control signals (narrow, slower)

**Example - Microinstruction Format:**
```
┌─────────────┬─────────────┬─────────────┬─────────────┬──────────┐
│    Next     │   Branch    │    ALU      │   Memory    │  Register│
│   Address   │   Control   │  Operation  │  Operation  │  Control │
│   (8 bits)  │   (2 bits)  │  (4 bits)   │  (3 bits)   │  (4 bits)│
└─────────────┴─────────────┴─────────────┴─────────────┴──────────┘
```

**Advantages:**
- Easier to design and modify
- Flexible for complex instruction sets
- Better for CISC processors

**Disadvantages:**
- Slower execution (microinstruction fetch overhead)
- Requires control memory

### 5.4 Comparison: Hardwired vs Microprogrammed

| Aspect | Hardwired Control | Microprogrammed Control |
|--------|-------------------|------------------------|
| Speed | Faster | Slower |
| Complexity | Complex circuit | Simpler circuit |
| Flexibility | Difficult to modify | Easy to modify |
| Design | Manual circuit design | Programming approach |
| Cost | Higher (more gates) | Lower (ROM) |
| Use Case | RISC processors | CISC processors |
| Example | ARM, MIPS | Intel 8086, x86 |

---

## 6. Delhi University Specific Examples

### 6.1 8085 Microprocessor Bus Structure

The **Intel 8085** is a classic 8-bit microprocessor commonly studied in Delhi University courses. Its bus organization provides an excellent example of practical bus implementation.

**8085 Pin Diagram (Bus Related):**
```
┌──────────────────────────────────────────────────────────────┐
│                     8085A PIN CONFIGURATION                  │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│     A15-A8 (Address Bus - Upper 8 bits)                     │
│     AD7-AD0 (Address/Data Bus - Multiplexed)                │
│     ALE (Address Latch Enable)                              │
│     RD' (Read Control)                                      │
│     WR' (Write Control)                                     │
│     S0, S1 (Status Signals)                                 │
│     IO/M' (I/O or Memory Select)                            │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**8085 Bus Timing Example (Machine Cycle):**

```c
// Pseudo-code demonstrating 8085 bus cycles

// Machine cycle types in 8085:
// Opcode Fetch (1-2 T-states)
// Memory Read (3 T-states)
// Memory Write (3 T-states)
// I/O Read/Write

void execute_mvi_instruction(uint8_t data) {
    // MVI instruction: Move Immediate to Register
    // Machine Cycles: Opcode Fetch (4T) + Data Read (3T)
    
    // Machine Cycle 1: Opcode Fetch
    // T1: Address (PC) placed on address bus
    // T2: RD' goes LOW
    // T3: Opcode latched, PC incremented
    // T4: Decode instruction
    
    // Machine Cycle 2: Data Read
    // T1: Address (PC) placed on address bus  
    // T2: RD' goes LOW
    // T3: Data latched into register
}
```

### 6.2 Control Signals in 8085

```
┌─────────────────────────────────────────────────────────────────┐
│              8085 CONTROL SIGNAL GENERATION                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Status Signals: S1, S0                                        │
│  ┌───────┬───────┬─────────────┐                               │
│  │   S1  │   S0  │   Machine   │                               │
│  │   0   │   0   │   HALT      │                               │
│  │   0   │   1   │   WRITE     │                               │
│  │   1   │   0   │   READ      │                               │
│  │   1   │   1   │   FETCH     │                               │
│  └───────┴───────┴─────────────┘                               │
│                                                                 │
│  Memory/I/O Control: IO/M'                                     │
│  ┌───────────┬─────────────────────┐                           │
│  │ IO/M' = 0 │  Memory Operation   │                           │
│  │ IO/M' = 1 │  I/O Operation      │                           │
│  └───────────┴─────────────────────┘                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Advanced Topics

### 7.1 Bus Master and Bus Slave

- **Bus Master** - Device that initiates bus transactions (usually CPU or DMA controller)
- **Bus Slave** - Device that responds to bus transactions (memory, I/O devices)

### 7.2 Plug and Play (PnP)

Modern bus architectures support automatic configuration:
- BIOS detects new devices
- Assigns unique I/O addresses and IRQ lines
- No manual configuration required

### 7.3 Bus Width and Performance

**Bandwidth Calculation:**
```
Bandwidth = (Bus Width / 8) × Clock Frequency × Transfer Rate

Example:
- 32-bit PCI bus at 33 MHz
- Bandwidth = (32/8) × 33 × 10⁶ = 132 MB/s
- Effective: ~100 MB/s (accounting for protocol overhead)
```

---

## 8. Multiple Choice Questions

**Question 1:** Which bus carries memory addresses from the CPU to memory?
- A) Data Bus
- B) Address Bus
- C) Control Bus
- D) System Bus

**Answer:** B) Address Bus

---

**Question 2:** In a typical computer system, which bus has the highest speed?
- A) I/O Bus
- B) Expansion Bus
- C) System Bus
- D) USB

**Answer:** C) System Bus

---

**Question 3:** Which control unit design method uses ROM to store control signals?
- A) Hardwired Control
- B) Microprogrammed Control
- C) Pipeline Control
- D) Pipeline Control

**Answer:** B) Microprogrammed Control

---

**Question 4:** What is bus arbitration?
- A) Speed of data transfer
- B) Process of granting bus access to devices
- C) Memory addressing scheme
- D) Type of bus

**Answer:** B) Process of granting bus access to devices

---

**Question 5:** In the 8085 microprocessor, what does the signal ALE stand for?
- A) Address Latch Enable
- B) Alternate Logic Enable
- C) Arithmetic Logic Extension
- D) Asynchronous Latch Entry

**Answer:** A) Address Latch Enable

---

**Question 6:** Which arbitration method uses a single arbiter to resolve conflicts?
- A) Distributed Arbitration
- B) Centralized Arbitration
- C) Daisy Chain
- D) Polling

**Answer:** B) Centralized Arbitration

---

**Question 7:** What type of bus timing uses handshaking signals?
- A) Synchronous
- B) Asynchronous
- C) Parallel
- D) Serial

**Answer:** B) Asynchronous

---

**Question 8:** Which bus standard introduced plug-and-play support?
- A) ISA
- B) PCI
- C) AGP
- D) EISA

**Answer:** B) PCI

---

**Question 9:** In microprogrammed control, what stores the microinstructions?
- A) Register
- B) ALU
- C) Control Memory (ROM)
- D) Cache

**Answer:** C) Control Memory (ROM)

---

**Question 10:** What is the primary advantage of hardwired control over microprogrammed control?
- A) Flexibility
- B) Ease of modification
- C) Speed
- D) Simplicity

**Answer:** C) Speed

---

## 9. Key Takeaways

1. **Bus Organization Fundamentals**: Buses are categorized into address, data, and control buses. The system bus connects CPU to memory, while I/O buses connect peripherals.

2. **Bus Arbitration**: Essential for preventing conflicts when multiple devices share a bus. Can be centralized (single arbiter) or distributed (collaborative).

3. **Bus Timing**: Synchronous buses use a common clock; asynchronous buses use handshaking protocols. Choice affects speed, complexity, and compatibility.

4. **Control Unit Design**: Two primary approaches—hardwired (fast, inflexible) and microprogrammed (flexible, slower). Modern processors often use hybrid approaches.

5. **Bus Standards**: PCI replaced ISA in modern systems. PCIe offers even higher speeds through serial point-to-point connections.

6. **8085 Relevance**: Delhi University syllabus emphasizes 8085 microprocessor bus structure, timing cycles, and control signals—essential for understanding basic processor architecture.

7. **Performance Factors**: Bus width, clock frequency, and arbitration method directly impact system performance.

8. **Practical Applications**: Understanding bus architecture is crucial for system programming, hardware troubleshooting, and embedded systems development.

---

**Word Count: ~2100 words**

*Material prepared for Ge2C Computer System Architecture - Delhi University NEP 2024*