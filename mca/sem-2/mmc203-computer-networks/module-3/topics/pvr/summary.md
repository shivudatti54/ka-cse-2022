# Path Vector Routing (PVR) - Summary

## Key Definitions and Concepts

- **Path Vector Routing**: A routing protocol class that maintains complete path information (sequence of AS numbers) to each destination, enabling loop prevention and policy-based routing between autonomous systems

- **Autonomous System (AS)**: A collection of IP networks under single administrative control with common routing policy; identified by unique AS number (16-bit or 32-bit)

- **BGP (Border Gateway Protocol)**: The de facto standard Path Vector protocol used for inter-domain routing across the Internet

- **eBGP**: External BGP operating between different autonomous systems; changes NEXT-HOP attribute

- **iBGP**: Internal BGP operating within the same autonomous system; preserves NEXT-HOP attribute

## Important Path Attributes in BGP

| Attribute | Purpose | Selection Preference |
|-----------|---------|---------------------|
| AS-PATH | Lists AS numbers route has traversed | Shorter is preferred |
| NEXT-HOP | IP address of next router | Lower IGP cost preferred |
| LOCAL-PREF | Exit point preference (outbound) | Higher is preferred |
| MED | Entry point preference (inbound) | Lower is preferred |
| ORIGIN | How route was learned | IGP > EGP > Incomplete |

## Key Points

1. BGP uses TCP port 179 for reliable peer communication, unlike OSPF (IP protocol 89) and RIP (UDP 520)

2. Four BGP message types: OPEN (establish session), UPDATE (advertise/withdraw routes), KEEPALIVE (maintain session), NOTIFICATION (report errors)

3. Loop prevention in PVR: Router rejects any route containing its own AS number in AS-PATH attribute

4. BGP route selection follows strict hierarchy: Highest LOCAL-PREF → Shortest AS-PATH → Best ORIGIN → Lowest MED → eBGP over iBGP → Lowest IGP cost → Lowest Router ID

5. AS numbers 64512-65534 are reserved for private use (analogous to private IP addresses)

6. Path Vector combines advantages of Distance Vector (simplicity) with explicit path information (scalability and policy support)

7. BGP supports classless inter-domain routing (CIDR) and is the protocol that enables global Internet connectivity

8. AS-PATH prepending is a traffic engineering technique where additional AS numbers are added to make a path appear longer

## Common Mistakes to Avoid

1. Confusing BGP with interior gateway protocols: BGP is for inter-domain (between AS), not intra-domain (within AS) routing

2. Forgetting that LOCAL-PREF affects outbound traffic (your traffic leaving your AS) while MED affects inbound traffic (traffic entering your AS)

3. Not understanding that iBGP does not advertise routes learned from one iBGP peer to another iBGP peer (split horizon), requiring route reflectors

4. Assuming BGP converges quickly: BGP convergence can take minutes due to path vector processing and routing policies

## Revision Tips

1. Practice drawing BGP network topologies and tracing how AS-PATH attributes change as routes propagate

2. Memorize the BGP message types and their purposes in order

3. Remember the BGP route selection criteria order - this is frequently tested in exams

4. Review the differences between eBGP and iBGP in terms of NEXT-HOP handling, TTL, and purpose

5. Understand that BGP is policy-driven rather than metric-driven, unlike RIP or OSPF