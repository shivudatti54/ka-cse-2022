# Introduction to Routing Algorithms - Summary

## Key Definitions and Concepts

- **Routing**: The process of determining optimal paths for data packets from source to destination across networks
- **Forwarding**: The local action of moving packets from input to output interface based on routing table entries
- **Routing Algorithm**: Mathematical procedure that computes optimal paths based on network topology and metrics
- **Metric**: A quantitative measure used to evaluate path quality (hop count, bandwidth, delay, cost)
- **Convergence**: The state when all routers in a network have consistent routing information

## Important Formulas and Theorems

- **Bellman-Ford Equation**: D(x,y) = min{c(x,v) + D(v,y)}
- Used in distance vector routing to compute shortest paths
- Where D(x,y) is distance from x to y, c(x,v) is cost from x to neighbor v

- **Dijkstra's Algorithm Time Complexity**:
- Simple implementation: O(V²)
- With priority queue: O(E + V log V)
- Where V = vertices, E = edges

## Key Points

1. Routing operates at the network layer (Layer 3) and determines end-to-end paths, while forwarding handles per-packet movement through individual routers.

2. Static routing uses manually configured routes and suits small, stable networks; dynamic routing automatically adapts to network changes.

3. Dijkstra's algorithm finds shortest paths by progressively expanding the set of vertices with known shortest distances from the source.

4. Distance Vector protocols (e.g., RIP) exchange entire routing tables with neighbors, while Link State protocols (e.g., OSPF) flood link state information.

5. Count-to-infinity problem occurs in distance vector routing when links fail, causing routing tables to slowly converge to incorrect values.

6. Link State routing provides faster convergence and more accurate network views but requires more memory and processing power than Distance Vector.

7. Path Vector routing (e.g., BGP) maintains complete path information, enabling routing policies and loop prevention.

8. Hierarchical routing organizes networks into areas/domains to reduce complexity, minimize routing table size, and limit update traffic.

9. Routing metrics determine path selection: hop count (RIP), bandwidth (OSPF), composite metrics (EIGRP).

10. Convergence time is critical - faster convergence means quicker adaptation to network failures but requires more resources.

## Common Mistakes to Confuse

- Mixing up routing and forwarding concepts - they are distinct network layer functions
- Forgetting that distance vector exchanges full tables, not just changes
- Not understanding that Dijkstra requires non-negative edge weights
- Confusing link state flooding (reliable, sequence-numbered) with broadcast updates
- Assuming all routing protocols use the same metric - they differ significantly

## Revision Tips

1. Practice Dijkstra's algorithm with at least 3 different network topologies to master the step-by-step process.

2. Create comparison tables for routing algorithm types - include pros/cons, examples, convergence time, and scalability.

3. Trace through distance vector updates manually for at least 2-3 iterations to understand the convergence process.

4. Remember real-world protocol associations: RIP = Distance Vector, OSPF = Link State, BGP = Path Vector.

5. Focus on understanding why certain algorithms are suitable for specific network sizes and requirements, not just memorizing facts.
