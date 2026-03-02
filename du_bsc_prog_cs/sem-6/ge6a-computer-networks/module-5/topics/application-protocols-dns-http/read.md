# Application Protocols: DNS and HTTP

## Comprehensive Study Material for Ge6A Computer Networks

---

## 1. Introduction

The modern internet relies on a layered architecture where application protocols serve as the foundation for user-facing services. Among these, the Domain Name System (DNS) and Hypertext Transfer Protocol (HTTP) stand as two of the most critical protocols that enable internet communication. Understanding these protocols is essential for any computer networks student at Delhi University, as they form the backbone of how we access websites, send emails, and interact with networked applications.

In our daily lives, we interact with these protocols constantly without even noticing. When you type "google.com" in your browser, DNS translates this human-readable name into an IP address (like 142.250.190.46) that computers use to locate the server. Then, HTTP (or its secure variant HTTPS) handles the actual communication between your browser and Google's servers to fetch the webpage content. This seamless process happens in milliseconds, enabling the instant access to information we now expect.

This study material aligns with the Ge6A Computer Networks syllabus for BSc Physical Science (CS) under NEP 2024, covering all essential concepts with detailed explanations, practical examples, and comprehensive assessment items.

---

## 2. Domain Name System (DNS)

### 2.1 What is DNS?

The Domain Name System (DNS) is a hierarchical and decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities. Most importantly, it translates human-readable domain names (like `www.example.com`) into numerical IP addresses (like `93.184.216.34`) needed for locating and identifying computer services and devices with the underlying network protocols.

### 2.2 Why Do We Need DNS?

Without DNS, users would need to remember the IP address of every website they want to visit—a nearly impossible task given that:

- IP addresses are difficult to remember (e.g., 142.250.190.46 vs. google.com)
- IP addresses can change due to server maintenance or load balancing
- DNS provides flexibility in changing infrastructure without affecting user experience

### 2.3 DNS Hierarchy

DNS uses a hierarchical tree structure:

```
                         (.)
                        / | \
                       /  |  \
                     .com .org .edu (TLDs)
                     /     |      \
                google   wikipedia  mit  (Second-Level Domains)
                   |        |
                  www      en        (Subdomains)
```

**Root Domain (.)**: The top of the DNS hierarchy, represented by a dot.

**Top-Level Domains (TLDs)**: The highest level of the DNS hierarchy after the root. Common TLDs include:
- Generic TLDs (gTLD): .com, .org, .net, .edu, .gov
- Country Code TLDs (ccTLD): .in, .us, .uk, .cn

**Second-Level Domains**: The domain name directly before the TLD (e.g., "google" in "google.com")

**Subdomains**: Additional domains under the second-level domain (e.g., "mail.google.com", "www.google.com")

### 2.4 DNS Query Types

#### Recursive Query
In a recursive query, the DNS server (typically your ISP's resolver) performs the complete resolution process on behalf of the client. If the resolver doesn't have the answer cached, it contacts other DNS servers until it gets the final answer or determines the domain doesn't exist.

**Process**: Client → Local DNS Server → Root Server → TLD Server → Authoritative Server → Local DNS Server → Client

#### Iterative Query
In an iterative query, the DNS server returns the best answer it can provide. If it doesn't have the requested record, it returns referrals to other DNS servers that might have the information. The client then queries those servers directly.

**Process**: Client → Local DNS Server → Root Server (returns TLD server) → Local DNS Server → TLD Server (returns authoritative server) → Local DNS Server → Authoritative Server → Client

### 2.5 DNS Resolution Process

Here's a step-by-step breakdown of what happens when you type "www.example.com" in your browser:

1. **Browser Check**: The browser first checks its cache, then the operating system's cache for the IP address.

2. **Local DNS Resolver**: If not found, the query goes to the local DNS resolver (usually provided by your ISP).

3. **Root Server Query**: The resolver queries a root DNS server. The root server responds with the address of the .com TLD server.

4. **TLD Server Query**: The resolver queries the .com TLD server, which responds with the authoritative DNS server for example.com.

5. **Authoritative Server Query**: The resolver queries the authoritative DNS server for example.com, which returns the IP address for www.example.com.

6. **Response to Client**: The resolver returns the IP address to the browser, which can now establish a connection to the web server.

### 2.6 DNS Resource Records

DNS servers store information in resource records (RRs). Common record types include:

| Record Type | Description | Example |
|-------------|-------------|---------|
| **A** | Maps a domain to an IPv4 address | example.com → 93.184.216.34 |
| **AAAA** | Maps a domain to an IPv6 address | example.com → 2606:2800:220:1:248:1893:25c8:1946 |
| **CNAME** | Creates an alias from one domain to another | blog.example.com → example.wordpress.com |
| **MX** | Specifies mail servers for the domain | mail.example.com → 10 mail.example.com |
| **TXT** | Provides text information for verification | v=spf1 include:_spf.google.com ~all |
| **NS** | Delegates authority to DNS servers | example.com → ns1.example.com |
| **SOA** | Contains administrative information | Serial: 2024010101, Refresh: 3600 |

### 2.7 DNS Caching

DNS caching is a mechanism where DNS query results are temporarily stored to reduce latency and decrease the load on DNS servers. Caching occurs at multiple levels:

**Browser Cache**: Modern browsers cache DNS records for a limited time.

**Operating System Cache**: OS-level DNS cache (can be viewed with `ipconfig /displaydns` on Windows or `scutil --dns` on macOS).

**ISP/Resolver Cache**: Local DNS servers cache records according to their TTL values.

### 2.8 Time To Live (TTL)

TTL is a value in a DNS record that specifies how long (in seconds) the record should be cached before being discarded and re-fetched. Typical TTL values:

- **Low TTL (300 seconds/5 minutes)**: Used for frequently changing records
- **Medium TTL (3600 seconds/1 hour)**: Common default value
- **High TTL (86400 seconds/24 hours)**: Used for stable, rarely changing records

**Example**: If you set TTL=3600 for your domain's A record, DNS resolvers will cache that record for one hour before querying your DNS server again.

### 2.9 DNSSEC (DNS Security Extensions)

DNSSEC is a security protocol that adds authentication to DNS queries. It ensures that:

- The response comes from an authentic DNS server
- The data hasn't been tampered with during transit
- The response is not fake (protecting against DNS spoofing/poisoning attacks)

DNSSEC works by signing DNS records with cryptographic keys. When you query a DNSSEC-signed domain, the server provides digital signatures along with the records. Your resolver verifies these signatures before accepting the data.

**DNSKEY Record**: Contains the public key used to verify signatures
**RRSIG Record**: Contains the cryptographic signature
**DS Record**: Delegates trust between parent and child zones

### 2.10 DNS Example with Command-Line Tools

You can use various tools to query DNS records:

```bash
# Query A record (IPv4 address)
dig A example.com

# Query AAAA record (IPv6 address)
dig AAAA example.com

# Query MX records (mail servers)
dig MX example.com

# Query with specific DNS server
dig @8.8.8.8 A example.com

# View full response with additional sections
dig +noall +answer +multiline example.com

# Use nslookup (simpler tool)
nslookup example.com
nslookup -type=MX example.com
```

**Sample Output**:
```
; <<>> DiG 9.18.1 <<>> A example.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;example.com.			IN	A

;; ANSWER SECTION:
example.com.		86400	IN	A	93.184.216.34
```

---

## 3. Hypertext Transfer Protocol (HTTP)

### 3.1 What is HTTP?

The Hypertext Transfer Protocol (HTTP) is an application-layer protocol for transmitting hypermedia documents, such as HTML. It was designed for communication between web browsers and web servers, but can also be used for other purposes. HTTP follows a request-response model where the client sends a request and the server returns a response.

HTTP is stateless, meaning each request is independent, and the server doesn't retain information about previous requests from the same client.

### 3.2 HTTP Request/Response Model

**HTTP Request Structure**:
```
METHOD /path/to/resource HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Accept-Language: en-US
[Empty Line]
[Optional Request Body]
```

**HTTP Response Structure**:
```
HTTP/1.1 200 OK
Date: Mon, 01 Jan 2024 12:00:00 GMT
Server: Apache/2.4.41
Content-Type: text/html
Content-Length: 1256
[Empty Line]
<!DOCTYPE html>
<html>
<body>
<h1>Welcome</h1>
...
</body>
</html>
```

### 3.3 HTTP Methods

HTTP defines several methods (also called verbs) that indicate the desired action to be performed on a resource:

| Method | Description | Idempotent | Safe |
|--------|-------------|------------|------|
| **GET** | Retrieve a resource | Yes | Yes |
| **POST** | Submit data to be processed | No | No |
| **PUT** | Replace a resource entirely | Yes | No |
| **PATCH** | Partially modify a resource | No | No |
| **DELETE** | Remove a resource | Yes | No |
| **HEAD** | Like GET but only headers | Yes | Yes |
| **OPTIONS** | Returns supported methods | Yes | Yes |
| **CONNECT** | Establish tunnel connection | Yes | No |

**Detailed Explanations**:

- **GET**: Used to request data from a specified resource. GET requests should only retrieve data and have no other effect. Parameters are passed in the URL query string.

  ```
  GET /api/users?id=123 HTTP/1.1
  Host: api.example.com
  ```

- **POST**: Submits data to be processed to a specified resource. Often used for form submissions, API data submission. Data is sent in the request body.

  ```
  POST /api/users HTTP/1.1
  Host: api.example.com
  Content-Type: application/json
  
  {"name": "John", "email": "john@example.com"}
  ```

- **PUT**: Replaces all current representations of the target resource with the request payload.

  ```
  PUT /api/users/123 HTTP/1.1
  Host: api.example.com
  Content-Type: application/json
  
  {"name": "John Doe", "email": "johndoe@example.com"}
  ```

- **PATCH**: Applies partial modifications to a resource.

  ```
  PATCH /api/users/123 HTTP/1.1
  Host: api.example.com
  Content-Type: application/json
  
  {"email": "newemail@example.com"}
  ```

- **DELETE**: Removes the specified resource.

  ```
  DELETE /api/users/123 HTTP/1.1
  Host: api.example.com
  ```

### 3.4 HTTP Status Codes

HTTP response status codes indicate whether a specific HTTP request has been successfully completed. They are divided into five classes:

**1xx - Informational**: Request received, continuing process

| Code | Meaning |
|------|---------|
| 100 | Continue - Client should continue with request |
| 101 | Switching Protocols - Server is switching protocols |

**2xx - Success**: Request successfully received, understood, and accepted

| Code | Meaning |
|------|---------|
| 200 | OK - Request succeeded |
| 201 | Created - Resource successfully created |
| 204 | No Content - Request succeeded, no content to return |
| 206 | Partial Content - Server is delivering part of the resource |

**3xx - Redirection**: Further action must be taken to complete request

| Code | Meaning |
|------|---------|
| 301 | Moved Permanently - Resource has permanently moved |
| 302 | Found - Resource temporarily at different URI |
| 304 | Not Modified - Cached version is still valid |
| 307 | Temporary Redirect - Temporary redirect, use same method |
| 308 | Permanent Redirect - Permanent redirect, use same method |

**4xx - Client Error**: Request contains bad syntax or cannot be fulfilled

| Code | Meaning |
|------|---------|
| 400 | Bad Request - Server cannot process malformed request |
| 401 | Unauthorized - Authentication required |
| 403 | Forbidden - Server refuses to authorize request |
| 404 | Not Found - Resource not found |
| 405 | Method Not Allowed - HTTP method not supported |
| 409 | Conflict - Request conflicts with current state |
| 429 | Too Many Requests - Rate limit exceeded |

**5xx - Server Error**: Server failed to fulfill valid request

| Code | Meaning |
|------|---------|
| 500 | Internal Server Error - Generic server error |
| 501 | Not Implemented - Server doesn't support functionality |
| 502 | Bad Gateway - Invalid response from upstream server |
| 503 | Service Unavailable - Server temporarily overloaded |
| 504 | Gateway Timeout - Upstream server timed out |

### 3.5 HTTP Headers

HTTP headers let the client and server pass additional information with an HTTP request or response.

**Common Request Headers**:

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Cookie: session_id=abc123; preferences=light
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
Cache-Control: no-cache
```

**Common Response Headers**:

```
HTTP/1.1 200 OK
Date: Mon, 01 Jan 2024 12:00:00 GMT
Server: Apache/2.4.52
Content-Type: text/html; charset=UTF-8
Content-Length: 5234
Cache-Control: max-age=3600
Set-Cookie: session_id=xyz789; HttpOnly; Secure; SameSite=Strict
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Last-Modified: Mon, 01 Jan 2024 10:00:00 GMT
```

**Important Header Categories**:

1. **General Headers**: Date, Connection, Cache-Control, Pragma
2. **Request Headers**: Host, User-Agent, Accept, Authorization, Cookie
3. **Response Headers**: Server, Set-Cookie, WWW-Authenticate
4. **Entity Headers**: Content-Type, Content-Length, Content-Encoding, ETag

### 3.6 HTTP/1.0 vs HTTP/1.1 vs HTTP/2 vs HTTP/3

| Feature | HTTP/1.0 | HTTP/1.1 | HTTP/2 | HTTP/3 |
|---------|----------|----------|--------|--------|
| **Connection** | New connection per request | Persistent connection | Multiplexed | QUIC (UDP-based) |
| **Header Compression** | None | None | HPACK | QPACK |
| **Server Push** | No | No | Yes | Yes |
| **Binary Protocol** | Text | Text | Binary | Binary |
| **HOL Blocking** | Yes | Yes | Partially | No |
| **Security** | Optional | Optional | Optional | Mandatory (in most impl) |

**HTTP/1.1 Improvements**:
- Persistent connections (keep-alive)
- Pipelining (later removed due to issues)
- Chunked transfer encoding
- Virtual hosting (Host header required)

**HTTP/2 Features**:
- **Multiplexing**: Multiple requests/responses over single TCP connection
- **Server Push**: Server proactively sends resources to client
- **Header Compression**: HPACK reduces overhead
- **Stream Prioritization**: Client can prioritize certain resources
- **Binary Framing**: More efficient parsing

**HTTP/3 Features**:
- **QUIC Protocol**: Built on UDP instead of TCP
- **0-RTT Connections**: Faster connection establishment
- **No HOL Blocking**: Head-of-line blocking eliminated at connection level
- **Improved Congestion Control**: Better handling of network conditions
- **Connection Migration**: Connections survive network changes

### 3.7 HTTPS (HTTP Secure)

HTTPS is the secure version of HTTP, using TLS (Transport Layer Security) or SSL (Secure Sockets Layer) to encrypt communications between the client and server.

**How HTTPS Works**:

1. **Client Hello**: Client sends supported cipher suites and random bytes
2. **Server Hello**: Server selects cipher, sends certificate and random bytes
3. **Certificate Verification**: Client verifies server's certificate against trusted CAs
4. **Key Exchange**: Client generates pre-master secret, encrypts with server's public key
5. **Session Keys**: Both parties derive session keys from the pre-master secret
6. **Secure Communication**: All data encrypted with session keys

**HTTPS Certificate Types**:
- **DV (Domain Validation)**: Basic validation, proves domain ownership
- **OV (Organization Validation)**: Validates organization identity
- **EV (Extended Validation)**: Highest validation, green address bar

### 3.8 Cookies and Sessions

**Cookies** are small pieces of data stored on the client's browser, sent with each HTTP request to the server. They enable stateful communication over HTTP.

**Cookie Types**:
- **Session Cookies**: Exist only while the browser is open, deleted on close
- **Persistent Cookies**: Remain until expiration date
- **Secure Cookies**: Only sent over HTTPS
- **HttpOnly Cookies**: Cannot be accessed via JavaScript (XSS protection)
- **SameSite Cookies**: Controls cross-site request forgery (CSRF)

**Example Cookie Header**:
```
Set-Cookie: session_id=abc123xyz; Expires=Wed, 01 Jan 2025 00:00:00 GMT; Path=/; HttpOnly; Secure; SameSite=Strict
```

**Sessions** maintain state across multiple requests. The server stores session data (typically in memory or database) and associates it with a session ID. The client stores this ID in a cookie.

**Session Flow**:
1. Client sends login credentials
2. Server validates, creates session, stores data, sends session ID in cookie
3. Client sends session ID with subsequent requests
4. Server retrieves session data, authenticates request

### 3.9 HTTP Example with cURL

```bash
# Basic GET request
curl https://api.example.com/users

# GET with headers
curl -H "Authorization: Bearer token123" \
     -H "Accept: application/json" \
     https://api.example.com/users/123

# POST request with JSON body
curl -X POST https://api.example.com/users \
     -H "Content-Type: application/json" \
     -d '{"name": "John", "email": "john@example.com"}'

# POST with form data
curl -X POST https://api.example.com/login \
     -d "username=john&password=secret"

# PUT request
curl -X PUT https://api.example.com/users/123 \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe"}'

# DELETE request
curl -X DELETE https://api.example.com/users/123

# Follow redirects
curl -L https://short.url/abc

# Verbose output to see request/response headers
curl -v https://api.example.com/data
```

**Sample HTTP Request and Response**:

```http
#### Request:
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: curl/7.88.1
Accept: */*

#### Response:
HTTP/1.1 200 OK
Server: nginx/1.18.0
Date: Mon, 01 Jan 2024 12:00:00 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 612
Connection: keep-alive

<!DOCTYPE html>
<html>
<head>
    <title>Example Domain</title>
</head>
<body>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents.</p>
</body>
</html>
```

---

## 4. Key Takeaways

### DNS Essentials:
- DNS translates human-readable domain names into IP addresses
- DNS uses a hierarchical system: Root → TLD → Authoritative → Subdomain
- DNS queries can be recursive (full resolution) or iterative (step-by-step referrals)
- Resource records (A, AAAA, CNAME, MX, TXT, NS, SOA) store different types of DNS information
- TTL determines how long DNS records are cached
- DNSSEC adds cryptographic authentication to DNS responses for security

### HTTP Essentials:
- HTTP is a stateless request-response protocol operating at the application layer
- HTTP methods (GET, POST, PUT, PATCH, DELETE) define the action to be performed
- Status codes (1xx-5xx) indicate the outcome of the request
- Headers provide metadata about requests and responses
- HTTP/2 introduced multiplexing and server push; HTTP/3 uses QUIC protocol
- HTTPS adds TLS encryption for secure communication
- Cookies and sessions enable stateful behavior over stateless HTTP

---

## 5. Assessment Section

### Multiple Choice Questions (MCQs)

#### Easy Level

**Q1. What does DNS stand for?**
- a) Digital Network System
- b) Domain Name System
- c) Data Network Service
- d) Dynamic Name Server

**Q2. Which DNS record type maps a domain name to an IPv4 address?**
- a) AAAA
- b) CNAME
- c) A
- d) MX

**Q3. Which HTTP method is used to retrieve data from a server?**
- a) POST
- b) PUT
- c) GET
- d) DELETE

#### Medium Level

**Q4. In DNS resolution, which server type is queried first by a local resolver after checking its cache?**
- a) Authoritative DNS server
- b) Root DNS server
- c) TLD DNS server
- d) Recursive resolver

**Q5. What does TTL stand for in the context of DNS?**
- a) Time To Load
- b) Transfer Time Limit
- c) Time To Live
- d) Token Transfer Latency

**Q6. Which HTTP status code indicates that a resource has permanently moved to a new URL?**
- a) 302
- b) 304
- c) 301
- d) 404

**Q7. What is the main security improvement of HTTPS over HTTP?**
- a) Faster connection
- b) Data encryption
- c) Compression
- d) Persistent connections

#### Hard Level

**Q8. In HTTP/2, which feature allows the server to send additional resources to the client without explicit request?**
- a) Multiplexing
- b) Server Push
- c) Header Compression
- d) Stream Prioritization

**Q9. Which HTTP header attribute prevents cookies from being accessed by JavaScript, providing protection against XSS attacks?**
- a) Secure
- b) SameSite
- c) HttpOnly
- d) Path

**Q10. DNSSEC primarily protects against which type of attack?**
- a) SQL Injection
- b) Cross-Site Scripting
- c) DNS Spoofing/Poisoning
- d) Man-in-the-Middle

**Q11. Which of the following is NOT an improvement in HTTP/3 over HTTP/2?**
- a) Uses QUIC protocol
- b) Built on UDP instead of TCP
- c) Uses HPACK for header compression
- d) Eliminates HOL blocking at connection level

**Q12. A user attempts to access a resource and receives a 405 Method Not Allowed error. What does this indicate?**
- a) The resource has been permanently moved
- b) The requested HTTP method is not supported for this resource
- c) The server is temporarily unavailable
- d) The user is not authorized to access the resource

### Flashcards

**Flashcard 1**
> **Term**: Recursive DNS Query
> **Definition**: A query where the DNS server performs the complete resolution process on behalf of the client, contacting other DNS servers as needed until it returns the final answer.

**Flashcard 2**
> **Term**: CNAME Record
> **Definition**: A Canonical Name record that creates an alias from one domain name to another, allowing multiple names to point to the same IP address.

**Flashcard 3**
> **Term**: Idempotent Method
> **Definition**: An HTTP method that can be called multiple times without producing different results beyond the initial application (e.g., GET, PUT, DELETE).

**Flashcard 4**
> **Term**: Cookie
> **Definition**: A small piece of data stored on the client's browser by the server, sent with each HTTP request to maintain state and session information.

**Flashcard 5**
> **Term**: TLS Handshake
> **Definition**: The process of establishing a secure HTTPS connection where the client and server exchange cryptographic keys and verify certificates.

**Flashcard 6**
> **Term**: HTTP/2 Multiplexing
> **Definition**: A feature allowing multiple HTTP requests and responses to be sent simultaneously over a single TCP connection, eliminating HOL blocking.

### Short Answer Questions

1. Explain the difference between recursive and iterative DNS queries.
2. Describe the process of DNS resolution when a user types "www.google.com" in a browser.
3. List and explain at least four HTTP methods and their purposes.
4. Differentiate between HTTP/1.1 and HTTP/2, highlighting key improvements.
5. Explain how cookies work and list at least three cookie attributes and their purposes.
6. What is DNSSEC and what security problems does it address?
7. Explain the difference between the HTTP status codes 301, 302, and 307.
8. How does HTTPS ensure secure communication between client and server?

---

## 6. References and Syllabus Alignment

This study material covers the following topics from the Ge6A Computer Networks syllabus for BSc Physical Science (CS) - Delhi University NEP 2024:

- Application Layer Protocols
- Domain Name System (DNS) - resolution, hierarchy, caching, security
- HTTP Protocol - methods, status codes, headers, versions
- Web Technologies - cookies, sessions, HTTPS

**Recommended Further Reading**:
- Kurose & Ross, "Computer Networking: A Top-Down Approach"
- Tanenbaum, "Computer Networks"
- RFC 1035 (DNS)
- RFC 7231 (HTTP/1.1)
- RFC 7540 (HTTP/2)
- RFC 9110 (HTTP Semantics)

---

*Study Material prepared for Delhi University, NEP 2024 - Ge6A Computer Networks*