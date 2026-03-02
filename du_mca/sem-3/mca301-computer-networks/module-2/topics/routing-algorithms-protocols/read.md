# Routing Algorithms & Protocols

## Introduction
Routing algorithms form the backbone of modern computer networks, determining optimal data paths between source and destination. In the context of DU's MCA program, understanding these algorithms is crucial for designing efficient networks and troubleshooting real-world systems. 

Routing protocols implement these algorithms through standardized communication mechanisms. The evolution from static routing (manual configuration) to dynamic protocols like OSPF and BGP has enabled the Internet's scalability, handling over 1.2 zettabytes of annual global traffic.

These concepts gain special significance in India's digital infrastructure landscape, where protocols like BGP manage traffic between 900+ Internet Service Providers. Recent developments like SDN (Software-Defined Networking) and IoT networks demand advanced routing strategies, making this knowledge essential for MCA graduates targeting roles in network engineering and cloud infrastructure.

## Key Concepts
1. **Distance Vector Algorithms**: 
   - Uses Bellman-Ford equation: D(x,y) = min{v}[c(x,v) + D(v,y)]
   - Periodic updates to neighbors (e.g., RIP updates every 30s)
   - Count-to-infinity problem mitigation via split horizon

2. **Link State Algorithms**:
   - Dijkstra's algorithm constructs shortest path tree
   - OSPF uses flooding for LSDB (Link State Database) synchronization
   - Areas and backbone design in enterprise networks

3. **Path Vector Protocols**:
   - BGP's AS_PATH attribute prevents loops
   - Policy-based routing between autonomous systems
   - Route aggregation and MED (Multi-Exit Discriminator)

4. **Convergence Metrics**:
   - Time complexity: OSPF (O(n log n)) vs RIP (O(n))
   - Message complexity comparison
   - Fast reroute mechanisms in modern implementations

5. **Hybrid Protocols**:
   - EIGRP's DUAL (Diffusing Update Algorithm)
   - Feasible successor concept
   - Reliable Transport Protocol (RTP) for updates

## Examples

**Example 1: Dijkstra's Algorithm**
```
Network topology:
Nodes: A-B(2), A-C(5), B-C(1), B-D(3), C-D(2)
Find shortest path from A to D.

Step 1: Initialize distances (A=0, others=∞)
Step 2: Process A → B(2), C(5)
Step 3: Process B → C(2+1=3 < 5), D(2+3=5)
Step 4: Process C → D(3+2=5)
Step 5: Two equal paths (A-B-D and A-B-C-D), select based on hop count
Final path: A-B-D (cost 5)
```

**Example 2: BGP Path Selection**
```
Available routes:
1. AS_PATH: 64500 64501 (MED=50)
2. AS_PATH: 64500 64502 64501 (MED=40)
3. AS_PATH: 64500 64503 (LocalPref=200)

Selection process:
1. Highest LocalPref (route 3) 
2. Shortest AS_PATH (route 1 vs 3)
3. Lowest MED (not applicable here)
Selected route: 3 (LocalPref override)
```

**Example 3: RIP Convergence**
```
Initial state:
A-B-C with metric 1 each
Link B-C fails:
- B marks C as unreachable (metric 16)
- A receives B's update after 30s
- A recalculates: min(current 2, B's 16+1) → 17
Full convergence in 180s (6 update cycles)
```

## Exam Tips
1. Always mention time complexities when comparing algorithms
2. For OSPF, remember the 3-way handshake process for adjacency formation
3. In BGP questions, list decision steps in exact order (LocalPref > AS_PATH > MED)
4. When explaining count-to-infinity, draw at least 3 node diagrams
5. For SDN-related questions, contrast traditional routing with OpenFlow's centralized control
6. In numerical problems, show intermediate steps for partial credit
7. Memorize IANA protocol numbers: OSPF=89, BGP=179, RIP=520