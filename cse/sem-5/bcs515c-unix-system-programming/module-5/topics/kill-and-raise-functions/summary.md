# Kill and Raise Functions - Summary

## Key Definitions and Concepts

- **Signal**: A software interrupt sent to a process to notify it of the occurrence of an asynchronous event.
- **kill()**: A system call that sends a signal to a specified process or process group.
- **raise()**: A function that sends a signal to the current (calling) process itself.
- **Signal Handler**: A user-defined function executed when a signal is delivered to a process.
- **Process Group**: A collection of processes identified by a process group ID (PGID), used for broadcast signal delivery.
- **Signal Disposition**: The action taken when a signal is delivered (ignore, default, or custom handler).

## Important Formulas and Theorems

- **kill() prototype**: `int kill(pid_t pid, int sig);`
- **raise() prototype**: `int raise(int sig);`
- **raise() equivalence**: `raise(sig)` is equivalent to `kill(getpid(), sig)`
- **pid interpretation**:
  - pid > 0: Signal to specific process
  - pid = 0: Signal to all processes in caller's process group
  - pid = -1: Signal to all processes (with permission check)
  - pid < -1: Signal to all processes in process group |pid|
- **Return values**: Both return 0 on success, -1 on failure with errno set.

## Key Points

- Signals provide asynchronous communication between processes in Unix/Linux systems.
- kill() allows sending signals to other processes or process groups; raise() sends to self.
- Common signals: SIGTERM (15), SIGKILL (9), SIGSTOP (19), SIGCHLD (17), SIGUSR1/SIGUSR2.
- Signal handlers are registered using signal() function with SIG_IGN, SIG_DFL, or custom handler.
- Using negative pid in kill() enables broadcast to entire process group for job control.
- Always check return values for error handling: ESRCH (process not found), EPERM (no permission), EINVAL (invalid signal).
- The kill() function is fundamental for implementing process synchronization and termination protocols.

## Common Mistakes to Avoid

1. **Forgetting to check return values**: Not checking if kill() or raise() succeeded can lead to silent failures.
2. **Confusing pid and pgid**: Using positive pid for process groups or negative values for individual processes incorrectly.
3. **Not handling signals properly**: Using non-async-signal-safe functions inside signal handlers can cause undefined behavior.
4. **Ignoring signal disposition**: Failing to set appropriate handlers before sending signals that need custom handling.

## Revision Tips

1. Practice writing programs that use fork(), kill(), and raise() together to understand process signal communication.
2. Memorize common signal numbers and their default actions for quick recall during exams.
3. Remember the pid interpretation rules in kill() - this is frequently tested in exams.
4. Review the difference between kill and raise functions by heart: kill = external signal, raise = self signal.
5. Understand process group concept as it relates to broadcast signals - negative pid sends to entire group.
