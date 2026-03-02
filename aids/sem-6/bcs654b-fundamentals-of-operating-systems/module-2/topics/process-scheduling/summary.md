# Process Scheduling

## Overview

Process scheduling is the mechanism by which the OS decides which process gets CPU access and when, to maximize CPU utilization and provide good response time. It maintains scheduling queues and uses schedulers to manage process execution efficiently.

## Key Points

- **Scheduling Objective**: Multiprogramming (keep CPU busy), Time-sharing (switch CPU frequently for interactivity)
- **PCB Information**: Process state, PID, program counter, CPU registers, CPU-scheduling info, memory-management info, accounting info, I/O status
- **Scheduling Queues**: Job Queue (all processes), Ready Queue (processes in memory ready to execute), Device Queues (waiting for I/O devices)
- **Three Schedulers**: Long-term (selects from disk to memory, controls multiprogramming degree), Short-term (selects from ready queue, must be very fast), Medium-term (swapping to manage multiprogramming)
- **Context Switch**: Save old process state in PCB → Load new process state from PCB, pure overhead (1-1000 microseconds)
- **Process Creation**: fork() creates child duplicate, exec() replaces with new program
- **Process States**: New → Ready → Running → Waiting/Blocked → Terminated
- **IPC Models**: Shared Memory (fast, requires sync) vs Message Passing (slower, kernel-managed, easier)

## Important Concepts

- Long-term scheduler controls degree of multiprogramming and mix of I/O-bound/CPU-bound processes
- Short-term scheduler invoked frequently (every 100ms) so must be extremely fast
- Context switch is overhead depending on hardware support (multiple register sets reduce time)
- Process tree formed by parent-child relationships traced back to init (PID 1)

## Notes

- Understand all three scheduler types and when each is invoked
- Know context switch is pure overhead - system does no useful work
- Be able to explain process state transitions with scheduling events
- Remember fork() returns 0 to child, child PID to parent - common exam question
