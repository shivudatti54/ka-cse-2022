# Java Servlets: Summary

## Overview

Java Servlets are server-side components that extend web servers to handle HTTP requests and generate dynamic responses. They form the foundational layer of Java web application development and serve as the architectural basis for modern web frameworks.

## Key Components

| Component | Description |
|-----------|-------------|
| `HttpServlet` | Base class for creating servlets handling HTTP requests |
| `HttpServletRequest` | Encapsulates client request data (parameters, headers, session) |
| `HttpServletResponse` | Encapsulates server response (content type, output stream) |
| `ServletConfig` | Initialization parameters for a single servlet instance |
| `ServletContext` | Shared application-wide resources and attributes |

## Servlet Lifecycle

1. **Initialization**: `init()` method called once when servlet loads
2. **Request Handling**: Container calls `service()`, which dispatches to `doGet()`/`doPost()` etc.
3. **Destruction**: `destroy()` method called when servlet is unloaded

## Essential Methods

- `doGet(HttpServletRequest, HttpServletResponse)`: Handle GET requests
- `doPost(HttpServletRequest, HttpServletResponse)`: Handle POST requests
- `setContentType(String)`: Set response MIME type
- `getWriter()`: Obtain PrintWriter for text response
- `getParameter(String)`: Retrieve request parameter values

## Configuration Methods

**Using web.xml:**
```xml
<servlet>
    <servlet-name>MyServlet</servlet-name>
    <servlet-class>com.example.MyServlet</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>MyServlet</servlet-name>
    <url-pattern>/api/*</url-pattern>
</servlet-mapping>
```

**Using Annotations:**
```java
@WebServlet(urlPatterns = "/api/*")
public class MyServlet extends HttpServlet { }
```

## Important Notes

- Always set content type before writing to response
- Override `doGet()` or `doPost()` rather than `service()` for specific HTTP methods
- Servlets are thread-safe: instance variables are NOT thread-safe
- Use `finally` block to ensure proper resource cleanup
- The servlet container manages instantiation, initialization, and lifecycle

## Examination Tips

- Be able to write a complete servlet with proper imports and method signatures
- Understand the difference between `doGet()` and `doPost()`
- Know how to retrieve form parameters using `request.getParameter()`
- Understand servlet mapping and URL patterns
- Remember to set response content type: `response.setContentType("text/html")`