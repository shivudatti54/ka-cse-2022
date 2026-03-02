# Module 2: Sequential Circuits

## 1. Introduction

In the previous module, we explored **combinational circuits**, where the output depends solely on the *current combination of inputs*. In this module, we shift our focus to **sequential circuits**, a fundamental building block for all modern computing systems. Unlike combinational logic, the output of a sequential circuit depends not only on the present inputs but also on the *past sequence of inputs*. This "memory" of past events allows sequential circuits to perform complex operations like counting, storing data, and controlling the flow of information, forming the basis of finite state machines, registers, and memory units.

## 2. Core Concepts

### 2.1. The Basic Building Block: The Flip-Flop

The fundamental memory element in sequential circuits is the **flip-flop**. It is a bistable device capable of storing one binary bit (a 0 or a 1). The most basic type of flip-flop is the **SR (Set-Reset) Latch**, constructed using cross-coupled NOR or NAND gates.

*   **Set (S):** Forces the output Q to 1.
*   **Reset (R):** Forces the output Q to 0.
*   **Hold:** When both inputs are de-asserted, the circuit maintains (or "remembers") its previous state.

While latches are level-sensitive, most practical sequential circuits use **clocked flip-flops**. The clock signal synchronizes all operations, ensuring that the circuit changes state only at specific instants, leading to predictable and reliable behavior.

### 2.2. The Clock Signal and Synchronous vs. Asynchronous Circuits

The **clock** is a periodic signal (typically a square wave) that controls the timing of all state changes in a synchronous sequential circuit.

*   **Synchronous Sequential Circuits:** The state of memory elements (flip-flops) changes only at the active edge (rising or falling) of the clock pulse. This synchronization allows the entire system to operate in a coordinated, predictable manner. Most complex digital systems (like CPUs) are synchronous.
*   **Asynchronous Sequential Circuits:** The state change occurs immediately in response to changes in the inputs, without a common clock. They can be faster but are more difficult to design and analyze due to potential timing hazards like races and glitches.

### 2.3. The D Flip-Flop: A Workhorse

The most commonly used flip-flop is the **D Flip-Flop (Data Flip-Flop)**. Its operation is simple and ideal for data storage.
*   It has a single data input (**D**) and a clock input.
*   On the active clock edge, the value present at the **D** input is transferred to the output **Q**.
*   The output **Q** holds this value until the next active clock edge, regardless of any changes at the **D** input in the meantime.

This "sample and hold" behavior makes the D flip-flop perfect for building **registers** (which store multi-bit data) and as the state memory in **finite state machines (FSMs)**.

### 2.4. Finite State Machines (FSMs)

An FSM is a mathematical model and the cornerstone of sequential logic design. It defines a circuit's behavior based on its **present state** and its inputs. An FSM consists of:
1.  **A set of States:** The various conditions the circuit can be in.
2.  **A set of Inputs:** Signals from the external world.
3.  **A set of Outputs:** Signals produced by the circuit.
4.  **Next State Logic:** A combinational function that determines the next state based on the current state and inputs.
5.  **Output Logic:** A combinational function that generates the outputs (this can be based on the present state only **Moore Machine** or on the present state and inputs **Mealy Machine**).

The flip-flops store the **present state**, and their inputs are driven by the **next state logic**.

### 2.5. Registers and Counters

*   **Register:** A group of D flip-flops (e.g., 4, 8, 32, 64) sharing a common clock signal. They are used to store binary data, such as an instruction or a number. A simple 4-bit register can be constructed with four D flip-flops.
*   **Counter:** A special type of register that cycles through a predefined sequence of states. For example, a 3-bit binary counter (built with three flip-flops) would count from 0 to 7 (000 to 111) and then reset. Counters are essential for tracking events, creating timers, and controlling sequences of operations.

## 3. Example: A Simple State Machine

Consider designing a circuit to detect the sequence "101" on a serial input line.

1.  **Define States:**
    *   `S0`: No sequence matched (initial state).
    *   `S1`: The first '1' has been detected.
    *   `S2`: "10" has been detected.
    *   `S3`: "101" has been detected (output `Z=1`).

2.  **Create State Table:** For each state and input value, define the next state and output.

| Present State | Input (X) | Next State | Output (Z) |
| :--- | :---: | :--- | :---: |
| S0 | 0 | S0 | 0 |
| S0 | 1 | S1 | 0 |
| S1 | 0 | S2 | 0 |
| S1 | 1 | S1 | 0 |
| S2 | 0 | S0 | 0 |
| S2 | 1 | S3 | 1 |
| S3 | 0 | S2 | 0 |
| S3 | 1 | S1 | 0 |

3.  **Implementation:** The states (`S0`, `S1`, `S2`, `S3`) would be encoded into binary (e.g., 00, 01, 10, 11) and stored in flip-flops. Combinational logic blocks would be designed from the state table to generate the next state logic (flip-flop inputs) and the output logic.

## 4. Key Points & Summary

*   **Memory:** Sequential circuits have memory (flip-flops), allowing output to depend on input history.
*   **Synchronous Operation:** Most systems use a clock to synchronize state changes, making them predictable.
*   **Fundamental Elements:** The **Flip-Flop** (especially the D-FF) is the basic storage unit.
*   **Core Model:** The **Finite State Machine (FSM)** is the abstract model used to design sequential circuits, describing states, transitions, and outputs.
*   **Applications:** Registers for data storage and counters for counting/timing are built from interconnected flip-flops.
*   **Design Flow:** The design process involves defining states, creating a state table, assigning binary codes, and implementing the next-state and output logic with combinational circuits.

Understanding sequential logic is crucial for progressing to more advanced topics like processor design, where the entire operation is controlled by a complex synchronous state machine.