# Instruction Cycle and Pipelining

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

### 1.1 Context and Relevance

The **Instruction Cycle** and **Pipelining** form the foundational concepts in understanding how modern computer processors execute instructions. These concepts are critical to the **Computer System Architecture** course under the Delhi University NEP 2024 UGCF curriculum for BSc (Hons) Computer Science students.

In today's computing landscape, where processors contain billions of transistors and execute billions of instructions per second, understanding how the CPU fetches, decodes, and executes instructions is essential. Whether you are using a smartphone, a desktop computer, or embedded systems in IoT devices, the instruction cycle and pipelining techniques directly impact:

- **Performance**: Clock speeds and instructions per cycle
- **Power Efficiency**: Critical for mobile and embedded devices
- **System Design**: Influences compiler design and software optimization

This study material provides an in-depth exploration of these concepts, addressing the limitations of previous versions by offering university-level depth, comprehensive coverage of hazards, forwarding mechanisms, branch prediction, and detailed performance calculations.

---

## 2. The Instruction Cycle

### 2.1 Definition and Overview

The **Instruction Cycle** (also known as the **Fetch-Decode-Execute Cycle**) is the fundamental process by which a CPU executes machine instructions. Each instruction undergoes a series of steps before completion, and the instruction cycle represents the complete lifetime of a single instruction in the processor.

**The Basic Equation:**
```
Total Execution Time = (Number of Instructions) × (Cycles per Instruction) × (Clock Cycle Time)
```

### 2.2 Detailed Phases of the Instruction Cycle

The instruction cycle consists of multiple distinct phases. Let us examine each in detail:

#### 2.2.1 Fetch Cycle (IF - Instruction Fetch)

**Purpose:** Retrieve the next instruction from memory into the Instruction Register (IR).

**Steps:**
1. **Program Counter (PC)** holds the address of the next instruction
2. The address is placed on the **address bus**
3. **Memory Address Register (MAR)** receives this address
4. The instruction is read from **Random Access Memory (RAM)** into the **Memory Data Register (MDR)**
5. The instruction is transferred to the **Instruction Register (IR)**
6. **PC is incremented** to point to the next instruction

**Key Registers Involved:**
- **PC (Program Counter)**: Contains address of next instruction
- **MAR (Memory Address Register)**: Holds address being accessed
- **MDR (Memory Data Register)**: Temporarily holds data being transferred
- **IR (Instruction Register)**: Holds the current instruction

**Timing:** Typically requires memory access time + register transfer time

#### 2.2.2 Decode Cycle (ID - Instruction Decode)

**Purpose:** Interpret the fetched instruction and prepare for execution.

**Steps:**
1. The instruction in IR is decoded by the **Control Unit**
2. Identify the **opcode** (operation to be performed)
3. Identify the **operand addresses** (source and destination)
4. **Register fetching**: If operands are in registers, fetch them
5. Determine if any **addressing mode** transformations are needed

**Control Signal Generation:** The control unit generates appropriate control signals based on the opcode.

#### 2.2.3 Execute Cycle (EX)

**Purpose:** Perform the actual operation specified by the instruction.

**Examples of Operations:**
- **Arithmetic**: ADD, SUB, MUL, DIV
- **Logical**: AND, OR, XOR, NOT
- **Data Transfer**: MOV, LOAD, STORE
- **Control Flow**: JMP, CALL, BRANCH

**ALU Operations:** For arithmetic/logical instructions, the ALU performs the computation:
```
Result = Operand1 OP Operand2
```

#### 2.2.4 Memory Access (MEM) - Optional

**Purpose:** Access memory for load/store operations.

- **Load (LDA/LOAD)**: Read data from memory into CPU
- **Store (STA/STORE)**: Write data from CPU to memory

#### 2.2.5 Write Back (WB) - Optional

**Purpose:** Store the result back to its destination.

- Write to **register file**
- Write to **memory** (for store instructions)
- Update **status flags** (for conditional instructions)

### 2.3 Instruction Cycle Timing

The number of clock cycles per instruction (CPI) varies based on instruction complexity:

| Instruction Type | Example | Typical Cycles |
|------------------|---------|----------------|
| Register-Register | ADD R1, R2, R3 | 1-2 cycles |
| Register-Immediate | ADDI R1, R2, #5 | 1-2 cycles |
| Load | LW R1, 0(R2) | 2-4 cycles |
| Store | SW R1, 0(R2) | 2-4 cycles |
| Branch | BEQ R1, R2, Label | 2-3 cycles |
| Jump | J Label | 2-3 cycles |

### 2.4 Example: Instruction Cycle in Action

Consider the following MIPS assembly code:

```mips
# Assuming: $t0 = 10, $t1 = 20
add $t2, $t0, $t1    # $t2 = $t0 + $t1
```

**Step-by-step Execution:**

1. **Fetch:** PC = 0x00400000 → Fetch instruction `add $t2, $t0, $t1`
2. **Decode:** Identify opcode 0 (ADD), registers $t0, $t1, $t2
3. **Fetch Operands:** Read values from registers $t0 (=10) and $t1 (=20)
4. **Execute:** ALU performs addition: 10 + 20 = 30
5. **Write Back:** Store result 30 in register $t2
6. **Update PC:** PC = PC + 4 (next instruction)

---

## 3. Pipelining: Concept and Implementation

### 3.1 Introduction to Pipelining

**Pipelining** is an implementation technique where multiple instructions are overlapped in execution. Like an assembly line in a factory, pipelining allows the processor to work on different phases of multiple instructions simultaneously, dramatically increasing throughput.

### 3.2 Why Pipelining?

**Without Pipelining (Sequential Execution):**
```
Instruction 1: F → D → E → W
Instruction 2:           F → D → E → W
Instruction 3:                     F → D → E → W
```

**With Pipelining:**
```
Instruction 1: F → D → E → W
Instruction 2:   F → D → E → W
Instruction 3:     F → D → E → W
Instruction 4:       F → D → E → W
```

**Key Insight:** The time per instruction (latency) remains similar, but the throughput (instructions per clock cycle) increases significantly.

### 3.3 Classic Five-Stage Pipeline

The classic RISC pipeline consists of five stages:

| Stage | Name | Function |
|-------|------|----------|
| IF | Instruction Fetch | Fetch instruction from memory |
| ID | Instruction Decode | Decode instruction, read registers |
| EX | Execute | ALU performs operation |
| MEM | Memory Access | Read/write memory (if needed) |
| WB | Write Back | Write result to register file |

### 3.4 Pipeline Registers

**Pipeline registers** (or **latches**) are placed between stages to hold intermediate results:

```
[IF/ID] → [ID/EX] → [EX/MEM] → [MEM/WB]
```

Each register stores:
- Instruction bits
- Register values
- Control signals
- Other necessary data

### 3.5 Pipeline Timing and Performance

#### 3.5.1 Speedup Calculation

For a pipeline with **k** stages and **n** instructions:

**Non-pipelined execution time:**
```
T_non_pipelined = n × k × T_clock
```

**Pipelined execution time:**
```
T_pipelined = (k + n - 1) × T_clock
```

**Speedup (S):**
```
S = (n × k) / (k + n - 1)

As n → ∞: S → k
```

**Theoretical Maximum Speedup = Number of Pipeline Stages**

#### 3.5.2 CPI Calculations

**Ideal CPI:** 1 (one instruction completes per cycle)

**Actual CPI:**
```
CPI_actual = CPI_ideal + (Stall cycles per instruction)
```

**Throughput:**
```
Throughput = Clock Frequency / CPI
```

#### 3.5.3 Example: Pipeline Performance

**Problem:** Consider a 5-stage pipeline with a 2ns clock cycle. Calculate the speedup for 100 instructions.

**Solution:**

- Non-pipelined: 100 × 5 × 2ns = 1000ns
- Pipelined: (5 + 100 - 1) × 2ns = 208ns
- Speedup = 1000 / 208 ≈ **4.81x**

The speedup approaches 5 (the number of stages) as the number of instructions increases.

---

## 4. Pipeline Hazards

**Pipeline hazards** are situations where the next instruction cannot execute in the next clock cycle. They limit the ideal performance of pipelining.

### 4.1 Structural Hazards

**Definition:** Occur when hardware cannot support all combinations of instructions in the pipeline simultaneously.

**Example:** Single-memory pipeline where both instruction fetch and data access require memory in the same cycle.

**Solution:**
- **Hardware duplication**: Separate instruction and data memory (Harvard architecture)
- **Stalling**: Insert bubble/stall until resource is available

**Example Code Showing Structural Hazard:**

```c
// If load and instruction fetch both use same memory:
LW R1, 0(R2)    // Cycle 2: MEM stage accesses memory
ADD R3, R4, R5  // Cycle 3: IF stage needs memory
                // Conflict if single memory port!
```

### 4.2 Data Hazards

Data hazards occur when instructions depend on the results of previous instructions still in the pipeline.

#### 4.2.1 Types of Data Hazards

| Hazard Type | Description | Example |
|-------------|-------------|---------|
| **RAW** (Read After Write) | True dependency | `ADD R1, R2, R3; SUB R4, R1, R5` |
| **WAR** (Write After Read) | Anti-dependency | `ADD R1, R2, R3; SUB R3, R4, R5` |
| **WAW** (Write After Write) | Output dependency | `ADD R1, R2, R3; SUB R1, R4, R5` |

**Note:** WAR and WAW hazards are more common in out-of-order execution pipelines.

#### 4.2.2 Data Hazard Example (RAW)

```mips
# MIPS assembly showing RAW hazard
    add $t0, $t1, $t2    # Instruction 1: $t0 = $t1 + $t2
    sub $t3, $t0, $t4    # Instruction 2: needs $t0 (data not available yet!)
```

**Pipeline Timeline (without forwarding):**
```
I1: IF → ID → EX → MEM → WB
I2:    IF → ID → EX(stall) → MEM → WB
                    ↑
              Must wait for I1 to write back to register
```

#### 4.2.3 Data Forwarding (Data Bypassing)

**Forwarding** routes the results directly from the output of one pipeline stage to the input of an earlier stage where it's needed, bypassing the register file.

**Hardware Implementation:**
```
EX/MEM register → ID/EX register (ALU result)
MEM/WB register → ID/EX register (load result)
```

**Example with Forwarding:**
```mips
    add $t0, $t1, $t2    # I1: produces result in EX stage
    sub $t3, $t0, $t4    # I2: can get $t0 from forwarding in EX stage
```

**Pipeline Timeline (with forwarding):**
```
I1: IF → ID → EX → MEM → WB
I2:    IF → ID → EX(forwarded) → MEM → WB
           ↑
     Result forwarded from I1's EX/MEM pipeline register
```

#### 4.2.4 Load-Use Hazard

A special case where a load instruction's data is needed by the next instruction:

```mips
    lw $t0, 0($t1)       # Load: data available after MEM stage
    add $t2, $t0, $t3    # Use: needs $t0 in EX stage
```

**Solution:** Insert a stall (one bubble) between load and use:
```
lw $t0, 0($t1)        # Cycle: IF ID EX MEM WB
nop                   # Cycle:    IF ID EX MEM WB (stall)
add $t2, $t0, $t3     # Cycle:       IF ID EX MEM WB
```

### 4.3 Control Hazards

**Definition:** Occur due to branches and jumps. The pipeline doesn't know which instruction to fetch next until the branch outcome is determined.

#### 4.3.1 Branch Penalty

The number of cycles lost when a branch is mispredicted or unresolved.

```
Branch Penalty = Number of cycles to resolve branch
```

#### 4.3.2 Solutions to Control Hazards

**1. Stall until Branch Resolution (Flush Pipeline)**
```
I1: IF → ID → EX → MEM → WB
beq $t0, $t1, Label   # Branch instruction
I2:    IF → ID → (stall) → (flush)
I3:           IF → ID → ...
```

**2. Branch Delay Slots**
```mips
    bne $t0, $t1, Loop
    nop              # Delay slot - always executed
    add $t2, $t3, $t4 # This executes regardless of branch
```

**3. Static Branch Prediction**
- **Predict Not Taken**: Assume branch not taken, continue fetching sequentially
- **Predict Taken**: Assume branch taken, fetch from target address

**4. Dynamic Branch Prediction**

**a) 1-bit Predictor:**
```
History: 0 (not taken), 1 (taken)
- If history=0, predict not taken
- If history=1, predict taken
- Update history based on actual outcome
```

**b) 2-bit Predictor ( Saturating Counter):**
```
00: Strongly not taken
01: Weakly not taken
10: Weakly taken
11: Strongly taken

- Need two consecutive mispredictions to change prediction
```

**c) Branch Target Buffer (BTB):**
- Cache storing: Branch instruction address → Target address + prediction bit
- Hardware table checked during IF stage

**d) Tournament Predictor:**
- Combines multiple predictors (local + global)
- Chooses best predictor for each branch

#### 4.3.3 Example: Branch Prediction in Code

```c
// Simple loop - predictable branch
for (int i = 0; i < 1000; i++) {
    sum += array[i];  // Branch: likely taken (i < 1000)
}
// For this loop, "predict taken" would be highly accurate
```

---

## 5. Advanced Pipeline Concepts

### 5.1 Pipeline Bubbles

A **bubble** is a NOP (no operation) instruction inserted into the pipeline to resolve hazards.

**Creating a Bubble:**
```
IF  ID  EX  MEM  WB
     bubble bubble bubble bubble bubble
```

**Impact:** Each bubble reduces effective CPI by 1.

### 5.2 Stall vs. Flush

| Concept | Description | Use Case |
|---------|-------------|----------|
| **Stall** | Pause pipeline at a stage | Data hazard (load-use) |
| **Flush** | Clear instructions in pipeline | Mispredicted branch |

### 5.3 Superpipelining

Deep pipelining with more than 5 stages (10-20 stages in modern processors).

**Advantages:** Higher clock frequency
**Disadvantages:** More hazards, higher penalty for misprediction

### 5.4 Superscalar Processors

Multiple instructions issued per cycle in parallel pipelines.

**CPI Formula for Superscalar:**
```
CPI = Instructions / (Cycles × Issue Width)
```

---

## 6. Performance Summary Formulas

### 6.1 Key Equations

```
1. CPU Time = Instruction Count × CPI × Clock Cycle Time
   
2. MIPS Rating = (Clock Rate in MHz) / CPI
   
3. Speedup = Non-pipelined Time / Pipelined Time
   
4. Ideal Speedup = Number of Pipeline Stages
   
5. Actual CPI = Ideal CPI + (Load Stalls + Branch Stalls + Structural Stalls)
   
6. Branch Penalty = (Branch frequency) × (Misprediction rate) × (Penalty cycles)
```

### 6.2 Worked Example

**Problem:** A processor has a 5-stage pipeline. 20% of instructions are branches. Branch predictor has 10% misprediction rate with a 2-cycle penalty. Calculate the effective CPI.

**Solution:**
```
Branch frequency = 0.20
Misprediction rate = 0.10
Penalty per mispredict = 2 cycles

Branch stalls = 0.20 × 0.10 × 2 = 0.004 cycles/instruction
Ideal CPI = 1

Effective CPI = 1 + 0.004 = 1.004
```

---

## 7. Key Takeaways

1. **Instruction Cycle**: The fetch-decode-execute cycle is the fundamental process by which CPUs execute instructions, involving multiple phases (IF, ID, EX, MEM, WB).

2. **Pipelining**: Overlaps instruction execution across multiple stages, achieving near-ideal speedup equal to the number of pipeline stages for large instruction sequences.

3. **Hazards**: Three types—structural (hardware conflicts), data (dependencies), and control (branches)—can reduce pipeline efficiency.

4. **Forwarding**: Data forwarding (bypassing) eliminates most RAW data hazards by routing results directly between pipeline stages.

5. **Branch Prediction**: Essential for minimizing control hazard penalties; includes static (predict not taken/taken) and dynamic (1-bit, 2-bit, BTB) methods.

6. **Performance**: Actual CPI accounts for stalls; optimal pipeline design minimizes hazards while maximizing clock frequency.

7. **Real-world Impact**: Modern processors use deep pipelines (10-20+ stages) and superscalar execution, but the fundamental concepts remain the same.

---

## 8. Assessment Questions

### Multiple Choice Questions

**Question 1:** In a classic 5-stage RISC pipeline (IF, ID, EX, MEM, WB), in which stage is the ALU operation performed?
- A) IF
- B) ID
- C) EX
- D) MEM

**Answer:** C) EX. The Execute (EX) stage is where the Arithmetic Logic Unit (ALU) performs arithmetic and logical operations.

---

**Question 2:** Consider a 5-stage pipeline with no hazards. What is the theoretical maximum speedup for processing 1000 instructions?
- A) 5x
- B) 1000x
- C) 995x
- D) 1005x

**Answer:** A) 5x. As n → ∞, the speedup approaches the number of pipeline stages (k). For 1000 instructions: S ≈ (1000 × 5)/(1000 + 5 - 1) ≈ 4.995, approaching 5.

---

**Question 3:** Which type of data hazard occurs when instruction J tries to read a register before instruction I writes to it?
- A) WAR (Write After Read)
- B) WAW (Write After Write)
- C) RAW (Read After Write)
- D) Structural Hazard

**Answer:** C) RAW. This is a true data dependency where the read must occur after the write completes.

---

**Question 4:** A load instruction reads data from memory in which stage of the classic 5-stage pipeline?
- A) IF
- B) ID
- C) EX
- D) MEM

**Answer:** D) MEM. Memory access (read for load, write for store) occurs in the MEM stage.

---

**Question 5:** In a pipeline with forwarding, the result from which pipeline register can be forwarded directly to the EX stage of the dependent instruction?
- A) IF/ID only
- B) ID/EX only
- C) EX/MEM or MEM/WB
- D) Only from MEM/WB

**Answer:** C) EX/MEM or MEM/WB. Forwarding routes results from the output of earlier pipeline stages directly to where they're needed in the EX stage.

---

**Question 6:** What is a branch delay slot?
- A) A hardware buffer that stores branch targets
- B) The position in the pipeline after a branch instruction where useful work can be placed
- C) The time between branch instruction fetch and its execution
- D) A type of branch predictor

**Answer:** B) The position after a branch instruction where an instruction can be executed regardless of whether the branch is taken or not.

---

**Question 7:** A 2-bit saturating branch predictor is in state "01" (weakly not taken). Two consecutive branches are taken. What is the new state?
- A) 00 (strongly not taken)
- B) 01 (weakly not taken)
- C) 10 (weakly taken)
- D) 11 (strongly taken)

**Answer:** C) 10 (weakly taken). With each taken branch: 01→10→11. After one taken branch: 01→10.

---

**Question 8:** Which of the following is NOT a solution to control hazards?
- A) Branch delay slots
- B) Data forwarding
- C) Branch prediction
- D) Pipeline flushing

**Answer:** B) Data forwarding. Data forwarding is a solution for data hazards, not control hazards.

---

**Question 9:** In a load-use hazard, what is typically inserted between the load instruction and the dependent instruction?
- A) Another load instruction
- B) A stall (bubble)
- C) A jump instruction
- D) Nothing needed

**Answer:** B) A stall (bubble). The dependent instruction must wait one cycle because load data is only available after the MEM stage.

---

**Question 10:** If a processor has a clock frequency of 3 GHz and an average CPI of 1.5, what is the MIPS rating?
- A) 2000 MIPS
- B) 1500 MIPS
- C) 4500 MIPS
- D) 3000 MIPS

**Answer:** A) 2000 MIPS. MIPS = (Clock Rate in MHz) / CPI = 3000 MHz / 1.5 = 2000 MIPS.

---

## 9. Flashcards for Quick Review

| # | Term | Definition |
|---|------|------------|
| 1 | Instruction Cycle | The complete process of fetching, decoding, and executing an instruction |
| 2 | Pipeline | Hardware technique overlapping execution of multiple instructions |
| 3 | Structural Hazard | Hardware cannot support all instruction combinations simultaneously |
| 4 | RAW Hazard | Read After Write - true dependency, must wait for write to complete |
| 5 | WAR Hazard | Write After Read - anti-dependency, write before read completes |
| 6 | WAW Hazard | Write After Write - output dependency, writes must occur in order |
| 7 | Forwarding | Routing results directly between pipeline stages, bypassing registers |
| 8 | Branch Penalty | Cycles lost due to branch misprediction or unresolved branches |
| 9 | Pipeline Stall | Pausing pipeline execution to resolve hazards |
| 10 | Bubble/NOP | No-operation instruction inserted to create deliberate pipeline delay |
| 11 | Branch Delay Slot | Instruction slot after branch that executes regardless of branch outcome |
| 12 | BTB | Branch Target Buffer - hardware cache storing branch target addresses |
| 13 | CPI | Cycles Per Instruction - average clock cycles per instruction execution |
| 14 | Clock Cycle Time | Time period of one clock pulse (inverse of clock frequency) |
| 15 | Speedup | Ratio of non-pipelined to pipelined execution time |

---

## 10. References and Further Reading

1. **Computer Organization and Design** - David A. Patterson, John L. Hennessy
2. **Computer Architecture: A Quantitative Approach** - John L. Hennessy, David A. Patterson
3. **MIPS Assembly Language Programming** - Robert Britton
4. **Digital Design and Computer Architecture** - David Harris, Sarah Harris
5. **Delhi University BSc (Hons) CS Syllabus - NEP 2024 UGCF**

---

*This study material is specifically designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum.*