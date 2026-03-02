# Accessing I/O Devices

## Introduction

In a computer system, the Central Processing Unit (CPU) and memory are only part of the story. The true utility of a computer is realized when it interacts with the external world through Input/Output (I/O) devices like keyboards, mice, displays, network cards, and storage drives. A fundamental challenge in computer organization is how the CPU efficiently communicates with these varied and typically slower peripherals. This module explores the core methods and mechanisms for **Accessing I/O Devices**, a critical concept for understanding how a complete computer system functions.

## Core Concepts

The primary function of an I/O system is to facilitate data transfer between the CPU (or memory) and an external device. This is achieved through three main techniques: **Program-Controlled I/O (Polling)**, **Interrupt-Driven I/O**, and **Direct Memory Access (DMA)**.

### 1. Program-Controlled I/O (Polling)

This is the simplest method where the CPU actively controls the entire data transfer process.

*   **How it works:** The CPU repeatedly checks (or *polls*) the status register of the I/O device interface to see if the device is ready to send or receive data. This happens in a tight loop within a program.
*   **Process:**
    1.  The CPU requests the I/O operation by writing a command to the device's command register.
    2.  The CPU continuously reads the device's status register until it indicates "ready."
    3.  Once ready, a single unit of data (e.g., a byte) is transferred between the device data register and the CPU register.
    4.  The process repeats for the next unit of data.
*   **Example:** Reading a character from a keyboard. The CPU loops endlessly, checking if a key has been pressed (`status == ready`). When it is, it reads the character code from the keyboard data register.
*   **Advantage:** Simple hardware implementation.
*   **Disadvantage:** Extremely inefficient. The CPU is busy waiting and cannot perform other useful work until the I/O operation is complete, leading to poor utilization.

### 2. Interrupt-Driven I/O

This mechanism is used to avoid the CPU-wastage inherent in polling. Here, the I/O device *notifies* the CPU when it is ready.

*   **How it works:** The CPU initiates an I/O operation and then moves on to execute other tasks. The I/O device, when it is ready, sends an **interrupt request** signal to the CPU.
*   **Process:**
    1.  The CPU issues a command to the I/O device and continues with other work.
    2.  When the device is ready, it sends an interrupt signal.
    3.  The CPU finishes its current instruction, saves the state of the current program (e.g., program counter, registers), and branches to a special program called an **Interrupt Service Routine (ISR)**.
    4.  The ISR handles the data transfer (e.g., moves a byte from the device to memory).
    5.  Upon completion, the CPU restores the saved state and resumes the original program.
*   **Advantage:** Much more efficient CPU usage. The CPU is free to do productive work while waiting for slow I/O devices.
*   **Disadvantage:** Overhead is involved in handling the interrupt (saving/restoring state). For transferring large blocks of data, an interrupt is generated for every single byte, which can still be inefficient.

### 3. Direct Memory Access (DMA)

DMA is a technique designed to overcome the overhead of byte-by-byte transfer, which is a problem in both polling and interrupt-driven I/O, especially for high-speed devices.

*   **How it works:** A special hardware controller, called the **DMA Controller**, is entrusted to manage the data transfer directly between the I/O device and the main memory, without continuous intervention from the CPU.
*   **Process:**
    1.  The CPU sets up the DMA controller by providing it with:
        *   The starting memory address.
        *   The number of bytes to transfer.
        *   The type of operation (read or write).
    2.  The CPU then proceeds with other tasks.
    3.  The DMA controller manages the entire data transfer. It requests control of the system bus from the CPU (a **bus request**), and upon being granted access (a **bus grant**), it transfers a block of data directly to/from memory.
    4.  Once the entire block is transferred, the DMA controller sends an **interrupt** to the CPU to signal completion.
*   **Advantage:** Highly efficient. It eliminates the need for the CPU to be involved in moving every byte, freeing it for more complex tasks and allowing much faster bulk data transfers.
*   **Disadvantage:** Increased hardware complexity and cost due to the added DMA controller chip.

## Memory-Mapped I/O vs. Isolated I/O

An important related concept is how the CPU addresses I/O devices.

*   **Memory-Mapped I/O:** The registers of I/O devices are mapped into the CPU's memory address space. Instructions that access memory (like `LOAD` and `STORE`) are used to communicate with devices. This simplifies the instruction set but uses up physical memory addresses.
*   **Isolated I/O (Port-Mapped I/O):** The I/O devices have a separate address space from memory. Special I/O instructions (e.g., `IN` and `OUT`) are used. This protects the memory space but requires additional CPU circuitry and instructions.

## Key Points / Summary

| Feature | Programmed I/O (Polling) | Interrupt-Driven I/O | Direct Memory Access (DMA) |
| :--- | :--- | :--- | :--- |
| **CPU Involvement** | High (active waiting) | Medium (per transfer) | Low (only for setup) |
| **Efficiency** | Very Low | Good | Very High |
| **Hardware Complexity** | Low | Medium | High (needs DMA controller) |
| **Use Case** | Simple, low-speed devices | General-purpose devices | High-speed, block-transfer devices (e.g., disk drives) |

*   **Summary:** The evolution from **Polling** to **Interrupts** to **DMA** represents a pursuit of greater efficiency, offloading work from the CPU to specialized hardware to allow for faster and more concurrent system operation. Most modern systems use a combination of all three techniques, applying the right method for the right device.