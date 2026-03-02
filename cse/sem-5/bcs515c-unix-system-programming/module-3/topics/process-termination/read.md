# Process Termination in Operating Systems

## Introduction

Process termination is a fundamental concept in operating system design that deals with the orderly completion and cleanup of processes. When a process finishes its execution or is forced to terminate, the operating system must perform several critical operations to ensure system stability and resource management. Understanding process termination is essential for CSE students as it forms the backbone of process management in modern operating systems.

In this topic, we will explore the various mechanisms through which processes terminate, the different exit statuses, the role of parent and child processes in termination, and the critical concept of orphan and zombie processes. These concepts are crucial for writing robust concurrent programs and understanding how operating systems manage system resources efficiently.

## Key Concepts

### 1. Process Termination Basics

A process in an operating system goes through several states during its lifecycle: new, ready, running, waiting, and terminated. The terminated state is the final state where the process completes execution. When a process terminates, the operating system performs the following actions:

- **Resource Deallocation**: All resources allocated to the process (memory, file descriptors, I/O buffers) are released back to the system
- **Exit Status Communication**: The process can communicate its exit status to its parent process
- **Process Table Entry Removal**: The process control block (PCB) remains in the system until the parent reads the exit status
- **Parent Notification**: The parent process is informed about the child's termination through signals or wait system calls

### 2. Ways a Process Can Terminate

**Normal Termination (Voluntary):**

- **Exit System Call**: The process calls `exit()` (in C) or equivalent in other languages
- **Return from Main**: In C/C++ programs, returning from `main()` function implicitly calls `exit()`
- **Calling `_exit()` or `_Exit()`**: These terminate the process without calling cleanup handlers or flushing standard I/O

**Abnormal Termination (Involuntary):**

- **Signal Reception**: Process receives signals like SIGKILL (cannot be caught), SIGSEGV (segmentation fault), SIGINT (Ctrl+C), etc.
- **Assertion Failures**: In debug builds, failed assertions can terminate the process
- **Division by Zero**: Hardware exception that typically sends SIGFPE signal

### 3. Exit Status and Return Codes

When a process terminates normally, it can return an exit status to its parent. This status is typically:

- An integer value (0-255 in Unix/Linux systems)
- Convention: 0 indicates success, non-zero indicates failure
- The exit status is stored in the process control block
- Parent retrieves this status using `wait()` or `waitpid()` system calls

In Unix/Linux:

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

int main() {
 pid_t pid = fork();

 if (pid == 0) {
 // Child process
 printf("Child process executing...\n");
 exit(42); // Exit with status 42
 } else if (pid > 0) {
 // Parent process
 int status;
 wait(&status); // Wait for child to terminate

 if (WIFEXITED(status)) {
 printf("Child exited with status: %d\n", WEXITSTATUS(status));
 }
 }
 return 0;
}
```

### 4. The wait() and waitpid() System Calls

These are crucial system calls that allow a parent process to synchronize with child termination and obtain the exit status:

- **wait()**: Blocks until any child terminates; returns child PID
- **waitpid()**: Allows waiting for specific child or non-blocking wait
- **Macros for status decoding**:
- `WIFEXITED(status)`: Returns true if child terminated normally
- `WEXITSTATUS(status)`: Returns the exit status of terminated child
- `WIFSIGNALED(status)`: Returns true if child was killed by signal
- `WTERMSIG(status)`: Returns the signal number that killed the child
- `WIFSTOPPED(status)`: Returns true if child is stopped
- `WIFCONTINUED(status)`: Returns true if child continued after stop

### 5. Zombie Processes

A **zombie process** (also called a defunct process) occurs when a child process has terminated, but its entry remains in the process table because the parent has not yet read its exit status.

**Characteristics of Zombie Processes:**

- They are dead processes (no longer executing)
- They retain their process ID (PID) and exit status in the process table
- They consume minimal system resources (just the process table entry)
- They do not consume CPU time or memory

**Creating a Zombie Process:**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
 pid_t pid = fork();

 if (pid > 0) {
 // Parent process - does NOT call wait()
 // This creates a zombie process
 printf("Parent PID: %d, Child PID: %d\n", getpid(), pid);
 sleep(30); // Sleep while child becomes zombie
 wait(NULL); // Now read the exit status
 } else {
 // Child process - exits immediately
 printf("Child exiting...\n");
 exit(0);
 }
 return 0;
}
```

**Why Zombies are Problematic:**

- If too many zombies accumulate, the system can run out of available PIDs
- They occupy process table entries
- Indicate programming errors (parent not calling wait())

### 6. Orphan Processes

An **orphan process** is a running process whose parent has terminated or crashed before the child completes execution.

**How Orphans are Handled:**

- In Unix/Linux, orphaned processes are adopted by the `init` process (PID 1)
- `init` process periodically calls `wait()` to collect exit statuses of adopted orphans
- This prevents orphan processes from becoming zombies

**Creating an Orphan Process:**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
 pid_t pid = fork();

 if (pid > 0) {
 // Parent exits immediately
 printf("Parent exiting, PID: %d\n", getpid());
 exit(0);
 } else {
 // Child becomes orphan
 sleep(5); // Parent exits before this
 printf("Orphan child, PID: %d, Parent PID: %d\n",
 getpid(), getppid()); // Will show init as parent
 }
 return 0;
}
```

### 7. Process Groups and Session Termination

- **Process Group**: Each process belongs to a process group (identified by PGID)
- **Session**: Processes can be part of a session (identified by SID)
- **Session Leader**: Process that creates a session becomes the session leader
- When session leader terminates, SIGHUP is sent to all processes in the session

### 8. Termination in Different Operating Systems

**Unix/Linux:**

- Uses `exit()` system call
- Exit status stored in PCB
- Parent must call `wait()` to retrieve status

**Windows:**

- Uses `ExitProcess()` or `TerminateProcess()`
- Exit code can be retrieved via `GetExitCodeProcess()`
- Handles are closed automatically

## Examples

### Example 1: Understanding Exit Status with wait()

**Problem**: Write a C program where parent creates two child processes. Both children perform different tasks and return different exit codes. Parent should print which child succeeded or failed.

**Solution:**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
 pid_t pid1, pid2;

 pid1 = fork();

 if (pid1 == 0) {
 // First child - performs addition
 printf("Child 1 (PID %d): Performing addition 10 + 20 = %d\n",
 getpid(), 10 + 20);
 exit(0); // Success
 }

 pid2 = fork();

 if (pid2 == 0) {
 // Second child - tries division by zero (simulated error)
 printf("Child 2 (PID %d): Operation failed!\n", getpid());
 exit(1); // Failure
 }

 // Parent waits for both children
 int status1, status2;
 waitpid(pid1, &status1, 0);
 waitpid(pid2, &status2, 0);

 printf("\nParent: Child 1 exit status: %d\n", WEXITSTATUS(status1));
 printf("Parent: Child 2 exit status: %d\n", WEXITSTATUS(status2));

 if (WEXITSTATUS(status1) == 0)
 printf("Child 1: SUCCESS\n");
 else
 printf("Child 1: FAILED\n");

 if (WEXITSTATUS(status2) == 0)
 printf("Child 2: SUCCESS\n");
 else
 printf("Child 2: FAILED (expected)\n");

 return 0;
}
```

### Example 2: Preventing Zombie Processes

**Problem**: Demonstrate how to prevent zombie processes using waitpid() in a loop.

**Solution:**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
 int num_children = 5;

 for (int i = 0; i < num_children; i++) {
 pid_t pid = fork();

 if (pid == 0) {
 // Child process does some work
 printf("Child %d (PID %d) working...\n", i, getpid());
 sleep(1);
 exit(i); // Exit with index as status
 }

 // Parent continues creating more children
 }

 // Parent waits for all children to prevent zombies
 printf("Parent waiting for all children...\n");

 int status;
 int terminated_pid;

 while ((terminated_pid = waitpid(-1, &status, 0)) > 0) {
 // -1 means wait for any child
 // WNOHANG could be used for non-blocking
 if (WIFEXITED(status)) {
 printf("Child with PID %d exited with status: %d\n",
 terminated_pid, WEXITSTATUS(status));
 }
 }

 printf("All children reaped. No zombie processes.\n");
 return 0;
}
```

### Example 3: Handling Signals and Abnormal Termination

**Problem**: Write a program that handles SIGINT (Ctrl+C) gracefully and performs cleanup before termination.

**Solution:**

```c
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void cleanup_handler(int signum) {
 printf("\n[Cleanup] Caught signal %d, performing cleanup...\n", signum);
 printf("[Cleanup] Closing files, releasing resources...\n");
 printf("[Cleanup] Exiting gracefully.\n");
 exit(0);
}

int main() {
 // Register signal handler for SIGINT
 struct sigaction sa;
 sa.sa_handler = cleanup_handler;
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = 0;

 sigaction(SIGINT, &sa, NULL);

 printf("Process PID: %d\n", getpid());
 printf("Press Ctrl+C to test graceful termination\n");

 // Simulate long-running process
 while (1) {
 printf("Working...\n");
 sleep(2);
 }

 return 0;
}
```

## Exam Tips

1. **Remember the difference between exit() and \_exit()**: exit() performs cleanup (calls atexit handlers, flushes I/O buffers) before termination, while \_exit() terminates immediately without cleanup.

2. **Zombie vs Orphan**: In exams, remember zombies are "dead but not buried" (parent hasn't read exit status), while orphans are "alive but parentless" (adopted by init).

3. **init process role**: The init process (PID 1) adopts orphans and calls wait() to prevent zombie accumulation.

4. **wait() blocks, waitpid() doesn't**: wait() blocks until a child terminates, while waitpid() can be made non-blocking with WNOHANG flag.

5. **Exit status conventions**: Remember 0 typically means success, non-zero means failure in Unix systems.

6. **WIFEXITED vs WIFSIGNALED**: Use WIFEXITED for normal exit, WIFSIGNALED for abnormal termination by signal.

7. **Process table entry**: A process entry remains in the process table until the parent reads the exit status via wait() system call.

8. **Signals that cannot be caught**: SIGKILL and SIGSTOP cannot be caught, blocked, or ignored - they always terminate the process.

9. **fork() returns twice**: Once in parent (returns child PID) and once in child (returns 0). This is a common exam question.

10. **Orphan process identification**: If you check getppid() in a child and it returns 1, the process is an orphan adopted by init.
