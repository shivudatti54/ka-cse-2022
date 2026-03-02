# sigprocmask() Function - Summary

## Key Definitions and Concepts

- **Signal Mask**: A set of signals blocked from delivery to a process
- **sigprocmask()**: System call to examine and modify the signal mask
- **Pending Signals**: Blocked signals that wait for delivery when unblocked
- **Signal Set (sigset_t)**: Data structure representing a set of signals

## Important Formulas and Function Signatures

```c
int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);

// how can be:
SIG_BLOCK   // Add signals to current mask
SIG_UNBLOCK // Remove signals from current mask
SIG_SETMASK // Replace current mask with new set

// Signal set functions:
int sigemptyset(sigset_t *set);
int sigfillset(sigset_t *set);
int sigaddset(sigset_t *set, int signum);
int sigdelset(sigset_t *set, int signum);
int sigismember(const sigset_t *set, int signum);
```

## Key Points

- sigprocmask() returns 0 on success, -1 on failure with errno set
- The oldset parameter can be NULL if previous mask need not be saved
- SIGKILL and SIGSTOP cannot be blocked under any circumstances
- Child processes inherit signal mask from parent via fork()
- Blocked signals remain pending until explicitly unblocked
- SIG_SETMASK completely replaces the mask, unlike SIG_BLOCK/SIG_UNBLOCK
- Signal handlers automatically block the signal being handled
- Each thread in a multi-threaded program has its own signal mask

## Common Mistakes to Avoid

1. **Forgetting to restore the signal mask**: Always save oldset and restore after critical section
2. **Using NULL for set without checking how**: When set is NULL, how is ignored
3. **Trying to block SIGKILL/SIGSTOP**: This will fail silently or return error
4. **Not initializing signal sets**: Always use sigemptyset() or sigfillset() before adding/removing signals

## Revision Tips

1. Practice writing programs that block SIGINT and SIGTSTP
2. Remember: SIG_BLOCK = union (add), SIG_SETMASK = replacement
3. Know that sigprocmask() only works in single-threaded context; use pthread_sigmask() for threads
4. Review the difference between ignoring a signal (SIG_IGN) and blocking it
5. Understand that wait() still works even when SIGCHLD is blocked
