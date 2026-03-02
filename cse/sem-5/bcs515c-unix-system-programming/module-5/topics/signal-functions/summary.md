# Signal Functions - Summary

## Key Definitions

- **Signal**: A software interrupt delivered to a process to notify it of an asynchronous event
- **Signal Handler**: A function executed when a specific signal is delivered to a process
- **Signal Mask**: The set of signals blocked from delivery to a process
- **Pending Signal**: A signal that has been generated but not yet delivered because it is blocked
- **Async-signal-safe**: Functions that can be safely called from within signal handlers

## Important Formulas

```c
// signal() handler typedef
void (*signal(int signum, void (*handler)(int)))(int);

// sigaction() structure
struct sigaction {
    void (*sa_handler)(int);
    sigset_t sa_mask;
    int sa_flags;
    void (*sa_sigaction)(int, siginfo_t *, void *);
};

// Key function prototypes
int sigaction(int signum, const struct sigaction *act, struct sigaction *oldact);
int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
int sigpending(sigset_t *set);
int sigsuspend(const sigset_t *mask);
int sigsetjmp(sigjmp_buf env, int savemask);
void siglongjmp(sigjmp_buf env, int val);
```

## Key Points

1. The signal() function provides a simple but non-portable interface for signal handling; sigaction() is the POSIX-standard reliable alternative

2. Signal handlers registered with signal() may be reset to default after first delivery in some implementations, requiring re-registration

3. The sa_flags field in struct sigaction controls handler behavior: SA_RESTART restarts system calls, SA_SIGINFO provides extended signal information

4. Signal masks are inherited across fork() but reset in exec() - important for understanding process behavior

5. Only async-signal-safe functions (approximately 120+ functions) can be safely called from signal handlers

6. sigsuspend() atomically replaces the signal mask and suspends the process, preventing race conditions

7. The raise() function sends a signal to the same process, while kill() can send to other processes

8. sigwaitinfo() and sigtimedwait() provide synchronous signal waiting for multithreaded applications

## Common Mistakes

1. **Using printf() in signal handlers**: Most standard library functions are not async-signal-safe; use write() instead for debugging

2. **Race conditions with pause()**: Never combine sigprocmask() and pause() separately; use sigsuspend() for atomic operations

3. **Forgetting to reset signal handlers**: In some implementations, handlers are automatically reset after first invocation when using signal()

4. **Incorrect signal set initialization**: Always use sigemptyset() or sigfillset() before using sigset_t variables; uninitialized sets have undefined contents

5. **Blocking critical signals**: Remember that SIGKILL and SIGSTOP cannot be blocked - attempting to do so results in EINVAL