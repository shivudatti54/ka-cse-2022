# IPv4 Datagram Header and Fragmentation


## Table of Contents

- [IPv4 Datagram Header and Fragmentation](#ipv4-datagram-header-and-fragmentation)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [IPv4 Datagram Header Structure](#ipv4-datagram-header-structure)
  - [IP Fragmentation](#ip-fragmentation)
  - [IPv4 Addressing](#ipv4-addressing)
- [Examples](#examples)
  - [Example 1: IPv4 Header Field Calculation](#example-1-ipv4-header-field-calculation)
  - [Example 2: TTL and Checksum Calculation](#example-2-ttl-and-checksum-calculation)
  - [Example 3: Fragment Offset Calculation](#example-3-fragment-offset-calculation)
- [Exam Tips](#exam-tips)

## Introduction

The Internet Protocol version 4 (IPv4) is the foundation of the Internet and remains the most widely used network layer protocol despite the emergence of IPv6. An IPv4 datagram is the fundamental unit of data transmission in TCP/IP networks, encapsulating data from the transport layer and enabling end-to-end communication across interconnected networks. Understanding the IPv4 datagram structure is crucial for computer science engineers as it forms the backbone of network communication and is a core topic in computer networks courses.

The IPv4 datagram consists of a header and the payload (data from upper layers). The header contains vital information for routing, delivery, and reassembly of fragmented packets. Each field in the IPv4 header serves a specific purpose, from identifying the source and destination addresses to controlling fragmentation and implementing quality of service mechanisms. Given that emphasizes practical and theoretical knowledge of networking protocols, a thorough understanding of IPv4 datagram structure and its fields is essential for both examination success and professional practice.

## Key Concepts

### IPv4 Datagram Header Structure

The IPv4 header is 20 bytes in its basic form and can extend to 60 bytes with options. The header fields are arranged in a specific order, and each field plays a critical role in packet delivery.

**Version (4 bits):** Indicates the IP version. For IPv4, this field contains the value 4. This field helps routers and hosts determine which version of the IP protocol to use for processing the datagram.

**Header Length (4 bits):** Specifies the length of the IP header in 32-bit words. The minimum value is 5 (20 bytes), and the maximum is 15 (60 bytes). This field is essential because the header may contain optional fields that increase its length.

**Type of Service (8 bits):** Also known as Differentiated Services Code Point (DSCP), this field indicates the quality of service parameters. It helps in prioritizing certain types of traffic (e.g., voice, video) over others. The field includes precedence bits (3 bits), delay flag, throughput flag, and reliability flag.

**Total Length (16 bits):** Specifies the total length of the IP datagram, including header and data, in bytes. The maximum size is 65,535 bytes (64 KB). This field is critical for reassembly at the destination.

**Identification (16 bits):** A unique identifier assigned to each datagram. This field is particularly important for fragmentation, where all fragments of the same original datagram carry the same identification value to enable reassembly at the destination.

**Flags (3 bits):** Three flags control fragmentation:

- Bit 0: Reserved (must be 0)
- Bit 1: Don't Fragment (DF) - when set, the datagram cannot be fragmented
- Bit 2: More Fragments (MF) - set to 1 for all fragments except the last one

**Fragment Offset (13 bits):** Indicates the position of the fragment in the original datagram. The offset is measured in 8-byte blocks, allowing for a maximum of 8,190 bytes of fragmentable data.

**Time to Live (8 bits):** Originally represented the maximum time (in seconds) a datagram can exist in the network. Now it serves as a hop count limit. Each router that processes the datagram decrements the TTL by at least 1. When TTL reaches 0, the datagram is discarded, preventing infinite looping.

**Protocol (8 bits):** Indicates the protocol of the upper layer. Common values include:

- 6: TCP
- 17: UDP
- 1: ICMP

**Header Checksum (16 bits):** A 16-bit one's complement checksum used for error detection in the header only. Each router recalculates this checksum because the TTL and possibly other fields change during transmission.

**Source IP Address (32 bits):** The IPv4 address of the sender.

**Destination IP Address (32 bits):** The IPv4 address of the intended recipient.

**Options (Variable):** Optional field that can be used for security, timestamp, record route, and source routing. When present, padding is added to make the header length a multiple of 32 bits.

### IP Fragmentation

Fragmentation is the process of breaking a large IP datagram into smaller fragments that can traverse networks with smaller Maximum Transmission Units (MTU). Each network link has a specific MTU that defines the maximum packet size it can handle.

**Why Fragmentation is Needed:** Different networks have different MTU values. For example, Ethernet typically has an MTU of 1500 bytes, while some WAN links may have MTUs of 576 bytes or lower. When a large datagram needs to pass through a network with a smaller MTU, it must be fragmented.

**Fragmentation Process:** When a router determines that the outgoing link has an MTU smaller than the incoming datagram and the DF flag is not set, it fragments the datagram. Each fragment becomes a separate IP packet with its own header, but they share the same identification value. The fragment offset field indicates where each fragment belongs in the original datagram.

**Reassembly:** Reassembly of fragments occurs only at the destination host, not at intermediate routers. This approach simplifies router operation and prevents reassembly attacks. The destination uses the identification, fragment offset, and MF flag to reassemble the original datagram correctly.

### IPv4 Addressing

IPv4 addresses are 32-bit numbers typically represented in dotted-decimal notation (e.g., 192.168.1.1). They are divided into classes:

- **Class A:** 1.0.0.0 to 126.255.255.255 (first bit 0)
- **Class B:** 128.0.0.0 to 191.255.255.255 (first two bits 10)
- **Class C:** 192.0.0.0 to 223.255.255.255 (first three bits 110)
- **Class D:** 224.0.0.0 to 239.255.255.255 (multicast)
- **Class E:** 240.0.0.0 to 255.255.255.255 (reserved)

**Special Addresses:**

- 0.0.0.0: This network
- 127.x.x.x: Loopback address
- 255.255.255.255: Limited broadcast

## Examples

### Example 1: IPv4 Header Field Calculation

**Problem:** An IPv4 datagram has a total length of 4000 bytes and needs to cross a link with MTU of 1500 bytes. Assuming no options in the header, calculate:
a) Number of fragments
b) Fragment sizes and offsets

**Solution:**

Given:

- Original datagram size: 4000 bytes
- Header size: 20 bytes (no options)
- Data size: 4000 - 20 = 3980 bytes
- MTU: 1500 bytes
- Maximum data per fragment: 1500 - 20 = 1480 bytes

Fragment 1:

- Data: 1480 bytes
- Offset: 0
- MF: 1
- Total size: 1500 bytes

Fragment 2:

- Data: 1480 bytes
- Offset: 1480/8 = 185
- MF: 1
- Total size: 1500 bytes

Fragment 3:

- Remaining data: 3980 - 2960 = 1020 bytes
- Data: 1020 bytes
- Offset: 2960/8 = 370
- MF: 0 (last fragment)
- Total size: 1020 + 20 = 1040 bytes

**Answer:** Total fragments = 3

### Example 2: TTL and Checksum Calculation

**Problem:** An IPv4 packet has TTL = 64 and Header Checksum = 0xABCD. After passing through one router, TTL becomes 63. Calculate the new Header Checksum using the incremental update method.

**Solution:**

When TTL decrements by 1 (from 64 to 63), only the TTL field changes. The old TTL value in the checksum computation was 0x40 (64 in decimal), and the new value is 0x3F (63 in decimal).

For incremental checksum update:

1. Compute one's complement of the old TTL: ~0x40 = 0xBF
2. Add to existing checksum: 0xABCD + 0xBF = 0xAC8C
3. Add carry back: 0xAC8C + 0x0001 = 0xAC8D
4. Take one's complement: ~0xAC8D = 0x5372

**Answer:** New Header Checksum = 0x5372

### Example 3: Fragment Offset Calculation

**Problem:** A host sends a 4000-byte datagram (including 20-byte header) with Identification = 0x1234 and MF = 0. The datagram passes through a network with MTU = 1000 bytes. Show the header fields for each fragment.

**Solution:**

Data size = 4000 - 20 = 3980 bytes
MTU = 1000 bytes
Max data per fragment = 1000 - 20 = 980 bytes

**Fragment 1:**

- Identification: 0x1234
- Offset: 0
- MF: 1
- Total Length: 1000 bytes

**Fragment 2:**

- Identification: 0x1234
- Offset: 980/8 = 122
- MF: 1
- Total Length: 1000 bytes

**Fragment 3:**

- Identification: 0x1234
- Offset: 1960/8 = 245
- MF: 1
- Total Length: 1000 bytes

**Fragment 4:**

- Identification: 0x1234
- Offset: 2940/8 = 367
- MF: 0
- Remaining data: 3980 - 2940 = 1040 bytes
- Total Length: 1040 + 20 = 1060 bytes

## Exam Tips

1. **Remember the IPv4 header length in bits:** Each of the 20 bytes is represented in 32-bit (4-byte) words. The IHL field value of 5 means 5 × 4 = 20 bytes.

2. **Fragment offset is in 8-byte units:** This is a common trick in exams. Remember that the offset field shows the position in terms of 8-byte blocks, not individual bytes.

3. **Identification field remains constant:** All fragments of the same original datagram carry the same identification value—this is crucial for reassembly at the destination.

4. **Don't Fragment flag prevents fragmentation:** If a datagram has DF = 1 and the MTU is too small, the router discards the packet and sends an ICMP "Destination Unreachable—Fragmentation Needed" message.

5. **TTL prevents infinite loops:** Each router decrements TTL by at least 1. When TTL reaches 0, the packet is discarded, preventing it from circulating indefinitely.

6. **Checksum is recalculated at each router:** Because fields like TTL change during routing, every router must recalculate the header checksum.

7. **Fragmentation happens at routers, reassembly at destination:** This is a key concept—only the final destination reassembles fragments, not intermediate routers.

8. **Maximum datagram size is 65,535 bytes:** The 16-bit Total Length field can represent values from 0 to 65,535, but a value of 0 is not used.
