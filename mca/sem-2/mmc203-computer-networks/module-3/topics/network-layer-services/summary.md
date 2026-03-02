# Network Layer Services - Summary

## Key Definitions and Concepts

- **Network Layer**: Layer 3 of OSI model responsible for end-to-end packet delivery across networks
- **Routing**: Process of determining the best path for packets from source to destination
- **Forwarding**: Actual transfer of packets from input to output interface based on routing table
- **Logical Addressing**: Hierarchical addressing (IP) that can be assigned and configured independently of hardware
- **Subnetting**: Division of a larger network into smaller subnets using subnet masks
- **CIDR**: Classless Inter-Domain Routing using prefix length notation (e.g., /24)
- **NAT**: Network Address Translation mapping private IPs to public IPs
- **Longest Prefix Match**: Routing lookup algorithm preferring routes with longest matching network prefix

## Important Formulas and Theorems

- **Subnet formula**: Number of subnets = 2^n (where n = borrowed bits)
- **Hosts per subnet**: 2^h - 2 (where h = remaining host bits, subtract network and broadcast)
- **Block size**: 256 - (last non-zero octet of subnet mask)
- **IPv4 Header minimum**: 20 bytes (without options)
- **IPv4 address size**: 32 bits (IPv6 uses 128 bits)

## Key Points

1. The network layer provides best-effort delivery without guarantees of reliability or ordering
2. IPv4 uses 32-bit addresses allowing approximately 4.3 billion unique addresses
3. Private IP ranges (10.x.x.x, 172.16-31.x.x, 192.168.x.x) require NAT for internet access
4. TTL field prevents packets from circulating indefinitely due to routing loops
5. Fragmentation occurs when packet size exceeds MTU; can be prevented using DF flag
6. Routing protocols converge to share network topology information
7. Routers make forwarding decisions based on destination IP address and routing table
8. ICMP works at network layer but supports higher layer protocols through error reporting

## Common Mistakes to Avoid

1. Confusing subnet mask /24 with 255.255.255.0 - they are equivalent but different notations
2. Forgetting to subtract 2 from host count (network and broadcast addresses are unusable)
3. Using default classful masks instead of CIDR when subnetting classful networks
4. Confusing routing (path determination) with forwarding (packet movement)
5. Assuming fragmented packets take the same path - each fragment is routed independently

## Revision Tips

1. Practice subnetting problems daily to build speed and accuracy
2. Memorize the protocol numbers (TCP=6, UDP=17, ICMP=1, OSPF=89)
3. Draw the IPv4 header structure and label all fields for visual memory
4. Remember that routers operate at Layer 3 and examine/modify IP headers
5. When solving routing problems, always apply Longest Prefix Match rule
