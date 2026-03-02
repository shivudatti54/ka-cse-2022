# \*\*20.1 Network Layer Services

### Overview

The network layer, also known as the internet layer, is the fourth layer of the OSI model. It provides various services to ensure efficient and reliable communication between devices on different networks.

### Network Layer Services

- **Routing**: The network layer is responsible for routing packets between different networks. It uses routing tables to determine the best path for packet forwarding.
- **Fragmentation**: If a packet is larger than the maximum size of a link layer frame, it is fragmented into smaller packets at the source node.
- **Reassembly**: The receiving node reassembles the fragmented packets into the original packet at the application layer.
- **Source Routing**: The source node specifies the path that the packet should take through the network.
- **Quality of Service (QoS)**: The network layer provides QoS features to ensure that packets are delivered in a timely and reliable manner.

### Network Layer Protocols

- **IP (Internet Protocol)**: IP is the primary protocol used at the network layer. It provides connectivity between nodes on different networks and is the foundation of the internet.
- **IGMP (Internet Group Management Protocol)**: IGMP is used to manage multicast groups and allows devices to join or leave a multicast group dynamically.
- **RIP (Routing Information Protocol)**: RIP is a distance-vector routing protocol used to exchange routing information between nodes on a network.

# \*\*20.2 Packet Switching

### Overview

Packet switching is a technique used in the network layer to transmit data in small packets. Each packet contains the destination address and other relevant information.

### How Packet Switching Works

- **Packet Creation**: The application layer breaks down data into small packets and assigns a header to each packet.
- **Packet Switching**: Each packet is transmitted through the network, where it is routed to its destination node.
- **Packet Reassembly**: The receiving node reassembles the packets into the original data at the application layer.

### Types of Packet Switching

- **Store-and-Forward**: In this method, each node stores a packet until it receives an acknowledgment from the next node.
- **Cut-Through**: In this method, each node forwards a packet without waiting for an acknowledgment.

# \*\*20.3 IPv4 Addressing and Datagram

### Overview

IPv4 (Internet Protocol version 4) is a protocol used for addressing devices on the internet. It uses a 32-bit address to uniquely identify each device.

### IPv4 Addressing

- **Classful Addressing**: In this method, IP addresses were divided into five classes based on the number of bits used in the network and host parts of the address.
- **Classless Addressing**: In this method, IP addresses are assigned without a class, and the network and host parts of the address can be of any size.

### IPv4 Datagram

- **Datagram Structure**: A datagram consists of a header and a payload. The header contains the source and destination addresses, as well as other relevant information.
- **Datagram Size**: The size of a datagram is determined by the size of the header and the payload.

### IPv4 Header Format

| Field                          | Length  | Description             |
| ------------------------------ | ------- | ----------------------- |
| Version                        | 4 bits  | Version number          |
| Header Length                  | 4 bits  | Header length           |
| Differentiated Services (DSCP) | 6 bits  | Differentiated services |
| Total Length                   | 16 bits | Total length            |
| Identification                 | 16 bits | Identification number   |
| Flags                          | 3 bits  | Flags (e.g., DF, MF)    |
| Fragment Offset                | 13 bits | Fragment offset         |
| TTL                            | 8 bits  | Time to live            |
| Protocol                       | 8 bits  | Protocol number         |
| Header Checksum                | 16 bits | Header checksum         |
| Source IP Address              | 32 bits | Source IP address       |
| Destination IP Address         | 32 bits | Destination IP address  |

Note: This is a basic overview of the topics and is not exhaustive. For a more detailed study, refer to the official documentation and other reliable sources.
