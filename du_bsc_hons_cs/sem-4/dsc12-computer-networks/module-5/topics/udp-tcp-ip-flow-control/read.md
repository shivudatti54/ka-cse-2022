# UDP, TCP, and IP Flow Control
## Comprehensive Study Material for BSc (H) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

In the modern internet ecosystem, data communication between devices occurs through a layered approach defined by the TCP/IP model. At the heart of reliable data transmission lie two fundamental transport layer protocols: **User Datagram Protocol (UDP)** and **Transmission Control Protocol (TCP)**. Additionally, the **Internet Protocol (IP)** operates at the network layer and plays a crucial role in addressing and routing packets across interconnected networks.

Understanding these protocols and their flow control mechanisms is essential for any computer science student, particularly those preparing for Delhi University examinations. Whether you're streaming a live video on YouTube, sending an email, or browsing a website, these protocols work behind the scenes to ensure data reaches its destination correctly.

### Real-World Relevance

- **UDP** is used in live video streaming (e.g., Zoom, Netflix in some modes), online gaming, VoIP calls (Skype, WhatsApp) where speed matters more than perfect accuracy
- **TCP** is used in web browsing (HTTP/HTTPS), email transmission (SMTP, POP3, IMAP), file transfers (FTP), and secure transactions (online banking)
- **IP Flow Control** ensures efficient utilization of network resources and prevents congestion collapse

---

## 2. IP Layer: Flow Control at the Network Layer

### 2.1 What is IP?

The **Internet Protocol (IP)** is a network layer protocol responsible for addressing and routing packets from the source to the destination. IP operates on a best-effort delivery model—it does not guarantee packet delivery, order, or error detection. These responsibilities are delegated to higher-layer protocols like TCP.

### 2.2 IP Flow Control Mechanisms

IP itself has limited flow control capabilities. However, the following mechanisms relate to flow control at the IP layer:

#### 2.2.1 Time-to-Live (TTL) Field

The TTL field in the IP header prevents packets from circulating indefinitely in the network. Each router decrements the TTL by 1; when TTL reaches 0, the packet is discarded. This prevents network congestion caused by routing loops.

```
┌─────────────────────────────────────────────────────────────┐
│  IP Header Format (IPv4)                                    │
├──────────┬──────────┬──────────────┬──────────────────────┤
│ Ver (4)  │  IHL (4) │   TOS (8)    │    Total Length (16) │
├──────────┴──────────┴──────────────┴──────────────────────┤
│         Identification (16)         │ Flags (3)│ Offset(13)│
├──────────┴──────────┴──────────────┴──────────────────────┤
│   TTL (8)   │   Protocol (8)      │   Header Checksum     │
├──────────┴──────────┴──────────────┴──────────────────────┤
│                Source IP Address (32)                      │
├─────────────────────────────────────────────────────────────┤
│              Destination IP Address (32)                   │
└─────────────────────────────────────────────────────────────┘
```

#### 2.2.2 Fragmentation and Reassembly

IP enables packet fragmentation when packets exceed the Maximum Transmission Unit (MTU) of a network link. Routers can fragment packets, and the destination host reassembles them. This is a form of flow control—preventing large packets from overwhelming links with smaller MTUs.

#### 2.2.3 ICMP Source Quench (Deprecated)

Originally, ICMP Source Quench messages were used to inform sources to slow down packet transmission when routers detected congestion. However, this mechanism is now deprecated due to security concerns and ineffectiveness.

### 2.3 Quality of Service (QoS) in IP

Modern IP networks implement QoS mechanisms to manage flow control:
- **Differentiated Services (DiffServ)**: Uses Type of Service (ToS) field for priority queuing
- **Packet Scheduling**: Weighted Fair Queuing (WFQ), Priority Queuing
- **Traffic Shaping**: Rate limiting to prevent bursts

---

## 3. User Datagram Protocol (UDP)

### 3.1 Overview

UDP is a **connectionless**, **unreliable** transport layer protocol defined in RFC 768. It provides a simple mechanism for sending datagrams without the overhead of connection establishment, reliability guarantees, or flow control.

### 3.2 UDP Header Format

```
┌────────────────────────────────────────┐
│         Source Port (16 bits)          │
├────────────────────────────────────────┤
│      Destination Port (16 bits)        │
├────────────────────────────────────────┤
│         Length (16 bits)               │
├────────────────────────────────────────┤
│       Checksum (16 bits)               │
└────────────────────────────────────────┘
```

- **Source Port**: Optional; identifies sending port (0 if unused)
- **Destination Port**: Identifies receiving port
- **Length**: Total length of UDP header + data (minimum 8 bytes)
- **Checksum**: Optional in IPv4, mandatory in IPv6 for error detection

### 3.3 Key Characteristics of UDP

| Feature | Description |
|---------|-------------|
| **Connectionless** | No handshake required; data sent immediately |
| **Unreliable** | No guarantee of delivery, order, or error correction |
| **Datagram-oriented** | Messages sent as discrete packets |
| **No flow control** | Sender can overwhelm receiver |
| **No congestion control** | Sender can saturate the network |
| **Low overhead** | 8-byte header vs. 20-byte TCP header |
| **No ordering** | Packets may arrive out of order |

### 3.4 UDP Operations

1. **Sender** creates a UDP datagram with source and destination ports
2. **IP layer** encapsulates UDP datagram into an IP packet
3. **Routers** forward the packet based on destination IP
4. **Receiver** extracts UDP datagram and delivers to application

### 3.5 Advantages and Disadvantages

**Advantages:**
- Lower latency due to no connection setup
- Reduced overhead (smaller header)
- Suitable for broadcast and multicast
- Simpler implementation

**Disadvantages:**
- No delivery guarantee
- No ordering mechanism
- No flow control (receiver may be overwhelmed)
- No congestion control

### 3.6 Common UDP Applications

- DNS queries (port 53)
- DHCP (Dynamic Host Configuration Protocol)
- SNMP (Simple Network Management Protocol)
- Streaming media (RTP - Real-time Transport Protocol)
- Online gaming
- VoIP applications

---

## 4. Transmission Control Protocol (TCP)

### 4.1 Overview

TCP is a **connection-oriented**, **reliable** transport layer protocol defined in RFC 793. It provides robust, ordered, error-checked delivery of data between applications. TCP is the backbone of most internet communication requiring reliability.

### 4.2 TCP Header Format

```
┌──────────────────────────────────────────────────────────────────┐
│         Source Port (16)        │      Destination Port (16)    │
├──────────────────────────────────────────────────────────────────┤
│                     Sequence Number (32)                        │
├──────────────────────────────────────────────────────────────────┤
│                  Acknowledgment Number (32)                     │
├────────┬─────────┴──────────────────────┬───────────────────────┤
│ Offset │  Reserved  │     Flags         │     Window Size (16)  │
├────────┴─────────┴──────────────────────┴───────────────────────┤
│            Checksum (16)                │  Urgent Pointer (16)  │
├──────────────────────────────────────────────────────────────────┤
│                      Options (Variable)                          │
├──────────────────────────────────────────────────────────────────┤
│                        Data (Variable)                           │
└──────────────────────────────────────────────────────────────────┘
```

**Key Fields:**
- **Sequence Number**: Byte position in data stream
- **Acknowledgment Number**: Next expected byte (cumulative ACK)
- **Flags**: SYN, ACK, FIN, RST, PSH, URG
- **Window Size**: Receiver's buffer capacity for flow control

### 4.3 TCP Connection Establishment: Three-Way Handshake

TCP establishes connections through a three-way handshake, ensuring both parties are ready to communicate.

```
Client                                            Server
   │                                                  │
   │─────────── SYN (seq=x) ──────────────────────►   │
   │                                                  │
   │◄──────── SYN-ACK (seq=y, ack=x+1) ─────────────   │
   │                                                  │
   │─────────── ACK (seq=x+1, ack=y+1) ──────────►   │
   │                                                  │
   │              Connection Established              │
   └──────────────────────────────────────────────────┘
```

**Step-by-Step Explanation:**

1. **SYN (Synchronize)**: Client sends a TCP segment with SYN flag set, containing an initial sequence number (ISN) `x`
2. **SYN-ACK**: Server responds with SYN-ACK, sending its ISN `y` and acknowledging client's ISN (`x+1`)
3. **ACK (Acknowledge)**: Client sends ACK, acknowledging server's ISN (`y+1`)

This process ensures:
- Both parties can send and receive
- Both parties agree on initial sequence numbers
- Resources are allocated at both ends

### 4.4 TCP Data Transfer

Once connected, TCP transfers data with the following mechanisms:

- **Sequential Delivery**: Data is numbered with sequence numbers
- **Positive Acknowledgment with Retransmission (PAR)**: Receiver sends ACK for successfully received data
- **Retransmission**: If ACK not received within timeout, sender retransmits

### 4.5 TCP Flow Control

Flow control prevents the sender from overwhelming the receiver. TCP uses a **sliding window protocol** with the **Receiver Window (rwnd)** field.

#### 4.5.1 Sliding Window Mechanism

```
Sender's View:
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
 ▲───────────▲───────────────▲
  Sent &      Sent but      Cannot
  ACKed       not ACKed     send yet
 (left edge)  (right edge)  (window)

Receiver's Window:
┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │
└───┴───┴───┴───┴───┴───┴───┴───┴───┘
 ▲───────────────▲
  Received &    Buffer
  ACKed          Available
```

#### 4.5.2 How Flow Control Works

1. **Receiver** advertises its available buffer space in the **Window Size** field of each ACK
2. **Sender** limits unacknowledged data to the advertised window size
3. When receiver's buffer fills up, window size becomes 0
4. Sender periodically sends **Zero Window Probes** to check if window has opened

#### 4.5.3 Silly Window Syndrome

When receiver advertises small windows (e.g., 1 byte), it leads to inefficiency. Solutions:
- **Nagle's Algorithm** (sender side): Wait for ACK before sending more data unless window is large
- **Clark's Solution** (receiver side): Don't advertise small windows; wait until buffer is at least MSS or half-full

### 4.6 TCP Congestion Control

Congestion control prevents network overload. TCP implements several algorithms:

#### 4.6.1 Key Concepts

- **cwnd (Congestion Window)**: Sender's limit on unacknowledged data
- **ssthresh (Slow Start Threshold)**: Threshold determining slow start vs. congestion avoidance
- **RTT (Round Trip Time)**: Time for packet to travel to receiver and back

#### 4.6.2 Four Phases of Congestion Control

```
Congestion Window (segments)
     │
  32 ├───────●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●───►
     │      /\        /\           /\   /\     
  16 ├─────/  \      /  \         /  \ /  \    
     │    /    \    /    \       /    X    \   
  8  ├───/      \__/      \_____/           \  
     │  /          \                            \
  4  ├─/            \                            \
     │/              \                            \
  2  ├               \                            \
     │                \                            \
  1  ├─────────────────\                            \
     └──────────────────────────────────────────────►
       SS   CA        SS    FR    CA         FR    CA
       
       SS = Slow Start, CA = Congestion Avoidance
       FR = Fast Retransmit, CA = Fast Recovery
```

#### 4.6.3 Slow Start

- Begin with cwnd = 1 MSS (Maximum Segment Size)
- Increase cwnd exponentially: cwnd doubles every RTT (add 1 MSS per ACK)
- Continue until cwnd reaches ssthresh or packet loss occurs

#### 4.6.4 Congestion Avoidance

- After reaching ssthresh, increase cwnd linearly: cwnd += 1 MSS per RTT
- Additive Increase (AI): cwnd = cwnd + MSS²/cwnd per ACK

#### 4.6.5 Fast Retransmit

When sender receives **3 duplicate ACKs** (indicating segment loss):
- Retransmit lost segment without waiting for timeout
- Enter Fast Recovery phase

#### 4.6.6 Fast Recovery

- After fast retransmit, set ssthresh = cwnd/2
- Set cwnd = ssthresh + 3×MSS
- Continue transmitting (sliding window not stuck)

#### 4.6.7 Timeout Handling

If timeout occurs:
- ssthresh = cwnd/2
- cwnd = 1 MSS
- Return to Slow Start phase

### 4.7 TCP Retransmission Mechanisms

TCP ensures reliability through two retransmission strategies:

1. **Timeout-based Retransmission**: If ACK not received within RTO (Retransmission Timeout), retransmit
2. **Fast Retransmit**: Triggered by 3 duplicate ACKs, faster than timeout

### 4.8 TCP Connection Termination

TCP connections are terminated through a four-way handshake:

```
Client                                            Server
   │                                                  │
   │─────────── FIN (seq=x, ACK=y) ──────────────►   │
   │◄─────────── ACK (x+1) ─────────────────────────   │
   │◄─────────── FIN (seq=y, ACK=x+1) ─────────────   │
   │─────────── ACK (y+1) ─────────────────────────►   │
   │                                                  │
   │              Connection Closed                   │
   └──────────────────────────────────────────────────┘
```

**States:**
- FIN-WAIT-1 → FIN-WAIT-2 → TIME-WAIT → CLOSED (Client)
- CLOSE-WAIT → LAST-ACK → CLOSED (Server)

TIME-WAIT state ensures delayed packets are processed and prevents old duplicates from opening new connections.

---

## 5. Comparison: UDP vs TCP

| Feature | UDP | TCP |
|---------|-----|-----|
| **Connection Type** | Connectionless | Connection-oriented |
| **Reliability** | Unreliable | Reliable |
| **Ordering** | Not guaranteed | Guaranteed in order |
| **Flow Control** | None | Sliding Window |
| **Congestion Control** | None | Yes (AIMD, Slow Start) |
| **Header Size** | 8 bytes | 20-60 bytes |
| **Speed** | Fast | Slower |
| **Use Cases** | Streaming, Gaming, DNS | Web, Email, File Transfer |
| **Broadcast/Multicast** | Supported | Not supported |
| **State** | Stateless | Stateful |

---

## 6. Practical Examples with Code

### 6.1 Example 1: UDP Socket Programming in Python

This example demonstrates a simple UDP client-server communication:

**UDP Server (Python)**

```python
import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and port
server_address = ('localhost', 8888)
server_socket.bind(server_address)

print("UDP Server is listening on port 8888...")

while True:
    # Receive data from client
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received from {client_address}: {data.decode()}")
    
    # Send response back to client
    response = f"Server received: {data.decode()}"
    server_socket.sendto(response.encode(), client_address)
```

**UDP Client (Python)**

```python
import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 8888)

try:
    # Send data to server
    message = "Hello, UDP Server!"
    client_socket.sendto(message.encode(), server_address)
    print(f"Sent: {message}")
    
    # Receive server response
    data, server = client_socket.recvfrom(1024)
    print(f"Received from server: {data.decode()}")
    
finally:
    client_socket.close()
```

### 6.2 Example 2: TCP Socket Programming in Python

This example demonstrates reliable TCP communication with flow control:

**TCP Server (Python)**

```python
import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow address reuse
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to address and port
server_address = ('localhost', 8888)
server_socket.bind(server_address)

# Listen for connections (backlog queue = 5)
server_socket.listen(5)
print("TCP Server is listening on port 8888...")

while True:
    # Accept client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connected to client: {client_address}")
    
    try:
        # Receive data from client
        while True:
            data = client_socket.recv(1024)
            if data:
                print(f"Received: {data.decode()}")
                # Send acknowledgment (flow control)
                client_socket.sendall(b"ACK: " + data)
            else:
                break
    finally:
        client_socket.close()
        print(f"Connection closed with {client_address}")
```

**TCP Client (Python)**

```python
import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8888)

try:
    # Establish connection (three-way handshake)
    client_socket.connect(server_address)
    print("Connected to TCP server")
    
    # Send data
    message = "Hello, TCP Server! This is reliable data."
    client_socket.sendall(message.encode())
    print(f"Sent: {message}")
    
    # Receive acknowledgment
    ack = client_socket.recv(1024)
    print(f"Received ACK: {ack.decode()}")
    
finally:
    client_socket.close()
    print("Connection closed")
```

### 6.3 Example 3: Simulating TCP Congestion Control

```python
# Simplified simulation of TCP Congestion Control

def tcp_congestion_simulation():
    cwnd = 1           # Initial congestion window (MSS)
    ssthresh = 16      # Slow start threshold
    rtt = 1            # Assume 1 RTT for simplicity
    
    print(f"Initial: cwnd={cwnd}, ssthresh={ssthresh}")
    
    for rtt_num in range(1, 11):
        if cwnd < ssthresh:
            # Slow Start: exponential growth
            cwnd = cwnd * 2
            phase = "Slow Start"
        else:
            # Congestion Avoidance: linear growth
            cwnd = cwnd + 1
            phase = "Congestion Avoidance"
        
        print(f"RTT {rtt_num}: cwnd={cwnd}, phase={phase}")
        
        # Simulate packet loss at RTT 6
        if rtt_num == 6:
            ssthresh = cwnd // 2
            cwnd = 1
            print(f"*** Packet Loss! ssthresh={ssthresh}, cwnd reset to 1 ***")

tcp_congestion_simulation()
```

**Output:**
```
Initial: cwnd=1, ssthresh=16
RTT 1: cwnd=2, phase=Slow Start
RTT 2: cwnd=4, phase=Slow Start
RTT 3: cwnd=8, phase=Slow Start
RTT 4: cwnd=16, phase=Slow Start
RTT 5: cwnd=17, phase=Congestion Avoidance
RTT 6: cwnd=18, phase=Congestion Avoidance
*** Packet Loss! ssthresh=9, cwnd reset to 1 ***
RTT 7: cwnd=2, phase=Slow Start
RTT 8: cwnd=4, phase=Slow Start
RTT 9: cwnd=8, phase=Slow Start
RTT 10: cwnd=9, phase=Slow Start
```

---

## 7. Key Takeaways

1. **IP Layer** provides best-effort delivery with TTL, fragmentation, and basic QoS mechanisms for flow control at the network level.

2. **UDP** is connectionless, unreliable, and suitable for real-time applications where speed matters more than perfect delivery. It has minimal overhead (8-byte header).

3. **TCP** provides reliable, ordered, error-checked delivery through:
   - Three-way handshake for connection establishment
   - Sequence numbers and acknowledgments for reliability
   - Sliding window protocol for flow control
   - Congestion control algorithms (Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery)
   - Four-way handshake for graceful connection termination

4. **Flow Control** (TCP) prevents receiver buffer overflow using the receiver-advertised window size.

5. **Congestion Control** (TCP) prevents network overload using cwnd, ssthresh, and various algorithms.

6. **Practical Applications**: UDP is used in DNS, streaming, VoIP, gaming; TCP is used in HTTP, HTTPS, email, FTP, SSH.

7. **Delhi University Examination Focus**: Be prepared to explain the three-way handshake, draw and interpret sliding window diagrams, calculate sequence/acknowledgment numbers, and analyze congestion control scenarios.

---

## 8. Assessment Questions

### 8.1 Multiple Choice Questions (Challenging)

**Question 1:** In TCP's three-way handshake, if the client sends SYN with sequence number 100, what will be the acknowledgment number in the server's SYN-ACK segment?

A) 99  
B) 100  
C) 101  
D) 200  

**Answer:** C) 101  
**Explanation:** The acknowledgment number indicates the next expected byte. Since the client sent sequence 100, the server acknowledges it by sending ACK = 100+1 = 101.

---

**Question 2:** Consider a TCP connection with receiver window size of 5000 bytes and current sequence number 1000. The sender has sent bytes 1000-2499. How many more bytes can the sender transmit before receiving an ACK?

A) 2500 bytes  
B) 3500 bytes  
C) 5000 bytes  
D) 1500 bytes  

**Answer:** B) 3500 bytes  
**Explanation:** The receiver window is 5000 bytes. Already sent (unacknowledged) = 2000 bytes (1000-2499). Available window = 5000 - 2000 = 3500 bytes.

---

**Question 3:** In TCP's slow start phase, if the initial congestion window (cwnd) is 1 MSS and ssthresh is 8 MSS, what will be the cwnd after 3 successful RTTs?

A) 3 MSS  
B) 4 MSS  
C) 6 MSS  
D) 8 MSS  

**Answer:** D) 8 MSS  
**Explanation:** Slow start doubles cwnd every RTT:
- RTT 1: cwnd = 1 → 2 MSS
- RTT 2: cwnd = 2 → 4 MSS  
- RTT 3: cwnd = 4 → 8 MSS (reaches ssthresh)

---

**Question 4:** Which of the following is NOT a TCP congestion control mechanism?

A) Slow Start  
B) Fast Retransmit  
C) Token Bucket  
D) Fast Recovery  

**Answer:** C) Token Bucket  
**Explanation:** Token Bucket is a traffic shaping/policing mechanism used in QoS, not a TCP congestion control algorithm. The other three are TCP congestion control mechanisms.

---

**Question 5:** A UDP server receives a datagram from client A. If client A crashes immediately after sending, what happens to the datagram?

A) The datagram is queued until client A reconnects  
B) The datagram is delivered to the application  
C) The datagram is discarded  
D) The datagram triggers an ICMP error  

**Answer:** B) The datagram is delivered to the application  
**Explanation:** UDP is connectionless. The server processes each datagram independently. Once received, it's delivered to the application regardless of the client's state.

---

### 8.2 Scenario-Based Questions

**Scenario 1:** A client is downloading a large file via TCP. The network experiences packet loss at the 10th RTT. Analyze the behavior:

a) What TCP mechanism detects the packet loss?  
b) What happens to cwnd and ssthresh?  
c) Which phase does TCP enter after loss detection?

**Answer:**  
a) **Fast Retransmit** detects packet loss when the sender receives 3 duplicate ACKs.  
b) If fast retransmit: ssthresh = cwnd/2, cwnd = ssthresh + 3×MSS  
   If timeout: ssthresh = cwnd/2, cwnd = 1 MSS  
c) TCP enters **Fast Recovery** (after fast retransmit) or returns to **Slow Start** (after timeout).

---

**Scenario 2:** An organization uses UDP for their internal video conferencing application. They experience dropped video frames during peak hours. Suggest modifications to improve reliability while keeping UDP.

**Answer:**  
1. Implement **application-level acknowledgment** - receiver sends ACKs for received frames  
2. Add **sequence numbers** to detect and reorder frames  
3. Implement **flow control** - receiver advertises buffer capacity  
4. Use **RED (Random Early Detection)** at routers to prevent congestion  
5. Implement **packet prioritization** using DiffServ  
6. Consider **RTP (Real-time Transport Protocol)** which adds timing, sequencing, and payload type identification

---

**Scenario 3:** Given a TCP connection with the following parameters:
- Receiver's advertised window: 8000 bytes
- Congestion window (cwnd): 6000 bytes
- Round Trip Time (RTT): 100ms

Calculate the maximum throughput and explain how flow control and congestion control interact.

**Answer:**  
The **effective window** = min(receiver window, cwnd) = min(8000, 6000) = 6000 bytes  

**Throughput** = Window Size / RTT = 6000 bytes / 0.1s = 60,000 bytes/s = 480 Kbps  

**Interaction:**  
- **Flow control** ensures the sender doesn't overwhelm the receiver (8000 bytes max)  
- **Congestion control** ensures the sender doesn't overwhelm the network (6000 bytes max)  
- TCP takes the **minimum** of both windows to determine actual sending capacity. In this case, the congestion window (6000) is the limiting factor, indicating network congestion.

---

## 9. Flashcards

### UDP

| Term | Definition |
|------|------------|
| **UDP** | Connectionless transport protocol sending datagrams without reliability guarantees |
| **UDP Header Size** | 8 bytes (fixed) |
| **UDP Port Numbers** | Identify specific applications (0-65535) |
| **UDP Checksum** | Optional in IPv4, mandatory in IPv6 |
| **UDP Use Cases** | DNS, DHCP, streaming, VoIP, online gaming |
| **UDP Advantage** | Low latency, minimal overhead |
| **UDP Disadvantage** | No reliability, ordering, or flow control |

### TCP

| Term | Definition |
|------|------------|
| **TCP** | Connection-oriented protocol providing reliable, ordered data delivery |
| **Three-Way Handshake** | SYN → SYN-ACK → ACK process establishing connection |
| **Sequence Number** | Byte position in data stream for ordering |
| **Acknowledgment Number** | Next expected byte from receiver |
| **Sliding Window Protocol** | Mechanism for flow control allowing continuous data transmission |
| **cwnd** | Congestion window - sender's limit on unacknowledged data |
| **ssthresh** | Slow start threshold - boundary between slow start and congestion avoidance |
| **Slow Start** | Phase where cwnd doubles every RTT (exponential growth) |
| **Congestion Avoidance** | Phase where cwnd increases linearly (+1 per RTT) |
| **Fast Retransmit** | Retransmit lost segment after receiving 3 duplicate ACKs |
| **Fast Recovery** | Continue transmitting after fast retransmit without going to slow start |
| **Zero Window Probe** | Sender checks if receiver's window has opened when it's zero |
| **Silly Window Syndrome** | Problem caused by advertising/receiving small windows |
| **Nagle's Algorithm** | Combines small data segments to reduce overhead |
| **TIME-WAIT State** | Ensures all packets are processed before closing connection (2×MSL) |

### IP Flow Control

| Term | Definition |
|------|------------|
| **TTL** | Time-to-Live field preventing indefinite packet circulation |
| **Fragmentation** | Breaking large packets into smaller ones for different MTUs |
| **MTU** | Maximum Transmission Unit - largest packet size on a network link |
| **ICMP Source Quench** | (Deprecated) Mechanism to request sender to slow down |
| **DiffServ** | QoS mechanism using Type of Service field for priority |

---

*Study Material prepared for BSc (H) Computer Science - Delhi University (NEP 2024 UGCF)*