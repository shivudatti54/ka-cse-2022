# **Datagram Protocol, Transmission Control Protocol: Services, Features, Segments, TCP Connections, Flow Control, Error Control, Congestion Control**

## **Overview**

### Datagram Protocol (UDP)

- **Service**: Best-effort, connectionless, unreliable
- **Features**:
  - Connectionless
  - No error-checking or correction
  - No flow control
- **Segments**: Small, relatively short
- **TCP Connections**: Not established before data transmission
- **Flow Control**: Not applicable
- **Error Control**: No error-checking or correction
- **Congestion Control**: Not applicable

### Transmission Control Protocol (TCP)

- **Service**: Reliable, connection-oriented
- **Features**:
  - Connection-oriented
  - Error-checking and correction
  - Flow control
- **Segments**: Medium to large
- **TCP Connections**: Established before data transmission
- **Flow Control**: Yes, to prevent network congestion
- **Error Control**:
  - **Error-checking**: Using CRC-16 or checksum
  - **Error-correction**: Using forward error correction (FEC) or retransmission
- **Congestion Control**: Yes, using congestion avoidance algorithms (e.g., Slow Start, Congestion Control Algorithm)

## **Important Formulas and Definitions**

- **Segment size**: Maximum size of a segment (e.g., 1460 bytes)
- **Window size**: Maximum amount of data that can be sent by a sender without receiving an acknowledgement (e.g., 16KB)
- **Congestion window**: The sum of the slow-start window and the congestion avoidance window (e.g., 64KB)
- **Slow-start threshold**: The maximum congestion window size at which the slow-start algorithm is activated (e.g., 1MB)
- **Congestion control algorithm**: A set of rules to control the congestion window size in response to changes in network congestion (e.g., Slow Start, Congestion Control Algorithm)

## **Key Theorems**

- **TCP Retransmission Timeout (RTO)**: The time between two consecutive retransmissions of a packet (e.g., 2 seconds)
- **Maximum segment size (MSS)**: The maximum size of a segment that can be sent by a sender over a network (e.g., 1460 bytes)
