# Introduction to Routing Algorithms


## Table of Contents

- [Introduction to Routing Algorithms](#introduction-to-routing-algorithms)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Routing vs. Forwarding](#1-routing-vs-forwarding)
  - [2. Classification of Routing Algorithms](#2-classification-of-routing-algorithms)
  - [3. Dijkstra's Shortest Path Algorithm](#3-dijkstras-shortest-path-algorithm)
  - [4. Distance Vector Routing](#4-distance-vector-routing)
  - [5. Link State Routing](#5-link-state-routing)
  - [6. Path Vector Routing](#6-path-vector-routing)
  - [7. Routing Metrics](#7-routing-metrics)
  - [8. Hierarchical Routing](#8-hierarchical-routing)
- [Examples](#examples)
  - [Example 1: Dijkstra's Algorithm Application](#example-1-dijkstras-algorithm-application)
  - [Example 2: Distance Vector Routing Simulation](#example-2-distance-vector-routing-simulation)
  - [Example 3: Analyzing Routing Algorithm Choice](#example-3-analyzing-routing-algorithm-choice)
- [Exam Tips](#exam-tips)

## Introduction

Routing algorithms are fundamental components of network layer protocols that determine the optimal path for data packets to travel from source to destination across interconnected networks. In modern computer networks, efficient routing is crucial for ensuring timely delivery of data, minimizing network congestion, and maximizing resource utilization. Whether it's a small local area network or the vast global internet, routing algorithms enable devices to communicate by finding the most efficient paths through complex network topologies.

The study of routing algorithms becomes essential as networks grow in scale and complexity. With millions of interconnected devices, the challenge of finding optimal paths while adapting to dynamic network conditions has led to the development of numerous routing algorithms, each with its own strengths and limitations. Understanding these algorithms is vital for network engineers and computer science professionals who design, implement, and manage network infrastructure.

In the context of 's Computer Science and Engineering curriculum, this topic forms the backbone of computer networks studies. It provides the theoretical foundation needed to comprehend how data traverses complex network infrastructures and prepares students for advanced networking concepts and certifications.

## Key Concepts

### 1. Routing vs. Forwarding

It is essential to distinguish between routing and forwarding. Routing is the process of determining the optimal path that a packet should take through the network, involving complex algorithms and network-wide intelligence. Forwarding, on the other hand, is the process of moving packets from a router's input interface to the appropriate output interface based on the routing table. Routing is a network-wide, global process, while forwarding is a local, per-router operation.

### 2. Classification of Routing Algorithms

**A. Based on Adaptation to Network Changes:**

- **Static Routing Algorithms**: These algorithms use manually configured routes that do not change automatically. They are simple but cannot adapt to network failures or congestion. Static routes are typically used in small networks or for specific traffic engineering purposes.

- **Dynamic Routing Algorithms**: These algorithms automatically adjust routes based on current network conditions such as traffic load, link failure, or congestion. They require more computational resources but provide better resilience and efficiency in dynamic network environments.

**B. Based on Routing Decision Location:**

- **Centralized Routing**: A central controller makes all routing decisions for the entire network. This approach can provide optimal solutions but creates a single point of failure and scalability issues.

- **Distributed Routing**: Each router makes routing decisions independently based on locally available information. This approach is more scalable and fault-tolerant but may not always produce globally optimal paths.

### 3. Dijkstra's Shortest Path Algorithm

Dijkstra's algorithm finds the shortest path from a source node to all other nodes in a weighted graph. It works by maintaining a set of vertices whose shortest distance from the source is known and progressively expanding this set.

**Algorithm Steps:**

1. Initialize distances: source vertex distance = 0, all others = ∞
2. Add all vertices to priority queue (or mark as unvisited)
3. While unvisited vertices exist:

- Select vertex with minimum distance
- For each neighbor, calculate new distance through current vertex
- Update distance if shorter path is found

4. Mark current vertex as visited

**Time Complexity**: O(V²) with simple implementation, O(E + V log V) with priority queue

### 4. Distance Vector Routing

In distance vector routing, each router maintains a table (vector) containing the best known distance to every destination and the next hop to reach that destination. Routers periodically exchange these tables with directly connected neighbors.

**Key Characteristics:**

- Each router knows only the distance to each destination and the next hop
- Updates occur periodically or when changes are detected
- Subject to count-to-infinity problem
- Examples: RIP (Routing Information Protocol)

**Bellman-Ford Equation**: The fundamental equation used is D(x,y) = min{c(x,v) + D(v,y)} where v is any neighbor of x

### 5. Link State Routing

Link state routing algorithms maintain a complete view of the network topology at each router. Each router discovers its immediate neighbors and the cost to reach them, then floods this information throughout the network.

**Key Characteristics:**

- Each router has a complete map of the network
- Faster convergence than distance vector
- Requires more memory and processing power
- Examples: OSPF (Open Shortest Path First), IS-IS

**Operations:**

1. Hello packets discover neighbors
2. Link state packets contain neighbor information
3. Flooding distributes information to all routers
4. Dijkstra's algorithm computes shortest paths

### 6. Path Vector Routing

Path vector routing maintains not just the destination and cost, but the entire path to each destination. This approach prevents routing loops and provides flexible routing policies.

**Key Characteristics:**

- Each routing update contains the complete path to destination
- Supports routing policies and route filtering
- Prevents count-to-infinity problems
- Example: BGP (Border Gateway Protocol)

### 7. Routing Metrics

The metric determines how routes are evaluated and compared:

- **Hop Count**: Number of routers a packet must traverse
- **Bandwidth**: Capacity of the link
- **Delay**: Time taken for packet transmission
- **Load**: Current traffic on the link
- **Reliability**: Likelihood of link failure
- **Cost**: Administrative weight assigned to links

### 8. Hierarchical Routing

As networks scale, flat routing becomes impractical. Hierarchical routing organizes routers into domains or areas, with routers within an area knowing only local topology. This reduces routing table size and update traffic.

## Examples

### Example 1: Dijkstra's Algorithm Application

**Problem**: Find the shortest path from node A to all other nodes in the following network:

```
 2 4
A-------B-------E
| /| |
| 1/ |3 2
| / | |
C---D----F------G
 2 3
```

**Solution**:

**Step 1**: Initialize

- A=0, B=∞, C=∞, D=∞, E=∞, F=∞, G=∞
- Current: A

**Step 2**: Process neighbors of A

- Via B: B = 0 + 2 = 2
- Via C: C = 0 + ∞ (no direct link)
- Unvisited: {B=2, C=∞, D=∞, E=∞, F=∞, G=∞}

**Step 3**: Current = B (distance 2)

- Process B's neighbors:
- To E: 2 + 4 = 6
- To D: 2 + 1 = 3 (D = 3)
- To F: 2 + 3 = 5 (F = 5)
- Unvisited: {C=∞, D=3, E=6, F=5, G=∞}

**Step 4**: Current = D (distance 3)

- To C: 3 + 2 = 5 (C = 5)
- To F: 3 + 3 = 6 (F remains 5)
- Unvisited: {C=5, E=6, F=5, G=∞}

**Step 5**: Current = F (distance 5)

- To E: 5 + 2 = 7 (E remains 6)
- To G: 5 + 3 = 8 (G = 8)
- Unvisited: {C=5, E=6, G=8}

**Final Shortest Paths from A**:

- A→A: 0
- A→B: 2
- A→D: 3
- A→C: 5 (via D)
- A→E: 6 (via B)
- A→F: 5
- A→G: 8 (via F)

### Example 2: Distance Vector Routing Simulation

**Problem**: Consider three routers A, B, and C in a linear topology: A—B—C. Initial distance vectors are:

- A's table: {A:0, B:1, C:∞}
- B's table: {A:1, B:0, C:1}
- C's table: {A:∞, B:1, C:0}

After one iteration of distance vector exchange, compute new distance vectors.

**Solution**:

**Step 1**: A receives updates from B

- Current distance to B = 1
- B's distance to A = 1 → New path: 1 + 1 = 2
- B's distance to C = 1 → New path: 1 + 1 = 2
- A's new table: {A:0, B:1, C:2}

**Step 2**: B receives updates from A and C

- From A: A→C via B = 1 + 2 = 3 (current is 1)
- From C: C→A via B = 1 + 2 = 3 (current is 1)
- B's table remains: {A:1, B:0, C:1}

**Step 3**: C receives updates from B

- Current distance to B = 1
- B's distance to A = 1 → New path: 1 + 1 = 2
- C's new table: {A:2, B:1, C:0}

**Result after first iteration**:

- A: {A:0, B:1, C:2}
- B: {A:1, B:0, C:1}
- C: {A:2, B:1, C:0}

### Example 3: Analyzing Routing Algorithm Choice

**Problem**: For a small campus network with 5 buildings and approximately 50 routers, compare suitable routing algorithms.

**Solution**:

**Option 1: RIP (Distance Vector)**

- Advantages: Simple to configure, low overhead, works well for small networks
- Disadvantages: Maximum 15 hops, slow convergence, may cause routing loops
- Suitable if: Network is small, limited hops needed, simple implementation priority

**Option 2: OSPF (Link State)**

- Advantages: Fast convergence, no hop limit, supports areas for hierarchy
- Disadvantages: More complex configuration, higher memory and CPU requirements
- Suitable if: Network may grow, fast convergence required, multiple paths needed

**Recommendation**: For a campus network of this size, OSPF is more appropriate due to:

1. Scalability for future expansion
2. Faster convergence during link failures
3. Better load balancing capabilities
4. Hierarchical design through areas reduces complexity

## Exam Tips

1. **Understand the fundamental difference** between routing and forwarding - this is a common exam question requiring clear explanation.

2. **Master Dijkstra's algorithm** - be prepared to trace through complete examples and compute shortest paths step by step.

3. **Know the comparison** between Distance Vector and Link State routing in terms of convergence time, memory requirements, scalability, and bandwidth usage.

4. **Remember the Bellman-Ford equation** D(x,y) = min{c(x,v) + D(v,y)} - it forms the basis of distance vector routing.

5. **Understand the count-to-infinity problem** in distance vector routing and how it manifests in networks with loops.

6. **Be familiar with routing metrics** - different protocols use different metrics (hop count, bandwidth, delay, etc.) and this affects path selection.

7. **Know real-world protocol examples**: RIP uses distance vector, OSPF uses link state, BGP uses path vector.

8. **Hierarchical routing** is important - understand how it reduces routing table size and why it's necessary for large networks.

9. **Practice tracing** through distance vector updates - this is a frequent examination problem.

10. **Understand when to use static vs. dynamic routing** - static for small, stable networks; dynamic for larger, changing networks.
