# FIFOs (Named Pipes) in Unix/Linux

## Introduction

FIFOs, also known as Named Pipes, are a fundamental interprocess communication (IPC) mechanism in Unix/Linux systems. Unlike anonymous pipes which exist only during the lifetime of the process that creates them, FIFOs are filesystem objects with persistent names that allow unrelated processes to communicate. They follow the First-In-First-Out (FIFO) principle, meaning data written first is read first, maintaining the order of data transmission.

FIFOs are particularly important in client-server architectures, producer-consumer problems, and scenarios where multiple processes need to exchange data in a structured manner. In the syllabus, this topic covers the creation, operation, and practical applications of FIFOs in Unix programming. Understanding FIFOs is essential for system programming and developing robust distributed applications.

## Key Concepts

### What is a FIFO?

A FIFO (First In First Out) is a special type of file in Unix/Linux that serves as a named pipe. It appears as a regular file in the filesystem but behaves like a pipe - data flows sequentially from one end to the other. The key difference from anonymous pipes is that FIFOs have a name in the filesystem, allowing processes that do not have a parent-child relationship to communicate.

### Creating a FIFO

There are two primary methods to create a FIFO in Unix:

1. **Using mkfifo command (shell):**

```bash
mkfifo myfifo
```

2. **Using mkfifo() system call (programmatic):**

```c
#include <sys/types.h>
#include <sys/stat.h>
int mkfifo(const char *pathname, mode_t mode);
```

The `mkfifo()` function creates a FIFO special file at the location specified by `pathname`. The `mode` parameter specifies the permissions (e.g., 0666 for read/write by owner, group, and others).

### Opening and Using FIFOs

FIFOs are opened using the standard `open()` system call. However, there are important considerations:

- **Opening for reading:** If no process has the FIFO open for writing, `open()` blocks until some process opens it for writing.
- **Opening for writing:** If no process has the FIFO open for reading, `open()` blocks until some process opens it for reading.

This blocking behavior can be changed using the `O_NONBLOCK` flag:

- `O_RDONLY | O_NONBLOCK`: Opens for reading without blocking (returns -1 if no writer)
- `O_WRONLY | O_NONBLOCK`: Opens for writing without blocking (returns -1 if no reader)

### Reading and Writing to FIFOs

FIFOs use standard file operations:

- `read(fd, buffer, n)` - Read data from FIFO
- `write(fd, buffer, n)` - Write data to FIFO
- `close(fd)` - Close the FIFO

### FIFO Buffer Size

Unix pipes and FIFOs have a limited buffer size (typically 64KB on modern systems). When the buffer is full, `write()` blocks (or returns -1 with `O_NONBLOCK`). When empty, `read()` blocks (or returns 0 with `O_NONBLOCK`).

### Unlinking a FIFO

To remove a FIFO from the filesystem, use the `unlink()` system call:

```c
unlink("/path/to/fifo");
```

## Examples

### Example 1: Basic Producer-Consumer using FIFO

This example demonstrates a simple producer-consumer model where one process writes to the FIFO and another reads from it.

**Writer Process (producer.c):**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>

int main() {
 int fd;
 char *fifo = "/tmp/myfifo";

 // Create FIFO if it doesn't exist
 mkfifo(fifo, 0666);

 // Open FIFO for writing
 fd = open(fifo, O_WRONLY);

 // Write data to FIFO
 char msg[] = "Hello from Producer!";
 write(fd, msg, strlen(msg) + 1);

 close(fd);
 return 0;
}
```

**Reader Process (consumer.c):**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

int main() {
 int fd;
 char msg[100];

 // Open FIFO for reading
 fd = open("/tmp/myfifo", O_RDONLY);

 // Read data from FIFO
 read(fd, msg, sizeof(msg));
 printf("Received: %s\n", msg);

 close(fd);
 return 0;
}
```

**Execution:**

```bash
gcc producer.c -o producer
gcc consumer.c -o consumer
./producer &
./consumer
```

### Example 2: Client-Server Communication using FIFO

This example shows how to implement a simple client-server model where the server creates two FIFOs - one for client requests and one for server responses.

**Server (server.c):**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>

int main() {
 mkfifo("/tmp/request_fifo", 0666);
 mkfifo("/tmp/response_fifo", 0666);

 // Open request FIFO for reading
 int req_fd = open("/tmp/request_fifo", O_RDONLY);

 // Open response FIFO for writing
 int resp_fd = open("/tmp/response_fifo", O_WRONLY);

 char request[100], response[100];

 while(1) {
 // Read client request
 int n = read(req_fd, request, sizeof(request));
 if(n > 0) {
 printf("Server received: %s\n", request);

 // Process request (uppercase it)
 for(int i = 0; request[i]; i++)
 response[i] = toupper(request[i]);
 response[strlen(request)] = '\0';

 // Send response
 write(resp_fd, response, strlen(response) + 1);
 }
 }

 close(req_fd);
 close(resp_fd);
 return 0;
}
```

**Client (client.c):**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>

int main() {
 // Open request FIFO for writing
 int req_fd = open("/tmp/request_fifo", O_WRONLY);

 // Open response FIFO for reading
 int resp_fd = open("/tmp/response_fifo", O_RDONLY);

 char request[100], response[100];

 // Send request
 strcpy(request, "hello world");
 write(req_fd, request, strlen(request) + 1);

 // Read response
 read(resp_fd, response, sizeof(response));
 printf("Client received: %s\n", response);

 close(req_fd);
 close(resp_fd);
 return 0;
}
```

### Example 3: Non-blocking FIFO Operations

This example demonstrates handling FIFOs with `O_NONBLOCK` to prevent deadlocks.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>

int main() {
 char *fifo = "/tmp/nonblock_fifo";
 mkfifo(fifo, 0666);

 // Open with non-blocking
 int fd = open(fifo, O_WRONLY | O_NONBLOCK);

 if (fd == -1) {
 perror("open");
 // FIFO might not have a reader yet
 if (errno == ENXIO) {
 printf("No reader available. Retrying...\n");
 sleep(1);
 fd = open(fifo, O_WRONLY | O_NONBLOCK);
 }
 }

 if (fd != -1) {
 char msg[] = "Non-blocking message";
 int result = write(fd, msg, strlen(msg) + 1);

 if (result == -1) {
 perror("write");
 } else {
 printf("Wrote %d bytes\n", result);
 }
 close(fd);
 }

 return 0;
}
```

## Exam Tips

1. **FIFO vs Anonymous Pipe:** Remember that anonymous pipes require parent-child relationship, while FIFOs (named pipes) allow communication between any unrelated processes.

2. **Blocking Behavior:** In exam questions, always identify blocking scenarios - `open()` blocks if no process has the other end open, `read()` blocks if FIFO is empty, `write()` blocks if buffer is full.

3. **O_NONBLOCK Flag:** Know how `O_NONBLOCK` changes behavior - `read()` returns 0 for empty FIFO, `write()` returns -1 with errno=ENXIO if no reader.

4. **FIFO Creation:** The `mkfifo()` function returns 0 on success and -1 on failure. Don't forget to include `<sys/stat.h>` and `<sys/types.h>`.

5. **Buffer Size:** Remember that FIFOs have finite buffer (typically 64KB). If writer writes more than buffer size without reader, it will block.

6. **Permission Issues:** Always specify proper permissions (e.g., 0666) when creating FIFOs. Remember that umask affects the actual permissions.

7. **Cleanup:** Always close FIFO file descriptors and use `unlink()` to remove FIFO from filesystem when done.

8. **Common Errors:** ENXIO error occurs when opening FIFO for writing with no reader. EACCES occurs due to permission denied.

9. **Bidirectional Communication:** For two-way communication, you need TWO FIFOs - one for each direction, as FIFOs are unidirectional.

10. **FIFO as Regular File:** Remember that FIFOs appear as regular files in filesystem (shown by 'p' in ls -l output) but behave like pipes.
