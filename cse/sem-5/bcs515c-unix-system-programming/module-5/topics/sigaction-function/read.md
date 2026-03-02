# The sigaction() Function in UNIX/Linux

## Introduction

Signal handling is a fundamental aspect of process management in UNIX/Linux operating systems. Signals are software interrupts that notify a process of the occurrence of a specific event, such as the user pressing Ctrl+C, a hardware fault, or a timer expiration. The sigaction() function provides a robust and portable mechanism for examining and changing the action associated with a specific signal. Unlike the older signal() function, sigaction() offers finer control over signal handling behavior, making it the preferred choice for writing reliable UNIX applications.

The sigaction() function was introduced to address several shortcomings in the traditional signal() system call. The primary issue with signal() is that its behavior varies across different UNIX implementations, leading to non-portable code. The sigaction() function provides a standardized interface that works consistently across POSIX-compliant systems, which is essential for modern software development. Additionally, sigaction() allows programmers to specify whether interrupted system calls should be automatically restarted, whether additional signal information should be available to the handler, and whether child process status changes should be ignored for certain signals.

In the context of 's Computer Science curriculum, understanding sigaction() is crucial for developing system-level applications, daemons, and embedded systems. This topic builds upon the fundamental concepts of signals covered in earlier modules and prepares students for advanced topics in UNIX systems programming, including process management, inter-process communication, and real-time signal handling.

## Key Concepts

### The sigaction Structure

The core of the sigaction() function is the struct sigaction, which defines the action to be taken when a signal is delivered. This structure contains several important fields:

```c
struct sigaction {
 void (*sa_handler)(int); // Signal handler function
 sigset_t sa_mask; // Signals to block during handler execution
 int sa_flags; // Special flags modifying signal behavior
 void (*sa_sigaction)(int, siginfo_t *, void *); // Alternative handler for SA_SIGINFO
};
```

The sa_handler field points to a function that handles the signal. It can be set to SIG_DFL (default action), SIG_IGN (ignore the signal), or a user-defined function. When SA_SIGINFO flag is set, the sa_sigaction field is used instead, which provides additional information about the signal origin.

### The sigaction() Function Prototype

```c
#include <signal.h>

int sigaction(int signum, const struct sigaction *act, struct sigaction *oldact);
```

The function takes three parameters: signum specifies the signal number (except SIGKILL and SIGSTOP), act is a pointer to the new action to be installed, and oldact is a pointer to store the previous action (can be NULL if not needed). The function returns 0 on success and -1 on error, with errno set appropriately.

### Important Signal Handling Flags

The sa_flags field in the sigaction structure modifies the behavior of signal handling:

- **SA_RESTART**: When set, certain system calls interrupted by this signal are automatically restarted by the kernel. This is particularly useful for I/O operations where interruption would require manual retry logic.

- **SA_SIGINFO**: When set, the signal handler receives three arguments instead of one. The second argument is a pointer to siginfo_t structure containing information about the signal, including the sending process ID, user ID, and any exit value or signal number. The third argument is an untyped pointer to additional context information.

- **SA_NOCLDSTOP**: When set for SIGCHLD, the signal is not generated when a child process stops (but it is still generated when a child terminates).

- **SA_NODEFER**: When set, the signal being handled is not automatically blocked during execution of the handler (unless explicitly included in sa_mask).

- **SA_ONSTACK**: When set, the signal is delivered to an alternate signal stack if one has been established using sigaltstack().

### Signal Sets and sigprocmask()

The sa_mask field specifies which signals should be blocked during the execution of the signal handler. Signal sets are manipulated using functions like sigemptyset(), sigfillset(), sigaddset(), and sigdelset(). Additionally, the sigprocmask() function can be used to examine or change the signal mask of the calling process, providing further control over signal delivery.

### Differences from signal() Function

The sigaction() function offers several advantages over the older signal() function. First, sigaction() provides portable behavior across different UNIX variants, while signal() semantics vary between systems. Second, sigaction() allows specification of a mask of signals to block during handler execution, preventing nested signal handling issues. Third, sigaction() supports the SA_RESTART flag for automatic system call restart. Fourth, sigaction() can retrieve the previous signal action before installing a new one, enabling dynamic restoration of handlers.

## Examples

### Example 1: Basic Signal Handling with sigaction()

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handle_sigint(int signum) {
 printf("\nReceived SIGINT (signal %d). Exiting gracefully...\n", signum);
}

int main() {
 struct sigaction sa;

 // Initialize the sigaction structure
 sa.sa_handler = handle_sigint;
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = 0; // No special flags

 // Install the signal handler for SIGINT
 if (sigaction(SIGINT, &sa, NULL) == -1) {
 perror("sigaction");
 return 1;
 }

 printf("Press Ctrl+C to trigger the signal handler...\n");

 // Infinite loop
 while (1) {
 sleep(1);
 }

 return 0;
}
```

**Step-by-step explanation:**

1. Declare a struct sigaction variable named sa
2. Set sa.sa_handler to our custom handler function handle_sigint
3. Initialize sa.sa_mask to empty set using sigemptyset()
4. Set sa.sa_flags to 0 for default behavior
5. Call sigaction() to install the handler for SIGINT
6. The program runs until Ctrl+C is pressed, triggering the handler

### Example 2: Using SA_SIGINFO for Detailed Signal Information

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>

void handle_siginfo(int signum, siginfo_t *info, void *context) {
 printf("Signal received: %d\n", signum);
 printf("Sending process PID: %d\n", info->si_pid);
 printf("Sending process UID: %d\n", info->si_uid);
 printf("Signal code: %d\n", info->si_code);
}

int main() {
 struct sigaction sa;

 sa.sa_sigaction = handle_siginfo; // Use SA_SIGINFO handler
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = SA_SIGINFO; // Enable extended information

 if (sigaction(SIGUSR1, &sa, NULL) == -1) {
 perror("sigaction");
 return 1;
 }

 printf("My PID: %d\n", getpid());
 printf("Send signal using: kill -USR1 %d\n", getpid());

 while (1) {
 pause(); // Wait for signals
 }

 return 0;
}
```

**Step-by-step explanation:**

1. Set sa.sa_sigaction instead of sa.sa_handler (for SA_SIGINFO)
2. Set sa.sa_flags to SA_SIGINFO to enable the extended handler
3. The handler receives three parameters: signal number, siginfo_t pointer, and context pointer
4. siginfo_t contains si_pid (sending process), si_uid, si_code, and other fields
5. Use pause() to block until a signal is delivered

### Example 3: Implementing Signal Masking and SA_RESTART

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <errno.h>

void handler(int signum) {
 printf("Handler executed for signal %d\n", signum);
}

int main() {
 struct sigaction sa, old_sa;

 sa.sa_handler = handler;
 sigemptyset(&sa.sa_mask);
 // Block SIGTERM during SIGUSR1 handling
 sigaddset(&sa.sa_mask, SIGTERM);
 // Restart interrupted system calls
 sa.sa_flags = SA_RESTART;

 if (sigaction(SIGUSR1, &sa, &old_sa) == -1) {
 perror("sigaction");
 return 1;
 }

 printf("Old handler address: %p\n", (void *)old_sa.sa_handler);
 printf("Sending SIGUSR1 to self...\n");
 raise(SIGUSR1);

 printf("Main function continues\n");

 return 0;
}
```

**Step-by-step explanation:**

1. The old_sa parameter captures the previous signal action
2. sigaddset() adds SIGTERM to the mask, blocking it during SIGUSR1 handling
3. SA_RESTART causes interrupted system calls (like read, write, open) to restart automatically
4. raise(SIGUSR1) sends the signal to the current process
5. This example demonstrates masking, SA_RESTART, and retrieving old action

## Exam Tips

1. **Remember the sigaction structure fields**: The four fields are sa_handler, sa_mask, sa_flags, and sa_sigaction. Know that sa_sigaction is used when SA_SIGINFO is set.

2. **Understand SA_RESTART vs no SA_RESTART**: When SA_RESTART is set, interrupted system calls are automatically restarted. Without it, system calls fail with errno set to EINTR, requiring manual retry logic.

3. **Difference between signal() and sigaction()**: sigaction() is portable, allows setting signal mask during handler execution, supports SA_RESTART, and can retrieve previous action.

4. **Signal numbers SIGKILL and SIGSTOP**: These cannot be caught, blocked, or ignored. This is a common exam question.

5. **siginfo_t structure**: Remember key fields like si_pid (process ID of sender), si_uid (user ID of sender), si_code, and si_value (signal-specific value).

6. **SA_NOCLDSTOP flag**: Used specifically with SIGCHLD to prevent signal generation when a child stops (but not when it terminates).

7. **Handling multiple signals**: Use sigaction() with properly initialized sigset_t for blocking multiple signals during handler execution.

8. **Return values**: sigaction() returns 0 on success and -1 on error. Always check return values in practical programs.

9. **Pause() and sigsuspend()**: These functions are used with sigaction() for waiting on signals. Remember that pause() suspends execution until a signal is delivered.
