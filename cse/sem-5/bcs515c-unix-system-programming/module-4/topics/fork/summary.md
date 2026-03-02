# Process Creation Using fork() - Summary

## Key Definitions and Concepts

- **fork()**: A system call that creates a new process (child) by duplicating the calling process (parent)
- **Parent Process**: The original process that calls fork()
- **Child Process**: The newly created process, an almost exact copy of the parent
- **Zombie Process**: A terminated process whose parent hasn't called wait() to read its exit status
- **Orphan Process**: A running child process whose parent has terminated
- **Copy-on-Write (COW)**: Optimization technique where memory is shared until modification is needed

## Important Formulas and Theorems

- **fork() return values**:
  - Positive (child's PID) → returned to parent
  - Zero (0) → returned to child
  - Negative (-1) → error occurred

- **Process relationship**: Every process (except init) has a parent, forming a hierarchical tree structure

- **Exit status macros**:
  - `WIFEXITED(status)` - returns true if child terminated normally
  - `WEXITSTATUS(status)` - returns the exit code (0-255)

## Key Points

1. fork() is the primary mechanism for process creation in Unix/Linux systems

2. Both parent and child execute the same program code after fork() returns

3. The child receives a copy of the parent's address space, registers, and open file descriptors

4. Modern fork() implementations use Copy-on-Write for memory efficiency

5. fork()+exec() is the standard pattern for running different programs

6. Always use wait() in parent to prevent zombie processes

7. File descriptors are shared between parent and child (same file table entry)

8. getpid() returns current process ID; getppid() returns parent's PID

## Common Mistakes to Avoid

- Forgetting that both processes continue execution after fork() - many students think code after fork() runs only once
- Not checking the return value of fork() for errors
- Using exit() instead of \_exit() in child process after fork(), causing buffer flushing issues
- Creating child processes without proper synchronization, leading to race conditions
- Not calling wait() in parent, resulting in zombie processes

## Revision Tips

1. Practice writing simple fork() programs to understand execution flow

2. Memorize the three return values of fork() - this is frequently asked in exams

3. Remember the difference between exit() and \_exit() in forked processes

4. Understand why vfork() is now obsolete due to COW optimization

5. Review how wait() works with fork() to prevent zombie processes

6. Trace through multiple fork() calls to understand process creation patterns
