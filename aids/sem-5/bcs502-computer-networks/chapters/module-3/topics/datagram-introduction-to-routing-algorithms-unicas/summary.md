# **Datagram, Introduction to Routing Algorithms, Unicast Routing Protocols**

### Datagram

- A Datagram is a self-contained packet of data that is transmitted independently of the reliability of the network.
- It is a best-effort delivery, meaning that it is not guaranteed to reach its destination.
- Characteristics:
  - No error detection or correction
  - No acknowledgement from the receiver
  - Routing tables are used to forward packets

### Introduction to Routing Algorithms

- A routing algorithm is used to determine the best path for forwarding packets between nodes in a network.
- Routing algorithms take into account factors such as network topology, traffic volume, and link costs.

### Unicast Routing Protocols

#### Distance-Vector Routing Protocols (DVR)

- DVRs maintain a distance vector that represents the minimum hop count to reach each destination.
- Protocols:
  - RIP (Routing Information Protocol)
  - PVR (Primarily Ventilated Routing)

#### Link-State Routing Protocols (LSR)

- LSRs use a link-state database to represent the network topology.
- Protocols:
  - OSPF (Open Shortest Path First)

#### Path-Vector Routing Protocols (PVR)

- PVRs use a path vector to represent the best path to reach each destination.
- Protocols:
  - BGP (Border Gateway Protocol)

#### Multicasting Routing

- Multicasting allows multiple receivers to share the same transmission.
- Protocols:
  - IGMP (Internet Group Management Protocol)
  - PIM (Protocol Independent Multicast)

### Important Formulas and Definitions

- **Hop limit:** The maximum number of hops allowed for a packet to travel before it is discarded.
- **Routing table entry:** A record in the routing table that specifies the next hop to reach a destination.
- **Metric:** A numerical value used to weigh the importance of a link in the routing algorithm.

### Important Theorems

- **Theorem 1:** The shortest path is always the minimum-weight path.
- **Theorem 2:** The routing algorithm that minimizes the sum of link costs will result in the shortest path.

### Key Concepts

- Routing algorithms
- Routing protocols
- Network topology
- Link state vs distance vector routing
