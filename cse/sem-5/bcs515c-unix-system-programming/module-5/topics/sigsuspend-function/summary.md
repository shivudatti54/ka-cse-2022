# Signal Handling: The sigsuspend Function - Summary

## Key Definitions and Concepts

- **sigsuspend()**: A system call that atomically replaces the signal mask and suspends the process until a signal is delivered
- **Signal Mask**: A set of signals blocked from delivery to a process
- **Atomic Operation**: An operation that executes completely without interruption, preventing race conditions
- **Signal Set**: A data structure (`sigset_t`) used to represent a group of signals

## Important Formulas and Theorems

- **Function Prototype**: `int sigsuspend(const sigset_t *sigmask)`
- **Return Value**: Always returns -1 (interrupted by signal), `errno = EINTR`
- **Key Property**: Signal mask is automatically restored after return
- **Atomic Property**: Mask change + suspension happens as single uninterruptible unit

## Key Points

1. `sigsuspend()` solves the race condition between `sigprocmask()` and `pause()`
2. It temporarily replaces the signal mask with the provided argument
3. The original signal mask is automatically restored after the function returns
4. Use `sigprocmask()` to block signals before using `sigsuspend()`
5. `sigsuspend()` never returns successfully - always interrupted by a signal
6. Each thread in a multi-threaded program can have its own signal mask
7. Use `volatile sig_atomic_t` for flag variables shared with signal handlers

## Common Mistakes to Avoid

1. **Forgetting to block signals first**: Always use `sigprocmask()` before `sigsuspend()` to block the signals you want to wait for
2. **Race conditions**: Never use separate `sigprocmask()` and `pause()` calls - use `sigsuspend()` instead
3. **Ignoring EINTR**: Always check for `EINTR` return value in production code
4. **Wrong mask in sigsuspend()**: Pass the OLD mask (saved before blocking) to restore original state during wait

## Revision Tips

1. Remember the typical pattern: Block signals → Save old mask → Call `sigsuspend(&oldmask)` → Mask auto-restored
2. The key advantage is ATOMICITY - no signals can be lost between mask change and suspension
3. Compare with `pause()`: `pause()` doesn't change mask, `sigsuspend()` does temporarily
4. Practice writing code that handles SIGUSR1 or SIGTERM using `sigsuspend()`
5. Draw a timeline to visualize how race conditions occur without `sigsuspend()`
