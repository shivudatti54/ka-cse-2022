# Network Layer Services


## Table of Contents

- [Network Layer Services](#network-layer-services)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Network Layer Functions](#1-network-layer-functions)
  - [2. Internet Protocol (IP)](#2-internet-protocol-ip)
  - [3. Subnetting and CIDR](#3-subnetting-and-cidr)
  - [4. Network Address Translation (NAT)](#4-network-address-translation-nat)
  - [5. Routing Protocols](#5-routing-protocols)
  - [6. ICMP (Internet Control Message Protocol)](#6-icmp-internet-control-message-protocol)
- [Examples](#examples)
  - [Example 1: Subnetting Calculation](#example-1-subnetting-calculation)
  - [Example 2: IP Packet Header Analysis](#example-2-ip-packet-header-analysis)
  - [Example 3: Routing Table Lookup](#example-3-routing-table-lookup)
- [Exam Tips](#exam-tips)

## Introduction

The Network Layer (Layer 3) is the third layer in the OSI (Open Systems Interconnection) model and forms the backbone of data communication across different networks. It is responsible for end-to-end packet delivery, including routing, forwarding, and logical addressing. The network layer abstracts the physical details of data transmission, enabling communication between devices that may be located on different networks across the globe.

In the TCP/IP model, the Network Layer corresponds to the Internet Layer, which includes the IP (Internet Protocol), ICMP (Internet Control Message Protocol), and various routing protocols. This layer ensures that packets find their way from the source to the destination through multiple intermediate networks, making internetworking possible. Without the network layer, communication across different network segments would be impossible, and the modern internet as we know it would not exist.

Understanding network layer services is crucial for computer science engineers as it forms the foundation of network design, configuration, and troubleshooting. 's curriculum emphasizes these concepts to prepare students for real-world networking challenges, including network administration, security, and optimization. This module covers the essential services provided by the network layer, including addressing, routing, forwarding, and supporting protocols.

## Key Concepts

### 1. Network Layer Functions

The network layer provides several critical services that enable communication between devices on different networks:

**Logical Addressing**: Unlike MAC addresses which are physical and tied to network interface cards, logical addresses (IP addresses) are hierarchical and can be assigned dynamically. IPv4 uses 32-bit addresses, while IPv6 uses 128-bit addresses. The network layer uses these addresses to identify devices and determine the best path for packet delivery.

**Routing**: Routing is the process of determining the best path for packets to travel from source to destination. Routers maintain routing tables that contain information about available routes and their metrics. Routing can be static (manually configured) or dynamic (automatically learned through routing protocols).

**Forwarding**: Forwarding is the actual process of moving packets from one router's input interface to the appropriate output interface based on the routing table. While routing is about determining the path, forwarding is about the action of transmitting the packet.

**Fragmentation**: When a packet is larger than the Maximum Transmission Unit (MTU) of a network segment, the network layer may fragment the packet into smaller pieces. Each fragment is then individually routed and reassembled at the destination.

### 2. Internet Protocol (IP)

**IPv4 Header Structure**: The IPv4 header contains essential fields including:

- Version (4 bits): Indicates IP version (4 for IPv4)
- Header Length (4 bits): Length of the header in 32-bit words
- Type of Service (8 bits): Specifies quality of service parameters
- Total Length (16 bits): Total packet size including header and data
- Identification (16 bits): Used for fragmentation reassembly
- Flags (3 bits): Control fragmentation
- Fragment Offset (13 bits): Position of fragment in original datagram
- Time to Live (8 bits): Prevents packets from circulating indefinitely
- Protocol (8 bits): Indicates upper layer protocol (TCP=6, UDP=17, ICMP=1)
- Source Address (32 bits): Sender's IP address
- Destination Address (32 bits): Receiver's IP address

**IPv4 Address Classes**: Traditional classful addressing divides the IPv4 address space into five classes:

- Class A: 1.0.0.0 to 126.255.255.255 (First octet 1-126)
- Class B: 128.0.0.0 to 191.255.255.255 (First octet 128-191)
- Class C: 192.0.0.0 to 223.255.255.255 (First octet 192-223)
- Class D: 224.0.0.0 to 239.255.255.255 (Multicast)
- Class E: 240.0.0.0 to 255.255.255.255 (Reserved)

### 3. Subnetting and CIDR

**Subnetting**: Subnetting divides a large network into smaller, manageable subnets. This improves security, reduces broadcast domains, and enhances network performance. The subnet mask determines how the IP address is divided into network and host portions.

**CIDR (Classless Inter-Domain Routing)**: CIDR replaces classful addressing by using notation like "/n" to indicate the number of bits used for the network portion. For example, 192.168.1.0/24 indicates that the first 24 bits are the network portion.

**Example Subnet Calculation**:
Given IP: 192.168.10.50/26

- Subnet Mask: 255.255.255.192
- Network Address: 192.168.10.0
- Broadcast Address: 192.168.10.63
- Usable Hosts: 62 (50-63 range, excluding network and broadcast)

### 4. Network Address Translation (NAT)

NAT allows multiple devices to share a single public IP address. It translates private IP addresses to public addresses and vice versa. NAT provides security by hiding internal network structure and conserves the limited IPv4 address space.

**Types of NAT**:

- Static NAT: One-to-one mapping between private and public IP
- Dynamic NAT: Pool of public IPs assigned dynamically
- PAT (Port Address Translation): Multiple devices share one IP using different ports

### 5. Routing Protocols

**Distance Vector Protocols**: These protocols (like RIP) use hop count as the metric and periodically broadcast their entire routing table to neighbors. They are simple but have limited scalability.

**Link State Protocols**: Link state protocols (like OSPF) maintain a complete map of the network topology. Each router calculates the best path independently, making them more scalable and faster to converge.

**Border Gateway Protocol (BGP)**: BGP is the routing protocol of the internet, handling routing between autonomous systems. It is a path vector protocol that considers multiple attributes for path selection.

### 6. ICMP (Internet Control Message Protocol)

ICMP is a supporting protocol used for error reporting and diagnostics. It operates at the network layer and is essential for network troubleshooting.

**Common ICMP Messages**:

- Echo Request/Reply: Used by ping command
- Destination Unreachable: Indicates delivery failure
- Time Exceeded: TTL reaches zero
- Source Quench: Congestion control (deprecated)

## Examples

### Example 1: Subnetting Calculation

**Problem**: Given the network 192.168.100.0/24, create 4 equal-sized subnets and determine the subnet mask, network address, broadcast address, and usable host range for the second subnet.

**Solution**:

Step 1: Determine the new subnet mask

- Original: /24 (256 addresses)
- Need 4 subnets: 2^2 = 4, so add 2 bits
- New prefix: /26
- Subnet mask: 255.255.255.192

Step 2: Calculate block size

- Block size = 256 - 192 = 64 addresses per subnet

Step 3: Identify the second subnet

- Subnet 0: 192.168.100.0 - 192.168.100.63
- Subnet 1: 192.168.100.64 - 192.168.100.127 ← Second subnet

Step 4: Fill in the details for Subnet 1

- Network Address: 192.168.100.64
- Broadcast Address: 192.168.100.127
- Usable Host Range: 192.168.100.65 to 192.168.100.126
- Usable Hosts: 62

### Example 2: IP Packet Header Analysis

**Problem**: An IPv4 packet has the following header values:

- Total Length: 1000 bytes
- Identification: 0x1234
- Flags: 010 (Don't Fragment bit set)
- Fragment Offset: 0
- Protocol: 6 (TCP)
- Source: 192.168.1.10
- Destination: 10.0.0.5

Analyze what these values indicate about the packet.

**Solution**:

1. **Total Length (1000 bytes)**: The entire IP packet including header is 1000 bytes. With a minimum header of 20 bytes, the data portion is 980 bytes.

2. **Identification (0x1234)**: This unique identifier helps in reassembling fragmented packets. This packet can be identified as belonging to datagram 0x1234.

3. **Flags (010)**:

- Bit 0: Reserved (always 0)
- Bit 1: Don't Fragment (DF) = 1 - Router cannot fragment this packet
- Bit 2: More Fragments (MF) = 0 - This is the last or only fragment

4. **Fragment Offset (0)**: Since MF is 0, this is either the only fragment or the last fragment, starting at offset 0.

5. **Protocol (6)**: Indicates TCP (Layer 4 protocol). Other common values: 1=ICMP, 17=UDP.

6. **Source/Destination**: Packet originates from private network (192.168.1.10) destined for another private address (10.0.0.5).

### Example 3: Routing Table Lookup

**Problem**: A router has the following routing table:
| Destination | Next Hop | Interface |
|-------------|----------|-----------|
| 0.0.0.0/0 | 203.0.113.1 | eth0 |
| 192.168.1.0/24 | 192.168.1.1 | eth1 |
| 10.0.0.0/8 | 10.1.1.1 | eth2 |
| 172.16.0.0/12 | 172.16.5.1 | eth3 |

For incoming packets with destination IP 192.168.1.50, determine which route will be selected using longest prefix matching.

**Solution**:

Step 1: Compare destination IP against each route

- Route 1 (0.0.0.0/0): Matches all IPs, prefix length = 0
- Route 2 (192.168.1.0/24): Matches 192.168.1.x, prefix length = 24
- Route 3 (10.0.0.0/8): Does not match 192.168.x.x
- Route 4 (172.16.0.0/12): Does not match 192.168.x.x

Step 2: Apply Longest Prefix Match

- Routes matching: Route 1 (0 bits meaningful) and Route 2 (24 bits)
- Longest match: Route 2 with /24

**Result**: Packet to 192.168.1.50 will be forwarded to 192.168.1.1 via interface eth1

## Exam Tips

1. **Remember the order of operations**: When a router receives a packet, it first checks if it's destined for the router itself, then performs routing table lookup using Longest Prefix Match, applies any access control lists, and finally forwards the packet.

2. **Difference between routing and forwarding**: Routing is the control plane function of determining paths, while forwarding is the data plane function of actually moving packets. This distinction is frequently tested in exams.

3. **Subnetting shortcut**: For subnetting questions, remember that the number of subnets = 2^n where n is the number of borrowed bits, and number of hosts = 2^h - 2 where h is the remaining host bits (subtract 2 for network and broadcast addresses).

4. **Protocol numbers to remember**: ICMP = 1, TCP = 6, UDP = 17, OSPF = 89, BGP = 6. These are commonly asked in exams.

5. **TTL purpose**: Time to Live prevents packets from circulating indefinitely in case of routing loops. Each router decrements TTL by 1; when TTL reaches 0, packet is discarded.

6. **Don't Fragment flag**: If a packet has DF bit set and its size exceeds the MTU of an outgoing interface, the router discards the packet and sends an ICMP "Fragmentation Needed" message back to the source.

7. **Private IP addresses ranges**: Remember the private IP ranges - 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. These are not routable on the internet and require NAT for external communication.

8. **OSI layer correspondence**: Remember that the Network Layer (Layer 3) corresponds to the Internet Layer in the TCP/IP model. The data link layer is often subdivided into MAC and LLC sublayers in practical implementations.
