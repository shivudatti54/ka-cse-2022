# Signal Handling and Signal Sets

## Introduction to Signals

Signals are software interrupts delivered to a process by the operating system or another process. They represent a fundamental mechanism for inter-process communication (IPC) and process control in Unix/Linux systems. Signals can notify a process of various events, such as hardware exceptions, terminal activity, or requests from other processes.

### What are Signals?

Signals are asynchronous notifications sent to a process to indicate that a specific event has occurred. Each signal is represented by a small integer value with a symbolic name (e.g., `SIGINT`, `SIGTERM`, `SIGKILL`).

**Key characteristics of signals:**

- Asynchronous: Can arrive at any time during process execution
- Predefined types: Standard signals have specific meanings
- Default actions: Each signal has a default behavior
- Custom handling: Processes can define their own signal handlers

### Common Unix Signals

| Signal  | Value    | Default Action | Description                                |
| ------- | -------- | -------------- | ------------------------------------------ |
| SIGHUP  | 1        | Terminate      | Hangup detected on controlling terminal    |
| SIGINT  | 2        | Terminate      | Interrupt from keyboard (Ctrl+C)           |
| SIGQUIT | 3        | Core dump      | Quit from keyboard (Ctrl+\)                |
| SIGKILL | 9        | Terminate      | Kill signal (cannot be caught or ignored)  |
| SIGTERM | 15       | Terminate      | Termination signal                         |
| SIGSTOP | 17,19,23 | Stop           | Stop process (cannot be caught or ignored) |
| SIGCONT | 18,19,25 | Continue       | Continue if stopped                        |
| SIGCHLD | 20,17,18 | Ignore         | Child stopped or terminated                |

## Signal Handling Functions

### Basic Signal Management

The `signal()` function is the traditional way to set a signal handler:

```c
#include <signal.h>

void (*signal(int sig, void (*func)(int)))(int);
```

**Example:**

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void sigint_handler(int sig) {
    printf("\nReceived SIGINT (Ctrl+C)\n");
}

int main() {
    signal(SIGINT, sigint_handler);

    while(1) {
        printf("Running...\n");
        sleep(1);
    }

    return 0;
}
```

### Modern Signal Handling with sigaction()

The `sigaction()` function provides more control and reliability:

```c
#include <signal.h>

int sigaction(int sig, const struct sigaction *act,
              struct sigaction *oact);
```

**Example using sigaction():**

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handler(int sig) {
    write(STDOUT_FILENO, "Signal received!\n", 17);
}

int main() {
    struct sigaction sa;

    sa.sa_handler = handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;

    if (sigaction(SIGINT, &sa, NULL) == -1) {
        perror("sigaction");
        return 1;
    }

    while(1) {
        pause(); // Wait for signals
    }

    return 0;
}
```

## Signal Sets (sigset_t)

Signal sets are data structures used to represent multiple signals. They are essential for advanced signal handling operations.

### Signal Set Operations

```c
#include <signal.h>

int sigemptyset(sigset_t *set);      // Initialize empty set
int sigfillset(sigset_t *set);       // Initialize full set
int sigaddset(sigset_t *set, int signum);  // Add signal to set
int sigdelset(sigset_t *set, int signum);  // Remove signal from set
int sigismember(const sigset_t *set, int signum); // Test membership
```

**Example: Creating and manipulating signal sets**

```c
#include <stdio.h>
#include <signal.h>

int main() {
    sigset_t my_set;

    // Initialize empty set
    sigemptyset(&my_set);

    // Add signals to set
    sigaddset(&my_set, SIGINT);
    sigaddset(&my_set, SIGTERM);
    sigaddset(&my_set, SIGQUIT);

    // Check if SIGINT is in set
    if (sigismember(&my_set, SIGINT)) {
        printf("SIGINT is in the set\n");
    }

    // Remove SIGTERM from set
    sigdelset(&my_set, SIGTERM);

    return 0;
}
```

## Process Signal Mask

The signal mask determines which signals are currently blocked from delivery to a process.

### Blocking and Unblocking Signals

```c
#include <signal.h>

int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
```

**How values:**

- `SIG_BLOCK`: Add signals to current mask
- `SIG_UNBLOCK`: Remove signals from current mask
- `SIG_SETMASK`: Replace current mask with new mask

**Example: Blocking signals temporarily**

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int main() {
    sigset_t new_mask, old_mask;

    // Create set with SIGINT
    sigemptyset(&new_mask);
    sigaddset(&new_mask, SIGINT);

    // Block SIGINT
    sigprocmask(SIG_BLOCK, &new_mask, &old_mask);

    printf("SIGINT is now blocked. Try Ctrl+C...\n");
    sleep(5);

    // Restore original mask
    sigprocmask(SIG_SETMASK, &old_mask, NULL);
    printf("SIGINT unblocked\n");

    sleep(5);
    return 0;
}
```

## Advanced Signal Handling

### Waiting for Specific Signals

The `sigsuspend()` function atomically changes the signal mask and waits for a signal:

```c
#include <signal.h>

int sigsuspend(const sigset_t *mask);
```

**Example:**

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handler(int sig) {
    printf("Received signal %d\n", sig);
}

int main() {
    struct sigaction sa;
    sigset_t mask;

    sa.sa_handler = handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;

    sigaction(SIGINT, &sa, NULL);

    // Block all signals except SIGINT
    sigfillset(&mask);
    sigdelset(&mask, SIGINT);

    printf("Waiting for SIGINT (Ctrl+C)...\n");
    sigsuspend(&mask);

    printf("Done\n");
    return 0;
}
```

### Signal Handling in Critical Sections

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

volatile sig_atomic_t flag = 0;

void handler(int sig) {
    flag = 1;
}

void critical_section() {
    sigset_t block_mask, old_mask;

    // Block SIGINT during critical section
    sigemptyset(&block_mask);
    sigaddset(&block_mask, SIGINT);
    sigprocmask(SIG_BLOCK, &block_mask, &old_mask);

    // Critical section code
    printf("In critical section - signals blocked\n");
    sleep(3);
    printf("Critical section completed\n");

    // Restore signal mask
    sigprocmask(SIG_SETMASK, &old_mask, NULL);

    // Check if signal arrived during blocking
    if (flag) {
        printf("SIGINT was received during critical section\n");
        flag = 0;
    }
}

int main() {
    struct sigaction sa;

    sa.sa_handler = handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    sigaction(SIGINT, &sa, NULL);

    while(1) {
        critical_section();
        sleep(2);
    }

    return 0;
}
```

## Signal Delivery and Handling

### Signal Delivery Process

```
Process Execution
    |
    |---> Signal Generated
    |         |
    |         |--> If signal blocked? -- Yes --> Add to pending signals
    |         |     |
    |         |     No
    |         |--> If signal ignored? -- Yes --> Discard signal
    |         |     |
    |         |     No
    |         |--> Deliver to signal handler or default action
    |
    |---> Return to normal execution
```

### Pending Signals

Pending signals are those that have been generated but not yet delivered. The system maintains a set of pending signals for each process.

```c
#include <signal.h>

int sigpending(sigset_t *set);  // Retrieve pending signals
```

**Example: Checking pending signals**

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int main() {
    sigset_t block_mask, pending_mask;

    // Block SIGINT and SIGTERM
    sigemptyset(&block_mask);
    sigaddset(&block_mask, SIGINT);
    sigaddset(&block_mask, SIGTERM);
    sigprocmask(SIG_BLOCK, &block_mask, NULL);

    printf("SIGINT and SIGTERM blocked for 5 seconds...\n");
    printf("Try generating these signals (Ctrl+C or kill command)\n");

    sleep(5);

    // Check pending signals
    sigpending(&pending_mask);

    if (sigismember(&pending_mask, SIGINT)) {
        printf("SIGINT is pending\n");
    }

    if (sigismember(&pending_mask, SIGTERM)) {
        printf("SIGTERM is pending\n");
    }

    // Unblock signals
    sigprocmask(SIG_UNBLOCK, &block_mask, NULL);
    printf("Signals unblocked - pending signals will be delivered\n");

    return 0;
}
```

## Real-World Applications

### Signal Handling in Server Applications

```c
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>

volatile sig_atomic_t shutdown_requested = 0;

void graceful_shutdown(int sig) {
    shutdown_requested = 1;
}

void setup_signal_handlers() {
    struct sigaction sa;

    sa.sa_handler = graceful_shutdown;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;

    // Handle termination signals
    sigaction(SIGTERM, &sa, NULL);
    sigaction(SIGINT, &sa, NULL);

    // Ignore SIGPIPE (broken pipe)
    sa.sa_handler = SIG_IGN;
    sigaction(SIGPIPE, &sa, NULL);
}

int main() {
    setup_signal_handlers();

    printf("Server started (PID: %d)\n", getpid());

    while (!shutdown_requested) {
        // Main server loop
        printf("Processing...\n");
        sleep(1);
    }

    printf("Shutting down gracefully...\n");
    // Cleanup code here
    printf("Server stopped\n");

    return 0;
}
```

## Exam Tips

1. **Remember the difference between `signal()` and `sigaction()`**: `sigaction()` is more portable and provides better control over signal handling behavior.

2. **Understand signal blocking**: Signals can be blocked during critical sections to prevent race conditions.

3. **Know the special signals**: `SIGKILL` and `SIGSTOP` cannot be caught, blocked, or ignored.

4. **Use `volatile sig_atomic_t`**: For global variables accessed in signal handlers, use this type to ensure proper behavior.

5. **Remember reentrancy**: Signal handlers should be reentrant and avoid calling non-reentrant functions.

6. **Understand the signal mask**: Each process has a signal mask that determines which signals are currently blocked.

7. **Practice with signal sets**: Be comfortable with `sigemptyset()`, `sigfillset()`, `sigaddset()`, `sigdelset()`, and `sigismember()`.

8. **Know the default actions**: For common signals like `SIGINT` (terminate), `SIGQUIT` (core dump), `SIGCHLD` (ignore).
