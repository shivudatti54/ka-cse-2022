# Process Termination and the `wait` System Call

## 1. Introduction to Process Lifecycle

In Unix-based operating systems, processes are the fundamental units of execution. A process is created (`fork`), executes a program (`exec`), and eventually terminates. Proper management of this lifecycle is crucial to prevent **zombie processes** (defunct processes that have terminated but whose status has not yet been read by their parent) and to ensure resources are cleaned up correctly.

Process termination can occur in several ways:

- Normal termination (e.g., returning from `main`, calling `exit()`).
- Abnormal termination (e.g., being killed by a signal, a segmentation fault).

The `wait` and `waitpid` system calls allow a parent process to synchronize with its children and reap their termination status, which is the focus of this topic.

## 2. The `exit()` Function: Voluntary Termination

A process can voluntarily terminate itself using the `exit()` function, defined in `<stdlib.h>`.

```c
#include <stdlib.h>
void exit(int status);
```

The `status` argument is the **exit status** of the process. By convention, a status of `0` indicates success, and any non-zero value indicates a specific error or abnormal termination. This status is made available to the parent process when it calls `wait`.

When `exit()` is called, the following actions occur:

1.  Exit handlers (functions registered with `atexit()`) are called in reverse order of their registration.
2.  All standard I/O streams are flushed and closed.
3.  The `_exit()` system call is invoked (discussed next).

## 3. The `_exit()` and `_Exit()` Functions: Kernel-Level Termination

The `_exit()` and `_Exit()` functions provide a more direct path to termination, bypassing the user-level cleanup performed by `exit()`.

```c
#include <unistd.h>
void _exit(int status);

#include <stdlib.h>
void _Exit(int status);
```

These functions:

- Immediately terminate the process.
- Do **not** flush standard I/O buffers.
- Do **not** call exit handlers registered with `atexit()`.
- Return the `status` value to the kernel, where it becomes available to the parent via `wait`.

`_exit()` is typically used in a child process after a `fork()` to avoid undoing the parent's state (like flushing buffers that are also held by the parent).

## 4. The `wait()` System Call

The `wait()` system call allows a parent process to block its execution until one of its child processes terminates. It is declared in `<sys/wait.h>`.

```c
#include <sys/wait.h>
pid_t wait(int *statloc);
```

**Parameters:**

- `statloc`: A pointer to an integer where the termination status of the child will be stored. If NULL, the status is discarded.

**Return Value:**

- On success: Returns the **Process ID (PID)** of the terminated child.
- On failure: Returns `-1` (e.g., if the calling process has no more child processes).

The information in `statloc` is encoded. Macros are provided to interpret it:

| Macro                 | Description                                                                                                                   |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| `WIFEXITED(status)`   | Returns true if the child terminated normally (e.g., via `exit`)                                                              |
| `WEXITSTATUS(status)` | If `WIFEXITED` is true, returns the exit status of the child (the low-order 8 bits of the `status` argument passed to `exit`) |
| `WIFSIGNALED(status)` | Returns true if the child was terminated by a signal                                                                          |
| `WTERMSIG(status)`    | If `WIFSIGNALED` is true, returns the number of the signal that caused the termination                                        |
| `WIFSTOPPED(status)`  | Returns true if the child is currently stopped (used with job control)                                                        |
| `WSTOPSIG(status)`    | If `WIFSTOPPED` is true, returns the number of the signal that caused the child to stop                                       |

**Example: Using `wait()`**

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    pid_t pid;
    int status;

    if ((pid = fork()) < 0) {
        perror("fork failed");
        exit(1);
    } else if (pid == 0) {
        /* Child process */
        printf("Child PID: %d is running\n", getpid());
        sleep(2); // Simulate some work
        exit(42);  // Child exits with status 42
    } else {
        /* Parent process */
        printf("Parent PID: %d is waiting for child (%d)...\n", getpid(), pid);
        pid_t child_pid = wait(&status); // Block until a child exits

        if (WIFEXITED(status)) {
            printf("Child PID %d exited normally with status: %d\n", child_pid, WEXITSTATUS(status));
        } else if (WIFSIGNALED(status)) {
            printf("Child PID %d was killed by signal: %d\n", child_pid, WTERMSIG(status));
        }
    }
    return 0;
}
```

_Output:_

```
Parent PID: 1234 is waiting for child (1235)...
Child PID: 1235 is running
Child PID 1235 exited normally with status: 42
```

## 5. The `waitpid()` System Call: Precision Waiting

The `wait()` call has limitations: it blocks until _any_ child terminates and offers no control over which child to wait for. The `waitpid()` system call addresses these limitations.

```c
#include <sys/wait.h>
pid_t waitpid(pid_t pid, int *statloc, int options);
```

**Parameters:**

- `pid`: Specifies which child process(es) to wait for.
  - `pid == -1`: Wait for **any** child process (same as `wait`).
  - `pid > 0`: Wait for the specific child whose process ID equals `pid`.
  - `pid == 0`: Wait for any child process whose process group ID equals that of the calling process.
  - `pid < -1`: Wait for any child process whose process group ID equals the absolute value of `pid`.
- `statloc`: Same as `wait()` - a pointer to store the status.
- `options`: Modify the behavior of `waitpid`. Common options are:
  - `0`: Default behavior - blocks until a child specified by `pid` terminates.
  - `WNOHANG`: Return immediately if no child has terminated yet (**non-blocking** or "polling" mode).
  - `WUNTRACED`: Also return if a child has stopped (but not terminated via `ptrace`).

**Return Value:**

- On success: Returns the PID of the child whose status changed.
- If `WNOHANG` was used and no child has terminated: Returns `0`.
- On failure: Returns `-1`.

**Example: Using `waitpid()` with `WNOHANG`**

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    pid_t pid;
    int status;

    if ((pid = fork()) < 0) {
        perror("fork failed");
        exit(1);
    } else if (pid == 0) {
        /* Child process */
        printf("Child is working...\n");
        sleep(5); // Simulate a long-running task
        exit(0);
    } else {
        /* Parent process */
        // Check on the child periodically without blocking
        while (waitpid(pid, &status, WNOHANG) == 0) {
            printf("Parent: Child is still running. Doing other work...\n");
            sleep(1); // Do some parent work
        }
        printf("Parent: Child has finally terminated.\n");
    }
    return 0;
}
```

_Output:_

```
Child is working...
Parent: Child is still running. Doing other work...
Parent: Child is still running. Doing other work...
Parent: Child is still running. Doing other work...
Parent: Child is still running. Doing other work...
Parent: Child has finally terminated.
```

## 6. Zombie Processes and the Need for `wait`

When a process terminates, its entry in the process table is not immediately freed. It is kept until the parent calls `wait()` or `waitpid()` to read its exit status. A process in this state is called a **zombie** or **defunct process**.

```
+----------------+      Terminates      +----------------+
|  Child Process | -------------------> |   Zombie       |
| (PID = 1235)   |                      | (PID = 1235)   |
+----------------+                      +----------------+
                                            ^
                                            | Parent must call
                                            | wait() to "reap"
                                            |
                                      +-------------+
                                      | Parent      |
                                      | Process     |
                                      +-------------+
```

**Why are zombies necessary?**
The kernel must keep a minimal amount of information about the terminated process (like its PID and exit status) so the parent can later check how it ended. If the parent were to `fork()` again, the kernel might reuse the zombie's PID before the parent had a chance to read its status, causing confusion.

**The Danger of Zombies:**
Zombies do not use CPU resources, but they consume a slot in the system's process table. If a parent continuously creates children but never waits for them (`wait`s), the process table can fill up, preventing any new processes from being created.

A process whose parent terminates without waiting for it becomes an **orphan** and is automatically adopted by the `init` process (PID 1), which periodically calls `wait()` to clean up these orphans, preventing them from becoming permanent zombies.

## 7. Race Conditions and Synchronization

A **race condition** occurs when the outcome of a program depends on the non-deterministic ordering of events in concurrently executing processes or threads. The timing of `fork()`, `exec()`, and `wait()` can easily create race conditions.

**Example Race Condition:**
A parent forks a child and then continues executing its own code. The parent's next instruction and the child's entire execution are now in a "race." If the parent's next action depends on the child having already completed its work, the result is unpredictable.

**Solution:**
Proper use of `wait()` or `waitpid()` is the primary tool for synchronizing a parent with its children, ensuring the parent does not proceed until the child has finished its designated task.

## 8. Comparison: `wait()` vs. `waitpid()`

| Feature          | `wait(&status)`                       | `waitpid(pid, &status, options)`                |
| :--------------- | :------------------------------------ | :---------------------------------------------- |
| **Target Child** | Any child (first one that terminates) | Specific child or group of children             |
| **Blocking**     | Always blocks                         | Can be non-blocking (`WNOHANG`)                 |
| **Options**      | None                                  | Supports `WNOHANG`, `WUNTRACED`, etc.           |
| **Use Case**     | Simple scenarios with few children    | Complex scenarios requiring control and polling |

## 9. Exam Tips

1.  **Know the Macros:** Be able to write and interpret the status-checking macros (`WIFEXITED`, `WEXITSTATUS`, `WIFSIGNALED`, `WTERMSIG`). They are a favorite exam topic.
2.  **Zombie Explanation:** Understand precisely _why_ zombies exist and what problem they solve. Be prepared to explain the lifecycle from `fork` to termination to zombie to reaping.
3.  **`waitpid` Arguments:** Memorize the meaning of the different `pid` values for `waitpid` (`-1`, `>0`, `0`, `<-1`). Pay special attention to the `WNOHANG` option and its return values (PID, 0, -1).
4.  **Race Conditions:** Be able to identify a code snippet with a potential race condition between parent and child and suggest using `wait` to fix it.
5.  **`exit` vs. `_exit`:** Remember the key difference: `exit` performs user-level cleanup (flushing buffers, calling `atexit` functions), while `_exit` does not. The correct choice in a child process after `fork` is often `_exit`.
