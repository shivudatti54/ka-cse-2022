# Addressing and Routing Algorithms

## Introduction

In modern computer networks, the seamless transfer of data from source to destination relies critically on two fundamental mechanisms: addressing and routing. **Addressing** provides a systematic way to identify devices on a network, while **routing** determines the optimal path that data packets must take to reach their intended destination. Together, these mechanisms form the backbone of internetwork communication.

In the context of the University of Delhi's Computer Science curriculum, understanding addressing and routing algorithms is essential for several reasons. First, IP addressing forms the foundation of network configuration and management in virtually every organization. Second, routing algorithms are the intellectual core of how the internet functions—they enable data to traverse multiple networks and reach destinations across the globe. Third, these concepts frequently appear in competitive examinations, internal assessments, and end-semester examinations, making them crucial for academic success.

This module explores the hierarchical structure of IPv4 addressing, the mathematics of subnetting, Classless Inter-Domain Routing (CIDR), and the two primary categories of routing algorithms: distance vector and link state. We will examine how routers make forwarding decisions, the advantages and limitations of different routing approaches, and practical considerations for network design.

## Key Concepts

### IPv4 Addressing Structure

An IPv4 address is a 32-bit logical address that uniquely identifies a device on a network. It is typically represented in dotted-decimal notation, where the 32 bits are divided into four 8-bit octets, each ranging from 0 to 255. For example, the address 192.168.1.100 in binary is 11000000.10101000.00000001.01100100.

The IPv4 address space is divided into two primary components:
- **Network Address (Network ID)**: The portion of the IP address that identifies the specific network on which a device resides. All devices on the same physical network share the same network address.
- **Host Address (Host ID)**: The portion that uniquely identifies a specific device within that network.

The division between network and host portions is determined by the **subnet mask**, a 32-bit number that uses contiguous 1s to mask the network portion and contiguous 0s to identify the host portion.

### IP Address Classes

Originally, IPv4 addresses were divided into five classes based on the leading bits:

| Class | First Octet Range | Default Subnet Mask | Purpose |
|-------|-------------------|---------------------|---------|
| A     | 1-126             | 255.0.0.0 (/8)      | Large networks |
| B     | 128-191           | 255.255.0.0 (/16)   | Medium networks |
| C     | 192-223           | 255.255.255.0 (/24) | Small networks |
| D     | 224-239           | N/A                 | Multicast |
| E     | 240-255           | N/A                 | Reserved |

**Important observations:**
- Class A addresses begin with a 0 bit, allowing 126 networks (0 and 127 are reserved) with approximately 16 million hosts each.
- Class B addresses begin with 10, providing about 16,384 networks with 65,534 hosts each.
- Class C addresses begin with 110, offering over 2 million networks with 254 hosts each.
- The address 127.x.x.x is reserved for loopback testing (typically 127.0.0.1).

### Subnetting

**Subnetting** is the process of dividing a single network into smaller subnetworks (subnets). This technique was introduced to address two major limitations of classful addressing: inefficient use of address space and insufficient hierarchy for large networks.

A subnet mask determines how the 32-bit IP address is divided. For example, with the IP address 192.168.1.100 and subnet mask 255.255.255.0 (/24):
- Network portion: 192.168.1 (first 24 bits)
- Host portion: 100 (last 8 bits)
- Number of usable hosts: 2^8 - 2 = 254 (subtract network and broadcast addresses)

When we borrow bits from the host portion to create a subnet portion, we create smaller subnets. For instance, borrowing 2 bits from a Class C network creates 4 subnets (2^2), each with 62 usable hosts (2^6 - 2).

**Key formulas for subnetting:**
- Number of subnets = 2^n where n = borrowed bits
- Number of hosts per subnet = 2^(8-n) - 2
- Subnet address = IP AND Subnet Mask
- Broadcast address = Network address OR (NOT Subnet Mask)

### Classless Inter-Domain Routing (CIDR)

CIDR, introduced in 1993, replaced classful addressing to combat the rapid depletion of IPv4 address space. CIDR uses **variable-length subnet masking (VLSM)**, allowing network prefixes of any length rather than being restricted to /8, /16, or /24.

CIDR notation expresses an IP address followed by a slash and a number indicating the prefix length. For example, 192.168.1.0/24 indicates that the first 24 bits are the network portion.

CIDR also enables **route aggregation** (also called supernetting), where multiple networks are summarized into a single routing entry. For instance, 192.168.0.0/22 represents the range from 192.168.0.0 to 192.168.3.255.

### Routing Algorithms

Routers make forwarding decisions based on routing tables that contain information about reachable networks. The process of building and maintaining these routing tables is governed by routing algorithms. There are two fundamental categories:

#### Distance Vector Routing

In **distance vector** algorithms, each router maintains a table (vector) containing the best known distance to every destination network. Routers periodically exchange their entire routing table with directly connected neighbors.

The **Bellman-Ford algorithm** forms the mathematical basis of distance vector routing. The key characteristics are:
- **Metric**: Typically uses hop count (number of routers to traverse)
- **Updates**: Periodic full table exchanges
- **Convergence**: Slow, may cause routing loops
- **Complexity**: O(n) per iteration

**RIP (Routing Information Protocol)** is the classic distance vector protocol. It uses hop count as its metric, with a maximum of 15 hops (16 hops indicates unreachable). RIP version 2 supports CIDR and subnet masks, while version 1 does not.

**Count-to-Infinity Problem**: This is a serious issue in distance vector routing where routers slowly converge when a route becomes unavailable. For example, if A reaches network X via B, and B's link to X fails, A might incorrectly believe it can reach X via C if C claims it has a path—creating an infinite loop of increasing hop counts.

#### Link State Routing

**Link State** algorithms take a different approach. Each router maintains a complete map of the network topology. Routers do not share their entire routing table; instead, they share information only about their directly connected links (link states).

The **Dijkstra shortest path algorithm** is used to compute the optimal path. Key characteristics include:
- **Metric**: Can use bandwidth, delay, or cost (not just hop count)
- **Updates**: Triggered updates when link state changes
- **Convergence**: Fast, less susceptible to routing loops
- **Complexity**: O(n²) with efficient implementation, O(n log n) with priority queue

**OSPF (Open Shortest Path First)** is the predominant link state protocol. It divides networks into areas, with area 0 (backbone) connecting all other areas. OSPF supports VLSM, authentication, and load balancing across equal-cost paths.

### Comparison of Routing Approaches

| Aspect | Distance Vector | Link State |
|--------|------------------|-------------|
| Information shared | Entire routing table | Link states only |
| Metric | Hop count | Bandwidth, cost, delay |
| Convergence | Slow | Fast |
| Routing loops | Prone | Less prone |
| Scalability | Limited | Highly scalable |
| CPU/Memory usage | Low | Higher |
| Examples | RIP, IGRP | OSPF, IS-IS |

## Examples

### Example 1: Subnet Calculation

**Problem**: Given the IP address 172.16.20.45 with subnet mask 255.255.255.224 (/27), determine:
- Network address
- Broadcast address
- First usable host
- Last usable host
- Number of hosts per subnet

**Solution**:

Step 1: Convert subnet mask to binary
255.255.255.224 = 11100000 (27 ones)

Step 2: Calculate host bits: 32 - 27 = 5 bits
Number of hosts = 2^5 - 2 = 32 - 2 = 30 hosts per subnet

Step 3: Determine the subnet size: The last non-zero bit in the subnet mask is 2^(5-1) = 16
So subnets increment by 16: 0, 16, 32, 48, 64...

Step 4: Find which subnet 172.16.20.45 falls into
20 ÷ 16 = 1 remainder 4, so the subnet is 172.16.20.32

Step 5: Calculate required values:
- Network address: 172.16.20.32
- Broadcast address: 172.16.20.63 (next subnet - 1)
- First usable host: 172.16.20.33
- Last usable host: 172.16.20.62

**Answer**: Network: 172.16.20.32/27, Broadcast: 172.16.20.63, Hosts: 172.16.20.33-172.16.20.62, Total: 30 hosts

### Example 2: CIDR Route Aggregation

**Problem**: An organization has the following networks that need to be summarized into a single route:
192.168.0.0/24
192.168.1.0/24
192.168.2.0/24
192.168.3.0/24

Determine the aggregate route.

**Solution**:

Step 1: Write each network in binary
192.168.0.0 = 11000000.10101000.00000000.00000000
192.168.1.0 = 11000000.10101000.00000001.00000000
192.168.2.0 = 11000000.10101000.00000010.00000000
192.168.3.0 = 11000000.10101000.00000011.00000000

Step 2: Find common bits
All four networks share the first 22 bits (192.168.0, 192.168.1, 192.168.2, 192.168.3 differ in the last 6 bits of the third octet and all bits of the fourth octet)

Step 3: Determine prefix length
Common prefix: /22 (255.255.252.0)

Step 4: Calculate range covered
Network: 192.168.0.0/22
Range: 192.168.0.0 to 192.168.3.255

**Answer**: Aggregate route: 192.168.0.0/22

### Example 3: Distance Vector Routing Table Update

**Problem**: Consider three routers A, B, and C in a linear topology: A — B — C. Initial distances from A to networks are: via B = 2 hops, direct = 1 hop. If B's cost to network X becomes 5 (was 3), and B advertises this to A, what is A's new distance to network X?

**Solution**:

Step 1: Current state
A's distance to X via B = 2 (A→B→X)

Step 2: B advertises new cost
B tells A that distance to X is now 5

Step 3: A calculates new path
A's new distance to X via B = A to B (1) + B to X (5) = 6

Step 4: Compare with direct route
If A has a direct route to X with distance 1, A will choose the direct route

**Answer**: A's new distance to X is 1 (direct), as 1 < 6. The route via B is now longer than the direct path.

## Exam Tips

1. **Memorize the default subnet masks** for Classes A, B, and C (/8, /16, /24) as this forms the basis for subnetting problems.

2. **Practice binary-decimal conversions**: Always convert IP addresses and subnet masks to binary when solving subnetting problems to avoid errors.

3. **Remember the special addresses**: 127.x.x.x is loopback, 0.0.0.0 is default route, 255.255.255.255 is limited broadcast.

4. **Understand when to use +2 in host calculations**: Always subtract 2 for network and broadcast addresses unless specified otherwise.

5. **Distinguish between classful and classless routing**: RIPv1 is classful (no VLSM support), while RIPv2 and OSPF support CIDR.

6. **Know the count-to-infinity problem**: This is a classic distance vector limitation—understand how split horizon and poison reverse attempt to solve it.

7. **OSPF uses areas**: Remember that OSPF divides networks into areas, with Area 0 being the backbone—always connects to Area 0.

8. **CIDR notation is crucial**: Be comfortable converting between CIDR notation (e.g., /24) and subnet masks (255.255.255.0).

9. **Private IP address ranges**: Class A: 10.0.0.0-10.255.255.255, Class B: 172.16.0.0-172.31.255.255, Class C: 192.168.0.0-192.168.255.255.

10. **Routing algorithm selection**: For exam questions, remember that link state scales better but uses more memory; distance vector is simpler but prone to loops.