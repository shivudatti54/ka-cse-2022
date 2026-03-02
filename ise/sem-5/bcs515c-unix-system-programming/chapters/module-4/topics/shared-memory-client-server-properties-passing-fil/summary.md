# **Shared Memory, Client-Server Properties, Passing File Descriptors, An Open Server-Version 1**

### Shared Memory

- **Definition:** A region of memory that can be shared between multiple processes.
- **Create:** `IPC_CREAT` flag with `shmdt` system call.
- **Destroy:** `shmdt` system call with `IPC_UNLINK` flag.

### Client-Server Properties

- **Definition:** A model where one process (server) provides services to multiple processes (clients).
- **Key Characteristics:**
  - Server waits for client requests.
  - Clients send requests to the server.
  - Server responds to client requests.

### Passing File Descriptors

- **Definition:** A technique to pass files between processes.
- **Methods:**
  - **pipe()**: Creates a pipe, which is a unidirectional channel for data exchange.
  - **socket()**: Creates a socket, which is a bidirectional channel for data exchange.

### An Open Server-Version 1

- **Definition:** A server process that listens for incoming connections.
- **Key Components:**
  - **Listen()**: Listens for incoming connections on a specified port.
  - **Accept()**: Accepts an incoming connection and creates a new process.
  - **Handle()**: Handles the incoming request.

**Important Formulas and Definitions**

- **Process Identifiers (PID):** A unique identifier for a process.
- **Process Status:** A description of the status of a process (e.g., running, sleeping, zombie).
- **System Calls:** Functions that interact with the operating system (e.g., `fork()`, `pipe()`).

**Theorems**

- **Theorem:** If two processes are connected through a pipe, then data can be sent from one process to the other through the pipe.
- **Theorem:** If a process sends data to a server through a socket, then the server can receive the data.
