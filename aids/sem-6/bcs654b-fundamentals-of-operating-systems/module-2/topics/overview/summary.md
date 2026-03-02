# Overview of Process Management

## Overview

Process Management is a fundamental OS function that handles processes (programs in execution). A process includes text section, data section, stack, heap, program counter, and CPU registers, moving through various states (New, Ready, Running, Waiting, Terminated) during its lifetime.

## Key Points

- **Process vs Program**: Program is passive (code on disk), Process is active (program in execution)
- **Process Control Block (PCB)**: Data structure containing process state, program counter, CPU registers, scheduling info, memory management info, accounting info, and I/O status
- **Process States**: New → Ready → Running → Waiting → Terminated with transitions based on events
- **Context Switch**: Saving old process state in PCB and loading new process state - pure overhead
- **Process Creation**: Parent creates child processes using fork() (returns 0 to child, PID to parent) and exec() (replaces memory with new program)
- **Process Termination**: Normal exit, error exit, fatal error, or killed by another process; Zombie (terminated but parent hasn't called wait()) vs Orphan (parent terminated first)
- **Scheduling Queues**: Job Queue (all processes), Ready Queue (processes ready to execute), Device Queues (waiting for I/O)
- **IPC Methods**: Shared Memory (fast, needs synchronization) vs Message Passing (slower, easier to implement)

## Important Concepts

- PCB contains all information needed to describe and manage a process
- Context switch is overhead where system does no useful work
- fork() creates duplicate, exec() replaces process memory with new program
- Three schedulers: Long-term (job scheduler), Short-term (CPU scheduler), Medium-term (swapping)

## Notes

- Know process state diagram with all transitions and their causes
- Memorize PCB fields and what each stores
- Understand fork() return values - common exam question
- Compare shared memory vs message passing for IPC
