# **UNIX SYSTEM PROGRAMMING**

**Module: Process Control: Introduction, Process Identifiers, fork, vfork, exit, wait, waitpid, wait3**

---

## **Introduction**

In UNIX, a process is a program in execution. A program can create multiple processes. This is achieved through process control. The process control allows a program to manage and control the creation, execution, and termination of processes.

## **Process Identifiers**

A process identifier (PID) is a unique number assigned to each process. It is used to identify a process. PIDs are assigned by the operating system when a process is created.

### Key Concepts

- Process identifier (PID)
- Unique number assigned to each process
- Assigned by the operating system
- Used to identify a process

## **Process Control Commands**

UNIX provides several process control commands to manage and control processes. Some of the most commonly used process control commands are:

### Key Concepts

- `fork()`: Creates a new process.
- `vfork()`: Creates a new process and also shares the parent's memory space.
- `exit()`: Terminates a process.
- `wait()`: Waits for a process to terminate.
- `waitpid()`: Waits for a process to terminate and also returns the PID.
- `wait3()`: Waits for a process to terminate and also returns the PID and exit status.

## **fork()**

The `fork()` system call creates a new process. The new process is a copy of the parent process. The `fork()` system call returns a value of 0 in the child process and the PID of the child process in the parent process.

### Syntax

```c
pid_t fork(void);
```

### Example

```c
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid;
    int status;

    pid = fork();

    if (pid < 0) {
        printf("Error occurred while creating a new process\n");
        return -1;
    }

    if (pid == 0) {
        printf("This is the child process\n");
        // Code to be executed in the child process
    } else {
        printf("This is the parent process\n");
        // Code to be executed in the parent process
        wait(NULL);
    }

    return 0;
}
```

## **vfork()**

The `vfork()` system call creates a new process and also shares the parent's memory space. The `vfork()` system call is similar to the `fork()` system call, but it also shares the parent's memory space.

### Syntax

```c
int vfork(void);
```

### Example

```c
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int status;

    status = vfork();

    if (status < 0) {
        printf("Error occurred while creating a new process\n");
        return -1;
    }

    if (status == 0) {
        printf("This is the child process\n");
        // Code to be executed in the child process
    } else {
        printf("This is the parent process\n");
        // Code to be executed in the parent process
        wait(NULL);
    }

    return 0;
}
```

## **exit()**

The `exit()` system call terminates a process. The `exit()` system call is used to terminate a process.

### Syntax

```c
int exit(int status);
```

### Example

```c
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    exit(0);
    return 0;
}
```

## **wait()**

The `wait()` system call waits for a process to terminate. The `wait()` system call is used to wait for a process to terminate.

### Syntax

```c
pid_t wait(int *wstatus);
```

### Example

```c
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid;
    int status;

    pid = fork();

    if (pid < 0) {
        printf("Error occurred while creating a new process\n");
        return -1;
    }

    if (pid == 0) {
        printf("This is the child process\n");
        // Code to be executed in the child process
        exit(0);
    } else {
        printf("This is the parent process\n");
        wait(NULL);
        printf("Child process terminated\n");
    }

    return 0;
}
```

## **waitpid()**

The `waitpid()` system call waits for a process to terminate and also returns the PID of the process.

### Syntax

```c
pid_t waitpid(int pid, int *wstatus, int options);
```

### Example

```c
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid;
    int status;

    pid = fork();

    if (pid < 0) {
        printf("Error occurred while creating a new process\n");
        return -1;
    }

    if (pid == 0) {
        printf("This is the child process\n");
        // Code to be executed in the child process
        exit(0);
    } else {
        printf("This is the parent process\n");
        waitpid(pid, NULL, 0);
        printf("Child process terminated\n");
    }

    return 0;
}
```

## **wait3()**

The `wait3()` system call waits for a process to terminate and also returns the PID and exit status of the process.

### Syntax

```c
pid_t wait3(int *wstatus, int *wgroupid, int *wpid);
```

### Example

```c
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid;
    int status;

    pid = fork();

    if (pid < 0) {
        printf("Error occurred while creating a new process\n");
        return -1;
    }

    if (pid == 0) {
        printf("This is the child process\n");
        // Code to be executed in the child process
        exit(0);
    } else {
        printf("This is the parent process\n");
        wait3(NULL, NULL, NULL);
        printf("Child process terminated\n");
    }

    return 0;
}
```

## **Conclusion**

In this chapter, we have learned about process control in UNIX. We have learned about process identifiers, fork, vfork, exit, wait, waitpid, and wait3. We have also learned about the syntax and examples of these process control commands. Understanding process control is essential for any UNIX programmer.
