# Distance Vector Routing (DVR) - Summary

## Key Definitions and Concepts

- **Distance Vector Routing**: A routing algorithm where each router maintains a table (distance vector) containing the best known distance to every destination and the next-hop router to reach it.
- **Routing Table**: A data structure stored in each router that maps destination networks to next-hop addresses and associated costs.
- **Convergence**: The state when all routers in a network have consistent and complete routing information.
- **Count-to-Infinity Problem**: A routing loop issue where routers continuously increment their distance estimates when a link fails.

## Important Formulas and Theorems

- **Bellman-Ford Equation**: D(x,y) = min{c(x,v) + D(v,y)}
  - Where D(x,y) is the minimum cost from node x to destination y
  - c(x,v) is the cost from x to neighbor v
  - D(v,y) is the cost from neighbor v to destination y

## Key Points

- In DVR, routers exchange their complete routing tables with directly connected neighbors at regular intervals.
- Each router computes the best path based on information received from neighbors using the Bellman-Ford algorithm.
- RIP (Routing Information Protocol) is the most common implementation of DVR using hop count as the metric.
- RIP has a maximum hop count of 15 (16 = infinity/unreachable).
- RIPv1 is classful; RIPv2 supports classless routing (CIDR and VLSM).
- Split Horizon prevents routing loops by not advertising routes back to the router from which they were learned.
- Triggered updates send immediate notifications when route costs change, speeding up convergence.
- DVR has slower convergence compared to link-state routing protocols.
- Each router only knows the distance to destinations, not the complete network topology.

## Common Mistakes to Avoid

- Confusing Distance Vector Routing with Link State Routing (LSP maintains complete topology).
- Forgetting that RIP uses a maximum hop count of 15, not 16 (16 is infinity).
- Not understanding that split horizon is a prevention technique, not a detection technique for loops.
- Assuming routers have complete network knowledge - they only know distances through neighbors.

## Revision Tips

1. Memorize the Bellman-Ford equation and practice applying it to simple network topologies.
2. Understand the sequence of events in the count-to-infinity problem.
3. Remember the key differences between RIP v1 and v2.
4. Practice constructing routing tables from network diagrams.
5. Review the three solutions to count-to-infinity: Split Horizon, Poison Reverse, and Triggered Updates.
