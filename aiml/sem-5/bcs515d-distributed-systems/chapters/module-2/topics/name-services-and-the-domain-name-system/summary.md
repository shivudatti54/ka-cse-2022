# Name Services and the Domain Name System

=====================================

### Introduction

The Domain Name System (DNS) is a system of hierarchical databases that translate human-readable domain names into IP addresses.

### Key Points

- **Definition:** A system that maps human-readable names to IP addresses or other domain names.
- **Components:**
  - Name servers: store and manage DNS records.
  - DNS resolver: finds the IP address associated with a domain name.
  - DNS query: a request to find the IP address associated with a domain name.
- **Protocols:**
  - DNS (Domain Name System) protocol: used for DNS queries and responses.
  - DHCP (Dynamic Host Configuration Protocol): used for assigning IP addresses.

### DNS Operations

- **Resolution process:**
  1.  DNS query sent to a resolver.
  2.  Resolver queries a name server.
  3.  Name server responds with IP address or a redirect to another name server.
  4.  Resolver caches the response for future requests.
- **Types of DNS records:**
  - A (Address): maps a domain name to an IP address.
  - AAAA (Address): maps a domain name to an IPv6 address.
  - MX (Mail Exchange): maps a domain name to a mail server.

### Theorems and Formulas

- **DNS lookup formula:** `IP = DNS(query, name_server)`
- **Time to First Byte (TTFB):** measures the time it takes for a DNS query to return an IP address.
- **Root zone:** the top-level domain of the DNS hierarchy.

### Key Concepts

- **Root domain:** the top-level domain of the DNS hierarchy.
- **Top-down resolution:** resolving a domain name from the top-level domain to the lowest level.
- **Bottom-up resolution:** resolving a domain name from the lowest level to the top-level domain.

### Important Formulas (continued)

- **DNS query response time:** `T = TTFB + response_time`
- **DNS lookup time:** `L = TTFB + response_time + caching_time`

### Quick Revision Tips

- Remember the DNS resolution process: DNS query -> resolver -> name server -> response.
- Familiarize yourself with DNS record types: A, AAAA, MX.
- Understand the role of name servers and resolvers in DNS operations.
