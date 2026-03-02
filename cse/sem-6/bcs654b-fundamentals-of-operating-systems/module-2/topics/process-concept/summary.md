# Process Concept

## Overview

A process is a program in execution, consisting of program code (text section), current activity (program counter, registers), stack (temporary data), data section (global variables), and heap (dynamically allocated memory). It is an active entity, unlike a program which is passive.

## Key Points

- **Memory Layout**: Text (program code) → Initialized Data → Uninitialized Data (BSS) → Heap (grows upward) → Stack (grows downward)
- **Process Control Block (PCB)**: Contains PID, process state, program counter, CPU registers, memory info, I/O status, and scheduling info
- **Process Creation**: Parent creates child using fork() (creates copy), exec() (replaces memory), CreateProcess() in Windows
- **Process Termination**: Normal exit (voluntary), error exit (voluntary), fatal error (involuntary), killed by another process (involuntary)
- **Parent-Child Relationship**: Parent may wait using wait(), orphan process (parent terminated first), zombie process (child terminated, parent hasn't called wait())
- **Resource Sharing**: Parent and child can share all, subset, or no resources

## Important Concepts

- Program is passive entity stored on disk, process is active entity loaded in memory
- One program can have multiple process instances
- PCB fields uniquely identify and manage each process
- fork() child gets copy of parent's address space

## Notes

- Know PCB fields and memory layout for exam
- Understand fork() behavior: child gets copy of parent
- Remember zombie vs orphan process definitions
- Be able to draw process memory layout diagram
