# Coding Rules for Signal Handling in Unix

## Introduction

When programming with signals in Unix systems, developers must follow specific coding rules and guidelines to ensure reliability, portability, and safety. Signal handling presents unique challenges because signal handlers can execute asynchronously, interrupting normal program flow at unpredictable times. Failure to follow proper coding practices can lead to race conditions, undefined behavior, corrupted data, and program crashes.

This topic covers the essential coding rules that every Unix programmer must understand when working with signals. These rules have evolved from decades of experience and are crucial for writing robust system programs, particularly daemons and server applications. The POSIX standard defines a set of async-signal-safe functions that can be safely called from within signal handlers, and understanding this distinction is fundamental to proper signal programming.

## Key Concepts

### 1. Async-Signal-Safe Functions

Only a limited set of functions can be safely called from within signal handlers. These are called async-signal-safe functions because they can be safely invoked from a signal handler while the same function is executing in the main program. The key async-signal-safe functions include:

- `_exit()`, `abort()`, `raise()`
- `signal()` (the POSIX version)
- `kill()`, `getpid()`, `getppid()`
- `getuid()`, `geteuid()`, `getgid()`, `getegid()`
- `alarm()`, `sleep()`
- `fsync()`, `fprintf()` with certain restrictions

Functions like `printf()`, `malloc()`, `free()`, `fprintf()` (for regular files), and most library functions are NOT async-signal-safe and should never be called from signal handlers.

### 2. Global Variables and volatile

When sharing variables between a signal handler and the main program, specific rules apply:

```c
volatile sig_atomic_t flag = 0; // Recommended for simple flags
```

- Use `volatile` to prevent compiler optimizations that might cache the variable value
- Use `sig_atomic_t` for atomic operations on simple types
- For complex data structures, use pipes or other IPC mechanisms instead of direct sharing

### 3. Signal Handler Characteristics

A signal handler must be a simple, re-entrant function:

- It should perform minimal operations
- It must not call non-async-signal-safe functions
- It should set a flag or write to a pipe/socket, not perform complex processing
- It must handle the possibility of being interrupted by another signal

### 4. sigaction vs signal

Always prefer `sigaction()` over `signal()`:

```c
struct sigaction sa;
sa.sa_handler = handler;
sigemptyset(&sa.sa_mask);
sa.sa_flags = SA_RESTART; // or SA_INTERRUPT
sigaction(SIGTERM, &sa, NULL);
```

The `signal()` function has implementation-dependent behavior across different Unix systems. The `sigaction()` function provides consistent, portable behavior and allows finer control over signal handling.

### 5. Proper Signal Mask Management

When establishing signal handlers, properly manage the signal mask:

```c
sigset_t newmask, oldmask, pendmask;
sigemptyset(&newmask);
sigaddset(&newmask, SIGTERM);
if (sigprocmask(SIG_BLOCK, &newmask, &oldmask) < 0)
 perror("sigprocmask");
```

Always save the old mask and restore it appropriately to avoid leaving signals blocked permanently.

## Examples

### Example 1: Correct Signal Handler Pattern

```c
#include <signal.h>
#include <stdio.h>
#include <unistd.h>

volatile sig_atomic_t got_signal = 0;

void handler(int sig) {
 got_signal = 1; // Safe: sig_atomic_t assignment
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

 while (!got_signal) {
 sleep(1); // Wait for signal
 }

 printf("Signal received, exiting gracefully\n");
 return 0;
}
```

This example demonstrates proper use of `volatile sig_atomic_t`, `sigaction()`, and a minimal signal handler.

### Example 2: Inter-Process Communication via Pipe

```c
#include <signal.h>
#include <unistd.h>
#include <fcntl.h>

void alarm_handler(int sig) {
 char msg = 'A';
 write(pipe_fd[1], &msg, 1); // write() is async-signal-safe
}

int main() {
 int pipe_fd[2];
 pipe(pipe_fd);

 struct sigaction sa;
 sa.sa_handler = alarm_handler;
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = 0;
 sigaction(SIGALRM, &sa, NULL);

 alarm(5); // Set alarm

 char buf;
 read(pipe_fd[0], &buf, 1); // Read from pipe in main program
 // Process the alarm event
}
```

This demonstrates using a pipe for communication from signal handler to main program, which is the recommended approach for complex data.

### Example 3: Atomic Flag with sigsuspend

```c
#include <signal.h>
#include <unistd.h>
#include <stdio.h>

volatile sig_atomic_t quit = 0;

void int_handler(int sig) {
 quit = 1;
}

int main() {
 sigset_t newmask, oldmask, waitmask;

 sigemptyset(&newmask);
 sigaddset(&newmask, SIGINT);

 sigemptyset(&waitmask);
 sigaddset(&waitmask, SIGUSR1);

 sigprocmask(SIG_BLOCK, &newmask, &oldmask);

 struct sigaction sa;
 sa.sa_handler = int_handler;
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = 0;
 sigaction(SIGINT, &sa, NULL);

 while (!quit) {
 sigsuspend(&waitmask); // Atomically unblocks and waits
 }

 sigprocmask(SIG_SETMASK, &oldmask, NULL);
 printf("Exiting\n");
 return 0;
}
```

This demonstrates atomic signal blocking with `sigsuspend()`, preventing race conditions between checking the flag and waiting for signals.

## Exam Tips

1. **Memorize the async-signal-safe functions list** - This is frequently tested in exams. Remember that `printf()` is NOT safe.

2. **Use sigaction instead of signal** - Always prefer `sigaction()` for portable, reliable signal handling.

3. **volatile sig_atomic_t for shared variables** - This is the standard pattern for communication between handlers and main program.

4. **Never call printf() in signal handlers** - This is a common mistake that leads to undefined behavior.

5. **Understand sigsuspend()** - It atomically replaces the signal mask and waits, preventing race conditions.

6. **SA_RESTART flag** - Use this to automatically restart interrupted system calls, but be aware it doesn't work for all system calls.

7. **Check return values** - Always check return values from sigaction(), sigprocmask(), and other signal-related functions.

8. **Signal handler should be minimal** - The handler should only set flags or write to pipes, not perform complex processing.

9. **Block signals during critical sections** - Use sigprocmask() to prevent signals from interrupting critical operations.

10. **Avoid race conditions** - Use sigprocmask() and sigsuspend() together to prevent races between signal checking and handling.
