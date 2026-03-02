# World Wide Web and HTTP

## Introduction

The World Wide Web (WWW) represents one of the most significant technological innovations of the modern era, fundamentally transforming how humanity communicates, accesses information, and conducts business. Developed by Tim Berners-Lee in 1989 at CERN (European Organization for Nuclear Research), the Web was originally conceived as a means to facilitate information sharing among researchers working on large scientific projects. Today, it has evolved into a global system of interconnected documents and resources, accessible through the Internet.

The HyperText Transfer Protocol (HTTP) serves as the foundation protocol for the World Wide Web, defining how messages are formatted and transmitted between clients (typically web browsers) and servers. As an application-layer protocol operating on top of TCP/IP, HTTP governs the request-response cycle that enables web communication. Understanding HTTP is essential for computer science engineers because it underpins virtually every web-based application and service we develop or interact with daily.

This topic covers the architecture of the World Wide Web, the HTTP protocol in detail including its methods, status codes, message formats, and the crucial concept of state management through cookies. These concepts form the backbone of modern web development and are frequently tested in examinations.

## Key Concepts

### World Wide Web Architecture

The Web operates on a client-server architecture where clients (web browsers) initiate requests for web resources, and servers respond by providing those resources. The architecture consists of several key components:

**Web Client (Browser):** A software application that sends HTTP requests to servers and renders the received HTML, CSS, JavaScript, and multimedia content. Examples include Chrome, Firefox, Safari, and Edge. The browser interprets HTML documents, executes embedded scripts, and displays formatted content to users.

**Web Server:** A software application that stores web resources (HTML files, images, videos, etc.) and responds to client requests. Popular web servers include Apache HTTP Server, Nginx, Microsoft IIS, and LiteSpeed. Servers listen on well-known ports (80 for HTTP, 443 for HTTPS) to receive client requests.

**Uniform Resource Locator (URL):** The address format used to identify resources on the Web. A complete URL consists of multiple components:

```
scheme://hostname:port/path?query-string#fragment
```

For example, in `http://www.example.com:8080/index.html?id=123#section1`:

- **Scheme:** http (specifies the protocol)
- **Hostname:** www.example.com (domain name)
- **Port:** 8080 (specific port number)
- **Path:** /index.html (resource location)
- **Query String:** id=123 (parameters)
- **Fragment:** section1 (specific section within the resource)

**Domain Name System (DNS):** The system that translates human-readable domain names (like www.example.com) into IP addresses that computers use to identify each other on the network.

### HTTP Protocol Overview

HTTP is a stateless, request-response protocol that operates on the client-server model. Each request from a client to a server contains all information needed to fulfill that request, and the server does not retain information about previous requests (statelessness).

**HTTP Transaction:** An HTTP transaction consists of:

1. Client establishes TCP connection to server
2. Client sends HTTP request message
3. Server processes request and sends HTTP response
4. Server closes or maintains connection

**HTTP Versions:**

- **HTTP/1.0:** Introduced in 1996, supports basic request-response with persistent connections disabled by default
- **HTTP/1.1:** Released in 1999, adds persistent connections, chunked transfer encoding, and host header support
- **HTTP/2:** Introduced in 2015, adds multiplexing, header compression, and server push
- **HTTP/3:** Latest version using QUIC instead of TCP for improved performance

### HTTP Request Methods

HTTP defines several request methods (also called HTTP verbs) that indicate the desired action to be performed on a resource:

**GET:** Retrieves data from the server. GET requests should only retrieve data and have no side effects (idempotent). Parameters are passed in the URL query string.

**POST:** Submits data to be processed by a specified resource. POST requests typically cause state changes on the server and are not idempotent. Data is sent in the request body.

**PUT:** Uploads a representation of the specified resource. Unlike POST, PUT is idempotent—calling it multiple times produces the same result.

**DELETE:** Removes the specified resource from the server. This method is idempotent.

**HEAD:** Similar to GET but requests only the headers without the response body. Useful for checking resource existence or metadata without downloading the entire content.

**OPTIONS:** Returns the HTTP methods supported by the server for a specific URL.

**PATCH:** Applies partial modifications to a resource (unlike PUT which replaces the entire resource).

### HTTP Status Codes

HTTP response status codes indicate whether a specific HTTP request has been successfully completed. They are divided into five categories:

**1xx Informational:**

- 100 Continue: Server has received the initial part of the request
- 101 Switching Protocols: Server is switching protocols as requested

**2xx Success:**

- 200 OK: Request succeeded
- 201 Created: Request succeeded and new resource was created
- 204 No Content: Request succeeded but returns no body

**3xx Redirection:**

- 301 Moved Permanently: Resource has permanently moved to a new URL
- 302 Found: Resource temporarily resides at a different URL
- 304 Not Modified: Cached version is still valid (for conditional GET requests)

**4xx Client Errors:**

- 400 Bad Request: Server cannot process malformed request
- 401 Unauthorized: Authentication is required
- 403 Forbidden: Server refuses to authorize the request
- 404 Not Found: Requested resource does not exist
- 405 Method Not Allowed: HTTP method not supported
- 408 Request Timeout: Client timed out waiting for response

**5xx Server Errors:**

- 500 Internal Server Error: Generic server-side error
- 502 Bad Gateway: Invalid response from upstream server
- 503 Service Unavailable: Server temporarily overloaded or down for maintenance
- 504 Gateway Timeout: Upstream server failed to respond in time

### HTTP Message Format

**Request Message:**

```
METHOD /path HTTP/Version
Host: hostname
Header-Name: Header-Value

Optional Message Body
```

Example:

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

**Response Message:**

```
HTTP/Version Status-Code Status-Message
Header-Name: Header-Value

Response Body
```

Example:

```
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2024 12:28:53 GMT
Server: Apache/2.4.41
Content-Type: text/html
Content-Length: 2345

<!DOCTYPE html>
<html>
...
</html>
```

### HTTP Headers

HTTP headers allow clients and servers to pass additional information with requests and responses. They are categorized as:

**General Headers:** Apply to both request and response messages

- Date: Message creation timestamp
- Connection: Control options for the connection
- Cache-Control: Caching directives

**Request Headers:** Sent only in requests

- Host: Required header specifying the domain
- User-Agent: Client application information
- Accept: Media types the client can process
- Accept-Language: Preferred languages
- Accept-Encoding: Accepted content encodings

**Response Headers:** Sent only in responses

- Server: Server software information
- Last-Modified: Last modification date of the resource
- Content-Type: Media type of the resource
- Content-Length: Size of the response body
- Set-Cookie: Cookie to be stored at client

### Cookies and Session Management

Since HTTP is stateless, cookies were introduced to maintain stateful sessions. A cookie is a small piece of data stored on the client side and sent with each HTTP request to the originating server.

**How Cookies Work:**

1. Server sends a `Set-Cookie` header in the response
2. Browser stores the cookie locally
3. For subsequent requests to the same domain, browser includes the cookie in the `Cookie` header
4. Server uses cookie data to identify user and maintain session

**Cookie Attributes:**

- **Name=value:** Cookie identifier and its value
- **Expires:** Expiration date and time
- **Path:** URL path where cookie is valid
- **Domain:** Domain where cookie is accessible
- **Secure:** Cookie only sent over HTTPS
- **HttpOnly:** Cookie inaccessible to JavaScript

**Cookie Types:**

- **Session Cookies:** Exist only while the browser is open (no expiration)
- **Persistent Cookies:** Remain until expiration date
- **Third-Party Cookies:** Created by domains other than the one visited

### HTTPS (HTTP Secure)

HTTPS is the secure version of HTTP that uses SSL/TLS (Secure Sockets Layer/Transport Layer Security) encryption for all communication. It provides:

- **Confidentiality:** Data is encrypted and cannot be read by intermediaries
- **Integrity:** Data cannot be modified during transmission
- **Authentication:** Verifies the server's identity through certificates

## Examples

### Example 1: Analyzing a Complete HTTP Request-Response

**Client Request:**

```
GET /courses/computer-networks HTTP/1.1
Host: www.-academy.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate
Connection: keep-alive
```

**Server Response:**

```
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2024 10:30:00 GMT
Server: Apache/2.4.52
Last-Modified: Fri, 24 Jul 2024 09:15:30 GMT
ETag: "abc123"
Accept-Ranges: bytes
Content-Length: 45678
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html>
<head><title>Computer Networks Course</title></head>
<body>
<h1>Computer Networks</h1>
<p>Welcome to the CN course...</p>
</body>
</html>
```

**Analysis:**

- Request method: GET (retrieving /courses/computer-networks)
- HTTP version: 1.1
- Response status: 200 OK (success)
- Content-Type: HTML document
- Content-Length: 45678 bytes
- Connection: keep-alive (persistent connection)

### Example 2: Form Submission Using POST

Consider a login form submission:

**Client Request:**

```
POST /login HTTP/1.1
Host: www.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 47

username=student&password=pass123&remember=on
```

**Server Response:**

```
HTTP/1.1 302 Found
Location: /dashboard
Set-Cookie: session_id=xyz789; HttpOnly; Secure
Content-Length: 0
```

**Analysis:**

- POST method used (sensitive data in body, not URL)
- Content-Type indicates URL-encoded form data
- Server returns 302 redirect to /dashboard
- Set-Cookie header creates a session cookie

### Example 3: Conditional GET Request

**Initial Request:**

```
GET /files/document.pdf HTTP/1.1
Host: docs.example.com
```

**Initial Response:**

```
HTTP/1.1 200 OK
Last-Modified: Mon, 20 Jul 2024 14:30:00 GMT
ETag: "1234-5678"
Content-Length: 102400

[Document content...]
```

**Subsequent Conditional Request:**

```
GET /files/document.pdf HTTP/1.1
Host: docs.example.com
If-Modified-Since: Mon, 20 Jul 2024 14:30:00 GMT
If-None-Match: "1234-5678"
```

**Conditional Response:**

```
HTTP/1.1 304 Not Modified
ETag: "1234-5678"
```

**Analysis:**

- Client caches the document with ETag and Last-Modified
- Subsequent request includes conditional headers
- Server checks if resource changed (it hasn't)
- Returns 304 Not Modified (saves bandwidth)
- Client uses cached copy

## Exam Tips

1. **Remember the URL Structure:** Understand all components of a URL including scheme, hostname, port, path, query string, and fragment. This is a common exam question.

2. **Distinguish Between GET and POST:** GET passes data in URL query strings (visible, bookmarkable, limited length), while POST passes data in message body (secure, no size limit, not bookmarkable).

3. **Memorize Common Status Codes:** Focus on 200 (OK), 301/302 (redirects), 400 (bad request), 401/403 (authentication), 404 (not found), 500 (server error).

4. **HTTP is Stateless:** Understand that each request is independent and the server doesn't remember previous requests. Explain how cookies solve this problem.

5. **Know HTTP Header Categories:** Be able to distinguish between general, request, and response headers and give examples of each.

6. **HTTPS vs HTTP:** Understand that HTTPS uses SSL/TLS encryption and operates on port 443 (HTTP uses port 80).

7. **Idempotent Methods:** Remember that GET, HEAD, PUT, and DELETE are idempotent (multiple identical requests have the same effect), while POST and PATCH are not.

8. **Persistent Connections:** Understand HTTP/1.1's persistent connection feature that allows multiple requests over a single TCP connection, improving efficiency.

9. **Cookie Purpose and Attributes:** Know why cookies are needed (state management) and important attributes like Expires, Path, Domain, Secure, and HttpOnly.

10. **HTTP/1.1 vs HTTP/2:** Know key differences: HTTP/2 supports multiplexing, header compression, and server push.
