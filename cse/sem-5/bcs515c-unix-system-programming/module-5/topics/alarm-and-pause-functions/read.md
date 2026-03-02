# Alarm and Pause Functions in Unix/Linux

## Introduction

In Unix/Linux system programming, alarm and pause functions are fundamental mechanisms provided by the operating system for managing time-based operations and process synchronization. These functions enable processes to suspend their execution for a specified duration or to schedule future notifications, which are essential capabilities for implementing timeouts, polling mechanisms, and periodic task execution in various applications.

The alarm function, specifically the `alarm()` system call, allows a process to schedule a SIGALRM signal to be delivered after a specified number of seconds. This mechanism is crucial for implementing timeouts in network operations, implementing watchdogs, and performing periodic background tasks. The pause function, on the other hand, suspends a process until a signal is received, making it essential for implementing wait mechanisms and signal-driven programming patterns.

Understanding these functions is critical for CSE students as they form the backbone of many concurrent and real-time programming concepts. These primitives are extensively used in device drivers, network servers, and embedded systems programming. The combination of alarm and pause functions, along with other signal handling mechanisms, provides powerful tools for creating responsive and efficient system programs.

## Key Concepts

### The alarm() Function

The `alarm()` function is declared in `<unistd.h>` and has the following prototype:

```c
unsigned int alarm(unsigned int seconds);
```

When a process calls `alarm(seconds)`, the kernel schedules a SIGALRM signal to be delivered to the calling process after the specified number of seconds have elapsed. If `seconds` is zero, any previously scheduled alarm is cancelled. The function returns the number of seconds remaining until any previously scheduled alarm was due to fire, or zero if there was no previously scheduled alarm.

The alarm mechanism operates at the process level, meaning that the alarm is associated with the calling process and persists across exec() calls but not across fork() calls. After a fork(), the child process starts with no alarm scheduled, regardless of the parent's alarm state.

**Example of basic alarm usage:**

```c
#include <stdio.h>
#include <unistd.h>
#include <signal.h>

void alarm_handler(int signum) {
 printf("Alarm triggered after 3 seconds!\n");
}

int main() {
 signal(SIGALRM, alarm_handler);
 alarm(3); // Schedule SIGALRM after 3 seconds
 pause(); // Wait for signal
 return 0;
}
```

### The pause() Function

The `pause()` function suspends the calling process until a signal is delivered that either terminates the process or invokes a signal handler. Its prototype is:

```c
int pause(void);
```

The pause function returns only when a signal handler is invoked (returning -1 with errno set to EINTR) or when the process is terminated. This function is particularly useful when combined with alarm for implementing sleep-like functionality or waiting for specific conditions signaled by other processes.

**Important consideration:** The pause function has a race condition issue. If the signal could be delivered before the process calls pause(), the process may sleep indefinitely. This is why alarm is typically set before pause to ensure a signal will arrive.

### Signal Handling Fundamentals

Signals are software interrupts delivered to processes to notify them of asynchronous events. The SIGALRM signal (signal number 14) is the signal raised by the alarm() function. Each signal has a default action, which for SIGALRM is to terminate the process. Therefore, programs using alarm must establish a signal handler for SIGALRM to prevent process termination.

Signal handlers must be carefully written because they can be invoked at any point during program execution. The signal handler function should only use async-signal-safe functions (like write(), but not printf()). Modern systems provide the sigaction() function for more robust signal handling compared to the older signal() function.

### Race Conditions and Best Practices

When combining alarm() and pause(), developers must be aware of potential race conditions. The sequence of operations matters significantly:

1. **Setting alarm before pause:** This is the recommended approach. By setting the alarm before calling pause(), you ensure that even if the signal arrives just before pause() is called, the kernel will still deliver it, causing pause() to return.

2. **Setting alarm after pause (unsafe):** If pause() is called before alarm(), and the alarm fires between these two calls, the process will sleep indefinitely because pause() was already waiting.

3. **Using setjmp/longjmp with signals:** For more complex scenarios involving signals and longjmp, processes must save and restore signal masks using sigsetjmp and siglongjmp to avoid race conditions.

### The sleep() Function Implementation

The standard library sleep() function is often implemented using alarm() and pause(). A simple implementation demonstrates this:

```c
unsigned int my_sleep(unsigned int seconds) {
 struct sigaction new_action, old_action;
 sigset_t new_mask, old_mask, sus_mask;
 unsigned int remaining, prev_alarm;

 // Save current SIGALRM handler
 new_action.sa_handler = SIG_DFL;
 sigemptyset(&new_action.sa_mask);
 new_action.sa_flags = 0;
 sigaction(SIGALRM, &new_action, &old_action);

 // Block SIGALRM and save current mask
 sigemptyset(&new_mask);
 sigaddset(&new_mask, SIGALRM);
 sigprocmask(SIG_BLOCK, &new_mask, &old_mask);

 // Schedule alarm
 prev_alarm = alarm(seconds);

 // Suspend process
 sus_mask = old_mask;
 sigdelset(&sus_mask, SIGALRM);
 sigsuspend(&sus_mask);

 // Get remaining time if alarm didn't fire
 remaining = alarm(0);

 // Restore previous state
 sigprocmask(SIG_SETMASK, &old_mask, NULL);
 sigaction(SIGALRM, &old_action, NULL);

 // Set alarm for remaining time
 if (remaining != 0) {
 remaining = alarm(remaining);
 }

 return remaining;
}
```

This implementation handles the interaction between alarm and other signals correctly, demonstrating the complexity of proper signal programming.

### Interval Timers (Advanced)

Unix systems provide interval timers through the setitimer() system call, which offers more flexibility than the basic alarm() function. The setitimer() allows setting timers that repeat at regular intervals (ITIMER_REAL, ITIMER_VIRTUAL, ITIMER_PROF) and is particularly useful for implementing profiling and real-time monitoring.

## Examples

### Example 1: Simple Timeout Implementation

**Problem:** Implement a function that attempts to read from standard input with a 5-second timeout.

**Solution:**

```c
#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

volatile sig_atomic_t timeout_occurred = 0;

void timeout_handler(int signum) {
 timeout_occurred = 1;
}

int read_with_timeout(char *buffer, size_t size, unsigned int timeout) {
 int bytes_read;

 // Set up signal handler
 struct sigaction sa;
 sa.sa_handler = timeout_handler;
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = 0;
 sigaction(SIGALRM, &sa, NULL);

 // Set alarm BEFORE reading (critical order)
 alarm(timeout);

 // Attempt read
 bytes_read = read(STDIN_FILENO, buffer, size);

 // Cancel alarm if read succeeded
 if (bytes_read > 0) {
 alarm(0);
 }

 if (timeout_occurred) {
 printf("Read timed out after %u seconds\n", timeout);
 return -1;
 }

 return bytes_read;
}

int main() {
 char buffer[100];
 int result = read_with_timeout(buffer, sizeof(buffer), 5);

 if (result > 0) {
 buffer[result] = '\0';
 printf("Read %d bytes: %s\n", result, buffer);
 }

 return 0;
}
```

**Step-by-step explanation:**

1. First, we establish a signal handler for SIGALRM that sets a flag
2. We set the alarm for 5 seconds before attempting the read
3. We attempt to read from stdin (this may complete before timeout)
4. If read succeeds, we cancel the pending alarm using alarm(0)
5. If timeout occurs, the signal handler sets the flag and interrupts read

### Example 2: Periodic Task Execution

**Problem:** Implement a program that performs a task every 2 seconds.

**Solution:**

```c
#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <time.h>

volatile sig_atomic_t alarm_count = 0;

void alarm_handler(int signum) {
 alarm_count++;
}

void do_periodic_task(void) {
 time_t now = time(NULL);
 printf("Task executed at: %s", ctime(&now));
}

int main() {
 struct sigaction sa;

 // Set up alarm handler
 sa.sa_handler = alarm_handler;
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = 0;

 if (sigaction(SIGALRM, &sa, NULL) == -1) {
 perror("sigaction");
 return 1;
 }

 // Schedule first alarm
 alarm(2);

 while (alarm_count < 5) {
 pause(); // Wait for signal

 if (alarm_count < 5) {
 do_periodic_task();
 alarm(2); // Schedule next alarm
 }
 }

 printf("Completed 5 iterations\n");
 return 0;
}
```

**Step-by-step explanation:**

1. We use sigaction for robust signal handling
2. The alarm_count variable acts as our timing mechanism
3. We schedule the first alarm for 2 seconds
4. The pause() suspends execution until SIGALRM arrives
5. After handling each alarm, we schedule the next one
6. The loop terminates after 5 iterations

### Example 3: Combining Multiple Timeouts

**Problem:** Implement a function that tries multiple operations with different timeouts, returning which operation succeeded.

**Solution:**

```c
#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

typedef struct {
 const char *name;
 unsigned int timeout;
 int completed;
} Operation;

volatile sig_atomic_t current_operation = -1;

void alarm_handler(int signum) {
 if (current_operation >= 0) {
 printf("Operation '%s' timed out\n",
 current_operation >= 0 ? "unknown" : "N/A");
 }
}

int try_operations(Operation *ops, int count) {
 struct sigaction sa;
 int i;

 // Set up signal handler
 sa.sa_handler = alarm_handler;
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = 0;
 sigaction(SIGALRM, &sa, NULL);

 for (i = 0; i < count; i++) {
 current_operation = i;
 ops[i].completed = 0;

 // Set timeout for this operation
 alarm(ops[i].timeout);

 // Simulate operation (replace with actual work)
 printf("Starting operation '%s' with timeout %us\n",
 ops[i].name, ops[i].timeout);
 sleep(1); // Simulated work

 // Check if alarm fired
 if (!ops[i].completed) {
 // If we reach here, alarm didn't fire means success
 // (in real code, you'd check operation result)
 ops[i].completed = 1;
 alarm(0); // Cancel any pending alarm
 printf("Operation '%s' completed successfully\n", ops[i].name);
 return i; // Return index of successful operation
 }
 }

 return -1; // All operations failed
}

int main() {
 Operation ops[] = {
 {"Network Request", 3},
 {"File Processing", 2},
 {"Database Query", 4}
 };

 int result = try_operations(ops, 3);

 if (result >= 0) {
 printf("First successful operation: %s\n", ops[result].name);
 } else {
 printf("All operations failed\n");
 }

 return 0;
}
```

## Exam Tips

1. **alarm() function returns:** Remember that alarm() returns the number of seconds remaining from the previously scheduled alarm, or 0 if there was no previous alarm. This is a common exam question.

2. **Order of operations:** Always set alarm() before pause() to avoid race conditions. This is critical for correct implementation.

3. **alarm(0) cancels alarm:** Setting alarm(0) cancels any previously scheduled alarm without scheduling a new one.

4. **Default SIGALRM action:** The default action for SIGALRM is process termination. Always establish a signal handler to prevent this.

5. **pause() return value:** pause() only returns when a signal is caught, returning -1 with errno set to EINTR.

6. **alarm vs setitimer:** Understand that setitimer() provides more features including repeated timers (interval timers), while alarm() is simpler for one-time delays.

7. **Async-signal-safe functions:** In signal handlers, only use functions like write(), \_exit(), or set variables. Avoid printf() in production code.

8. **Process inheritance:** Alarms are not inherited across fork() but persist across exec() calls.

9. **sigaction preferred:** Use sigaction() instead of signal() for more predictable and portable signal handling behavior.

10. **Real-world applications:** Be prepared to explain applications like implementing timeouts, watchdogs, and periodic task execution in exam scenarios.
