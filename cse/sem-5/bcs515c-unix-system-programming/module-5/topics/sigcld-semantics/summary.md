# SIGCLD Semantics - Summary

## Key Definitions and Concepts

- **SIGCLD (SIGCHLD)**: Signal sent to parent when a child process terminates or when wait() is called
- **Zombie Process**: A terminated process that remains in the process table until parent retrieves its exit status via wait()
- **Process Reaping**: The act of a parent retrieving a child process's exit status, removing it from the process table
- **Orphaned Zombie**: A zombie process whose parent has terminated; adopted by init (PID 1)

## Important Formulas and Theorems

- `pid_t wait(int *status)` - Blocks until any child terminates, returns child PID
- `pid_t waitpid(pid_t pid, int *status, int options)` - Flexible waiting with options
- `WNOHANG` - Option that makes waitpid() non-blocking
- `WIFEXITED(status)` - Macro to check normal termination
- `WEXITSTATUS(status)` - Macro to extract exit code (always check WIFEXITED first)
- `WIFSTOPPED(status)` - Checks if child was stopped (requires WUNTRACED)
- `WSTOPSIG(status)` - Extracts signal number that stopped the process

## Key Points

- The default action for SIGCLD is to ignore the signal, causing zombie accumulation if wait() is not called
- Always call wait()/waitpid() in parent to prevent zombies - this is called "reaping" the child
- Use waitpid(-1, &status, WNOHANG) in a loop inside signal handlers to reap multiple children
- The SA_RESTART flag in sigaction() restarts interrupted system calls automatically
- wait() blocks indefinitely when no children have terminated; use WNOHANG for non-blocking behavior
- When parent dies before reaping children, init adopts and reaps the zombie children
- SIGCLD is essentially an alias for SIGCHLD in modern Linux systems
- SIGCHLD is a standard POSIX signal; SIGCLD was the older BSD terminology

## Common Mistakes to Avoid

- Calling wait() inside a signal handler without WNOHANG - can cause deadlock if multiple children terminate
- Not checking return value of wait()/waitpid() - always check if return > 0, = 0 (WNOHANG), or -1 (error)
- Using WEXITSTATUS() without first checking WIFEXITED() - status contains garbage if child was killed by signal
- Forgetting to initialize sigaction structure properly with sigemptyset() and sa_flags

## Revision Tips

1. Practice writing code with fork(), wait(), and signal handlers until the pattern is automatic
2. Remember: zombie = dead but still in table; orphan = child without parent; defunct = zombie
3. Draw the process state diagram showing transitions between running, sleeping, stopped, and zombie states
4. Remember the three macros: WIFEXITED (normal exit), WIFSIGNALED (killed by signal), WIFSTOPPED (suspended)
5. In exams, always mention "call wait()" as the solution to zombie prevention
