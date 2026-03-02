# Alarm and Pause Functions - Summary

## Key Definitions and Concepts

- **alarm()**: POSIX function that schedules a SIGALRM signal to be delivered after a specified number of seconds. Prototype: `unsigned int alarm(unsigned int seconds)`

- **pause()**: POSIX function that suspends process execution until a signal is received. Prototype: `int pause(void)`

- **SIGALRM**: Signal number 14, raised by alarm() when the timer expires; default action is process termination

- **Race condition**: Potential issue when using alarm and pause where the signal arrives before pause() is called, causing indefinite blocking

## Important Formulas and Theorems

- `alarm(seconds)` returns previously pending alarm seconds remaining (0 if none)
- `alarm(0)` cancels any pending alarm without scheduling new one
- `pause()` returns -1 with errno=EINTR when interrupted by signal handler

## Key Points

- Always set alarm BEFORE pause to avoid race conditions
- Use sigaction() instead of signal() for portable and robust signal handling
- Default SIGALRM action terminates the process - always install a handler
- Alarms are NOT inherited across fork() but persist across exec()
- alarm(0) cancels pending alarms; returns remaining time from previous alarm
- Signal handlers should only use async-signal-safe functions
- setitimer() provides more features than alarm() including repeated timers
- The volatile sig_atomic_t type ensures atomic operations in signal handlers

## Common Mistakes to Avoid

1. Calling pause() before alarm() - causes race condition and potential indefinite sleep
2. Not installing signal handler for SIGALRM - leads to process termination
3. Using printf() in signal handlers - printf is not async-signal-safe
4. Forgetting to cancel alarm after successful operation - causes spurious timeouts
5. Not checking return values from alarm and pause functions

## Revision Tips

- Practice writing code that implements timeouts using alarm and pause
- Remember the critical order: alarm() first, then pause()
- Review sigaction structure and its sa_flags options
- Understand when to use alarm() versus setitimer() for different timing needs
- Be able to trace through code examples to predict behavior with different alarm/pause orderings
