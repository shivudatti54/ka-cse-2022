# **Client-Server Program Summary**

### Overview

- A client-server program is designed to allow a client to request a file from a server and receive its contents.
- The client sends the file name to the server, which checks if the file exists and, if so, sends its contents back to the client.

### Key Points

- **Client Responsibilities:**
  - Send file name to server
  - Receive file contents from server
- **Server Responsibilities:**
  - Store files
  - Check if requested file exists
  - Send file contents to client if present
- **Network Concepts:**
  - Sockets (for establishing communication between client and server)
  - Addresses (IP addresses and port numbers for identifying clients and servers)

### Important Formulas and Definitions

- **Socket Programming:** Using sockets to establish communication between client and server.
- **Transmission Control Protocol (TCP):** Ensures reliable data transfer between client and server.
- **File Transfer Protocol (FTP):** A protocol for transferring files between clients and servers.

### Theorems and Principles

- **Client-Server Model:** A model where a client requests services from a server, which provides the requested services.
- **Stateless vs. Stateful Servers:** A stateless server does not maintain any information about the client, while a stateful server maintains information about the client.

### Quick Revision Notes

- Client sends file name to server
- Server checks if file exists and sends contents if present
- Use sockets for communication between client and server
- TCP and FTP protocols used for reliable data transfer
