# Client-Server Program for File Sharing

=====================================

### Requirements

- Maximum 1 page
- Key points only in bullet format
- Important formulas, definitions, theorems included
- Perfect for quick revision before exams

### Overview

The client-server program allows the client to send the file name to the server, and then the server sends back the contents of the requested file if present.

### Key Points

- **Client-Server Architecture**
  - Client initiates connection with server
  - Client sends file name to server
  - Server checks if file exists and sends its contents to client
- **Sockets**
  - Used for establishing communication between client and server
  - Enable bidirectional, connection-oriented communication
- **TCP (Transmission Control Protocol)**
  - Ensures reliable data transfer between client and server
  - Guarantees delivery, ordering, and error checking of packets

### Important Formulas, Definitions, Theorems

- **UDP (User Datagram Protocol)**
  - Used for connectionless communication
  - Ensures fast data transfer but lacks reliability
- **Socket Programming**
  - Uses socket addresses (IP address and port number) to identify communication endpoints
  - Enables communication between processes or threads

### Example Use Case

- Client sends file name (e.g., "document.txt") to server
- Server checks if file exists and sends its contents to client
- Client receives file contents and displays it

### Key Concepts

- **File Sharing**
  - Enables multiple users to access and share files over a network
  - Can be implemented using client-server architecture
- **Network Protocols**
  - TCP/IP (Transmission Control Protocol/Internet Protocol) is the most commonly used protocol suite
  - Other protocols include UDP, ICMP, and IGMP
