# Network Layer Protocols: IPv4 and IPv6

## Introduction

The Network Layer (Layer 3) handles logical addressing and routing of packets across different networks. IPv4 (Internet Protocol version 4) has been the dominant protocol, but IPv6 (Internet Protocol version 6) was developed to address IPv4's limitations. Understanding both protocols is essential for the Delhi University BSc (Hons) Computer Science NEP 2024 syllabus.

---

## IPv4 (Internet Protocol Version 4)

- **Addressing**: Uses 32-bit addresses, providing approximately 4.3 billion unique addresses (e.g., 192.168.1.1)
- **Classes**: Class A, B, C (unicast), Class D (multicast), Class E (reserved)
- **Packet Format**: Header contains Version (4), IHL, TOS, Total Length, Identification, Flags, Fragment Offset, TTL, Protocol, Header Checksum, Source/Destination Address
- **Fragmentation**: Routers can fragment packets exceeding MTU; reassembly only at destination
- **Subnetting & CIDR**: Divide networks into subnets; CIDR (Classless Inter-Domain Routing) uses variable-length subnet masks
- **Private Addresses**: 10.0.0.0-10.255.255.255, 172.16.0.0-172.31.255.255, 192.168.0.0-192.168.255.255
- **NAT (Network Address Translation)**: Maps private to public addresses

### Supporting Protocols

- **ICMP (Internet Control Message Protocol)**: Error reporting and diagnostics (ping, traceroute)
- **ARP (Address Resolution Protocol)**: Maps IP to MAC addresses
- **RARP (Reverse ARP)**: Maps MAC to IP addresses
- **DHCP (Dynamic Host Configuration Protocol)**: Auto-assigns IP addresses

---

## IPv6 (Internet Protocol Version 6)

- **Addressing**: Uses 128-bit addresses, virtually unlimited (e.g., 2001:0db8:85a3::8a2e:0370:7334)
- **Packet Format**: Simplified header (40 bytes) with Version, Traffic Class, Flow Label, Payload Length, Next Header, Hop Limit, Source/Destination Addresses
- **No Fragmentation**: Source performs Path MTU Discovery; routers do not fragment
- **No Header Checksum**: Reduces processing overhead
- **Auto-configuration**: Stateless Address Auto-configuration (SLAAC)
- **Security**: Built-in IPsec support
- **QoS (Quality of Service)**: Flow label field for packet classification
- **Anycast**: One-to-nearest communication

---

## IPv4 vs IPv6: Key Differences

| Feature | IPv4 | IPv6 |
|---------|------|------|
| Address Size | 32-bit | 128-bit |
| Header Size | Variable (20-60 bytes) | Fixed (40 bytes) |
| Fragmentation | Router & Destination | Source only |
| checksum | Present | Removed |
| Options | Yes | No (Extension Headers) |
| Address Configuration | DHCP/Manual | SLAAC/DHCPv6 |
| Broadcast | Yes | No (Multicast used) |

---

## Conclusion

IPv4 remains widely used but faces address exhaustion. IPv6 offers expanded address space, enhanced security, and improved efficiency. The transition from IPv4 to IPv6 is gradual, requiring knowledge of both protocols for network administration and design—a crucial topic for Delhi University examinations.