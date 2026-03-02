# Application Layer Protocols: FTP, SMTP, Telnet, WWW, and HTTP - Summary

## Key Definitions and Concepts

- **Application Layer:** The topmost layer of the TCP/IP model that provides network services directly to end-users and applications.
- **FTP (File Transfer Protocol):** A standard protocol for transferring files between client and server using TCP ports 20 (data) and 21 (commands).
- **SMTP (Simple Mail Transfer Protocol):** The protocol used for sending and relaying emails across networks, typically on port 25 or 587.
- **Telnet:** A protocol for bidirectional text-based communication with remote systems, operating on TCP port 23.
- **WWW (World Wide Web):** An information system using URLs to identify resources and HTTP for data communication.
- **HTTP (HyperText Transfer Protocol):** The foundation protocol for web data transfer, using a request-response model between client and server.

## Important Formulas and Theorems

- **Passive Mode Port Calculation:** Server port = (first_octet × 256) + second_octet (from PASV response)
- **URL Structure:** `protocol://hostname:port/path?query#fragment`
- **HTTP Status Code Categories:** 1xx (Informational), 2xx (Success), 3xx (Redirection), 4xx (Client Error), 5xx (Server Error)

## Key Points

- FTP operates in two modes: Active (PORT) and Passive (PASV); passive mode is more firewall-friendly.
- SMTP uses store-and-forward mechanism for emails and works with POP3/IMAP for email retrieval.
- Telnet transmits data in plain text (security risk), while SSH provides encrypted communication.
- HTTP is stateless; cookies and sessions maintain user state across requests.
- HTTP/1.1 introduced persistent connections, while HTTP/2 added multiplexing and header compression.
- MIME extends SMTP to support binary attachments and multimedia content.
- Port numbers: FTP (20/21), SMTP (25/587), Telnet (23), HTTP (80), HTTPS (443).

## Common Mistakes to Avoid

- **Confusing FTP ports:** Port 20 is for data transfer (active mode), not command transfer; port 21 handles commands.
- **Mixing up HTTP methods:** GET retrieves data, POST submits data, PUT updates entire resource, PATCH updates partially.
- **Assuming HTTP maintains state:** Remember HTTP is stateless; use cookies for session management.
- **Using Telnet for production:** Never use Telnet over untrusted networks; always use SSH for secure access.

## Revision Tips

1. Create a comparison table of all five protocols including their port numbers, purposes, and key commands.
2. Practice analyzing HTTP request/response messages by writing them out and identifying each component.
3. Remember that WWW is just one service on the Internet—the Web uses HTTP, email uses SMTP/POP3/IMAP, file transfer uses FTP.
4. Focus on understanding why certain design choices were made (e.g., stateless HTTP, MIME for SMTP) rather than just memorizing facts.
5. Solve previous year DU question papers to understand the exam pattern and frequently asked questions.