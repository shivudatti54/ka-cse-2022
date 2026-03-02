# Module 2: Sequential Circuits - The Memory of Digital Systems

## Introduction

In the previous module, you learned about **combinational circuits**, where the output depends solely on the present combination of inputs. However, most real-world digital systems (like computers) require memory to store past states and sequence through operations. This is where **Sequential Circuits** come in. Unlike combinational logic, the outputs of a sequential circuit depend not only on the current inputs but also on the **past sequence of inputs**. This ability to "remember" history is what enables counting, data storage, and controlled sequencing, forming the foundational memory elements of a computer.

## Core Concepts

### 1. The Basic Building Block: The Flip-Flop

The fundamental memory unit in sequential circuits is the **flip-flop**. It is a bistable multivibrator, meaning it has two stable states (0 and 1) and can remain in either state indefinitely until triggered by an input signal. This allows it to store one bit of information.

The most common and fundamental type is the **D Flip-Flop**. Its operation is simple:

- **Data Input (D):** The bit you want to store.
- **Clock Input (CLK):** A control signal that determines _when_ the input is read and stored.
- **Output (Q):** The stored bit.
- **Complementary Output (Q'):** The inverse of Q.

On the **active edge** (usually the rising or falling edge) of the clock signal, the value present at the `D` input is latched and appears at the output `Q`. This value is then stored until the next active clock edge.

**Example:** Consider a positive-edge-triggered D flip-flop.

- At time `t0`, `CLK` is low, `D=1`, `Q` is unknown.
- At the rising edge of the clock (`t1`), the value `D=1` is captured, so `Q` becomes 1.
- Now, even if `D` changes to 0 while the clock is high, `Q` will remain 1, "remembering" the value that was present at the clock edge.
- `Q` will only change again on the _next_ rising clock edge.

### 2. Clock Signal and Synchronization

Most sequential circuits are **synchronous**, meaning their operation is synchronized by a common **clock signal**. This clock is a periodic square wave that coordinates when all the flip-flops in the system will update their state. This synchronization is crucial for predictable and reliable operation, ensuring all parts of the circuit change state in a coordinated manner.

### 3. Classification of Sequential Circuits

Sequential circuits are broadly classified based on their output behavior:

- **Moore Machine:** The outputs depend **only** on the present state of the flip-flops. The outputs are synchronous with the clock.
  - `Output = f(Present State)`
- **Mealy Machine:** The outputs depend on **both** the present state **and** the present inputs. This can make outputs change asynchronously if inputs change.
  - `Output = f(Present State, Present Inputs)`

Mealy machines often have fewer states than their Moore counterparts for the same logic, but their timing can be more complex.

### 4. Registers and Counters: Simple Sequential Circuits

Groups of flip-flops used together form more complex structures:

- **Register:** A group of D flip-flops (e.g., 4, 8, 32) sharing a common clock line. They are used to **store** multi-bit data (a "word"). A 4-bit register, for instance, can store a nibble of data.
- **Counter:** A register of flip-flops designed to go through a **predetermined sequence of states** upon the application of clock pulses. They are essential for tasks like counting events, generating timing sequences, and addressing memory. Common types include binary up-counters, down-counters, and modulo-n counters.

### 5. Finite State Machines (FSM)

This is the most general and powerful model for sequential circuits. An FSM is defined by:

- A set of **states** (the values stored in the flip-flops).
- A set of **inputs**.
- A set of **outputs**.
- A **state transition function** that defines the next state based on the current state and input.
- An **output function** (defining Moore or Mealy output).

FSMs are used to design control units, sequence detectors, and complex digital systems.

## Summary & Key Points

- **Core Difference:** Combinational circuits have no memory; Sequential circuits **do have memory** (past state).
- **Fundamental Unit:** The **Flip-Flop** (especially the D flip-flop) is the basic 1-bit memory element.
- **Synchronization:** Most sequential circuits are **synchronous**, using a global clock signal to control the timing of state changes.
- **Classification:** Sequential circuits are modeled as **Moore** (outputs depend only on state) or **Mealy** (outputs depend on state and input) machines.
- **Applications:** Flip-flops are building blocks for **registers** (storage), **counters** (counting/timing), and complex **Finite State Machines** (control logic).
- **Why It Matters:** Understanding sequential logic is essential for comprehending how a computer's central processing unit (CPU) manages data, executes instructions in sequence, and stores intermediate results—the very heart of computer organization.
