# Instruction Cycle and Pipelining
## BSc (Hons) Computer Science - Delhi University (NEP 2024 UGCF)

### Introduction
The **Instruction Cycle** is the fundamental process by which CPUs execute instructions, while **Pipelining** is an optimization technique used to improve throughput. These concepts are core to understanding processor architecture and performance.

---

### Instruction Cycle (Fetch-Decode-Execute)

The CPU executes instructions through a series of steps called the **Instruction Cycle**:

- **Fetch (F)**: 
  - Instruction is fetched from memory into the Instruction Register (IR)
  - Program Counter (PC) is incremented
  
- **Decode (D)**: 
  - Instruction is decoded to determine operation
  - Operand addresses are calculated
  
- **Fetch Operands (FO)**: 
  - Required data is fetched from memory/registers
  
- **Execute (EX)**: 
  - ALU performs the operation
  
- **Store Result (S)**: 
  - Result is stored back to memory/register

> **Note**: Basic 3-step cycle = Fetch → Decode → Execute (may vary based on architecture)

**Timing**: Each step typically takes **one clock cycle**. Complex instructions may require multiple cycles.

---

### Pipelining

Pipelining is a technique that **overlaps** the execution of multiple instructions to improve throughput.

**Key Concepts:**

- **Pipeline Stages**: Dividing instruction execution into discrete stages (e.g., 5-stage: IF, ID, EX, MEM, WB)
- **Speedup**: Achieved by processing multiple instructions simultaneously in different stages
- **Throughput**: Number of instructions completed per unit time

**Pipeline Hazards** (Problems):

- **Structural Hazards**: Hardware cannot support all instruction combinations simultaneously
- **Data Hazards**: Instructions depend on results of previous instructions
  - *Solutions*: Data forwarding, stalling, NOPs
- **Control Hazards**: Caused by branch instructions
  - *Solutions*: Branch prediction, delay slots

**Speedup Formula:**
$$Speedup = \frac{\text{Execution time without pipeline}}{\text{Execution time with pipeline}}$$

理想情况下，k-stage pipeline 可达到 k 倍加速（但受 hazards 和 branch 影响）。

---

### Conclusion
The instruction cycle forms the basic operational model of the CPU, while pipelining is a crucial performance optimization technique. Understanding the fetch-decode-execute phases and pipeline hazards is essential for exam success and comprehending modern processor design.

---

*Reference: Delhi University BSc (Hons) CS Syllabus - Computer System Architecture Unit*