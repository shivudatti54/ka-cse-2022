# Pipes in Unix/Linux

## Introduction

Pipes are one of the most fundamental and widely used Inter-Process Communication (IPC) mechanisms in Unix/Linux operating systems. A pipe is a unidirectional communication channel that allows data to flow between two related processes, typically between a parent process and its child process. Since their introduction in early Unix systems, pipes have become an essential tool for process communication and data streaming in shell commands, program execution, and complex system designs.

The importance of pipes in modern computing cannot be overstated. They form the backbone of the Unix philosophy of composing small, focused programs to accomplish complex tasks. When you use commands like `ls | grep "txt" | sort`, you are leveraging pipes to create a data pipeline. In system programming, pipes provide a simple yet powerful mechanism for parent-child process communication without the complexity of shared memory or message queues. Understanding pipes is essential for any computer science engineer, as they are extensively used in operating systems, shell scripting, client-server applications, and distributed systems.

## Key Concepts

### Types of Pipes

**1. Anonymous Pipes**
Anonymous pipes are the most common type of pipes in Unix/Linux systems. They are created using the `pipe()` system call and exist only within the kernel. These pipes are unidirectional, meaning data flows in one direction only. To enable bidirectional communication, two pipes must be created—one for each direction. Anonymous pipes are typically used for communication between parent and child processes that share a common ancestor.

The `pipe()` system call creates a pipe and returns two file descriptors: one for reading (`pipefd[0]`) and one for writing (`pipefd[1]`). The data written to the write end can be read from the read end in a First-In-First-Out (FIFO) manner. If a process attempts to read from an empty pipe, it will block until data is available. Similarly, if a process writes to a full pipe, it will block until data is read.

**2. Named Pipes (FIFOs)**
Named pipes, also known as FIFOs (First-In-First-Out), are special files in the filesystem that provide a named communication channel. Unlike anonymous pipes, named pipes persist in the filesystem and can be accessed by unrelated processes. They are created using the `mkfifo()` system call or the `mkfifo` shell command.

Named pipes appear as regular files in the filesystem, which means multiple processes can open them for reading or writing. However, the behavior is still unidirectional—a process cannot simultaneously read and write through the same FIFO without proper synchronization. Named pipes are particularly useful for client-server applications where the client and server are not parent-child related.

### Pipe Creation and Usage

The `pipe()` system call has the following prototype:

```c
#include <unistd.h>
int pipe(int pipefd[2]);
```

On success, `pipe()` returns 0 and populates `pipefd[0]` with the read end file descriptor and `pipefd[1]` with the write end file descriptor. On failure, it returns -1 and sets `errno`.

**Basic Pipe Creation Example:**

```c
int pipefd[2];
if (pipe(pipefd) == -1) {
 perror("pipe");
 exit(EXIT_FAILURE);
}
```

### Pipe Behavior and Characteristics

**1. Blocking Operations**
By default, read and write operations on pipes are blocking. A `read()` call on an empty pipe blocks until data is available. A `write()` call on a full pipe blocks until enough data is read to accommodate the write. The pipe buffer size is typically 64KB on modern Linux systems, but this can vary.

**2. End-of-File Behavior**
When all write ends of a pipe are closed, a subsequent `read()` returns 0, indicating end-of-file (EOF). This is crucial for process synchronization—reading processes must know when all writers have finished.

**3. Data Ordering**
Pipes guarantee FIFO ordering—data written first is read first. This sequential nature makes pipes suitable for streaming data between processes.

**4. Unrelated Process Communication**
Anonymous pipes only work between processes with a common ancestor (typically parent-child). For unrelated processes, named pipes (FIFOs) must be used.

### Pipe in fork() Context

When a process calls `fork()`, the child process inherits the parent's file descriptors, including pipe ends. This is the primary mechanism for parent-child communication:

1. Parent creates a pipe before fork
2. Parent forks a child process
3. Both processes have access to both pipe ends
4. Each process closes the unused end
5. Communication proceeds through the remaining ends

## Examples

### Example 1: Basic Parent-Child Communication Using Pipe

**Problem:** Create a pipe, fork a child process, and send a message from parent to child through the pipe.

**Solution:**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main() {
 int pipefd[2];
 pid_t pid;
 char write_msg[] = "Hello from parent!";
 char read_msg[100];

 // Create the pipe
 if (pipe(pipefd) == -1) {
 perror("pipe");
 exit(EXIT_FAILURE);
 }

 // Fork the process
 pid = fork();

 if (pid == -1) {
 perror("fork");
 exit(EXIT_FAILURE);
 }

 if (pid == 0) {
 // Child process
 close(pipefd[1]); // Close unused write end

 // Read from pipe
 ssize_t bytes_read = read(pipefd[0], read_msg, sizeof(read_msg));
 if (bytes_read > 0) {
 read_msg[bytes_read] = '\0';
 printf("Child received: %s\n", read_msg);
 }

 close(pipefd[0]); // Close read end when done
 exit(EXIT_SUCCESS);
 } else {
 // Parent process
 close(pipefd[0]); // Close unused read end

 // Write to pipe
 write(pipefd[1], write_msg, strlen(write_msg));

 close(pipefd[1]); // Close write end to send EOF

 wait(NULL); // Wait for child to finish
 printf("Parent: Child process completed\n");
 }

 return 0;
}
```

**Step-by-step explanation:**

1. First, we create a pipe using `pipe(pipefd)`, which gives us two file descriptors
2. We fork the process to create a child
3. In the child process, we close the write end (we only want to read)
4. The child reads from the pipe and prints the message
5. In the parent process, we close the read end (we only want to write)
6. The parent writes the message to the pipe
7. Parent closes the write end to signal EOF to the child
8. Parent waits for child to complete using `wait(NULL)`

### Example 2: Bidirectional Communication Using Two Pipes

**Problem:** Implement bidirectional communication between parent and child using two pipes.

**Solution:**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main() {
 int pipe_parent_to_child[2];
 int pipe_child_to_parent[2];
 pid_t pid;

 // Create two pipes
 if (pipe(pipe_parent_to_child) == -1 || pipe(pipe_child_to_parent) == -1) {
 perror("pipe");
 exit(EXIT_FAILURE);
 }

 pid = fork();

 if (pid == -1) {
 perror("fork");
 exit(EXIT_FAILURE);
 }

 if (pid == 0) {
 // Child process
 char msg_from_parent[100];
 char msg_to_parent[] = "Hello from child!";

 // Close unused ends in child
 close(pipe_parent_to_child[1]);
 close(pipe_child_to_parent[0]);

 // Read from parent
 read(pipe_parent_to_child[0], msg_from_parent, sizeof(msg_from_parent));
 printf("Child received from parent: %s\n", msg_from_parent);

 // Write to parent
 write(pipe_child_to_parent[1], msg_to_parent, strlen(msg_to_parent));

 // Close remaining ends
 close(pipe_parent_to_child[0]);
 close(pipe_child_to_parent[1]);

 exit(EXIT_SUCCESS);
 } else {
 // Parent process
 char msg_from_child[100];
 char msg_to_child[] = "Hello from parent!";

 // Close unused ends in parent
 close(pipe_parent_to_child[0]);
 close(pipe_child_to_parent[1]);

 // Write to child
 write(pipe_parent_to_child[1], msg_to_child, strlen(msg_to_child));

 // Read from child
 read(pipe_child_to_parent[0], msg_from_child, sizeof(msg_from_child));
 printf("Parent received from child: %s\n", msg_from_child);

 // Close remaining ends
 close(pipe_parent_to_child[1]);
 close(pipe_child_to_parent[0]);

 wait(NULL);
 }

 return 0;
}
```

### Example 3: Using Named Pipe (FIFO) for Unrelated Process Communication

**Problem:** Create a named pipe and have two unrelated processes communicate through it.

**Solution - Server Process (Writer):**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>

#define FIFO_PATH "/tmp/myfifo"

int main() {
 // Create FIFO if it doesn't exist
 mkfifo(FIFO_PATH, 0666);

 // Open FIFO for writing
 int fd = open(FIFO_PATH, O_WRONLY);
 if (fd == -1) {
 perror("open");
 exit(EXIT_FAILURE);
 }

 // Write data to FIFO
 char msg[] = "Message through named pipe!";
 write(fd, msg, strlen(msg));

 printf("Server: Message sent through FIFO\n");
 close(fd);

 return 0;
}
```

**Solution - Client Process (Reader):**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#define FIFO_PATH "/tmp/myfifo"

int main() {
 // Open FIFO for reading
 int fd = open(FIFO_PATH, O_RDONLY);
 if (fd == -1) {
 perror("open");
 exit(EXIT_FAILURE);
 }

 // Read data from FIFO
 char buffer[100];
 ssize_t bytes_read = read(fd, buffer, sizeof(buffer));

 if (bytes_read > 0) {
 buffer[bytes_read] = '\0';
 printf("Client: Received message: %s\n", buffer);
 }

 close(fd);
 // Optionally unlink FIFO: unlink(FIFO_PATH);

 return 0;
}
```

## Exam Tips

1. **Remember pipe() system call syntax**: The `pipe()` function takes an integer array of size 2 and returns 0 on success, -1 on failure. The first element is for reading, second is for writing.

2. **Close unused pipe ends**: Always close the unused end of the pipe in each process. This is crucial for proper EOF detection and resource management.

3. **Blocking nature of pipes**: Understand that read() blocks on empty pipe, write() blocks on full pipe. Use `fcntl()` with `O_NONBLOCK` flag for non-blocking I/O if needed.

4. **EOF detection**: When all write ends are closed, read() returns 0. This is how reading processes detect that writers have finished.

5. **Anonymous vs Named pipes**: Anonymous pipes require parent-child relationship, while named pipes (FIFOs) can connect unrelated processes through the filesystem.

6. **Pipe buffer size**: Default pipe buffer is 64KB on Linux. Writes larger than PIPE_BUF (4096 bytes) may not be atomic.

7. **Fork behavior**: After fork(), both parent and child inherit the pipe file descriptors. Both processes must close their respective unused ends for proper operation.

8. **FIFO creation**: Use `mkfifo()` or shell command `mkfifo` to create named pipes. Use `unlink()` to remove them when done.

9. **wait() usage**: Always use wait() or waitpid() in parent to prevent zombie processes after child termination.

10. **Direction confusion**: Remember—data flows from write end (pipefd[1]) to read end (pipefd[0]). A common mistake is to reverse this direction.
