# Signal Handling: sigpending() - Summary

## Key Definitions and Concepts

- **Pending Signal**: A signal that has been generated but cannot be delivered because it is currently blocked by the signal mask
- **Signal Mask**: A set of signals blocked for a process; signals in this set become pending rather than being delivered immediately
- **sigpending()**: POSIX function that retrieves the set of signals pending for the calling process

## Important Formulas and Theorems

```c
int sigpending(sigset_t *set);
// Returns: 0 on success, -1 on error
```

- **sigemptyset(&set)**: Initialize empty set (no signals)
- **sigfillset(&set)**: Initialize full set (all signals)
- **sigaddset(&set, signum)**: Add signal to set
- **sigdelset(&set, signum)**: Remove signal from set
- **sigismember(&set, signum)**: Test membership (returns 1 if true, 0 if false)

## Key Points

- sigpending() allows examination of pending signals without altering the signal mask
- Pending signals are automatically delivered when unblocked
- The sigset_t type represents signal sets as bit arrays
- Multiple occurrences of standard signals may result in only one delivery
- sigpending() is commonly used with sigprocmask() for sophisticated signal control
- The function is part of POSIX.1-2001 and POSIX.1-2008 standards
- In multithreaded processes, pending signals are process-wide
- Always check return values for error handling in production code

## Common Mistakes to Avoid

1. **Forgetting to initialize sigset_t**: Always use sigemptyset() or sigfillset() before using a sigset_t variable
2. **Confusing pending with delivered**: Pending signals are blocked; delivered signals have invoked their handlers
3. **Not checking return values**: sigpending() can fail; always check for -1 return
4. **Incorrect signal mask manipulation**: Using wrong how parameter in sigprocmask() can accidentally unblock all signals

## Revision Tips

1. Draw a flow diagram showing: Signal Generated → Check Mask → If blocked, add to pending → If unblocked, deliver immediately
2. Practice writing code that blocks signals, sends signals to self, uses sigpending(), then unblocks
3. Remember: Pending ⊆ Blocked (pending signals are always a subset of blocked signals)
4. Review the relationship between sigprocmask() and sigpending() as they work together
5. Study the difference between sigaction()-based and signal()-based handler installation
