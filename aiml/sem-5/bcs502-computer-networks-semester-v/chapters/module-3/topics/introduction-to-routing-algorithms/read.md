# Routing Algorithms: DVR, LSR, PVR

=====================================

## Introduction

Routing algorithms are used to determine the best path for forwarding packets between nodes in a network. In this chapter, we will discuss three types of routing algorithms: Distance Vector Routing (DVR), Link State Routing (LSR), and Path Vector Routing (PVR).

## Distance Vector Routing (DVR)

Distance Vector Routing (DVR) is a type of routing algorithm that uses a distance vector to determine the best path for forwarding packets. Each node in the network maintains a distance vector that contains the shortest distance to each destination node.

### How DVR Works

Here's an example of how DVR works:

Suppose we have a network with four nodes: A, B, C, and D. Each node maintains a distance vector that contains the shortest distance to each destination node.

| Node | Distance Vector    |
| ---- | ------------------ |
| A    | {B: 2, C: 3, D: 4} |
| B    | {A: 2, C: 1, D: 3} |
| C    | {A: 3, B: 1, D: 2} |
| D    | {A: 4, B: 3, C: 2} |

When a packet arrives at node A, it checks the distance vector to determine the shortest path to the destination node. If the destination node is C, node A will forward the packet to node B, which is the next hop on the shortest path.

### Advantages and Disadvantages of DVR

Advantages:

- Simple to implement
- Low overhead

Disadvantages:

- Can lead to routing loops
- Slow convergence

## Link State Routing (LSR)

Link State Routing (LSR) is a type of routing algorithm that uses a link state database to determine the best path for forwarding packets. Each node in the network maintains a link state database that contains information about the state of each link in the network.

### How LSR Works

Here's an example of how LSR works:

Suppose we have a network with four nodes: A, B, C, and D. Each node maintains a link state database that contains information about the state of each link in the network.

| Node | Link State Database     |
| ---- | ----------------------- |
| A    | {B: up, C: down, D: up} |
| B    | {A: up, C: up, D: down} |
| C    | {A: down, B: up, D: up} |
| D    | {A: up, B: down, C: up} |

When a packet arrives at node A, it checks the link state database to determine the shortest path to the destination node. If the destination node is C, node A will forward the packet to node B, which is the next hop on the shortest path.

### Advantages and Disadvantages of LSR

Advantages:

- Fast convergence
- No routing loops

Disadvantages:

- High overhead
- Complex to implement

## Path Vector Routing (PVR)

Path Vector Routing (PVR) is a type of routing algorithm that uses a path vector to determine the best path for forwarding packets. Each node in the network maintains a path vector that contains the shortest path to each destination node.

### How PVR Works

Here's an example of how PVR works:

Suppose we have a network with four nodes: A, B, C, and D. Each node maintains a path vector that contains the shortest path to each destination node.

| Node | Path Vector                  |
| ---- | ---------------------------- |
| A    | {B: A-B, C: A-B-C, D: A-B-D} |
| B    | {A: B-A, C: B-C, D: B-D}     |
| C    | {A: C-A, B: C-B, D: C-D}     |
| D    | {A: D-A, B: D-B, C: D-C}     |

When a packet arrives at node A, it checks the path vector to determine the shortest path to the destination node. If the destination node is C, node A will forward the packet to node B, which is the next hop on the shortest path.

### Advantages and Disadvantages of PVR

Advantages:

- Fast convergence
- No routing loops

Disadvantages:

- High overhead
- Complex to implement

## Comparison of DVR, LSR, and PVR

| Algorithm | Advantages                         | Disadvantages                               |
| --------- | ---------------------------------- | ------------------------------------------- |
| DVR       | Simple to implement, low overhead  | Can lead to routing loops, slow convergence |
| LSR       | Fast convergence, no routing loops | High overhead, complex to implement         |
| PVR       | Fast convergence, no routing loops | High overhead, complex to implement         |

## Exam Tips

- Understand the basics of each routing algorithm
- Be able to compare and contrast the advantages and disadvantages of each algorithm
- Practice solving problems involving routing algorithms
