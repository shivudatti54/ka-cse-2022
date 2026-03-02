# Process Synchronization: The wait() and waitpid() System Calls

## Introduction

In Unix/Linux operating systems, process management is a fundamental concept that every computer science engineer must master. When a parent process creates a child process using the fork() system call, proper synchronization between them becomes essential. The wait() system call (including its variant wait3()) serves as a critical mechanism for this synchronization. The wait3() function specifically allows the parent process to suspend its execution until the child process terminates, while also providing information about the child's resource usage.

Understanding wait(), waitpid(), and wait3() is crucial for CSE students because these system calls form the backbone of process coordination in real-world applications. Whether you're building server processes, daemon applications, or concurrent systems, proper handling of child processes prevents common issues like zombie processes and resource leaks. This topic is particularly important from an exam perspective, as frequently tests concepts related to process creation, termination, and synchronization in operating system examinations.

## Key Concepts

### The wait() System Call

The basic wait() system call is defined as:

```c
#include <sys/wait.h>
pid_t wait(int *status);
```

When a parent process calls wait(), it blocks until one of its child processes terminates. The function returns the process ID (PID) of the terminated child and stores the exit status in the memory location pointed to by the status parameter. If the parent has multiple children, wait() returns when any child terminates, and the order is not guaranteed.

The status parameter encodes information about how the child process terminated. Macros like WIFEXITED(), WEXITSTATUS(), WIFSIGNALED(), and WTERMSIG() are used to extract this information. If the status parameter is NULL, no status information is returned.

### The waitpid() System Call

The waitpid() function provides more control over which child to wait for:

```c
pid_t waitpid(pid_t pid, int *status, int options);
```

The pid argument specifies which child to wait for:

- pid > 0: Wait for the child with specific PID
- pid = 0: Wait for any child in the same process group
- pid = -1: Wait for any child (similar to wait())
- pid < -1: Wait for any child whose process group ID equals |pid|

The options parameter can include WNOHANG (return immediately if no child has exited), WUNTRACED (report stopped children), and WCONTINUE (report continued children).

### The wait3() System Call

The wait3() function is similar to wait() but provides additional resource usage information:

```c
#include <sys/types.h>
#include <sys/resource.h>
pid_t wait3(int *status, int options, struct rusage *rusage);
```

The key difference is the rusage parameter, which when not NULL, receives information about the child process's resource usage including user CPU time, system CPU time, page faults, and other statistics. This makes wait3() particularly useful for performance monitoring and accounting purposes.

### Zombie and Orphan Processes

When a child process terminates but its parent has not yet called wait(), the child becomes a zombie process (defunct process). The process entry remains in the process table until the parent collects its status using wait(). If the parent terminates before the child, the child is adopted by the init process (PID 1), which periodically calls wait() to reap zombie processes.

Orphan processes are running child processes whose parent has terminated. These are adopted by init and continue running normally.

### Process Termination Status

The status integer encodes termination information:

- If the child terminated normally (called exit() or returned from main()), the status contains the exit code in bits 8-15
- If the child was killed by a signal, the status contains the signal number in bits 0-7, and bit 7 (core dump flag) may be set
- Macros: WIFEXITED(status), WEXITSTATUS(status), WIFSIGNALED(status), WTERMSIG(status), WIFSTOPPED(status), WSTOPSIG(status)

## Examples

### Example 1: Basic wait() Usage

Write a program where parent waits for child to complete:

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
 pid_t pid;
 int status;

 pid = fork();

 if (pid < 0) {
 perror("fork failed");
 exit(1);
 }

 if (pid == 0) {
 // Child process
 printf("Child: My PID is %d\n", getpid());
 printf("Child: Executing ls command\n");
 execlp("ls", "ls", "-l", NULL);
 perror("execlp failed");
 exit(1);
 } else {
 // Parent process
 printf("Parent: Created child with PID %d\n", pid);
 printf("Parent: Waiting for child to finish...\n");

 pid_t terminated_pid = wait(&status);

 printf("Parent: Child %d terminated\n", terminated_pid);

 if (WIFEXITED(status)) {
 printf("Parent: Child exited normally with status %d\n",
 WEXITSTATUS(status));
 } else if (WIFSIGNALED(status)) {
 printf("Parent: Child killed by signal %d\n",
 WTERMSIG(status));
 }
 }

 return 0;
}
```

**Output:**

```
Parent: Created child with PID 12345
Parent: Waiting for child to finish...
Child: My PID is 12345
Child: Executing ls command
[ls output]
Parent: Child 12345 terminated
Parent: Child exited normally with status 0
```

### Example 2: Using waitpid() with WNOHANG

Create multiple children and handle them without blocking:

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
 pid_t pid;
 int status;
 int num_children = 3;

 for (int i = 0; i < num_children; i++) {
 pid = fork();

 if (pid < 0) {
 perror("fork failed");
 exit(1);
 }

 if (pid == 0) {
 // Child process - sleep for random time
 sleep(i + 1);
 printf("Child %d (PID %d) finishing\n", i, getpid());
 exit(i * 10);
 }
 }

 // Parent process - wait for all children
 int children_terminated = 0;
 while (children_terminated < num_children) {
 pid_t terminated_pid = waitpid(-1, &status, WNOHANG);

 if (terminated_pid > 0) {
 children_terminated++;
 printf("Parent: Child %d terminated (exit status: %d)\n",
 terminated_pid, WEXITSTATUS(status));
 } else if (terminated_pid == 0) {
 // No child terminated yet, do other work
 printf("Parent: Doing other work, no child yet...\n");
 sleep(1);
 } else {
 // Error or no more children
 break;
 }
 }

 printf("Parent: All children terminated\n");
 return 0;
}
```

### Example 3: Using wait3() for Resource Usage

Monitor child process resource utilization:

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/resource.h>
#include <sys/time.h>

int main() {
 pid_t pid;
 int status;
 struct rusage usage;

 pid = fork();

 if (pid < 0) {
 perror("fork failed");
 exit(1);
 }

 if (pid == 0) {
 // Child process - perform some computation
 printf("Child: Starting computation\n");
 long sum = 0;
 for (long i = 0; i < 100000000; i++) {
 sum += i;
 }
 printf("Child: Computation complete, sum = %ld\n", sum);
 exit(0);
 } else {
 // Parent process - wait and get resource usage
 pid_t terminated_pid = wait3(&status, 0, &usage);

 if (WIFEXITED(status)) {
 printf("Parent: Child exited with status %d\n",
 WEXITSTATUS(status));
 }

 printf("\nResource Usage Information:\n");
 printf("User CPU time: %ld.%06ld seconds\n",
 usage.ru_utime.tv_sec, usage.ru_utime.tv_usec);
 printf("System CPU time: %ld.%06ld seconds\n",
 usage.ru_stime.tv_sec, usage.ru_stime.tv_usec);
 printf("Max resident set size: %ld KB\n", usage.ru_maxrss);
 printf("Page reclaims (soft page faults): %ld\n", usage.ru_minflt);
 printf("Page faults (hard page faults): %ld\n", usage.ru_majflt);
 printf("Context switches (voluntary): %ld\n", usage.ru_nvcsw);
 printf("Context switches (involuntary): %ld\n", usage.ru_nivcsw);
 }

 return 0;
}
```

## Exam Tips

1. **Remember the return values**: wait() returns child PID on success, -1 on error (ECHILD if no children). waitpid() additionally returns 0 if WNOHANG is set and no child has exited.

2. **Status macros are crucial**: For exams, memorize WIFEXITED(status), WEXITSTATUS(status), WIFSIGNALED(status), WTERMSIG(status). Questions frequently ask about extracting exit codes or signal numbers.

3. **Difference between wait(), waitpid(), and wait3()**: wait3() provides resource usage information via struct rusage, while waitpid() provides options for non-blocking waits and specific child selection.

4. **Zombie process concept**: A process that has terminated but whose parent has not yet called wait() to read its status remains as a zombie. This is important for preventing process table overflow.

5. **Handling multiple children**: When a parent has multiple children, use waitpid() with pid = -1 in a loop to reap all children and prevent zombie creation.

6. **Wait vs waitpid behavior**: wait() is equivalent to waitpid(-1, &status, 0) - it blocks until any child terminates.

7. **Signal handling consideration**: If a child is stopped (not terminated) by a signal, use WIFSTOPPED() macro. The child can later be continued with SIGCONT.
