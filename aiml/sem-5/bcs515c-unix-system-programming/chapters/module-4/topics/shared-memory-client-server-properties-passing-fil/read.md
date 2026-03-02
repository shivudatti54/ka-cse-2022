# **Shared Memory**

### Definition

Shared memory is a region of memory shared by multiple processes. It allows processes to communicate and exchange data without the need for inter-process communication (IPC) mechanisms like pipes or sockets.

### Characteristics

- Multiple processes can access the same shared memory region simultaneously.
- Changes made to the shared memory are reflected in all processes that have access to it.
- Shared memory is more efficient than IPC mechanisms for large amounts of data transfer.

### Types of Shared Memory

- **System V Shared Memory**: This is the most widely used shared memory mechanism in Unix-like systems. It provides a set of system calls for creating, accessing, and deleting shared memory regions.
- **POSIX Shared Memory**: This is a standard for shared memory mechanisms that provides a set of APIs for creating, accessing, and deleting shared memory regions.

### Creation and Accessing Shared Memory

To create a shared memory region, you need to call the `shmat` system call, which maps the shared memory region to your process's address space. You can then access the shared memory region using the `mmap` system call.

```c
#include <sys/shm.h>
#include <sys/mman.h>

int main() {
    // Create a shared memory region
    int shm_fd = shmget(0, 1024, 0);
    if (shm_fd == -1) {
        perror("shmget");
        return 1;
    }

    // Map the shared memory region to your process's address space
    void* shm_addr = mmap(NULL, 1024, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    if (shm_addr == MAP_FAILED) {
        perror("mmap");
        return 1;
    }

    // Access the shared memory region
    char* data = (char*) shm_addr;
    *data = 'X';

    // Unmap the shared memory region
    munmap(shm_addr, 1024);

    // Delete the shared memory region
    shmctl(shm_fd, SHR_UNLINK, NULL);
    return 0;
}
```

### Shared Memory Example

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <sys/mman.h>

int main() {
    // Create a shared memory region
    int shm_fd = shmget(0, 1024, 0);
    if (shm_fd == -1) {
        perror("shmget");
        return 1;
    }

    // Map the shared memory region to your process's address space
    void* shm_addr = mmap(NULL, 1024, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    if (shm_addr == MAP_FAILED) {
        perror("mmap");
        return 1;
    }

    // Access the shared memory region
    char* data = (char*) shm_addr;
    *data = 'X';

    // Create another process
    pid_t pid = fork();
    if (pid == -1) {
        perror("fork");
        return 1;
    }

    if (pid == 0) {
        // Child process
        char* data = (char*) shm_addr;
        printf("Child process: %c\n", *data);
    } else {
        // Parent process
        while (1);
    }

    return 0;
}
```

# **Client-Server Properties**

### Definition

A client-server architecture is a design pattern where one process, the server, provides services to multiple processes, the clients. The server is responsible for managing the shared resources and providing services to the clients.

### Characteristics

- The server is responsible for managing the shared resources.
- The clients are responsible for connecting to the server and requesting services.
- The server provides services to multiple clients simultaneously.

### Types of Client-Server Architectures

- **Request-Response Architecture**: In this architecture, the client sends a request to the server, and the server responds with the result.
- **Publish-Subscribe Architecture**: In this architecture, the client subscribes to a service provided by the server, and the server notifies the client when the service is available.

### Client-Server Example

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

// Server code
int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    char buffer[1024] = {0};

    // Create a socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8080);

    // Bind the socket to the address and port
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    // Listen for incoming connections
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }

    printf("Server listening on port 8080...\n");

    while (1) {
        // Accept incoming connections
        if ((new_socket = accept(server_fd, (struct sockaddr*)&address, (socklen_t*)&addrlen)) < 0) {
            perror("accept");
            continue;
        }

        printf("Connection accepted...\n");

        // Receive data from the client
        read(new_socket, buffer, 1024);
        printf("Received message from client: %s\n", buffer);

        // Send response to the client
        char* message = "Hello from server!";
        send(new_socket, message, strlen(message), 0);

        // Close the connection
        close(new_socket);
    }

    return 0;
}
```

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

// Client code
int main() {
    int socket_fd;
    struct sockaddr_in server_addr;

    // Create a socket
    if ((socket_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);

    // Convert the server's IP address to binary format
    inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr);

    // Connect to the server
    if (connect(socket_fd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("connect");
        exit(EXIT_FAILURE);
    }

    printf("Connected to server...\n");

    // Send message to the server
    char* message = "Hello from client!";
    send(socket_fd, message, strlen(message), 0);

    // Receive response from the server
    char buffer[1024];
    read(socket_fd, buffer, 1024);
    printf("Received response from server: %s\n", buffer);

    // Close the connection
    close(socket_fd);
    return 0;
}
```

# **Passing File Descriptors**

### Definition

A file descriptor is a small integer used to refer to an open file. Passing file descriptors between processes allows them to share resources.

### Types of File Descriptors

- **Reading File Descriptors**: Used to read data from a file.
- **Writing File Descriptors**: Used to write data to a file.
- **Closing File Descriptors**: Used to close a file.

### Passing File Descriptors

To pass a file descriptor between processes, you can use the `pipe2` system call, which creates a pipe with the specified file descriptor.

```c
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int read_fd, write_fd;
    pid_t pid;

    // Create a pipe
    if (pipe2(0, O_CLOEXEC) == -1) {
        perror("pipe2");
        return 1;
    }

    // Create a new process
    pid = fork();
    if (pid == -1) {
        perror("fork");
        return 1;
    }

    if (pid == 0) {
        // Child process
        read_fd = 0;
        close(1);
        write(1, "Hello from child!", 15);
        close(read_fd);
    } else {
        // Parent process
        close(0);
        read_fd = 0;
        write(0, "Hello from parent!", 15);
        close(read_fd);
    }

    // Wait for the child process to finish
    wait(NULL);

    return 0;
}
```

# **An Open Server-Version 1**

### Definition

An open server is a server that accepts incoming connections and allows clients to send data to it. The open server version 1 is a specific implementation of this concept.

### Characteristics

- The server listens for incoming connections on a specified port.
- The server accepts incoming connections and allows clients to send data to it.
- The server provides services to multiple clients simultaneously.

### Open Server-Version 1 Example

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    char buffer[1024] = {0};

    // Create a socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_port = htons(8080);

    // Convert the server's IP address to binary format
    inet_pton(AF_INET, "127.0.0.1", &address.sin_addr);

    // Bind the socket to the address and port
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    // Listen for incoming connections
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }

    printf("Server listening on port 8080...\n");

    while (1) {
        // Accept incoming connections
        if ((new_socket = accept(server_fd, (struct sockaddr*)&address, (socklen_t*)&addrlen)) < 0) {
            perror("accept");
            continue;
        }

        printf("Connection accepted...\n");

        // Receive data from the client
        read(new_socket, buffer, 1024);
        printf("Received message from client: %s\n", buffer);

        // Send response to the client
        char* message = "Hello from server!";
        send(new_socket, message, strlen(message), 0);

        // Close the connection
        close(new_socket);
    }

    return 0;
}
```
