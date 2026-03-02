# Virtual Circuits and Datagrams: Addressing in Computer Networks

## Introduction

In the realm of computer networking, the way data is transmitted from source to destination forms the backbone of all communication systems. When we examine how packets travel across networks, we encounter two fundamental switching techniques: **virtual circuit switching** and **datagram switching**. Understanding these paradigms is crucial for any computer science student, as they represent the foundational architectural decisions that determine how networks operate at the layer 3 (Network Layer) of the OSI model.

The choice between virtual circuits and datagrams impacts everything from network latency and reliability to routing complexity and quality of service. Traditional telephone networks utilize virtual circuits, while the modern Internet primarily employs datagram-based communication (specifically, the Internet Protocol). This dichotomy reflects a fundamental trade-off in network design: between the predictable, connection-oriented reliability of virtual circuits and the flexible, resilient nature of datagram switching.

Addressing forms the critical mechanism that enables packets to reach their intended destinations across interconnected networks. Without proper addressing schemes, the vast ecosystem of interconnected devices that constitute the Internet would be unable to communicate. This topic explores how different network architectures handle switching and addressing, providing you with the conceptual foundation necessary to understand both classical networking concepts and modern Internet protocols.

## Key Concepts

### Virtual Circuit Switching

**Virtual Circuit (VC) switching** establishes a dedicated logical connection between the source and destination before any data transfer begins. Despite being called a "virtual" circuit, this approach creates a path that behaves like a dedicated physical link, though multiple virtual circuits may share the same physical infrastructure.

The operation of virtual circuit switching involves three distinct phases:

1. **Connection Establishment**: Before transmitting data, a logical path is established through the network. This involves signaling messages that reserve resources (bandwidth, buffer space) at each intermediate router along the path.

2. **Data Transfer**: Once the circuit is established, all packets belonging to the connection follow the same predetermined path. Each packet carries a **Virtual Circuit Identifier (VCI)** rather than the complete destination address, making forwarding more efficient.

3. **Connection Teardown**: After data transfer completes, the resources are released, and the virtual circuit is terminated.

Virtual circuits can be either **permanent** (PVC - Permanent Virtual Circuit) or **switched** (SVC - Switched Virtual Circuit). PVCs are manually configured and remain active indefinitely, while SVCs are dynamically established when needed and torn down after use.

**Frame Relay** and **Asynchronous Transfer Mode (ATM)** are classic examples of technologies that utilize virtual circuit switching. In ATM, for instance, connections are identified by **Virtual Path Identifiers (VPI)** and **Virtual Circuit Identifiers (VCI)**.

### Datagram Switching

**Datagram switching** represents a connectionless approach where each packet (datagram) is treated as an independent unit. Unlike virtual circuits, there is no pre-established path—each router makes independent forwarding decisions for every packet based on its current routing table.

Key characteristics of datagram switching include:

1. **No Connection Setup**: Packets can be sent immediately without any preliminary handshake or resource reservation.

2. **Independent Routing**: Each packet contains the complete destination address and is routed individually. Packets from the same communication might take different paths.

3. **Best-Effort Delivery**: The network makes no guarantees about delivery, sequencing, or quality of service.

4. **Stateless Forwarding**: Routers do not need to maintain connection state information, reducing memory requirements and simplifying router design.

The **Internet Protocol (IP)** is the quintessential example of datagram switching. Each IP packet carries the full source and destination IP addresses, and routers make forwarding decisions independently for each packet.

### Comparison: Virtual Circuits vs Datagrams

| Aspect | Virtual Circuit | Datagram |
|--------|-----------------|----------|
| **Connection Setup** | Required before data transfer | Not required |
| **Addressing** | Uses VCI (short identifier) | Uses full destination address |
| **Router State** | Maintains per-connection state | Stateless (no connection state) |
| **Path Consistency** | All packets follow same path | Packets may take different paths |
| **Quality of Service** | Easier to guarantee | Difficult to guarantee |
| **Failure Handling** | Entire connection fails | Only affected packets fail |
| **Resource Reservation** | Resources reserved in advance | No reservation (congestion possible) |
| **Examples** | ATM, Frame Relay, X.25 | IP, UDP |

### Addressing in Computer Networks

Addressing enables identification and location of devices within a network. Different layers utilize different addressing schemes:

#### Data Link Layer (Layer 2) Addressing: MAC Addresses

**Media Access Control (MAC) addresses** operate at the data link layer and provide hardware-level identification for network interfaces. A MAC address is 48 bits (6 bytes), typically represented in hexadecimal notation (e.g., `00:1A:2B:3C:4D:5E`).

Characteristics of MAC addresses:
- **Burned-in Address (BIA)**: Most MAC addresses are permanently assigned to network hardware
- **Flat Address Space**: MAC addresses have no hierarchical structure
- **Local Scope**: MAC addresses function only within the local network segment (broadcast domain)
- **ARP**: The Address Resolution Protocol maps IP addresses to MAC addresses

#### Network Layer (Layer 3) Addressing: IP Addresses

**Internet Protocol (IP) addresses** operate at the network layer and provide logical addressing that enables routing across interconnected networks. IPv4 addresses are 32 bits, while IPv6 addresses are 128 bits.

IPv4 addressing structure:
- **Network Portion**: Identifies the specific network
- **Host Portion**: Identifies the specific device within the network
- **Subnet Mask**: Determines the network/host boundary

For example, in the IP address `192.168.1.100` with subnet mask `255.255.255.0`:
- Network: `192.168.1.0`
- Host: `100`
- This allows routing to the network `192.168.1.0/24`

#### Port Numbers (Transport Layer)

At the transport layer, **port numbers** identify specific application processes. While IP addresses handle host-to-host communication, ports enable multiple simultaneous connections to the same host. Well-known ports (0-1023) include HTTP (80), HTTPS (443), and FTP (21).

### Hierarchical Addressing and Routing

The hierarchical structure of IP addresses is fundamental to the Internet's scalability. Without hierarchical addressing, routers would need to maintain entries for every single device—a practically impossible task given billions of devices.

The hierarchy works as follows:
1. **Internet Service Providers (ISPs)** allocate address blocks to organizations
2. Organizations subdivide their address space into subnets
3. Individual devices receive host addresses within subnets

This hierarchical allocation means that routers only need to know how to reach the appropriate network prefix, not every individual host. The concept of **Classless Inter-Domain Routing (CIDR)** further enhances this by allowing flexible prefix lengths.

## Examples

### Example 1: Virtual Circuit Path Establishment

Consider a scenario where Host A (connected to Router 1) needs to communicate with Host D (connected to Router 4) through an ATM network. The path is: Host A → Router 1 → Router 2 → Router 3 → Router 4 → Host D.

**Step 1: Connection Request**
Host A sends a SETUP message to Router 1 requesting connection to Host D.

**Step 2: Resource Reservation**
Router 1 allocates VCI=15 for this connection and forwards the SETUP to Router 2. Router 2 allocates VCI=22, Router 3 allocates VCI=31, and Router 4 allocates VCI=18.

**Step 3: Connection Confirmation**
Each router confirms the connection, and a complete path is established:
- Link 1-2: VCI=15 (Router 1), VCI=22 (Router 2)
- Link 2-3: VCI=22 (Router 2), VCI=31 (Router 3)
- Link 3-4: VCI=31 (Router 3), VCI=18 (Router 4)

**Step 4: Data Transfer**
All subsequent packets from Host A to Host D carry VCI=15. Each router uses this VCI to forward packets along the established path, without examining the full destination address.

### Example 2: Datagram Routing Decision

Consider the same topology, but now using IP datagram switching. Host A wants to send three packets to Host D (IP: 203.0.113.50).

**Packet 1**: Router 1 receives the packet with destination 203.0.113.50. Its routing table shows the next hop toward this network is via Router 2. The packet is forwarded to Router 2.

**Packet 2**: Due to network conditions (perhaps congestion on the Router 2 link), Router 1's routing table might update to prefer Router 3. This packet takes a different path: Router 1 → Router 3 → Router 4.

**Packet 3**: This packet might follow yet another path depending on current network state.

Each packet arrives at Host D potentially via different routes and possibly out of order. Host D's transport layer (TCP) handles reordering and reliability.

### Example 3: IP Address Subnetting

Given the IP address `192.168.10.175` with subnet mask `255.255.255.224`, determine:

1. **Network Address**: 
   - IP in binary: `11000000.10101000.00001010.10101111`
   - Mask: `11111111.11111111.11111111.11100000`
   - Network: `11000000.10101000.00001010.10100000` = `192.168.10.160`

2. **Broadcast Address**:
   - Host bits set to 1: `11000000.10101000.00001010.10111111` = `192.168.10.191`

3. **Usable Host Range**:
   - First host: `192.168.10.161`
   - Last host: `192.168.10.190`
   - Total usable hosts: 30

4. **Number of Subnets**:
   - Since /27 (224 = 11100000), we have 3 subnet bits
   - With classful /24 network: 2³ = 8 subnets

## Exam Tips

1. **Remember the Key Difference**: The fundamental distinction is that virtual circuits require connection setup and maintain state, while datagrams are connectionless and stateless. This frequently appears in exam questions.

2. **Address Types**: Know that MAC addresses are flat (48-bit hardware addresses), while IP addresses are hierarchical (32-bit logical addresses enabling routing). Understand how ARP bridges these layers.

3. **VCI vs IP Address**: In virtual circuits, packets use short connection identifiers (VCIs) rather than full destination addresses—this is more efficient but requires connection state management.

4. **Trade-offs Matter**: Be prepared to explain trade-offs between virtual circuits (predictability, QoS) and datagrams (simplicity, resilience). Real-world applications often choose based on these factors.

5. **Subnetting is Essential**: Practice subnetting problems thoroughly—you must be able to calculate network addresses, broadcast addresses, and usable host ranges quickly.

6. **CIDR Understanding**: Classless Inter-Domain Routing notation (e.g., /24, /26) represents the number of network bits. Calculate usable hosts as 2^(32-prefix) - 2.

7. **Historical Context**: While ATM and Frame Relay (virtual circuits) were once dominant, modern networks predominantly use IP (datagrams). Understand why the industry moved toward datagram-based architectures.

8. **Quality of Service**: Virtual circuits easier guarantee QoS because resources are reserved upfront—this is why some applications still benefit from connection-oriented approaches.