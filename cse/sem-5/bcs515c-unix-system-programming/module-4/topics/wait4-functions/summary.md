# Wait Functions - Summary

## Key Definitions and Concepts

- **Zombie Process**: A child process that has terminated but retains its process table entry until the parent collects its status via wait()
- **wait()**: System call that blocks until any child process terminates, returning the child's PID and storing termination status
- **waitpid()**: Extended version allowing waiting for specific children or non-blocking waiting via options
- **Orphan Process**: A child whose parent has terminated; adopted by init process (PID 1)

## Important Formulas and Macros

- **wait(&status)**: Blocks until any child terminates; returns child PID or -1
- **waitpid(pid, &status, options)**: Waits for specific process/group; options include WNOHANG, WUNTRACED
- **WIFEXITED(status)**: True if normal exit
- **WEXITSTATUS(status)**: Returns exit code (0-255)
- **WIFSIGNALED(status)**: True if killed by signal
- **WTERMSIG(status)**: Returns signal number
- **wait3()/wait4()**: Extended calls returning struct rusage with resource utilization

## Key Points

1. Parent processes MUST call wait() to prevent zombie accumulation
2. wait() blocks indefinitely; waitpid() with WNOHANG returns immediately
3. Status must be checked with WIF\* macros before extracting specific information
4. waitpid(-1, ...) behaves identically to wait()
5. Negative pid values in waitpid() operate on process groups
6. wait4() provides most comprehensive functionality (specific pid + resource info)
7. If parent doesn't call wait(), init process automatically handles orphaned zombies

## Common Mistakes to Avoid

- Using WEXITSTATUS() without first checking WIFEXITED() - leads to undefined behavior
- Forgetting to call wait() in parent - causes zombie processes
- Using wait() when specific child waiting is needed - blocks unnecessarily
- Not checking return value of wait() - treating errors as valid child termination

## Revision Tips

1. Remember the lifecycle: Fork → Execute → Terminate → Zombie → wait() collected → Process entry freed
2. Practice identifying when to use WNOHANG vs blocking wait()
3. Memorize the macro checking sequence: WIFEXITED → WIFSIGNALED → WIFSTOPPED → WIFCONTINUED
4. Remember that wait3/wait4 provide additional resource usage data (CPU time, page faults, I/O)
5. For exam: focus on understanding when and why each wait variant is preferred over others
