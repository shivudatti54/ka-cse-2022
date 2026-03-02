# Process Creation Using fork() System Call

## Introduction

The **fork()** system call is one of the most fundamental concepts in operating systems, particularly in Unix-like systems. It serves as the primary mechanism for creating new processes in Linux and UNIX environments. Understanding fork() is essential for any computer science engineer as it forms the backbone of process management and multitasking in modern operating systems.

In the context of 's Operating Systems syllabus (Module 4), fork() represents the cornerstone of process creation. When a process calls fork(), the operating system creates an almost exact copy of the calling process. The original process is called the **parent process**, while the newly created process is called the **child process**. Both processes continue execution from the point where fork() returns, but with different return values that allow the program to distinguish between parent and child.

The importance of fork() extends beyond simple process creation. It enables parallel processing, allows programs to create worker processes for handling multiple tasks concurrently, and is extensively used in system programming, daemon processes, and client-server applications. Modern operating systems implement fork() with optimizations like Copy-on-Write (COW) to make process creation efficient despite the apparent complexity of duplicating an entire address space.

## Key Concepts

### The fork() System Call

The fork() function is declared as:

```c
#include <unistd.h>
pid_t fork(void);
```

When fork() is called, the kernel performs the following operations:

1. Creates a new process control block (PCB) in the kernel
2. Allocates a new process ID (PID) for the child process
3. Copies the parent's context including the program counter, register values, and open file descriptors
4. Duplicate the parent's address space (with Copy-on-Write optimization)
5. Returns twice - once to the parent with the child's PID, once to the child with value 0

### Return Values of fork()

The fork() function returns different values to parent and child:

- **Positive value**: Returned to the parent process. This value is the Process ID (PID) of the newly created child process.
- **Zero (0)**: Returned to the child process, indicating it is the newly created process.
- **Negative value**: Returned to the parent if process creation fails (error condition).

### Copy-on-Write (COW) Mechanism

Modern Unix systems implement a memory optimization called **Copy-on-Write**. Instead of immediately copying the entire parent's memory to the child, both processes initially share the same physical memory pages. The actual copying occurs only when either process attempts to modify a memory page. This makes fork() extremely efficient for programs that immediately call exec() or for read-heavy operations.

### Process Hierarchy

Each process in Unix has a parent except **init** (PID 1), which is the ancestor of all processes. The relationship can be viewed using commands like:

- `ps -ef` - shows full process hierarchy
- `pstree` - displays processes in tree format
- `getpid()` - returns current process ID
- `getppid()` - returns parent process ID

### Differences Between Parent and Child

After fork(), the parent and child processes have:

- **Different PIDs**: Each has a unique process identifier
- **Shared everything else initially**: Open files, working directory, memory (COW)
- **Independent execution**: Both run concurrently
- **Separate address spaces**: Despite initial sharing, they have distinct memory

### The exec() Family

fork() is often followed by exec() family of functions, which replace the child's memory with a new program. This two-step process (fork + exec) is the standard way to run programs in Unix:

1. fork() creates a copy of the current program
2. exec() replaces that copy with a new program

### vfork() System Call

The vfork() function is similar to fork() but:

- Does not copy the parent's address space (for efficiency)
- Child runs in parent's address space until exec() or exit()
- Parent is suspended until child terminates
- Now largely obsolete due to COW optimization in fork()

## Examples

### Example 1: Basic fork() Usage

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
 pid_t pid;

 printf("Before fork - Process ID: %d\n", getpid());

 pid = fork();

 if (pid < 0) {
 // Error occurred
 fprintf(stderr, "Fork failed\n");
 return 1;
 }
 else if (pid == 0) {
 // Child process
 printf("I am the child - My PID: %d, Parent PID: %d\n",
 getpid(), getppid());
 printf("fork() returned: 0 to child\n");
 }
 else {
 // Parent process
 printf("I am the parent - My PID: %d, Child PID: %d\n",
 getpid(), pid);
 printf("fork() returned: %d to parent\n", pid);
 }

 printf("This prints from both processes\n");
 return 0;
}
```

**Output Explanation:**

- The program prints "Before fork" once
- After fork(), both processes continue execution
- Child gets return value 0, Parent gets child's PID (> 0)
- "This prints from both processes" appears twice

### Example 2: Demonstrating Multiple Forks

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
 pid_t pid1, pid2;

 printf("Original process: PID = %d\n", getpid());

 pid1 = fork();

 if (pid1 == 0) {
 // First child process
 printf("First child: PID = %d, Parent = %d\n",
 getpid(), getppid());
 }
 else {
 // Parent creates second child
 pid2 = fork();

 if (pid2 == 0) {
 // Second child process
 printf("Second child: PID = %d, Parent = %d\n",
 getpid(), getppid());
 }
 else {
 // Original parent
 printf("Parent: PID = %d\n", getpid());
 printf("Children: PID1 = %d, PID2 = %d\n", pid1, pid2);
 }
 }

 return 0;
}
```

**Step-by-step execution:**

1. Original process (P) calls first fork()
2. Creates first child (C1), P returns with pid1 > 0, C1 returns with 0
3. P then calls second fork(), creates second child (C2)
4. Now we have 4 processes running: P, C1, and C2

### Example 3: fork() with wait() - Avoiding Orphan Processes

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

int main() {
 pid_t pid;
 int status;

 pid = fork();

 if (pid == 0) {
 // Child process
 printf("Child starting computation...\n");
 sleep(2); // Simulate some work
 printf("Child finishing...\n");
 _exit(5); // Child exits with status 5
 }
 else if (pid > 0) {
 // Parent process
 printf("Parent waiting for child (PID: %d)\n", pid);
 wait(&status); // Parent waits for child to complete

 if (WIFEXITED(status)) {
 printf("Child exited with status: %d\n",
 WEXITSTATUS(status));
 }
 printf("Parent continuing after child completion\n");
 }
 else {
 fprintf(stderr, "Fork failed\n");
 return 1;
 }

 return 0;
}
```

**Key points:**

- `wait()` blocks parent until child terminates
- `WIFEXITED()` checks if child terminated normally
- `WEXITSTATUS()` extracts the exit status
- `_exit()` is used instead of `exit()` in child after fork() to prevent flushing parent's buffers twice

## Exam Tips

1. **Remember the three return values**: +ve (parent gets child's PID), 0 (child gets this), -1 (error occurred)

2. **fork() creates a copy**: The child gets an exact copy of parent's address space including all variables, open files, and program counter

3. **Copy-on-Write optimization**: Modern systems don't actually copy memory immediately - they share until modification

4. **fork() + exec() pattern**: This is the standard Unix way to run new programs - fork creates process, exec replaces program

5. **Avoiding zombie processes**: Always use wait() or waitpid() in parent to reap terminated children

6. **Different from Windows CreateProcess()**: fork() is Unix-specific; Windows uses different API for process creation

7. **vfork() is deprecated**: Due to COW, vfork() is rarely used in modern programming

8. **File descriptor sharing**: Parent and child share file descriptors (same file table entries), affecting file position

9. **printf buffering issue**: Remember that printf buffers may be duplicated, leading to unexpected output - use fflush() or \_exit()

10. **Process ID uniqueness**: Each process has unique PID; getpid() returns current, getppid() returns parent's PID
