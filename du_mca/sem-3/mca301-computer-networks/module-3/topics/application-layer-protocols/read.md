# Application Layer Protocols

## Introduction
Application layer protocols form the backbone of modern network communication, enabling end-user services and distributed applications. As the topmost layer in both OSI and TCP/IP models, these protocols directly interface with software applications to provide human-readable communication services.

In computer networks, application layer protocols define:
- Message formats for data exchange
- Rules for communication initiation/termination
- Error handling mechanisms
- Data representation standards

These protocols are crucial for implementing internet services like web browsing (HTTP), email (SMTP), file transfer (FTP), and domain resolution (DNS). With the growth of cloud computing and IoT, understanding these protocols is essential for developing secure, efficient network applications.

## Key Concepts
1. **HTTP/HTTPS**:
   - Stateless request-response protocol (port 80/443)
   - Methods: GET, POST, PUT, DELETE
   - Status codes: 1xx (Informational), 2xx (Success), 3xx (Redirection), 4xx (Client Error), 5xx (Server Error)
   - HTTPS adds TLS encryption layer

2. **SMTP/POP3/IMAP**:
   - SMTP (port 25) for sending emails
   - POP3 (port 110) and IMAP (port 143) for receiving
   - MIME extensions for multimedia content

3. **DNS**:
   - Distributed database translating domain names to IP addresses
   - Record types: A, AAAA, CNAME, MX, TXT
   - Iterative vs recursive resolution

4. **FTP/SFTP**:
   - FTP (port 21) for file transfer with separate control/data channels
   - SFTP (port 22) adds SSH encryption

5. **WebSocket**:
   - Full-duplex communication over single TCP connection (port 80/443)
   - Enables real-time web applications

## Examples

**Example 1: HTTP GET Request**
```http
GET /index.html HTTP/1.1
Host: www.du.ac.in
User-Agent: Mozilla/5.0
Accept: text/html
```

*Response:*
```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1278

<!DOCTYPE html>
<html>...</html>
```

**Example 2: DNS Resolution for "mca.du.ac.in"**
1. Client queries local DNS resolver
2. Resolver contacts root server → .in server → ac.in server → du.ac.in server
3. Authoritative server returns A record (IP address)
4. Response cached at multiple levels

**Example 3: SMTP Email Delivery**
1. Client connects to SMTP server on port 25
2. EHLO command initiates session
3. MAIL FROM: <student@du.ac.in>
4. RCPT TO: <prof@cs.du.ac.in>
5. DATA command sends message body
6. Server queues message for delivery

## Exam Tips
1. Memorize standard port numbers (HTTP=80, HTTPS=443, SMTP=25)
2. Understand differences between HTTP 1.1 vs HTTP/2 (multiplexing, header compression)
3. Compare stateful vs stateless protocols with examples
4. Draw DNS hierarchy diagram with root/TLD/authoritative servers
5. Explain TLS handshake process in HTTPS
6. Differentiate between POP3 (download-delete) and IMAP (server synchronization)
7. Describe persistent vs non-persistent HTTP connections