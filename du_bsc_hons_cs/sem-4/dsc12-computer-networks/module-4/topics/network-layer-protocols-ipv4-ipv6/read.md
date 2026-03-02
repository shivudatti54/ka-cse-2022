# Network Layer Protocols: IPv4 and IPv6

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## Table of Contents

1. [Introduction and Real-World Relevance](#1-introduction-and-real-world-relevance)
2. [Internet Protocol Version 4 (IPv4)](#2-internet-protocol-version-4-ipv4)
3. [IPv4 Addressing and Subnetting](#3-ipv4-addressing-and-subnetting)
4. [Classless Inter-Domain Routing (CIDR)](#4-classless-inter-domain-routing-cidr)
5. [Internet Protocol Version 6 (IPv6)](#5-internet-protocol-version-6-ipv6)
6. [IPv6 Header Structure](#6-ipv6-header-structure)
7. [IPv6 Addressing](#7-ipv6-addressing)
8. [Transition from IPv4 to IPv6](#8-transition-from-ipv4-to-ipv6)
9. [Key Takeaways](#9-key-takeaways)
10. [Multiple Choice Questions](#10-multiple-choice-questions)
11. [Flashcards for Quick Revision](#11-flashcards-for-quick-revision)

---

## 1. Introduction and Real-World Relevance

The **Network Layer** (Layer 3 of the OSI model) is responsible for logical addressing, routing, and forwarding packets between different networks. The Internet Protocol (IP) is the fundamental protocol at this layer that enables communication across interconnected networks worldwide.

### Why This Topic Matters

- **Global Internet Infrastructure**: Every device connected to the internet has an IP address—your phone, laptop, smart TV, and servers all rely on IP for communication.
- **Delhi University Syllabus**: This topic is a core component of the Computer Networks paper in BSc (Hons) Computer Science (NEP 2024 UGCF), carrying significant weight in examinations.
- **Career Relevance**: Network administrators, cybersecurity professionals, and cloud engineers must master IP addressing and subnetting.
- **IPv4 Exhaustion**: The depletion of IPv4 addresses led to IPv6 adoption—understanding both protocols is essential for modern networking.

---

## 2. Internet Protocol Version 4 (IPv4)

### 2.1 Overview

IPv4 is a connectionless protocol that provides logical addressing for devices on a network. It uses **32-bit addresses**, allowing for approximately 4.3 billion unique addresses (2³²).

### 2.2 IPv4 Header Structure

The IPv4 header is **20 to 60 bytes** in size, with a minimum of 20 bytes for the fixed portion:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Version  │  IHL  │   ToS/DSCP   │           Total Length                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                         Identification                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│  Flags    │                Fragment Offset                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│   TTL     │    Protocol     │              Header Checksum                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                        Source IP Address (32 bits)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                    Destination IP Address (32 bits)                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                      Options (Variable, 0-320 bits)                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Header Field Descriptions

| Field | Size | Description |
|-------|------|-------------|
| **Version** | 4 bits | IP version (4 for IPv4) |
| **IHL** | 4 bits | Internet Header Length - number of 32-bit words in header (min 5) |
| **ToS/DSCP** | 8 bits | Type of Service / Differentiated Services Code Point |
| **Total Length** | 16 bits | Total packet size (header + data) in bytes |
| **Identification** | 16 bits | Used for fragment reassembly |
| **Flags** | 3 bits | Control flags (Don't Fragment, More Fragments) |
| **Fragment Offset** | 13 bits | Position of fragment in original datagram |
| **TTL** | 8 bits | Time To Live - hop count limit |
| **Protocol** | 8 bits | Upper layer protocol (6=TCP, 17=UDP, 1=ICMP) |
| **Header Checksum** | 16 bits | Error detection for header |
| **Source IP** | 32 bits | Sender's address |
| **Destination IP** | 32 bits | Receiver's address |
| **Options** | Variable | Optional fields for routing, timestamp, security |

---

## 3. IPv4 Addressing and Subnetting

### 3.1 IPv4 Address Structure

An IPv4 address is a **32-bit binary number** represented as four decimal octets (0-255):

```
Example: 192.168.1.100

Binary: 11000000.10101000.00000001.01100100
        └────┬────┘└────┬────┘└────┬────┘└────┬────┘
           192      168        1        100
```

### 3.2 IPv4 Address Classes

The original IPv4 addressing scheme divided the address space into five classes:

| Class | First Octet Range | Default Subnet Mask | Purpose | Network Bits | Host Bits |
|-------|-------------------|---------------------|---------|--------------|-----------|
| **A** | 1-126 | 255.0.0.0 (/8) | Large organizations | 8 | 24 |
| **B** | 128-191 | 255.255.0.0 (/16) | Medium organizations | 16 | 16 |
| **C** | 192-223 | 255.255.255.0 (/24) | Small networks | 24 | 8 |
| **D** | 224-239 | N/A | Multicast | N/A | N/A |
| **E** | 240-255 | N/A | Reserved (experimental) | N/A | N/A |

**Important Notes:**
- **127.x.x.x** is reserved for loopback testing (127.0.0.1 = localhost)
- **0.0.0.0** represents the default route
- **255.255.255.255** is the limited broadcast address

### 3.3 Private IPv4 Addresses

RFC 1918 defines private address ranges not routed on the internet:

| Class | Private Range | CIDR Notation |
|-------|---------------|---------------|
| A | 10.0.0.0 - 10.255.255.255 | 10.0.0.0/8 |
| B | 172.16.0.0 - 172.31.255.255 | 172.16.0.0/12 |
| C | 192.168.0.0 - 192.168.255.255 | 192.168.0.0/16 |

### 3.4 Subnetting

**Subnetting** is the process of dividing a network into smaller sub-networks (subnets). This allows for:
- Better network management
- Improved security
- Reduced broadcast domains
- Efficient IP address utilization

#### Subnet Mask

A subnet mask is a 32-bit number that divides the IP address into network and host portions:

```
IP Address:    192.168.10.50
Subnet Mask:   255.255.255.0 (/24)

Binary:
IP:      11000000.10101000.00001010.00110010
Mask:    11111111.11111111.11111111.00000000
         └──────────────┬─────────────┘
            Network       Host
           (24 bits)     (8 bits)
```

#### Practical Example: Subnetting a Class C Network

**Problem:** You have network 192.168.1.0/24 and need to create 4 subnets with at least 50 hosts each.

**Solution:**

Step 1: Determine the required subnet bits
- 4 subnets = 2² = need 2 bits for subnetting
- New prefix = /24 + 2 = /26

Step 2: Calculate subnet mask
- /26 = 255.255.255.192
- Binary: 11111111.11111111.11111111.11000000

Step 3: Calculate number of hosts per subnet
- Host bits = 32 - 26 = 6 bits
- Usable hosts = 2⁶ - 2 = 64 - 2 = **62 hosts** (✓ meets requirement)

Step 4: List all subnets:

| Subnet | Network Address | Range | Broadcast Address |
|--------|-----------------|-------|-------------------|
| 1 | 192.168.1.0 | 192.168.1.1 - 192.168.1.62 | 192.168.1.63 |
| 2 | 192.168.1.64 | 192.168.1.65 - 192.168.1.126 | 192.168.1.127 |
| 3 | 192.168.1.128 | 192.168.1.129 - 192.168.1.190 | 192.168.1.191 |
| 4 | 192.168.1.192 | 192.168.1.193 - 192.168.1.254 | 192.168.1.255 |

### 3.5 VLSM (Variable Length Subnet Masking)

VLSM allows subnets of different sizes within the same network, maximizing address efficiency.

**Example:**

```
Company Network: 192.168.100.0/24

Requirements:
- Subnet A: 100 hosts
- Subnet B: 50 hosts  
- Subnet C: 25 hosts
- Subnet D: 10 hosts

Solution using VLSM:

Subnet A: 192.168.100.0/25    (128 addresses, 126 usable)
Subnet B: 192.168.100.128/26 (64 addresses, 62 usable)
Subnet C: 192.168.100.192/27 (32 addresses, 30 usable)
Subnet D: 192.168.100.224/28 (16 addresses, 14 usable)
Unused: 192.168.100.240/28
```

---

## 4. Classless Inter-Domain Routing (CIDR)

### 4.1 Why CIDR?

CIDR (introduced in 1993) replaced classful addressing to address:
- **IPv4 exhaustion** - efficient address allocation
- **Routing table explosion** - route aggregation (supernetting)
- **Flexibility** - any prefix length instead of /8, /16, /24

### 4.2 CIDR Notation

CIDR notation combines an IP address with a prefix length:

```
192.168.1.100/24

- /24 means the first 24 bits are the network portion
- Remaining 8 bits (32-24=8) are for host addresses
- Total addresses: 2^(32-24) = 256
- Usable hosts: 256 - 2 = 254
```

### 4.3 CIDR Block Size Reference Table

| Prefix | Subnet Mask | Total Addresses | Usable Hosts |
|--------|-------------|-----------------|--------------|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 |
| /31 | 255.255.255.254 | 2 | 0 (point-to-point) |
| /32 | 255.255.255.255 | 1 | 1 (single host) |

### 4.4 Supernetting (Route Aggregation)

Supernetting combines multiple networks into a single route:

```
Four Class C networks:
192.168.0.0/24
192.168.1.0/24
192.168.2.0/24
192.168.3.0/24

These can be aggregated into: 192.168.0.0/22

Verification:
Network: 192.168.0.0
Mask:    255.255.252.0 (/22)

Binary of first octet in decimal:
0 = 00000000
1 = 00000001
2 = 00000010
3 = 00000011
           └─ Common prefix /22 covers 0-3
```

---

## 5. Internet Protocol Version 6 (IPv6)

### 5.1 Why IPv6?

IPv4's 32-bit address space (≈4.3 billion addresses) is exhausted. IPv6 uses **128-bit addresses**, providing:

- **340 undecillion** unique addresses (3.4 × 10³⁸)
- **Simplified header** for faster processing
- **Built-in security** (IPsec)
- **Auto-configuration** (SLAAC)
- **No NAT** (Native end-to-end connectivity)
- **Quality of Service** improvements

### 5.2 IPv6 Address Format

IPv6 addresses are represented as **8 groups of 4 hexadecimal digits**:

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

**Simplification Rules:**
1. Leading zeros in a group can be omitted: `0db8` → `db8`
2. A single group of consecutive zeros can be replaced with `::` (only once)

```
Full:   2001:0db8:85a3:0000:0000:8a2e:0370:7334
Simplified: 2001:db8:85a3::8a2e:370:7334
```

### 5.3 IPv6 Address Types

| Type | Prefix | Description |
|------|--------|-------------|
| **Unicast** | N/A | Single interface (one-to-one) |
| **Multicast** | ff00::/8 | Group of interfaces (one-to-many) |
| **Anycast** | N/A | Nearest interface in group (one-to-nearest) |

**Note:** IPv6 has **no broadcast** address (replaced by multicast)

### 5.4 Unicast Address Types

| Type | Scope | Prefix | Description |
|------|-------|--------|-------------|
| **Global Unicast** | Worldwide | 2000::/3 | Public internet addresses |
| **Link-Local** | Single link | fe80::/10 | Auto-configured, not routed |
| **Unique Local** | Private | fc00::/7 | Private addressing (like IPv4 private) |
| **Loopback** | Localhost | ::1 | Equivalent to 127.0.0.1 |
| **Unspecified** | Local | :: | All zeros, like 0.0.0.0 |

### 5.5 IPv6 Address Structure

```
Global Routing Prefix (48 bits)    Subnet ID (16 bits)    Interface ID (64 bits)
┌─────────────────────────────────┬──────────────────────┬─────────────────────────┐
│      2001:0db8:abcd:           │       0012:          │    0000:0000:0001       │
│    (ISP assigned)              │   (Organization)     │    (Device/Host)        │
└─────────────────────────────────┴──────────────────────┴─────────────────────────┘
```

---

## 6. IPv6 Header Structure

The IPv6 header is **40 bytes fixed** (simpler than IPv4):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Version  │ Traffic Class │              Flow Label                        │
├─────────────────────────────────────────────────────────────────────────────┤
│         Payload Length        │  Next Header  │       Hop Limit             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                    Source Address (128 bits)                                │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                  Destination Address (128 bits)                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### IPv6 Header Field Descriptions

| Field | Size | Description |
|-------|------|-------------|
| **Version** | 4 bits | IP version (6 for IPv6) |
| **Traffic Class** | 8 bits | QoS/Cos (like IPv4 ToS) |
| **Flow Label** | 20 bits | Identifies packet flows for QoS |
| **Payload Length** | 16 bits | Size of data in bytes |
| **Next Header** | 8 bits | Type of extension header or upper layer protocol |
| **Hop Limit** | 8 bits | TTL equivalent (renamed for clarity) |
| **Source Address** | 128 bits | Sender's IPv6 address |
| **Destination Address** | 128 bits | Receiver's IPv6 address |

### 6.1 Key Differences: IPv4 vs IPv6 Headers

| Feature | IPv4 | IPv6 |
|---------|------|------|
| Header Size | 20-60 bytes | Fixed 40 bytes |
| Checksum | Yes | No (handled by upper layers) |
| Fragmentation | Router and host | Host only |
| Options | Yes (in header) | Extension headers |
| Flow Label | No | Yes (20 bits) |
| Address Size | 32 bits | 128 bits |
| Address Types | Unicast, Multicast, Broadcast | Unicast, Multicast, Anycast |
| Security | Optional (IPsec) | Mandatory (IPsec) |

### 6.2 IPv6 Extension Headers

IPv6 uses extension headers for optional functionality:

1. **Hop-by-Hop Options** - Processed by all routers
2. **Destination Options** - Processed by destination
3. **Routing** - Source routing (like IPv4 loose/strict)
4. **Fragment** - Fragmentation handling
5. **Authentication Header (AH)** - Security
6. **Encapsulating Security Payload (ESP)** - Encryption

---

## 7. IPv6 Addressing (Practical Examples)

### 7.1 IPv6 Address Types with Examples

```python
# Example: Types of IPv6 Addresses

# 1. Global Unicast Address (public internet)
global_unicast = "2001:0db8:85a3::8a2e:0370:7334"

# 2. Link-Local Address (automatic on every interface)
link_local = "fe80::1"

# 3. Unique Local Address (private network)
unique_local = "fd00::1"

# 4. Loopback Address
loopback = "::1"

# 5. Multicast Address
multicast_all_nodes = "ff02::1"
multicast_all_routers = "ff02::2"
```

### 7.2 IPv6 Subnetting Example

```
Given Network: 2001:db8:abcd::/48

Create 100 subnets:

Required bits: log2(100) = 7 bits
New prefix: 48 + 7 = /55

Each /55 subnet has: 2^(128-55) = 2^73 addresses

Subnet addresses:
2001:db8:abcd:0000::/55
2001:db8:abcd:0001::/55
2001:db8:abcd:0002::/55
...
2001:db8:abcd:0063::/55  (64th subnet)
...
2001:db8:abcd:00ff::/55  (256th subnet)
```

### 7.3 IPv6 Configuration Example (Linux)

```bash
# View IPv6 addresses
ip -6 addr show

# Add an IPv6 address to an interface
ip -6 addr add 2001:db8::1/64 dev eth0

# Delete an IPv6 address
ip -6 addr del 2001:db8::1/64 dev eth0

# Set IPv6 default gateway
ip -6 route add default via 2001:db8::ffff

# Check IPv6 connectivity
ping6 google.com

# View IPv6 neighbors (like ARP)
ip -6 neigh show
```

---

## 8. Transition from IPv4 to IPv6

### 8.1 Transition Mechanisms

| Method | Description | Dual Stack | Tunneling | Translation |
|--------|-------------|------------|------------|-------------|
| **Dual Stack** | Devices run both IPv4 and IPv6 simultaneously | ✓ | | |
| **Tunneling** | Encapsulate IPv6 in IPv4 packets | | ✓ | |
| **Translation** | Convert between IPv4 and IPv6 | | | ✓ |

### 8.2 Common Transition Techniques

1. **Tunnel Brokers** - Create tunnels for IPv6 over IPv4
2. **6to4** - Automatic tunneling using 2002::/16 prefix
3. **Teredo** - NAT-friendly tunneling protocol
4. **Dual-Stack Lite** - IPv4-over-IPv6 tunneling

---

## 9. Key Takeaways

### IPv4 Essentials
- **32-bit addressing** with approximately 4.3 billion addresses
- **Header**: 20-60 bytes with checksum, options, fragmentation
- **Classes**: A (1-126), B (128-191), C (192-223), D (224-239), E (240-255)
- **Private ranges**: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
- **Subnetting**: Divides networks using subnet masks; /24 = 254 hosts
- **CIDR**: Flexible prefix notation (e.g., /22) replacing classful routing
- **VLSM**: Variable-length subnet masks for efficient address allocation

### IPv6 Essentials
- **128-bit addressing** with virtually unlimited addresses
- **Header**: Fixed 40 bytes, no checksum, extension headers
- **Address types**: Unicast (global, link-local, unique local), Multicast
- **Simplified representation**: 8 groups of 4 hex digits with `::` compression
- **Auto-configuration**: SLAAC for automatic address assignment
- **Built-in IPsec**: Mandatory security features

### Delhi University Exam Focus
- IPv4 header fields and their functions
- IPv4 classful addressing calculations
- Subnetting problems (finding network address, broadcast, usable range)
- CIDR notation and supernetting
- IPv6 header structure differences from IPv4
- IPv6 address types and representation

---

## 10. Multiple Choice Questions

### Subnetting and Calculation Questions

**Question 1:** What is the network address of the IP 192.168.25.123 with subnet mask 255.255.255.192?

A) 192.168.25.0  
B) 192.168.25.64  
C) 192.168.25.120  
D) 192.168.25.192  

**Answer:** B) 192.168.25.64

---

**Question 2:** How many usable hosts are in a /26 network?

A) 30  
B) 62  
C) 64  
D) 126  

**Answer:** B) 62

---

**Question 3:** You need a subnet with at least 100 hosts. What is the smallest CIDR prefix that satisfies this requirement?

A) /24  
B) /25  
C) /26  
D) /27  

**Answer:** C) /26 (62 usable hosts - doesn't meet) → **Correction:** /25 (126 usable hosts) = **B**

*Wait, let me recalculate:*  
- /26 = 64 - 2 = 62 hosts ❌  
- /25 = 128 - 2 = 126 hosts ✓  

So answer is **B) /25**

---

**Question 4:** Which IPv4 class has the default subnet mask 255.255.0.0?

A) Class A  
B) Class B  
C) Class C  
D) Class D  

**Answer:** B) Class B

---

**Question 5:** The IP address 172.16.25.100 belongs to which private address range?

A) 10.0.0.0/8  
B) 172.16.0.0/12  
C) 192.168.0.0/16  
D) None of the above  

**Answer:** B) 172.16.0.0/12

---

**Question 6:** What is the full expanded form of the IPv6 address `2001:db8::1`?

A) 2001:0db8:0000:0000:0000:0000:0000:0001  
B) 2001:0db8:0:0:0:0:0:1  
C) Both A and B are correct  
D) None of the above  

**Answer:** C) Both A and B are correct (both are valid expansions)

---

**Question 7:** Which protocol in IPv6 replaces the ARP function?

A) RARP  
B) ICMPv6  
C) NDP (Neighbor Discovery Protocol)  
D) IGMP  

**Answer:** C) NDP (Neighbor Discovery Protocol)

---

**Question 8:** A network administrator needs to subnet 192.168.1.0/24 into 8 equal subnets. What will be the new subnet mask?

A) 255.255.255.128 (/25)  
B) 255.255.255.192 (/26)  
C) 255.255.255.224 (/27)  
D) 255.255.255.240 (/28)  

**Answer:** C) 255.255.255.224 (/27)

*Explanation: 8 subnets = 2³, so add 3 bits to /24 = /27*

---

**Question 9:** What is the loopback address in IPv6?

A) 127.0.0.1  
B) ::1  
C) fe80::1  
D) 255.255.255.255  

**Answer:** B) ::1

---

**Question 10:** Which of the following is NOT a valid IPv6 address type?

A) Unicast  
B) Broadcast  
C) Multicast  
D) Anycast  

**Answer:** B) Broadcast (IPv6 does not have broadcast; uses multicast instead)

---

**Question 11:** In IPv4, what is the purpose of the TTL field?

A) Specifies packet priority  
B) Limits packet lifetime (hop count)  
C) Identifies the protocol  
D) Error correction  

**Answer:** B) Limits packet lifetime (hop count)

---

**Question 12:** The CIDR block 192.168.0.0/22 represents how many Class C networks?

A) 1  
B) 2  
C) 4  
D) 8  

**Answer:** C) 4

*Explanation: /22 covers 4 contiguous Class C networks (192.168.0.0, .1, .2, .3)*

---

## 11. Flashcards for Quick Revision

### IPv4 Flashcards

| Term | Definition |
|------|------------|
| **IPv4** | Internet Protocol Version 4 - 32-bit logical addressing scheme |
| **Subnet Mask** | 32-bit number dividing IP into network and host portions |
| **CIDR** | Classless Inter-Domain Routing - flexible prefix notation |
| **VLSM** | Variable Length Subnet Masking - different subnet sizes |
| **Default Gateway** | Router connecting local network to other networks |
| **Broadcast Address** | Last address in subnet - sends to all hosts |
| **Network Address** | First address in subnet - identifies the network |
| **Private IP** | Non-routable addresses (10.x, 172.16-31.x, 192.168.x) |
| **Loopback** | 127.0.0.1 - testing local network stack |
| **ARP** | Address Resolution Protocol - maps IP to MAC |

### IPv6 Flashcards

| Term | Definition |
|------|------------|
| **IPv6** | Internet Protocol Version 6 - 128-bit addressing |
| **Global Unicast** | Public IPv6 address (2000::/3 prefix) |
| **Link-Local** | Auto-configured address (fe80::/10) - not routed |
| **Unique Local** | Private IPv6 addresses (fc00::/7) |
| **Multicast** | One-to-many communication (ff00::/8) |
| **Anycast** | One-to-nearest delivery |
| **SLAAC** | Stateless Address Autoconfiguration |
| **NDP** | Neighbor Discovery Protocol - replaces ARP, ICMP |
| **Extension Headers** | Optional headers for options, routing, security |
| **Dual Stack** | Running IPv4 and IPv6 simultaneously |

---

## References for Further Study

1. **Textbook:** Computer Networking: A Top-Down Approach by Kurose & Ross
2. **RFC Documents:** RFC 791 (IPv4), RFC 2460 (IPv6), RFC 1517 (CIDR)
3. **Delhi University Recommended:** Data Communications and Networking by Behrouz A. Forouzan

---

*This study material is specifically designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum.*