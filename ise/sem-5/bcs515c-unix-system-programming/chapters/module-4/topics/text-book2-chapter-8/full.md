# **UNIX SYSTEM PROGRAMMING**

## **CHAPTER 8: PROCESS CONTROL**

### Introduction

---

Process control is a fundamental aspect of UNIX system programming, allowing programmers to create, manage, and manipulate processes within a UNIX system. In this chapter, we will delve into the world of process control, exploring the various tools and techniques available for managing processes.

### Process Identifiers

---

A process identifier (PID) is a unique integer assigned to each process running in a UNIX system. PIDs are used to identify and manage processes, allowing programmers to track the status of individual processes and perform actions accordingly.

Understanding PIDs is crucial for process control, as it enables programmers to:

- Create and manage new processes
- Suspend and resume processes
- Kill and terminate processes
- Monitor process performance and resource usage

Here's an example of how to retrieve the PID of the current process using the `pidof` command:

```bash
$ pidof -s
1234
```

In this example, the `pidof` command returns the PID of the current process, which is 1234.

### Fork

---

The `fork` system call is used to create a new process by duplicating an existing process. The `fork` system call is similar to `vfork`, but it creates a new process with its own memory space, whereas `vfork` creates a new process with a shared memory space.

Here's an example of how to use `fork` to create a new process:

```c
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    pid_t pid;
    pid = fork();
    if (pid == 0) {
        // This is the child process
        printf("Hello from child process!\n");
    } else {
        // This is the parent process
        printf("Hello from parent process!\n");
    }
    return 0;
}
```

In this example, the `fork` system call creates a new process with a PID of 0. The child process prints a message, while the parent process prints a different message.

### vfork

---

The `vfork` system call is similar to `fork`, but it creates a new process with a shared memory space. The `vfork` system call is useful when you need to access shared memory or when you need to inherit the parent process's file descriptors.

Here's an example of how to use `vfork` to create a new process with a shared memory space:

```c
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    pid_t pid;
    pid = vfork();
    if (pid == 0) {
        // This is the child process
        int shared_var = 10;
        printf("Child process: shared_var = %d\n", shared_var);
    } else {
        // This is the parent process
        int shared_var = 10;
        printf("Parent process: shared_var = %d\n", shared_var);
    }
    return 0;
}
```

In this example, the `vfork` system call creates a new process with a shared memory space. The child process can access the shared memory variable `shared_var`, while the parent process cannot.

### Exit

---

The `exit` system call is used to terminate a process. The `exit` system call can be used to terminate a process immediately, or to terminate a process after a specified amount of time.

Here's an example of how to use `exit` to terminate a process immediately:

```c
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    exit(0);
    return 0;
}
```

In this example, the `exit` system call terminates the process immediately.

### Wait

---

The `wait` system call is used to suspend the execution of a process until a child process terminates. The `wait` system call can be used to wait for a child process to terminate and to retrieve the PID of the terminated child process.

Here's an example of how to use `wait` to suspend the execution of a process:

```c
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    pid_t pid;
    pid = fork();
    if (pid == 0) {
        // This is the child process
        sleep(5);
        exit(0);
    } else {
        // This is the parent process
        sleep(2);
        printf("Parent process: waiting for child process to terminate...\n");
        wait(NULL);
        printf("Parent process: child process terminated with PID %d\n", pid);
    }
    return 0;
}
```

In this example, the `wait` system call suspends the execution of the parent process until the child process terminates. The `wait` system call also retrieves the PID of the terminated child process.

### Waitpid

---

The `waitpid` system call is used to suspend the execution of a process until a child process terminates. The `waitpid` system call can be used to wait for a child process to terminate and to retrieve the PID of the terminated child process.

Here's an example of how to use `waitpid` to suspend the execution of a process:

```c
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    pid_t pid;
    pid = fork();
    if (pid == 0) {
        // This is the child process
        sleep(5);
        exit(0);
    } else {
        // This is the parent process
        sleep(2);
        printf("Parent process: waiting for child process to terminate...\n");
        waitpid(pid, NULL, 0);
        printf("Parent process: child process terminated with PID %d\n", pid);
    }
    return 0;
}
```

In this example, the `waitpid` system call suspends the execution of the parent process until the child process terminates. The `waitpid` system call also retrieves the PID of the terminated child process.

### Wait3

---

The `wait3` system call is used to suspend the execution of a process until a child process terminates. The `wait3` system call can be used to wait for a child process to terminate and to retrieve the PID of the terminated child process.

Here's an example of how to use `wait3` to suspend the execution of a process:

```c
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    pid_t pid;
    pid = fork();
    if (pid == 0) {
        // This is the child process
        sleep(5);
        exit(0);
    } else {
        // This is the parent process
        sleep(2);
        printf("Parent process: waiting for child process to terminate...\n");
        wait3(NULL, NULL, 0);
        printf("Parent process: child process terminated with PID %d\n", pid);
    }
    return 0;
}
```

In this example, the `wait3` system call suspends the execution of the parent process until the child process terminates. The `wait3` system call also retrieves the PID of the terminated child process.

### Case Study: Process Control

---

In this case study, we will explore how to use process control to manage a group of processes. We will create a parent process that creates multiple child processes, each of which will perform a different task.

Here's an example of how to create a parent process that creates multiple child processes:

```c
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    pid_t pids[5];
    for (int i = 0; i < 5; i++) {
        pids[i] = fork();
        if (pids[i] == 0) {
            // This is a child process
            printf("Child process %d: starting task...\n", i);
            sleep(i + 2);
            printf("Child process %d: completing task...\n", i);
            exit(0);
        }
    }
    printf("Parent process: waiting for child processes to complete...\n");
    for (int i = 0; i < 5; i++) {
        waitpid(pids[i], NULL, 0);
    }
    return 0;
}
```

In this example, the parent process creates five child processes using the `fork` system call. Each child process performs a different task, and the parent process waits for each child process to complete using the `waitpid` system call.

### Applications

---

Process control has numerous applications in UNIX system programming, including:

- **Job scheduling**: Process control is used to manage jobs, which are batches of processes that need to be executed.
- **Resource management**: Process control is used to manage resources, such as memory and CPU time, allocated to processes.
- **Security**: Process control is used to manage access control, including permissions and privileges granted to processes.
- **Fault tolerance**: Process control is used to manage fault-tolerant systems, including process restarts and recovery from failures.

### Further Reading

---

If you're interested in learning more about process control in UNIX system programming, here are some recommended resources:

- **"UNIX System Administration" by D. Richard Hipp**: This book provides a comprehensive overview of UNIX system administration, including process control.
- **"Linux System Programming" by Michael Kerrisk**: This book provides a comprehensive overview of Linux system programming, including process control.
- **"The UNIX Programming Environment" by Brian W. Kernighan and Dennis M. Ritchie**: This book provides a comprehensive overview of UNIX programming, including process control.

## Conclusion

In this chapter, we explored the world of process control in UNIX system programming. We learned about process identifiers, `fork`, `vfork`, `exit`, `wait`, `waitpid`, and `wait3`. We also explored case studies and applications of process control, including job scheduling, resource management, security, and fault tolerance. Finally, we provided further reading resources for those interested in learning more about process control in UNIX system programming.
