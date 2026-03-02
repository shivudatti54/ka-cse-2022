# OSPF Protocol - Summary

## Key Definitions and Concepts

- **OSPF (Open Shortest Path First):** A link-state interior gateway protocol that uses Dijkstra's algorithm to find the shortest path to destination networks
- **Link-State Advertisement (LSA):** OSPF packets containing routing information about network topology
- **Designated Router (DR):** Router elected in multi-access networks to reduce adjacency overhead
- **Router ID:** 32-bit identifier for each OSPF router, typically highest loopback or interface IP

## Important Formulas and Theorems

- **OSPF Cost:** Cost = Reference Bandwidth (100 Mbps) / Interface Bandwidth
- **Dead Timer:** 4 × Hello Timer (40 seconds default for broadcast, 120 seconds for NBMA)
- **Dijkstra's Algorithm:** Used to compute shortest path; evaluates cumulative cost to each destination

## Key Points

- OSPF is a classless protocol supporting VLSM and CIDR addressing
- Hierarchical design uses areas to limit LSA flooding and reduce LSDB size
- Five LSA types serve different purposes: Router, Network, Summary, ASBR-Summary, and External
- OSPF uses multicast addresses 224.0.0.5 (all OSPF routers) and 224.0.0.6 (DR/BDR)
- Stub areas block external routes (Type 5 LSAs) and use default routes for external destinations
- Adjacency forms through seven states: Down, Init, 2-Way, ExStart, Exchange, Loading, Full
- Router ID selection priority: Configured > Highest Loopback > Highest Physical Interface

## Common Mistakes to Avoid

- Forgetting that all areas must connect to Area 0; using virtual links as a workaround
- Mismatching Hello/Dead timers between OSPF neighbors preventing adjacency formation
- Assuming OSPF cost is inversely proportional to bandwidth without using the correct formula
- Confusing LSA Type 3 (summary routes between areas) with LSA Type 5 (external routes)

## Revision Tips

- Practice configuring OSPF on packet tracer or GNS3 to reinforce learning
- Memorize the LSA type functions using flashcards; focus on what each type carries
- Draw network topologies and trace LSA flooding to understand OSPF behavior
- Remember: OSPF priority of 0 makes a router ineligible for DR/BDR election
