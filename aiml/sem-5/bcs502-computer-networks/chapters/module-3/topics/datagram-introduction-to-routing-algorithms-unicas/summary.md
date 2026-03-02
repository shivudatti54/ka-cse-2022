# **Datagram, Introduction to Routing Algorithms, Unicast Routing Protocols**

## **Key Points**

### Datagram

- A datagram is a single communication packet that contains the entire data and control information of a message.
- Datagram is broadcast to all destinations in a network.
- It does not guarantee delivery of packets.

### Introduction to Routing Algorithms

- Routing algorithms are used to determine the best path for forwarding packets between nodes in a network.
- Routing algorithms can be categorized into two types: unicast and multicast.

### Unicast Routing Protocols

#### Unicast Routing Protocols: DVR, LSR, PVR

- **DVR (Destination-Independent Routing)**: A routing protocol that does not consider the destination of the packet while making routing decisions.
- **LSR (Link-State Routing)**: A routing protocol that uses a link-state database to make routing decisions.
- **PVR (Path-Vector Routing)**: A routing protocol that uses path vectors to make routing decisions.

#### Unicast Routing protocols: RIP, OSPF, BGP

- **RIP (Routing Information Protocol)**: A distance-vector routing protocol that uses hop count as the metric.
- **OSPF (Open Shortest Path First)**: A link-state routing protocol that uses the Dijkstra's algorithm to find the shortest path.
- **BGP (Border Gateway Protocol)**: A path-vector routing protocol that is used for inter-autonomous system routing.

**Formulas and Definitions**

- **Hop count**: The number of routers a packet must traverse to reach its destination.
- **Metric**: A measure of the cost or overhead of a link.
- **Link-state advertisement**: A message sent by a router to its neighbors to describe its link state.

**Theorems and Concepts**

- **Theorem of the minimum distance**: A packet will always take the route with the minimum distance to reach its destination.
- **Breadth-first search**: A traversal algorithm used to find a path in a network.

Note: This summary is a concise revision guide and is not intended to be a comprehensive study guide.
