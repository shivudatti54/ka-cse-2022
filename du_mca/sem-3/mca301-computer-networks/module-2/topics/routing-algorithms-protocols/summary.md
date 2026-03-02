# Routing Algorithms and Protocols - Summary

## Key Definitions and Concepts

- **Routing**: Control-plane function that determines optimal paths for packets through the network
- **Forwarding**: Data-plane function that moves packets from input to output interfaces based on routing tables
- **Autonomous System (AS)**: A collection of routers under single administrative control
- **Interior Gateway Protocol (IGP)**: Routing protocol used within an AS (RIP, OSPF, EIGRP)
- **Exterior Gateway Protocol (EGP)**: Routing protocol used between ASes (BGP)
- **Administrative Distance (AD)**: Trustworthiness metric for routing protocols; lower wins

## Important Formulas and Theorems

- **Bellman-Ford Equation**: D(x,y) = min{c(x,v) + D(v,y)} where v is any neighbor
- **Dijkstra's Algorithm**: Iteratively adds the node with smallest tentative distance to the shortest path tree
- **OSPF Cost**: Cost = Reference Bandwidth (default 100 Mbps) / Interface Bandwidth
- **RIP Maximum Hops**: 16 = unreachable (infinity)

## Key Points

- Distance Vector protocols (RIP) are simple but suffer from slow convergence and count-to-infinity
- Link State protocols (OSPF) maintain complete topology and converge quickly but require more memory/CPU
- BGP is the Internet's exterior gateway protocol using Path Vector with AS-path for loop prevention
- OSPF implements hierarchical routing through areas, with Area 0 as the backbone
- BGP path selection prioritizes: Local Preference > AS-Path Length > Origin > MED > IGP cost
- Static routing provides security and predictability; dynamic routing provides automation and resilience
- Routing metrics differ: RIP uses hop count, OSPF uses cost (bandwidth-based), BGP uses policy attributes

## Common Mistakes to Avoid

- Confusing routing (computing paths) with forwarding (moving packets)
- Assuming RIP can route to networks more than 15 hops away
- Forgetting that OSPF must have a backbone area (Area 0) connecting all other areas
- Not understanding that BGP does not use a traditional metric—it uses path attributes for policy
- Assuming faster protocols always "win"—Administrative Distance determines which route is used

## Revision Tips

1. Draw network topologies and manually work through Dijkstra's algorithm step-by-step
2. Memorize the BGP decision process with a mnemonic or flowchart
3. Create a comparison table of RIP, OSPF, and BGP covering algorithm, metric, port/protocol, convergence
4. Practice determining which routing protocol to use based on network size and requirements
5. Remember: RIP = small/simple, OSPF = enterprise/medium, BGP = ISP/inter-domain