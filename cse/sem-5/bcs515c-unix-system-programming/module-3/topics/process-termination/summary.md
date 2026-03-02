# Process Termination - Summary

## Key Definitions and Concepts

- **Process Termination**: The final state in the process lifecycle where a process completes execution and releases all allocated resources
- **Zombie Process**: A terminated child process whose exit status has not yet been read by its parent (still occupies process table entry)
- **Orphan Process**: A running process whose parent has terminated before the child completes (adopted by init process)
- **Exit Status**: An integer value (0-255) returned by a terminating process to indicate success/failure
- **init Process**: PID 1, the first process that adopts orphaned processes and calls wait() to prevent zombies

## Important Formulas and Theorems

- **Exit Status Convention**: 0 = Success, Non-zero = Failure
- **wait() return values**: Returns child PID on success, -1 on error
- **WEXITSTATUS(status)**: Extracts lower 8 bits of exit status (0-255 range)
- **Orphan detection**: If getppid() returns 1, process is an orphan adopted by init

## Key Points

- Process termination involves resource deallocation, exit status storage, and PCB cleanup
- exit() performs cleanup (flush buffers, call atexit handlers); \_exit() terminates immediately
- Parent must call wait()/waitpid() to read child's exit status and prevent zombie formation
- wait() blocks until any child terminates; waitpid() with WNOHANG is non-blocking
- WIFEXITED checks normal termination; WIFSIGNALED checks if killed by signal
- Orphans are automatically adopted by init which prevents resource leaks
- Zombie processes accumulate if parent never calls wait() - this is a programming error
- SIGKILL and SIGSTOP cannot be caught or ignored; they always terminate the process
- Process groups and sessions handle termination of related processes collectively

## Common Mistakes to Avoid

- Forgetting to call wait() in parent - leads to zombie process accumulation
- Confusing exit() with \_exit() - one cleans up, the other doesn't
- Not checking return values of wait() calls - can miss child termination details
- Assuming process termination is instantaneous - exit status remains until wait() is called

## Revision Tips

1. Practice writing fork() + wait() code to understand parent-child termination synchronization
2. Use `ps aux` command to view zombie processes (marked as `<defunct>`)
3. Remember: Zombie = Dead but not buried (waiting for parent to read status)
4. Remember: Orphan = Alive without parent (adopted by init)
5. Quick recall: exit(0) = success, exit(1) = failure is the standard convention
