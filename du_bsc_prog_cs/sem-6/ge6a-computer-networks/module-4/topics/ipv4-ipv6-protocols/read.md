# IPv4 and IPv6 Protocols

## Introduction

The Internet Protocol (IP) forms the backbone of modern computer networking, providing the fundamental addressing and routing mechanism that enables communication between devices across the globe. Among the two principal versions of IP currently in use—IPv4 and IPv6—each represents distinct approaches to network layer addressing and carries significant implications for network design, security, and scalability.

IPv4 (Internet Protocol version 4), developed in 1981, has been the dominant protocol powering the internet for over four decades. It utilizes a 32-bit addressing scheme, theoretically allowing for approximately 4.3 billion unique IP addresses. However, the explosive growth of internet-connected devices—smartphones, tablets, IoT sensors, cloud servers—has exhausted the IPv4 address space, creating an urgent need for a more expansive addressing scheme. This scarcity led to the development of workarounds like Network Address Translation (NAT) and Classless Inter-Domain Routing (CIDR), which extended IPv4's lifespan but couldn't provide a permanent solution.

IPv6 (Internet Protocol version 6), standardized in 1998, addresses these limitations through a 128-bit addressing system, offering approximately 340 undecillion (3.4 × 10³⁸) unique addresses. Beyond addressing, IPv6 incorporates numerous improvements including simplified header structures for faster processing, built-in security through IPsec, auto-configuration capabilities, and enhanced quality of service (QoS) support. The University of Delhi's Computer Science curriculum recognizes the critical importance of understanding both protocols, as organizations worldwide are in various stages of transitioning from IPv4 to IPv6—a process that will span many years and requires professionals who comprehend both systems.

## Key Concepts

### IPv4 Header Structure

The IPv4 header consists of 20-60 bytes containing essential information for packet delivery. Understanding each field is crucial for network troubleshooting and optimization:

**Version (4 bits):** Indicates the IP version; for IPv4, this field contains the value 4.

**IHL (Internet Header Length) (4 bits):** Specifies the header length in 32-bit words. A minimum value of 5 indicates a 20-byte header without options.

**Type of Service (8 bits):** Originally designed for QoS, this field (now often called Differentiated Services Code Point - DSCP) helps prioritize certain types of traffic. Values include precedence levels (0-7) and delay/throughput/reliability flags.

**Total Length (16 bits):** Defines the entire packet size in bytes, including header and data. Maximum size is 65,535 bytes.

**Identification (16 bits):** Used for fragment reassembly; each fragment of a packet carries the same identification value.

**Flags (3 bits):** Control fragmentation—Bit 0: Reserved; Bit 1: Don't Fragment (DF); Bit 2: More Fragments (MF).

**Fragment Offset (13 bits):** Indicates the position of the fragment in the original packet, measured in 8-byte blocks.

**Time to Live (8 bits):** Prevents packets from circulating indefinitely; decremented by each router. When TTL reaches zero, the packet is discarded.

**Protocol (8 bits):** Identifies the upper-layer protocol—6 for TCP, 17 for UDP, 1 for ICMP.

**Header Checksum (16 bits):** Error-checking mechanism for the header only.

**Source Address (32 bits):** The sender's IP address.

**Destination Address (32 bits):** The receiver's IP address.

**Options (variable):** Optional fields for security, routing, timestamp, etc.

### IPv4 Addressing System

IPv4 addresses are 32-bit numbers typically expressed in dotted-decimal notation (e.g., 192.168.1.1), where each octet represents 8 bits (0-255).

**Address Classes:**
- Class A: 1.0.0.0 – 126.255.255.255 (First bit 0, /8 network)
- Class B: 128.0.0.0 – 191.255.255.255 (First two bits 10, /16 network)
- Class C: 192.0.0.0 – 223.255.255.255 (First three bits 110, /24 network)
- Class D (Multicast): 224.0.0.0 – 239.255.255.255
- Class E (Reserved): 240.0.0.0 – 255.255.255.255

**Special Addresses:**
- 0.0.0.0: Default route (this network)
- 127.0.0.1: Loopback address
- 255.255.255.255: Limited broadcast
- Private IP ranges: 10.0.0.0-10.255.255.255, 172.16.0.0-172.31.255.255, 192.168.0.0-192.168.255.255

### Classless Inter-Domain Routing (CIDR)

CIDR, introduced in 1993, replaced classful addressing by allowing flexible prefix lengths. The notation uses a slash (/) followed by the number of network bits: e.g., 192.168.1.0/24 represents 256 addresses (254 usable hosts). CIDR enables:
- More efficient address allocation
- Route aggregation (supernetting)
- Reduced routing table sizes

### IPv6 Header Structure

IPv6 headers are simplified (40 bytes fixed) compared to IPv4, enabling faster processing:

**Version (4 bits):** Value 6 for IPv6.

**Traffic Class (8 bits):** Similar to Type of Service, for QoS prioritization.

**Flow Label (20 bits):** Identifies packet flows for special handling (e.g., real-time video).

**Payload Length (16 bits):** Size of the data payload in bytes.

**Next Header (8 bits):** Identifies the type of header following IPv6 header (TCP, UDP, ICMPv6, or extension headers).

**Hop Limit (8 bits):** Equivalent to TTL in IPv4.

**Source Address (128 bits):** Sender's 128-bit IPv6 address.

**Destination Address (128 bits):** Receiver's 128-bit IPv6 address.

### IPv6 Address Types

**Unicast:** Identifies a single interface. Types include:
- Global Unicast: Public addresses (2000::/3)
- Link-Local: FE80::/10 (auto-configured, not routable)
- Unique Local: FC00::/7 (private addresses, similar to IPv4 private ranges)
- Loopback: ::1

**Multicast:** Identifies multiple interfaces (FF00::/8). Replaces IPv4 broadcast.

**Anycast:** Assigned to multiple interfaces; delivery to the nearest one.

### IPv6 Address Representation

IPv6 addresses use colon-hexadecimal notation (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334). Compression rules:
- Leading zeros in each hextet can be omitted
- A single consecutive group of zeros can be replaced by :: (only once per address)

Example: 2001:db8::1 represents a complete IPv6 address.

### Transition Mechanisms

Since complete IPv6 adoption is gradual, several transition mechanisms exist:

**Dual Stack:** Running both IPv4 and IPv6 on devices simultaneously.

**Tunneling:** Encapsulating IPv6 packets within IPv4 for transport over IPv4 networks. Types include:
- 6to4 (uses 2002::/16)
- Teredo
- ISATAP

**NAT64/DNS64:** Allows IPv6-only clients to communicate with IPv4 servers.

**Translation:** Converting between IPv4 and IPv6 at network boundaries (e.g., SIIT, NAT64).

## Examples

### Example 1: IPv4 Subnet Calculation

**Problem:** Given the network 192.168.10.0/26, determine:
a) Number of subnets
b) Number of usable hosts per subnet
c) First and last usable IP addresses

**Solution:**
- /26 means 26 bits for network, 6 bits for hosts
- Number of usable hosts = 2⁶ - 2 = 64 - 2 = 62 hosts
- Since this is a Class C network (192.x.x.x), originally /24, borrowing 2 bits creates 2² = 4 subnets
- Subnet size = 64 addresses (256/4 = 64)
- Subnets: 0-63, 64-127, 128-191, 192-255
- First usable in 192.168.10.0/26 subnet: 192.168.10.1
- Last usable: 192.168.10.62

### Example 2: IPv6 Address Compression

**Problem:** Compress the following IPv6 address:
2001:0db8:0000:0000:0000:8a2e:0370:7334

**Solution:**
Step 1: Remove leading zeros from each hextet:
2001:db8:0:0:0:8a2e:370:7334

Step 2: Replace a single consecutive group of zeros with :::
2001:db8::8a2e:370:7334

This is the compressed form. Note that :: can only be used once.

### Example 3: IPv4 to IPv6 Address Mapping

**Problem:** Map the IPv4 address 192.168.1.100 to its IPv6 equivalent using the IPv4-mapped IPv6 address format.

**Solution:**
IPv4-mapped IPv6 addresses use the format ::ffff:xxxx:xxxx, where xxxx:xxxx represents the 32-bit IPv4 address in hexadecimal.

1. Convert each octet to hexadecimal:
   - 192 = C0
   - 168 = A8
   - 1 = 01
   - 100 = 64

2. Combine: C0A8:0164

3. Create IPv6-mapped address: ::ffff:C0A8:0164

Or fully expanded: 0000:0000:0000:0000:0000:ffff:C0A8:0164

## Exam Tips

1. **IPv4 Header Field Order:** Remember the exact sequence of IPv4 header fields—Version, IHL, TOS, Total Length, Identification, Flags, Fragment Offset, TTL, Protocol, Checksum, Source, Destination, Options.

2. **Maximum Transmission Unit (MTU):** IPv4 requires a minimum MTU of 68 bytes; routers can fragment packets. IPv6 requires minimum MTU of 1280 bytes and prohibits fragmentation by routers (only source can fragment).

3. **Private Address Ranges:** For exam questions, always identify whether an address is public or private. The three IPv4 private ranges are 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16.

4. **IPv6 Loopback:** Unlike IPv4's 127.0.0.1, IPv6 uses ::1 as the loopback address—memorize this distinction.

5. **Broadcast Elimination:** IPv6 eliminates broadcast completely; multicast serves all purposes that broadcast served in IPv4 (address resolution, router discovery).

6. **Fragmentation Differences:** IPv4 allows both routers and hosts to fragment; IPv6 allows only the source to fragment. This is a crucial distinction for troubleshooting.

7. **Header Checksum:** IPv4 has header checksum; IPv6 removed it because link-layer and transport-layer protocols handle error detection, improving router processing speed.

8. **Auto-configuration:** IPv6 hosts can auto-configure their addresses using Stateless Address Autoconfiguration (SLAAC) combined with Router Advertisement messages—no DHCP server required.

9. **Extension Headers:** IPv6 uses extension headers for optional functionality (routing, fragmentation, authentication, encryption), placed between the fixed header and upper-layer data.