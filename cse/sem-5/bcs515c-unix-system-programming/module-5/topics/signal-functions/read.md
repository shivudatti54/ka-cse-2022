# Signal Functions in Unix System Programming

## Introduction

Signals are software interrupts that provide a mechanism for notifying processes about asynchronous events. In Unix systems, signals are a fundamental method of communication between processes and the kernel, allowing programs to respond to various conditions such as keyboard interrupts, timer expirations, and program errors. Understanding signal functions is essential for developing robust Unix applications that can handle exceptional conditions gracefully.

The signal mechanism in Unix dates back to early versions of the operating system and has evolved through several standards, including POSIX. Originally, the signal() function provided a simple interface, but it had limitations regarding reliability and portability. The POSIX standard introduced the sigaction() function, which offers more control and reliability for signal handling. Modern Unix programming predominantly uses sigaction() for its superior features, though signal() remains available for backward compatibility.

This topic covers the various functions available for signal management in Unix, including signal registration, signal manipulation, and advanced features like signal masks and jump functions. A thorough understanding of these functions enables programmers to create responsive and fault-tolerant applications.

## Key Concepts

### The signal() Function

The signal() function is the traditional Unix interface for specifying how a process handles a specific signal. Its prototype is:

```c
#include <signal.h>
void (*signal(int signum, void (*handler)(int)))(int);
```

The function takes two parameters: the signal number (signum) and a pointer to a signal handler function. The handler function receives the signal number as its sole parameter. The return value is a pointer to the previously installed handler, or SIG_ERR on error.

Three special handler values can be specified: SIG_DFL restores the default action for the signal, SIG_IGN ignores the signal, and a custom handler function address installs user-defined handling. For example, to handle SIGINT (Ctrl+C):

```c
void handler(int signum) {
 printf("Caught signal %d\n", signum);
}

int main() {
 signal(SIGINT, handler);
 // ... rest of program
}
```

### The sigaction() Function

The sigaction() function provides a more robust and flexible interface for signal handling. Its prototype is:

```c
#include <signal.h>
int sigaction(int signum, const struct sigaction *act, struct sigaction *oldact);
```

The sigaction structure contains several important fields:

```c
struct sigaction {
 void (*sa_handler)(int); // signal handler
 sigset_t sa_mask; // signals to block during handler
 int sa_flags; // special flags
 void (*sa_sigaction)(int, siginfo_t *, void *); // alternative handler
};
```

The sa_flags field can include various options such as SA_RESTART (restart interrupted system calls), SA_SIGINFO (use the sa_sigaction handler with additional information), and SA_NODEFER (don't block signal during its own handler).

### Signal Sets and Manipulation Functions

Signal sets are used to represent collections of signals. The sigset_t data type holds a set of signals, and several functions manipulate these sets:

- **sigemptyset()**: Initializes an empty signal set
- **sigfillset()**: Initializes a set to contain all signals
- **sigaddset()**: Adds a signal to a set
- **sigdelset()**: Removes a signal from a set
- **sigismember()**: Tests whether a signal is in a set

```c
sigset_t signal_set;
sigemptyset(&signal_set); // clear all signals
sigaddset(&signal_set, SIGINT); // add SIGINT
sigaddset(&signal_set, SIGTERM); // add SIGTERM
if (sigismember(&signal_set, SIGINT)) {
 printf("SIGINT is in the set\n");
}
```

### Signal Mask Management

The sigprocmask() function allows processes to examine and change the signal mask, which determines which signals are blocked from delivery:

```c
#include <signal.h>
int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
```

The how parameter specifies the operation: SIG_BLOCK adds signals to the mask, SIG_UNBLOCK removes signals from the mask, and SIG_SETMASK replaces the mask entirely. The oldset parameter can retrieve the previous mask if not NULL.

### Signal Pending Status

The sigpending() function returns the set of signals that have been sent to the process but are currently blocked:

```c
#include <signal.h>
int sigpending(sigset_t *set);
```

This allows programs to check which pending signals would be delivered if they were unblocked.

### Atomic Signal Operations with sigsetjmp/siglongjmp

When implementing signal handlers that must perform non-local jumps, sigsetjmp() and siglongjmp() provide safe alternatives to the standard setjmp/longjmp:

```c
#include <setjmp.h>
int sigsetjmp(sigjmp_buf env, int savemask);
void siglongjmp(sigjmp_buf env, int val);
```

The savemask parameter, when non-zero, causes the signal mask to be saved in env and restored by siglongjmp().

### The sigsuspend() Function

The sigsuspend() function atomically changes the signal mask and waits for a signal:

```c
#include <signal.h>
int sigsuspend(const sigset_t *mask);
```

This is essential for implementing critical sections where a specific set of signals must be unblocked atomically, preventing race conditions.

## Examples

### Example 1: Basic Signal Handling with signal()

```c
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void handle_alarm(int signum) {
 printf("Alarm clock! Process %d received SIGALRM\n", getpid());
}

int main() {
 printf("Setting up signal handler for SIGALRM\n");

 if (signal(SIGALRM, handle_alarm) == SIG_ERR) {
 perror("signal");
 exit(1);
 }

 alarm(5); // schedule alarm after 5 seconds
 printf("Waiting for alarm...\n");
 pause(); // wait for signal

 printf("Exiting normally\n");
 return 0;
}
```

This program registers a handler for SIGALRM, schedules an alarm, and waits for its delivery using pause(). When the alarm fires, the handler executes and prints a message.

### Example 2: Using sigaction() with SA_SIGINFO

```c
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void handler(int signum, siginfo_t *info, void *context) {
 printf("Received signal %d\n", signum);
 printf("Signal sender PID: %d\n", info->si_pid);
 printf("Signal code: %d\n", info->si_code);
}

int main() {
 struct sigaction sa;

 sa.sa_sigaction = handler;
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = SA_SIGINFO; // request extended information

 if (sigaction(SIGUSR1, &sa, NULL) == -1) {
 perror("sigaction");
 exit(1);
 }

 printf("Sending myself SIGUSR1...\n");
 raise(SIGUSR1); // send signal to self

 return 0;
}
```

This example demonstrates the use of SA_SIGINFO to receive additional information about the signal, including the PID of the sending process and signal code.

### Example 3: Protecting Critical Sections with sigsuspend()

```c
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

volatile sig_atomic_t flag = 0;

void handler(int signum) {
 flag = 1;
}

int main() {
 sigset_t block_mask, old_mask, wait_mask;

 // Setup signal handler
 signal(SIGUSR1, handler);

 // Initialize signal sets
 sigemptyset(&block_mask);
 sigaddset(&block_mask, SIGUSR1);

 sigemptyset(&wait_mask);

 // Block SIGUSR1
 if (sigprocmask(SIG_BLOCK, &block_mask, &old_mask) < 0) {
 perror("sigprocmask block");
 exit(1);
 }

 // Critical section - SIGUSR1 is blocked
 printf("In critical section (SIGUSR1 blocked)\n");
 sleep(3);

 // Atomically unblock SIGUSR1 and wait
 printf("Waiting for SIGUSR1...\n");
 sigsuspend(&wait_mask);

 // Restore old mask
 sigprocmask(SIG_SETMASK, &old_mask, NULL);

 if (flag) {
 printf("Flag was set - signal was handled\n");
 }

 return 0;
}
```

This program demonstrates proper protection of critical sections using sigprocmask() and sigsuspend() to prevent race conditions when handling signals.

## Exam Tips

1. **Remember signal() vs sigaction()**: The signal() function is simpler but less reliable across different Unix implementations. sigaction() is the POSIX-standard, more robust choice for production code.

2. **Understand signal masks**: The signal mask determines which signals are blocked. Use sigprocmask() to modify it, and remember that blocked signals are queued until unblocked.

3. **SA_RESTART flag**: When set, this flag automatically restarts certain interrupted system calls. Be aware of which system calls support this feature.

4. **sig_atomic_t**: Use this type for variables accessed in signal handlers and main program to ensure atomic operations.

5. **Signal-safe functions**: Only async-signal-safe functions (like write(), \_exit(), etc.) should be called from signal handlers. Avoid printf() and other unsafe functions in production handlers.

6. **Race condition prevention**: Always use sigsuspend() when you need to atomically unblock signals and wait, never combine sigprocmask() and pause() separately.

7. **Default signal actions**: Know that some signals (like SIGKILL and SIGSTOP) cannot be caught, blocked, or ignored. This is crucial for exam questions about signal handling.
