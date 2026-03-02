# Process Identifiers - Summary

## Key Definitions and Concepts

- **Process Identifier (PID)**: A unique positive integer assigned by the OS kernel to each process; used to identify and reference processes
- **Parent Process Identifier (PPID)**: The PID of the process that created the current process; establishes the process hierarchy
- **Process Control Block (PCB)**: A kernel data structure containing all information about a process, indexed by its PID
- **User Identifier (UID)**: Determines the owner's user account and associated permissions
- **Group Identifier (GID)**: Determines the process's group membership for access control

## Important Formulas and Theorems

- Maximum PID: Found in `/proc/sys/kernel/pid_max` (typically 32768 on older systems, up to 4 million on 64-bit)
- fork() return value: Returns 0 to child, returns child's PID to parent, returns -1 on failure
- PCB contains: Process state, program counter, CPU registers, memory management info, accounting info, I/O status

## Key Points

- PID 0 is reserved for swapper/idle process; PID 1 is reserved for init process
- Every process (except init) has a parent, creating a process tree structure
- The kernel uses PID as the primary key to access process information in the PCB
- When a parent dies before child, child becomes orphan and is adopted by init (PPID = 1)
- Zombie processes occur when terminated process's PCB remains until parent calls wait()
- Real UID identifies the actual user; effective UID determines access permissions
- Process identifiers are recycled after process termination to conserve the identifier space

## Common Mistakes to Avoid

1. Confusing PID with PPID - remember PID is self, PPID is parent
2. Forgetting that fork() returns different values to parent and child
3. Not calling wait() in parent, leading to zombie processes
4. Assuming PIDs are never reused - they are recycled after wraparound

## Revision Tips

1. Practice writing C programs using getpid(), getppid(), getuid(), getgid()
2. Use `ps` and `pstree` commands to visualize process hierarchies on Linux
3. Trace the parent-child relationship through multiple fork() calls
4. Remember the reserved PIDs (0 and 1) and their significance
5. Understand how zombie and orphan states arise from parent-child relationship failures
