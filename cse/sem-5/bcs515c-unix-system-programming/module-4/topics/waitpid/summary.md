# waitpid() System Call - Summary

## Key Definitions and Concepts

- **waitpid()**: A system call that allows a parent process to wait for a specific child process to terminate or change state, providing more control than the basic wait() function.

- **Zombie Process**: A terminated child process that remains in the process table until its parent reads its exit status via wait()/waitpid().

- **Process Group**: A collection of processes identified by a process group ID; waitpid() with pid=0 waits for any child in the same process group.

## Important Formulas and Theorems

**Function Prototype:**

```c
pid_t waitpid(pid_t pid, int *status, int options);
```

**Status Interpretation Macros:**

- `WIFEXITED(status)` → True if normal exit
- `WEXITSTATUS(status)` → Exit code (0-255)
- `WIFSIGNALED(status)` → True if killed by signal
- `WTERMSIG(status)` → Signal number that killed process
- `WIFSTOPPED(status)` → True if process was stopped
- `WIFCONTINUED(status)` → True if process resumed

## Key Points

- The pid parameter determines which child to wait for: >0 for specific PID, 0 for process group, -1 for any child, <-1 for specific process group ID.

- WNOHANG makes waitpid() non-blocking - returns 0 immediately if no child has exited instead of blocking.

- waitpid() returns the child's PID on success, 0 (with WNOHANG) if no status available yet, -1 on error.

- Always check the status using WIFEXITED/WIFSIGNALED macros before using WEXITSTATUS/WTERMSIG.

- Using waitpid(-1, &status, 0) is equivalent to wait(&status).

- The status parameter can be NULL if the caller doesn't need exit status information.

## Common Mistakes to Avoid

1. **Not checking status before extracting exit code**: Always verify WIFEXITED is true before using WEXITSTATUS.

2. **Forgetting to wait for children**: This leads to zombie processes accumulating and eventually exhausting process table entries.

3. **Incorrect use of WNOHANG in loops**: Some students check once and assume child is done, rather than looping properly.

4. **Confusing pid=-1 with pid=0**: Remember -1 waits for any child, 0 waits for same process group only.

## Revision Tips

1. Practice writing programs that create multiple child processes and wait for each using waitpid().

2. Memorize the status macros and their purposes - these are frequently asked in exams.

3. Understand the difference between WNOHANG, WUNTRACED, and WCONTINUED options.

4. Trace through code examples to understand the flow of parent and child processes.

5. Review the relationship between fork(), exit(), and waitpid() in process lifecycle.
