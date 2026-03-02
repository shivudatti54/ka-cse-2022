# Domain Name System (DNS) - Summary

## Key Definitions and Concepts

- **DNS (Domain Name System):** A distributed hierarchical naming system that translates human-readable domain names into numerical IP addresses.

- **Name Resolution:** The process of converting domain names to IP addresses, the core function of DNS.

- **Authoritative Server:** A DNS server that holds the original zone data and provides definitive answers for a domain.

- **Recursive Resolver:** A DNS server that performs complete resolution on behalf of clients by querying other servers.

## Important Formulas and Concepts

- **DNS Hierarchy:** Root (.) → TLD (.com, .org) → Second-Level Domain → Subdomain

- **TTL (Time-To-Live):** Determines cache duration; typical values range from 300 seconds (5 minutes) to 86400 seconds (24 hours).

- **Root Servers:** 13 logical root server IP addresses (A-M) managed by ICANN.

## Key Points

- DNS solves the problem of memorizing IP addresses by providing a human-readable naming system.

- The DNS query process typically involves: Client → Recursive Resolver → Root Server → TLD Server → Authoritative Server → Response.

- DNS records are cached at multiple levels (browser, OS, resolver) to improve performance.

- A records map domains to IPv4; AAAA records map to IPv6 addresses.

- CNAME records create aliases but cannot coexist with other record types for the same name.

- MX records specify mail servers with priority values (lower number = higher priority).

- DNSSEC adds cryptographic authentication to verify DNS response authenticity.

- DNS uses both UDP (typically port 53) and TCP for zone transfers.

## Common Mistakes to Avoid

- Confusing recursive and iterative queries—recursive provides complete answers, iterative provides referrals.

- Forgetting that CNAME records cannot be used alongside other record types for the same domain.

- Assuming DNS resolution is instantaneous; caching and TTL values affect propagation times.

- Misunderstanding MX record priority—lower numeric values indicate higher preference.

## Revision Tips

1. Draw the complete DNS resolution flow from typing a URL to receiving an IP address.

2. Create a table comparing all DNS record types with their purposes and examples.

3. Practice tracing DNS queries using tools like `nslookup`, `dig`, or `host` on real domains.

4. Remember the hierarchy: Root → TLD → Authoritative is the fundamental structure to memorize.
