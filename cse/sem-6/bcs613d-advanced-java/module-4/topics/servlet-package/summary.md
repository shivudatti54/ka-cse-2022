# Servlet Package

## Overview

The servlet package (jakarta.servlet and jakarta.servlet.http) provides comprehensive API for building web applications including interfaces, classes, and exceptions for request handling, response generation, session management, and application configuration.

## Key Points

- **jakarta.servlet**: Core servlet interfaces and classes (Servlet, ServletConfig, ServletContext)
- **jakarta.servlet.http**: HTTP-specific classes (HttpServlet, HttpServletRequest, HttpServletResponse)
- **GenericServlet**: Abstract class implementing Servlet interface
- **HttpServlet**: Extends GenericServlet for HTTP protocol support
- **ServletException**: Thrown when servlet encounters difficulty
- **UnavailableException**: Indicates servlet temporarily or permanently unavailable
- **Filter Interface**: For request/response filtering
- **Listener Interfaces**: For monitoring servlet lifecycle and session events

## Important Concepts

- Two main packages: jakarta.servlet and jakarta.servlet.http
- Most servlets extend HttpServlet, not GenericServlet
- Request and response objects encapsulate HTTP communication
- ServletContext provides application-wide functionality
- Filter chains intercept requests before servlets

## Notes

- Remember HttpServlet in jakarta.servlet.http package
- For exams, know key classes in each package
- Understand servlet, filter, listener relationship in request processing
