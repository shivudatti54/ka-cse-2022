# Pipes and FIFOs: Inter-Process Communication Mechanisms

## Introduction to IPC

Inter-Process Communication (IPC) refers to the mechanisms that allow processes to exchange data and synchronize their actions. In Unix/Linux systems, various IPC methods exist, with Pipes and FIFOs being among the most fundamental and widely used. These mechanisms enable communication between related processes (parent-child) and unrelated processes, forming the backbone of many Unix utilities and system programming paradigms.

## What are Pipes?

A pipe is a unidirectional communication channel that allows data to flow in one direction only. It provides a means for one process to send data to another process. Pipes are created using the `pipe()` system call and are typically used for communication between related processes (those with a common ancestor).

### The pipe() System Call

```c
#include <unistd.h>
int pipe(int fd[2]);
```

The `pipe()` function creates a pipe and returns two file descriptors:

- `fd[0]` - the read end of the pipe
- `fd[1]` - the write end of the pipe

**Return value**: Returns 0 on success, -1 on error

### How Pipes Work: A Simple Example

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd[2];
    char buffer[100];
    char *message = "Hello through pipe!";

    // Create the pipe
    if (pipe(fd) == -1) {
        perror("pipe");
        return 1;
    }

    // Write to the pipe
    write(fd[1], message, strlen(message) + 1);

    // Read from the pipe
    read(fd[0], buffer, sizeof(buffer));
    printf("Received: %s\n", buffer);

    // Close both ends
    close(fd[0]);
    close(fd[1]);

    return 0;
}
```

### Pipe Communication Between Parent and Child Processes

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main() {
    int fd[2];
    pid_t pid;
    char buffer[100];

    if (pipe(fd) == -1) {
        perror("pipe");
        return 1;
    }

    pid = fork();

    if (pid < 0) {
        perror("fork");
        return 1;
    }

    if (pid > 0) {  // Parent process
        close(fd[0]);  // Close read end in parent

        char *message = "Message from parent";
        write(fd[1], message, strlen(message) + 1);
        close(fd[1]);

        wait(NULL);  // Wait for child to finish
    } else {        // Child process
        close(fd[1]);  // Close write end in child

        read(fd[0], buffer, sizeof(buffer));
        printf("Child received: %s\n", buffer);
        close(fd[0]);
    }

    return 0;
}
```

## Pipe Characteristics and Behavior

### Key Properties of Pipes

1. **Unidirectional**: Data flows in one direction only
2. **Byte-oriented**: Treats data as a stream of bytes
3. **Synchronization**: Reading blocks when pipe is empty, writing blocks when pipe is full
4. **Buffer size**: Limited capacity (typically 4KB-64KB)
5. **Automatic closing**: All copies of write end must be closed for read to see EOF

### Pipe Capacity and Blocking Behavior

```
+----------------+      write()      +----------------+
| Process A      | ----------------->| Pipe Buffer    |
| (Writer)       |                   | (Limited Size) |
+----------------+                   +----------------+
                                         |
                                         | read()
                                         v
                                    +----------------+
                                    | Process B      |
                                    | (Reader)       |
                                    +----------------+
```

When the pipe buffer is full, subsequent `write()` calls will block until space becomes available. When the pipe is empty, `read()` calls block until data is available.

## popen() and pclose() Functions

The `popen()` function creates a pipe and forks a child process to execute a shell command, providing a simpler interface than using `pipe()`, `fork()`, and `exec()` directly.

```c
#include <stdio.h>
FILE *popen(const char *command, const char *type);
int pclose(FILE *stream);
```

**Example using popen():**

```c
#include <stdio.h>

int main() {
    FILE *fp;
    char buffer[100];

    // Execute 'ls -l' command and read its output
    fp = popen("ls -l", "r");
    if (fp == NULL) {
        perror("popen");
        return 1;
    }

    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }

    pclose(fp);
    return 0;
}
```

## Limitations of Regular Pipes

Regular pipes have several limitations:

1. **Temporary existence**: Exist only as long as the processes using them
2. **Related processes**: Can only be used by processes with a common ancestor
3. **Unidirectional**: Data flows in one direction only
4. **No name**: Cannot be referenced by pathname

These limitations led to the development of FIFOs (Named Pipes).

## What are FIFOs?

FIFOs (First-In-First-Out), also known as Named Pipes, are similar to regular pipes but have a name in the filesystem. This allows unrelated processes to communicate through the FIFO.

### Creating FIFOs

FIFOs can be created in two ways:

1. **Using mkfifo() system call:**

```c
#include <sys/types.h>
#include <sys/stat.h>
int mkfifo(const char *pathname, mode_t mode);
```

2. **Using mkfifo command:**

```bash
$ mkfifo myfifo
```

### FIFO Example: Writer Process

```c
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd;
    char *fifo = "/tmp/myfifo";
    char message[] = "Hello from FIFO!";

    // Create the FIFO if it doesn't exist
    mkfifo(fifo, 0666);

    // Open FIFO for writing
    fd = open(fifo, O_WRONLY);
    write(fd, message, sizeof(message));
    close(fd);

    return 0;
}
```

### FIFO Example: Reader Process

```c
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

int main() {
    int fd;
    char *fifo = "/tmp/myfifo";
    char buffer[100];

    // Open FIFO for reading
    fd = open(fifo, O_RDONLY);
    read(fd, buffer, sizeof(buffer));
    printf("Received: %s\n", buffer);
    close(fd);

    // Remove the FIFO
    unlink(fifo);

    return 0;
}
```

## FIFO Characteristics and Behavior

### Key Properties of FIFOs

1. **Persistence**: Exist in the filesystem until explicitly removed
2. **Unrelated processes**: Can be used by any process with appropriate permissions
3. **Blocking behavior**: Opening for read blocks until another process opens for write, and vice versa
4. **Byte-stream oriented**: Like pipes, treat data as a stream of bytes

### FIFO Communication Model

```
Process A (Writer)          Process B (Reader)
      |                            |
      v                            v
+-----------+                +-----------+
| Open FIFO |                | Open FIFO |
| for write |                | for read  |
+-----------+                +-----------+
      |                            |
      v                            v
+-----------+                +-----------+
| Write data|                | Read data |
| to FIFO   |                | from FIFO |
+-----------+                +-----------+
      |                            |
      v                            v
+-----------+                +-----------+
| Close FIFO|                | Close FIFO|
+-----------+                +-----------+
```

## Comparison: Pipes vs FIFOs

| Feature                  | Regular Pipes               | FIFOs (Named Pipes)                |
| ------------------------ | --------------------------- | ---------------------------------- |
| **Lifetime**             | Process duration            | Filesystem persistence             |
| **Process Relationship** | Related processes only      | Any processes                      |
| **Naming**               | No name                     | Has filename in filesystem         |
| **Creation**             | pipe() system call          | mkfifo() or mkfifo command         |
| **Visibility**           | Private to creating process | Public through filesystem          |
| **Use Case**             | Parent-child communication  | Client-server, unrelated processes |

## Practical Applications and Examples

### Building a Simple Client-Server System

**Server Process (Reader):**

```c
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

int main() {
    int fd;
    char *fifo = "/tmp/service_fifo";
    char buffer[100];

    mkfifo(fifo, 0666);

    while (1) {
        printf("Server waiting for messages...\n");
        fd = open(fifo, O_RDONLY);
        read(fd, buffer, sizeof(buffer));
        printf("Server received: %s\n", buffer);
        close(fd);

        if (strcmp(buffer, "exit") == 0) {
            break;
        }
    }

    unlink(fifo);
    return 0;
}
```

**Client Process (Writer):**

```c
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[]) {
    int fd;
    char *fifo = "/tmp/service_fifo";

    if (argc < 2) {
        printf("Usage: %s <message>\n", argv[0]);
        return 1;
    }

    fd = open(fifo, O_WRONLY);
    write(fd, argv[1], strlen(argv[1]) + 1);
    close(fd);

    return 0;
}
```

### Implementing a Coprocess with popen()

Coprocesses are processes that run concurrently with the main process and communicate through pipes.

```c
#include <stdio.h>

int main() {
    FILE *fp;
    char buffer[100];

    // Create coprocess that converts text to uppercase
    fp = popen("tr '[:lower:]' '[:upper:]'", "w");
    if (fp == NULL) {
        perror("popen");
        return 1;
    }

    // Send data to coprocess
    fprintf(fp, "hello world\n");
    fprintf(fp, "this is a test\n");

    pclose(fp);
    return 0;
}
```

## Error Handling and Best Practices

### Common Errors with Pipes and FIFOs

1. **Forgetting to close unused ends**: Can cause deadlocks
2. **Not checking return values**: System calls can fail
3. **Buffer overflow**: Writing more than pipe capacity
4. **Race conditions**: In FIFO opening sequences

### Best Practices

1. Always check return values of system calls
2. Close unused pipe ends promptly
3. Use non-blocking I/O for better control when needed
4. Implement proper error handling and cleanup
5. Consider using select() or poll() for multiple I/O operations

## Exam Tips

1. **Remember the key differences** between pipes and FIFOs - pipes are for related processes, FIFOs for unrelated processes
2. **Understand the blocking behavior** - pipes block when full/empty, FIFOs block on open until counterpart opens
3. **Know the system calls** - pipe(), mkfifo(), popen(), pclose() with their parameters and return values
4. **Practice writing code examples** for both pipes and FIFOs
5. **Understand the file descriptor usage** - pipe() returns two FDs, FIFOs use regular file operations
6. **Remember that pipes are unidirectional** while some other IPC mechanisms (like sockets) can be bidirectional
