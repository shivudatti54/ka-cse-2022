# **Sliding Window Protocol Revision Notes**

## **What is Sliding Window Protocol?**

- A connection-oriented protocol used in the data link layer
- Used for efficient data transfer over a communication link
- Each device in the connection sends and receives data in fixed-size packets (window size)

**Key Components:**

- **Sender (S)**
- **Receiver (R)**
- **Window Size (W)**
- **Maximum Transmission Unit (MTU)**

**How it Works:**

- Sender breaks data into fixed-size packets
- Receiver acknowledges each packet and sends back an acknowledgement (ACK) packet
- Sender sends data packets in a window of size W
- If a packet is lost, sender retransmits it until it is acknowledged by receiver

**Sliding Window Protocol Algorithm:**

- 1. Sender sends a packet header with sequence number (SN)
- 2. Receiver acknowledges received packet with ACK packet
- 3. If packet is lost, sender sends retransmitted packet
- 4. If sender receives ACK, it fills its window with new packets
- 5. If sender's window is full, it sends a "window full" message to receiver
- 6. Receiver sends an NACK packet if it receives a packet out of order
- 7. Sender retransmits out-of-order packet

**Formulas and Theorems:**

- **Window Size (W) = MTU / 2**
- **Round-Trip Time (RTT) = Time taken for a packet to travel from S to R and back**

**Important Concepts:**

- **Packet Loss**: When a packet is lost during transmission
- **ACK Packet**: Acknowledgement packet sent by receiver to sender
- **NACK Packet**: Non-acknowledgement packet sent by receiver to sender
- **Window Full**: When sender's window is full and it sends a message to receiver
