# File Transfer Protocol (FTP)

## Introduction

File Transfer Protocol (FTP) is a standard network protocol used for transferring files between a client and a server on a computer network. FTP is one of the oldest application layer protocols in the TCP/IP suite, first defined in 1971, and continues to be widely used today for file sharing and website management. FTP operates on a client-server architecture where the client initiates a connection to the server, authenticates itself, and then can upload or download files.

FTP is particularly important in the context of computer networks because it provides a reliable and efficient method for transferring large amounts of data. Unlike simple HTTP transfers, FTP maintains state throughout a session, allowing features like resume interrupted transfers, directory navigation, and user authentication. The protocol operates on TCP ports 20 and 21 by default, with port 21 used for control commands and port 20 used for data transfer. Understanding FTP is essential for network engineers, system administrators, and software developers as it forms the foundation for many modern cloud storage and file sharing services.

## Key Concepts

### FTP Architecture

FTP follows a client-server model with two distinct channels:

- **Control Channel (Port 21)**: Used for sending commands and receiving responses. This channel remains open throughout the FTP session.
- **Data Channel (Port 20)**: Used for actual file transfer. A new data channel is established for each file transfer operation.

The FTP protocol uses TCP for reliable transmission, ensuring that all data packets arrive correctly and in order.

### FTP Connection Modes

**Active Mode (PORT):**
In active mode, the client opens a random port and sends this port number to the server via the control channel. The server then initiates the data connection from port 20 to the client's specified port. This mode can cause issues with firewalls because the server initiates a connection back to the client, which may be blocked by firewall rules.

**Passive Mode (PASV):**
In passive mode, the client sends a PASV command to the server. The server responds with an IP address and port number. The client then initiates the data connection to this specified address. Passive mode is more firewall-friendly as all connections are initiated by the client.

### FTP Commands

FTP uses text-based commands sent over the control channel. Some important commands include:

- **USER**: Specifies the username for authentication
- **PASS**: Provides the password
- **LIST**: Lists files in the current directory
- **RETR**: Downloads a file from the server
- **STOR**: Uploads a file to the server
- **CWD**: Changes working directory
- **PWD**: Prints working directory
- **QUIT**: Terminates the FTP session

### FTP Responses

FTP servers send three-digit response codes:

- **1xx**: Positive preliminary reply (e.g., 150 - File status okay, about to open data connection)
- **2xx**: Positive completion reply (e.g., 226 - Transfer complete)
- **3xx**: Positive intermediate reply (e.g., 331 - User name okay, need password)
- **4xx**: Transient negative completion (e.g., 425 - Can't open data connection)
- **5xx**: Permanent negative completion (e.g., 530 - Not logged in)

### FTP Modes

**ASCII Mode:**
Used for transferring text files. The sender converts the file to ASCII format, and the receiver converts it back to the local character set. This mode handles end-of-line character conversions between different operating systems.

**Binary Mode (Image Mode):**
Used for transferring binary files such as images, executables, and compressed files. Data is transferred exactly as-is without any conversion, preserving the exact byte structure.

### Anonymous FTP

Anonymous FTP allows users to access public directories without providing specific credentials. Users typically log in using the username "anonymous" and their email address as the password. This feature is commonly used for distributing public software and documents.

### FTPS and SFTP

**FTPS (FTP over SSL/TLS):**
Adds encryption to FTP using SSL or TLS protocol. It can operate in explicit mode (using the AUTH TLS command) or implicit mode (establishing SSL connection immediately).

**SFTP (SSH File Transfer Protocol):**
A different protocol entirely, often confused with FTPS. SFTP runs over SSH (Secure Shell) and provides secure file transfer capabilities. It is not the same as FTP with encryption.

## Examples

### Example 1: FTP Session Walkthrough

**Problem:** Trace through a typical FTP session to download a file named "report.pdf" from a server.

**Solution:**

Step 1: Client establishes TCP connection to server port 21

```
Client: Connect to ftp.example.com:21
Server: 220 (ftp.example.com) FTP server ready
```

Step 2: User authentication

```
Client: USER john
Server: 331 User name okay, need password
Client: PASS secretpassword
Server: 230 User logged in
```

Step 3: Change to appropriate directory

```
Client: CWD /public/docs
Server: 250 CWD command successful
```

Step 4: Enter passive mode (client-friendly)

```
Client: PASV
Server: 227 Entering Passive Mode (203,0,113,50,117,45)
 (Server IP: 203.0.113.50, Port: 117*256+45 = 29997)
```

Step 5: Request file list

```
Client: LIST
Server: 150 Opening ASCII mode data connection
Server: -rw-r--r-- 1 user group 1024 Jan 15 10:00 report.pdf
Server: 226 Transfer complete
```

Step 6: Download the file

```
Client: RETR report.pdf
Server: 150 Opening BINARY mode data connection
[Data transfer of report.pdf occurs on port 29997]
Server: 226 Transfer complete
```

Step 7: Terminate session

```
Client: QUIT
Server: 221 Goodbye
```

### Example 2: FTP Mode Selection Problem

**Problem:** A user needs to transfer a 50MB ZIP file from a Windows server to a Linux client. Determine the appropriate FTP mode and justify your answer.

**Solution:**

The appropriate mode is **Binary Mode (Image Mode)**.

**Justification:**

1. ZIP files are binary files containing compressed data with specific byte patterns
2. ASCII mode would perform character conversions (like CR/LF to LF), corrupting binary data
3. Binary mode transfers the exact byte sequence without modification
4. This ensures file integrity - a single bit error would make the ZIP file unusable

**Commands to use:**

```
ftp> binary
200 Switching to Binary mode
ftp> get data.zip
200 PORT command successful
150 Opening BINARY mode data connection
226 Transfer complete
```

### Example 3: Troubleshooting FTP Connection

**Problem:** A client behind a corporate firewall cannot establish FTP data connections in active mode but can establish control connections. Explain why and provide a solution.

**Solution:**

**Root Cause:**
In active mode, the FTP client sends a PORT command with its IP and a random high port. The server then attempts to connect FROM port 20 TO the client's specified port. Corporate firewalls typically block these incoming connections for security reasons, preventing the data channel from being established.

**Solution - Use Passive Mode:**

```
Client: PASV
Server: 227 Entering Passive Mode (198.51.100.10, 2048)
```

In passive mode:

1. Client sends PASV command
2. Server responds with an IP and port for the client to connect to
3. Client initiates the OUTGOING data connection to the server
4. Firewall allows this as it's an outbound connection

The client should use the `passive` command or use an FTP client that defaults to passive mode.

## Exam Tips

1. **Remember FTP Port Numbers**: Port 21 for control channel, Port 20 for data channel (in active mode). This is a frequently asked question in exams.

2. **Active vs Passive Mode**: Active mode - client sends PORT, server connects back to client. Passive mode - client sends PASV, server provides address, client connects to server. Passive mode is firewall-friendly.

3. **FTP is Stateful**: Unlike HTTP, FTP maintains state throughout the session, allowing operations like rename, resume, and directory navigation.

4. **ASCII vs Binary Mode**: Use ASCII for text files (handles line ending conversions), Binary for all other files (images, executables, archives).

5. **FTP Responses**: Know the meaning of common response codes - 200 (command okay), 220 (service ready), 230 (user logged in), 226 (transfer complete), 530 (not logged in).

6. **Difference between FTPS and SFTP**: FTPS is FTP with SSL/TLS encryption, while SFTP is a completely different protocol running over SSH. Both provide security but are not the same.

7. **Anonymous FTP**: Allows access using username "anonymous" and email as password. Used for public file distribution.

8. **FTP Commands**: Remember at least 5-6 basic commands: USER, PASS, LIST, RETR, STOR, QUIT, CWD, PWD.

9. **FTP Uses TCP**: FTP uses TCP (connection-oriented) because it requires reliable, ordered delivery of data. UDP is not suitable for file transfer.

10. **Two-Channel Architecture**: Understand that FTP uses separate channels for control and data, which is different from protocols like HTTP that use a single channel.
