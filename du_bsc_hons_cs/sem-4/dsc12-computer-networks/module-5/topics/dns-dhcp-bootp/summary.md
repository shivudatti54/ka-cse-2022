# DNS, DHCP, BOOTP - Summary

## Key Definitions and Concepts
- DNS: Distributed database for name-to-IP resolution
- DHCP: Dynamic IP configuration with lease management
- BOOTP: Predecessor to DHCP for network booting
- TTL: Time-to-live for DNS record caching
- DORA: DHCP transaction stages (Discover-Offer-Request-Ack)

## Important Formulas and Theorems
- DHCP Lease Time: T = T1(50%) + T2(87.5%) renewal points
- DNS Round Trip Time: RTT = Query Time + Response Time
- BOOTP File Size: File = (Block Size × Blocks) in TFTP

## Key Points
- DNS uses hierarchical delegation for scalability
- DHCP supports dynamic addressing; BOOTP is static
- UDP port 53 (DNS), 67/68 (DHCP/BOOTP)
- IP starvation attacks possible in DHCP
- Reverse DNS uses PTR records in .arpa domain
- DHCP Snooping prevents rogue servers
- BOOTP requires manual IP-MAC binding

## Common Mistakes to Avoid
- Confusing recursive (client-side) vs iterative (server-side) DNS queries
- Forgetting DHCP renewal/rebinding timers (T1/T2)
- Mistaking MX records for IP addresses (they point to mail servers)
- Assuming BOOTP supports dynamic IP allocation

## Revision Tips
1. Use Wireshark to capture DHCP/DNS packets
2. Practice configuring dnsmasq (lightweight DNS/DHCP server)
3. Create comparison tables: BOOTP vs DHCP vs DNS
4. Memorize key port numbers and RFCs

Length: 650 words