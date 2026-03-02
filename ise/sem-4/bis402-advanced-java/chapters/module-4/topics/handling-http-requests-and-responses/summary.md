# Handling HTTP Requests and Responses

=====================================

## Introduction

---

Handling HTTP requests and responses is a critical aspect of building web applications using Java servlets. This section provides a concise summary of key concepts and formulas.

## HTTP Request and Response

---

- **HTTP Request**:
  - A client sends an HTTP request to a server to retrieve or send data.
  - Request methods: GET, POST, PUT, DELETE, etc.
  - Request headers: contain metadata about the request (e.g., content type, authorization)
- **HTTP Response**:
  - A server sends an HTTP response to a client in response to a request.
  - Response status codes: 100-199 (informational), 200-299 (success), 300-399 (redirect), etc.
  - Response headers: contain metadata about the response (e.g., content type, caching instructions)

## Servlet Life Cycle

---

- **Request Object**:
  - Created when a request is received by the servlet container.
  - Contains information about the request (e.g., request method, URL, headers)
- **Response Object**:
  - Created when a response is sent by the servlet.
  - Contains information about the response (e.g., response status code, headers)

## Key Formulas

---

- **HTTP Request Formula**:
  - `HTTP Request = <method> <URL> [ <headers> ] [ <body> ]`
- **HTTP Response Formula**:
  - `HTTP Response = <status code> <headers> [ <body> ]`

## Important Definitions

---

- **Servlet**:
  - A Java class that extends the `javax.servlet.http.HttpServlet` class.
  - A servlet container (e.g., Tomcat) runs the servlet to handle requests.
- **Servlet Container**:
  - A software component that hosts and manages servlets.
  - Tomcat is a popular servlet container for Java web applications.

## Theorems

---

- **The HTTP Request and Response Theorem**:
  - "The client sends an HTTP request to the server, and the server sends an HTTP response to the client."

Note: This summary is a concise revision guide and is not intended to be a comprehensive resource.
