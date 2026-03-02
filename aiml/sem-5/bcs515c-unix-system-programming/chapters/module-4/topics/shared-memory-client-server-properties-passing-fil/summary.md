# **Shared Memory, Client-Server Properties, Passing File Descriptors, An Open Server-Version 1**

## **Key Concepts**

- **Shared Memory**
  - Definition: A region of memory shared by multiple processes.
  - Creation: `shm_open()`, `shm_unlink()`
  - Functions: `shm_getaddrinfo()`, `shm_setvaddr()`, `shm_unlink()`
  - Example: Using shared memory for inter-process communication.

- **Client-Server Properties**
  - Definition: A client-server architecture where one process acts as a server and others as clients.
  - Characteristics: Asynchronous communication, request-response model.
  - Example: A web server and its clients.

- **Passing File Descriptors**
  - Definition: File descriptors are integers that represent open files.
  - Passing file descriptors through pipes, sockets, or shared memory.
  - Example: Using pipes for inter-process communication.

- **An Open Server-Version 1**
  - Definition: A basic server implementation using `listen()`, `accept()`, and `fork()`.
  - Functions: `listen()`, `accept()`, `fork()`, `close()`
  - Example: A simple TCP server using sockets.

## **Important Formulas and Definitions**

- **Process Identifier (PID)**: Unique identifier for a process.
- **Process Status**: The state of a process, including running, waiting, zombie, etc.
- **System V IPC (Inter-Process Communication)**: A set of functions for inter-process communication.
- **Socket Options**: A set of options used to configure sockets.

## **Theorems and Key Points**

- Theorem 1: **Inter-Process Communication (IPC)**: The ability of processes to communicate with each other.
- Key Point: Shared memory is faster than pipes or sockets for large data transfers.
- Key Point: A client-server architecture is suitable for large-scale applications.
