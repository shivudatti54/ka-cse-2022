# The Jakarta Servlet HTTP Package - Summary

## Key Definitions and Concepts

- **HttpServlet**: Abstract class handling HTTP requests via `doGet()`, `doPost()`, etc.
- **HttpServletRequest**: Encapsulates HTTP request data (parameters, headers, method type).
- **HttpServletResponse**: Manages HTTP response (status codes, headers, output stream).
- **HttpSession**: Tracks client session state across multiple requests using `getSession()`.
- **Cookie**: Stores client-side data via `Cookie(name,value)` constructor and `response.addCookie()`.

## Important Formulas and Theorems

```java
// HTTP Method Handling
protected void doGet(HttpServletRequest req, HttpServletResponse resp)
protected void doPost(HttpServletRequest req, HttpServletResponse resp)

// Response Status Codes
response.sendError(HttpServletResponse.SC_NOT_FOUND, "Message");
response.setStatus(HttpServletResponse.SC_OK);

// Cookie Operations
cookie.setMaxAge(3600); // Seconds
response.addCookie(cookie);

// Session Management
session.setAttribute("key", object);
Object val = session.getAttribute("key");
```

## Key Points

1. Core package for HTTP-specific servlet operations in Jakarta EE
2. `HttpServlet` must be extended to create HTTP servlets (override service methods)
3. Request data accessible via:
   - `request.getParameter("name")`
   - `request.getHeader("User-Agent")`
4. Response controlled through:
   - `response.setContentType("text/html")`
   - `response.getWriter().println()`
5. Sessions maintain state using cookies or URL rewriting
6. Cookies require:
   - Creation with name/value pair
   - Configuration (maxAge, domain)
   - Addition to response object
7. JSP implicitly uses `HttpServletRequest` and `HttpServletResponse` objects
8. Common HTTP status codes:
   - 200 (OK), 302 (Redirect), 404 (Not Found), 500 (Server Error)
9. Always override `doPost()`/`doGet()` instead of `service()` for method-specific handling
10. Session timeout configurable in `web.xml` via `<session-config>`

## Common Mistakes to Avoid

1. Forgetting to call `super.doGet()`/`super.doPost()` when overriding methods
2. Not setting content type before writing response (`text/html` default assumed)
3. Cookie creation errors:
   - Adding cookies to request instead of response
   - Not using `response.addCookie()` after creation
4. Session management pitfalls:
   - Using `getSession(true)` unnecessarily
   - Storing large objects in session affecting performance

## Revision Tips

1. Practice writing servlets that:
   - Handle form submissions (GET/POST)
   - Set cookies and read them in subsequent requests
   - Track user sessions for login simulation
2. Create a cheat sheet for HTTP status codes:
   - 2xx (Success), 3xx (Redirection), 4xx (Client errors), 5xx (Server errors)
3. Draw request-response flow diagrams showing:
   - Servlet container interaction
   - Session ID propagation
   - Cookie header handling
4. Compare and contrast:
   - `sendRedirect()` vs RequestDispatcher
   - GET vs POST method characteristics
   - Cookies vs Session storage approaches
