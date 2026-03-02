# **Shared Memory**

Shared memory is a region of memory that can be accessed by multiple processes simultaneously. It is a type of inter-process communication (IPC) mechanism that allows processes to share data with each other.

## **How Shared Memory Works**

Shared memory is created using the `memmap` system call, which maps a file or a block of memory into the address space of a process. The memory region is shared between the process and all processes that access it.

### Key Concepts

- **Shared Memory Region**: A region of memory that can be accessed by multiple processes.
- **Process Address Space**: The memory space of a process, which includes the shared memory region.
- **Shm_open**: A system call used to create a shared memory region.

### Example

```c
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>

int main() {
    int shm_fd = shm_open("my_shm", O_RDWR | O_CREAT, 0644);
    if (shm_fd == -1) {
        perror("shm_open");
        return 1;
    }

    struct shmid_ds sb;
    if (fstat(shm_fd, &sb) == -1) {
        perror("fstat");
        return 1;
    }

    int *shared_data = mmap(NULL, sb.ss_size, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    if (shared_data == MAP_FAILED) {
        perror("mmap");
        return 1;
    }

    *shared_data = 10;
    printf("%d\n", *shared_data);

    munmap(shared_data, sb.ss_size);
    close(shm_fd);
    return 0;
}
```

# **Client-Server Properties**

Client-server properties refer to the characteristics that define a client-server system.

### Key Concepts

- **Client**: A process that requests a service from a server.
- **Server**: A process that provides a service to clients.
- **Request-Response Model**: A model where a client sends a request to the server and receives a response.
- **Synchronous-Asynchronous Model**: A model where clients wait for the response from the server or receive it asynchronously.

### Example

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Server function
int server(int client_fd) {
    char message[1024];
    read(client_fd, message, 1024);
    printf("Received message: %s\n", message);
    return 0;
}

int main() {
    int server_fd = socket(AF_UNIX, SOCK_STREAM, 0);
    if (server_fd == -1) {
        perror("socket");
        return 1;
    }

    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
        perror("bind");
        return 1;
    }

    if (listen(server_fd, 3) == -1) {
        perror("listen");
        return 1;
    }

    printf("Waiting for a connection...\n");

    int client_fd = accept(server_fd, (struct sockaddr *)&client_addr, NULL);
    if (client_fd == -1) {
        perror("accept");
        return 1;
    }

    server(client_fd);
    close(client_fd);
    close(server_fd);
    return 0;
}
```

# **Passing File Descriptors**

File descriptors are used to represent open files in a process.

### Key Concepts

- **File Descriptor**: A small integer that represents an open file.
- **FD Read**: Reading from a file descriptor.
- **FD Write**: Writing to a file descriptor.
- **FD Close**: Closing a file descriptor.

### Example

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    int fd1 = open("file1.txt", O_RDWR);
    int fd2 = open("file2.txt", O_RDWR);

    write(fd1, "Hello", 5);
    write(fd2, "World", 5);

    close(fd1);
    close(fd2);
    return 0;
}
```

# **An Open Server Version 1**

This is a simple example of an open server that listens for incoming connections and handles them.

### Key Concepts

- **Server Socket**: A socket that is bound to a specific address and port.
- **Client Socket**: A socket that connects to the server socket.
- **Accept Function**: A function used to accept incoming client connections.

### Example

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

// Server function
void server(int server_fd) {
    char message[1024];
    recv(server_fd, message, 1024, 0);
    printf("Received message: %s\n", message);
}

int main() {
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1) {
        perror("socket");
        return 1;
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);
    inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr);

    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
        perror("bind");
        return 1;
    }

    if (listen(server_fd, 3) == -1) {
        perror("listen");
        return 1;
    }

    printf("Waiting for a connection...\n");

    int client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_len);
    if (client_fd == -1) {
        perror("accept");
        return 1;
    }

    server(client_fd);
    close(client_fd);
    close(server_fd);
    return 0;
}
```
