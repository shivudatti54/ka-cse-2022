# Sequential Logic: The Foundation of Stateful Digital Systems

**Subject:** Digital Design and Computer Organization
**Module:** Module 2
**Topic:** Sequential Logic

## Introduction

Combinational logic circuits, which we studied previously, produce outputs based solely on the current inputs. They have no memory. However, most practical digital systems—from a simple vending machine to a complex CPU—require the ability to remember past inputs and states. This is the domain of **Sequential Logic**. Sequential logic circuits use memory elements (flip-flops) to store state information, and their outputs depend on both the current inputs and the past sequence of inputs. This ability to remember makes them the fundamental building blocks for finite state machines, registers, counters, and memory units.

## Core Concepts

### 1. The Concept of "State"

The key differentiator of sequential circuits is their **state**. The state is the stored information at a given time, which represents the history of the system. The output and the next state are determined by the current inputs and the current state.

### 2. Basic Memory Element: The Flip-Flop

The fundamental unit of memory in sequential logic is the **flip-flop**. It is a bistable multivibrator, meaning it has two stable states (0 and 1) and can remain in one state indefinitely until directed by an input signal to switch.

*   **Latches vs. Flip-Flops:** Latches are level-sensitive memory elements (e.g., SR Latch, D Latch). Their state can change as long as the enable signal is active. Flip-flops are edge-triggered devices, meaning they sample their inputs and change state only at a specific point in time—the rising or falling edge of a clock signal. This makes them more reliable for synchronous systems.
*   **The Clock Signal:** Most sequential circuits are **synchronous**, meaning their operation is synchronized by a periodic clock signal. The clock provides a timing reference, ensuring that all flip-flops in the system update their state simultaneously. This prevents instability and race conditions.

### 3. Types of Sequential Circuits

Based on their structure and behavior, sequential circuits are classified into two main types:

*   **Moore Machine:** The outputs depend **only** on the current state of the circuit. The inputs affect only the path to the next state, not the immediate output.
    *   `Output = f(Current State)`

*   **Mealy Machine:** The outputs depend on **both** the current state **and** the current inputs.
    *   `Output = f(Current State, Current Inputs)`

Mealy machines often have fewer states than Moore machines for the same functionality but can have asynchronous output behavior.

## Example: A Simple Finite State Machine (FSM)

Let's design a sequential circuit to detect the sequence "101" on a serial input line.

1.  **Define States:**
    *   `S0`: Start state (no meaningful input detected). Also represents the state after a failed sequence.
    *   `S1`: The first '1' has been detected.
    *   `S2`: "10" has been detected.
    *   `S3`: "101" has been detected (the target sequence).

2.  **State Transition Diagram (Mealy Machine):**
    The diagram shows transitions between states based on the input `X`. The output `Z` is 1 only when the sequence is completed (`S3` in a Moore machine, or on the transition into `S3` in a Mealy machine).


    *(Note: A full diagram would show all transitions, e.g., from S2, if X=1, we go to S1, not S0, because the last input '1' could be the start of a new sequence.)*

3.  **Implementation:**
    *   We need flip-flops to represent the states (e.g., 2 flip-flops for 4 states).
    *   We create a state table showing the next state and output for every combination of current state and input.
    *   Using Karnaugh Maps, we derive the combinational logic for the **Next State** and the **Output**.
    *   This combinational logic is connected to the `D` inputs of the flip-flops, and the flip-flops' outputs (`Q`) represent the current state.

## Key Sequential Circuits Built from Flip-Flops

*   **Registers:** Groups of D-flip-flops used to store binary data (e.g., a 8-bit register). They load data on a clock edge.
*   **Counters:** Sequential circuits that cycle through a predefined sequence of states. They are essential for counting events, generating timing sequences, and addressing memory. A simple **3-bit binary up-counter** made from T-flip-flops is a classic example.
*   **Shift Registers:** Circuits that shift their stored data one bit left or right on each clock pulse. Used for serial-to-parallel conversion and arithmetic operations.

## Summary

| Key Point | Description |
| :--- | :--- |
| **Definition** | Sequential logic circuits have memory. Their output depends on both current inputs and past history (state). |
| **Core Element** | The flip-flop is the basic memory unit. Edge-triggered flip-flops (e.g., D-FF) are used for synchronous design. |
| **Synchronous Design** | Operation is synchronized by a global clock signal, ensuring stable and predictable state changes. |
| **State Machines** | The behavior of sequential circuits is modeled using finite state machines (FSMs) like Moore and Mealy machines. |
| **Applications** | Essential for building registers, counters, memory units, and the control logic of a CPU. |