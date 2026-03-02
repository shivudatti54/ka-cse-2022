# Coding Rules - Summary

## Key Definitions

- **Async-Signal-Safe Function**: A function that can be safely called from a signal handler while the same function may be executing in the main program
- **Re-entrant Function**: A function that can be safely called concurrently by multiple threads without causing data corruption
- **volatile sig_atomic_t**: A type qualifier that ensures atomic access to a variable shared between signal handlers and main program

## Important Formulas

```c
// Standard signal handler setup pattern
struct sigaction sa;
sa.sa_handler = handler_function;
sigemptyset(&sa.sa_mask);
sa.sa_flags = 0;  // or SA_RESTART
sigaction(signal_number, &sa, NULL);

// Atomic signal blocking pattern
sigset_t newmask, oldmask;
sigemptyset(&newmask);
sigaddset(&newmask, SIGTERM);
sigprocmask(SIG_BLOCK, &newmask, &oldmask);
// Critical section
sigprocmask(SIG_SETMASK, &oldmask, NULL);

// Safe waiting with sigsuspend
sigset_t waitmask;
sigemptyset(&waitmask);
sigsuspend(&waitmask);  // Atomically unblocks waitmask and waits
```

## Key Points

1. Only async-signal-safe functions can be called from signal handlers
2. Never use `printf()`, `malloc()`, `free()`, or most library functions in signal handlers
3. Always use `sigaction()` instead of `signal()` for portable behavior
4. Use `volatile sig_atomic_t` for simple flags shared between handler and program
5. Use pipes or sockets for complex data communication from handlers
6. Signal handlers should be minimal and perform only essential operations
7. `sigsuspend()` atomically replaces signal mask and waits, preventing race conditions
8. Always save and restore signal masks properly to avoid permanent signal blocking
9. Block signals during critical sections using `sigprocmask()`
10. The `SA_RESTART` flag automatically restarts some interrupted system calls

## Common Mistakes

1. **Calling printf() in signal handlers** - This causes undefined behavior; use write() instead
2. **Using signal() instead of sigaction()** - This leads to non-portable code across Unix systems
3. **Forgetting to restore signal mask** - Leaving signals permanently blocked
4. **Not using volatile for shared variables** - Compiler may optimize away variable checks
5. **Performing complex operations in handlers** - Handlers should only set flags or write to pipes
6. **Not checking return values** - Signal functions can fail; always check return codes
7. **Race conditions with signal checking** - Use sigsuspend() instead of checking flags before pause()