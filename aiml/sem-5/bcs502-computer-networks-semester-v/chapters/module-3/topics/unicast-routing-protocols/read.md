# Routing Protocols: RIP, OSPF, BGP

=====================================

## Introduction

---

Routing protocols are used to determine the best path for forwarding packets between networks. They are essential for the functioning of the internet and are used by routers to exchange information about the network topology.

## RIP (Routing Information Protocol)

---

RIP is a distance-vector routing protocol that uses hop count as the metric to determine the best path. It is a simple protocol that is easy to implement but has some limitations.

### How RIP Works

1. Each router sends its routing table to its neighbors every 30 seconds.
2. The neighbors update their routing tables based on the information received.
3. The router with the lowest hop count is chosen as the best path.

### Advantages of RIP

- Simple to implement
- Easy to configure
- Works well in small networks

### Disadvantages of RIP

- Limited scalability (max 15 hops)
- Slow convergence
- Does not support VLSM (Variable Length Subnet Masks)

## OSPF (Open Shortest Path First)

---

OSPF is a link-state routing protocol that uses the shortest path first (SPF) algorithm to determine the best path. It is a more complex protocol than RIP but offers more features and scalability.

### How OSPF Works

1. Each router sends a link-state advertisement (LSA) to its neighbors, which includes information about its links and neighbors.
2. The neighbors update their link-state databases based on the information received.
3. The router with the lowest cost is chosen as the best path.

### Advantages of OSPF

- Scalable
- Fast convergence
- Supports VLSM
- Can handle large networks

### Disadvantages of OSPF

- Complex to implement
- Requires more CPU and memory resources

## BGP (Border Gateway Protocol)

---

BGP is a path-vector routing protocol that is used to exchange routing information between autonomous systems (AS). It is a complex protocol that is used by ISPs and large organizations.

### How BGP Works

1. Each AS sends its routing table to its neighbors, which includes information about its routes and attributes.
2. The neighbors update their routing tables based on the information received.
3. The router with the best path is chosen based on the attributes.

### Advantages of BGP

- Scalable
- Can handle large networks
- Supports policy-based routing

### Disadvantages of BGP

- Complex to implement
- Requires more CPU and memory resources

## Comparison of RIP, OSPF, and BGP

---

| Protocol | Metric     | Scalability | Complexity |
| -------- | ---------- | ----------- | ---------- |
| RIP      | Hop count  | Limited     | Simple     |
| OSPF     | Cost       | Scalable    | Complex    |
| BGP      | Attributes | Scalable    | Complex    |

## Exam Tips

---

- Understand the basics of each protocol
- Know the advantages and disadvantages of each protocol
- Be able to compare and contrast the protocols
- Practice configuring and troubleshooting each protocol
