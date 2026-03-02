# vfork - Process Creation - Summary

## Key Definitions and Concepts

- **vfork()**: A system call that creates a new process without copying the parent's address space; the child shares the parent's memory until calling exec() or exiting

- **Copy-On-Write (COW)**: A memory optimization technique where pages are shared between parent and child until modification, making fork() more efficient

- **Process**: An instance of a program in execution, identified by a unique Process ID (PID)

## Important Formulas and Theorems

- **Return Value**: `vfork()` returns 0 to child process, returns child's PID (>0) to parent, returns -1 on error

- **Memory Sharing**: Unlike fork(), vfork() creates NO copy of parent address space; child operates in parent's memory directly

## Key Points

- vfork() is more efficient than fork() when child immediately calls exec() to load a new program

- Child process MUST call exec() or \_exit() after vfork(); returning without these causes undefined behavior

- Use \_exit() not exit() in child after vfork() to avoid flushing parent's I/O buffers

- Parent process remains blocked until child calls exec() or terminates

- vfork() was designed for early Unix systems with limited memory resources

- Modern OS with COW have reduced the performance gap, but vfork() still useful in embedded systems

- Any modification by child to parent's memory affects the parent immediately

- vfork() does not copy the parent's address space, making it extremely memory-efficient

## Common Mistakes to Avoid

- Using exit() instead of \_exit() in child after vfork() causes buffer corruption
- Returning from the calling function in child without calling exec() or \_exit()
- Calling non-async-signal-safe functions in child after vfork()
- Assuming fork() and vfork() behave identically in terms of memory management

## Revision Tips

1. Remember the golden rule: Child after vfork() must either call exec() to load new program or \_exit() to terminate

2. Practice writing at least 2-3 vfork() programs to understand the memory sharing behavior

3. Compare fork() vs vfork() in terms of memory copying, performance, and use cases

4. Remember that vfork() parent is blocked until child completes exec() or exits
