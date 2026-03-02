# UDP, TCP & IP Flow Control
**BSc (Hons) Computer Science – Delhi University (NEP 2024 UGCF)**

---

## Introduction
Flow control is a critical mechanism in computer networks that ensures efficient data transmission between sender and receiver. It prevents the sender from overwhelming the receiver with more data than it can process. The **TCP/IP protocol suite** implements flow control at different layers, primarily in TCP, while UDP and IP have minimal or no built-in flow control mechanisms.

---

## IP (Internet Protocol) - Network Layer
- **Best-effort delivery** service — no guarantee of packet delivery, order, or error control
- **No flow control** mechanism at this layer
- Each packet (datagram) is routed independently
- Router congestion may lead to packet drops but IP does not implement any flow control
- Designed for simplicity and scalability

---

## UDP (User Datagram Protocol) - Transport Layer
- **Connectionless** protocol — no handshake or persistent connection
- **No flow control** mechanism implemented
- Sender transmits datagrams without checking receiver's capacity
- No acknowledgment (ACK) of received packets
- Suitable for real-time applications (video streaming, VoIP, DNS) where speed matters more than reliability
- **Limitations**: Packets may be lost, duplicated, or arrive out of order

---

## TCP (Transmission Control Protocol) - Transport Layer
- **Connection-oriented** protocol with reliable, ordered data delivery
- Implements **robust flow control** to prevent sender from overwhelming receiver

### Key Flow Control Mechanisms:

1. **Sliding Window Protocol**
   - Sender maintains a "window" of unacknowledged packets
   - Window size determines how much data can be sent before receiving ACKs
   - Dynamically adjusts based on receiver's capacity

2. **Receiver's Window (rwnd)**
   - Receiver advertises available buffer space in every ACK
   - Sender limits data to this advertised window size

3. **Acknowledgments (ACKs)**
   - Cumulative ACKs confirm successful receipt of data
   - Sender uses ACKs to slide the window forward

4. **Zero Window Probe**
   - If receiver's buffer fills, it advertises rwnd = 0
   - Sender periodically probes to check if window has reopened

5. **Silly Window Syndrome Prevention**
   - Avoids small window sizes through Nagle's algorithm (sender) and delayed ACKs (receiver)

---

## Key Differences Summary

| Feature | IP | UDP | TCP |
|---------|----|----|-----|
| Layer | Network | Transport | Transport |
| Connection | N/A | Connectionless | Connection-oriented |
| Flow Control | ❌ | ❌ | ✅ |
| Reliability | Best-effort | Unreliable | Reliable |
| Use Case | Routing | Real-time apps | Web, Email, File transfer |

---

## Conclusion
Flow control is essential for network efficiency and reliability. While **IP provides no flow control** and **UDP prioritizes speed over reliability**, **TCP implements comprehensive flow control** through sliding windows, ACKs, and buffer management. For the Delhi University exam, remember that TCP ensures data integrity through flow and congestion control, whereas UDP is best suited for latency-sensitive applications where occasional data loss is acceptable.