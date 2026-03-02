# TCP Connections - Summary

## Key Definitions and Concepts

- **TCP (Transmission Control Protocol)**: A connection-oriented, reliable transport layer protocol that ensures ordered, error-free delivery of data between applications.

- **Socket**: A combination of IP address and port number (e.g., 192.168.1.100:8080) that uniquely identifies one end of a TCP connection.

- **Three-Way Handshake**: The process of establishing a TCP connection through SYN, SYN-ACK, and ACK segments.

- **Four-Way Handshake**: The process of gracefully terminating a TCP connection through FIN, ACK, FIN, ACK exchanges.

- **Sequence Number**: A 32-bit number identifying each byte of data in a TCP stream for ordering and reliability.

- **Acknowledgment Number**: Indicates the next expected sequence number from the receiver, confirming successful receipt of all prior bytes.

## Important Formulas and Theorems

- **ACK Number**: ACK = Last received sequence number + 1
- **Window Size**: Maximum data that can be sent without acknowledgment (default max: 65,535 bytes, up to 1GB with window scaling)
- **MSS (Maximum Segment Size)**: Typically 1460 bytes for Ethernet (1500 - 20 IP header - 20 TCP header)
- **TIME_WAIT Duration**: 2 × MSL (Maximum Segment Life), typically 2-4 minutes

## Key Points

- TCP provides reliable, ordered, and error-checked data delivery through acknowledgments and retransmissions.

- The three-way handshake prevents stale connections and synchronizes initial sequence numbers (ISN) between endpoints.

- TCP flags control connection behavior: SYN for connection establishment, FIN for graceful termination, RST for abrupt reset, ACK for acknowledgments.

- The server uses listen() to queue incoming connections and accept() to retrieve established connections from the queue.

- Client connects using connect(), which initiates the three-way handshake with the server.

- TIME_WAIT state exists to ensure delayed segments are properly handled and the final ACK reaches the destination.

- Well-known ports: HTTP (80), HTTPS (443), SSH (22), FTP (21), SMTP (25).

- TCP is connection-oriented (requires handshake), while UDP is connectionless (no handshake required).

## Common Mistakes to Avoid

1. **Confusing ACK and sequence numbers**: ACK number = next expected byte, not the last received byte.

2. **Forgetting port numbers**: Both source and destination ports are essential for socket identification.

3. **Mixing up three-way and four-way handshakes**: Remember three-way is for connection establishment, four-way for termination.

4. **Ignoring network byte order**: Always use htons() and htonl() for port and IP conversion in socket programming.

## Revision Tips

1. Draw the three-way and four-way handshakes on paper, labeling each step with sequence numbers and flags.

2. Practice writing simple client-server socket programs in C - this is frequently asked in lab exams.

3. Memorize the TCP header fields and their bit lengths for direct questions.

4. Use network analysis tools like Wireshark to observe real TCP connections and correlate with theory.

5. Focus on state transitions - especially ESTABLISHED, LISTEN, SYN_SENT, FIN_WAIT states.
