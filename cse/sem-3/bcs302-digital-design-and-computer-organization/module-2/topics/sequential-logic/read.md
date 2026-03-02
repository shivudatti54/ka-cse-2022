# Introduction to Sequential Logic

## Introduction

In combinational circuits, the output depends solely on the present inputs at any given instant. However, practical digital systems—such as computers, counters, registers, and controllers—require **memory** to retain historical information and make decisions based on sequences of events. **Sequential logic** constitutes the class of digital circuits whose outputs depend on both the **current inputs** and the **previous state** (stored history) of the circuit. This fundamental ability to store and recall information distinguishes sequential logic from combinational logic and forms the architectural foundation for all modern computing devices.

## Fundamental Distinction: Combinational vs. Sequential Circuits

The critical difference between combinational and sequential circuits lies in the presence of memory elements and feedback paths.

| Characteristic                | Combinational Circuits                   | Sequential Circuits                           |
| ----------------------------- | ---------------------------------------- | --------------------------------------------- |
| **Memory**                    | No memory elements                       | Contains memory elements (latches/flip-flops) |
| **Output Dependency**         | Present inputs only                      | Present inputs + past state                   |
| **Feedback**                  | No feedback paths                        | Feedback from outputs to inputs               |
| **Time Dependency**           | Instantaneous (time-independent)         | Time-dependent (clocked)                      |
| **Behavioral Representation** | Truth table                              | State table / State diagram                   |
| **Design Complexity**         | Simpler                                  | More complex                                  |
| **Examples**                  | Adders, multiplexers, decoders, encoders | Counters, shift registers, FSMs, memory units |

The inclusion of feedback creates a temporal dimension wherein the circuit's future behavior depends on its history—a property essential for implementing computational memory, control state machines, and synchronization mechanisms.

## Structural Architecture of Sequential Circuits

A sequential circuit comprises two primary components interconnected via feedback:

```
 +------------------+
 Inputs ──────→ │ COMBINATIONAL │ ────────→ Outputs
 │ LOGIC │
 ┌───────→ │ │ ───────┐
 │ +------------------+ │
 │ │
 │ +------------------+ │
 │ │ STORAGE │ │
 └─────────│ ELEMENTS │ ←──────┘
 │ (Memory) │
 Clock ──────→ │ │
 +------------------+
 Present State Next State
```

**Combinational Logic Block:** Computes the next state and output functions based on present state and inputs. Mathematically, if Q represents the present state and X represents inputs:

- Next State: Q⁺ = f(X, Q)
- Output: Z = g(X, Q) [Mealy] or Z = g(Q) [Moore]

**Storage Elements:** Maintain the present state and update to the next state synchronously with clock transitions. These elements—typically latches or flip-flops—implement the memory function.

## Classification: Synchronous vs. Asynchronous Sequential Circuits

### Synchronous Sequential Circuits

In **synchronous sequential circuits**, state transitions occur only at discrete time instants defined by a clock signal. All storage elements (flip-flops) are edge-triggered and update simultaneously on the active clock transition.

**Characteristics:**

- State changes occur only at clock edges (rising or falling)
- All flip-flops share a common clock signal
- Timing analysis is simplified (single clock domain)
- Easier to design, analyze, and debug
- More predictable timing behavior
- Used in CPUs, memory interfaces, and most digital systems

**Timing Constraint:** The minimum clock period TCLK must satisfy:
$$T_{CLK} ≥ t_{pFF} + t_{pCOMB} + t_{su}$$
where t*{pFF} is flip-flop propagation delay, t*{pCOMB} is combinational logic delay, and t\_{su} is setup time.

### Asynchronous Sequential Circuits

In **asynchronous sequential circuits**, state changes can occur at any time when inputs change, without a global clock signal. The circuit operates based on input transitions propagating through the combinational logic.

**Characteristics:**

- No clock signal—changes propagate immediately
- Faster operation (eliminates clock latency)
- Lower power consumption (no switching overhead)
- **Prone to race conditions and hazards**
- More difficult to analyze and design
- Used in handshaking protocols, arbitters, and asynchronous processors

**Critical Issue:** Race conditions occur when multiple inputs change simultaneously, leading to unpredictable state transitions. Hazards (glitches) arise from unequal propagation delays in combinational paths.

## The Clock Signal

The **clock** serves as the global timing reference in synchronous sequential circuits, providing a periodic square wave that synchronizes all state transitions.

```
 ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐
Clock: │ │ │ │ │ │ │ │ │ │
 ───┘ └──┘ └──┘ └──┘ └──┘
 ↑ ↑ ↑ ↑
 Rising edges (positive-edge triggered)

 ───┐ ┌──┐ ┌──┐ ┌──┐ ┌──
 └──┘ └──┘ └──┘ └──┘
 ↑ ↑ ↑ ↑
 Falling edges (negative-edge triggered)
```

**Key Definitions:**

- **Clock Period (T):** Time for one complete clock cycle (seconds)
- **Clock Frequency (f):** f = 1/T, measured in Hertz
- **Duty Cycle:** Percentage of period where clock is HIGH
- **Rising Edge:** Transition from logic 0 to logic 1
- **Falling Edge:** Transition from logic 1 to logic 0

## Storage Elements: Latches and Flip-Flops

Sequential circuits employ two fundamental types of storage elements that differ in their sensitivity to enable signals.

### Latches (Level-Sensitive)

Latches are level-triggered devices that are transparent when the enable (gate) signal is active, allowing data to pass through continuously.

#### SR Latch (Set-Reset Latch)

**Circuit Implementation:** Two cross-coupled NOR gates

**Truth Table:**

| S   | R   | Q (Next State) | Operation     |
| --- | --- | -------------- | ------------- |
| 0   | 0   | Q (No Change)  | Hold          |
| 1   | 0   | 1              | Set           |
| 0   | 1   | 0              | Reset         |
| 1   | 1   | 0 (Invalid)    | Indeterminate |

**Characteristic Equation:** Q⁺ = S + R̄Q, with constraint SR = 0

#### Gated SR Latch

Adds an enable input (E) that controls when the latch is active:

- When E = 1: Functions as SR latch
- When E = 0: Maintains previous state (memory)

#### D Latch (Data Latch)

Eliminates the invalid state by ensuring S and R are complements:

- Q⁺ = D when E = 1
- Q⁺ = Q when E = 0

**Characteristic Equation:** Q⁺ = D·E + Q·Ē = D·E + Q·Ē

### Flip-Flops (Edge-Triggered)

Flip-flops capture input values only at specific clock transitions, providing definite timing boundaries essential for synchronous design.

#### D Flip-Flop

**Operation:** Transfers input D to output Q on the active clock edge.

**Characteristic Table:**

| D   | Q (Current) | Q⁺ (Next) |
| --- | ----------- | --------- |
| 0   | X           | 0         |
| 1   | X           | 1         |

**Characteristic Equation:** Q⁺ = D

**Excitation Table (for circuit analysis):**

| Q   | Q⁺  | D Required |
| --- | --- | ---------- |
| 0   | 0   | 0          |
| 0   | 1   | 1          |
| 1   | 0   | 0          |
| 1   | 1   | 1          |

#### JK Flip-Flop

**Operation:** Universal flip-flop with toggle capability.

**Characteristic Table:**

| J   | K   | Q⁺  | Operation |
| --- | --- | --- | --------- |
| 0   | 0   | Q   | Hold      |
| 0   | 1   | 0   | Reset     |
| 1   | 0   | 1   | Set       |
| 1   | 1   | Q̄   | Toggle    |

**Characteristic Equation:** Q⁺ = J·Q̄ + K̄·Q

#### T Flip-Flop

**Operation:** Toggles output when T = 1.

**Characteristic Table:**

| T   | Q⁺  | Operation |
| --- | --- | --------- |
| 0   | Q   | Hold      |
| 1   | Q̄   | Toggle    |

**Characteristic Equation:** Q⁺ = T ⊕ Q = T·Q̄ + T̄·Q

### Master-Slave Flip-Flop Construction

Edge-triggered behavior is achieved by cascading two level-sensitive latches:

- **Master latch:** Operates when clock is HIGH
- **Slave latch:** Operates when clock is LOW
- Output changes only on clock edge transition

## State Representation: Tables and Diagrams

Sequential circuit behavior is formally described using state tables and state diagrams.

### State Table

A state table explicitly lists all possible present states, inputs, next states, and outputs.

**Example: Modulo-3 Counter**

| Present State (Q₁Q₀) | Next State (Q₁⁺Q₀⁺) | Output (Y) |
| :------------------: | :-----------------: | :--------: |
|          00          |         01          |     0      |
|          01          |         10          |     0      |
|          10          |         00          |     1      |

### State Diagram

A graphical representation with circles (states) and directed edges (transitions labeled with input/output).

```
 0/0 0/0 1/1
 ┌────────┐ ┌────────┐ ┌────────┐
 │ S0 │──→ │ S1 │──→ │ S2 │
 └────────┘ └────────┘ └────────┘
 ↑ ↓
 └────────────────────────────────────┘
 1/0
```

## Finite State Machine Models

### Moore Machine

**Output depends solely on the present state.**

- Output is associated with each state
- Output changes only on clock edges (when state changes)
- Generally has more states than equivalent Mealy machine
- Used in applications where output timing is critical

**Formal Definition:** Z: Q → O (output function maps states to outputs)

### Mealy Machine

**Output depends on both present state and current inputs.**

- Output is associated with each state transition
- Output can change asynchronously with input changes
- Often requires fewer states than Moore machine
- More responsive to input changes

**Formal Definition:** Z: Q × X → O (output function maps state-input pairs to outputs)

## Timing Analysis

Synchronous sequential circuits must satisfy critical timing constraints to ensure reliable operation.

### Setup and Hold Times

- **Setup Time (t_su):** Minimum time input must be stable before clock edge
- **Hold Time (t_h):** Minimum time input must remain stable after clock edge

**Constraint Violation:** If setup or hold times are violated, the flip-flop may enter a metastable state with unpredictable output.

### Maximum Clock Frequency

For a synchronous circuit with propagation delays:

$$f_{MAX} = \frac{1}{T_{CLK(min)}} = \frac{1}{t_{pFF} + t_{pCOMB} + t_{su}}$$

**Example Calculation:** Given t*{pFF} = 2ns, t*{pCOMB} = 8ns, t*{su} = 1ns:
$$T*{CLK(min)} = 2 + 8 + 1 = 11ns$$
$$f\_{MAX} ≈ 90.9 MHz$$

## Key Concepts Summary

1. **Memory Property:** Sequential circuits maintain history through feedback paths
2. **Structural Components:** Combinational logic + storage elements + feedback
3. **Synchronous Operation:** Clocked state changes at discrete intervals
4. **Asynchronous Operation:** Immediate response to input changes (race-prone)
5. **Storage Elements:** Latches (level-sensitive) vs. Flip-flops (edge-triggered)
6. **State Representation:** State tables and state diagrams formally describe behavior
7. **FSM Models:** Moore (output = f(state)) vs. Mealy (output = f(state, input))
8. **Timing Constraints:** Setup time, hold time, and maximum clock frequency

### Further Reading

Consult prescribed textbooks for detailed coverage of sequential circuit design methodology, state minimization techniques, and HDL implementation.
