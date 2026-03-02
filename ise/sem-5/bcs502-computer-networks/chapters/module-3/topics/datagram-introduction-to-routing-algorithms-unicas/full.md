# **Datagram, Introduction to Routing Algorithms, Unicast Routing Protocols**

## **Table of Contents**

1. [Datagram](#datagram)
2. [Introduction to Routing Algorithms](#introduction-to-routing-algorithms)
3. [Unicast Routing Protocols](#unicast-routing-protocols)
   - [DVR (Destination-Dependent Routing)](#dvr-destination-dependent-routing)
   - [LSR (Link-State Routing)](#lsr-link-state-routing)
   - [PVR (Path-Vector Routing)](#pvr-path-vector-routing)
   - [Unicast Routing Protocols: RIP (Routing Information Protocol)](#unicast-routing-protocol-rip-routing-information-protocol)
   - [Unicast Routing Protocols: OSPF (Open Shortest Path First)](#unicast-routing-protocol-ospf-open-shortest-path-first)
   - [Unicast Routing Protocols: BGP (Border Gateway Protocol)](#unicast-routing-protocol-bgp-border-gateway-protocol)
4. [Multicasting Routing](#multicasting-routing)

## **Datagram**

A datagram is a self-contained, packet-switched message that is transmitted between devices on a network. It is essentially a small packet of data that carries a header with information about the packet, such as its source and destination addresses, protocol, and sequence number.

### Characteristics of a Datagram

- Self-contained: A datagram is a complete packet of data that contains everything needed to deliver it to its destination.
- Packet-switched: Datagram transmission uses packet switching, where the data is broken into small packets and transmitted independently.
- Header information: The header contains information about the packet, such as source and destination addresses, protocol, and sequence number.

### Types of Datagram

- **IP datagrams**: Used in the Internet Protocol (IP) suite of protocols.
- **UDP datagrams**: Used in the User Datagram Protocol (UDP) suite of protocols, which is often used for applications that require fast and reliable delivery.

### Datagram Header

A datagram header typically consists of the following fields:

- Source IP address
- Destination IP address
- Protocol number (e.g., TCP, UDP, ICMP)
- Sequence number
- Datagram length

### Example Datagram Header

```
Hexadecimal   ASCII   Description
ffffffff   0xff   Destination IP address
00000000   0x00   Source IP address
00000006   0x06   Protocol number (UDP)
00000000   0x00   Sequence number
00000004   0x04   Datagram length
```

## **Introduction to Routing Algorithms**

Routing algorithms are used to determine the best path for forwarding packets between devices on a network. There are several types of routing algorithms, including unicast routing protocols and multicasting routing protocols.

### Types of Routing Algorithms

- **Unicast routing algorithms**: Used for unicast routing, which involves forwarding packets between a single sender and receiver.
- **Multicast routing algorithms**: Used for multicast routing, which involves forwarding packets to multiple receivers.

## **Unicast Routing Protocols**

Unicast routing protocols are used for unicast routing, which involves forwarding packets between a single sender and receiver.

### DVR (Destination-Dependent Routing)

DVR is a routing protocol that uses the destination IP address to determine the best path for forwarding packets. It is not commonly used today.

### LSR (Link-State Routing)

LSR is a routing protocol that uses link-state information to determine the best path for forwarding packets. It is used in some network protocols, such as the Intermediate System to Intermediate System (IS-IS) protocol.

### PVR (Path-Vector Routing)

PVR is a routing protocol that uses path-vector information to determine the best path for forwarding packets. It is used in some network protocols, such as the Path-Vector Routing (PVR) protocol.

### Unicast Routing Protocols: RIP (Routing Information Protocol)

RIP is a distance-vector routing protocol that uses hop count information to determine the best path for forwarding packets. It is a simple and intuitive protocol, but it is not very scalable.

### Unicast Routing Protocols: OSPF (Open Shortest Path First)

OSPF is an interior gateway protocol (IGP) that uses link-state information to determine the best path for forwarding packets. It is used in many network protocols, such as the Internet Protocol (IP) suite of protocols.

### Unicast Routing Protocols: BGP (Border Gateway Protocol)

BGP is an exterior gateway protocol (EGP) that uses path-vector information to determine the best path for forwarding packets. It is used in many network protocols, such as the Internet Protocol (IP) suite of protocols.

## **Multicasting Routing**

Multicasting routing is used for multicast routing, which involves forwarding packets to multiple receivers.

### Types of Multicasting Routing

- **Source-based multicasting**: The source of the multicast broadcast is specified in the multicast packet.
- **Sourcing multicasting**: The source of the multicast broadcast is dynamically determined.

### Multicast Routing Protocols

- **IGMP (Internet Group Management Protocol)**: Used for source-based multicasting.
- **PIM (Protocol Independent Multicast)**: Used for sourcing multicasting.

## **Case Studies and Applications**

- **Internet Protocol (IP) suite of protocols**: RIP, OSPF, BGP, and others are used in the IP suite of protocols.
- **Network protocols**: LSR, PVR, and others are used in network protocols such as IS-IS and PVR.
- **Application protocols**: IGMP and PIM are used in application protocols such as video conferencing and online gaming.

## **Historical Context and Modern Developments**

- **ARPANET**: The ARPANET network used the IP suite of protocols, including RIP and OSPF.
- **Internet Protocol (IP) suite of protocols**: RIP, OSPF, BGP, and others are used in the IP suite of protocols.
- **Network protocols**: LSR, PVR, and others are used in network protocols such as IS-IS and PVR.
- **Application protocols**: IGMP and PIM are used in application protocols such as video conferencing and online gaming.

## **Diagrams and Descriptions**

Here are some diagrams and descriptions of the routing protocols:

- **DVR**: The DVR protocol uses the destination IP address to determine the best path for forwarding packets.

```
+---------------+
|  Destination  |
|  IP Address   |
+---------------+
         |
         |
         v
+---------------+
|  DVR Router  |
|  (DVR)       |
+---------------+
         |
         |
         v
+---------------+
|  Forwarding   |
|  Table       |
+---------------+
```

- **LSR**: The LSR protocol uses link-state information to determine the best path for forwarding packets.

```
+---------------+
|  Link-State  |
|  Database    |
+---------------+
         |
         |
         v
+---------------+
|  LSR Router  |
|  (LSR)       |
+---------------+
         |
         |
         v
+---------------+
|  Forwarding   |
|  Table       |
+---------------+
```

- **PVR**: The PVR protocol uses path-vector information to determine the best path for forwarding packets.

```
+---------------+
|  Path-Vector  |
|  Database     |
+---------------+
         |
         |
         v
+---------------+
|  PVR Router  |
|  (PVR)       |
+---------------+
         |
         |
         v
+---------------+
|  Forwarding   |
|  Table       |
+---------------+
```

## **Further Reading**

- **"Computer Networks"** by Andrew S. Tanenbaum and David J. Wetherall
- **"Routing in the Internet"** by Jeffrey C. Herzberg
- **"Multicast Routing Protocols"** by W. Brian Cox and John D. Thomson
