# Naming and Directory Services - Summary

## Key Definitions and Concepts

- **Name**: Human-readable string identifying an entity; **Address**: Location where entity can be accessed; **Identifier**: Unique value referring to one entity throughout its lifetime
- **Name-to-address binding**: The mapping between names and their corresponding addresses
- **DNS (Domain Name System)**: Hierarchical, distributed database translating domain names to IP addresses
- **LDAP (Lightweight Directory Access Protocol)**: Lightweight protocol for accessing and managing directory services
- **Distinguished Name (DN)**: Unique path from root to entry in LDAP Directory Information Tree
- **DNSSEC**: DNS Security Extensions providing cryptographic authentication of DNS records

## Important Formulas and Theorems

- DNS uses record types: A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), NS (nameserver), SOA (Start of Authority)
- LDAP search scope: base (0), one-level (1), subtree (2)
- TTL (Time-To-Live) values control cache duration; typical values range from 300 seconds to 86400 seconds

## Key Points

1. DNS operates hierarchically with root servers at apex, TLD servers beneath, and authoritative servers for specific domains
2. Iterative resolution places burden on client-side resolver; recursive resolution offloads work to intermediate servers
3. LDAP emerged as a simplified alternative to the complex X.500 standard
4. Directory services optimize for read-heavy workloads with hierarchical query patterns
5. DNSSEC adds cryptographic signatures (RRSIG, DNSKEY, DS, NSEC records) to protect against cache poisoning
6. Caching improves performance dramatically but introduces consistency challenges when bindings change
7. LDAP uses Distinguished Names for unique identification and filters for selective retrieval

## Common Mistakes to Avoid

- Confusing iterative with recursive resolution—the client performs more work in iterative resolution
- Treating DNS and LDAP as competing technologies—they serve different but complementary purposes
- Ignoring TTL implications when updating DNS records—propagation delays affect all cached copies
- Overlooking security considerations—naming services are frequent attack vectors

## Revision Tips

1. Trace through a complete DNS resolution from client to root server to understand the full hierarchy
2. Practice constructing LDAP search filters using logical operators (AND, OR, NOT) and attribute matching
3. Review recent DNS security incidents to understand practical implications of naming service vulnerabilities
4. Compare Active Directory (Microsoft's LDAP implementation) with OpenLDAP to understand enterprise directory services