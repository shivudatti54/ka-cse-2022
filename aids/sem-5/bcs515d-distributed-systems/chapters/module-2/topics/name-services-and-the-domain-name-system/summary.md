# **Name Services and the Domain Name System**

### Definitions and Key Concepts

- **Name Service**: A system that maps names to addresses or other identifiers.
- **Domain Name System (DNS)**: A decentralized, hierarchical system for mapping names to IP addresses.
- **Resolver**: A program that queries a DNS server to resolve a domain name to an IP address.
- **Authoritative Name Server**: A DNS server that has the most up-to-date information for a domain.
- **Recursive Name Server**: A DNS server that can query other DNS servers to resolve a domain name.

### Key Components

- **Root DNS Servers**: The top-level DNS servers that manage the . (dot) top-level domain.
- **Top-Level Domain (TLD) Servers**: DNS servers that manage the . (dot) top-level domains (e.g. .com, .org).
- **Name Server Hierarchies**: A hierarchical structure of DNS servers that manage domain names.
- **DNS Queries**: Requests to a DNS server to resolve a domain name to an IP address.

### Important Formulas and Theorems

- **DNS Query Formula**:

* Query (q) = Domain name (d)
* Response (r) = IP address (i)

- **DNS Resolution Algorithm**:
  1. Query the root DNS server for the top-level domain (TLD) server.
  2. Query the TLD server for the authoritative name server.
  3. Query the authoritative name server for the IP address.

### Key Theorems

- **DNS Caching Theorem**: The DNS cache can improve response times and reduce the load on DNS servers.
- **DNS Security Theorem**: DNS can be vulnerable to attacks such as DNS spoofing and DNS amplification.

### Revision Tips

- Understand the hierarchy of DNS servers and the role of each component.
- Familiarize yourself with DNS queries and responses.
- Be able to explain the DNS resolution algorithm and the role of caching.
