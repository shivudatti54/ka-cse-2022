# Interconnection Networks in Parallel Processing

## 1. Introduction and Fundamentals

Interconnection networks constitute the fundamental communication infrastructure in parallel computing systems, enabling efficient data exchange between processors, memory modules, and I/O devices. The performance characteristics of parallel systems—latency, bandwidth, and scalability—are fundamentally constrained by the underlying network architecture. As processor speeds continue to improve according to Moore's Law, the communication subsystem often becomes the critical bottleneck limiting overall system efficiency.

In contemporary parallel architectures ranging from multicore processors to distributed-memory supercomputers, the interconnection network determines achievable parallelism, scalability, and energy efficiency. The design of interconnection networks involves careful trade-offs between competing objectives: minimizing latency, maximizing bandwidth, reducing hardware cost, and ensuring reliable communication under varying traffic conditions.

### 1.1 Classification of Interconnection Networks

Interconnection networks can be classified based on multiple criteria:

**Based on Connection Pattern:**

- **Direct Networks**: Each node has direct links to neighboring nodes (mesh, hypercube, torus)
- **Indirect Networks**: Communication through intermediate switching elements (crossbar, multistage networks)

**Based on Topology:**

- **Static Networks**: Fixed point-to-point connections (mesh, hypercube, tree)
- **Dynamic Networks**: Connections established on-demand (crossbar, bus with arbitration)

**Based on Routing Mechanism:**

- **Deterministic Routing**: Fixed path for each source-destination pair
- **Adaptive Routing**: Multiple possible paths based on network state

## 2. Performance Metrics and Analytical Framework

### 2.1 Fundamental Metrics

**Latency (L)**: The time required for a unit message to traverse the network from source to destination. Total latency comprises multiple components:

- **Software overhead**: Time spent at source/destination for message preparation, including buffer management and protocol processing
- **Transmission time**: Time to place all bits on the channel, computed as message length divided by channel bandwidth
- **Routing delay**: Time consumed by routing computation at each intermediate switch
- **Propagation delay**: Distance-dependent signal travel time, proportional to physical distance

For a message of length _m_ bits traversing _h_ hops on a channel with bandwidth _B_ bits/sec, assuming identical delay _t_ at each hop:
$$L_{total} = L_{overhead} + \frac{m}{B} + h \cdot t_{hop} + d \cdot t_{prop}$$

Where:

- $L_{overhead}$ = software overhead (source + destination)
- $m/B$ = transmission time
- $h \cdot t_{hop}$ = routing + queuing delay at _h_ hops
- $d \cdot t_{prop}$ = propagation delay over distance _d_

**Example Calculation**: For a message of 1024 bytes traversing 5 hops on a 10 Gbps channel with 100 ns hop delay:

- Transmission time = 1024 × 8 / 10^10 = 0.819 μs
- Hop delay = 5 × 100 ns = 0.5 μs
- Total (excluding overhead) = 1.319 μs

### 2.2 Bandwidth Analysis

**Channel Bandwidth**: The maximum data transfer rate of a single communication channel, typically expressed in GB/s or Gb/s.

**Bisection Bandwidth** ($B_{bis}$): The minimum aggregate bandwidth separating the network into two equal halves. This metric characterizes the network's capacity to support simultaneous communication between two partitions:

$$B_{bis} = \min_{\text{cut}} \sum_{e \in cut} B_e$$

For a symmetric network with _N_ nodes and uniform channel bandwidth:
$$B_{bis} = \frac{N}{2} \times B_{channel}$$

The bisection bandwidth determines the worst-case throughput when half the nodes communicate with the other half.

**Network Bisection**: A cut that divides the network into two equal (or nearly equal) subsets of nodes.

### 2.3 Structural Metrics

**Network Diameter (D)**: The maximum shortest-path distance (in hops) between any pair of nodes:
$$D = \max_{u,v \in V} d(u,v)$$
where _d(u,v)_ denotes the minimum number of hops between nodes _u_ and _v_. Lower diameter implies better worst-case latency.

**Degree (k)**: The number of incident links at each node. Node degree directly impacts:

- Hardware complexity and cost per node
- Routing complexity
- Physical packaging constraints
- Network expandability

**Average Path Length (APL)**: The mean hop count over all source-destination pairs:
$$APL = \frac{1}{N(N-1)} \sum_{u \neq v} d(u,v)$$
Lower APL indicates better average-case performance.

### 2.4 Cost Analysis

Network cost scales with total edge count:
$$Cost \propto k \times N$$

The **cost-diameter product** provides a unified performance-cost metric, balancing latency against hardware expense:
$$C_{normalized} = k \times D$$

A superior network achieves low diameter with minimal degree, yielding a small cost-diameter product.

## 3. Topological Analysis

### 3.1 Bus-Based Networks

**Architecture**: All nodes share a single communication medium through broadcast. Arbitration logic prevents simultaneous transmissions.

```
    +----+    +----+    +----+    +----+
    | P0 |    | P1 |    | P2 |    | P3 |
    +----+    +----+    +----+    +----+
       |         |         |         |
       +---------+---------+---------+
                     |
                Bus (B)
```

**Analytical Properties**:

- **Degree**: $k = 1$ (each node connects to single bus)
- **Diameter**: $D = 1$ (single hop to any node)
- **Bisection bandwidth**: $B_{bis} = B_{channel}$
- **Total edges**: $E = N - 1$

**Evaluation**: Despite minimal latency and simple implementation, bus networks suffer from $\mathcal{O}(N)$ contention as node count increases. The shared medium becomes the bottleneck, limiting scalability. Maximum practical size: 4-8 processors. Used in early multiprocessors (e.g., Sun Fire) and as intra-processor interconnects.

### 3.2 Ring Networks

**Architecture**: Nodes arranged in circular topology with unidirectional or bidirectional links. Each node communicates with immediate neighbors.

```
    P0 ----- P1 ----- P2 ----- P3 ----- P4
     ^                                 ^
     |                                 |
     +---------------------------------+
                    (wraparound)
```

**Analytical Properties**:

- **Degree**: $k = 2$ (bidirectional)
- **Diameter (unidirectional)**: $D = N - 1$
- **Diameter (bidirectional)**: $D = \lfloor N/2 \rfloor$
- **Bisection bandwidth**: $B_{bis} = 2 \times B_{channel}$ (bidirectional)
- **Total edges**: $E = N$

The bidirectional variant reduces diameter to $\lfloor N/2 \rfloor$ while maintaining constant degree 2, demonstrating the latency-bandwidth trade-off.

**Example**: For N = 8 nodes bidirectional ring:

- Maximum distance = 4 hops (from node 0 to node 4)
- Bisection bandwidth = 2 channels

### 3.3 Mesh and Torus Networks

**k-ary n-cube**: Generalized topology with _k_ nodes per dimension in _n_ dimensions. Total nodes: $N = k^n$.

#### 2D Mesh Analysis

```
    P00 --- P10 --- P20
     |       |       |
    P01 --- P11 --- P21
     |       |       |
    P02 --- P12 --- P22
```

For a $k \times k$ mesh ($N = k^2$):

- **Degree**: $k_{mesh} = 4$ (interior nodes), 3 (edges), 2 (corners)
- **Diameter**: $D = 2(k-1)$
- **Bisection bandwidth**: $B_{bis} = k \times B_{channel}$

**Example**: 4×4 mesh (k=4, N=16):

- Diameter = 2(4-1) = 6 hops (corner to opposite corner)
- Bisection bandwidth = 4 channels

#### Torus Networks (k-ary n-cube with wraparound)

The torus eliminates boundary effects by adding wraparound connections:

```
    P00 ==== P10 ==== P20
     ||      ||      ||
    P01 --- P11 --- P21
     ||      ||      ||
    P02 --- P12 --- P22
    == : wraparound (bidirectional)
```

For an $n$-dimensional torus with $k$ nodes per dimension:

- **Degree**: $k_{torus} = 2n$ (each dimension provides 2 links)
- **Diameter**: $D = \lfloor nk/2 \rfloor$
- **Bisection bandwidth**: $B_{bis} = 2k^{n-1} \times B_{channel}$ (full bisection)

**Theorem**: A 2D torus with $k \times k$ nodes has diameter $D = \lfloor k \rfloor$.

_Proof_: Each coordinate can differ by at most $\lfloor k/2 \rfloor$ in each dimension due to wraparound. The worst-case path traverses $\lfloor k/2 \rfloor$ hops in x-direction plus $\lfloor k/2 \rfloor$ hops in y-direction, giving $D = \lfloor k/2 \rfloor + \lfloor k/2 \rfloor \leq k$. ∎

**Example**: 4×4 torus:

- Diameter = ⌊4/2⌋ + ⌊4/2⌋ = 2 + 2 = 4 (vs 6 for mesh)
- Bisection bandwidth = 2 × 4 = 8 channels (full bisection)

### 3.4 Hypercube Networks

**Definition**: An n-dimensional hypercube (n-cube) contains $N = 2^n$ nodes, each uniquely labeled with n-bit binary addresses. Two nodes are adjacent (connected by an edge) iff their addresses differ in exactly one bit position.

```
                4-cube (n=4, N=16)

        0000----0001----0010----0011
         |       |       |       |
        0100----0101----0110----0111
         |       |       |       |
        1000----1001----1010----1011
         |       |       |       |
        1100----1101----1110----1111
```

**Theorem 1**: The diameter of an n-cube is _n_.

_Proof_: Any two nodes with Hamming distance _h_ (number of differing bits) require exactly _h_ hops to traverse, since each hop can change at most one bit. The maximum Hamming distance in n bits is _n_, achieved between nodes 0...0 (all zeros) and 1...1 (all ones). Thus, maximum path length = _n_. ∎

**Theorem 2**: An n-cube has degree _n_.

_Proof_: Each node address contains _n_ bit positions. Changing bit _i_ (where 0 ≤ i < n) yields a distinct neighbor. Thus, exactly _n_ neighbors exist—one for each bit position. ∎

**Theorem 3**: Bisection bandwidth of an n-cube is $2^{n-1} \times B_{channel}$.

_Proof_: Partition nodes by the most significant bit (0 versus 1). This divides the n-cube into two $(n-1)$-cubes, each containing $2^{n-1}$ nodes. Exactly $2^{n-1}$ edges cross this partition (each node in left half connects to exactly one node in right half via the MSB dimension). Each edge carries one unit of bandwidth, yielding $B_{bis} = 2^{n-1} \times B_{channel}$. ∎

**Properties Summary** for n-cube:
| Property | Value |
|----------|-------|
| Nodes | $N = 2^n$ |
| Degree | $n = \log_2 N$ |
| Diameter | $D = \log_2 N$ |
| Bisection bandwidth | $B_{bis} = N/2 \times B_{channel}$ |
| Total edges | $E = n \times 2^{n-1}$ |
| Cost-diameter product}(N \log | $\mathcal{O N)$ |

**Example**: For n=4 (16-node hypercube):

- Degree = 4
- Diameter = 4
- Bisection bandwidth = 8 channels
- Maximum distance between opposite corners = 4 hops

**Scaling Limitation**: Degree grows with $\log_2 N$, causing hardware complexity issues for large systems. Each node must have $\log_2 N$ ports, complicating physical implementation. Maximum practical: $n \leq 10-12$ (1024-4096 nodes).

### 3.5 Binary Tree Networks

**Complete Binary Tree** with _L_ levels (root at level 1):

```
              level 1:     [root]
                           /    \
              level 2:   [N]    [N]
                        / \    / \
              level 3: [N] [N][N] [N]
```

**Analytical Properties** for height-L tree ($N = 2^L - 1$ nodes):

- **Levels**: $L = \lceil \log_2(N+1) \rceil$
- **Maximum degree**: 3 (root has 3, internal nodes have 3, leaves have 1)
- **Diameter**: $D = 2(L-1)$ (path from bottom-left leaf to bottom-right leaf)
- **Bisection bandwidth**: $B_{bis} = 1 \times B_{channel}$ (single edge at narrowest point)

**Example**: Complete binary tree with L=4 (15 nodes):

- Diameter = 2(4-1) = 6 hops
- Bisection bandwidth = 1 channel (severely limited)

**Fat-Tree Variant**: Addresses the bisection bandwidth bottleneck by increasing channel width at upper levels. In a $k$-ary fat-tree, each level toward the root has $2^{level-1}$ channels, providing full bisection bandwidth.

```
                ====== (4 channels)
               |      |
             ====    ====  (2 channels each)
            |    |  |    |
           ==   == ==   == (1 channel each)
```

A $k$-ary fat-tree achieves $B_{bis} = (N/2) \times B_{channel}$, matching the theoretical maximum for symmetric networks.

### 3.6 Crossbar Switch Networks

**Architecture**: $N \times N$ crossbar with $\mathcal{O}(N^2)$ switching elements enabling simultaneous non-blocking connections between any input-output pair.

```
    Inputs    Crossbar Matrix     Outputs
    P0  ----> [●--●--●--●] ----> M0
    P1  ----> [●--●--●--●] ----> M1
    P2  ----> [●--●--●--●] ----> M2
    P3  ----> [●--●--●--●] ----> M3
```

**Analytical Properties**:

- **Degree**: $k = 2$ (one input link, one output link per endpoint)
- **Diameter**: $D = 2$ (source → input switch → output switch → destination)
- **Bisection bandwidth**: $B_{bis} = N \times B_{channel}$ (full crossbar, non-blocking)
- **Complexity**: $\mathcal{O}(N^2)$ switches
- **Cost**: $N^2$ crosspoints

**Throughput Analysis**: Each input can communicate with any output simultaneously, providing aggregate throughput of $N \times B_{channel}$. However, cost scales quadratically, limiting practical implementation to small $N$ (typically $N \leq 64$).

**Example**: 8×8 crossbar:

- Can support 8 simultaneous connections
- Bisection bandwidth = 8 channels
- Switch complexity = 64 crosspoints

### 3.7 Multistage Interconnection Networks (MINs)

Omega Network: A log-stage network connecting N inputs to N outputs using $n = \log_2 N$ stages, each containing $N/2$ switching elements.

```
Stage 0     Stage 1     Stage 2
  ○──┬──○    ○──┬──○    ○──┬──○
     │  │        │  │       │  │
  ○──┴──○    ○──┴──○    ○──┴──○
  ○──┬──○    ○──┬──○    ○──┬──○
     │  │        │  │       │  │
  ○──┴──○    ○──┴──○    ○──┴──○
```

**Properties**:

- **Stages**: $\log_2 N$
- **Switches per stage**: $N/2$
- **Total switches**: $(N/2) \log_2 N$
- **Degree**: 2 (input, output)
- **Diameter**: $2 \log_2 N$
- **Blocking**: Path-dependent; may block for certain permutations

**Routing in Omega Network**: For destination address D (binary), bit i of D determines the switch output at stage i.

**Butterfly Network**: Equivalent to omega network with perfect shuffle connection pattern. Each switch is $2 \times 2$, and routing follows deterministic bit-fixation: at stage $i$, bit $i$ of destination address determines path.

## 4. Switching Mechanisms

### 4.1 Store-and-Forward (Message Passing)

The entire message is stored at each intermediate node before forwarding. Used in traditional packet switching.

**Latency Analysis**:
$$L_{sf} = L_{overhead} + h \left( \frac{m}{B} + t_{routing} \right)$$

For message of $m$ bits over $h$ hops:

- Each hop incurs full message transmission time
- Total latency increases linearly with hop count
- High memory requirements at each node (must store entire message)

**Example**: 1024-byte message, 5 hops, 1 Gbps channel:

- Per-hop transmission: 8.192 μs
- 5-hop latency: ~41 μs (plus overhead)

### 4.2 Cut-Through (Pipelined) Routing

Message header proceeds immediately without waiting for entire message to be received. Establishes path before full transmission.

**Latency Analysis**:
$$L_{ct} = L_{overhead} + \frac{m}{B} + h \cdot t_{hop}$$

First bit reaches destination after $(m/B + h \cdot t_{hop})$, then subsequent bits stream continuously.

**Improvement Factor**: For large messages ($m \gg B \cdot t_{hop}$):
$$\text{Speedup} \approx \frac{h \cdot m/B}{m/B + h \cdot t_{hop}} \approx h$$

When $m/B \gg h \cdot t_{hop}$, cut-through achieves near $h\times$ speedup over store-and-forward.

### 4.3 Wormhole Routing

Flits (flow control digits) are the smallest units that can be buffered. Header flit establishes path; data flits follow in pipeline; tail flit releases resources.

**Properties**:

- Low latency (similar to cut-through)
- Low buffer requirements (one flit per channel)
- deadlock-prone without virtual channels
- Used in modern supercomputers (Cray, IBM Blue Gene)

**Deadlock Prevention**: Virtual channels provide multiple logical channels per physical channel, allowing escape paths for deadlock avoidance.

## 5. Routing Algorithms

### 5.1 Dimension-Order Routing (DOR)

In k-ary n-cubes, route dimensions in fixed order (e.g., X then Y). For destination $(d_x, d_y)$ from source $(s_x, s_y)$:

1. Route in X-dimension until $x$-coordinate matches
2. Then route in Y-dimension until $y$-coordinate matches

**Properties**:

- Deterministic: single path per source-destination
- Deadlock-free in wormhole routing (no channel dependencies in same dimension)
- Simple hardware implementation

**Example**: Source (0,0) → Destination (3,2) in 4×4 mesh:

- Route: (0,0) → (1,0) → (2,0) → (3,0) → (3,1) → (3,2)
- Total: 5 hops

### 5.2 Adaptive Routing

Multiple paths available based on network state (congestion, fault). Examples:

**Minimal Adaptive**: Route only along shortest paths, selecting least congested.

**Fully Adaptive**: May take non-minimal paths to avoid congestion.

**Turn Model Routing**: Prohibits certain turns to prevent deadlock while maintaining adaptiveness.

## 6. Comparative Analysis

| Network     | Nodes (N) | Degree | Diameter | Bisection BW | Cost ($k \times N$) |
| ----------- | --------- | ------ | -------- | ------------ | ------------------- |
| Bus         | N         | 1      | 1        | 1            | N                   |
| Ring        | N         | 2      | ⌊N/2⌋    | 2            | 2N                  |
| 2D Mesh     | $k^2$     | 4      | 2(k-1)   | k            | $4k^2$              |
| 2D Torus    | $k^2$     | 4      | k        | $2k$         | $4k^2$              |
| Hypercube   | $2^n$     | n      | n        | N/2          | $n \times 2^n$      |
| Binary Tree | $2^L-1$   | 3      | 2(L-1)   | 1            | $3(2^L-1)$          |
| Crossbar    | N         | 2      | 2        | N            | $2N$                |

## 7. Numerical Problems

**Problem 1**: Calculate the minimum latency for a 1024-bit message traveling through a 4×4 torus network with 10 Gbps channels and 50 ns routing delay per hop. Assume store-and-forward switching and negligible propagation delay.

**Solution**:

- Message length: $m = 1024$ bits
- Channel bandwidth: $B = 10$ Gbps $= 10^{10}$ bits/s
- Hop count (worst-case in 4×4 torus): $D = \lfloor 4/2 \rfloor + \lfloor 4/2 \rfloor = 4$ hops
- Routing delay per hop: $t_{hop} = 50$ ns

Transmission time per hop: $t_{tx} = m/B = 1024/10^{10} = 102.4$ ns

Total latency = $h \times (t_{tx} + t_{hop}) = 4 \times (102.4 + 50) = 4 \times 152.4 = 609.6$ ns

**Problem 2**: Compare bisection bandwidth for a 64-node hypercube versus a 8×8 mesh.

**Solution**:

- Hypercube (n=6, since $2^6 = 64$): $B_{bis} = 2^{6-1} \times B_{channel} = 32 \times B_{channel}$
- Mesh (8×8, k=8): $B_{bis} = k \times B_{channel} = 8 \times B_{channel}$

Hypercube provides $32/8 = 4\times$ more bisection bandwidth.

**Problem 3**: For a complete binary tree with 7 nodes (height 3), calculate diameter and bisection bandwidth.

**Solution**:

- Nodes: $N = 2^3 - 1 = 7$
- Height: $L = 3$
- Diameter: $D = 2(L-1) = 2(3-1) = 4$ (leaf at level 3 to opposite leaf at level 3)
- Bisection bandwidth: $B_{bis} = 1 \times B_{channel}$ (single edge separates root's subtrees)

## 8. Assessment Questions

### Question 1 (Hard - Analytical)

In a 3D mesh with 4 nodes per dimension (4×4×4 = 64 nodes), calculate:

(a) Network diameter  
(b) Bisection bandwidth (in terms of channel bandwidth $B$)  
(c) Average path length (assuming uniform traffic distribution)

**Answer**:
(a) Diameter = $3(4-1) = 9$ hops (corner to opposite corner)  
(b) $B_{bis} = 4^2 \times B = 16B$ (minimum cut separates $4 \times 4 = 16$ nodes)  
(c) For 3D mesh, average path length $\approx 1.5(k-1) = 1.5 \times 3 = 4.5$ hops

### Question 2 (Hard - Comparative Analysis)

Given a parallel system requiring communication between 32 processors, compare a hypercube network and a 2D torus (4×4) in terms of diameter, bisection bandwidth, and hardware cost. Which network would you recommend for nearest-neighbor communication patterns? Justify your answer.

**Answer**:

- **Hypercube** (n=5, $2^5 = 32$):
  - Diameter = 5
  - $B_{bis} = 2^{5-1} \times B = 16B$
  - Degree = 5, \times 32 = 160$

Cost = $5- **Torus** (4×4, N=16) — insufficient, need 8×4 = 32:

- Diameter = ⌊8/2⌋ + ⌊4/2⌋ = 4 + 2 = 6
- $B_{bis} = 2 \times 4 \times B = 8B$
- Degree = 4, Cost = $4 \times 32 = 128$

**Recommendation**: For nearest-neighbor communication, hypercube provides lower diameter and higher bisection bandwidth despite higher degree. The regular connectivity in hypercube ensures efficient one-hop communication between nodes differing in any single bit position.

### Question 3 (Hard - Routing)

Using dimension-order routing in a 4-ary 2-cube (4×4 torus), trace the path from source node (0,3) to destination node (3,1). How many hops does this require? Is this a minimal path?

**Answer**:
Source: (0,3), Destination: (3,1)

Dimension-order (X then Y):

- X-difference: $3 - 0 = 3$ (mod 4), but minimal is 1 via wraparound: $0 \to 3$ (1 hop)
- Y-difference: $1 - 3 = -2$ (mod 4), minimal is 2: $3 \to 1$ (2 hops)

Path: (0,3) → (3,3) → (3,2) → (3,1)  
Total: 3 hops

Without wraparound (X→Y order, no wrap): (0,3) → (1,3) → (2,3) → (3,3) → (3,2) → (3,1) = 5 hops

The actual path uses wraparound in X-dimension (1 hop instead of 3), achieving 3 hops, which equals the diameter and is therefore minimal. The X→Y routing with wraparound achieves optimal distance.
