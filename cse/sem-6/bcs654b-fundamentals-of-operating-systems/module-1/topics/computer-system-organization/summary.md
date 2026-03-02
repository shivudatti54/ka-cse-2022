# Computer System Organization

## Overview

Computer system organization describes the structural components and their interactions in a computer system. The four main components are CPU, Main Memory, I/O Devices, and System Bus, all working together to execute programs and process data.

## Key Points

- **CPU Components**: Control Unit (coordinates activities), ALU (performs operations), and Registers (high-speed storage)
- **Fetch-Decode-Execute Cycle**: CPU retrieves instruction, interprets it, performs operation, and updates program counter
- **Memory Hierarchy**: Registers, Cache, RAM, ROM, and Secondary Storage arranged by speed and capacity
- **I/O Operations**: Handled through Programmed I/O, Interrupt-driven I/O, or Direct Memory Access (DMA)
- **Interrupts**: Hardware interrupts (from devices), Software interrupts (from programs), and Traps (error conditions)
- **SMP Architecture**: Multiple processors sharing same main memory running same OS instance
- **Storage Devices**: Magnetic disks (HDD) with tracks/sectors and Solid State Drives (SSD) with flash memory

## Important Concepts

- Memory hierarchy balances speed, cost, and capacity from fastest (registers) to slowest (secondary storage)
- Interrupt handling process: signal, save state, execute ISR, restore state, resume execution
- DMA allows direct data transfer between devices and memory without CPU intervention
- Bootstrap loader initializes system and loads OS kernel during boot process

## Notes

- Be able to draw and explain the fetch-decode-execute cycle
- Memorize memory hierarchy characteristics (speed, capacity, volatility)
- Understand difference between SMP (Symmetric Multiprocessing) and clustered systems
