# Process Synchronization: wait() and waitpid() - Summary

## Key Definitions and Concepts

- **wait()**: System call that suspends parent execution until a child terminates, returning child's PID and storing exit status
- **waitpid()**: Extended version allowing specific child selection and non-blocking behavior via options parameter
- **wait3()**: Variant that additionally returns resource usage statistics in struct rusage
- **Zombie process**: Defunct process that has terminated but parent hasn't called wait() to collect status
- **Orphan process**: Running child whose parent has terminated; adopted by init process

## Important Formulas and Functions

```c
pid_t wait(int *status);
pid_t waitpid(pid_t pid, int *status, int options);
pid_t wait3(int *status, int options, struct rusage *rusage);
```

Key macros for status extraction:

- `WIFEXITED(status)` - True if normal exit
- `WEXITSTATUS(status)` - Extracts exit code (0-255)
- `WIFSIGNALED(status)` - True if killed by signal
- `WTERMSIG(status)` - Extracts signal number
- `WIFSTOPPED(status)` - True if stopped (not terminated)

Options for waitpid: `WNOHANG`, `WUNTRACED`, `WCONTINUE`

## Key Points

- wait() blocks until ANY child terminates; returns first available
- waitpid(-1, &status, 0) is equivalent to wait(&status)
- WNOHANG prevents blocking - returns 0 if no child exited
- Always call wait()/waitpid() in parent to prevent zombie processes
- Exit status is stored in lower 8 bits; signal number in lower 7 bits
- wait3() provides CPU time, page faults, context switches via rusage
- init process (PID 1) reaps orphans to prevent zombie accumulation

## Common Mistakes to Avoid

- Not calling wait()/waitpid() - leads to zombie process accumulation
- Using wrong status macros (e.g., using WTERMSIG on normally exited process)
- Forgetting that wait() returns only on child termination, not when child is stopped
- Not checking return value of wait() - can miss ECHILD error (no children)
- Confusing wait3() with waitpid() - different purposes and return structures

## Revision Tips

1. Practice writing code that spawns children and properly waits for them
2. Memorize the status macro definitions and their purposes
3. Understand the difference between WNOHANG and blocking wait behavior
4. Remember that wait3() is used when resource usage monitoring is needed
5. Review zombie process prevention techniques for exam questions
