# Signal Sets - Summary

## Key Definitions

- **Signal Set (sigset_t)**: An opaque data type that represents a collection of signals, used for operations involving multiple signals simultaneously.

- **Signal Mask**: The set of signals currently blocked from delivery to a process; managed using signal sets and `sigprocmask()`.

- **Pending Signals**: Signals that have been generated but are blocked from delivery, waiting in a pending queue.

## Important Formulas

| Function | Purpose |
|----------|---------|
| `sigemptyset(set)` | Initialize empty set (no signals) |
| `sigfillset(set)` | Initialize full set (all signals) |
| `sigaddset(set, signum)` | Add signal to set |
| `sigdelset(set, signum)` | Remove signal from set |
| `sigismember(set, signum)` | Test signal membership (returns 1, 0, or -1) |
| `sigprocmask(how, set, oldset)` | Modify signal mask using signal sets |
| `sigpending(set)` | Retrieve pending signals into set |

## Key Points

1. Always initialize `sigset_t` variables with `sigemptyset()` or `sigfillset()` before use.

2. Signal sets enable efficient management of multiple signals through bit-mask operations.

3. `sigprocmask()` with `SIG_BLOCK` adds signals to the mask, `SIG_UNBLOCK` removes them, and `SIG_SETMASK` replaces the mask.

4. When a blocked signal arrives, it becomes pending rather than being delivered immediately.

5. Only one instance of each signal can be pending; multiple occurrences are coalesced.

6. Child processes inherit the signal mask from parent via `fork()`, but `exec()` resets it.

7. Use `pthread_sigmask()` instead of `sigprocmask()` in multithreaded applications.

8. The `oldset` parameter in `sigprocmask()` allows restoration of the previous signal mask.

9. Signal sets in `sigaction` structures specify which signals to block during handler execution.

10. `sigpending()` is essential for detecting signals that arrived while they were blocked.

## Common Mistakes

1. **Using uninitialized signal sets**: Failing to call `sigemptyset()` or `sigfillset()` leads to undefined behavior.

2. **Confusing return values**: `sigismember()` returns 1 (member), 0 (not member), and -1 (error)—not just true/false.

3. **Forgetting signal number limits**: Using invalid signal numbers with set manipulation functions causes `EINVAL`.

4. **Incorrect sigprocmask usage**: Using `SIG_SETMASK` when intending to add signals, which replaces rather than adds to the mask.