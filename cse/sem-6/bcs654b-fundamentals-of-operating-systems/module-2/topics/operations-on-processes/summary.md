# Operations on Processes

## Overview

Process operations include creating, executing, terminating, and synchronizing processes. The fundamental operations are process creation (fork/exec), process termination (exit/kill), and process synchronization (wait). These operations form the basis of process management in operating systems.

## Key Points

- **Process Creation**: Parent creates child forming process tree; fork() creates duplicate, exec() replaces memory with new program
- **fork() System Call**: Returns child PID to parent, returns 0 to child; child gets copy of parent's address space
- **exec() System Call**: Replaces current process memory with new program, PID remains same but program changes
- **Process Termination**: Normal exit (exit()), error exit (voluntary), fatal error (involuntary), killed by another process (kill())
- **Termination Steps**: Save status, deallocate resources, free PCB, inform parent via wait()
- **Cascading Termination**: Parent termination causes all children to terminate in some systems
- **wait() System Call**: Parent suspends until child terminates, retrieves child's exit status, prevents zombie processes
- **Zombie Process**: Terminated child whose parent hasn't called wait() - PCB entry remains
- **Orphan Process**: Child whose parent terminated - adopted by init process (PID 1)

## Important Concepts

- Process creation reasons: user request, system initialization, batch job, system call execution
- Resource sharing options: share all, share subset, share no resources
- IPC enables cooperating processes via shared memory (fast) or message passing (easier)
- Process operations cause state transitions: fork (Running→Ready), exit (Running→Terminated), wait (Running→Waiting)

## Notes

- Trace code involving fork() - understand return values (0 to child, PID to parent)
- Distinguish creation (fork) from execution (exec) - often used together but separate
- Know zombie (child terminated, parent hasn't waited) vs orphan (parent terminated first)
- Relate operations to state transitions in diagrams
