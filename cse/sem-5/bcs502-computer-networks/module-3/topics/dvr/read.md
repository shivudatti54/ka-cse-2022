# Distance Vector Routing (DVR)

## Introduction

Distance Vector Routing (DVR) is one of the fundamental routing algorithms used in computer networks to determine the best path for forwarding data packets between routers. It belongs to the class of adaptive routing protocols where routers periodically exchange routing information with their directly connected neighbors to maintain an up-to-date view of the network topology.

The algorithm operates on the principle that each router maintains a distance vector (a table) containing the best known distance to every destination network and the next-hop router to reach that destination. DVR is particularly significant because it forms the foundation for more complex routing protocols like RIP (Routing Information Protocol) and IGRP (Interior Gateway Routing Protocol). Understanding DVR is essential for network engineers and computer science students as it demonstrates fundamental concepts in network layer operations, including convergence, routing loops, and metric-based path selection.

The simplicity of DVR makes it an ideal starting point for studying routing algorithms. Unlike link-state routing, where routers have a complete map of the network, in distance vector routing, routers only know the distance (cost) to reach destinations through their immediate neighbors. This distributed approach ensures scalability but also introduces challenges that network designers must address.

## Key Concepts

### Basic Working Principle

In Distance Vector Routing, each router maintains a routing table with the following information for every known destination:

- **Destination Network**: The network ID or address
- **Cost (Distance)**: The total metric value to reach that destination
- **Next Hop**: The address of the neighbor router to which packets should be forwarded

Routers initially discover their directly connected neighbors and set the cost to those networks (typically 1 for hop count). Then, at regular intervals, each router sends its distance vector (the entire routing table) to all directly connected neighbors. Upon receiving a neighbor's distance vector, a router updates its own routing table using the Bellman-Ford algorithm.

### The Bellman-Ford Algorithm

The core of DVR is the Bellman-Ford equation, which can be expressed as:

**D(x,y) = min{ c(x,v) + D(v,y) }**

Where:

- D(x,y) = cost from node x to destination y
- c(x,v) = cost from node x to neighbor v
- D(v,y) = cost from neighbor v to destination y

Each router calculates the cost to each destination by considering the cost to each neighbor plus the neighbor's cost to that destination, choosing the minimum.

### Routing Update Process

When a router receives an update from a neighbor, it performs the following steps:

1. Add the cost of the incoming interface to each entry in the neighbor's distance vector
2. Compare each entry with the current routing table entry
3. If the new route has a lower cost, update the routing table
4. If the new route is through a different next-hop but has the same cost, keep the existing route (for stability)

### Count-to-Infinity Problem

A significant drawback of DVR is the "count-to-infinity" problem, which occurs when a link fails. Consider two routers A and B, with A believing it can reach a destination through B. If the link between B and the destination fails, B updates its distance to infinity. However, before B can send this update to A, A sends its periodic update to B, claiming it can still reach the destination (with a cost of 2). B then updates its distance as 2+1=3, and this process continues until both routers converge at infinity.

**Solutions to Count-to-Infinity:**

- **Split Horizon**: A router never advertises a route back to the router from which it learned that route
- **Split Horizon with Poison Reverse**: When advertising routes, set distance to infinity for routes learned from neighbors
- **Triggered Updates**: Immediately send updates when a route changes, without waiting for the periodic timer

### RIP (Routing Information Protocol)

RIP is the most common implementation of Distance Vector Routing. It uses hop count as the metric, with a maximum of 15 hops (16 represents infinity). RIP version 1 uses classful routing, while RIP version 2 supports classless inter-domain routing (CIDR) and VLSM.

## Examples

### Example 1: Initial Routing Table Setup

Consider a simple network topology with four routers A, B, C, and D connected in a linear fashion:

- A connected to B
- B connected to C
- C connected to D

**Step 1: Initial Direct Connections**
Router A's initial routing table:
| Destination | Cost | Next Hop |
|-------------|------|----------|
| Network A | 0 | Direct |
| Network B | 1 | B |

Router B's initial routing table:
| Destination | Cost | Next Hop |
|-------------|------|----------|
| Network A | 1 | A |
| Network B | 0 | Direct |
| Network C | 1 | C |

**Step 2: After First Exchange**
Router A receives B's table. Since B can reach Network C with cost 1, A can reach Network C via B with cost 1+1=2.

Updated Router A table:
| Destination | Cost | Next Hop |
|-------------|------|----------|
| Network A | 0 | Direct |
| Network B | 1 | B |
| Network C | 2 | B |

### Example 2: Routing Update Calculation

Assume router X has the following routing table entry for destination D:

- Current: via Y, cost 5

Now X receives an update from Z for destination D:

- Z's cost to D = 3
- Link cost X-Z = 2

**Calculation:**
New cost via Z = cost(X to Z) + cost(Z to D) = 2 + 3 = 5

Since 5 equals the current cost, X keeps the existing route (via Y) for stability.

**If Z's cost was 2:**
New cost via Z = 2 + 2 = 4 (which is less than 5)
Router X would update its table to use Z as next hop with cost 4.

### Example 3: Split Horizon Demonstration

Network: A — B — C (destination is network behind C)

Initial state: A believes it can reach C's network via B with cost 2.

Without Split Horizon: A tells B it can reach C with cost 2. If B's link to C fails, B might learn from A that A can reach C (cost 2), so B updates its route via A with cost 3, creating a loop.

With Split Horizon: When A sends updates to B, it does NOT include the route to C (since A learned about C from B). This prevents the routing loop from forming.

## Exam Tips

1. **Remember the Bellman-Ford equation**: D(x,y) = min{c(x,v) + D(v,y)} - this is frequently asked in exams.

2. **Maximum hop count in RIP**: Remember that RIP uses a maximum hop count of 15, with 16 representing infinity (unreachable).

3. **Know the difference between RIP v1 and v2**: Version 1 is classful, supports no VLSM; Version 2 is classless, supports VLSM and CIDR.

4. **Count-to-infinity problem**: Understand why it occurs and the solutions (Split Horizon, Poison Reverse, Triggered Updates).

5. **Periodic updates**: RIP sends updates every 30 seconds (with some randomness to prevent synchronization).

6. **Algorithm characteristics**: DVR is also known as Bellman-Ford routing and is a distance vector protocol.

7. **Convergence time**: Distance vector protocols typically have slower convergence compared to link-state protocols.

8. **Administrative Distance**: For RIP, the default administrative distance is 120.

9. **Metric**: RIP uses hop count as the sole metric for path selection.

10. **VLSM support**: Only RIPv2 and later versions support Variable Length Subnet Masking (VLSM).
