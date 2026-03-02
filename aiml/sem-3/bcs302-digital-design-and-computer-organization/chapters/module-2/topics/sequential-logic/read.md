# Sequential Logic: The Foundation of Stateful Digital Systems

## Introduction

In **Digital Design and Computer Organization**, Module 1 introduced **combinational logic**—circuits whose outputs depend solely on their current inputs. **Sequential logic**, the focus of Module 2, is the crucial next step. These are circuits whose outputs depend on both the *current inputs* and the *past sequence of inputs*. This "memory" of past events is what allows digital systems to have state, enabling them to perform complex operations like counting, storing data, and controlling the flow of operations—the very essence of a computer's organization.

## Core Concepts

### 1. The Basic Building Block: The Flip-Flop

The fundamental unit of memory in sequential circuits is the **flip-flop (FF)**. It is a bistable multivibrator, meaning it has two stable states (`0` and `1`) and can remain in one state indefinitely until directed to change.

The most common and fundamental type is the **D-type Flip-Flop (Data FF)**.
*   **Inputs:** `D` (Data input), `CLK` (Clock input).
*   **Outputs:** `Q`, `Q'` (complement of Q).
*   **Function:** On the active edge (usually the rising edge) of the clock signal, the value present at the `D` input is latched and appears at the `Q` output. The output `Q` holds this value until the next active clock edge.

This clock signal synchronizes changes in the circuit's state, preventing instability and chaos, making it a **synchronous sequential circuit**.

### 2. The Concept of State

The "state" of a sequential circuit is the collective value stored in all its memory elements (flip-flops) at a given time. The circuit's output and its next state are a function of its **current state** and its **current inputs**.

### 3. State Tables and State Diagrams

To design and analyze sequential circuits, we use specific tools:
*   **State Table:** A tabular representation that shows for every possible combination of current state and inputs, what the next state and outputs will be.
*   **State Diagram:** A graphical representation where circles represent states and directed arcs represent transitions between states based on inputs and outputs. It provides an intuitive view of the circuit's behavior.

### 4. Registers and Counters: Fundamental Sequential Circuits

*   **Register:** A group of D flip-flops used to store a multi-bit binary value (e.g., a byte or a word). All flip-flops share a common clock signal, so the entire register loads data simultaneously.
*   **Counter:** A sequential circuit that cycles through a predefined sequence of states. A simple **modulo-N counter** counts from `0` to `N-1` and then resets. Counters are essential for generating addresses, keeping track of time, and controlling operations.

## Example: A Simple 2-Bit Counter

Let's design a circuit that counts in the sequence: 00 → 01 → 10 → 11 → 00...

1.  **Define States:** The count value *is* the state. We need two flip-flops (`A` and `B`) to represent the four states (00, 01, 10, 11).
2.  **Create a State Table:**

| Present State | Next State |
| :-----------: | :--------: |
|      A B      |    A B     |
|      0 0      |    0 1     |
|      0 1      |    1 0     |
|      1 0      |    1 1     |
|      1 1      |    0 0     |

3.  **Determine Flip-Flop Inputs:** We use D flip-flops. For a D-FF, `D = Next State`. So, we need to find the logic for `D_A` and `D_B` based on the present state (`A` and `B`).

    From the table:
    *   `D_A = A'B + AB'`  (This is an XOR function)
    *   `D_B = B'`

4.  **Implement the Circuit:** The circuit would consist of two D flip-flops. The `D` input of the first FF (`B`) is connected to `B'`. The `D` input of the second FF (`A`) is connected to the output of an XOR gate whose inputs are `A` and `B`. A clock signal drives both flip-flops.

## Key Points & Summary

*   **Core Difference:** Combinational logic has no memory; sequential logic *does* have memory (state).
*   **Fundamental Element:** The flip-flop is the basic 1-bit memory cell. The D Flip-Flop is the most common building block.
*   **Synchronization:** The clock signal is critical for synchronizing state changes in most sequential circuits, making them predictable and reliable.
*   **State Representation:** The behavior of sequential circuits is defined by their state, which can be modeled using state tables and state diagrams.
*   **Essential Components:** Registers (for storage) and counters (for sequencing) are two of the most vital sequential circuits in computer organization, forming the basis for memory units, ALU control, and program counters.
*   **Foundation for Computing:** Understanding sequential logic is paramount for grasping how a CPU manages instructions, stores temporary data, and controls the flow of execution—all of which are stateful processes.