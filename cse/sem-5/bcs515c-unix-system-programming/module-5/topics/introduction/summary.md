# Introduction to Signals in Unix System Programming - Summary

## Key Definitions

- **Signal**: A software interrupt delivered to a process by the operating system to notify it of an asynchronous event.
- **Signal Disposition**: The action associated with a signal, determining how a process responds when the signal is delivered.
- **Signal Handler**: A user-defined function executed when a specific signal is delivered to a process.
- **Signal Mask**: A set of signals that are currently blocked from delivery to a process.
- **Async-Signal-Safe**: Functions that can be safely called from within a signal handler without causing undefined behavior.

## Important Formulas

- Signal identification: Each signal is identified by a small positive integer constant (e.g., SIGINT = 2, SIGTERM = 15).
- Default signal actions: terminate, terminate with core dump, stop, continue, or ignore.
- Signal disposition setting: `sigaction(signum, &new_action, &old_action)`

## Key Points

1. Signals are asynchronous notifications that interrupt normal program flow to handle specific events.

2. The kernel delivers signals when events occur, and processes can respond by catching, ignoring, or using default actions.

3. POSIX sigaction() is the preferred method for signal handling due to its reliability and portability.

4. Common signals include SIGINT (Ctrl+C), SIGTERM (termination request), SIGKILL (cannot be caught), SIGSEGV (segmentation fault), and SIGCHLD (child terminated).

5. Signals cannot be generated for blocked signals; they remain pending until unblocked.

6. Child processes inherit signal dispositions from their parent through fork().

7. Signal handlers must only call async-signal-safe functions to avoid race conditions and undefined behavior.

8. The kill() system call allows processes to send signals to other processes using their PIDs.

9. SIGKILL and SIGSTOP cannot be caught, blocked, or ignored by user programs.

10. The pause() function suspends process execution until a signal is delivered.

## Common Mistakes

1. **Using printf() in signal handlers**: printf() is not async-signal-safe and can cause deadlocks or corruption. Use write() instead.

2. **Assuming signals are queued**: Traditional Unix signals do not queue; if multiple identical signals arrive while blocked, only one is delivered.

3. **Forgetting to reset signal masks**: When using sigsetjmp/siglongjmp, failing to restore the signal mask can leave signals permanently blocked.

4. **Not checking return values**: Ignoring return values from sigaction() and other signal-related functions can lead to undetected errors.

5. **Confusing SIGTERM and SIGKILL**: SIGTERM allows graceful termination and can be caught, while SIGKILL forcibly terminates immediately and cannot be handled.