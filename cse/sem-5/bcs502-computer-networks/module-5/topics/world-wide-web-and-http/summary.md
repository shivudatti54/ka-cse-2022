# World Wide Web and HTTP - Summary

## Key Definitions and Concepts

- **World Wide Web (WWW):** A global system of interconnected documents and resources accessible via the Internet, using HTTP as the underlying communication protocol.

- **HTTP (HyperText Transfer Protocol):** An application-layer protocol that defines how messages are formatted and transmitted between web clients and servers.

- **URL (Uniform Resource Locator):** The address format for resources on the Web: `scheme://hostname:port/path?query-string#fragment`

- **Cookie:** A small piece of data stored on the client side to maintain session state across HTTP requests.

- **HTTPS:** HTTP over SSL/TLS, providing encrypted communication and server authentication.

## Important Formulas and Theorems

There are no specific formulas in this topic, but key relationships include:

- **HTTP Port Numbers:** HTTP defaults to port 80, HTTPS defaults to port 443
- **Idempotent Methods:** GET, PUT, DELETE, HEAD, OPTIONS are idempotent; POST and PATCH are not

## Key Points

1. The Web operates on client-server architecture where browsers (clients) request resources from web servers.

2. A complete URL consists of: scheme (http/https), hostname, optional port, path, optional query string, and optional fragment.

3. HTTP is stateless—each request is independent, requiring cookies or sessions for state management.

4. Common HTTP methods: GET (retrieve), POST (submit data), PUT (replace), DELETE (remove), HEAD (headers only).

5. Status codes: 1xx (informational), 2xx (success), 3xx (redirection), 4xx (client error), 5xx (server error).

6. HTTP headers provide metadata: General (Date, Connection), Request (Host, User-Agent, Accept), Response (Server, Content-Type, Set-Cookie).

7. Cookies use Set-Cookie header from server and Cookie header in subsequent client requests for session tracking.

8. HTTP/1.1 introduced persistent connections allowing multiple requests over one TCP connection.

9. HTTPS provides confidentiality, integrity, and authentication through SSL/TLS encryption.

10. Conditional GET requests use If-Modified-Since and If-None-Match headers to avoid unnecessary data transfer.

## Common Mistakes to Avoid

1. Confusing GET and POST: GET is for retrieval (in URL), POST is for submitting data (in body).

2. Mixing up 401 and 403: 401 means unauthorized (need authentication), 403 means forbidden (authenticated but not permitted).

3. Thinking HTTP maintains state: Remember, HTTP is stateless and requires cookies/sessions for state.

4. Forgetting that HTTP/1.1 requires Host header: This was mandatory since HTTP/1.1.

5. Not understanding cookie scope: Cookies are only sent to the domain and path specified in their attributes.

## Revision Tips

1. Practice breaking down URLs into their component parts.

2. Memorize at least 10 common status codes and their meanings.

3. Review the complete structure of HTTP request and response messages.

4. Understand the complete cookie lifecycle: creation, storage, and transmission.

5. Compare HTTP versions (1.0, 1.1, 2, 3) to understand protocol evolution.
