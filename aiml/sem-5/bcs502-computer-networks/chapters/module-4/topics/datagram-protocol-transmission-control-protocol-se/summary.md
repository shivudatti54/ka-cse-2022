# **Datagram Protocol, Transmission Control Protocol: Services, Features, Segments, TCP Connections, Flow Control, Error Control, Congestion Control**

## **Introduction**

- Datagram Protocol (UDP):
  - Connectionless protocol
  - No guarantee of delivery or order of packets
  - Used for applications requiring fast transmission, such as online gaming and video streaming
- Transmission Control Protocol (TCP):
  - Connection-oriented protocol
  - Guarantees delivery and order of packets
  - Used for applications requiring reliable data transfer, such as email and file transfer

## **Services**

- UDP services:
  - Best-effort delivery
  - No acknowledgement or retransmission
  - No flow control or error correction
- TCP services:
  - Reliable data transfer
  - Error detection and correction
  - Flow control to prevent network congestion

## **Features**

- UDP features:
  - Fast transmission
  - Simple header format
  - No connection establishment or termination
- TCP features:
  - Connection establishment and termination
  - Reliable data transfer
  - Error detection and correction

## **Segments**

- UDP segments:
  - No segmentation or reassembly
  - No error correction or flow control
- TCP segments:
  - Segmentation and reassembly
  - Error correction and flow control

## **TCP Connections**

- Three-way handshake for connection establishment:
  1.  SYN (synchronize) packet sent by client
  2.  SYN-ACK (synchronize-acknowledgment) packet sent by server
  3.  ACK (acknowledgment) packet sent by client
- Four-way handshake for connection termination:
  1.  FIN (finish) packet sent by client
  2.  ACK packet sent by server
  3.  FIN packet sent by server
  4.  ACK packet sent by client

## **Flow Control**

- TCP flow control:
  - Window size determines amount of data that can be sent
  - sender throttles transmission to prevent network congestion
- UDP flow control:
  - No flow control, packets sent without consideration for network congestion

## **Error Control**

- TCP error control:
  - Checksum for error detection
  - Acknowledgment and retransmission for error correction
- UDP error control:
  - No error control, packets may be lost or corrupted

## **Formulas and Theorems**

- Shannon-Hartley theorem:
  - relates bit rate to bandwidth and signal-to-noise ratio
- TCP congestion control algorithm:
  - uses slow-start and congestion avoidance to regulate transmission rate

Note: This summary is a concise revision guide and is not intended to be an exhaustive treatment of the topic.
