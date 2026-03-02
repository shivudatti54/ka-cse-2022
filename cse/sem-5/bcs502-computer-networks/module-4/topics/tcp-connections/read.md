# TCP Connections

## Introduction

TCP (Transmission Control Protocol) is one of the core protocols of the Internet protocol suite, operating at the transport layer of the OSI model. Unlike UDP (User Datagram Protocol), which is connectionless and unreliable, TCP provides a reliable, ordered, and error-checked delivery of data between applications running on different hosts. The foundation of TCP's reliability lies in its connection-oriented nature, where a logical connection must be established before any data transfer occurs.

TCP connections are fundamental to modern networking, enabling applications ranging from web browsing (HTTP/HTTPS) to email transfer (SMTP, POP3, IMAP) and file transfers (FTP). The connection-oriented approach ensures that data packets arrive in the correct order and without errors, making TCP the preferred protocol for applications requiring guaranteed delivery. Understanding TCP connections is essential for computer science engineers, as it forms the backbone of client-server communication and is a critical topic in 's computer networks curriculum.

The beauty of TCP lies in its elegant mechanism for establishing and terminating connections through a process called the three-way handshake and four-way handshake respectively. These mechanisms ensure that both endpoints are ready to communicate and have agreed on initial sequence numbers, preventing stale or duplicate connections from causing issues.

## Key Concepts

### TCP Header Structure

Before understanding TCP connections, it's crucial to know the TCP header format. A TCP header consists of the following fields:

- **Source Port (16 bits)**: Port number of the sender
- **Destination Port (16 bits)**: Port number of the receiver
- **Sequence Number (32 bits)**: Sequence number of the first data byte
- **Acknowledgment Number (32 bits)**: Next expected sequence number
- **Data Offset (4 bits)**: Length of TCP header
- **Reserved (6 bits)**: Reserved for future use
- **Control Flags (6 bits)**: URG, ACK, PSH, RST, SYN, FIN
- **Window Size (16 bits)**: Receive window size
- **Checksum (16 bits)**: Error checking
- **Urgent Pointer (16 bits)**: Points to urgent data
- **Options (Variable)**: Optional fields like MSS, window scaling

### Three-Way Handshake (Connection Establishment)

The three-way handshake is the process by which TCP establishes a connection between a client and server. This mechanism ensures both parties are ready and agree on initial parameters.

**Step 1: SYN (Synchronize)**
The client sends a TCP segment with the SYN flag set to the server. This segment contains an initial sequence number (ISN) that the client will use for data transmission. The sequence number is random for security reasons to prevent TCP hijacking attacks. The client enters the SYN_SENT state.

**Step 2: SYN-ACK (Synchronize-Acknowledge)**
The serverSYN segment, responds with a segment having both SYN and ACK flags set. The server's segment contains its own initial sequence number (ISN) and acknowledges the client's ISN by setting the acknowledgment number to client_ISN + 1. The server enters the SYN_RCVD state.

**Step 3: ACK (Acknowledge)**
The client receives the SYN-ACK segment, sends an ACK segment back to the server with acknowledgment number set to server_ISN + 1. Both client and server now enter the ESTABLISHED state, meaning the connection is open and ready for data transfer.

### Four-Way Handshake (Connection Termination)

TCP connections are terminated gracefully using a four-way handshake, ensuring all data is transmitted before closing.

**Step 1: FIN (Finish)**
The application calls close function. The initiating end sends a TCP segment with FIN flag set, indicating it has no more data to send. It enters the FIN_WAIT_1 state.

**Step 2: ACK**
The receiving end acknowledges the FIN segment by sending an ACK with acknowledgment number equal to received sequence number + 1. It enters the CLOSE_WAIT state. The initiating end receives this ACK and enters FIN_WAIT_2 state.

**Step 3: FIN**
When the receiving application also closes, it sends a FIN segment to the initiator. The receiving end enters the LAST_ACK state.

**Step 4: ACK**
The initiator receives the FIN, sends an ACK, and enters the TIME_WAIT state. After waiting for 2MSL (Maximum Segment Lifetime), it closes the connection. The receiving end enters the CLOSED state upon receiving this final ACK.

### TCP States

TCP connections exist in various states throughout their lifecycle:

- **LISTEN**: Server waiting for client connection request
- **SYN_SENT**: Client waiting for matching connection request
- **SYN_RCVD**: Server waiting for acknowledgment after sending acknowledgment
- **ESTABLISHED**: Open connection, data transfer in progress
- **FIN_WAIT_1**: Waiting for connection termination request
- **FIN_WAIT_2**: Waiting for connection termination request from remote end
- **CLOSE_WAIT**: Waiting for connection termination request from local user
- **LAST_ACK**: Waiting for final acknowledgment
- **TIME_WAIT**: Waiting for enough time to pass to ensure remote end received acknowledgment
- **CLOSED**: No connection state

### Socket Programming

In Unix-like systems, TCP connections are established using sockets. The basic workflow involves:

**Server Side:**

1. Create socket using socket
2. Bind socket to address using bind
3. Listen for connections using listen
4. Accept connection using accept
5. Communicate using send/recv
6. Close socket using close

**Client Side:**

1. Create socket using socket
2. Connect to server using connect
3. Communicate using send/recv
4. Close socket using close

### Connection Parameters and Options

TCP supports various connection options negotiated during the three-way handshake:

- **Maximum Segment Size (MSS)**: Maximum size of TCP payload
- **Window Scaling**: Increases receive window size beyond 65,535 bytes
- **Selective Acknowledgment (SACK)**: Allows acknowledging non-contiguous data blocks
- **Timestamps**: Used for RTT estimation and PAWS (Protection Against Wrapped Sequence Numbers)

## Examples

### Example 1: Tracing a Three-Way Handshake

Consider a client with IP 192.168.1.100 connecting to a web server at 192.168.1.200 on port 80.

**Step 1: Client sends SYN**

```
Source: 192.168.1.100:5000 → Dest: 192.168.1.200:80
SEQ = 1000, ACK = 0, Flags: SYN
```

**Step 2: Server sends SYN-ACK**

```
Source: 192.168.1.200:80 → Dest: 192.168.1.100:5000
SEQ = 2000, ACK = 1001, Flags: SYN, ACK
```

**Step 3: Client sends ACK**

```
Source: 192.168.1.100:5000 → Dest: 192.168.1.200:80
SEQ = 1001, ACK = 2001, Flags: ACK
```

After this handshake, the connection is established. The client will send HTTP request starting with SEQ=1001, and the server will start its response with SEQ=2001.

### Example 2: Server Socket Programming

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main {
 int server_socket, client_socket;
 struct sockaddr_in server_addr, client_addr;
 socklen_t client_len;
 char buffer[1024];

 // Step 1: Create socket
 server_socket = socket(AF_INET, SOCK_STREAM, 0);

 // Step 2: Configure server address
 memset(&server_addr, 0, sizeof(server_addr));
 server_addr.sin_family = AF_INET;
 server_addr.sin_addr.s_addr = INADDR_ANY;
 server_addr.sin_port = htons(8080);

 // Step 3: Bind socket
 bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr));

 // Step 4: Listen for connections
 listen(server_socket, 5);
 printf("Server listening on port 8080...\n");

 // Step 5: Accept connection
 client_len = sizeof(client_addr);
 client_socket = accept(server_socket, (struct sockaddr*)&client_addr, &client_len);
 printf("Client connected\n");

 // Step 6: Receive data
 memset(buffer, 0, sizeof(buffer));
 read(client_socket, buffer, sizeof(buffer));
 printf("Received: %s\n", buffer);

 // Step 7: Send response
 char response[] = "Hello from server";
 write(client_socket, response, strlen(response));

 // Step 8: Close sockets
 close(client_socket);
 close(server_socket);

 return 0;
}
```

### Example 3: Client Socket Programming

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main {
 int client_socket;
 struct sockaddr_in server_addr;
 char buffer[1024];

 // Step 1: Create socket
 client_socket = socket(AF_INET, SOCK_STREAM, 0);

 // Step 2: Configure server address
 memset(&server_addr, 0, sizeof(server_addr));
 server_addr.sin_family = AF_INET;
 server_addr.sin_port = htons(8080);
 inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr);

 // Step 3: Connect to server
 connect(client_socket, (struct sockaddr*)&server_addr, sizeof(server_addr));
 printf("Connected to server\n");

 // Step 4: Send data
 char message[] = "Hello from client";
 write(client_socket, message, strlen(message));

 // Step 5: Receive response
 memset(buffer, 0, sizeof(buffer));
 read(client_socket, buffer, sizeof(buffer));
 printf("Server says: %s\n", buffer);

 // Step 6: Close socket
 close(client_socket);

 return 0;
}
```

## Exam Tips

1. **Remember the exact sequence of three-way handshake**: SYN → SYN-ACK → ACK. This is frequently asked in exams.

2. **Know all TCP flags**: URG, ACK, PSH, RST, SYN, FIN - remember their purposes and when each is used.

3. **Understand TIME_WAIT state**: After receiving FIN-ACK, the initiator waits for 2MSL (Maximum Segment Lifetime) to ensure the final ACK reaches the other end.

4. **Difference between socket and port**: A socket is the combination of IP address and port number (e.g., 192.168.1.100:5000), while a port is just a 16-bit number.

5. **SYN flood attack**: Understand how attackers exploit the three-way handshake by sending multiple SYN packets without completing the handshake.

6. **Sequence and Acknowledgment numbers**: Remember that ACK number always indicates the next expected byte, not the last received byte.

7. **Connection vs Connectionless**: TCP is connection-oriented (requires handshake), UDP is connectionless (no handshake required).

8. **State transitions**: Be familiar with the state transition diagram, especially ESTABLISHED, LISTEN, SYN_SENT, SYN_RCVD, FIN_WAIT, CLOSE_WAIT.

9. **MSS negotiation**: Maximum Segment Size is typically 1460 bytes for Ethernet (1500 - 20 IP header - 20 TCP header).

10. **Well-known ports**: Remember common ports - HTTP (80), HTTPS (443), FTP (21), SSH (22), Telnet (23), SMTP (25).
