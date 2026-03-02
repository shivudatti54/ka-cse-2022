# Addressing and Routing Algorithms - Summary

## Key Definitions and Concepts

- **IPv4 Address**: A 32-bit logical address uniquely identifying a device, represented as four octets in dotted-decimal notation (e.g., 192.168.1.100).

- **Subnet Mask**: A 32-bit number with contiguous 1s for network portion and 0s for host portion that determines network/host division.

- **Subnetting**: Process of dividing a network into smaller subnets by borrowing host bits for subnet identification.

- **CIDR (Classless Inter-Domain Routing)**: Addressing scheme using variable-length subnet masks, denoted as prefix length (e.g., /24).

- **Route Aggregation**: Combining multiple networks into a single summarized route, reducing routing table size.

- **Distance Vector Routing**: Algorithm where routers share entire routing tables with neighbors; uses hop count as metric.

- **Link State Routing**: Algorithm where routers maintain complete topology map; uses cost/bandwidth as metric.

## Important Formulas and Theorems

- **Hosts per subnet**: 2^n - 2 (where n = host bits)
- **Number of subnets**: 2^n (where n = borrowed bits)
- **Network address**: IP AND Subnet Mask
- **Broadcast address**: Network address OR (NOT Subnet Mask)
- **Bellman-Ford**: D(x,y) = min{v} [c(x,v) + D(v,y)]
- **Dijkstra**: Uses priority queue to find shortest path; O(n log n) complexity

## Key Points

- Class A: /8 (255.0.0.0), Class B: /16 (255.255.0.0), Class C: /24 (255.255.255.0)
- Loopback address: 127.0.0.1 (entire 127.x.x.x range reserved)
- Private IP ranges: 10.x.x.x, 172.16-31.x.x, 192.168.x.x
- RIP uses hop count (max 15), OSPF uses cost (bandwidth-based)
- Distance vector prone to count-to-infinity; link state converges faster
- OSPF requires Area 0 as backbone; supports VLSM and authentication
- CIDR notation enables efficient IP allocation and route summarization

## Common Mistakes to Avoid

1. **Forgetting to subtract 2** from host calculations (network and broadcast addresses are unusable).

2. **Confusing default masks** with subnet masks in classful vs classless scenarios.

3. **Incorrect binary conversion** leading to wrong subnet boundaries.

4. **Not updating routing tables** properly when link state changes in distance vector protocols.

5. **Misidentifying network class** when given an IP address (e.g., 191 is Class B, not C).

## Revision Tips

1. Practice at least 5 subnetting problems daily, covering different scenarios (Class A, B, C networks).

2. Create a comparison table for routing protocols (RIP vs OSPF vs EIGRP) to memorize key differences.

3. Memorize the powers of 2 from 2^1 to 2^10 (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024).

4. Write step-by-step procedures for subnet calculation and Dijkstra algorithm—exam questions often ask for these steps.

5. Review previous year DU question papers to understand the pattern and difficulty level of numerical problems.