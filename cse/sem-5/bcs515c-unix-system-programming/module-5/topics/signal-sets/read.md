# Signal Sets in Unix System Programming

## Introduction

Signal sets are fundamental data structures in Unix System Programming that allow programmers to work with multiple signals simultaneously. In POSIX-compliant systems, a signal set is represented by the `sigset_t` data type, which serves as a collection mechanism for storing information about multiple signals. The concept of signal sets becomes essential when working with advanced signal handling functions such as `sigprocmask()`, `sigpending()`, and `sigaction()`, where operations often involve blocking, unblocking, or examining multiple signals at once.

The signal set mechanism provides a clean and efficient way to manage signal masks, which determine which signals are currently blocked from delivery to a process. Understanding signal sets is crucial for writing robust concurrent programs and daemon processes that require precise control over signal delivery and handling. This topic covers the definition of signal sets, the functions provided for manipulating them, and practical examples demonstrating their usage in real-world Unix programming scenarios.

## Key Concepts

### The sigset_t Data Type

The `sigset_t` is an opaque data type defined in the `<signal.h>` header file that represents a set of signals. The internal implementation is system-dependent, but it is typically implemented as a bit mask or a structure containing bit fields. Programs should treat `sigset_t` as an opaque type and use the provided manipulation functions to modify signal sets, rather than directly accessing its internal representation.

The size of `sigset_t` must be sufficient to represent all signals defined in the system. The number of distinct signals supported varies across different Unix implementations, but POSIX guarantees that `sigset_t` can represent at least 32 different signals. On most modern systems, it can handle significantly more signals, including real-time signals.

### Signal Set Manipulation Functions

POSIX defines five primary functions for manipulating signal sets, each serving a specific purpose in signal set management.

The `sigemptyset()` function initializes a signal set to contain no signals. Its prototype is:

```c
int sigemptyset(sigset_t *set);
```

This function must be called before using a signal set variable, as the contents of `sigset_t` variables are not automatically initialized. Upon success, it returns 0; on failure, it returns -1 and sets `errno`.

The `sigfillset()` function initializes a signal set to contain all signals supported by the system:

```c
int sigfillset(sigset_t *set);
```

This function is particularly useful when you want to block all signals or when working with `sigprocmask()` to temporarily disable all signal handling. Like `sigemptyset()`, it returns 0 on success and -1 on failure.

The `sigaddset()` function adds a specified signal to an existing signal set:

```c
int sigaddset(sigset_t *set, int signum);
```

The `signum` parameter specifies the signal number to add. This function returns 0 on success and -1 on failure, with `EINVAL` returned if an invalid signal number is specified.

The `sigdelset()` function removes a specified signal from a signal set:

```c
int sigdelset(sigset_t *set, int signum);
```

This function is the inverse of `sigaddset()` and is used when you want to selectively remove signals from a set. It returns 0 on success and -1 on failure with `EINVAL` for invalid signal numbers.

The `sigismember()` function tests whether a specified signal is a member of a signal set:

```c
int sigismember(const sigset_t *set, int signum);
```

This function returns 1 if the specified signal is a member of the set, 0 if it is not, and -1 if an error occurs with `EINVAL` for invalid signal numbers.

### Signal Mask Operations

Signal sets are primarily used with `sigprocmask()` to manipulate the signal mask of a process. The signal mask is the set of signals whose delivery is currently blocked. The `sigprocmask()` function can add signals to the mask (blocking them), remove signals from the mask (unblocking them), or set the mask to a specific value.

The function prototype is:

```c
int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
```

The `how` parameter specifies the operation to perform: `SIG_BLOCK` adds signals to the current mask, `SIG_UNBLOCK` removes signals from the current mask, and `SIG_SETMASK` replaces the current mask with the new set. The `oldset` parameter, if not NULL, receives the previous signal mask, which can be useful for restoring the original mask later.

### Pending Signals

When a signal is blocked, it becomes pending rather than being delivered immediately. The `sigpending()` function retrieves the set of signals that are pending for the process:

```c
int sigpending(sigset_t *set);
```

Upon successful completion, the signal set pointed to by `set` contains all signals that are pending (blocked and waiting for delivery). This function is useful for checking which signals have arrived while they were blocked.

## Examples

### Example 1: Blocking and Unblocking Signals

The following example demonstrates how to use signal sets to block and unblock the SIGINT signal:

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handler(int sig) {
 printf("Caught signal %d\n", sig);
}

int main() {
 struct sigaction sa;
 sigset_t block_set, old_set, pending_set;

 /* Set up the signal handler */
 sa.sa_handler = handler;
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = 0;
 sigaction(SIGINT, &sa, NULL);

 /* Initialize an empty signal set */
 sigemptyset(&block_set);

 /* Add SIGINT to the signal set */
 sigaddset(&block_set, SIGINT);

 /* Block SIGINT and save the old mask */
 sigprocmask(SIG_BLOCK, &block_set, &old_set);
 printf("SIGINT is now blocked. Press Ctrl+C - nothing will happen.\n");
 sleep(5);

 /* Check for pending signals */
 sigpending(&pending_set);
 if (sigismember(&pending_set, SIGINT)) {
 printf("SIGINT is pending.\n");
 }

 /* Restore the old signal mask (unblock SIGINT) */
 sigprocmask(SIG_SETMASK, &old_set, NULL);
 printf("SIGINT is now unblocked.\n");

 /* If SIGINT was pressed, it will be delivered now */
 sleep(5);

 return 0;
}
```

This example shows the complete workflow of blocking signals using signal sets. The program blocks SIGINT for 5 seconds, checks if any signals are pending, then restores the original mask allowing any pending SIGINT to be delivered.

### Example 2: Blocking Multiple Signals

This example demonstrates handling multiple signals simultaneously using signal sets:

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handler(int sig) {
 const char *name = strsignal(sig);
 printf("Caught signal %d (%s)\n", sig, name);
}

int main() {
 sigset_t signal_set, old_set;
 struct sigaction sa;

 /* Initialize signal set and add multiple signals */
 sigemptyset(&signal_set);
 sigaddset(&signal_set, SIGINT); /* Ctrl+C */
 sigaddset(&signal_set, SIGTERM); /* Termination request */
 sigaddset(&signal_set, SIGQUIT); /* Ctrl+\ */

 /* Set up the handler with the signal set */
 sa.sa_handler = handler;
 sa.sa_mask = signal_set; /* Block these signals during handler */
 sa.sa_flags = 0;

 sigaction(SIGINT, &sa, NULL);
 sigaction(SIGTERM, &sa, NULL);
 sigaction(SIGQUIT, &sa, NULL);

 /* Block all these signals */
 sigprocmask(SIG_BLOCK, &signal_set, &old_set);

 printf("SIGINT, SIGTERM, and SIGQUIT are blocked.\n");
 printf("PID: %d\n", getpid());
 printf("Sleeping for 10 seconds. Send signals to see pending behavior.\n");

 sleep(10);

 /* Check which signals are pending */
 sigset_t pending;
 sigpending(&pending);

 printf("\nPending signals:\n");
 if (sigismember(&pending, SIGINT)) printf(" SIGINT is pending\n");
 if (sigismember(&pending, SIGTERM)) printf(" SIGTERM is pending\n");
 if (sigismember(&pending, SIGQUIT)) printf(" SIGQUIT is pending\n");

 /* Restore old mask */
 sigprocmask(SIG_SETMASK, &old_set, NULL);
 printf("\nSignals unblocked. Pending signals will be delivered.\n");

 return 0;
}
```

This program demonstrates blocking multiple signals, checking for pending signals, and how signals accumulate when blocked. The signal handler is set to block the same signals during execution, preventing nested signal handling.

### Example 3: Selective Signal Blocking in Multithreaded Environment

Signal sets are particularly important in multithreaded programs where signal handling must be carefully controlled:

```c
#include <stdio.h>
#include <signal.h>
#include <pthread.h>
#include <unistd.h>

sigset_t mask;

void* thread_function(void* arg) {
 int sig;

 /* This thread will wait for signals */
 sigwait(&mask, &sig);
 printf("Thread received signal: %d\n", sig);

 return NULL;
}

int main() {
 pthread_t tid;

 /* Initialize the signal set */
 sigemptyset(&mask);
 sigaddset(&mask, SIGUSR1);
 sigaddset(&mask, SIGUSR2);

 /* Block signals in the main thread - they will be handled by sigwait */
 pthread_sigmask(SIG_BLOCK, &mask, NULL);

 /* Create a thread to handle the signals */
 pthread_create(&tid, NULL, thread_function, NULL);

 printf("Sending SIGUSR1...\n");
 kill(getpid(), SIGUSR1);
 sleep(1);

 printf("Sending SIGUSR2...\n");
 kill(getpid(), SIGUSR2);
 sleep(1);

 pthread_join(tid, NULL);

 return 0;
}
```

This example shows a common pattern in multithreaded programs where signals are blocked in all threads and a specific thread uses `sigwait()` to handle them synchronously. The signal set is used to specify which signals the dedicated thread should handle.

## Exam Tips

1. **Remember Initialization**: Always call `sigemptyset()` or `sigfillset()` before using a `sigset_t` variable. Using an uninitialized signal set leads to undefined behavior.

2. **Signal Set Functions Return Values**: Most signal set functions return 0 on success and -1 on failure. Always check return values in production code, especially when validating signal numbers.

3. **Difference Between sigemptyset and sigfillset**: `sigemptyset()` creates an empty set (no signals), while `sigfillset()` creates a full set (all signals). Choose based on whether you want to add or remove signals.

4. **sigprocmask Operations**: Remember that `SIG_BLOCK` adds to the mask, `SIG_UNBLOCK` removes from the mask, and `SIG_SETMASK` replaces the mask entirely.

5. **Pending Signals Behavior**: If multiple instances of the same signal arrive while blocked, only one instance becomes pending. However, different signals each become pending.

6. **sigismember Return Values**: Note that `sigismember()` returns 1 for membership, 0 for non-membership, and -1 for errors. Test carefully to avoid confusion between 0 and -1.

7. **Signal Mask Inheritance**: Child processes inherit the parent's signal mask via `fork()`, but the mask is reset in the child of `exec()`.

8. **Thread Safety**: The `sigprocmask()` function is not thread-safe; use `pthread_sigmask()` in multithreaded programs instead.

9. **Relationship with sigaction**: Signal sets are used in `struct sigaction` to specify which signals should be blocked while a signal handler executes.

10. **Common Pitfalls**: A common mistake is forgetting that signal numbers vary between systems. Always use symbolic constants like `SIGINT` rather than magic numbers.
