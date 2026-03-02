# Signal Functions in Unix System Programming

## Introduction to Signals

Signals are software interrupts delivered to a process by the kernel, another process, or the process itself. They provide a mechanism for handling asynchronous events in Unix systems. When a signal is sent to a process, the normal flow of execution is interrupted, and if the process has registered a signal handler, that function is executed.

### Basic Signal Concepts

Signals serve various purposes:

- Notification of events (e.g., child process termination)
- Error conditions (e.g., segmentation fault)
- User-initiated interrupts (e.g., Ctrl+C)
- Process control (e.g., stopping/resuming processes)

Each signal has a unique integer value and a symbolic name defined in `<signal.h>`. Common signals include:

- SIGINT (2): Interrupt from keyboard (Ctrl+C)
- SIGKILL (9): Kill signal (cannot be caught or ignored)
- SIGTERM (15): Termination signal
- SIGSEGV (11): Segmentation violation
- SIGCHLD (17): Child process terminated or stopped

## Signal Generation and Delivery

**Signal Generation**: The event that causes a signal to be created
**Signal Delivery**: The process of invoking the signal handler or default action

```
+----------------+      Generate       +-----------------+
| Event Source   | ------------------> | Signal Queue    |
| (Kernel, User, |                    | of Process      |
|   Process)     | <------------------ |                 |
+----------------+      Deliver        +-----------------+
                              |
                              v
                      +-----------------+
                      | Signal Handler  |
                      | or Default Action|
                      +-----------------+
```

## Signal Functions

### 1. signal() Function

The `signal()` function is the basic interface for establishing signal handlers.

**Syntax:**

```c
#include <signal.h>

void (*signal(int signum, void (*handler)(int)))(int);
```

**Parameters:**

- `signum`: Signal number to handle
- `handler`: Function pointer to the signal handler

**Handler options:**

- `SIG_DFL`: Default action
- `SIG_IGN`: Ignore the signal
- Function pointer: Custom signal handler

**Example:**

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void sigint_handler(int sig) {
    printf("Caught SIGINT (Ctrl+C)\n");
}

int main() {
    // Register signal handler for SIGINT
    if (signal(SIGINT, sigint_handler) == SIG_ERR) {
        perror("signal");
        return 1;
    }

    printf("Press Ctrl+C to test signal handler...\n");
    pause(); // Wait for a signal

    return 0;
}
```

### 2. kill() and raise() Functions

**kill()**: Send a signal to a process or group of processes
**raise()**: Send a signal to the current process

**Syntax:**

```c
#include <signal.h>

int kill(pid_t pid, int sig);
int raise(int sig);
```

**pid values for kill():**

- `pid > 0`: Send to specific process
- `pid == 0`: Send to all processes in sender's process group
- `pid == -1`: Send to all processes with permission
- `pid < -1`: Send to process group with ID = |pid|

**Example:**

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int main() {
    pid_t child_pid = fork();

    if (child_pid == 0) {
        // Child process
        printf("Child process running (PID: %d)\n", getpid());
        sleep(5);
        printf("Child process exiting\n");
    } else {
        // Parent process
        sleep(2);
        printf("Parent sending SIGTERM to child\n");
        kill(child_pid, SIGTERM);
        wait(NULL);
    }

    return 0;
}
```

### 3. alarm() and pause() Functions

**alarm()**: Schedule a SIGALRM signal after specified seconds
**pause()**: Suspend calling process until a signal is received

**Syntax:**

```c
#include <unistd.h>

unsigned int alarm(unsigned int seconds);
int pause(void);
```

**Example:**

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void alarm_handler(int sig) {
    printf("Alarm clock ring!\n");
}

int main() {
    signal(SIGALRM, alarm_handler);

    printf("Setting alarm for 3 seconds...\n");
    alarm(3);

    printf("Waiting for alarm...\n");
    pause();

    printf("Program continues after alarm\n");
    return 0;
}
```

### 4. Signal Sets and Related Functions

Signal sets (sigset_t) allow manipulation of multiple signals simultaneously.

**Key functions:**

- `sigemptyset()`: Initialize empty signal set
- `sigfillset()`: Initialize set with all signals
- `sigaddset()`: Add signal to set
- `sigdelset()`: Remove signal from set
- `sigismember()`: Test if signal is in set

**Example:**

```c
#include <stdio.h>
#include <signal.h>

int main() {
    sigset_t set;

    // Initialize empty set
    sigemptyset(&set);

    // Add some signals to set
    sigaddset(&set, SIGINT);
    sigaddset(&set, SIGTERM);

    // Check if SIGINT is in set
    if (sigismember(&set, SIGINT)) {
        printf("SIGINT is in the set\n");
    }

    return 0;
}
```

### 5. sigprocmask() Function

Controls the signal mask of the calling process, which defines which signals are currently blocked.

**Syntax:**

```c
#include <signal.h>

int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
```

**how values:**

- `SIG_BLOCK`: Add signals in set to current mask
- `SIG_UNBLOCK`: Remove signals in set from current mask
- `SIG_SETMASK`: Replace current mask with set

**Example:**

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int main() {
    sigset_t newset, oldset;

    // Initialize new set and add SIGINT
    sigemptyset(&newset);
    sigaddset(&newset, SIGINT);

    // Block SIGINT
    sigprocmask(SIG_BLOCK, &newset, &oldset);

    printf("SIGINT is now blocked. Try Ctrl+C...\n");
    sleep(5);

    // Restore original signal mask
    sigprocmask(SIG_SETMASK, &oldset, NULL);
    printf("SIGINT unblocked. Now try Ctrl+C...\n");
    sleep(5);

    return 0;
}
```

### 6. sigaction() Function

The preferred, more robust alternative to signal(), providing better control over signal handling.

**Syntax:**

```c
#include <signal.h>

int sigaction(int signum, const struct sigaction *act,
              struct sigaction *oldact);
```

**struct sigaction members:**

- `sa_handler`: Pointer to signal handler
- `sa_sigaction`: Alternative handler for SA_SIGINFO
- `sa_mask`: Additional signals to block during handler execution
- `sa_flags`: Special flags modifying signal behavior

**Example:**

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handler(int sig, siginfo_t *info, void *context) {
    printf("Received signal %d from process %d\n",
           sig, info->si_pid);
}

int main() {
    struct sigaction act;

    act.sa_sigaction = handler;
    sigemptyset(&act.sa_mask);
    act.sa_flags = SA_SIGINFO;

    if (sigaction(SIGINT, &act, NULL) < 0) {
        perror("sigaction");
        return 1;
    }

    printf("Process %d waiting for SIGINT...\n", getpid());
    pause();

    return 0;
}
```

## Comparison of Signal Handling Methods

| Feature       | signal()           | sigaction()            |
| ------------- | ------------------ | ---------------------- |
| Portability   | Less portable      | More portable          |
| Control       | Basic              | Advanced               |
| Information   | No additional info | Additional signal info |
| Flags support | No                 | Yes (SA_RESTART, etc.) |
| Reliability   | Less reliable      | More reliable          |

## Signal Handling Best Practices

1. **Keep handlers simple**: Signal handlers should be short and avoid complex operations
2. **Use async-signal-safe functions**: Only certain functions are safe to call from signal handlers
3. **Avoid non-reentrant functions**: printf(), malloc(), etc. are not safe in signal handlers
4. **Use volatile sig_atomic_t**: For global variables accessed in handlers
5. **Consider signal masking**: Block signals during critical sections

## Common Signal Handling Patterns

### Restarting System Calls

Some system calls can be automatically restarted after signal handling:

```c
struct sigaction act;
act.sa_handler = handler;
sigemptyset(&act.sa_mask);
act.sa_flags = SA_RESTART; // Enable restarting

sigaction(SIGINT, &act, NULL);
```

### Self-Piping Technique

A robust method for integrating signals with event loops:

```c
#include <signal.h>
#include <unistd.h>
#include <fcntl.h>

static int pipefds[2];

void handler(int sig) {
    write(pipefds[1], &sig, sizeof(sig));
}

int main() {
    // Create pipe
    pipe(pipefds);
    fcntl(pipefds[0], F_SETFL, O_NONBLOCK);

    // Set up signal handler
    signal(SIGINT, handler);

    // Event loop
    while (1) {
        fd_set readfds;
        FD_ZERO(&readfds);
        FD_SET(pipefds[0], &readfds);

        select(pipefds[0] + 1, &readfds, NULL, NULL, NULL);

        if (FD_ISSET(pipefds[0], &readfds)) {
            int sig;
            read(pipefds[0], &sig, sizeof(sig));
            printf("Received signal %d\n", sig);
        }
    }
}
```

## Exam Tips

1. **Remember key signal numbers**: SIGKILL (9), SIGTERM (15), SIGINT (2)
2. **Understand signal() vs sigaction()**: sigaction() is preferred for new code
3. **Know async-signal-safe functions**: write(), read(), \_exit(), etc.
4. **Understand signal masking**: How sigprocmask() affects signal delivery
5. **Practice common patterns**: Alarm timers, restarting system calls, self-piping
6. **Remember special signals**: SIGKILL and SIGSTOP cannot be caught or ignored
7. **Understand race conditions**: Signals can arrive at any time, causing potential races
