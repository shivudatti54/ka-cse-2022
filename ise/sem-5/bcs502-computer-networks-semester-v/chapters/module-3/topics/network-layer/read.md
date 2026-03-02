# Network Layer Services and IPv4

## Introduction

The Network Layer is the third layer of the OSI model and is responsible for routing data between different networks. It provides logical addressing, routing, and congestion control. In this chapter, we will discuss the services provided by the Network Layer and the basics of IPv4.

## Network Layer Services

The Network Layer provides the following services:

- **Connectionless Service**: In this service, each packet is treated as an independent entity and is routed separately. There is no guarantee of delivery or order of packets.
- **Connection-Oriented Service**: In this service, a connection is established between the sender and receiver before data is sent. The packets are delivered in the order they were sent.
- **Reliable Service**: In this service, the Network Layer guarantees that the packets will be delivered to the destination without errors.
- **Unreliable Service**: In this service, the Network Layer does not guarantee that the packets will be delivered to the destination without errors.

## IPv4

IPv4 is a connectionless protocol that provides logical addressing and routing. It uses 32-bit addresses, which are divided into five classes: A, B, C, D, and E.

### IPv4 Address Format

The IPv4 address format is as follows:

```
+---------------+---------------+---------------+---------------+
|  Class A     |  Class B     |  Class C     |  Class D     |
+---------------+---------------+---------------+---------------+
|  0   |  1   |  2   |  3   |  4   |  5   |  6   |  7   |
+---------------+---------------+---------------+---------------+
```

- **Class A**: The first bit is 0, and the next 7 bits are the network ID. The remaining 24 bits are the host ID.
- **Class B**: The first two bits are 10, and the next 14 bits are the network ID. The remaining 16 bits are the host ID.
- **Class C**: The first three bits are 110, and the next 21 bits are the network ID. The remaining 8 bits are the host ID.
- **Class D**: The first four bits are 1110, and the remaining 28 bits are the multicast address.
- **Class E**: The first five bits are 11110, and the remaining 27 bits are reserved for future use.

### IPv4 Datagram Format

The IPv4 datagram format is as follows:

```
+---------------+---------------+---------------+---------------+
|  Version    |  Header Length|  Type of Service|  Total Length|
+---------------+---------------+---------------+---------------+
|  Identification|  Flags       |  Fragment Offset|
+---------------+---------------+---------------+---------------+
|  Time to Live |  Protocol    |  Header Checksum|
+---------------+---------------+---------------+---------------+
|  Source IP Address|
+---------------+---------------+---------------+---------------+
|  Destination IP Address|
+---------------+---------------+---------------+---------------+
|  Options      |  Padding     |
+---------------+---------------+---------------+---------------+
|  Data         |
+---------------+---------------+---------------+---------------+
```

- **Version**: The version of the IP protocol.
- **Header Length**: The length of the IP header.
- **Type of Service**: The type of service required.
- **Total Length**: The total length of the datagram.
- **Identification**: The identification number of the datagram.
- **Flags**: The flags that indicate whether the datagram can be fragmented.
- **Fragment Offset**: The offset of the fragment in the original datagram.
- **Time to Live**: The time to live of the datagram.
- **Protocol**: The protocol used in the datagram.
- **Header Checksum**: The checksum of the IP header.
- **Source IP Address**: The source IP address.
- **Destination IP Address**: The destination IP address.
- **Options**: The options used in the datagram.
- **Padding**: The padding used to make the header a multiple of 4 bytes.
- **Data**: The data carried by the datagram.

## Routing Algorithms

Routing algorithms are used to determine the best path for forwarding packets between networks. There are two types of routing algorithms:

- **Static Routing**: In this algorithm, the routing table is manually configured and does not change.
- **Dynamic Routing**: In this algorithm, the routing table is automatically updated based on changes in the network.

## Exam Tips

- Understand the services provided by the Network Layer.
- Know the IPv4 address format and the different classes of addresses.
- Understand the IPv4 datagram format and the different fields in the header.
- Know the different types of routing algorithms and how they work.
