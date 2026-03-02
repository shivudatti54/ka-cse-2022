# Routing Information Protocol (RIP) - Summary

## Key Definitions and Concepts

- **RIP (Routing Information Protocol)**: A distance-vector routing protocol that uses hop count as the metric for path selection, with a maximum of 15 hops.
- **Hop Count**: The number of routers a packet must traverse to reach the destination; RIP's sole routing metric.
- **Infinite Metric**: Value of 16 used to indicate unreachable networks in RIP.
- **Split Horizon**: Loop prevention mechanism that prevents advertising routes back to the interface they were learned from.
- **Poison Reverse**: Loop prevention technique that advertises unreachable routes with metric 16.

## Important Formulas and Theorems

- **Maximum Hops**: 15 (16 = unreachable)
- **Update Timer**: 30 seconds (periodic routing updates)
- **Invalid Timer**: 180 seconds (route marked invalid without updates)
- **Holddown Timer**: 180 seconds (prevents premature route acceptance)
- **Flush Timer**: 240 seconds (route removed from table)
- **Administrative Distance**: 120
- **Protocol Port**: UDP 520

## Key Points

- RIP is a classful distance-vector protocol suitable for small networks (up to 15 hops).
- RIPv1 supports classful routing only; RIPv2 supports VLSM/CIDR and provides authentication.
- RIP uses UDP for transport, making it connectionless but faster than TCP-based protocols.
- Periodic updates (every 30 seconds) contain the entire routing table, consuming bandwidth.
- The holddown mechanism prevents routing loops during convergence.
- Split horizon and poison reverse are essential loop prevention mechanisms.
- RIP does not support load balancing across unequal-cost paths by default.
- RIPv2 uses multicast (224.0.0.9) for updates instead of broadcast.
- Slow convergence due to timer-based updates is a major limitation of RIP.

## Common Mistakes to Avoid

1. **Confusing RIP timers**: Students often mix up the different timer values and their purposes—remember the sequence: invalid at 180s, holddown at 180s, flush at 240s.
2. **Forgetting maximum hop count**: Always remember that metric values of 16 represent infinity/unreachable.
3. **Not understanding RIPv1 limitations**: RIPv1 does not support VLSM, which is essential for modern networks.
4. **Assuming RIP supports unequal-cost load balancing**: Unlike EIGRP, RIP cannot perform unequal-cost load balancing.
5. **Overlooking administrative distance**: RIP has AD of 120, which is higher than OSPF (110) and EIGRP (90).

## Revision Tips

1. Create a comparison table between RIPv1 and RIPv2 to remember key differences.
2. Draw the network convergence timeline showing when each timer expires after a route failure.
3. Practice configuring RIP on virtual routers to understand command syntax.
4. Memorize the port number (520) and administrative distance (120) as these are frequently tested.
5. Focus on loop prevention mechanisms as they are critical to understanding why RIP works reliably.
