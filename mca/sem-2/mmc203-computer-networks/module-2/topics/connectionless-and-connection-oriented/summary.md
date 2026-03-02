# Connectionless and Connection-Oriented Services - Summary

## Key Definitions and Concepts

- **Connectionless Communication**: A communication paradigm where data packets (datagrams) are sent without establishing a dedicated connection beforehand. Each packet is independent and contains complete addressing information.

- **Connection-Oriented Communication**: A communication paradigm requiring a formal connection establishment (handshake) before data transfer begins, providing reliable and ordered delivery.

- **UDP (User Datagram Protocol)**: A connectionless transport layer protocol offering minimal overhead (8-byte header) with no reliability guarantees, ordering, or flow control.

- **TCP (Transmission Control Protocol)**: A connection-oriented transport layer protocol providing reliable, ordered, full-duplex communication with flow and congestion control mechanisms.

## Important Formulas and Theorems

- **UDP Datagram Size**: Minimum 8 bytes (header only), maximum 65,535 bytes
- **TCP Segment Size**: Minimum 20 bytes (header without options), maximum 65,535 bytes
- **Three-Way Handshake**: SYN → SYN-ACK → ACK
- **Four-Way Handshake**: FIN → ACK → FIN → ACK
- **Sequence Number**: 32-bit field indicating the byte position in the data stream
- **Acknowledgment Number**: 32-bit field indicating the next expected byte (cumulative ACK)

## Key Points

- UDP provides unreliable, connectionless service ideal for latency-sensitive applications like video streaming, VoIP, and DNS queries
- TCP provides reliable, connection-oriented service essential for applications requiring guaranteed delivery like HTTP, HTTPS, FTP, and email protocols
- TCP's three-way handshake synchronizes initial sequence numbers to prevent delayed segments from previous connections being accepted
- Flow control using sliding window prevents overwhelming slow receivers; congestion control prevents network overload
- TCP maintains state at both endpoints (memory overhead); UDP is stateless (minimal memory usage)
- UDP supports broadcast and multicast; TCP is strictly unicast
- Connection-oriented protocols have higher overhead but guarantee delivery; connectionless protocols prioritize speed

## Common Mistakes to Avoid

1. **Confusing IP (network layer) with transport layer protocols**: IP is connectionless at layer 3; TCP and UDP operate at layer 4
2. **Assuming UDP never delivers data**: UDP is unreliable but can deliver data; it simply doesn't guarantee delivery
3. **Forgetting that TCP provides byte-stream, not message-stream service**: Applications must implement their own message boundaries
4. **Ignoring the TIME-WAIT state**: After connection closure, TCP waits 2MSL (Maximum Segment Lifetime) to handle delayed segments
5. **Thinking TCP is always better**: For real-time applications, TCP's retransmission delays can be worse than occasional packet loss

## Revision Tips

1. Practice drawing the three-way and four-way handshake diagrams—they frequently appear in exams
2. Memorize the exact field sizes in UDP and TCP headers
3. Create a comparison table associating common applications with their transport protocols
4. Understand why each TCP flag (SYN, ACK, FIN, RST, PSH, URG) is used
5. Review sample questions on socket programming differences between UDP and TCP
