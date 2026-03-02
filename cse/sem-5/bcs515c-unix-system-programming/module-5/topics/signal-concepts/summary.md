# Signal Concepts - Summary

## Key Definitions

- **Signal**: A software interrupt delivered to a process to notify it of asynchronous events; identified by a small positive integer (signal number)
- **Signal Handler**: A user-defined function invoked when a specific signal is delivered to a process
- **Signal Disposition**: The association between a signal and the action to perform when the signal is delivered
- **Signal Mask**: A set of signals blocked from delivery to a process; stored in the process control block
- **Pending Signal**: A signal that has been generated but not yet delivered because it is currently blocked
- **Async-Signal-Safe**: Functions that can be safely called from within a signal handler without causing race conditions or data corruption

## Important Formulas

- Signal number range: 1 to SIGRTMAX (typically 64 on modern systems)
- sigaction structure: `struct sigaction { void (*sa_handler)(int); sigset_t sa_mask; int sa_flags; }`
- Signal set operations: sigemptyset(), sigfillset(), sigaddset(), sigdelset(), sigismember()
- Signal mask operations: sigprocmask(how, set, oldset) where how is SIG_BLOCK, SIG_UNBLOCK, or SIG_SETMASK

## Key Points

1. Signals are asynchronous notifications that can interrupt a process at any point during execution
2. Each signal has a default action: terminate (with/without core dump), stop, ignore, or continue
3. The sigaction() interface is preferred over signal() for reliable and portable signal handling
4. Signal handlers should only use async-signal-safe functions to avoid undefined behavior
5. The signal mask determines which signals are blocked; blocked signals remain pending until unblocked
6. Signal delivery occurs when the process transitions from kernel mode to user mode
7. Multiple occurrences of standard signals while pending typically result in only one delivery
8. The sa_mask in sigaction specifies additional signals to block during handler execution
9. Race conditions can occur between checking pending signals and blocking; use sigsuspend() atomically
10. The volatile sig_atomic_t type ensures atomic reads/writes for variables shared between handlers and main code

## Common Mistakes

1. **Using non-async-signal-safe functions in handlers**: Calling printf(), malloc(), or other unsafe functions in signal handlers can cause deadlocks or corruption
2. **Race conditions with signal masking**: Using separate sigprocmask() and pause() calls creates a window where signals can be missed
3. **Ignoring signal handler return**: Handlers should return void and not attempt to return values
4. **Forgetting to initialize signal sets**: Always use sigemptyset() or sigfillset() before using sigset_t variables
5. **Not checking return values**: Functions like sigaction() and sigprocmask() return -1 on error; always check for failures
6. **Assuming immediate signal delivery**: Signals are delivered at safe points, not immediately when generated
7. **Using wrong signal numbers**: Remember that signal numbers vary between systems; use symbolic constants (SIGTERM, SIGINT) instead of magic numbers
8. **Confusing SIG_DFL and SIG_IGN**: SIG_DFL restores default action, SIG_IGN completely ignores the signal