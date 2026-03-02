# **Daemon Processes: Revision Notes**

### Introduction

- **Definition:** A daemon process is a program that runs in the background, performing specific tasks without interacting with the user.
- **Purpose:** To automate tasks, provide services, and perform system maintenance.

### Daemon Characteristics

- **Background execution:** Runs in the background, not interacting with the user.
- **System resource usage:** Can consume system resources, such as CPU and memory.
- **File descriptor management:** Uses file descriptors to communicate with the operating system.

### Coding Rules

- **Use `fork` and `exec` for daemonization**
- **Close unnecessary file descriptors**
- **Use `setsid` to gain process group ID**
- **Use `chdir` to change working directory**
- **Use `umask` to set file mode creation mask**

### Error Logging

- **Use `log` and `logrotate` for error logging**
- **Log errors to a file or console**
- **Log error messages with date, time, and process ID**

### Client-Server Model

- **Definition:** A client-server model is a communication pattern where a client requests services from a server.
- **Components:**
  - **Client:** Requests services from the server.
  - **Server:** Provides services to the client.
  - **Network:** Enables communication between the client and server.
- **Protocols:** TCP/IP, UDP, HTTP, FTP, etc.

**Important Formulas and Definitions**

- **Process ID (PID):** A unique identifier for a process.
- **User ID (UID):** A unique identifier for a user.
- **Group ID (GID):** A unique identifier for a group.
- **File descriptor (FD):** A small, non-negative integer used to identify a file or socket.

**Key Theorems**

- **First-In-First-Out (FIFO) theory:** Describes the order of file descriptor allocation.
- **Operating System (OS) theory:** Describes the behavior of the operating system.
