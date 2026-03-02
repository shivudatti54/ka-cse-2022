# Module 5: Input/Output Organization

**Subject:** Digital Design and Computer Organization
**Module:** Module 5
**Topic:** Input/Output (I/O) Organization

## Introduction

A computer system is more than just a CPU and memory; it must communicate with the external world. This communication is handled by its **Input/Output (I/O) system**. The I/O subsystem facilitates the transfer of data between the central components of the computer (CPU, Memory) and external peripherals like keyboards, mice, displays, hard drives, and network interfaces. Efficient I/O organization is crucial for overall system performance, as the speed of these peripherals is vastly different from that of the CPU and memory. This module explores the fundamental concepts of how a computer manages these vital communications.

## Core Concepts

### 1. I/O Bus

The I/O bus is a shared communication pathway that connects the CPU, memory, and all peripheral devices. It consists of three types of lines:
*   **Data Lines:** Carry the actual data being transferred.
*   **Address Lines:** Specify the memory address or the specific I/O device involved in the transfer.
*   **Control Lines:** Carry signals that manage the timing and nature of the transfer (e.g., Read, Write, Interrupt Acknowledge).

### 2. I/O Interface (Device Controller)

Each peripheral device has a dedicated **I/O interface** or controller. This is a hardware component (often a specialized chip) that acts as an intermediary between the device and the system bus. Its primary functions are:
*   **Data Buffering:** Temporarily holds data to compensate for the speed difference between the CPU and the slow peripheral.
*   **Command Decoding:** Interprets commands sent by the CPU (e.g., "read sector," "spin up motor").
*   **Signal Conversion:** Translates electrical signals from the device into a format understandable by the computer and vice-versa.
*   **Error Detection:** Checks for and sometimes corrects errors that may occur during data transfer.

### 3. Methods of I/O Data Transfer

There are three primary methods for transferring data to and from peripherals:

#### a) Programmed I/O (Polling)
The CPU directly controls the entire transfer. It repeatedly checks (polls) the status register of the I/O interface in a loop until the device is ready. Then, it reads or writes a single word of data (e.g., a byte) from/to the data register.

*   **Example:** Transferring a byte from a keyboard.
    1.  CPU reads the keyboard status register: "Is a key pressed?"
    2.  If status is "not ready," the CPU loops back to step 1.
    3.  If status is "ready," the CPU reads the data register to get the ASCII value of the key.
    4.  CPU stores this value in memory.
*   **Disadvantage:** Inefficient, as the CPU is busy waiting and cannot perform other tasks.

#### b) Interrupt-Driven I/O
The peripheral informs the CPU when it is ready. The I/O interface sends an **interrupt signal** to the CPU. The CPU suspends its current program, saves its state, and executes a special program called an **Interrupt Service Routine (ISR)** to handle the data transfer. After the ISR completes, the CPU resumes its previous task.

*   **Example:** Same keyboard transfer.
    1.  A key is pressed.
    2.  The keyboard controller sends an interrupt signal to the CPU.
    3.  CPU finishes its current instruction, saves the state, and jumps to the keyboard ISR.
    4.  The ISR reads the key data and stores it in a buffer in memory.
    5.  CPU returns to the program it was executing.
*   **Advantage:** Frees the CPU from wasteful polling, greatly improving efficiency.

#### c) Direct Memory Access (DMA)
Used for high-speed bulk data transfers (e.g., to/from a disk drive). A special controller, called the **DMA Controller (DMAC)**, is employed. The CPU initializes the DMAC by providing the source address, destination address, and the number of bytes to transfer. The DMAC then takes control of the system bus and manages the entire data transfer directly between the device and memory, without continuous CPU intervention.

*   **Advantage:** Offloads the CPU completely during the transfer, allowing it to execute other programs. This is the most efficient method for large data blocks.

### 4. I/O Addressing Techniques

*   **Memory-Mapped I/O:** I/O devices and memory share the same address space. The CPU uses the same instructions (e.g., `LOAD`, `STORE`) to access both memory and I/O registers. This simplifies the instruction set.
*   **Isolated I/O (Port-Mapped I/O):** I/O devices have a separate, dedicated address space. The CPU uses special I/O instructions (e.g., `IN`, `OUT`) to communicate with them. This requires more instructions but keeps I/O traffic separate from memory traffic.

## Key Points / Summary

*   The **I/O subsystem** is essential for computer communication with external devices.
*   An **I/O bus** provides the shared communication path for all components.
*   An **I/O interface (controller)** manages the interaction between a specific device and the system bus.
*   The three main data transfer methods are:
    *   **Programmed I/O (Polling):** Simple but inefficient; CPU waits for the device.
    *   **Interrupt-Driven I/O:** Efficient; the device notifies the CPU when ready.
    *   **Direct Memory Access (DMA):** Most efficient for large blocks; a DMAC handles the transfer, freeing the CPU.
*   I/O devices can be addressed via **Memory-Mapped I/O** (shared address space) or **Isolated I/O** (separate address space).