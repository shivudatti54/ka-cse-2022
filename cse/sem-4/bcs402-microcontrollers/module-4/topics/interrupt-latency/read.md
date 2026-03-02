# Interrupt Latency in Microcontrollers

## Table of Contents

- [Interrupt Latency in Microcontrollers](#interrupt-latency-in-microcontrollers)
- [Introduction](#introduction)
- [Theoretical Framework](#theoretical-framework)
  - [Mathematical Model of Interrupt Latency](#mathematical-model-of-interrupt-latency)
  - [Quantitative Analysis: 8051 Microcontroller](#quantitative-analysis-8051-microcontroller)
  - [ARM Cortex-M Interrupt Latency Analysis](#arm-cortex-m-interrupt-latency-analysis)
  - [Factors Affecting Interrupt Latency](#factors-affecting-interrupt-latency)
- [Optimization Techniques](#optimization-techniques)
  - [Mathematical Analysis of Optimization Strategies](#mathematical-analysis-of-optimization-strategies)
- [Worst-Case vs. Statistical Analysis](#worst-case-vs-statistical-analysis)
- [Summary](#summary)

## Introduction

Interrupt latency is a fundamental parameter in real-time embedded systems that determines the temporal responsiveness of a microcontroller to asynchronous events. In safety-critical applications including automotive engine control units, industrial programmable logic controllers, and medical device pacemakers, the deterministic behavior of interrupt response times directly impacts system safety and reliability. This chapter provides a rigorous examination of interrupt latency from theoretical foundations through quantitative analysis, aligned with the engineering/students/students curriculum requirements for embedded systems design.

Interrupt latency (τ_latency) is formally defined as the time interval between the assertion of an interrupt request (IRQ) signal and the execution of the first instruction of the corresponding interrupt service routine (ISR). Mathematically, this can be expressed as:

τ_latency = τ_detection + τ_completion + τ_context_save + τ_vector_fetch + τ_isr_entry

Where each component represents discrete temporal overhead within the interrupt response mechanism. Understanding these components enables embedded system designers to perform worst-case execution time (WCET) analysis essential for real-time system certification.

## Theoretical Framework

### Mathematical Model of Interrupt Latency

The total interrupt latency in a microcontroller system comprises five primary components, each of which can be analyzed quantitatively:

**1. Detection Latency (τ_detection)**: This represents the time interval between the physical occurrence of an interrupt event and the point at which the processor core recognizes the interrupt request. In systems with peripheral interrupt controllers (PICs), this includes the propagation delay through the interrupt routing logic. For edge-triggered interrupts, τ_detection depends on the sampling rate of interrupt pins, typically equal to one or two clock cycles in synchronous designs.

**2. Completion Latency (τ_completion)**: Processors cannot preempt instructions mid-execution; therefore, the currently executing instruction must complete before interrupt handling begins. This component varies significantly based on instruction complexity. Let n represent the maximum number of clock cycles required by any instruction in the instruction set architecture (ISA). For a CISC processor like 8051:

- Simple instructions (MOV, ADD): 1-2 machine cycles
- Complex instructions (MUL, DIV): 4-12 machine cycles
- Where one machine cycle = 12 oscillator periods in standard 8051

For RISC architectures like ARM Cortex-M, τ_completion is more deterministic since most instructions execute in single-cycle fashion, with load-store operations requiring 2 cycles.

**3. Context Saving Latency (τ_context_save)**: Before transferring control to the ISR, the processor must preserve the current execution context. This typically involves saving the program counter (PC), status register (xPSR), and general-purpose registers. In ARM Cortex-M, the hardware automatically pushes an 8-register stack frame (R0-R3, R12, LR, PC, xPSR) requiring 8 clock cycles. Additional software context saving adds overhead proportional to the number of additional registers preserved.

**4. Vector Fetch Latency (τ_vector_fetch)**: The processor must fetch the interrupt vector address from the vector table and load the program counter with the ISR entry point. In ARM Cortex-M processors, this vector fetch requires 3 clock cycles for a new instruction fetch from flash memory, assuming zero wait states.

**5. ISR Entry Latency (τ_isr_entry)**: The initial instructions of the ISR itself incur overhead for additional register saves (beyond hardware-saved registers), stack pointer adjustments, and possible branch prediction initialization. This typically requires 2-4 clock cycles.

### Quantitative Analysis: 8051 Microcontroller

The 8051 microcontroller provides an excellent case study for interrupt latency calculation due to its variable instruction timing. Consider an 8051 system operating at 12 MHz (T_osc = 83.33 ns):

Given worst-case conditions:

- Maximum instruction completion: 12 machine cycles (DIV instruction)
- Interrupt acknowledgment: 2 machine cycles
- Context saving (4 register banks × 2 cycles each for PUSH operations): 8 machine cycles
- Vector fetch: 2 machine cycles

Total worst-case latency = (12 + 2 + 8 + 2) machine cycles
= 24 machine cycles
= 24 × 12 × 83.33 ns
= 24 μs (approximately)

Minimum latency (simple instruction in progress):

- Completion: 1 machine cycle
- Acknowledgment: 2 machine cycles
- Context save: 4 machine cycles
- Vector: 2 machine cycles
- Total: 9 machine cycles = 9 μs

### ARM Cortex-M Interrupt Latency Analysis

Modern ARM Cortex-M processors implement advanced interrupt handling mechanisms that substantially reduce latency compared to classical architectures. The Nested Vectored Interrupt Controller (NVIC) provides hardware interrupt nesting and priority resolution.

**Tail-Chaining Optimization**: When an interrupt of higher priority arrives while another ISR is executing, Cortex-M processors employ tail-chaining to eliminate redundant stack operations. Rather than popping the current ISR context and pushing a new one, the processor directly transitions between ISR handlers, reducing latency by approximately 12 clock cycles.

**Late Arrival Optimization**: If a higher-priority interrupt arrives within 6 clock cycles of a lower-priority ISR entry, the processor services the higher-priority interrupt first without additional overhead.

**Latency Calculation for ARM Cortex-M4 (16 MHz with Flash wait states)**:

| Component                      | Clock Cycles  |
| ------------------------------ | ------------- |
| Detection + Acknowledge        | 4             |
| Instruction completion (worst) | 2             |
| Hardware stack frame save      | 8             |
| Vector fetch                   | 3             |
| Additional ISR entry           | 2             |
| **Total WCET**                 | **19 cycles** |

At 16 MHz: τ_latency = 19 × 62.5 ns = 1.1875 μs

### Factors Affecting Interrupt Latency

**Instruction Pipeline Effects**: In pipelined processors, interrupt latency increases when the interrupt occurs mid-pipeline. The processor must flush instructions after the interrupted point and refill the pipeline for the ISR. ARM Cortex-M3/M4 employ a 3-stage pipeline, meaning interrupts typically incur a 3-cycle penalty for pipeline refill.

**Memory Wait States**: Flash memory access times significantly impact vector fetch latency. For a Cortex-M running at 100 MHz with 2 wait-state flash:

- Vector fetch: 3 cycles × (1 + wait_states) = 9 cycles
- This demonstrates why many MCUs use instruction cache to mitigate flash latency

**Interrupt Priority and Masking**: Higher priority interrupts can preempt lower priority ones, but the NVIC requires 3-4 cycles to update the priority mask register. When global interrupt enable (I bit in PRIMASK) is set, additional latency occurs until the processor recognizes the interrupt.

**Critical Section Impact**: When interrupts are disabled (via CPSID instruction in ARM or CLR EA in 8051), pending interrupts remain queued until re-enabling. If a critical section executes for N clock cycles, this N cycles directly adds to the effective latency of any interrupt occurring during this period.

## Optimization Techniques

### Mathematical Analysis of Optimization Strategies

**1. Interrupt Nesting**: Enabling nested interrupts reduces effective latency for high-priority events by allowing preemption of lower-priority ISRs. However, this increases stack complexity. The effective latency for priority P interrupts becomes:

τ_effective(P) = τ_isr_low(P) + τ_preempt(P, higher)

Where τ_isr_low is the time spent in lower-priority ISRs that can be preempted.

**2. Register Banking (8051)**: The 8051 provides four register banks (32 registers total). By selecting an alternate register bank at ISR entry using the PSW register, context switching requires only 1 cycle (SETB PSW.3 or PSW.4) rather than 8+ PUSH operations. Speedup factor: approximately 8× for context save operations.

**3. ISR Optimization through Inline Functions**: Placing critical code directly in the ISR eliminates function call overhead. Mathematical analysis: If function call overhead is C cycles and the ISR executes N critical instructions, the overhead ratio is C/(C+N). Minimizing C improves real-time responsiveness.

**4. Memory Alignment for Vector Tables**: Placing the vector table in zero-wait-state memory (SRAM or flash) reduces τ_vector_fetch. For systems with external flash, copying vectors to SRAM during boot can reduce latency by 50-70%.

## Worst-Case vs. Statistical Analysis

Real-time systems require WCET analysis, but statistical characterization provides useful design insights:

- **Worst-Case Latency**: Maximum possible latency under all conditions, used for schedulability analysis
- **Average-Case Latency**: Expected latency computed from instruction mix probability distributions
- **Jitter**: Variation in latency between interrupt occurrences, critical for control loop stability

For a typical 8051 system executing a mix of instructions (60% 1-cycle, 30% 2-cycle, 10% 4-cycle), the statistical average completion latency is:
τ_avg_completion = 0.6(1) + 0.3(2) + 0.1(4) = 1.4 cycles

This contrasts with WCET of 12 cycles, demonstrating the importance of probabilistic analysis for system optimization while maintaining deterministic guarantees.

## Summary

Interrupt latency represents a critical figure of merit in embedded system design, comprising detection, completion, context saving, vector fetch, and ISR entry components. Quantitative analysis reveals significant architectural differences: 8051 exhibits variable latency (9-24 machine cycles) due to complex instruction timing, while ARM Cortex-M provides more deterministic behavior (approximately 19 cycles worst-case) with optimizations like tail-chaining. Mathematical modeling enables precise latency calculation essential for real-time schedulability analysis. Optimization techniques including interrupt nesting, register banking, and memory alignment directly impact system responsiveness. For examination purposes, students must be able to calculate total latency given component timings, analyze trade-offs between optimization techniques, and determine worst-case scenarios for safety-critical applications.
