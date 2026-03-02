# Process Fundamentals

## What is a Process?
A process is a program in execution. It includes the program code, current activity (program counter, registers), stack, data section, and heap.

## Process vs Program
| Program | Process |
|---------|---------|
| Passive entity | Active entity |
| Stored on disk | Loaded in memory |
| No state | Has state (running, waiting, etc.) |
| Single copy | Multiple instances possible |

## Process Memory Layout
```
High Address
┌─────────────────┐
│     Stack       │ ← Local variables, function calls
│        ↓        │
├─────────────────┤
│                 │
│        ↑        │
│      Heap       │ ← Dynamic allocation
├─────────────────┤
│  Uninitialized  │ ← BSS segment
│      Data       │
├─────────────────┤
│  Initialized    │ ← Data segment
│      Data       │
├─────────────────┤
│      Text       │ ← Program code (read-only)
└─────────────────┘
Low Address
```

## Process Control Block (PCB)
The PCB contains all information about a process:

| Field | Description |
|-------|-------------|
| Process ID (PID) | Unique identifier |
| Process State | Running, ready, waiting, etc. |
| Program Counter | Address of next instruction |
| CPU Registers | Contents of registers |
| Memory Info | Page tables, limits |
| I/O Status | Open files, devices |
| Scheduling Info | Priority, CPU time used |

## Process Creation
- **Parent process** creates **child processes**
- Creates tree of processes
- Options for resource sharing:
  - Parent and child share all resources
  - Child shares subset
  - No sharing

### System Calls
- **fork()**: Creates new process (Unix/Linux)
- **exec()**: Replaces process memory with new program
- **CreateProcess()**: Windows process creation

## Process Termination
- Normal exit (voluntary)
- Error exit (voluntary)
- Fatal error (involuntary)
- Killed by another process (involuntary)

### Parent-Child Relationship
- Parent may wait for child (wait())
- Orphan process: parent terminated first
- Zombie process: child terminated, parent hasn't called wait()

> **Exam Tip**: Know the PCB fields and memory layout. Understand fork() behavior - child gets copy of parent's address space.
