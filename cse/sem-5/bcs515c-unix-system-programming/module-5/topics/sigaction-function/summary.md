# The sigaction() Function - Summary

## Key Definitions and Concepts

- **sigaction()**: A POSIX function for examining and changing the action associated with a specific signal, providing more control than the traditional signal() function.

- **struct sigaction**: A structure containing four fields - sa_handler (signal handler function), sa_mask (signals to block during handler), sa_flags (modifying flags), and sa_sigaction (extended handler for SA_SIGINFO).

- **Signal Handler**: A user-defined function called when a specific signal is delivered to a process.

- **Signal Mask**: A set of signals blocked during execution of a signal handler, specified in sa_mask field.

## Important Formulas and Theorems

The sigaction() function prototype:

```c
int sigaction(int signum, const struct sigaction *act, struct sigaction *oldact);
```

Key flags and their meanings:

- **SA_RESTART**: Automatically restart interrupted system calls
- **SA_SIGINFO**: Provide extended signal information via siginfo_t
- **SA_NOCLDSTOP**: Don't generate SIGCHLD when child stops
- **SA_NODEFER**: Don't block signal during its own handler

## Key Points

1. sigaction() returns 0 on success and -1 on error; always check return values.

2. SIGKILL and SIGSTOP cannot be caught, blocked, or ignored - they always perform their default actions.

3. When SA_SIGINFO is set, the handler receives three arguments: signal number, siginfo_t pointer, and context pointer.

4. The sa_mask field uses sigset_t - manipulated by sigemptyset(), sigfillset(), sigaddset(), sigdelset().

5. SA_RESTART does not restart all system calls; some always fail with EINTR when interrupted.

6. sigaction() provides portable behavior across different UNIX implementations, unlike signal().

7. The oldact parameter allows saving the previous signal action before installing a new one.

8. siginfo_t contains si_pid (sender's PID), si_uid (sender's UID), si_code, and si_value.

## Common Mistakes to Avoid

1. **Forgetting to initialize sa_mask**: Always use sigemptyset() or sigfillset() before using sa_mask.

2. **Confusing sa_handler and sa_sigaction**: Use sa_handler for basic handlers, sa_sigaction only when SA_SIGINFO flag is set.

3. **Not checking sigaction() return value**: Always verify success to handle error conditions properly.

4. **Using non-async-signal-safe functions in handlers**: Avoid printf(), malloc(), etc. in signal handlers; use only async-signal-safe functions.

## Revision Tips

1. Remember the sigaction structure has four fields and understand when each is used.

2. Practice writing complete signal handling programs using sigaction().

3. Memorize the purpose of each SA\_ flag as they are frequently asked in exams.

4. Understand the difference between signal() and sigaction() thoroughly.

5. Review siginfo_t structure fields as they are essential for SA_SIGINFO handlers.
