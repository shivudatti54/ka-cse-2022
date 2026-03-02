# Basic Structure of Computers

## Introduction

Welcome to Module 3 of Digital Design and Computer Organization. A computer is a complex system, but its fundamental operation can be understood by examining its basic structure. This structure, often referred to as the von Neumann architecture (after the mathematician John von Neumann), forms the bedrock of virtually all modern computers. Understanding this structure is crucial for any computer engineer, as it explains how hardware components work together to execute programs and process data.

## Core Concepts of the Von Neumann Architecture

The von Neumann architecture is characterized by its **stored-program concept**, where program instructions and data are stored together in the same memory unit. This was a revolutionary idea that distinguished it from earlier fixed-program computers. The model consists of five main functional units:

### 1. Input Unit
This unit accepts data and instructions from the outside world and converts them into a form that the computer can understand (binary format). Examples include keyboards, mice, scanners, and touchscreens.

### 2. Output Unit
This unit takes results produced by the computer and converts them from binary into a human-readable or machine-usable form. Examples include monitors, printers, and speakers.

### 3. Memory Unit (Main Memory/RAM)
Often called Random Access Memory (RAM), this is the computer's internal storage. It stores both the program instructions and the data required while the computer is powered on. Its key characteristics are:
*   It is volatile (contents are lost when power is off).
*   It is directly accessible by the CPU.
*   Each storage location has a unique address.

### 4. Arithmetic Logic Unit (ALU)
This is the computational heart of the computer. The ALU performs all arithmetic operations (e.g., addition, subtraction) and logical operations (e.g., AND, OR, NOT, comparisons). It operates on data fetched from the memory unit.

### 5. Control Unit (CU)
This unit acts as the central nervous system of the computer. It directs the operation of all other parts of the processor. Its primary functions are:
*   **Fetching** an instruction from memory.
*   **Decoding** the instruction to understand what needs to be done.
*   **Executing** the instruction by generating control signals that command the ALU, registers, and other components.

The **Central Processing Unit (CPU)** is the core of the computer and is formed by the combination of the **Control Unit (CU)** and the **Arithmetic Logic Unit (ALU)**.

### 6. Registers
These are small, high-speed storage locations *inside the CPU* used to hold temporary data, instructions, and memory addresses that are immediately required for processing. Key registers include the **Program Counter (PC)**, which holds the address of the next instruction to be executed, and the **Instruction Register (IR)**, which holds the current instruction being decoded.

## The System Bus: The Communication Highway

These components do not operate in isolation; they must communicate. This communication happens over the **system bus**, a collection of parallel wires that carry information between components. The bus is typically divided into three sub-buses:

1.  **Data Bus:** Carries the actual data between the processor, memory, and I/O devices. Its width (e.g., 32-bit, 64-bit) determines how much data can be transferred at once.
2.  **Address Bus:** Carries the memory addresses from the CPU to the memory unit, specifying where data is to be read from or written to. Its width determines the maximum addressable memory (e.g., a 32-bit address bus can address 2³² locations).
3.  **Control Bus:** Carries control and timing signals (e.g., Read, Write, Interrupt) from the control unit to coordinate the activities of all the components.

**Example:** To add two numbers (say, 5 and 3) stored in memory, the CPU would:
1.  Fetch the "ADD" instruction via the data bus.
2.  Fetch the operand `5` from its memory address (sent over the address bus).
3.  Fetch the operand `3` from its memory address.
4.  The CU would command the ALU to perform the addition.
5.  The result `8` would be sent back to memory or a register via the data bus.

## Key Points & Summary

*   The **von Neumann architecture** is the fundamental design upon which modern computers are built, based on the **stored-program concept**.
*   The five main functional units are: **Input, Output, Memory, ALU, and Control Unit**.
*   The **CPU** is the brain of the computer, comprising the **Control Unit (CU)** and the **Arithmetic Logic Unit (ALU)**.
*   **Registers** are the CPU's internal, high-speed temporary storage for critical data during execution.
*   The **System Bus** (comprising Data, Address, and Control buses) is the communication pathway that connects all the major components, allowing them to work together as a unified system.
*   This basic structure creates a machine that follows a simple **fetch-decode-execute cycle** repeatedly to run programs. Understanding this cycle is key to mastering computer organization.