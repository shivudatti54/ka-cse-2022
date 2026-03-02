# Transport Layer Features - Summary

## Key Definitions and Concepts

- **Multiplexing/Demultiplexing**: Using port numbers to direct data to correct application processes
- **Socket**: Combination of IP address and port number identifying a unique endpoint
- **Socket Pair**: Four-tuple (source IP, source port, destination IP, destination port) identifying a TCP connection
- **Sliding Window Protocol**: Mechanism enabling multiple segments in transit while controlling data rate
- **Congestion Window (cwnd)**: Sender-side limit on unacknowledged data based on network capacity
- **Receive Window (rwnd)**: Receiver-advertised limit preventing buffer overflow

## Important Formulas and Theorems

- **Maximum Port Range**: 0 to 65535 (65,536 ports)
- **Well-Known Ports**: 0-1023 (reserved for standard services)
- **Throughput Formula**: Throughput = Window Size / RTT
- **Slow Start**: cwnd doubles every RTT until ssthresh
- **Congestion Avoidance**: cwnd increases by 1 MSS per RTT
- **Timeout Recovery**: cwnd resets to 1 MSS, ssthresh = cwnd/2
- **Fast Recovery**: cwnd = ssthresh + 3×MSS after duplicate ACKs

## Key Points

1. TCP provides reliable, connection-oriented service with error recovery, flow control, and congestion control; UDP provides unreliable, connectionless service with minimal overhead.

2. Port numbers enable multiple applications to share network resources through multiplexing and demultiplexing.

3. Three-way handshake (SYN, SYN-ACK, ACK) establishes TCP connections; four-way handshake (FIN, ACK, FIN, ACK) terminates connections.

4. Flow control prevents receiver buffer overflow using the advertised window mechanism.

5. TCP congestion control includes Slow Start, Congestion Avoidance, Fast Retransmit, and Fast Recovery phases.

6. Sequence numbers ensure ordered delivery and enable detection of lost segments.

7. ACKs confirm receipt of data; cumulative ACKs acknowledge all bytes up to a point; SACK provides selective acknowledgment.

8. Transport Layer features determine application performance characteristics and suitability for different network conditions.

## Common Mistakes to Avoid

1. Confusing flow control with congestion control: Flow control protects the receiver; congestion control protects the network.

2. Thinking UDP provides no error detection: UDP has optional checksum coverage, but no error recovery.

3. Believing sequence numbers represent segment numbers: Sequence numbers represent byte positions in the data stream.

4. Forgetting that TCP is byte-oriented, not segment-oriented: The cwnd is measured in bytes, not segments.

5. Assuming larger window sizes always improve performance: Excessively large windows can cause buffer exhaustion and increased latency.

## Revision Tips

1. Draw and label the TCP header to memorize all fields and their sizes.

2. Practice tracing TCP three-way handshakes and data transfer sequences.

3. Solve numerical problems on congestion window growth over multiple RTTs.

4. Create comparison tables between TCP and UDP features.

5. Review past DU examination questions on Transport Layer features.