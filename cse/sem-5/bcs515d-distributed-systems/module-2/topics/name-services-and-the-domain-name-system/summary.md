# Name Services and the Domain Name System (DNS) - Summary

## Key Definitions and Concepts

- **DNS (Domain Name System)**: A distributed hierarchical naming system that translates human-readable domain names into IP addresses, functioning as the Internet's directory service.

- **DNS Namespace**: Organized as an inverted tree hierarchy with Root (.) at the top, followed by TLDs (.com, .in, .org), Second-Level Domains, and Subdomains.

- **Recursive Resolution**: A query where the DNS server performs complete name resolution on behalf of the client, contacting multiple servers and returning the final answer.

- **Authoritative Name Server**: A DNS server that holds the original zone file and has definitive knowledge of a domain's records.

## Important Formulas and Theorems

- **DNS Message Format**: Header (12 bytes) + Question + Answer + Authority + Additional sections
- **DNS Port Numbers**: Port 53 (UDP for queries, TCP for zone transfers and large responses)
- **TTL (Time-To-Live)**: Determines cache duration; typical values range from 300s to 86400s

## Key Points

- DNS operates at the Application Layer (Layer 7) of the OSI model
- There are 13 logical root server addresses (A through M) with hundreds of physical instances worldwide
- DNS uses UDP as the primary transport protocol for faster performance
- A records map to IPv4 addresses; AAAA records map to IPv6 addresses
- CNAME records create aliases but should not point to other CNAMEs
- MX records have priority values (lower = higher priority) for mail routing
- DNS caching occurs at multiple levels: browser, operating system, and recursive resolver
- Reverse DNS uses PTR records in in-addr.arpa domain for IPv4
- DNSSEC provides cryptographic authentication for DNS responses
- Every domain requires at least two authoritative name servers for redundancy

## Common Mistakes to Avoid

1. **Confusing Authoritative with Recursive**: Authoritative servers hold original zone data; recursive servers perform queries on behalf of clients.

2. **Forgetting TTL Impact**: Setting very high TTL values during domain migration causes outdated IP addresses to be served from cache.

3. **CNAME Chain Mistakes**: Creating chains of CNAME records (A→B→C) is inefficient and can cause resolution failures.

4. **MX Record Priority**: Remember that lower priority numbers indicate higher preference for mail delivery.

## Revision Tips

1. **Practice tracing DNS resolution** by using tools like `dig`, `nslookup`, or `host` - understand the output of +trace option.

2. **Memorize the DNS hierarchy order**: Root → TLD → Authoritative → Recursive resolver.

3. **Remember all resource record types** and their one-line purposes - this is frequently tested in exams.

4. **Understand the difference between iterative and recursive queries** - recursive resolvers use iterative queries to resolve names.

5. **Review DNS security concepts** including DNSSEC, cache poisoning, and DNS hijacking for complete exam preparation.
