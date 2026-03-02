# **Datagram, Introduction to Routing Algorithms, Unicast Routing Protocols**

## **I. Datagram**

- A datagram is a self-contained unit of data transmitted over a network, such as the internet.
- It is similar to a packet, but does not contain a header with routing information.
- Datagram is a best-effort delivery, meaning it will not be guaranteed to reach its destination.

## **II. Introduction to Routing Algorithms**

- Routing algorithms determine the best path for data to travel from the source to the destination.
- Types of routing algorithms:
  - Static routing
  - Dynamic routing

## **III. Unicast Routing Protocols**

### A. Distance-Vector Routing Protocols

- **DVR (Distance-Vector Routing Protocol)**: uses distance-vector routing algorithm to compute the shortest path.
- **LSR (Link-State Routing Protocol)**: uses link-state routing algorithm to compute the shortest path.

### B. Link-State Routing Protocols

- **PVR (Path-Vector Routing Protocol)**: uses path-vector routing algorithm to compute the shortest path.

### C. Unicast Routing Protocols

- **RIP (Routing Information Protocol)**: a distance-vector routing protocol used for internal routing.
- **OSPF (Open Shortest Path First)**: a link-state routing protocol used for external routing.
- **BGP (Border Gateway Protocol)**: a distance-vector routing protocol used for inter-autonomous system routing.

## **IV. Important Formulas and Definitions**

- **Bellman-Ford Algorithm**: a dynamic routing algorithm used for link-state routing.
- **Dijkstra's Algorithm**: a dynamic routing algorithm used for link-state routing.
- **Routing Table**: a table used to store the shortest paths from the source to all destinations.
- **Neighbor**: a router that shares a link with the current router.
- **Shortest Path First (SPF)**: a routing algorithm used to compute the shortest path.

## **V. Theorems**

- **Theorem 1**: A routing protocol should be able to handle route flapping and route convergence.
- **Theorem 2**: A routing protocol should be able to handle network topology changes.

This summary is a concise revision guide for the topic of datagram, introduction to routing algorithms, and unicast routing protocols. It covers key points, formulas, definitions, and theorems in bullet format, making it perfect for quick revision before exams.
