# Process Wait Operations - Summary

## Key Definitions and Concepts

- **wait()**: System call that suspends parent process until a child terminates, returning the child's PID and storing exit status
- **waitpid()**: Extended version allowing waiting for specific children or non-blocking checks
- **Zombie Process**: Defunct process that has terminated but whose entry remains in process table until parent calls wait()
- **Orphan Process**: Child whose parent has terminated; adopted by init process (PID 1)
- **Exit Status**: Value passed by child to parent via exit() call, examined using status macros

## Important Formulas and Theorems

- **wait() syntax**: `pid_t wait(int *status)`
- **waitpid() syntax**: `pid_t waitpid(pid_t pid, int *status, int options)`
- **PID interpretation**: pid > 0 (specific child), pid = 0 (any child in process group), pid = -1 (any child), pid < -1 (process group |pid|)

## Key Points

- Parent process must call wait() to prevent zombie process accumulation
- Status macros extract different information: WIFEXITED checks normal exit, WEXITSTATUS gets exit code
- waitpid() with WNOHANG option performs non-blocking check - returns 0 if child running
- Orphan processes are adopted by init which periodically calls wait() to clean them
- wait() blocks indefinitely; waitpid() with WNOHANG returns immediately
- WIFSIGNALED and WTERMSIG used when child is terminated by a signal
- Multiple children can be waited for using waitpid() with pid = -1 in a loop

## Common Mistakes to Avoid

- Forgetting to call wait() in parent, leading to zombie process buildup
- Confusing wait() return value (-1 on error) with child PID (positive on success)
- Not checking WIFEXITED before calling WEXITSTATUS - status is only valid if WIFEXITED is true
- Using uninitialized status variable without checking for errors

## Revision Tips

1. Remember: Parent must wait - zombies form when parent ignores terminated children
2. Practice writing code with fork(), exit(), and wait() together
3. Memorize the macro purpose: WIF\* checks condition, WEXIT/WTERMSIG extracts value
4. For exam: Remember that wait() = waitpid(-1, &status, 0)
5. Keep in mind that init (PID 1) prevents system-wide zombie accumulation by adopting orphans
