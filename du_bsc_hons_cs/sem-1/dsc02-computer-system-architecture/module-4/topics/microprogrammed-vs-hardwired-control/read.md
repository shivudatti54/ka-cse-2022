# Microprogrammed Vs Hardwired Control

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

The Control Unit (CU) is the brain of the CPU, responsible for orchestrating all operations by generating control signals that direct the data path. Understanding how control signals are generated is fundamental to computer architecture, and there are two primary approaches: **Hardwired Control** and **Microprogrammed Control**.

### Why This Topic Matters

In modern computing, the choice between hardwired and microprogrammed control affects:
- **Performance**: Hardwired control is faster; microprogrammed control is more flexible
- **Design Complexity**: Hardwired requires complex combinatorial logic; microprogrammed uses stored microcode
- **Cost and Flexibility**: Trade-offs between manufacturing cost, design time, and adaptability
- **Instruction Set Design**: Influences whether a processor is classified as RISC or CISC

This topic is explicitly covered in the Delhi University BSc (Hons) Computer Science syllabus under "Computer System Architecture" and is essential for understanding CPU design, instruction execution, and processor evolution.

---

## 2. Control Unit: Foundational Concepts

Before comparing control approaches, let's establish the fundamentals:

### 2.1 What Does the Control Unit Do?

The Control Unit:
- Fetches instructions from memory
- Decodes instructions to determine operations
- Generates control signals for data path elements (ALU, registers, buses, memory)
- Manages instruction sequencing and pipeline (if applicable)
- Handles interrupts and exceptions

### 2.2 Control Signal Requirements

A typical CPU requires control signals for:
- Register selection (which register to read/write)
- ALU operation selection
- Memory read/write enable
- Bus transfer direction
- Timing and sequencing

---

## 3. Hardwired Control

### 3.1 Overview

Hardwired control implements the control logic using combinational circuits (logic gates, decoders, flip-flops). The control signals are generated through hardware logic based on the current instruction opcode, timing cycle, and processor state.

### 3.2 Architecture of Hardwired Control

```
┌─────────────────────────────────────────────────────────────┐
│                    HARDWIRED CONTROL                        │
│                                                             │
│  Instruction Register ──────┐                               │
│                             │                               │
│  Timing/Step Counter ───────┼──► Control Logic ──► Control │
│                             │    (Decoder + State          │   
│  Flags/Status ──────────────┘     Machine)        Signals  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Key Components

1. **Instruction Register (IR)**: Holds the current instruction
2. **Decoder**: Decodes the opcode to identify the operation
3. **Sequencer/State Machine**: Manages timing sequences (fetch, decode, execute)
4. **Control Logic**: Generates control signals based on decoded instruction and timing

### 3.4 How It Works (Step-by-Step)

**Example: ADD R1, R2, R3 (Register-register ADD)**

```
Step 1 (Fetch): 
  - IR ← M[PC], PC ← PC + 1

Step 2 (Decode):
  - Decode opcode = ADD (register format)
  - Identify source registers R2, R3 and destination R1

Step 3 (Execute):
  - Control signals generated:
    * Select R2, R3 as ALU inputs
    * Select ADD operation
    * Enable ALU output to destination register R1
```

### 3.5 PLA-Based Control

A Programmable Logic Array (PLA) is commonly used in hardwired control:

- **Structure**: AND plane + OR plane
- **How it works**: 
  - AND gates implement product terms (minterms)
  - OR gates implement sum terms (output functions)
- **Advantages**: Flexible, reduces gate count, easy to modify
- **Disadvantages**: Slower than dedicated gates, more expensive

**PLA Truth Table Example (Simplified):**

| Instruction | Opcode Bits | S1 | S0 | Add | Sub | Load | Store |
|-------------|-------------|----|----|-----|-----|------|-------|
| ADD         | 000         | 1  | 0  | 1   | 0   | 0    | 0     |
| SUB         | 001         | 0  | 1  | 0   | 1   | 0    | 0     |
| LOAD        | 010         | 0  | 0  | 0   | 0   | 1    | 0     |
| STORE       | 011         | 0  | 0  | 0   | 0   | 0    | 1     |

### 3.6 Advantages of Hardwired Control

- **Speed**: Fastest possible control signal generation (typically 1-2 gate delays)
- **No microcode storage needed**: Saves die area
- **Deterministic timing**: Easy to analyze timing behavior
- **Efficient for simple instruction sets**: RISC processors benefit greatly

### 3.7 Disadvantages of Hardwired Control

- **Complex design**: Requires extensive manual logic design
- **Difficult to modify**: Changes require hardware redesign
- **Scalability issues**: Complex for large instruction sets
- **Not flexible**: Cannot easily support new instructions

---

## 4. Microprogrammed Control

### 4.1 Overview

Microprogrammed control stores the control logic as **microinstructions** in a **control memory** (ROM, PROM, or RAM). Each machine instruction is implemented as a **microprogram** — a sequence of microinstructions that generate control signals.

### 4.2 Basic Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                    MICROPROGRAMMED CONTROL                      │
│                                                                  │
│  Instruction Register ──► Microprogram Counter ──► Control    │
│         │                         │                   Memory    │
│         │                         │                     │       │
│         │                         │                     ▼       │
│         │                    ┌────┴────┐            Microinstruction
│         │                    │ Address │                 │
│         │                    │  Logic  │                 │
│         │                    └─────────┘                 │
│         │                         │                       │
│         └─────────────────────────┼───────────────────────┘
│                                   │
│                              Control Signals
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### 4.3 Control Word Format

The **control word** (microinstruction) contains fields that specify:

```
┌──────────┬──────────┬──────────┬──────────┬──────────┬─────────────┐
│  ALU     │  Src     │  Dest    │  Memory  │  PC      │   Next      │
│  Function│  Register│  Register│  Control │  Control │   Address   │
│  (4 bits)│  (3 bits)│  (3 bits)│  (2 bits)│  (2 bits)│   (n bits)  │
└──────────┴──────────┴──────────┴──────────┴──────────┴─────────────┘
  ←────────────────────── Horizontal ──────────────────────────────→
```

**Example Control Word (16-bit):**

```
Bits 0-3:   ALU Operation (0000=NOP, 0001=ADD, 0010=SUB, 0011=AND, etc.)
Bits 4-6:   Source Register Select (R0-R7)
Bits 7-9:   Destination Register Select (R0-R7)
Bit  10:    Memory Read Enable
Bit  11:    Memory Write Enable
Bit  12:    PC Increment Enable
Bit  13:    Jump/Branch Enable
Bits 14-15: Next Address Control (00=Sequential, 01=Jump, 10=Call)
```

### 4.4 Horizontal vs Vertical Microprogramming

#### Horizontal Microprogramming

- **Wide microinstructions**: Each control signal has its own bit
- **More parallelism**: Can generate multiple control signals simultaneously
- **Faster execution**: No decoding needed
- **Disadvantage**: Long instruction word (80-100 bits typical)

**Example Horizontal Format:**
```
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│MRE│MWE│ALU│RS1│RS2│RD1│RD2│PC │...│...│  ← 100+ bits
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
```

#### Vertical Microprogramming

- **Narrow microinstructions**: Encoded control signals
- **Requires decoding**: Additional decoder stage
- **Less parallelism**: Some signal encoding reduces concurrency
- **Advantage**: Compact (20-30 bits typical), simpler control memory

**Example Vertical Format:**
```
┌─────────────────┬─────────────────┐
│  Operation     │   Address       │
│  Code (8 bits) │   Field         │
└─────────────────┴─────────────────┘
       ↓ Decode
┌───┬───┬───┬───┬───┬───┐
│MRE│MWE│ALU│RS1│RS2│RD1│  ← Generated after decoding
└───┴───┴───┴───┴───┴───┘
```

### 4.5 Microinstruction Types

1. **Horizontal Microinstructions**: Fully decoded, directly generate all control signals
2. **Vertical Microinstructions**: Encoded, require decoding
3. **Hybrid**: Combination with some encoding

**Microinstruction Sequencing Types:**

- **Sequential**: Next microaddress = current + 1
- **Unconditional Jump**: Next microaddress = specified address
- **Conditional Jump**: Jump based on condition flags (e.g., zero flag, carry flag)
- **Subroutine Call**: Push return address, jump to micro-subroutine

### 4.6 Example: Microprogram for ADD Instruction

Let's design microcode for a simple processor:

```
; Microprogram for ADD Rdest, Rsrc1, Rsrc2
; Assume format: ADD Rdest, Rsrc1, Rsrc2

; Microaddress 0x10: Fetch Instruction
0x10:  MRE=1, PC_INC=1      ; Read memory[PC], increment PC
       GOTO 0x11            ; Next: Decode

; Microaddress 0x11: Decode
0x11:  IR_LOAD=1            ; Load instruction into IR
       GOTO 0x12            ; Next: Identify instruction type

; Microaddress 0x12: Check for ADD opcode
0x12:  IF (IR[15:12]==ADD)  ; Check opcode
         GOTO 0x20          ; Go to ADD microcode
       ELSE
         GOTO ERROR         ; Unknown instruction

; Microaddress 0x20: Execute ADD
0x20:  RSEL1=IR[11:9]       ; Select first source register
       RSEL2=IR[8:6]        ; Select second source register
       ALU_OP=ADD          ; Set ALU to ADD
       RDSEL=IR[5:3]        ; Select destination register
       DEST_LOAD=1         ; Load result into destination
       FLAGS_UPDATE=1      ; Update zero/carry flags
       GOTO 0x00           ; Return to fetch
```

### 4.7 Real-World Example: Intel 8086 Microcode

The Intel 8086 (1978) used microprogrammed control:

```assembly
; Simplified 8086 ADD instruction microcode
; Actual 8086 used different addressing modes

FETCH:  MAR <- PC, READ, PC <- PC + 1
DECODE: IR <- MDR, decode opcode
ADD_RR: A <- R[src1], B <- R[src2]  ; Register-Register
        ALU <- A + B
        R[dest] <- ALU
        FLAGS <- ALU
        GOTO FETCH
```

### 4.8 Advantages of Microprogrammed Control

- **Flexibility**: Easy to modify, add new instructions via microcode updates
- **Structured design**: Organized into microprograms, easier to design
- **Testing**: Microcode can be tested independently
- **Cost-effective for complex ISAs**: CISC processors benefit
- **Can emulate other architectures**: IBM 360 could emulate older systems

### 4.9 Disadvantages of Microprogrammed Control

- **Slower execution**: Additional memory fetch for each microinstruction
- **Control memory overhead**: Requires ROM/RAM for microcode storage
- **More complex hardware**: Need for microprogram counter, address logic
- **Performance penalty**: Two-level interpretation (machine instruction → microinstructions)

---

## 5. Comprehensive Comparison Table

| Aspect | Hardwired Control | Microprogrammed Control |
|--------|-------------------|------------------------|
| **Speed** | Very fast (1-2 gate delays) | Slower (memory fetch + decode) |
| **Flexibility** | Low - hardware changes needed | High - microcode updates |
| **Design Complexity** | Complex logic design | Structured, organized |
| **Cost** | Lower for simple ISAs | Lower for complex ISAs |
| **Modifiability** | Difficult to modify | Easy to add instructions |
| **Area** | More gates, no control memory | Control memory + decoder |
| **Reliability** | More reliable (no storage) | Susceptible to microcode bugs |
| **Power Consumption** | Generally higher | Generally lower (smaller logic) |
| **Debugging** | Hardware debugging required | Microcode can be traced |
| **Suitable For** | RISC, simple ISAs, high-performance | CISC, complex ISAs, emulation |
| **Timing Analysis** | Straightforward | More complex |
| **Technology Changes** | Requires redesign | Can adapt via microcode |

---

## 6. RISC vs CISC Implications

### 6.1 RISC (Reduced Instruction Set Computer)

- **Control Approach**: Primarily **Hardwired**
- **Rationale**:
  - Simple instruction format (fixed length)
  - Few instruction types
  - Most instructions execute in single cycle
  - Hardwired control provides maximum speed
- **Examples**: ARM (early versions), MIPS, SPARC, RISC-V
- **Microcode usage**: Minimal or none; some RISC-V implementations use it for complex operations

### 6.2 CISC (Complex Instruction Set Computer)

- **Control Approach**: Primarily **Microprogrammed**
- **Rationale**:
  - Variable-length instructions
  - Complex addressing modes
  - Many instruction types
  - Microcode provides flexibility to implement complex semantics
- **Examples**: Intel x86, IBM System/360, VAX
- **Evolution**: Modern x86 uses hybrid approach (hardware decoder converts to micro-ops)

### 6.3 Modern Processors: The Hybrid Approach

Modern processors like Intel Core i7 use **both**:

```
┌─────────────────────────────────────────────────────┐
│            MODERN HYBRID CONTROL                    │
│                                                      │
│   CISC Instruction → Decoder → Micro-ops            │
│   (x86)              ↓              ↓               │
│                  Hardwired    Microprogrammed      │
│                  (Simple ops) (Complex ops)        │
│                                    ↓                │
│                              Execution Units        │
└─────────────────────────────────────────────────────┘
```

---

## 7. Timing Considerations

### 7.1 Hardwired Control Timing

```
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│  T1     │  T2     │  T3     │  T4     │  T5     │
├─────────┼─────────┼─────────┼─────────┼─────────┤
│ Fetch   │ Decode  │ Execute │ Result  │ Next    │
│         │         │         │ Write   │ Instr   │
└─────────┴─────────┴─────────┴─────────┴─────────┘
  ↑
  Control signals generated with minimal delay
  (typically 5-10 nanoseconds)
```

### 7.2 Microprogrammed Control Timing

```
┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
│  T1     │  T2     │  T3     │  T4     │  T5     │  T6     │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ Fetch   │ Fetch   │ Decode  │ Decode  │ Execute │ Execute │
│ µinst   │ µinst   │ µinst   │ µinst   │ µinst   │ µinst   │
└─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
  ↑                ↑              ↑
  Memory          Memory         Memory
  Access          Access         Access
  (~10-20ns each)
```

### 7.3 Performance Impact

| Factor | Hardwired | Microprogrammed |
|--------|-----------|------------------|
| Control Signal Delay | 2-5 ns | 15-30 ns per microstep |
| Microsteps per Instruction | 1-4 | 2-10 |
| Total Control Overhead | Low | High |
| Pipeline Friendliness | Better | Requires careful design |

---

## 8. Example with Code: Designing Simple Control Units

### 8.1 Example 1: Hardwired Control for Simple ALU

```verilog
// Simple Hardwired Control Unit (Verilog)
// For a 4-function ALU

module hardwired_control (
    input [3:0] opcode,
    input [1:0] funct,
    input clk, reset,
    output reg [2:0] alu_op,
    output reg reg_write, mem_read, mem_write
);

    // State machine states
    parameter FETCH = 3'b000;
    parameter DECODE = 3'b001;
    parameter EXECUTE = 3'b010;
    parameter MEM_ACCESS = 3'b011;
    parameter WRITE_BACK = 3'b100;

    reg [2:0] state, next_state;

    // State transition
    always @(posedge clk or posedge reset) begin
        if (reset)
            state <= FETCH;
        else
            state <= next_state;
    end

    // Next state logic
    always @(*) begin
        case (state)
            FETCH: next_state = DECODE;
            DECODE: next_state = EXECUTE;
            EXECUTE: begin
                if (opcode == 4'b0001) // LOAD/STORE
                    next_state = MEM_ACCESS;
                else
                    next_state = WRITE_BACK;
            end
            MEM_ACCESS: next_state = WRITE_BACK;
            WRITE_BACK: next_state = FETCH;
            default: next_state = FETCH;
        endcase
    end

    // Control signal generation
    always @(*) begin
        {reg_write, mem_read, mem_write} = 3'b000;
        alu_op = 3'b000;

        case (state)
            FETCH: begin
                mem_read = 1'b1;
            end

            EXECUTE: begin
                case (opcode)
                    4'b0000: begin // R-type
                        case (funct)
                            2'b00: alu_op = 3'b001; // ADD
                            2'b01: alu_op = 3'b010; // SUB
                            2'b10: alu_op = 3'b011; // AND
                            2'b11: alu_op = 3'b100; // OR
                        endcase
                        reg_write = 1'b1;
                    end
                    4'b0001: mem_read = 1'b1; // LOAD
                    4'b0010: mem_write = 1'b1; // STORE
                endcase
            end

            MEM_ACCESS: begin
                if (opcode == 4'b0001) begin // LOAD
                    mem_read = 1'b1;
                    reg_write = 1'b1;
                end
            end
        endcase
    end
endmodule
```

### 8.2 Example 2: Microprogrammed Control Memory Definition

```c
// Microprogram Control Memory Definition
// For a simple processor with 8-bit control words

#define MICROMEM_SIZE 256

// Control word bit positions
typedef struct {
    unsigned int alu_sel   : 3;  // ALU operation select
    unsigned int src_reg   : 3;  // Source register 1
    unsigned int src_reg2  : 3;  // Source register 2
    unsigned int dst_reg   : 3;  // Destination register
    unsigned int mem_read  : 1;  // Memory read enable
    unsigned int mem_write : 1;  // Memory write enable
    unsigned int pc_inc    : 1;  // Increment PC
    unsigned int pc_load   : 1;  // Load PC (jump)
    unsigned int ir_load   : 1;  // Load Instruction Register
    unsigned int acc_load  : 1;  // Load Accumulator
    unsigned int flags_en  : 1;  // Enable flag update
    unsigned int next_sel  : 2;  // Next address selection
} ControlWord;

// Microinstruction encoding
typedef struct {
    ControlWord cw;
    unsigned char next_addr;  // Next microaddress
    unsigned char branch_addr; // Branch target (if conditional)
} MicroInstruction;

// Control Memory (ROM)
const MicroInstruction control_memory[MICROMEM_SIZE] = {
    // Fetch Cycle - Read instruction from memory
    [0x00] = {
        .cw = {
            .alu_sel = 0,        // NOP
            .mem_read = 1,      // Read memory
            .pc_inc = 1,        // Increment PC
            .ir_load = 0,
            .next_sel = 0        // Sequential
        },
        .next_addr = 0x01
    },

    // Decode - Load instruction into IR
    [0x01] = {
        .cw = {
            .alu_sel = 0,
            .ir_load = 1,
            .next_sel = 0
        },
        .next_addr = 0x02
    },

    // Execute ADD R1, R2 (register-register)
    [0x10] = {
        .cw = {
            .alu_sel = 1,        // ADD operation
            .src_reg = 2,        // R2
            .src_reg2 = 3,       // R3
            .dst_reg = 1,        // R1 = R2 + R3
            .acc_load = 1,
            .flags_en = 1,
            .next_sel = 0
        },
        .next_addr = 0x00        // Return to fetch
    },

    // Execute LOAD R1, [R2] (register-indirect)
    [0x11] = {
        .cw = {
            .src_reg = 2,        // Base address from R2
            .mem_read = 1,
            .next_sel = 0
        },
        .next_addr = 0x12
    },

    // Store to register
    [0x12] = {
        .cw = {
            .dst_reg = 1,        // Load to R1
            .acc_load = 1,
            .next_sel = 0
        },
        .next_addr = 0x00
    }
};

// Function to fetch microinstruction
MicroInstruction get_microinstruction(unsigned char addr) {
    return control_memory[addr];
}
```

---

## 9. Delhi University Examination Focus Areas

Based on the BSc (Hons) Computer Science syllabus (NEP 2024 UGCF), focus on:

1. **Understanding**: Difference between hardwired and microprogrammed control
2. **Analysis**: When to use each approach
3. **Design**: Basic control unit design concepts
4. **Comparison**: Advantages/disadvantages of each
5. **Application**: RISC vs CISC implications
6. **Timing**: Understanding control signal timing

---

## 10. Multiple Choice Questions

### Basic Level

1. **Which control approach provides faster execution?**
   - a) Microprogrammed
   - b) Hardwired
   - c) Both equally fast
   - d) Neither
   
   **Answer: (b)** Hardwired control generates signals directly through combinational logic, avoiding memory access overhead.

2. **Microprogrammed control stores control logic in:**
   - a) Register
   - b) Cache
   - c) Control Memory (ROM/PROM)
   - d) ALU
   
   **Answer: (c)** Control memory stores microinstructions.

3. **Horizontal microprogramming has:**
   - a) Narrow instruction format
   - b) Encoded control signals
   - c) Wide instruction format with dedicated bits
   - d) No decoding required
   
   **Answer: (c)** Horizontal microinstructions are wide with dedicated bits for each control signal.

### Intermediate Level

4. **Which architecture typically uses hardwired control?**
   - a) CISC
   - b) RISC
   - c) VAX
   - d) IBM 360
   
   **Answer: (b)** RISC processors use hardwired control for maximum performance due to simple instruction sets.

5. **PLA in hardwired control stands for:**
   - a) Programmable Logic Array
   - b) Parallel Logic Architecture
   - c) Programmable Logic Adapter
   - d) Primary Logic Unit
   
   **Answer: (a)** PLA (Programmable Logic Array) implements combinational control logic.

6. **In vertical microprogramming, control signals are:**
   - a) Directly generated
   - b) Encoded and require decoding
   - c) Not generated
   - d) Generated randomly
   
   **Answer: (b)** Vertical microinstructions are encoded and require additional decoding logic.

### Advanced/Scenario-Based

7. **A processor designer needs to add a new floating-point instruction to an existing CPU. Which control approach would require minimal hardware changes?**
   - a) Hardwired with PLA
   - b) Hardwired with discrete gates
   - c) Microprogrammed
   - d) Both equally difficult
   
   **Answer: (c)** Microprogrammed control only requires adding new microcode, no hardware changes.

8. **For a processor requiring 50 different instructions with complex addressing modes, which is more suitable?**
   - a) Hardwired control
   - b) Microprogrammed control
   - c) No control needed
   - d) PLA alone sufficient
   
   **Answer: (b)** Microprogrammed control handles complex instruction sets more effectively.

9. **The control word format in microprogrammed control contains:**
   - a) Only memory address
   - b) Only ALU operation
   - c) Multiple fields specifying control signals and next address
   - d) Only register selection
   
   **Answer: (c)** Control words contain various fields including ALU operation, register selection, memory control, and next address.

10. **In a pipelined RISC processor, the control unit is most likely:**
    - a) Fully microprogrammed
    - b) Hardwired
    - c) PLA-based with 10-bit address
    - d) Implemented in software
    
    **Answer: (b)** RISC processors use hardwired control for minimal pipeline stalls and maximum speed.

11. **What is the main disadvantage of hardwired control?**
    - a) Slow speed
    - b) Difficult to modify or extend
    - c) Requires control memory
    - d) Cannot handle complex instructions
    
    **Answer: (b)** Hardwired control is difficult to modify as it requires hardware redesign.

12. **Modern Intel/AMD processors use which approach?**
    - a) Pure microprogrammed
    - b) Pure hardwired
    - c) Hybrid (both)
    - d) Neither
    
    **Answer: (c)** Modern processors use hybrid approaches, decoding CISC instructions into micro-ops.

---

## 11. Flashcards

### Flashcard 1
**Q: What is Hardwired Control?**
**A:** A control unit design approach using combinational logic circuits (gates, decoders, flip-flops) to generate control signals. The control logic is fixed in hardware.

### Flashcard 2
**Q: What is Microprogrammed Control?**
**A:** A control unit design approach where control signals are stored as microinstructions in control memory (ROM/RAM). Each machine instruction is implemented as a microprogram.

### Flashcard 3
**Q: Define Control Word in Microprogramming.**
**A:** A control word (microinstruction) is a binary pattern containing fields that specify which control signals to activate, register selections, ALU operations, and next microaddress.

### Flashcard 4
**Q: What is the difference between Horizontal and Vertical microprogramming?**
**A:** Horizontal: Wide microinstructions with dedicated bits for each control signal (parallel, fast, but long). Vertical: Narrow encoded microinstructions requiring decoding (compact, slower).

### Flashcard 5
**Q: What is a PLA in hardwired control?**
**A:** Programmable Logic Array (PLA) - A logic device with an AND plane and OR plane that implements combinational control functions efficiently, allowing easier modifications than discrete gates.

### Flashcard 6
**Q: Why is RISC typically hardwired?**
**A:** RISC instructions are simple, fixed-format, and execute in few cycles. Hardwired control provides maximum speed (no microcode fetch overhead) and fits well with pipelining.

### Flashcard 7
**Q: Why is CISC typically microprogrammed?**
**A:** CISC has complex, variable-length instructions with many addressing modes. Microprogrammed control provides flexibility to implement these complex semantics and can be easily modified.

### Flashcard 8
**Q: What is microprogram sequencing?**
**A:** The process of determining the next microaddress to fetch. Types include: sequential (next address = current + 1), unconditional jump, conditional jump (based on flags), and subroutine calls.

### Flashcard 9
**Q: What is the advantage of microprogrammed control in terms of flexibility?**
**A:** New instructions can be added by writing new microcode without any hardware changes. This allows processor upgrades through firmware updates.

### Flashcard 10
**Q: What is the main performance disadvantage of microprogrammed control?**
**A:** Slower execution due to control memory access time for each microinstruction. Each microstep requires fetching a microinstruction from memory, adding latency.

---

## 12. Key Takeaways

1. **Fundamental Difference**: Hardwired control uses combinational logic circuits; microprogrammed control uses stored microinstructions.

2. **Speed vs Flexibility Trade-off**: Hardwired is faster but inflexible; microprogrammed is slower but easily modifiable.

3. **Control Word Format**: Contains fields for ALU operations, register selection, memory control, and next address — typically 20-100 bits depending on horizontal/vertical encoding.

4. **Horizontal vs Vertical**: Horizontal = wide, fast, parallel control; Vertical = narrow, compact, requires decoding.

5. **RISC vs CISC Connection**: RISC → Hardwired (for speed), CISC → Microprogrammed (for flexibility).

6. **PLA Usage**: Programmable Logic Arrays implement hardwired control efficiently, allowing some modification capability.

7. **Timing Impact**: Hardwired control has minimal delay (2-5ns); microprogrammed adds memory fetch time (10-20ns per microstep).

8. **Modern Processors Use Hybrid Approaches**: x86 decodes CISC instructions to RISC-like micro-ops, combining benefits of both approaches.

9. **Design Considerations**: Choice depends on instruction set complexity, performance requirements, design budget, and expected modification frequency.

10. **Examination Priority**: Focus on understanding concepts, comparison tables, advantages/disadvantages, and being able to explain when each approach is appropriate.

---

## References (Delhi University Syllabus Context)

- Computer Organization and Design, Patterson & Hennessy (RISC perspective)
- Computer Architecture: A Quantitative Approach, Hennessy & Patterson
- Microprocessor Architecture, Programming, and Applications with the 8085, Gaonkar
- Delhi University BSc (Hons) Computer Science Syllabus, NEP 2024 UGCF

---

*This study material covers the complete syllabus requirements for "Microprogrammed Vs Hardwired Control" under the Delhi University BSc (Hons) Computer Science program (NEP 2024 UGCF).*