# Signal Handling: The sigsuspend Function

## Introduction

In UNIX/LINUX operating systems, signal handling is a crucial mechanism for inter-process communication and asynchronous event management. The `sigsuspend()` function is a powerful system call used to temporarily change the signal mask of a process and wait for a signal to be delivered. Unlike simple functions like `pause()` or `sleep()`, `sigsuspend()` provides atomic operation on signal masks, making it essential for implementing critical sections protected by signals.

The `sigsuspend()` function is particularly important in scenarios where a process needs to block certain signals while waiting for a specific condition, then restore the original signal mask after the wait. This functionality is extensively used in implementing synchronization primitives and handling race conditions in multi-threaded and signal-driven programming. Understanding `sigsuspend()` is essential for CSE students as it forms the foundation for advanced signal handling techniques in UNIX systems programming.

## Key Concepts

### What is sigsuspend()?

The `sigsuspend()` function temporarily replaces the signal mask of the calling thread with the mask provided by the `sigmask` argument and then suspends the thread until a signal is delivered. Upon return, the signal mask is restored to its original value before the call. This atomic operation ensures that no signals can be delivered between changing the mask and suspending the process, which is critical for avoiding race conditions.

**Function Prototype:**

```c
#include <signal.h>
int sigsuspend(const sigset_t *sigmask);
```

**Parameters:**

- `sigmask`: Pointer to a signal set that specifies the new signal mask. This set replaces the current signal mask during the suspension.

**Return Value:**

- Returns -1 if interrupted by a signal, and `errno` is set to `EINTR`.
- On success, the function does not return (it suspends until a signal is caught).

### The Need for sigsuspend()

Consider a scenario where a process wants to wait for a specific signal while blocking other signals. Simply using `pause()` after changing the signal mask using `sigprocmask()` creates a race condition:

```c
sigset_t mask, oldmask;
sigemptyset(&mask);
sigaddset(&mask, SIGUSR1);
sigprocmask(SIG_BLOCK, &mask, &oldmask); // Block SIGUSR1
/* Race condition window here! */
pause(); // Wait for any signal
sigprocmask(SIG_SETMASK, &oldmask, NULL); // Restore mask
```

Between the `sigprocmask()` and `pause()` calls, a SIGUSR1 signal could be delivered but lost because `pause()` would not be waiting for it. The `sigsuspend()` function solves this atomicity problem.

### Signal Mask Operations

The signal mask determines which signals are blocked from delivery to a process. Key operations include:

- `sigemptyset()`: Initializes an empty signal set
- `sigfillset()`: Initializes a full signal set
- `sigaddset()`: Adds a signal to a set
- `sigdelset()`: Removes a signal from a set
- `sigismember()`: Checks if a signal is in a set

### Atomic Nature of sigsuspend()

The critical advantage of `sigsuspend()` is its atomic execution. The kernel ensures that:

1. The signal mask is changed to the provided value
2. The process is suspended waiting for a signal
3. Both operations happen as a single uninterruptible unit

No signals can be lost in the gap between mask change and suspension, preventing race conditions.

### Difference Between sigsuspend(), pause(), and sleep()

| Function       | Purpose                             | Signal Mask Behavior                            |
| -------------- | ----------------------------------- | ----------------------------------------------- |
| `sigsuspend()` | Wait for signals with specific mask | Temporarily replaces mask atomically            |
| `pause()`      | Wait for any signal                 | Does not change signal mask                     |
| `sleep()`      | Wait for timeout                    | Does not change signal mask, can be interrupted |

## Examples

### Example 1: Basic sigsuspend() Usage

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handler(int sig) {
 printf("Caught signal %d\n", sig);
}

int main() {
 struct sigaction sa;
 sigset_t mask, oldmask;

 // Setup signal handler for SIGUSR1
 sa.sa_handler = handler;
 sa.sa_flags = 0;
 sigemptyset(&sa.sa_mask);
 sigaction(SIGUSR1, &sa, NULL);

 // Block SIGUSR1
 sigemptyset(&mask);
 sigaddset(&mask, SIGUSR1);
 sigprocmask(SIG_BLOCK, &mask, &oldmask);

 printf("SIGUSR1 is blocked. Sending signal...\n");
 printf("Calling sigsuspend() to wait for SIGUSR1\n");

 // Wait for SIGUSR1 while it's blocked
 sigsuspend(&oldmask); // Use oldmask (unblock SIGUSR1)

 printf("After sigsuspend() returned\n");

 // Restore original mask
 sigprocmask(SIG_SETMASK, &oldmask, NULL);

 return 0;
}
```

**Step-by-step execution:**

1. SIGUSR1 is blocked using `sigprocmask()`
2. Original mask is saved in `oldmask`
3. `sigsuspend(&oldmask)` temporarily unblocks SIGUSR1 and suspends
4. When SIGUSR1 arrives, handler executes, then `sigsuspend()` returns
5. Original signal mask is restored

### Example 2: Implementing a Wait for Specific Signal

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>

volatile sig_atomic_t done = 0;

void sigterm_handler(int sig) {
 done = 1;
}

int main() {
 sigset_t block_sigterm, wait_sigterm, oldmask;

 // Setup handler for SIGTERM
 struct sigaction sa;
 sa.sa_handler = sigterm_handler;
 sa.sa_flags = 0;
 sigemptyset(&sa.sa_mask);
 sigaction(SIGTERM, &sa, NULL);

 // Create sets
 sigemptyset(&block_sigterm);
 sigaddset(&block_sigterm, SIGTERM);

 // Block SIGTERM
 sigprocmask(SIG_BLOCK, &block_sigterm, &oldmask);

 printf("Process running. Send SIGTERM to terminate...\n");

 // Wait in a loop until SIGTERM is received
 while (!done) {
 // Create wait set: block all except SIGTERM
 sigfillset(&wait_sigterm);
 sigdelset(&wait_sigterm, SIGTERM);
 sigsuspend(&wait_sigterm);
 }

 // Restore original mask
 sigprocmask(SIG_SETMASK, &oldmask, NULL);

 printf("Process terminated gracefully.\n");
 return 0;
}
```

### Example 3: Critical Section Protection

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void alarm_handler(int sig) {
 printf("Alarm triggered - critical section interrupted\n");
}

int main() {
 sigset_t mask, oldmask, wait_mask;

 // Setup alarm handler
 struct sigaction sa;
 sa.sa_handler = alarm_handler;
 sa.sa_flags = 0;
 sigemptyset(&sa.sa_mask);
 sigaction(SIGALRM, &sa, NULL);

 // Block SIGALRM
 sigemptyset(&mask);
 sigaddset(&mask, SIGALRM);
 sigprocmask(SIG_BLOCK, &mask, &oldmask);

 // Start critical section
 printf("Starting critical section...\n");

 // Set alarm for 2 seconds
 alarm(2);

 // Wait for alarm (unblocked) while protecting from other signals
 sigemptyset(&wait_mask);
 sigsuspend(&wait_mask);

 printf("Exiting critical section\n");

 sigprocmask(SIG_SETMASK, &oldmask, NULL);
 return 0;
}
```

## Exam Tips

1. **Atomic Operation**: Remember that `sigsuspend()` performs mask change and suspension atomically - this is its primary advantage over separate `sigprocmask()` and `pause()` calls.

2. **Return Value**: `sigsuspend()` always returns -1 when interrupted by a signal, with `errno` set to `EINTR`. It never returns successfully.

3. **Signal Mask Restoration**: After `sigsuspend()` returns, the signal mask is automatically restored to its original state before the call.

4. **Common Usage Pattern**: The typical pattern is: block desired signals, save old mask, call `sigsuspend()` with the old mask to temporarily unblock, then original mask is restored automatically.

5. **Difference from pause()**: Unlike `pause()` which only suspends until any signal arrives, `suspenspend()` allows specifying which signals to unblock during wait.

6. **EINTR Handling**: Always check for `EINTR` return value to handle interrupted system calls properly in production code.

7. **Thread Safety**: `sigsuspend()` affects the signal mask of the calling thread. In multi-threaded programs, each thread can have its own signal mask.

8. **Volatile Variables**: When using flag variables in signal handlers, declare them as `volatile sig_atomic_t` to ensure atomic access and proper optimization.

9. **Comparison with sigwaitinfo()**: `suspenspend()` is used with signal handlers, while `sigsuspend()` is used when you want to synchronously wait for signals in a specific masked state.
