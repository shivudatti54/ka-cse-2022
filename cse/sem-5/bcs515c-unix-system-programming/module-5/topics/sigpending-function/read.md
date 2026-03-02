# Signal Handling: The sigpending() Function

## Introduction

In Unix/Linux operating systems, signal handling is a fundamental mechanism for inter-process communication and asynchronous event notification. When a signal is generated but blocked (using the signal mask), it becomes a "pending" signal. The operating system maintains a set of pending signals for each process, and the sigpending() function provides a way to examine which signals are currently pending. This topic is crucial for understanding advanced signal programming in operating systems, particularly for 's Operating Systems course under the 2022 scheme.

The sigpending() function is part of the POSIX signal handling API and is extensively used in real-world applications such as daemon processes, signal-driven I/O, and multithreaded applications. Understanding how to check pending signals allows programmers to implement sophisticated signal handling strategies where signals can be temporarily blocked and later examined or processed according to application logic.

## Key Concepts

### Understanding Pending Signals

When a signal is generated, the operating system checks if the signal is currently blocked for the process. If the signal is blocked, it is added to the process's "pending signals" set. If the signal is not blocked, it is immediately delivered to the process, invoking the associated signal handler. The sigpending() function allows a process to examine which signals are currently pending (blocked and waiting to be delivered).

A signal can be pending when:

1. The signal is generated while the process has blocked it
2. The signal handler was established using sigaction() with the SA_RESTART flag
3. Multiple occurrences of the same signal can be pending (implementation-dependent)

### The sigpending() Function Prototype

```c
#include <signal.h>

int sigpending(sigset_t *set);
```

The function stores the set of signals that are pending for the calling process in the space pointed to by set. It returns 0 on success and -1 on failure, with errno set to indicate the error.

### The sigset_t Data Type

The sigset_t data type is an abstract data type used to represent signal sets. It is implemented as a bit array where each bit corresponds to a particular signal. Several functions are used to manipulate signal sets:

- **sigemptyset()**: Initializes an empty signal set
- **sigfillset()**: Initializes a full signal set (all signals included)
- **sigaddset()**: Adds a signal to a signal set
- **sigdelset()**: Removes a signal from a signal set
- **sigismember()**: Tests whether a signal is a member of a signal set

### Signal Mask and sigpending()

The signal mask determines which signals are blocked for a process. When a signal is blocked, it becomes pending rather than being delivered immediately. The relationship between the signal mask and pending signals is fundamental:

1. A signal can be blocked using sigprocmask()
2. Blocked signals are stored in the pending set
3. sigpending() retrieves pending signals
4. When a signal is unblocked, if it was pending, it gets delivered

### Relationship with sigprocmask()

The sigprocmask() function is used to examine and change the signal mask. Together, sigprocmask() and sigpending() provide complete control over signal handling:

```c
#include <signal.h>

int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
```

The how argument specifies how the signal mask is changed:

- **SIG_BLOCK**: Add signals to current mask
- **SIG_UNBLOCK**: Remove signals from current mask
- **SIG_SETMASK**: Replace current mask with new set

## Examples

### Example 1: Basic Use of sigpending()

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handler(int signum) {
 printf("Signal %d received\n", signum);
}

int main() {
 struct sigaction sa;
 sigset_t block_set, pending_set, old_set;

 // Setup signal handler for SIGINT
 sa.sa_handler = handler;
 sa.sa_flags = 0;
 sigemptyset(&sa.sa_mask);
 sigaction(SIGINT, &sa, NULL);

 // Block SIGINT
 sigemptyset(&block_set);
 sigaddset(&block_set, SIGINT);
 sigprocmask(SIG_BLOCK, &block_set, &old_set);

 printf("SIGINT is now blocked. Sending SIGINT...\n");
 kill(getpid(), SIGINT);

 // Check pending signals
 sigpending(&pending_set);
 if (sigismember(&pending_set, SIGINT)) {
 printf("SIGINT is pending\n");
 }

 // Unblock SIGINT - it will now be delivered
 printf("Unblocking SIGINT...\n");
 sigprocmask(SIG_SETMASK, &old_set, NULL);

 return 0;
}
```

**Step-by-step explanation:**

1. A signal handler is installed for SIGINT
2. SIGINT is blocked using sigprocmask() with SIG_BLOCK
3. SIGINT is sent to itself using kill()
4. Since SIGINT is blocked, it becomes pending
5. sigpending() retrieves the pending signal set
6. sigismember() checks if SIGINT is in the pending set
7. When SIGINT is unblocked, the pending signal is delivered

### Example 2: Handling Multiple Pending Signals

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int sigint_count = 0;
int sigterm_count = 0;

void handler(int signum) {
 if (signum == SIGINT) sigint_count++;
 if (signum == SIGTERM) sigterm_count++;
}

int main() {
 struct sigaction sa;
 sigset_t block_set, pending_set;

 sa.sa_handler = handler;
 sa.sa_flags = 0;
 sigemptyset(&sa.sa_mask);
 sigaction(SIGINT, &sa, NULL);
 sigaction(SIGTERM, &sa, NULL);

 // Block both SIGINT and SIGTERM
 sigemptyset(&block_set);
 sigaddset(&block_set, SIGINT);
 sigaddset(&block_set, SIGTERM);
 sigprocmask(SIG_BLOCK, &block_set, NULL);

 // Send multiple signals
 printf("Sending signals...\n");
 for (int i = 0; i < 3; i++) {
 kill(getpid(), SIGINT);
 }
 kill(getpid(), SIGTERM);

 // Check pending signals
 sigpending(&pending_set);
 printf("Pending SIGINT: %s\n",
 sigismember(&pending_set, SIGINT) ? "Yes" : "No");
 printf("Pending SIGTERM: %s\n",
 sigismember(&pending_set, SIGTERM) ? "Yes" : "No");

 // Unblock all signals
 sigprocmask(SIG_UNBLOCK, &block_set, NULL);

 printf("Delivered: SIGINT=%d, SIGTERM=%d\n",
 sigint_count, sigterm_count);

 return 0;
}
```

**Expected Output:**

```
Sending signals...
Pending SIGINT: Yes
Pending SIGTERM: Yes
Delivered: SIGINT=3, SIGTERM=1
```

### Example 3: Real-World Application - Signal-Driven Processing

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>

volatile sig_atomic_t got_signal = 0;

void sig_handler(int signum) {
 got_signal = 1;
}

void process_pending_signals() {
 sigset_t pending, blocked, old_mask;
 sigpending(&pending);
 sigprocmask(SIG_BLOCK, NULL, &blocked);

 // Check and process each signal we're interested in
 if (sigismember(&pending, SIGUSR1)) {
 printf("Processing SIGUSR1\n");
 // Process SIGUSR1 specific task
 }
 if (sigismember(&pending, SIGUSR2)) {
 printf("Processing SIGUSR2\n");
 // Process SIGUSR2 specific task
 }
}

int main() {
 struct sigaction sa;

 sa.sa_handler = sig_handler;
 sa.sa_flags = 0;
 sigemptyset(&sa.sa_mask);
 sigaction(SIGUSR1, &sa, NULL);
 sigaction(SIGUSR2, &sa, NULL);

 // Block signals temporarily
 sigset_t block_set;
 sigemptyset(&block_set);
 sigaddset(&block_set, SIGUSR1);
 sigaddset(&block_set, SIGUSR2);
 sigprocmask(SIG_BLOCK, &block_set, NULL);

 // Simulate receiving signals while blocked
 printf("Simulating incoming signals...\n");
 kill(getpid(), SIGUSR1);
 sleep(1);
 kill(getpid(), SIGUSR2);

 // Check and process pending signals before continuing
 printf("Checking pending signals...\n");
 process_pending_signals();

 printf("Continuing normal execution\n");

 return 0;
}
```

## Exam Tips

1. **Remember the function signature**: sigpending(sigset_t \*set) returns 0 on success and -1 on failure. This is frequently asked in exams.

2. **Understand the difference between blocked and pending**: A blocked signal is held in the pending set until explicitly unblocked. sigpending() queries which signals are in this pending set.

3. **sigpending() vs sigprocmask()**: sigprocmask() modifies the signal mask (what is blocked), while sigpending() queries what is pending (blocked but not yet delivered).

4. **Key relationship**: If a signal is in the pending set, it is guaranteed to be blocked. The pending set is always a subset of the blocked signals.

5. **sigismember() usage**: When examining the result of sigpending(), use sigismember() to test if a specific signal is pending.

6. **Real-time signals**: For real-time signals (SIGRTMIN to SIGRTMAX), multiple occurrences of the same signal can be queued and pending. Check your implementation.

7. **Thread considerations**: In multithreaded programs, pending signals are process-wide. However, only one thread can handle a signal.

8. **Common error handling**: Always check return values from sigpending() and other signal functions for error conditions.
