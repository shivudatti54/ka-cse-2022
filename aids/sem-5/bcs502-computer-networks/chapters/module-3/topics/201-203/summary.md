# **20.1-20.3: Network Layer Services, Packet Switching, IPv4 Address, IPv4 Datagram, IPv6**

### Key Concepts

- **Network Layer Services**
  - Connectionless vs Connection-Oriented
  - Reliable vs Unreliable
  - Error Detection and Correction

- **Packet Switching**
  - Packet Format: Source IP, Destination IP, Header, Payload
  - Routing: Determining the path for a packet to reach its destination
  - Forwarding: Passing packets between routers

- **IPv4 Address**
  - Address Format: XXX.XXX.XXX.XXX
  - Address Classes: A, B, C, D, E
  - Subnetting: Dividing an IP address into smaller networks

- **IPv4 Datagram**
  - Datagram Format: Source IP, Destination IP, Header, Option, payload
  - IP Header: Version, Header Length, Type of Service, Total Length, ID
  - IP Options: Routing, Fragmentation, Redirection

- **IPv6**
  - Address Format: XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX
  - Address Classes: Global, Unique Local, Link-Local, Hierarchical
  - IPv6 Header: Version, Header Length, Traffic Class, Flow Label, Fragment Offset

### Important Formulas and Definitions

- **Routing Table Entry**
  - Destination Network Address
  - Next-hop Router IP Address
  - Metric (Cost) to reach the next-hop router

- **IPv4 MTU**
  - Maximum Transmission Unit: The maximum size of a packet that can be transmitted over a network

- **Fragmentation**
  - Breaking down a large packet into smaller packets to ensure safe transmission

- **Hops**
  - The number of times a packet is forwarded between routers to reach its destination.

- **Theorem:**
  - The Network Layer Theorem: A packet is forwarded to its next hop based on the best available path.
