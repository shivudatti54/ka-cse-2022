# IP Addressing & Subnetting

## Introduction
IP addressing and subnetting form the backbone of modern network design. IPv4 (Internet Protocol version 4) uses 32-bit addresses to uniquely identify devices on a network, while IPv6 employs 128-bit addresses to address IPv4 exhaustion. Subnetting allows efficient utilization of IP addresses by dividing large networks into smaller, manageable sub-networks.

With the exponential growth of IoT devices and cloud infrastructure, proper subnetting ensures optimal routing, reduced network congestion, and enhanced security through segmentation. Enterprises like Airtel and Jio use advanced subnetting strategies to manage millions of subscribers while maintaining QoS.

This topic is critical for network engineers designing enterprise networks, cloud infrastructure, and IoT systems. DU's MCA program emphasizes practical implementation through Cisco Packet Tracer and Wireshark analysis.

## Key Concepts
1. **IPv4 Addressing**
   - 32-bit address (4 octets) in dotted-decimal notation (e.g., 192.168.1.1)
   - Classful addressing (A, B, C, D, E) vs Classless (CIDR)
   - Private ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16

2. **Subnet Mask**
   - 32-bit number separating network and host portions
   - /24 = 255.255.255.0 in dotted-decimal

3. **CIDR Notation**
   - Classless Inter-Domain Routing (e.g., 192.168.1.0/26)
   - Enables Variable Length Subnet Masking (VLSM)

4. **Subnetting Process**
   - Determine required subnets/hosts
   - Calculate subnet bits: 2^n ≥ required subnets
   - Calculate host bits: 2^h - 2 ≥ required hosts

5. **IPv6 Addressing**
   - 128-bit hexadecimal (e.g., 2001:0db8:85a3::8a2e:0370:7334)
   - Simplified notation with :: compression

## Examples
**Example 1: Class C Subnetting**
Problem: Divide 192.168.1.0/24 into 4 subnets with equal hosts.

Solution:
1. Required subnets = 4 → 2^2 = 4 → borrow 2 bits
2. New subnet mask: /24 + 2 = /26 (255.255.255.192)
3. Subnet ranges:
   - 192.168.1.0/26 (1-62)
   - 192.168.1.64/26 (65-126)
   - 192.168.1.128/26 (129-190)
   - 192.168.1.192/26 (193-254)

**Example 2: VLSM Implementation**
Problem: Allocate 172.16.0.0/16 for: 
- 10 subnets with 1000 hosts each
- 20 subnets with 50 hosts each

Solution:
1. Large subnets: 1000 hosts → 2^10=1024 → /22 mask (32-10=22)
2. Small subnets: 50 hosts → 2^6=64 → /26 mask
3. Hierarchical allocation prevents address waste

**Example 3: IPv6 Shortening**
Problem: Abbreviate 2001:0db8:0000:0000:0000:ff00:0042:8329

Solution:
1. Remove leading zeros: 2001:db8:0:0:0:ff00:42:8329
2. Compress consecutive zeros with :: 
3. Final: 2001:db8::ff00:42:8329

## Exam Tips
1. Always subtract 2 for network/broadcast addresses in host calculation
2. For quick binary conversion: 128 64 32 16 8 4 2 1 (for each octet)
3. CIDR to dotted-decimal: /25 = 128, /26 = 192, /27 = 224, etc.
4. IPv6 shorthand rules: 
   - Remove leading zeros in each hextet
   - Replace longest consecutive zero sequence with ::
5. Practice network design problems using VLSM
6. Remember special addresses:
   - 127.0.0.1 (loopback)
   - 169.254.x.x (APIPA)
   - 255.255.255.255 (limited broadcast)
7. In subnetting questions, always show your bit-wise calculations