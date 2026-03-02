# Border Gateway Protocol (BGP)

## Introduction

Border Gateway Protocol (BGP) is the foundational routing protocol that powers the modern Internet. As the standard exterior gateway protocol (EGP) used between autonomous systems (AS), BGP is responsible for routing traffic between different organizations, Internet service providers (ISPs), and network domains across the globe. Unlike interior gateway protocols (IGPs) such as OSPF or RIP that operate within a single autonomous system, BGP operates at a macro level, facilitating communication between different autonomous systems that have their own independent routing policies.

BGP was originally developed in 1989 as BGP-1 and has evolved through several versions, with BGP-4 (introduced in 1995) being the current standard that supports IPv4 and later IPv6. The protocol was designed with scalability and flexibility in mind, recognizing that the Internet would grow to encompass thousands of autonomous systems with diverse routing requirements. BGP's path vector mechanism, which tracks the entire path to a destination network rather than just the next hop, provides the foundation for implementing complex routing policies, including route selection based on multiple attributes, loop prevention, and policy-based routing.

In the context of 's Computer Science and Engineering curriculum, understanding BGP is essential for comprehending how the Internet functions at a macroscopic level. Network engineers and system administrators frequently encounter BGP in enterprise networks connected to multiple ISPs, data center environments, and service provider infrastructure. The protocol's importance cannot be overstated—it is estimated that virtually all Internet traffic passes through BGP-routed paths at some point in its journey from source to destination.

## Key Concepts

### Autonomous Systems (AS)

An Autonomous System (AS) is a collection of IP networks and routers under the control of a single organization that presents a common routing policy to the Internet. Each AS is assigned a unique 16-bit or 32-bit AS number (ASN) by the Internet Assigned Numbers Authority (IANA). Public ASNs range from 1 to 64511 (16-bit), while 64512 to 65535 are reserved for private use. Extended 32-bit ASNs range from 1 to 4,294,967,295. Organizations typically obtain public ASNs when they connect to more than one ISP or require specific routing policies.

### BGP Session Types

BGP operates using two primary session types that serve different networking purposes:

**External BGP (eBGP):** This session is established between routers belonging to different autonomous systems. eBGP is typically used when connecting to ISPs or establishing peering relationships between organizations. By default, the TTL (Time To Live) for eBGP packets is set to 1, meaning the sessions must be established directly between neighboring AS routers.

**Internal BGP (iBGP):** This session runs between BGP routers within the same autonomous system. iBGP is used to propagate external routes learned from eBGP peers throughout the internal network. Important characteristics of iBGP include: routes learned from one iBGP peer are not advertised to other iBGP peers (to prevent loops), and routers within the same AS may use any IGP (like OSPF or EIGRP) to reach their iBGP neighbors.

### BGP Message Types

BGP uses four distinct message types to establish and maintain neighbor relationships and exchange routing information:

**OPEN Message:** After TCP connection establishment (on port 179), BGP routers exchange OPEN messages containing parameters for the session, including BGP version, AS number, hold time, and router identifier (BGP ID - typically the highest IP address on a loopback interface).

**KEEPALIVE Message:** These messages are exchanged periodically to maintain the neighbor relationship. If no message is received within the hold time (typically 180 seconds), the BGP session is considered down. Keepalives are sent every 60 seconds by default.

**UPDATE Message:** This is the core BGP message for exchanging routing information. UPDATE messages can announce new routes (network layer reachability information with path attributes) or withdraw previously announced routes. A single UPDATE can announce multiple routes but can only withdraw one route or advertise one route, not both simultaneously.

**NOTIFICATION Message:** When a BGP error is detected, a NOTIFICATION message is sent, and the BGP session is immediately closed. Common error conditions include hold timer expiration, malformed message headers, or unsupported optional parameters.

### BGP Path Attributes

BGP path attributes provide metadata about routes that enable sophisticated routing policy implementation. Attributes are categorized as well-known (must be recognized by all BGP implementations) or optional, and as transitive or non-transitive.

**Origin (Well-known, Transitive):** Indicates how the route was learned—IGP (i), EGP (e), or incomplete (?). Routes learned through network commands in BGP are preferred (IGP), followed by EGP, then redistributed routes.

**AS_Path (Well-known, Transitive):** Lists the AS numbers through which the route has passed. This attribute is crucial for loop prevention—BGP rejects any route where its own AS number appears in the AS_Path. Shorter AS_Path is generally preferred.

**Next_Hop (Well-known, Transitive):** Specifies the IP address of the next hop router to reach the destination. For eBGP sessions, the next hop is typically changed to the IP address of the eBGP neighbor interface.

**Multi_Exit_Discriminator or MED (Optional, Transitive):** Used to influence incoming traffic from a neighboring AS. Lower MED values are preferred. Unlike Local Preference, MED is communicated to the neighboring AS but is not propagated beyond that AS.

**Local_Preference (Well-known, Transitive):** Used for outbound traffic selection within an AS. Higher values are preferred. Local Preference is only sent to iBGP peers and is not propagated to other ASs. Default value is 100.

**Community (Optional, Transitive):** A tag that allows grouping of routes for policy application. Communities can be used for filtering, marking, or influencing routing decisions. Common well-known communities include NO_EXPORT (do not advertise to eBGP peers) and NO_ADVERTISE (do not advertise to any peer).

### BGP Route Selection Process

BGP uses a sophisticated decision process (modified by path attributes) to select the best path when multiple routes to the same destination exist. The router evaluates routes in the following order, stopping at the first definitive criteria:

1. Highest Local Preference (default 100)
2. Shortest AS_Path length
3. Lowest Origin type (IGP < EGP < Incomplete)
4. Lowest MED (if comparing routes from the same neighboring AS)
5. Prefer eBGP over iBGP paths
6. Lowest IGP metric to the BGP next hop (for iBGP)
7. Lowest BGP Router ID

### BGP States

BGP neighbor relationships transition through six distinct states:

**Idle:** Initial state where the BGP process is starting or has been reset. The router initiates a TCP connection to the peer.

**Connect:** Waiting for the TCP connection to complete. If successful, the state moves to OpenSent.

**Active:** If TCP connection fails, BGP attempts to connect again. Repeated failures may indicate configuration issues.

**OpenSent:** BGP has sent an OPEN message and is waiting for an OPEN from the peer. The router verifies that the peer's AS number matches the configuration.

**OpenConfirm:** OPEN messages have been exchanged successfully. Now waiting for a KEEPALIVE or UPDATE message.

**Established:** The BGP session is fully established. KEEPALIVE messages are exchanged, and UPDATE messages can be processed.

## Examples

### Example 1: Basic BGP Configuration

Consider two autonomous systems: AS 100 (ISP) and AS 200 (Enterprise). Configure eBGP peering between routers R1 (AS 100) and R2 (AS 200).

**R1 Configuration:**

```
router bgp 100
 neighbor 192.168.1.2 remote-as 200
 network 10.0.0.0 mask 255.0.0.0
```

**R2 Configuration:**

```
router bgp 200
 neighbor 192.168.1.1 remote-as 100
 network 172.16.0.0 mask 255.255.0.0
```

**Step-by-Step Verification:**

1. Establish TCP connection on port 179
2. Exchange OPEN messages—R1 announces AS 100, R2 announces AS 200
3. Verify AS numbers match configured remote-as values
4. Sessions enter ESTABLISHED state
5. Routes are advertised via UPDATE messages
6. R1 learns 172.16.0.0/16 with next-hop 192.168.1.2
7. R2 learns 10.0.0.0/8 with next-hop 192.168.1.1

### Example 2: BGP Route Selection with Local Preference

Suppose an enterprise (AS 200) connects to two ISPs: ISP-A (AS 100) and ISP-B (AS 300). The enterprise wants all outbound traffic to prefer ISP-A as the primary path and ISP-B as backup.

**Configuration on enterprise edge routers:**

```
! On router connected to ISP-A
router bgp 200
 neighbor 203.0.113.1 remote-as 100
 neighbor 203.0.113.1 route-map SET_LOCAL_PREF out

route-map SET_LOCAL_PREF permit 10
 set local-preference 200
```

```
! On router connected to ISP-B
router bgp 200
 neighbor 198.51.100.1 remote-as 300
 neighbor 198.51.100.1 route-map SET_LOCAL_PREF out

route-map SET_LOCAL_PREF permit 10
 set local-preference 100
```

**Explanation:** Routes received from ISP-A are assigned Local Preference 200, while routes from ISP-B get the default value of 100. BGP automatically prefers higher Local Preference, so all outbound traffic will use ISP-A as the primary path.

### Example 3: AS_Path Prepending for Inbound Traffic Engineering

A multi-homed enterprise wants to influence incoming traffic to prefer the path through ISP-A. They implement AS_Path prepending through ISP-B to make that path appear less attractive.

**Configuration through ISP-B:**

```
router bgp 200
 neighbor 198.51.100.1 remote-as 300
 neighbor 198.51.100.1 route-map PREPEND_AS out

route-map PREPEND_AS permit 10
 match ip address prefix-list OUR_NETWORKS
 set as-path prepend 200 200

ip prefix-list OUR_NETWORKS permit 172.16.0.0/16
```

**Step-by-Step Analysis:**

1. Without prepending, the route to 172.16.0.0/16 is advertised with AS_PATH "200 300"
2. With prepending, AS_PATH becomes "200 200 300" (two additional AS numbers added)
3. When ISP-B advertises this route to its upstream providers, the longer AS_PATH makes the route less preferable
4. Remote networks preferring shorter AS_PATH will select ISP-A's advertisement
5. Result: Inbound traffic preferentially uses ISP-A path

## Exam Tips

1. **Remember BGP operates over TCP port 179**—unlike OSPF (protocol 89) or EIGRP (protocol 88), BGP uses reliable connection-oriented transport.

2. **Key difference between iBGP and eBGP:** iBGP does not change the next-hop address by default, while eBGP changes the next-hop to the sender's IP address. This often requires IGP redistribution or explicit next-hop-self configuration.

3. **BGP Synchronization Rule:** A BGP route will not be advertised to external peers unless the route exists in the routing table via an IGP. This rule is often disabled in modern networks due to full mesh iBGP requirements.

4. **BGP Convergence Time:** BGP is not designed for rapid convergence. The default Hold Time is 180 seconds, though in practice networks configure faster keepalive intervals (30-60 seconds).

5. **Route Flapping and BGP Stability:** BGP implements route flap damping to suppress unstable routes. Understand how penalty values increase with each flap and how routes are re-advertised after the penalty decays below the reuse threshold.

6. **iBGP Full Mesh Requirement:** All iBGP routers within an AS must be fully meshed to prevent routing loops, or use Route Reflectors/Confederations to scale the topology.

7. **BGP Attributes Priority for Selection:** Remember the order—Local Preference > AS_Path > Origin > MED > eBGP/iBGP > IGP Metric > Router ID.

8. **Common BGP States in Exam Questions:** Always identify which state involves TCP connection waiting (Connect/Active) versus waiting for OPEN messages (OpenSent/OpenConfirm).

9. **BGP Community Values:** Remember NO_EXPORT (65535:65281) prevents advertising outside the AS, while NO_ADVERTISE (65535:65282) prevents advertising to any peer.

10. **Route Aggregation:** When using aggregate-address command, the default behavior creates a summary route without attributes from the more-specific routes. Use the as-set keyword to include AS_PATH information from component routes.
