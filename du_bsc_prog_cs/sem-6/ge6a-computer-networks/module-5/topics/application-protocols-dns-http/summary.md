# Application Protocols: DNS & HTTP
**Ge6A Computer Networks - BSc Physical Science (CS), Delhi University (NEP 2024)**

## Introduction

Application protocols form the backbone of network communication, enabling distributed applications to exchange data across the internet. DNS (Domain Name System) and HTTP (HyperText Transfer Protocol) are two fundamental application layer protocols that facilitate domain name resolution and web communication respectively.

## Domain Name System (DNS)

- **Purpose**: Translates human-readable domain names (e.g., www.du.ac.in) into IP addresses
- **Hierarchical Structure**: Distributed database system with root, TLD, authoritative, and recursive resolvers
- **Query Types**: 
  - *Recursive*: Full resolution by DNS server
  - *Iterative*: Step-by-step查询 with client handling referrals
- **Record Types**: A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), NS (nameserver)
- **Port Number**: Uses UDP port 53 (typically)
- **Caching**: Reduces query load; TTL (Time To Live) determines cache duration
- **Process**: Client → Recursive Resolver → Root Server → TLD Server → Authoritative Server → Response

## HyperText Transfer Protocol (HTTP)

- **Purpose**: Foundation protocol for web communication; transfers hypertext resources
- **Version Evolution**: HTTP/1.0, HTTP/1.1 (persistent connections), HTTP/2 (multiplexing), HTTP/3 (QUIC)
- **Request Methods**: GET (retrieve), POST (submit), PUT (update), DELETE (remove), HEAD, OPTIONS
- **Status Codes**: 
  - 1xx: Informational
  - 2xx: Success (200 OK, 201 Created)
  - 3xx: Redirection (301 Moved, 304 Not Modified)
  - 4xx: Client Error (400 Bad Request, 404 Not Found)
  - 5xx: Server Error (500 Internal Server Error)
- **Message Structure**: Request line/Status line, Headers, Blank line, Body
- **Stateless Protocol**: Each request is independent; sessions managed via cookies
- **Port Number**: Default port 80 (HTTP), 443 (HTTPS)
- **HTTPS**: HTTP over TLS/SSL for secure communication

## Key Differences

| Aspect | DNS | HTTP |
|--------|-----|------|
| Function | Name resolution | Web resource transfer |
| Transport | UDP primarily | TCP |
| Port | 53 | 80/443 |
| Model | Query-response | Request-response |

## Conclusion

DNS and HTTP are essential application protocols. DNS enables seamless internet access through domain name resolution, while HTTP facilitates web content delivery. Understanding their functions, message formats, and operational mechanisms is crucial for network communication and web development. These protocols are foundational as per the Delhi University Ge6A syllabus and frequently appear in examinations.