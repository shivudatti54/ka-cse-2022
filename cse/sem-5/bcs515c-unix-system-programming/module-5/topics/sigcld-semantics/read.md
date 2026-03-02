# SIGCLD Semantics in Unix/Linux

## Introduction

The SIGCLD signal (Signal Child) is one of the most important signals in Unix/Linux systems, specifically related to process management and child process termination. Understanding SIGCLD semantics is crucial for developing robust Unix applications that properly handle child processes and prevent resource leaks. In modern Linux systems, SIGCLD is essentially equivalent to SIGCHLD, though there are subtle historical differences that matter in certain programming contexts.

When a child process terminates, it does not immediately disappear from the system. Instead, it enters a "zombie" state (also called "defunct" state) where it remains in the process table until its parent reads its exit status using the wait() system call. The SIGCLD signal is sent to the parent process when a child terminates, allowing the parent to be notified and take appropriate action. Without proper handling, zombie processes can accumulate and exhaust the process table, leading to system instability.

This topic is particularly important for CSE students because process management is a fundamental concept in operating systems, and signal handling is essential for writing correct concurrent programs. Interview questions and practical programming assignments frequently test understanding of these concepts.

## Key Concepts

### The SIGCLD Signal

SIGCLD (signal child) is sent to a process when one of its child processes terminates. The signal is also sent when a process calls one of the wait() family functions. Historically, SIGCLD was defined in older Unix systems, while POSIX standardized on SIGCHLD. In Linux, SIGCLD is defined as an alias for SIGCHLD, but the underlying semantics can differ slightly in behavior.

The default action for SIGCLD is to ignore the signal. This default behavior is significant because if a parent process does not install a signal handler for SIGCLD and does not call wait(), terminated child processes become zombies that remain in the system until the parent terminates. This is a common source of resource leaks in Unix programs.

### Process States and Zombie Processes

Understanding process states is essential for grasping SIGCLD semantics. A Unix process can be in several states:

1. **Running**: The process is currently executing or ready to execute
2. **Sleeping**: The process is waiting for some event or resource
3. **Stopped**: The process is suspended (typically by a job control signal)
4. **Zombie**: The process has terminated but its entry remains in the process table

When a child process terminates, it enters the zombie state. In this state, the process has finished execution but retains its process table entry, containing information such as exit status, resource usage statistics, and process ID. The kernel retains this information so the parent can retrieve it later through the wait() system call.

If the parent never calls wait() for a terminated child, the zombie process remains in the system indefinitely (or until the parent terminates). This is called "orphaning" the zombie. When the parent eventually terminates, the orphaned zombie is adopted by the init process (PID 1), which periodically calls wait() to reap such processes.

### The wait() System Call

The wait() system call is the primary mechanism for a parent process to retrieve information about terminated children and prevent zombie creation. When a parent calls wait(), it blocks until one of its children terminates. Upon return, wait() provides:

- The process ID of the terminated child
- The exit status of the child (stored in an integer pointer argument)
- Information about whether the child terminated normally or was killed by a signal

The function prototype is:

```c
pid_t wait(int *status);
```

If multiple children have terminated, each call to wait() reaps one child. When all children have been reaped, subsequent calls to wait() block indefinitely (or return -1 if using waitpid() with WNOHANG).

### The waitpid() System Call

waitpid() provides more flexible control over child process reaping:

```c
pid_t waitpid(pid_t pid, int *status, int options);
```

Key features of waitpid():

- **pid**: Can specify a specific child PID, -1 to wait for any child, or 0 to wait for any child in the same process group
- **options**: Bitwise OR of flags like WNOHANG (don't block if no child has terminated) and WUNTRACED (report stopped children)

WNOHANG is particularly useful for implementing non-blocking wait in event-driven programs.

### Signal Handling for SIGCLD

To handle SIGCLD asynchronously, a parent process can install a signal handler using the signal() or sigaction() system calls:

```c
void sigchld_handler(int sig) {
 int status;
 pid_t pid;

 // Reap all available zombie children
 while ((pid = waitpid(-1, &status, WNOHANG)) > 0) {
 // Process terminated child information
 }
}
```

This handler uses waitpid() with WNOHANG in a loop because multiple children may have terminated before the handler executes. Using wait() inside a signal handler is problematic because wait() can block, and during signal handling, signals are typically blocked.

### The sigaction() Function

The POSIX-recommended way to install signal handlers is using sigaction():

```c
struct sigaction sa;
sa.sa_handler = sigchld_handler;
sigemptyset(&sa.sa_mask);
sa.sa_flags = SA_RESTART; // Restart interrupted system calls

if (sigaction(SIGCLD, &sa, NULL) == -1) {
 perror("sigaction");
 exit(1);
}
```

The SA_RESTART flag causes certain system calls to be automatically restarted if interrupted by the signal handler, which is useful for programs using blocking I/O.

## Examples

### Example 1: Basic wait() Usage

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
 pid_t pid = fork();

 if (pid < 0) {
 perror("fork failed");
 exit(1);
 }

 if (pid == 0) {
 // Child process
 printf("Child PID %d: Starting work...\n", getpid());
 sleep(2);
 printf("Child PID %d: Work complete, exiting with status 42\n", getpid());
 exit(42);
 } else {
 // Parent process
 int status;
 printf("Parent PID %d: Created child %d\n", getpid(), pid);
 printf("Parent: Waiting for child to terminate...\n");

 pid_t terminated_pid = wait(&status);

 if (terminated_pid > 0) {
 printf("Parent: Child %d terminated\n", terminated_pid);
 if (WIFEXITED(status)) {
 printf("Parent: Exit status = %d\n", WEXITSTATUS(status));
 }
 }
 }

 return 0;
}
```

**Step-by-step execution:**

1. Parent process calls fork(), creating a child process
2. Child prints message, sleeps for 2 seconds, then exits with status 42
3. Parent blocks at wait() until child terminates
4. When child exits, parent wakes up and retrieves exit status using WIFEXITED() and WEXITSTATUS()
5. No zombie process remains because parent called wait()

### Example 2: Non-blocking wait with SIGCHLD Handler

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

void sigchld_handler(int sig) {
 int status;
 pid_t pid;

 // Reap all terminated children (non-blocking)
 while ((pid = waitpid(-1, &status, WNOHANG)) > 0) {
 if (WIFEXITED(status)) {
 printf("Handler: Child %d exited with status %d\n",
 pid, WEXITSTATUS(status));
 }
 }
}

int main() {
 struct sigaction sa;
 sa.sa_handler = sigchld_handler;
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = SA_RESTART;

 if (sigaction(SIGCLD, &sa, NULL) == -1) {
 perror("sigaction");
 exit(1);
 }

 // Create multiple child processes
 for (int i = 0; i < 3; i++) {
 if (fork() == 0) {
 // Child
 printf("Child %d working...\n", getpid());
 sleep(1);
 printf("Child %d done\n", getpid());
 exit(i);
 }
 }

 // Parent continues immediately without blocking
 printf("Parent: Created children, doing other work...\n");
 sleep(3); // Simulate other work
 printf("Parent: All work complete\n");

 return 0;
}
```

**Key points:**

- Parent installs SIGCLD handler before creating children
- Each child terminates at different times
- Signal handler executes when children terminate, reaping them automatically
- Parent does not need to call wait() - zombies are reaped in the handler
- Using WNOHANG prevents blocking in the signal handler
- SA_RESTART ensures blocked system calls resume after signal handling

### Example 3: Handling Stopped Children with waitpid()

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

int main() {
 pid_t pid = fork();

 if (pid == 0) {
 // Child: run for a while
 printf("Child: Running, will stop myself with SIGSTOP\n");
 raise(SIGSTOP); // Stop myself
 printf("Child: Resumed, exiting\n");
 exit(0);
 } else {
 // Parent
 sleep(1); // Let child stop itself

 int status;
 printf("Parent: Checking child status with WUNTRACED\n");

 pid_t result = waitpid(pid, &status, WUNTRACED);

 if (result > 0 && WIFSTOPPED(status)) {
 printf("Parent: Child was stopped by signal %d\n",
 WSTOPSIG(status));

 // Send SIGCONT to resume child
 kill(pid, SIGCONT);
 printf("Parent: Sent SIGCONT to resume child\n");

 // Now wait for final termination
 waitpid(pid, &status, 0);
 printf("Parent: Child finally terminated\n");
 }
 }

 return 0;
}
```

This example demonstrates handling not just termination but also stopped processes using WUNTRACED option.

## Exam Tips

1. **Remember the default action**: The default action for SIGCLD is to ignore the signal, which leads to zombie processes if wait() is not called.

2. **Difference between wait() and waitpid()**: wait() blocks until any child terminates; waitpid() can wait for a specific child or return immediately with WNOHANG.

3. **WIFEXITED and WEXITSTATUS**: These macros check if a child terminated normally (via exit()) and extract the exit status. Always check WIFEXITED before using WEXITSTATUS.

4. **Zombie prevention**: Always call wait()/waitpid() in the parent to prevent zombie accumulation. Either block on wait(), use waitpid() with WNOHANG in a loop, or install a SIGCLD handler.

5. **Signal handler best practice**: When writing signal handlers for SIGCLD, use waitpid(-1, &status, WNOHANG) in a loop rather than wait() to handle multiple terminated children.

6. **SA_RESTART flag**: Use this flag in sigaction() to automatically restart system calls interrupted by the signal, preventing EINTR errors in your main code.

7. **Historical note**: In older Unix systems, SIGCLD behaved differently - it was automatically reset when caught. POSIX standardized on SIGCHLD, which Linux uses as an alias.

8. **Orphaned zombies**: When a parent terminates before calling wait(), its zombie children are adopted by init (PID 1), which reaps them.

9. **Two fork() pattern**: In server programs, the common pattern is fork() twice to prevent zombie accumulation - the intermediate child terminates immediately, and init reaps it.

10. **System limits**: Most systems have a limit on maximum zombie processes (usually thousands). Exceeding this can prevent forking new processes.
