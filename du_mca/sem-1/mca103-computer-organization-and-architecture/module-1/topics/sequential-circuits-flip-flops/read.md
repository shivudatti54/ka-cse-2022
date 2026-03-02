# Sequential Circuits & Flip-Flops

## Introduction
Sequential circuits form the backbone of digital systems' memory capabilities. Unlike combinational circuits whose outputs depend only on current inputs, sequential circuits incorporate memory elements that enable output dependence on both current inputs and previous states. This fundamental property makes them essential for building registers, counters, and control units in modern processors.

Flip-flops serve as the basic building blocks of sequential circuits. These bistable multivibrators maintain their state until directed by clock signals to change, enabling controlled data storage and transfer. The evolution from basic SR flip-flops to more sophisticated JK and D flip-flops reflects their critical role in addressing real-world challenges like race conditions and metastability in high-speed computing systems.

In contemporary computer architecture, mastery of sequential circuits is crucial for designing:
- CPU registers and cache memory
- State machines in control units
- Clock domain crossing circuits
- I/O interface controllers

## Key Concepts

**1. Sequential Circuit Classification**
- *Synchronous*: State changes synchronized with clock edges
- *Asynchronous*: State changes triggered by input changes (no global clock)

**2. Flip-Flop Types**
- **SR Flip-Flop**: Basic Set-Reset configuration with NOR/NAND gates
  - Truth Table:
    | S | R | Q(t+1) |
    |---|---|--------|
    | 0 | 0 | Q(t)   |
    | 0 | 1 | 0      |
    | 1 | 0 | 1      |
    | 1 | 1 | Invalid|

- **JK Flip-Flop**: Eliminates SR's invalid state using feedback
  - Characteristic Equation: Q(t+1) = JQ' + K'Q

- **D Flip-Flop**: Single input design for data storage
  - Q(t+1) = D (on clock edge)

- **T Flip-Flop**: Toggle functionality for counting applications
  - Q(t+1) = T ⊕ Q

**3. Timing Parameters**
- Setup Time (t<sub>su</sub>): Minimum time data must be stable before clock edge
- Hold Time (t<sub>h</sub>): Minimum time data must remain stable after clock edge
- Clock-to-Q Delay (t<sub>cq</sub>): Propagation delay from clock edge to output

**4. Metastability**
- Occurs when setup/hold times are violated
- Resolved using synchronizer chains in multi-clock domain systems

## Examples

**Example 1: D Flip-Flop Based Shift Register**
*Problem*: Design 4-bit serial-in parallel-out register using positive-edge triggered DFFs

*Solution*:
1. Connect D1 input to serial data line
2. Q1 output → D2 input
3. Q2 → D3, Q3 → D4
4. All flip-flops share common clock
5. After 4 clock cycles, parallel outputs (Q1-Q4) contain stored data

**Example 2: JK Flip-Flop Mod-3 Counter**
*Problem*: Implement synchronous counter with sequence 0→1→2→0...

*Solution*:
1. State Table:
   | Present State | Next State |
   |---------------|------------|
   | 00            | 01         |
   | 01            | 10         |
   | 10            | 00         |

2. K-Map simplification for J/K inputs:
   J1 = Q0, K1 = 1
   J0 = Q1', K0 = 1

3. Circuit implementation with two JK flip-flops

## Exam Tips
1. Always draw timing diagrams with clear clock edges and propagation delays
2. For state machine design problems:
   - Start with state diagram
   - Derive excitation tables
   - Use K-maps for logic minimization
3. Setup/Hold time calculations often involve checking t<sub>su</sub> ≤ T - t<sub>cq</sub> - t<sub>comb</sub>
4. Master-Slave flip-flops eliminate transparency but introduce ½ cycle delay
5. Remember characteristic equations for each flip-flop type:
   - D: Q+ = D
   - T: Q+ = T ⊕ Q
   - JK: Q+ = JQ' + K'Q
6. For asynchronous counters, propagation delay accumulates creating ripple effect
7. Always check for invalid states in finite state machines and implement self-correcting logic