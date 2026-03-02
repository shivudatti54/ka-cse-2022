# Border Gateway Protocol (BGP) - Summary

## Key Definitions and Concepts

- **Border Gateway Protocol (BGP):** The standard exterior gateway protocol used for routing between autonomous systems on the Internet. Operates over TCP port 179 using a path vector algorithm.

- **Autonomous System (AS):** A collection of IP networks under single administrative control with a unique ASN. Public ASNs (1-64511) are assigned by IANA; private ASNs (64512-65535) for internal use.

- **eBGP (External BGP):** BGP session between routers in different autonomous systems. Default TTL is 1; next-hop address is changed by default.

- **iBGP (Internal BGP):** BGP session between routers within the same AS. Routes from one iBGP peer are not advertised to other iBGP peers; next-hop is preserved by default.

## Important Formulas and Theorems

- **BGP Hold Time:** Default 180 seconds; Keepalive sent every 60 seconds (one-third of hold time)

- **BGP Router ID:** Highest IP address on loopback interface, or highest physical interface if no loopback exists

- **iBGP Full Mesh Formula:** For n iBGP routers, requires n(n-1)/2 sessions; impractical beyond small deployments—use Route Reflectors for scaling

## Key Points

- BGP uses four message types: OPEN (establishes session), KEEPALIVE (maintains session), UPDATE (advertises/withdraws routes), NOTIFICATION (reports errors and closes session)

- BGP Path Attributes: AS_Path (loop prevention, path selection), Local Preference (outbound traffic, default 100, higher preferred), MED (inbound traffic influence, lower preferred), Origin (IGP > EGP > Incomplete), Next Hop (destination reachability)

- BGP Route Selection Order: Highest Local Preference → Shortest AS_Path → Lowest Origin → Lowest MED → eBGP over iBGP → Lowest IGP metric → Lowest Router ID

- BGP States: Idle → Connect → Active → OpenSent → OpenConfirm → Established

- Route Reflectors solve iBGP full mesh scaling by allowing iBGP route reflection to other clients

- Route flap damping suppresses unstable routes by assigning penalties; routes are suppressed when penalty exceeds suppress-limit (2000 default)

## Common Mistakes to Avoid

- Forgetting that iBGP does not change next-hop by default, causing reachability issues when the next-hop is not in the IGP

- Configuring eBGP peers with incorrect AS numbers—the remote-as must match the neighbor's actual AS number

- Believing BGP converges quickly—it is designed for stability over speed, with hold timers of 180 seconds

- Assuming BGP automatically advertises connected networks—must use network command or redistribution

## Revision Tips

1. Focus on understanding the difference between eBGP and iBGP operational behaviors, especially regarding next-hop handling

2. Memorize the BGP route selection order using a mnemonic or sequential list—it frequently appears in exams

3. Practice reading BGP routing tables and interpreting AS_PATH, Local Preference, and other attributes

4. Remember that BGP is path-vector—not distance-vector like RIP, nor link-state like OSPF
