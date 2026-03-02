# Pipeline Performance

## Introduction

Pipeline performance analysis constitutes a fundamental pillar in the study of computer organization and architecture. Pipelining represents an implementation technique that enables overlapping the execution of multiple instructions through a processor pipeline, thereby achieving substantial improvements in instruction throughput. This technique transforms the traditional sequential execution model into a parallel processing paradigm, where different instructions reside in various stages of execution simultaneously during each clock cycle.

The theoretical foundation of pipelining rests upon the principle of dividing the instruction execution process into discrete, balanced stages, each consuming approximately equal time. When properly implemented, a pipeline achieves throughput approaching one instruction per clock cycle, representing the maximum theoretical throughput for a perfectly balanced pipeline. The study of pipeline performance encompasses mathematical formulations for speedup, efficiency, and throughput, along with the analysis of pipeline hazards that inevitably degrade ideal performance in practical implementations.

This module provides a rigorous treatment of pipeline performance metrics, including formal derivations of key relationships, comprehensive analysis of pipeline hazards and their mitigation strategies, and quantitative performance evaluation using the cycles-per-instruction (CPI) metric. The mathematical foundations presented herein are essential for understanding modern processor design and for solving complex numerical problems encountered in university examinations and competitive assessments.

## Key Concepts

### Basic Pipeline Organization

A pipeline processor organizes instruction execution into a sequence of stages, where each stage completes a specific portion of the instruction's lifecycle. The classic RISC five-stage pipeline exemplifies this organization:

**Stage 1 - Instruction Fetch (IF):** The instruction is fetched from memory using the program counter (PC). The PC is incremented to point to the subsequent instruction.

**Stage 2 - Instruction Decode (ID):** The instruction is decoded to determine the operation type, and register operands are read from the register file.

**Stage 3 - Execute (EX):** The arithmetic logic unit (ALU) performs the specified operation, including effective address calculation for memory operations.

**Stage 4 - Memory Access (MEM):** For load and store instructions, data is transferred between the processor and memory. Branch decisions are resolved in this stage.

**Stage 5 - Write Back (WB):** The result, either from the ALU operation or memory, is written back to the destination register.

Pipeline registers are inserted between consecutive stages to hold intermediate results and control signals, ensuring data integrity as instructions propagate through the pipeline. These registers introduce a small overhead but are essential for maintaining correct pipeline operation.

### Performance Metrics: Mathematical Foundation

#### Speedup Factor

The speedup factor quantifies the performance improvement achieved by pipelining relative to sequential (non-pipelined) execution. Consider a processor executing n instructions with a pipeline having k stages, where each stage requires one clock cycle of time τ.

**Non-pipelined execution time:**
In a non-pipelined processor, each instruction requires k clock cycles to complete. Therefore, the total execution time for n instructions is:

T<sub>n</sub> = n × k × τ

**Pipelined execution time:**
In a pipelined processor, the first instruction emerges after k cycles (the pipeline fill time), and subsequent instructions complete at a rate of one per cycle. Thus:

T<sub>p</sub> = (k + n - 1) × τ

**Speedup factor (S):**
S = T<sub>n</sub> / T<sub>p</sub> = (n × k × τ) / [(k + n - 1) × τ]
S = (n × k) / (k + n - 1)

**Proof of Maximum Speedup:**
To determine the limiting behavior as the number of instructions approaches infinity, we analyze the limit:

lim<sub>n→∞</sub> S = lim<sub>n→∞</sub> (n × k) / (k + n - 1)

Dividing numerator and denominator by n:

= lim<sub>n→∞</sub> k / (k/n + 1 - 1/n)

As n → ∞, k/n → 0, therefore:

lim<sub>n→∞</sub> S = k / 1 = k

**Theorem:** The maximum theoretical speedup achievable by a k-stage pipeline equals k, the number of pipeline stages.

This result establishes that a five-stage pipeline cannot achieve speedup exceeding five, regardless of the number of instructions executed. This limitation arises from the pipeline fill and drain overhead affecting a finite number of instructions.

#### Pipeline Efficiency

Pipeline efficiency (E) measures the ratio of actual speedup achieved to the theoretical maximum speedup:

E = S / k = [(n × k) / (k + n - 1)] / k = n / (k + n - 1)

Expressed as a percentage:

E(%) = [n / (k + n - 1)] × 100

**Proof of Efficiency Limit:**
Taking the limit as n approaches infinity:

lim<sub>n→∞</sub> E = lim<sub>n→∞</sub> n / (k + n - 1) = lim<sub>n→∞</sub> 1 / (k/n + 1 - 1/n) = 1

Therefore, efficiency approaches 100% (or 1.0) as the number of instructions becomes large. The efficiency formula reveals that:

1. For small n relative to k, efficiency is significantly reduced due to pipeline fill/drain overhead
2. For n >> k, efficiency approaches the ideal value of 100%
3. The efficiency formula provides a direct measure of pipeline utilization

#### Throughput

Throughput (TP) represents the rate at which instructions are completed, measured in instructions per unit time:

**Ideal throughput (per cycle):**
TP<sub>ideal</sub> = 1 instruction per cycle = 1/τ

**Practical throughput considering stalls:**
TP<sub>practical</sub> = 1 / CPI<sub>actual</sub> × τ

Throughput is commonly expressed in MIPS (Million Instructions Per Second) or, for floating-point intensive applications, MFLOPS (Million Floating Point Operations Per Second):

MIPS = (Clock Rate in MHz) / CPI

#### Latency vs. Throughput

**Latency:** The total time required to complete a single instruction from initiation to termination. In a k-stage pipeline, the latency of one instruction is k × τ.

**Throughput:** The number of instructions completed per unit time. The ideal throughput is 1/τ instructions per cycle.

The critical distinction: A pipeline reduces latency for subsequent instructions in the sequence (since they overlap), but the first instruction's latency remains k × τ. Throughput improves because multiple instructions are in various stages of execution simultaneously.

### Pipeline Hazards

Pipeline hazards are conditions that prevent the next instruction from entering the pipeline in the designated cycle, causing stalls that degrade performance below the theoretical maximum. Three principal hazard types exist:

#### Structural Hazards

Structural hazards arise when hardware resources are insufficient to support all combinations of instructions in the pipeline simultaneously. This occurs when the processor lacks sufficient functional units or when resources cannot be shared among pipeline stages.

**Example:** If the processor contains only one ALU, it cannot execute the EX stage of instruction i+1 while simultaneously performing the MEM stage of instruction i if both require the ALU.

**Resolution techniques:**

1. **Resource duplication:** Add additional hardware units (e.g., multiple memory ports, additional ALUs)
2. **Stalling:** Insert bubble cycles until the resource becomes available
3. **Scheduling:** Rearrange instructions to avoid resource conflicts (not applicable to in-order execution)

#### Data Hazards

Data hazards occur when instructions executing concurrently access the same data, and the execution order differs from the program order. Three subtypes exist:

**1. Read After Write (RAW) - True Data Dependency:**
This hazard occurs when instruction j attempts to read a register before instruction i writes to it. The read obtains an incorrect (stale) value.

_Example:_

```
I1: ADD R1, R2, R3 // R1 ← R2 + R3
I2: SUB R4, R1, R5 // R2: R4 ← R1 - R5 (should use new value of R1)
```

Instruction I2 reads R1 before I1 writes the result, causing incorrect computation.

**2. Write After Read (WAR) - Anti-Dependency:**
This hazard occurs when instruction j attempts to write to a register before instruction i reads it. The read obtains an incorrect (overwritten) value.

_Example:_

```
I1: ADD R1, R2, R3 // R1 ← R2 + R3
I2: SUB R2, R4, R5 // R2 ← R4 - R5 (overwrites before I1 reads R2)
```

WAR hazards cannot occur in in-order pipelines with scoreboarding because reads always precede writes in program order. However, they may arise in out-of-order execution.

**3. Write After Write (WAW) - Output Dependency:**
This hazard occurs when instruction j attempts to write to a register before instruction i writes to it. The final value differs from program order.

_Example:_

```
I1: ADD R1, R2, R3 // R1 ← R2 + R3
I2: SUB R1, R4, R5 // R1 ← R4 - R5 (should be final value)
```

WAW hazards are prevented in in-order pipelines but may occur in out-of-order execution.

**Hazard Resolution Techniques:**

**a) Data Forwarding (Bypassing):**
Forwarding routes the result directly from the output of one pipeline stage to the input of another, bypassing the register file. For RAW hazards, the result from the EX/MEM pipeline register of instruction i is forwarded to the ALU input for instruction j.

**b) Stall Insertion (Pipeline Interlocking):**
Hardware inserts bubble cycles until the dependency is resolved. This simplifies hardware design but degrades performance.

**c) Compiler Scheduling:**
The compiler rearranges independent instructions to fill delay slots, reducing stall cycles.

#### Control Hazards

Control hazards arise from conditional and unconditional branch instructions. The processor cannot determine the next instruction address until the branch is resolved, causing pipeline stalls.

**Branch Penalty:**
If the branch decision requires k cycles, the pipeline must stall for k-1 cycles (assuming the first instruction of the branch path is fetched in cycle k).

**Example:** In a 5-stage pipeline where branch outcome is known in MEM stage (3-cycle delay):

- 3 bubble cycles must be inserted if branch is mispredicted

**Resolution Techniques:**

**a) Branch Prediction:**

- Static prediction: Always predict taken or not-taken (typically 67% accuracy for backward branches)
- Dynamic prediction: Uses runtime information (branch history table)

**b) Delayed Branch:**
The compiler inserts independent instructions in the branch delay slot, ensuring useful work during branch resolution.

**c) Branch Target Buffer (BTB):**
A hardware cache storing branch target addresses and prediction bits for faster resolution.

### Pipeline Stall Analysis and CPI

When hazards cannot be fully resolved, the pipeline incurs stalls, increasing the effective cycles per instruction:

**Effective CPI Formula:**
CPI<sub>pipeline</sub> = CPI<sub>ideal</sub> + Σ (fraction<sub>i</sub> × penalty<sub>i</sub>)

Where:

- CPI<sub>ideal</sub> = 1 for an ideal pipeline
- fraction<sub>i</sub> = fraction of instructions experiencing hazard type i
- penalty<sub>i</sub> = stall cycles for hazard type i

**Example Calculation:**
For a 5-stage pipeline:

- Base CPI = 1
- 30% branch instructions with 2-cycle penalty
- 20% load instructions with 1-cycle penalty (data hazard)

Branch penalty = 0.30 × 2 = 0.60 cycles
Load penalty = 0.20 × 1 = 0.20 cycles

CPI<sub>actual</sub> = 1 + 0.60 + 0.20 = 1.80

Speedup = CPI<sub>ideal</sub> / CPI<sub>actual</sub> = 5 / 1.80 ≈ 2.78

This represents significant degradation from the theoretical maximum speedup of 5.

---

## Summary

Pipeline performance analysis provides the mathematical framework for evaluating processor efficiency. The key relationships establish that maximum speedup equals the number of pipeline stages (k), achieved only in the asymptotic limit of infinite instructions. Pipeline efficiency measures actual utilization relative to this theoretical maximum. Three hazard types—structural, data, and control—degrade performance by introducing stall cycles. Modern processors employ sophisticated mitigation techniques including forwarding, branch prediction, and dynamic scheduling to approximate ideal pipeline performance. The effective CPI metric integrates all factors affecting pipeline efficiency, enabling quantitative comparison of different pipeline designs and hazard mitigation strategies.
