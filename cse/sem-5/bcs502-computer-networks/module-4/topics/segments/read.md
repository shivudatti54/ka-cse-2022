# TCP Segments

## Introduction

In the TCP/IP model, the Transport Layer is responsible for end-to-end communication between applications running on different hosts. When using the Transmission Control Protocol (TCP), data at this layer is organized into units called **segments**. TCP is a connection-oriented, reliable, and flow-controlled protocol that ensures ordered, error-free delivery of data between communicating endpoints.

A TCP segment consists of a header followed by data. The header contains critical information that enables TCP to provide its reliable communication service, including sequence numbers, acknowledgment numbers, flags, and checksums. Understanding the structure and functionality of TCP segments is fundamental to comprehending how reliable data transmission works in computer networks.

## Key Concepts

### TCP Segment Structure

The TCP segment header has a minimum size of 20 bytes and can extend to 60 bytes with options. The structure includes:

1. **Source Port (16 bits)**: Identifies the sending application's port number
2. **Destination Port (16 bits)**: Identifies the receiving application's port number
3. **Sequence Number (32 bits)**: Indicates the byte position of the first data byte in this segment
4. **Acknowledgment Number (32 bits)**: Confirms received bytes, indicating next expected byte
5. **Data Offset (4 bits)**: Specifies the header length in 32-bit words
6. **Reserved (6 bits)**: Reserved for future use, must be zero
7. **Control Flags (6 bits)**: URG, ACK, PSH, RST, SYN, FIN
8. **Window Size (16 bits)**: Flow control mechanism indicating receive buffer capacity
9. **Checksum (16 bits)**: Error detection for header and data
10. **Urgent Pointer (16 bits)**: Points to urgent data (used with URG flag)
11. **Options (Variable)**: Maximum Segment Size (MSS), window scaling, timestamps

### Sequence Number and Acknowledgment

The sequence number is crucial for reliability. Each byte of data sent is numbered sequentially. When Host A sends a segment containing 100 bytes starting from sequence number 1000, the sequence numbers range from 1000 to 1099. The acknowledgment number in the response indicates the next expected byte, meaning all bytes up to (ack_num - 1) have been received correctly.

### Control Flags

- **SYN**: Initiates a connection (first segment of three-way handshake)
- **ACK**: Acknowledgment number field is valid
- **FIN**: Requests connection termination
- **RST**: Resets the connection immediately
- **PSH**: Push data immediately to application
- **URG**: Urgent pointer field is valid

### Maximum Segment Size (MSS)

MSS defines the largest amount of data TCP can send in a single segment. Typically 1460 bytes (1500 byte Ethernet MTU minus 20 bytes IP header minus 20 bytes TCP header). During connection establishment, endpoints exchange their MSS preferences.

## Examples

### Example 1: Three-Way Handshake

Consider a client (192.168.1.10:5000) connecting to a server (192.168.1.20:80):

1. **Client sends SYN**: Seq=0, Flags=SYN
2. **Server sends SYN-ACK**: Seq=0, Ack=1, Flags=SYN,ACK
3. **Client sends ACK**: Seq=1, Ack=1, Flags=ACK

Connection established with sequence numbers initialized.

### Example 2: Data Transfer with Acknowledgment

Client sends 500 bytes starting at Seq=1000:
- Segment 1: Seq=1000, Data=500 bytes, Flags=ACK
- Server responds: Ack=1500 (expecting next byte at 1500)

If Segment 1 is lost, server continues sending Ack=1500, prompting client to retransmit.

### Example 3: Segment with Multiple Flags

A segment closing a connection:
- Seq=3500, Ack=1200, Flags=FIN,ACK
- This acknowledges received data and initiates connection closure

## Exam Tips

1. Remember that TCP segment header minimum size is 20 bytes (without options) and maximum is 60 bytes (with options)
2. Sequence numbers are 32-bit and can wrap around (modulo 2³²)
3. The acknowledgment number is cumulative—it acknowledges all bytes up to but not including the specified number
4. The Data Offset field indicates header length in 32-bit words (value 5 = 20 bytes, value 15 = 60 bytes)
5. Both sequence and acknowledgment numbers are exchanged during the three-way handshake using the SYN flag
6. The checksum covers the pseudo-header (source IP, destination IP, protocol, TCP length) plus the TCP header and data
7. Window size field is 16 bits, allowing a maximum window of 65,535 bytes; window scaling extends this
8. In exam questions, always verify whether sequence numbers start from 0 or are ISN (Initial Sequence Number) based