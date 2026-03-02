# Features of the Transport Layer

## Introduction

The Transport Layer is the fourth layer in the OSI (Open Systems Interconnection) model and serves as the bridge between the application layer and the network layer. It is responsible for end-to-end communication services, ensuring that data is transferred reliably or unreliably between applications running on different hosts. Understanding the features of the Transport Layer is crucial for network engineers and software developers, as these features determine how applications communicate across networks.

The Transport Layer provides several critical services that are essential for modern networking. These services include process-to-process communication, multiplexing and demultiplexing, congestion control, flow control, and error control. The two primary protocols operating at this layer are the User Datagram Protocol (UDP), which provides a connectionless and unreliable service, and the Transmission Control Protocol (TCP), which offers a connection-oriented and reliable service. Each protocol has its own set of features tailored to different application requirements.

In the context of the University of Delhi's Computer Science curriculum, a thorough understanding of Transport Layer features is essential for both theoretical examinations and practical networking implementations. The features discussed here form the foundation for understanding how reliable data transfer is achieved over unreliable networks, a fundamental concept in computer networking.

## Key Concepts

### Multiplexing and Demultiplexing

Multiplexing at the Transport Layer allows multiple applications on a single host to use network services simultaneously. This is achieved through port numbers, which serve as unique identifiers for each application process. The Transport Layer uses source and destination port numbers to direct incoming data to the correct application process. There are 65,536 ports available (ranging from 0 to 65535), with well-known ports (0-1023) reserved for standard services like HTTP (port 80), HTTPS (port 443), and FTP (port 21).

Demultiplexing is the reverse process, where the Transport Layer receives segments from the network layer and delivers them to the appropriate socket based on the destination port number. This mechanism enables multiple applications to communicate concurrently over a single network connection, making efficient use of available resources.

### Connection-Oriented and Connectionless Services

The Transport Layer offers two fundamentally different types of service. Connection-oriented service, implemented by TCP, requires establishing a connection before data transfer begins. This connection involves a three-way handshake (SYN, SYN-ACK, ACK) to establish parameters and ensure both endpoints are ready for communication. The connection remains active until explicitly terminated through a four-way handshake (FIN, ACK, FIN, ACK).

Connectionless service, provided by UDP, does not require any connection establishment or termination. Each datagram is treated independently, with no overhead for maintaining connection state. This approach reduces latency but provides no guarantees about delivery, ordering, or error-free transmission.

### Flow Control

Flow control is a mechanism that prevents the sender from overwhelming the receiver with data faster than it can process. TCP implements flow control using a sliding window mechanism and the Receive Window (rwnd) field in the TCP header. The receiver advertises its available buffer space in the rwnd field, and the sender ensures that the amount of unacknowledged data never exceeds this window size.

The sliding window protocol allows for efficient data transfer by enabling multiple segments to be in flight simultaneously while maintaining control over the data rate. This prevents buffer overflow at the receiver and ensures data integrity.

### Error Control

Error control in the Transport Layer ensures reliable data delivery through error detection and recovery mechanisms. TCP employs checksums for error detection, sequence numbers for ordering, and acknowledgments (ACKs) for reliable delivery. When segments arrive with errors or are lost, TCP implements retransmission mechanisms to recover the lost data.

The acknowledgment scheme in TCP can be cumulative (acknowledging all bytes up to a certain sequence number) or selective (acknowledging specific blocks of data). Selective Acknowledgments (SACK) allow the receiver to specify non-contiguous blocks of data that have been received, improving retransmission efficiency.

### Congestion Control

Congestion control is perhaps the most important feature of the Transport Layer in modern networks. It prevents network collapse by regulating the rate at which senders transmit data based on network conditions. TCP implements several congestion control algorithms:

The Slow Start algorithm begins with a congestion window (cwnd) of one maximum segment size (MSS) and exponentially increases the window size for each successful acknowledgment, until a loss event occurs or the slow start threshold is reached.

The Congestion Avoidance algorithm increases the congestion window linearly, assuming the network is operating close to its capacity. This gradual increase helps stabilize the data transfer rate.

Fast Retransmit and Fast Recovery are mechanisms that allow TCP to recover from packet loss more quickly. When multiple duplicate ACKs are received (indicating out-of-order segments), TCP assumes packet loss and immediately retransmits the missing segment without waiting for a timeout.

### Reliability

TCP provides reliable data transfer through a combination of sequence numbers, acknowledgments, and retransmissions. Each byte of data is numbered, allowing the receiver to detect missing segments and reorder them correctly. Acknowledgments confirm successful receipt of data, and unacknowledged data is retransmitted after timeout periods.

The reliability mechanisms in TCP ensure that data delivered to the application layer is error-free, in sequence, and without duplicates. This makes TCP suitable for applications requiring guaranteed delivery, such as file transfer, email, and web browsing.

### Port Numbers and Socket Pairs

A socket is defined by the combination of IP address and port number, representing a unique endpoint in a network. TCP connections are established between two sockets, identified by the four-tuple: (source IP, source port, destination IP, destination port). This socket pair uniquely identifies each connection, allowing multiple simultaneous connections between the same hosts.

Well-known ports are assigned to specific services, while registered ports (1024-49151) can be used by user applications. Ephemeral or dynamic ports (49152-65535) are typically assigned by the operating system to client-side connections.

## Examples

### Example 1: Understanding TCP Three-Way Handshake

Consider a client application on host A (IP: 192.168.1.10) connecting to a web server on host B (IP: 192.168.1.100) on port 80.

Step 1: Client sends SYN segment with sequence number x. The SYN flag is set, indicating a connection request.
Step 2: Server receives SYN, allocates resources, and responds with SYN+ACK. The acknowledgment number is x+1, and the server chooses its own initial sequence number y.
Step 3: Client receives SYN+ACK, allocates resources, and sends ACK to server. The acknowledgment number is y+1, confirming the server's initial sequence number.

After this exchange, both parties have confirmed each other's ability to receive data, and the connection is established. The three-way handshake prevents old duplicate connections from being accepted.

### Example 2: TCP Flow Control in Action

Suppose a receiver has a receive buffer of 16 KB and has acknowledged receipt of bytes up to sequence number 1000, advertising a receive window (rwnd) of 8000 bytes. If the sender has already sent 2000 bytes (sequence numbers 1001-3000), the amount of data it can send without waiting for further acknowledgments is:

Maximum send window = rwnd - (last byte sent - last byte acknowledged)
= 8000 - (3000 - 1000) = 8000 - 2000 = 6000 bytes

This calculation ensures the sender does not overflow the receiver's buffer. As the receiver processes data and frees buffer space, it sends updated window advertisements to allow more data transmission.

### Example 3: Congestion Control Phases

Consider a TCP connection starting with cwnd = 1 MSS and ssthresh = 64 KB:

Phase 1 - Slow Start: cwnd doubles every RTT (Round Trip Time). After 1 RTT: 2 MSS, after 2 RTTs: 4 MSS, after 3 RTTs: 8 MSS. This exponential growth continues until cwnd reaches ssthresh (64 KB) or packet loss occurs.

Phase 2 - Congestion Avoidance: Once cwnd reaches ssthresh, the growth becomes linear. cwnd increases by 1 MSS per RTT. For example, from 64 KB to approximately 65 KB after one RTT.

Phase 3 - Loss Detection: If three duplicate ACKs are received, TCP performs fast retransmit and sets ssthresh to cwnd/2, then sets cwnd to ssthresh plus 3 MSS (accounting for the three duplicate ACKs). This is the fast recovery phase.

Phase 4 - Timeout: If a timeout occurs (more severe congestion), TCP sets ssthresh to cwnd/2 and cwnd to 1 MSS, returning to slow start phase.

## Exam Tips

1. Understand the difference between TCP and UDP clearly: TCP is connection-oriented, reliable, provides flow and congestion control; UDP is connectionless, unreliable, and provides minimal overhead.

2. Remember the TCP header fields: Source Port, Destination Port, Sequence Number, Acknowledgment Number, Data Offset, Flags (URG, ACK, PSH, RST, SYN, FIN), Window Size, Checksum, Urgent Pointer.

3. Know the three-way handshake steps (SYN, SYN-ACK, ACK) and four-way termination handshake (FIN, ACK, FIN, ACK).

4. Be able to explain each congestion control algorithm: Slow Start, Congestion Avoidance, Fast Retransmit, and Fast Recovery.

5. Understand how sliding window protocol works for flow control and the significance of the receive window (rwnd) field.

6. Remember that port numbers range from 0 to 65535, with well-known ports (0-1023) reserved for standard services.

7. Know the difference between error detection (checksums) and error correction (retransmission) in TCP.

8. Be prepared to calculate practical values: maximum segment size, throughput based on window size and RTT, and timeout values.

9. Understand the concept of socket pairs and how they uniquely identify TCP connections.

10. Know when to use UDP versus TCP: UDP for real-time applications (VoIP, video streaming) where speed is critical and some packet loss is acceptable; TCP for applications requiring reliable delivery (HTTP, FTP, email).