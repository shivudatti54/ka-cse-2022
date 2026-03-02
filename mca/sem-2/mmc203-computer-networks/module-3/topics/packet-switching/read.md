# Packet Switching


## Table of Contents

- [Packet Switching](#packet-switching)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Packet Structure](#1-packet-structure)
  - [2. Store-and-Forward Mechanism](#2-store-and-forward-mechanism)
  - [3. Routing in Packet Switching](#3-routing-in-packet-switching)
  - [4. Types of Packet Switching](#4-types-of-packet-switching)
  - [5. Packet Switching vs Circuit Switching](#5-packet-switching-vs-circuit-switching)
  - [6. Queueing Theory in Packet Switching](#6-queueing-theory-in-packet-switching)
  - [7. Quality of Service (QoS) in Packet Switching](#7-quality-of-service-qos-in-packet-switching)
- [Examples](#examples)
  - [Example 1: Web Page Request](#example-1-web-page-request)
  - [Example 2: Datagram vs Virtual Circuit Path Selection](#example-2-datagram-vs-virtual-circuit-path-selection)
  - [Example 3: Delay Calculation](#example-3-delay-calculation)
- [Exam Tips](#exam-tips)

## Introduction

Packet switching is a fundamental networking paradigm that revolutionized data communication by enabling efficient transmission of data across computer networks. Unlike traditional circuit-switched networks where a dedicated communication path is established before data transfer, packet switching breaks data into smaller, manageable chunks called packets that are transmitted independently across the network. This approach was developed to address the inefficiencies of circuit switching, particularly for bursty traffic patterns common in computer communications.

The concept emerged from ARPANET in the late 1960s and has become the foundation of modern data communications, including the Internet. In packet switching, each packet contains not only the data payload but also control information, including source and destination addresses, sequence numbers, and error-checking information. This self-contained nature of packets allows them to be routed independently through the network, potentially taking different paths to reach the same destination. Upon arrival, packets are reassembled in the correct order to reconstruct the original message. This methodology offers significant advantages in terms of resource efficiency, robustness, and scalability, making it the dominant paradigm for data transmission in contemporary networks.

## Key Concepts

### 1. Packet Structure

A data packet typically consists of two main components: the header and the payload (data). The header contains crucial control information including:

- **Source Address**: IP address of the sending device
- **Destination Address**: IP address of the intended recipient
- **Sequence Number**: Position of the packet in the original message for reassembly
- **Protocol Information**: Indicates the transport protocol being used (TCP/UDP)
- **Error Detection**: Checksum or CRC for data integrity verification
- **Time-to-Live (TTL)**: Prevents packets from circulating indefinitely in the network

The payload contains the actual application data being transmitted. Modern networks typically use variable-length packets, though some protocols specify fixed lengths.

### 2. Store-and-Forward Mechanism

Packet switching employs the store-and-forward technique where each network node (router or switch) receives the complete packet, stores it in memory, examines the header to determine the appropriate output interface, and then forwards the packet to the next node. This process introduces latency but ensures reliability and enables error checking at each hop. The store-and-forward mechanism also allows routers to implement congestion control and quality of service (QoS) mechanisms.

### 3. Routing in Packet Switching

Packets are routed based on routing tables maintained by each router. These tables can be populated through static configuration or dynamic routing protocols. Each packet is examined individually, and the router determines the best path based on factors such as:

- Network topology
- Link congestion levels
- Routing protocol metrics (cost, hop count, bandwidth)
- Quality of Service requirements

### 4. Types of Packet Switching

**Datagram Packet Switching (Connectionless)**
In datagram switching, each packet is treated independently with no prior connection establishment. Each packet contains complete destination information and is routed individually. Since packets may take different paths, they may arrive out of order at the destination. This approach provides high resilience as the failure of one node or link doesn't affect other packets. The Internet uses this approach (IP protocol).

**Virtual Circuit Switching (Connection-Oriented)**
Virtual circuit switching establishes a logical connection (virtual circuit) before data transmission begins. All packets belonging to a session follow the same predetermined path. A virtual circuit identifier in each packet identifies the connection. This approach guarantees packet ordering and provides more predictable performance. Frame Relay and X.25 are examples of virtual circuit networks.

### 5. Packet Switching vs Circuit Switching

| Feature        | Packet Switching          | Circuit Switching           |
| -------------- | ------------------------- | --------------------------- |
| Connection     | No dedicated path         | Dedicated path required     |
| Resource Usage | Dynamic, shared           | Reserved for entire session |
| Congestion     | Packet-level              | Call-level                  |
| Delay          | Variable                  | Fixed (once established)    |
| Efficiency     | Higher for bursty traffic | Lower for idle periods      |
| Cost           | Based on data volume      | Based on connection time    |

### 6. Queueing Theory in Packet Switching

Packet-switched networks use queueing theory to analyze performance. When packets arrive faster than they can be forwarded, they wait in queues. Key metrics include:

- **Average Queue Length**: Number of packets waiting
- **Packet Loss**: Occurs when queues overflow
- **End-to-end Delay**: Sum of propagation, transmission, processing, and queueing delays

### 7. Quality of Service (QoS) in Packet Switching

Packet-switched networks must implement QoS mechanisms to guarantee performance for different traffic types. Common mechanisms include:

- **Priority Queueing**: Higher priority packets processed first
- **Weighted Fair Queueing**: Bandwidth allocation based on weights
- **Traffic Shaping**: Regulating packet flow rates
- **Congestion Management**: Techniques to handle network congestion

## Examples

### Example 1: Web Page Request

Consider a user requesting a web page of size 50 KB over an HTTP connection. The data is broken into packets assuming maximum segment size (MSS) of 1460 bytes:

**Given:**

- Page size: 50 KB = 51,200 bytes
- MSS: 1460 bytes
- Number of packets: 51,200 ÷ 1460 ≈ 35 packets

**Solution:**

1. The TCP layer breaks the 50 KB data into 35 segments
2. Each segment gets a TCP header (20 bytes) and IP header (20 bytes)
3. Each packet is individually addressed and routed
4. The receiving host acknowledges each packet
5. TCP reassembles packets in sequence order
6. HTTP delivers the complete web page to the browser

The packets may travel through different routers and arrive at slightly different times. The sequence numbers in TCP headers enable proper reassembly.

### Example 2: Datagram vs Virtual Circuit Path Selection

**Scenario:** Sending 5 packets from Node A to Node D through an intermediate network.

**Datagram Approach:**

- Packet 1: A → R1 → R3 → D
- Packet 2: A → R2 → R4 → D (different path due to congestion)
- Packet 3: A → R1 → R3 → D
- Packet 4: A → R2 → R4 → D
- Packet 5: A → R1 → R3 → D

**Virtual Circuit Approach:**

- A virtual circuit is established: A → R1 → R3 → D
- All 5 packets follow this exact path
- Each packet carries virtual circuit identifier

**Analysis:** The datagram approach adapts to network conditions but packets may arrive out of order. The virtual circuit provides ordering but cannot adapt if a link fails.

### Example 3: Delay Calculation

**Problem:** Calculate end-to-end delay for transmitting a 1000-byte packet across 3 links.

**Given:**

- Packet size: 1000 bytes = 8000 bits
- Each link: 1 Mbps bandwidth, 10 ms propagation delay
- Each router: 2 ms processing delay
- No queueing delay

**Solution:**

**Step 1: Transmission delay on each link**

- Tt = Packet size / Bandwidth = 8000 bits / 1,000,000 bps = 8 ms per link

**Step 2: Propagation delay**

- Tp = 10 ms per link × 3 = 30 ms

**Step 3: Processing delay**

- At 2 routers: 2 × 2 ms = 4 ms

**Step 4: Total delay**

- Total = (3 × 8 ms) + 30 ms + 4 ms = 24 + 30 + 4 = **58 ms**

## Exam Tips

1. **Remember packet switching characteristics**: No dedicated path, dynamic resource sharing, packets routed independently, store-and-forward operation.

2. **Difference between datagram and virtual circuit**: Datagram is connectionless (each packet independent), virtual circuit is connection-oriented (logical path established first).

3. **Packet header fields**: For exam questions, remember key fields include source/destination addresses, sequence number, TTL, and checksum.

4. **Advantages over circuit switching**: Better resource utilization, handles bursty traffic efficiently, more resilient to failures, cost-effective.

5. **Calculate number of packets**: Divide total data size by maximum segment size, always round up since you can't have partial packets.

6. **Understand delay components**: End-to-end delay = Transmission delay + Propagation delay + Processing delay + Queueing delay.

7. **QoS mechanisms**: Be familiar with priority queueing, weighted fair queueing, and traffic shaping as methods to manage packet-switched network performance.

8. **Real-world examples**: The Internet uses IP (datagram), while Frame Relay and ATM use virtual circuits - know these associations for exam questions.
