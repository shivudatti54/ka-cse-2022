# Network Types, Topologies, OSI & TCP/IP Models

## Comprehensive Study Material for GE6A Computer Networks

---

## 1. Introduction and Real-World Relevance

Computer networking forms the backbone of modern digital communication. From sending emails and streaming videos to conducting video conferences and accessing cloud services, every digital interaction relies on network infrastructure. Understanding network types, topologies, and communication models is fundamental for any computer science professional.

This study material covers the core concepts prescribed in the Delhi University BSc Physical Science (CS) syllabus under NEP 2024. These concepts are essential for comprehending how data travels across networks, how devices are interconnected, and how communication protocols enable seamless data exchange between heterogeneous systems.

---

## 2. Network Types (Classification by Geographic Area)

Networks are classified based on the geographic area they cover. This classification determines the technology, speed, and purpose of the network.

### 2.1 Personal Area Network (PAN)

- **Coverage**: Up to 10 meters
- **Purpose**: Connects personal devices like smartphones, tablets, laptops, and wearables
- **Technology**: Bluetooth, Infrared, NFC (Near Field Communication)
- **Example**: Transferring a file from your phone to a laptop via Bluetooth

### 2.2 Local Area Network (LAN)

- **Coverage**: Limited to a building or campus (up to a few kilometers)
- **Purpose**: Connects computers and devices in a limited area for resource sharing
- **Technology**: Ethernet (10 Mbps to 100 Gbps), Wi-Fi (802.11 standards)
- **Characteristics**: High speed, low latency, owned by a single organization
- **Example**: Office network connecting workstations, printers, and servers

### 2.3 Metropolitan Area Network (MAN)

- **Coverage**: City-wide (10-50 km)
- **Purpose**: Connects multiple LANs within a metropolitan region
- **Technology**: Fiber optic cables, Wireless bridges, DOCSIS
- **Characteristics**: Higher latency than LAN, covers larger geographic area
- **Example**: Cable television network, university campus spread across a city

### 2.4 Wide Area Network (WAN)

- **Coverage**: Global or nationwide
- **Purpose**: Connects LANs and MANs across vast distances
- **Technology**: Satellite links, leased lines, MPLS, cellular networks (4G/5G)
- **Characteristics**: Lower speed compared to LAN, high latency, typically owned by service providers
- **Example**: Internet, corporate VPN connecting branch offices across countries

### 2.5 Campus Area Network (CAN)

- **Coverage**: Multiple buildings in a university or corporate campus
- **Purpose**: Interconnects multiple LANs within a limited geographic area
- **Technology**: Fiber optic backbone, high-speed Ethernet
- **Example**: University network connecting multiple departments

---

## 3. Network Topologies

Network topology defines how devices (nodes) are arranged and how they communicate with each other. The choice of topology affects performance, reliability, cost, and scalability.

### 3.1 Bus Topology

**Structure**: All devices are connected to a single central cable (bus or backbone).

```
    [Node A]    [Node B]    [Node C]    [Node D]
        |          |          |          |
        --------------------------------------
                        Bus/Backbone
```

**Advantages**:
- Easy to implement and cost-effective for small networks
- Requires less cable length

**Disadvantages**:
- If the bus fails, the entire network collapses
- Limited cable length and number of nodes
- Performance degrades with increased traffic
- Difficult to troubleshoot

**Practical Use**: Small legacy networks, temporary networks, labs

### 3.2 Star Topology

**Structure**: All devices connect to a central hub or switch.

```
        [Node A]
            |
        [Hub/Switch]
            /    \
    [Node B]    [Node C]
```

**Advantages**:
- Failure of one node doesn't affect others
- Easy to add or remove devices
- Centralized management and troubleshooting

**Disadvantages**:
- Central device failure affects the entire network
- Requires more cable length than bus topology
- Performance depends on central device capacity

**Practical Use**: Most common in modern LANs, home networks, offices

### 3.3 Ring Topology

**Structure**: Devices connect in a circular fashion; data travels node to node.

```
    [Node A] → [Node B] → [Node C] → [Node D] → [Node A]
```

**Advantages**:
- Equal access for all nodes (token passing)
- Predictable performance
- No collisions

**Disadvantages**:
- Failure of one node can disrupt the entire network
- Difficult to troubleshoot
- Adding/removing nodes disrupts the network

**Practical Use**: IBM Token Ring networks, some fiber distributed data interface (FDDI) networks

### 3.4 Mesh Topology

**Structure**: Devices connect to multiple other devices, providing multiple paths for data.

**Full Mesh**: Every device connects to every other device.

```
    [A]──────[B]
    │╲      ╱│
    │  ╲  ╱  │
    │    X    │
    │  ╱  ╲  │
    │╱      ╲│
    [D]──────[C]
```

**Partial Mesh**: Some devices connect to multiple others.

**Advantages**:
- High redundancy and reliability
- Multiple paths for data transmission
- Fault tolerance

**Disadvantages**:
- Expensive due to extensive cabling
- Complex configuration and maintenance

**Practical Use**: Critical infrastructure, backbone networks, wireless mesh networks

### 3.5 Tree (Hierarchical) Topology

**Structure**: Combination of star and bus topologies; devices organized in a hierarchical manner.

```
                    [Root Hub]
                   /    |    \
            [Switch] [Switch] [Switch]
              /|\      /|\      /|\
           [PCs]    [PCs]    [PCs]
```

**Advantages**:
- Scalable and extensible
- Easy to manage segments
- Supports broadband transmission

**Disadvantages**:
- Root node failure affects entire network
- Complex cabling
- Dependent on backbone capacity

**Practical Use**: Large organizations, campus networks, cable TV networks

### 3.6 Hybrid Topology

**Structure**: Combination of two or more different topologies.

**Example**: Star-bus hybrid commonly used in modern networks.

```
        [Switch 1]       [Switch 2]
           |    \         /    |
        [PCs]  [PCs]   [PCs]  [PCs]
```

**Advantages**:
- Leverages strengths of multiple topologies
- Flexible and scalable

**Disadvantages**:
- Complex design and maintenance

**Practical Use**: Enterprise networks, large-scale installations

---

## 4. OSI Reference Model

The Open Systems Interconnection (OSI) model, developed by ISO (International Organization for Standardization), provides a conceptual framework for understanding network communication. It divides network functions into seven layers.

### 4.1 Layer 1: Physical Layer

**Purpose**: Transmits raw bit streams over a physical medium.

**Functions**:
- Bit synchronization
- Transmission rate control
- Physical topology selection
- Transmission mode (simplex, duplex, half-duplex)
- Cable specifications (UTP, STP, fiber)

**Devices**: Hubs, repeaters, network cables, connectors

**Example**: Ethernet cable (Cat 6), fiber optic patch cord

### 4.2 Data Link Layer

**Purpose**: Provides node-to-node transfer; ensures reliable communication.

**Functions**:
- Framing (dividing data into manageable packets)
- Physical addressing (MAC addresses)
- Error detection and control
- Flow control
- Media access control

**Sub-layers**:
- **LLC (Logical Link Control)**: Handles multiplexing, flow control, error reporting
- **MAC (Media Access Control)**: Manages access to the physical medium

**Devices**: Switches, bridges, Network Interface Cards (NICs)

**Example**: Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11), PPP

### 4.3 Network Layer

**Purpose**: Enables data routing between different networks.

**Functions**:
- Logical addressing (IP addresses)
- Routing (determining best path)
- Fragmentation (breaking large packets)
- Congestion control

**Devices**: Routers, Layer 3 switches

**Protocols**: IP (IPv4, IPv6), ICMP, IGMP, ARP

**Example**: Router forwarding packets between LAN and WAN

### 4.4 Transport Layer

**Purpose**: Provides end-to-end communication and error recovery.

**Functions**:
- Segmentation and reassembly
- Flow control
- Error correction
- Port addressing (distinguishes applications)

**Protocols**:
- **TCP (Transmission Control Protocol)**: Connection-oriented, reliable, ordered delivery
- **UDP (User Datagram Protocol)**: Connectionless, faster, unreliable

**Example**: Web browser communicating with web server (port 80/443)

### 4.5 Session Layer

**Purpose**: Manages sessions between applications.

**Functions**:
- Session establishment, maintenance, and termination
- Authentication
- Synchronization (checkpoints for recovery)

**Protocols**: NetBIOS, RPC, PPTP

**Example**: Video call maintaining continuous connection

### 4.6 Presentation Layer

**Purpose**: Handles data translation and formatting.

**Functions**:
- Data encryption/decryption
- Data compression
- Character code translation
- Format conversion

**Standards**: JPEG, GIF, SSL/TLS, ASCII, EBCDIC

**Example**: SSL encryption for secure web browsing

### 4.7 Application Layer

**Purpose**: Provides network services to end-user applications.

**Functions**:
- Network access
- Resource sharing
- Remote file access
- Email services

**Protocols**: HTTP, FTP, SMTP, DNS, SNMP, Telnet, SSH

**Example**: Web browser requesting a webpage

---

## 5. TCP/IP Model

The TCP/IP (Transmission Control Protocol/Internet Protocol) model is the actual protocol suite used on the Internet. It has four layers.

### 5.1 Comparison: OSI vs TCP/IP

| OSI Layer | TCP/IP Layer | Protocols |
|-----------|--------------|-----------|
| Application | Application | HTTP, FTP, SMTP, DNS |
| Presentation | Application | SSL/TLS, JPEG |
| Session | Application | RPC, NetBIOS |
| Transport | Transport | TCP, UDP |
| Network | Internet | IP, ICMP, ARP |
| Data Link | Network Access | Ethernet, PPP |
| Physical | Network Access | Cables, Hubs |

### 5.2 Detailed TCP/IP Layers

**Network Access Layer (Link Layer)**:
- Combines OSI Physical and Data Link layers
- Handles physical addressing and access to transmission medium
- Protocols: Ethernet, Wi-Fi, Frame Relay

**Internet Layer**:
- Corresponds to OSI Network layer
- Handles logical addressing and routing
- **IP (Internet Protocol)**: Provides best-effort delivery
- **ICMP (Internet Control Message Protocol)**: Error reporting
- **ARP (Address Resolution Protocol)**: Maps IP to MAC addresses

**Transport Layer**:
- Same as OSI Transport layer
- **TCP**: Reliable, connection-oriented
  - Three-way handshake: SYN → SYN-ACK → ACK
  - Flow control using sliding window
  - Error recovery through acknowledgments
- **UDP**: Unreliable, connectionless
  - No handshake, no guaranteed delivery
  - Used for streaming, VoIP, DNS queries

**Application Layer**:
- Combines OSI Application, Presentation, and Session layers
- Protocols for specific applications
- HTTP/HTTPS, FTP, SMTP, POP3, IMAP, DNS, SSH, Telnet

---

## 6. Encapsulation and Decapsulation

When data is transmitted across a network, each layer adds its own header to the data. This process is called **encapsulation**.

### 6.1 Data Encapsulation Process

```
[Application Data]
    ↓ Add Application Header (Data)
[APPDATA]
    ↓ Add Transport Header (Segment/Datagram)
[TCP Header | APPDATA]
    ↓ Add Network Header (Packet)
[IP Header | TCP Header | APPDATA]
    ↓ Add Data Link Header + Trailer (Frame)
[Eth Header | IP Header | TCP Header | APPDATA | CRC]
    ↓ Convert to Bits (Physical Layer)
```

### 6.2 Protocol Data Units (PDUs)

| Layer | PDU Name |
|-------|----------|
| Application | Data |
| Transport | Segment (TCP) / Datagram (UDP) |
| Network | Packet |
| Data Link | Frame |
| Physical | Bits |

### 6.3 Decapsulation

At the receiving end, each layer removes its corresponding header (decapsulation) and passes the data to the layer above.

---

## 7. Practical Examples

### Example 1: Python Socket Programming (TCP Client-Server)

This example demonstrates the Application and Transport layers in action.

**Server Code (Python):**

```python
import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to address and port
server_address = ('localhost', 8888)
server_socket.bind(server_address)

# Listen for connections
server_socket.listen(1)
print("Server listening on port 8888...")

while True:
    # Accept client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    
    try:
        # Receive data
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")
        
        # Send response
        response = "Hello from server!"
        client_socket.sendall(response.encode())
    finally:
        client_socket.close()
```

**Client Code (Python):**

```python
import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
server_address = ('localhost', 8888)
client_socket.connect(server_address)

try:
    # Send data
    message = "Hello server!"
    client_socket.sendall(message.encode())
    print("Message sent")
    
    # Receive response
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
finally:
    client_socket.close()
```

This demonstrates TCP's reliable, connection-oriented communication at the Transport layer.

### Example 2: Network Topology Simulation with NetworkX

```python
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes (devices)
devices = ['PC1', 'PC2', 'PC3', 'PC4', 'Router', 'Server']
G.add_nodes_from(devices)

# Define Star Topology connections
edges = [
    ('PC1', 'Router'), ('PC2', 'Router'), 
    ('PC3', 'Router'), ('PC4', 'Router'),
    ('Router', 'Server')
]
G.add_edges_from(edges)

# Visualize
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=1500, font_size=10, font_weight='bold')
plt.title("Star Topology Network")
plt.show()

# Calculate network metrics
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Network diameter (max shortest path): {nx.diameter(G)}")
```

---

## 8. Key Takeaways

1. **Network Types**: PAN (personal), LAN (local), MAN (metropolitan), WAN (wide), CAN (campus) - classified by geographic coverage.

2. **Topologies**:
   - **Bus**: Single backbone, cost-effective but vulnerable
   - **Star**: Central hub/switch, most common, easy to manage
   - **Ring**: Circular token-passing, predictable but fragile
   - **Mesh**: High redundancy, expensive, used in critical systems
   - **Tree**: Hierarchical, scalable, complex
   - **Hybrid**: Combination of multiple topologies

3. **OSI Model (7 Layers)**: Physical → Data Link → Network → Transport → Session → Presentation → Application

4. **TCP/IP Model (4 Layers)**: Network Access → Internet → Transport → Application

5. **Encapsulation**: Data is wrapped with headers at each layer as it moves down the stack (Application → Physical).

6. **TCP vs UDP**: TCP provides reliable, ordered delivery with error recovery; UDP provides faster, connectionless communication.

7. **Practical Consideration**: Modern networks typically use star topology for LANs, combined with hierarchical tree structures for larger installations.

---

## 9. Practice Questions (Multiple Choice)

### Easy Level

1. Which network type covers the smallest geographic area?
   - A) LAN
   - B) PAN
   - C) MAN
   - D) WAN

2. In which topology is a central device required?
   - A) Bus
   - B) Ring
   - C) Star
   - D) Mesh

3. Which layer of the OSI model handles MAC addresses?
   - A) Network Layer
   - B) Data Link Layer
   - C) Transport Layer
   - D) Physical Layer

### Medium Level

4. What is the primary advantage of a mesh topology?
   - A) Low cost
   - B) High redundancy
   - C) Easy troubleshooting
   - D) Simple cabling

5. Which TCP/IP layer corresponds to the OSI Network layer?
   - A) Application Layer
   - B) Transport Layer
   - C) Internet Layer
   - D) Network Access Layer

6. What is the purpose of the Transport layer?
   - A) Routing packets
   - B) End-to-end communication
   - C) Physical transmission
   - D) Data framing

### Hard Level

7. In the OSI model, which layer is responsible for data encryption?
   - A) Application Layer
   - B) Presentation Layer
   - C) Session Layer
   - D) Network Layer

8. What is the correct order of encapsulation?
   - A) Data → Segment → Packet → Frame → Bits
   - B) Data → Packet → Segment → Frame → Bits
   - C) Bits → Frame → Packet → Segment → Data
   - D) Packet → Data → Segment → Frame → Bits

9. Which protocol operates at the Transport layer and provides unreliable delivery?
   - A) IP
   - B) TCP
   - C) UDP
   - D) HTTP

10. In a full mesh topology with 5 nodes, how many connections are required?
    - A) 4
    - B) 5
    - C) 10
    - D) 20

---

**Answer Key**: 1-B, 2-C, 3-B, 4-B, 5-C, 6-B, 7-B, 8-A, 9-C, 10-C