# Interconnection Networks in Parallel Processing

=====================================

### Overview

Interconnection networks are the communication backbone of parallel computing systems, enabling data exchange between processors, memory modules, and I/O devices. The choice of network topology directly impacts system latency, bandwidth, scalability, and overall performance.

### Key Points

- **Key Metrics:** Latency (message travel time), Bandwidth (max data rate), Bisection Bandwidth (min bandwidth between two halves), Diameter (max shortest path between any two nodes).
- **Static vs Dynamic:** Static networks have fixed connections (mesh, ring, hypercube); dynamic networks can be reconfigured (crossbar, multistage).
- **Bus:** Simple, inexpensive, but limited bandwidth and poor scalability; single shared pathway.
- **Ring:** Circular connections with predictable latency; simple but vulnerable to single breaks.
- **2D Mesh:** Grid-like structure with good scalability; diameter = 2(sqrt(N)-1), degree = 4.
- **Hypercube:** n-dimensional cube with 2^n nodes; diameter = log2(N), high connectivity but complex wiring.
- **Crossbar:** Non-blocking switch connecting any input to any output; O(N^2) cost, difficult to scale.
- **Multistage Networks (MINs):** Multiple stages of smaller switches (Omega, butterfly); more scalable than crossbar but may be blocking.

### Important Concepts

- Performance comparison: Bus (degree 1, diameter 1), Ring (degree 2, diameter N/2), Mesh (degree 4, diameter 2(sqrt(N)-1)), Hypercube (degree log2(N), diameter log2(N))
- Routing techniques: deterministic (fixed path), adaptive (dynamic path), minimal (shortest), non-minimal (avoids congestion)
- Switching: circuit switching (dedicated path), packet switching (independent packets), wormhole routing (hybrid, low latency)
- Real-world: IBM Blue Gene (3D torus), Intel Xeon Phi (mesh), Intel Core (ring bus)

### Notes

- Focus on diameter and bisection bandwidth as critical metrics for evaluating network performance in exams.
- Know the formulas for degree, diameter, and bisection width of common topologies (bus, ring, mesh, hypercube).
- Be prepared to compare topologies and explain when each is appropriate based on cost, scalability, and performance trade-offs.
