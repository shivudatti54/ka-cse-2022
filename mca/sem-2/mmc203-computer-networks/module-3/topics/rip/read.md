# Routing Information Protocol (RIP)


## Table of Contents

- [Routing Information Protocol (RIP)](#routing-information-protocol-rip)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Distance Vector Routing Fundamentals](#distance-vector-routing-fundamentals)
  - [RIP Message Format](#rip-message-format)
  - [RIP Timers](#rip-timers)
  - [Hop Count Limitation](#hop-count-limitation)
  - [Loop Prevention Mechanisms](#loop-prevention-mechanisms)
  - [RIPv1 vs RIPv2](#ripv1-vs-ripv2)
- [Examples](#examples)
  - [Example 1: RIP Routing Table Calculation](#example-1-rip-routing-table-calculation)
  - [Example 2: Handling Route Failure](#example-2-handling-route-failure)
  - [Example 3: Calculating Best Path](#example-3-calculating-best-path)
- [Exam Tips](#exam-tips)

## Introduction

Routing Information Protocol (RIP) is one of the oldest and most widely used interior gateway protocols in computer networking. It is a distance-vector routing protocol that uses hop count as its sole metric for determining the best path to a destination network. RIP was originally designed for small to medium-sized networks and has been a fundamental topic in computer networks education, particularly in the CSE curriculum.

The protocol operates at the Application layer of the OSI model and uses UDP port 520 for communication between routers. RIP was first defined in RFC 1058 and later updated in RFC 2453 (RIPv2). Despite its age, RIP remains relevant in certain network scenarios due to its simplicity and ease of configuration. Understanding RIP is essential for network engineers as it provides the foundation for understanding more complex routing protocols like OSPF and EIGRP. The protocol's behavior, limitations, and convergence mechanisms offer valuable insights into the challenges of dynamic routing in IP networks.

## Key Concepts

### Distance Vector Routing Fundamentals

RIP is classified as a distance-vector routing protocol, which means each router maintains a routing table that contains information about the distance (metric) to each destination network. In RIP, the "distance" is measured in hops, where each router along a path adds one hop to the metric. A directly connected network has a metric of 0, while a network reachable through one router has a metric of 1, and so forth.

The fundamental principle behind distance-vector routing is that each router periodically shares its entire routing table with its directly connected neighbors. When a router receives an update from a neighbor, it examines the information and updates its own routing table if the new path offers a shorter route to a destination. This process continues iteratively until all routers in the network converge to a consistent view of the network topology.

### RIP Message Format

RIP uses two types of messages: request messages and response messages. Request messages are sent by a router when it first comes online or when it needs updated routing information from neighbors. Response messages contain the routing table entries that are shared with neighboring routers.

A RIP message consists of a header followed by route entries. The header is 4 bytes and contains command (1 for request, 2 for response), version number, and must be zero field. Each route entry is 20 bytes and includes: address family identifier (2 for IP), route tag, IP address, subnet mask, metric, and next hop. RIPv1 uses a fixed subnet mask of 255.255.255.0 for classful networks, while RIPv2 supports variable length subnet masking (VLSM).

### RIP Timers

RIP employs several timers to control the routing update process and ensure network stability:

1. **Update Timer (30 seconds)**: This timer controls the periodic broadcast of the entire routing table. By default, RIP routers send their complete routing table to all neighboring routers every 30 seconds.

2. **Invalid Timer (180 seconds)**: If no updates are received for a particular route within 180 seconds, the route is marked as invalid. However, the route is still maintained in the routing table with an infinite metric.

3. **Holddown Timer (180 seconds)**: When a route is marked as invalid, the holddown timer starts. During this period, the router ignores any updates about that specific route to prevent routing loops caused by inconsistent information.

4. **Flush Timer (240 seconds)**: If no updates are received for a route within 240 seconds, the route is removed entirely from the routing table. The flush timer starts simultaneously with the invalid timer.

### Hop Count Limitation

RIP has a maximum hop count of 15, which means any destination more than 15 routers away is considered unreachable. The 16th hop is designated as "infinite" or unreachable. This limitation makes RIP unsuitable for large enterprise networks but helps prevent routing loops by limiting the network diameter.

The hop count limitation is both a disadvantage and a safety mechanism. While it restricts network size, it also ensures that routing information does not circulate indefinitely in case of network problems.

### Loop Prevention Mechanisms

RIP implements several mechanisms to prevent routing loops:

1. **Split Horizon**: This mechanism prevents a router from advertising a route back to the interface from which it learned that route. For example, if Router A learns about network X from Router B via interface FastEthernet 0/0, Router A will not advertise network X back to Router B through FastEthernet 0/0.

2. **Poison Reverse**: Instead of simply not advertising routes back, a router using poison reverse sends those routes with a metric of 16 (infinite). This explicitly tells the neighbor that the network is unreachable through that path.

3. **Count to Infinity Problem**: This occurs when two routers have routes to the same destination through each other. RIP handles this by setting the metric to 16 (infinite) when a route becomes invalid, and the holddown timer prevents premature acceptance of alternative routes.

### RIPv1 vs RIPv2

| Feature            | RIPv1                       | RIPv2                        |
| ------------------ | --------------------------- | ---------------------------- |
| Classful/Classless | Classful only               | Classless (supports VLSM)    |
| Subnet Mask        | Not advertised              | Advertised in updates        |
| Authentication     | Not supported               | MD5 authentication supported |
| Multicast Updates  | Broadcast (255.255.255.255) | Multicast (224.0.0.9)        |
| Route Tag          | Not supported               | Supported                    |
| Triggered Updates  | Not supported               | Supported                    |

## Examples

### Example 1: RIP Routing Table Calculation

Consider a simple network topology with three routers: Router A, Router B, and Router C connected in a linear fashion.

```
[Router A] ---- [Router B] ---- [Router C]
 | | |
 Net1 Net2 Net3
```

Initially, Router A knows only about Net1 (connected directly with metric 0), Router B knows about Net2, and Router C knows about Net3.

**Step 1**: After the first RIP update cycle:

- Router A learns about Net2 from Router B with metric 1 (one hop away)
- Router B learns about Net1 from Router A with metric 1, and Net3 from Router C with metric 1
- Router C learns about Net2 from Router B with metric 1

**Step 2**: After convergence:

- Router A has routes: Net1 (metric 0, directly connected), Net2 (metric 1 via B), Net3 (metric 2 via B)
- Router B has routes: Net1 (metric 1 via A), Net2 (metric 0, directly connected), Net3 (metric 1 via C)
- Router C has routes: Net1 (metric 2 via B), Net2 (metric 1 via B), Net3 (metric 0, directly connected)

### Example 2: Handling Route Failure

Assume Router C's interface to Net3 fails. The sequence of events in RIP:

1. Router C detects the failure and marks Net3 as unreachable (metric 16)
2. Router C sends an update to Router B announcing Net3 with metric 16
3. Router B receives the update, but due to holddown timer, it maintains the existing route to Net3 temporarily
4. After 180 seconds (invalid timer), Router B marks Net3 as invalid
5. After 240 seconds (flush timer), Router B removes Net3 from its routing table
6. The new route to Net3 (through Router C) is removed, and if alternative paths existed, they would be considered

### Example 3: Calculating Best Path

Consider a network where Router A can reach Network X through two paths:

- Path 1: Router A → Router B → Router C → Network X (3 hops)
- Path 2: Router A → Router D → Network X (2 hops)

RIP will select Path 2 because it has a lower hop count (2 < 3). Router A will install the route via Router D with metric 2 in its routing table.

If Path 2 fails (Router D goes down), Router A will eventually timeout the route and fall back to Path 1 if it still exists, updating its metric to 3.

## Exam Tips

1. **Remember the maximum hop count**: RIP considers networks beyond 15 hops as unreachable (metric 16 = infinity).

2. **RIP uses UDP port 520**: This is an important distinction as many students confuse it with TCP port numbers.

3. **Default update timer is 30 seconds**: Understand that entire routing tables are exchanged every 30 seconds, not just changes.

4. **Administrative distance for RIP is 120**: This is crucial when comparing RIP routes with other routing protocols like OSPF (110) or EIGRP (90).

5. **RIPv2 is classless**: Unlike RIPv1, RIPv2 supports VLSM and CIDR, which is essential for modern network design.

6. **Holddown prevents routing loops**: Remember that holddown timers prevent acceptance of potentially inferior routes during convergence.

7. **Split horizon is enabled by default**: This mechanism prevents routing loops by not advertising routes back to the interface they were learned from.

8. **RIP is suitable for small networks**: Always remember that RIP's simplicity comes at the cost of scalability limitations.

9. **Convergence time is slow**: RIP can take several minutes to converge after network changes due to timer-based updates.

10. **Metric is hop count only**: Unlike OSPF (cost) or EIGRP (composite), RIP uses only hop count as its routing metric.
