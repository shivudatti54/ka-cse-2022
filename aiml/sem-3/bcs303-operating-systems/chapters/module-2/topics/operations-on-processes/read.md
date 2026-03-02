# **Operations on Processes**

## **Overview**

In operating systems, a process is a program in execution. Processes are independent entities that can be executed concurrently. Operations on processes refer to the various ways in which processes can be created, managed, and terminated.

## **Process Creation Operations**

### 1. Fork

- **Definition:** The `fork` system call creates a new process by duplicating an existing process.
- **Syntax:** `fork()`
- **Example:**

      ```c

  #include <stdio.h>
  #include <stdlib.h>

int main() {
pid_t pid;
pid = fork();
if (pid == 0) {
// Child process
printf("Hello from child process\n");
} else {
// Parent process
printf("Hello from parent process\n");
}
return 0;
}

````

    In this example, the `fork` system call creates a new process, and the child process prints "Hello from child process", while the parent process prints "Hello from parent process".

### 2. Vfork

*   **Definition:** The `vfork` system call is similar to `fork`, but it creates a new process, and then waits until the child process starts executing before returning in the parent process.
*   **Syntax:** `vfork()`
*   **Example:**

    ```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    pid_t pid;
    pid = vfork();
    if (pid == 0) {
        // Child process
        printf("Hello from child process\n");
    } else {
        // Parent process
        printf("Hello from parent process\n");
    }
    return 0;
}
````

    In this example, the `vfork` system call creates a new process, and then waits until the child process starts executing before returning in the parent process.

### 3. Exec

- **Definition:** The `exec` system call replaces the current process image with a new one, effectively terminating the current process.
- **Syntax:** `exec(path_name)`
- **Example:**

      ```c

  #include <stdio.h>
  #include <stdlib.h>

int main() {
execl("/bin/ls", "ls", NULL);
return 0;
}

````

    In this example, the `execl` system call replaces the current process image with the `ls` command, effectively terminating the current process.

**Process Termination Operations**
----------------------------------

### 1. Exit

*   **Definition:** The `exit` system call terminates a process and returns an exit status to the operating system.
*   **Syntax:** `exit(status)`
*   **Example:**

    ```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    exit(0);
    return 0;
}
````

    In this example, the `exit` system call terminates the process with a status of 0.

### 2. Wait

- **Definition:** The `wait` system call blocks the parent process until one of its child processes terminates.
- **Syntax:** `wait(&status)`
- **Example:**

      ```c

  #include <stdio.h>
  #include <stdlib.h>

int main() {
pid_t pid;
pid = fork();
if (pid == 0) {
// Child process
printf("Hello from child process\n");
exit(0);
} else {
// Parent process
printf("Hello from parent process\n");
wait(NULL);
}
return 0;
}

````

    In this example, the `wait` system call blocks the parent process until the child process terminates.

**Process Management Operations**
----------------------------------

### 1. Kill

*   **Definition:** The `kill` system call sends a signal to a process to terminate or interrupt it.
*   **Syntax:** `kill(pid, sig)`

    ```c
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

int main() {
    pid_t pid;
    pid = fork();
    if (pid == 0) {
        // Child process
        signal(SIGINT, SIGKILL);
        while (1) {
            printf("Hello from child process\n");
            sleep(1);
        }
    } else {
        // Parent process
        printf("Hello from parent process\n");
        kill(pid, SIGKILL);
    }
    return 0;
}
````

    In this example, the `kill` system call sends a `SIGKILL` signal to the child process to terminate it.

### 2. Ctrl+C

- **Definition:** The `Ctrl+C` keyboard combination sends a `SIGINT` signal to the current process.
- **Example:**

      ```c

  #include <stdio.h>
  #include <stdlib.h>
  #include <signal.h>

int main() {
signal(SIGINT, SIG_DFL);
while (1) {
printf("Hello from process\n");
sleep(1);
}
}

```

    In this example, the `Ctrl+C` keyboard combination sends a `SIGINT` signal to the process, which terminates it.
```
