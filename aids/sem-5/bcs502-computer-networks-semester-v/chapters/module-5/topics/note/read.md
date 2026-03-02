Of course. Here is a comprehensive educational note on a fundamental topic in Computer Networks, formatted for  Engineering students.

***

# Module 5: Network Layer - Routing Algorithms

**Subject:** Computer Networks (Semester V)

## 1. Introduction

The Network Layer is the third layer in the OSI model and is responsible for the logical addressing and routing of packets across multiple networks from the source to the destination. The core function that enables this is **routing**—the process of selecting the best path for data travel. Routing Algorithms are the set of rules or protocols that routers use to make these path-determination decisions. They are the "brains" of the network, dynamically adapting to changes in topology and traffic.

## 2. Core Concepts & Explanation

Routing algorithms can be broadly classified into two main categories based on how they operate and the information they use.

### A. Non-Adaptive (Static) Routing

In static routing, the routing paths are pre-configured by a network administrator. These paths are fixed and do not change unless manually altered. The router forwards packets based on a static routing table.

*   **How it works:** The administrator manually enters routes into the routing table. The router has no knowledge of the state of the network; it simply uses the pre-defined path.
*   **Example:**
    *   On a router, the command `ip route 192.168.2.0 255.255.255.0 10.0.0.2` tells the router that to reach the network `192.168.2.0/24`, send the packet to the next-hop router at IP address `10.0.0.2`.
*   **Advantages:** Simple to configure, no routing protocol overhead, and very secure as no routing updates are exchanged.
*   **Disadvantages:** Does not scale for large networks, cannot adapt to link failures or network congestion, and requires manual reconfiguration for any network change.

### B. Adaptive (Dynamic) Routing

In dynamic routing, routers automatically discover remote networks and build their routing tables by exchanging information with other routers using **routing protocols**. They can adapt to changes in network topology, like a link going down, by recalculating the best path.

Dynamic routing protocols are further classified based on their operation:

#### i. Distance Vector Routing

Routers using this algorithm share their entire routing table with their directly connected neighbors at regular intervals. The primary information shared is the **distance** (a metric like hop count) and the **vector** (the next-hop direction) to reach known networks.

*   **Key Protocol:** RIP (Routing Information Protocol).
*   **How it works:** Each router only knows what its neighbors tell it. It adds its own cost (e.g., +1 hop) to the learned routes and advertises them further. It uses algorithms like the **Bellman-Ford** algorithm to calculate paths.
*   **Problems:** Slow convergence and susceptibility to **routing loops** (where packets circulate endlessly). Techniques like **Split Horizon** and **Poison Reverse** are used to prevent these loops.

#### ii. Link State Routing

Routers using this algorithm have a complete map of the entire network. Each router floods information about the state of its own directly connected links to every other router in the area. Each router then independently calculates the best path to every network using this complete knowledge.

*   **Key Protocol:** OSPF (Open Shortest Path First).
*   **How it works:**
    1.  **Link State Advertisement (LSA):** Each router creates an LSA describing its own links and shares it with all routers.
    2.  **Flooding:** LSAs are reliably flooded throughout the routing domain.
    3.  **Dijkstra's Algorithm:** Every router runs this algorithm on the collected LSAs to build a shortest-path tree, with itself as the root, to determine the best path to all networks.
*   **Advantages:** Faster convergence, no routing loops, and more scalable for large networks.
*   **Disadvantages:** More complex to implement and requires more CPU and memory resources on the router.

## 3. Example Scenario

Imagine a network with three routers: R1, R2, and R3, connected in a triangle.
*   **Static Routing:** An admin manually configures R1 to send traffic for R3's network via R2.
*   **Distance Vector (RIP):** R1 tells R2, "I can reach Network X in 1 hop." R2 then tells R3, "I can reach Network X in 2 hops (through R1)."
*   **Link State (OSPF):** Each router tells every other router, "Here is a list of my directly connected links and their costs." Each router then independently uses Dijkstra's algorithm to calculate the absolute shortest path to Network X.

## 4. Key Points & Summary

| Feature | Static Routing | Dynamic Routing (Distance Vector) | Dynamic Routing (Link State) |
| :--- | :--- | :--- | :--- |
| **Configuration** | Manual | Automatic | Automatic |
| **Overhead** | None | Low to Moderate | High (CPU/Memory) |
| **Scalability** | Poor | Moderate | Good |
| **Convergence** | N/A | Slow | Fast |
| **Algorithm** | N/A | Bellman-Ford | Dijkstra |
| **Protocol Examples** | N/A | RIP, IGRP | OSPF, IS-IS |

**Summary:**
*   The choice of routing algorithm depends on network size, administrative overhead, and need for fault tolerance.
*   **Static routing** is simple but inflexible, suitable for small, stable networks.
*   **Dynamic routing** is essential for large, complex networks.
    *   **Distance Vector** protocols are simpler but have limitations like slow convergence.
    *   **Link State** protocols are more complex but provide faster convergence and a loop-free topology, making them the standard for most enterprise networks today.