# Path Vector Routing (PVR)

## Introduction

Path Vector Routing (PVR) is a fundamental routing protocol classification used extensively in inter-domain routing across the global Internet. While Distance Vector protocols like RIP are suitable for small networks and Link State protocols like OSPF work well within autonomous systems, neither can effectively handle the complex requirements of routing between different administrative domains. Path Vector Routing bridges this gap by maintaining not just the metric to each destination, but also the complete path information through autonomous systems.

The Internet is organized into thousands of Autonomous Systems (AS), each under independent administrative control. Routing between these autonomous systems requires protocols that can implement routing policies, prevent routing loops across domain boundaries, and scale to handle millions of routes. Path Vector Routing addresses all these requirements by carrying explicit path information, enabling loop detection, and supporting policy-based routing decisions.

The Border Gateway Protocol (BGP) is the de facto standard implementation of Path Vector Routing used throughout the Internet. As the protocol that glues together all autonomous systems, BGP carries over 900,000 IPv4 routes and enables global Internet connectivity. Understanding Path Vector Routing and BGP is essential for network engineers and computer science professionals, as it forms the backbone of modern Internet infrastructure.

## Key Concepts

### Autonomous Systems (AS)

An Autonomous System is a collection of IP networks and routers under the control of a single organization that presents a common routing policy to the Internet. Each AS is assigned a unique 16-bit or 32-bit AS number (ASN). Examples include large ISPs (AS 15169 is Google, AS 2914 is NTT), universities, and enterprise networks. AS numbers 64512 to 65534 are reserved for private use, similar to private IP addresses.

The AS serves as the fundamental unit of routing policy in the Internet. Within an AS, interior gateway protocols (IGP) like OSPF or EIGRP handle routing, while BGP handles routing between autonomous systems (inter-domain routing).

### Comparison with Distance Vector and Link State Routing

**Distance Vector Protocols** (e.g., RIP):
- Each router maintains only the distance (metric) to each destination
- Routers share entire routing tables with immediate neighbors
- Simple but prone to counting-to-infinity problems
- Suitable for small networks with simple topology
- Example: RIP uses hop count as metric

**Link State Protocols** (e.g., OSPF):
- Each router maintains a complete map of network topology
- Routers flood link state advertisements to all routers in the area
- Fast convergence but requires more memory and processing
- Suitable for large intra-domain routing
- Example: OSPF uses cost as metric

**Path Vector Protocols** (e.g., BGP):
- Each router maintains the complete path to each destination
- Path information includes the sequence of AS numbers
- Explicit loop prevention using AS path analysis
- Supports complex routing policies
- Suitable for inter-domain routing between autonomous systems

### BGP: The Path Vector Protocol

BGP operates as a Path Vector protocol where each route update carries the complete AS-PATH attribute listing all autonomous systems that the route has traversed. This explicit path information enables sophisticated loop prevention and policy enforcement that Distance Vector and Link State protocols cannot provide.

BGP uses TCP port 179 for reliable communication between peers. Unlike IGPs that converge based on metrics, BGP makes routing decisions based on multiple path attributes, allowing network operators to implement complex routing policies that reflect business relationships and traffic engineering requirements.

## How It Works

### BGP Message Types

BGP uses four primary message types to establish and maintain peer relationships:

**OPEN Message**: After TCP connection is established, BGP peers exchange OPEN messages to establish peering sessions. The OPEN message includes:
- BGP version number
- My AS (Autonomous System number)
- Hold time (maximum time between keepalive or update messages)
- BGP identifier (router ID - highest loopback or interface IP)
- Optional parameters (including authentication information)

**UPDATE Message**: The UPDATE message is the core of BGP routing, carrying new routes or withdrawing previously advertised routes. Each UPDATE contains:
- Withdrawn routes (IP prefixes no longer reachable)
- Path attributes (AS-PATH, NEXT-HOP, ORIGIN, LOCAL-PREF, MED, etc.)
- Network Layer Reachability Information (NLRI) - the prefixes being advertised

**KEEPALIVE Message**: BGP uses KEEPALIVE messages to maintain peer relationships. These are simple messages without any data, exchanged at intervals not exceeding one-third of the Hold Time. If no KEEPALIVE, UPDATE, or NOTIFICATION is received within the Hold Time, the connection is closed.

**NOTIFICATION Message**: When BGP detects an error condition, it sends a NOTIFICATION message and closes the BGP connection. Error codes include Message Header Error, OPEN Message Error, UPDATE Message Error, Hold Timer Expired, and Cease (administrative close).

### Path Attributes

BGP path attributes provide metadata about routes that enable policy-based routing decisions:

**AS-PATH**: This attribute contains the sequence of AS numbers through which the route has been advertised. When a BGP speaker advertises a route to an iBGP peer, it prepends its own AS number to the AS-PATH. Loop prevention works by rejecting any route where the local AS number already appears in the AS-PATH.

**NEXT-HOP**: Specifies the IP address of the next-hop router to reach the destination. For eBGP peers, this is typically the interface address of the neighbor. For iBGP, the NEXT-HOP learned from eBGP is preserved unless the router is a route reflector.

**ORIGIN**: Indicates how the route was originally learned by BGP. Three values exist: IGP (route originated from an interior protocol, coded as "i"), EGP (learned via EGP, coded as "e"), and Incomplete (learned by some other means, coded as "?"). This attribute is well-known and mandatory.

**LOCAL-PREF**: Used for traffic leaving the AS to specify preferred exit points. Higher values are preferred. This is a well-known discretionary attribute used extensively in multi-homed scenarios.

**MED (Multi-Exit Discriminator)**: Used for traffic entering the AS to indicate which entry point is preferred. Lower MED values are preferred. This is an optional transitive attribute signaled to neighboring ASes.

### eBGP vs iBGP

**eBGP (External BGP)**: Runs between routers in different autonomous systems. eBGP peers are typically directly connected (or have a few hops in between). In eBGP, the NEXT-HOP address is changed to the IP address of the eBGP peer when advertising to iBGP.

**iBGP (Internal BGP)**: Runs between routers within the same autonomous system. iBGP peers do not need to be directly connected and can be many hops apart. iBGP ensures that routes learned from other ASes are propagated throughout the AS.

**Key Differences**:
- TTL: eBGP uses TTL=1 (peers must be directly connected), iBGP uses higher TTL
- Route Reflection: Used to reduce iBGP mesh requirements
- NEXT-HOP: eBGP changes NEXT-HOP, iBGP preserves it
- Loop Prevention: iBGP does not accept routes from other iBGP peers to prevent loops within AS

### Route Selection Process

BGP uses a sophisticated route selection process with multiple criteria evaluated in order:

1. **Highest LOCAL-PREF**: Routes with higher LOCAL-PREF are preferred (only applicable within AS)
2. **Shortest AS-PATH**: Routes with fewer AS numbers in AS-PATH are preferred
3. **Lowest ORIGIN**: IGP (i) is preferred over EGP (e), which is preferred over Incomplete (?)
4. **Lowest MED**: Routes with lower MED are preferred (when comparing routes from same neighboring AS)
5. **eBGP over iBGP**: Prefer routes learned via eBGP
6. **Lowest IGP metric to NEXT-HOP**: Prefer routes with lower IGP cost to NEXT-HOP
7. **Lowest Router ID**: If all else equal, prefer the route from the peer with lowest BGP Router ID

## Examples

### Example 1: AS Path Loop Prevention

Consider four autonomous systems arranged as follows:
- AS 100 connected to AS 200
- AS 200 connected to AS 300
- AS 300 connected to AS 400
- AS 100 also connected to AS 400

Assume AS 100 advertises network 192.168.1.0/24:

1. AS 100 advertises to AS 200: AS-PATH = "100"
2. AS 200 advertises to AS 300: AS-PATH = "200 100"
3. AS 300 advertises to AS 400: AS-PATH = "300 200 100"

Now, suppose AS 400 attempts to advertise this route back to AS 100:
- AS 400 creates update with AS-PATH = "400 300 200 100"
- When AS 100 receives this, it checks its own AS (100) in the AS-PATH
- AS 100 detects its own AS number in the path → REJECTS THE ROUTE

This mechanism effectively prevents routing loops between autonomous systems.

### Example 2: BGP Route Selection with LOCAL-PREF

Consider AS 200 with two connections to the Internet:
- Link 1 to AS 100 (primary)
- Link 2 to AS 300 (backup)

Configuration at AS 200 routers:
- Router A (connected to AS 100): Set LOCAL-PREF = 200 for routes from AS 100
- Router B (connected to AS 300): Set LOCAL-PREF = 100 for routes from AS 300

Result: All outbound traffic from AS 200 will use the link to AS 100 (higher LOCAL-PREF), with AS 300 serving as backup. When the primary link fails, traffic automatically shifts to the backup.

### Example 3: Multi-Exit Discriminator (MED) Usage

Consider AS 100 connected to AS 200 at two locations:
- Location A: High bandwidth (10 Gbps)
- Location B: Low bandwidth (1 Gbps)

AS 100 can set MED values:
- Routes via Location A: MED = 100
- Routes via Location B: MED = 200

AS 200, upon receiving both routes, will prefer the path through Location A (lower MED) for inbound traffic from AS 100.

## Real-World Applications

### Internet Backbone Routing

BGP is the protocol that makes global Internet connectivity possible. Every Internet Service Provider participates in BGP to exchange routing information. When you access a website, your request traverses multiple autonomous systems, each making BGP routing decisions to find the optimal path. Major IXPs (Internet Exchange Points) like DE-CIX in Frankfurt and Equinix Exchange in multiple cities see billions of BGP updates daily.

### Multi-Homing for Redundancy

Enterprises and organizations connect to multiple ISPs for redundancy. BGP enables these organizations to receive full routing tables from multiple providers and implement sophisticated failover strategies. If one ISP experiences an outage, traffic automatically routes through the backup connection.

### Traffic Engineering

Service providers use BGP attributes to implement traffic engineering. By manipulating LOCAL-PREF, AS-PATH prepending (adding extra AS numbers to make a path appear longer), and MED values, operators can control which links carry traffic and how traffic flows through their network.

### Content Delivery Networks (CDN)

CDNs like Cloudflare, Akamai, and Amazon CloudFront use BGP to announce their prefixes from multiple locations worldwide. When users access content, BGP routing ensures they connect to the nearest CDN edge server, optimizing latency and performance.

### Cloud Connectivity

Enterprises connecting to public cloud platforms (AWS, Azure, Google Cloud) use BGP to exchange routes between on-premises networks and cloud virtual networks. This enables hybrid cloud architectures with seamless workload migration.

## Exam Tips

1. **Remember the four BGP message types**: OPEN establishes session, UPDATE carries routes, KEEPALIVE maintains session, NOTIFICATION reports errors.

2. **AS-PATH loop prevention**: A router rejects any route containing its own AS number in the AS-PATH attribute - this is the key loop prevention mechanism in PVR.

3. **BGP attributes order**: Remember the route selection hierarchy: LOCAL-PREF → AS-PATH length → ORIGIN → MED → eBGP/iBGP → IGP cost → Router ID.

4. **eBGP vs iBGP key differences**: eBGP changes NEXT-HOP, runs between different AS, requires direct connection; iBGP preserves NEXT-HOP, runs within same AS, no direct connection required.

5. **Path Vector vs Distance Vector**: Path Vector carries complete AS path information enabling loop prevention; Distance Vector only carries metric, making loop detection harder.

6. **BGP uses TCP port 179**: Unlike OSPF (uses IP protocol 89) and RIP (uses UDP port 520), BGP relies on TCP for reliable delivery.

7. **Private AS numbers**: Remember AS 64512 to 65534 are reserved for private use, similar to private IP addresses.

8. **LOCAL-PREF vs MED**: LOCAL-PREF affects outbound traffic (within AS), MED affects inbound traffic (from neighboring AS). LOCAL-PREF: higher is better; MED: lower is better.