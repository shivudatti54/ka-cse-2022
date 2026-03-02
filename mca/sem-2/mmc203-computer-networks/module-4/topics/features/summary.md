# Features of Transmission Control Protocol (TCP) - Summary

## Key Definitions

- **Transmission Control Protocol (TCP)**: A connection-oriented transport layer protocol providing reliable, ordered, error-checked delivery of data between applications over IP networks.

- **Sequence Number**: A 32-bit field in the TCP header identifying the position of the first data byte in a segment within the byte stream.

- **Acknowledgment Number**: A 32-bit field indicating the next expected sequence number, confirming receipt of all prior bytes.

- **Congestion Window (cwnd)**: A TCP variable limiting the amount of unacknowledged data the sender can transmit, controlling network load.

- **Advertised Window (rwnd)**: The receive buffer space advertised by the receiver, controlling flow to prevent buffer overflow.

- **Socket**: The combination of an IP address and port number identifying a unique endpoint for TCP communication.

## Important Formulas

- **Effective Window**: min(cwnd, rwnd) - The actual amount of data that can be sent without waiting for acknowledgments.

- **Slow Start Threshold (ssthresh)**: Typically set to half the congestion window when packet loss occurs, determining the transition from exponential to linear growth.

- **Sequence Space**: TCP uses a 32-bit sequence number space that wraps around (modulo 2³²) for very long connections.

## Key Points

1. TCP is connection-oriented, establishing virtual connections through the three-way handshake (SYN, SYN-ACK, ACK) before data transfer.

2. Reliability is achieved through sequence numbers, cumulative acknowledgments, checksums, and automatic retransmission of unacknowledged segments.

3. Flow control uses a sliding window protocol where the receiver advertises available buffer space to prevent overwhelming the sender.

4. Congestion control involves slow start (exponential cwnd growth), congestion avoidance (linear cwnd growth), and loss recovery algorithms.

5. TCP supports full-duplex communication, allowing simultaneous bidirectional data transfer with independent sequence spaces.

6. The TCP header is 20-60 bytes containing source/destination ports, sequence/acknowledgment numbers, flags, window size, checksum, and options.

7. TCP provides byte-stream service, treating data as an unstructured stream rather than discrete messages, with no inherent message boundaries.

8. Port numbers (16-bit) distinguish multiple connections on a single host, with well-known ports (0-1023) reserved for privileged services.

9. The four-way handshake (FIN, ACK, FIN, ACK) gracefully terminates TCP connections, ensuring all data is delivered before closure.

10. Modern TCP includes optimizations like selective acknowledgments (SACK), window scaling, and timestamps for improved performance.

## Common Mistakes

1. **Confusing flow control with congestion control**: Flow control manages receiver buffer space (rwnd), while congestion control manages network load (cwnd).

2. **Misunderstanding sequence numbers**: TCP sequence numbers represent byte positions, not segment counts, and start at random initial values.

3. **Assuming message boundaries**: TCP is a byte-stream protocol; a single send() might result in multiple segments, and a single recv() might receive data from multiple segments.

4. **Ignoring the three-way handshake purpose**: The handshake synchronizes sequence numbers, negotiates options, and prevents old duplicate segments from being accepted as valid.