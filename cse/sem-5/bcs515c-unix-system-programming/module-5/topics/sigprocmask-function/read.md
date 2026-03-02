# Signal Masking with sigprocmask() Function

## Introduction

The `sigprocmask()` function is a fundamental system call in UNIX/Linux programming that allows processes to examine and modify their signal mask. The signal mask is a set of signals that are currently blocked from delivery to a process. Understanding how to manipulate the signal mask is crucial for writing robust concurrent programs, implementing signal handlers, and protecting critical sections of code from being interrupted by specific signals.

In the context of 's Computer Science & Engineering curriculum, signal handling forms an essential part of Unix System Programming (22CS62). The `sigprocmask()` function provides a more controlled approach to signal management compared to the basic `signal()` function, enabling programmers to temporarily block signals during critical operations and then restore the previous signal mask when done. This capability is particularly important in multi-threaded applications and when implementing custom signal handling routines.

This topic covers the syntax, parameters, return values, and practical applications of the `sigprocmask()` function, along with detailed examples and examination-relevant tips for students.

## Key Concepts

### Understanding Signal Masks

A signal mask is a set of signals that are currently blocked from being delivered to a process. When a signal is blocked, it remains pending (waiting) until the signal is unblocked. Each process has its own signal mask that can be modified using `sigprocmask()`. By default, child processes inherit the signal mask from their parent process.

### Function Prototype

```c
#include <signal.h>

int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
```

### Parameters

1. **how**: Specifies how the signal mask is modified. It can have one of three values:

- `SIG_BLOCK`: Add the signals in _set_ to the current signal mask
- `SIG_UNBLOCK`: Remove the signals in _set_ from the current signal mask
- `SIG_SETMASK`: Replace the current signal mask with _set_

2. **set**: Points to a signal set that specifies the signals to be blocked, unblocked, or used for replacement. If this is NULL, the _how_ parameter is ignored.

3. **oldset**: Points to a sigset_t object where the previous signal mask will be stored. This can be NULL if you don't need to save the previous mask.

### Return Value

- Returns 0 on success
- Returns -1 on failure and sets `errno` to indicate the error (e.g., EINVAL for invalid value of how)

### Signal Set Operations

The `<signal.h>` header provides several functions to manipulate signal sets:

```c
int sigemptyset(sigset_t *set); // Initialize empty set
int sigfillset(sigset_t *set); // Initialize set to contain all signals
int sigaddset(sigset_t *set, int signum); // Add signal to set
int sigdelset(sigset_t *set, int signum); // Remove signal from set
int sigismember(const sigset_t *set, int signum); // Check if signal in set
```

### Important Characteristics

- Signals that are blocked cannot interrupt the process
- Blocked signals remain pending until unblocked
- The `SIGKILL` and `SIGSTOP` signals cannot be blocked
- Nested calls to `sigprocmask()` are possible when saving and restoring oldset

## Examples

### Example 1: Blocking a Specific Signal

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int main() {
 sigset_t newmask, oldmask;

 // Initialize empty signal set
 sigemptyset(&newmask);

 // Add SIGINT (Ctrl+C) to the signal set
 sigaddset(&newmask, SIGINT);

 // Block SIGINT and save the old mask
 if (sigprocmask(SIG_BLOCK, &newmask, &oldmask) < 0) {
 perror("sigprocmask error");
 return 1;
 }

 printf("SIGINT is now blocked. Press Ctrl+C - nothing will happen.\n");
 sleep(5);

 // Restore the old mask (unblock SIGINT)
 if (sigprocmask(SIG_SETMASK, &oldmask, NULL) < 0) {
 perror("sigprocmask error");
 return 1;
 }

 printf("SIGINT is now unblocked. Ctrl+C will terminate.\n");
 sleep(5);

 return 0;
}
```

**Step-by-step explanation:**

1. Declare two sigset_t variables: newmask and oldmask
2. Initialize newmask to empty set using sigemptyset()
3. Add SIGINT to newmask using sigaddset()
4. Call sigprocmask() with SIG_BLOCK to block SIGINT, saving old mask
5. During the 5-second sleep, Ctrl+C is ignored
6. Restore old mask using SIG_SETMASK to unblock SIGINT

### Example 2: Temporarily Blocking Signals for Critical Section

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

volatile int counter = 0;

void handler(int sig) {
 printf("Signal %d received, counter = %d\n", sig, counter);
}

int main() {
 struct sigaction sa;
 sigset_t block_mask, old_mask;

 // Setup signal handler for SIGUSR1
 sa.sa_handler = handler;
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = 0;
 sigaction(SIGUSR1, &sa, NULL);

 // Create signal set containing SIGUSR1
 sigemptyset(&block_mask);
 sigaddset(&block_mask, SIGUSR1);

 // Critical section - block SIGUSR1
 sigprocmask(SIG_BLOCK, &block_mask, &old_mask);

 printf("Critical section started - SIGUSR1 blocked\n");

 // Simulate critical work
 for (int i = 0; i < 1000000; i++) {
 counter++;
 }
 printf("Counter value: %d\n", counter);

 // Restore previous signal mask
 sigprocmask(SIG_SETMASK, &old_mask, NULL);

 printf("Critical section ended - SIGUSR1 unblocked\n");
 return 0;
}
```

**Step-by-step explanation:**

1. Set up a signal handler for SIGUSR1 using sigaction()
2. Create a signal set containing SIGUSR1
3. Block SIGUSR1 before entering critical section
4. Perform critical work (incrementing counter)
5. Restore old signal mask to unblock SIGUSR1

### Example 3: Using sigprocmask() to Implement Signal Synchronization

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
 pid_t pid;
 sigset_t mask, oldmask;

 sigemptyset(&mask);
 sigaddset(&mask, SIGCHLD);

 // Block SIGCHLD before forking
 sigprocmask(SIG_BLOCK, &mask, &oldmask);

 pid = fork();

 if (pid == 0) {
 // Child process
 printf("Child process executing...\n");
 sleep(2);
 printf("Child exiting...\n");
 _exit(0);
 } else {
 // Parent process
 printf("Parent waiting for child (SIGCHLD blocked)...\n");

 // Even though SIGCHLD is blocked, we can still wait
 wait(NULL);

 printf("Child terminated\n");

 // Restore old mask
 sigprocmask(SIG_SETMASK, &oldmask, NULL);
 }

 return 0;
}
```

## Exam Tips

1. **Remember the three how parameters**: SIG_BLOCK adds signals to mask, SIG_UNBLOCK removes signals, SIG_SETMASK replaces entire mask.

2. **SIGKILL and SIGSTOP cannot be blocked**: These are the only two signals that cannot be masked - this is a frequently asked question in exams.

3. **Difference between signal() and sigprocmask()**: signal() sets a handler for a specific signal, while sigprocmask() controls which signals can be delivered.

4. **Return value checking**: Always check return value - returns -1 on error with errno set.

5. **oldset parameter**: Can be NULL if you don't need to save the previous mask, but saving is good practice for restoration.

6. **Blocking during signal handler**: When a signal handler is executing, that signal is automatically blocked (added to handler's sa_mask).

7. **Pending signals**: Blocked signals remain pending and are delivered when unblocked - know this concept for short answer questions.

8. **Inheritance**: Child processes inherit the parent's signal mask via fork() - this is important for understanding signal behavior in processes.

9. **sigemptyset vs sigfillset**: sigemptyset() creates an empty set (no signals), sigfillset() creates a full set (all signals).

10. **Thread safety**: sigprocmask() affects only the calling thread - in multi-threaded programs, each thread has its own signal mask.
