# The Jakarta Servlet Package

## Overview

Jakarta Servlet (formerly javax.servlet) package contains core interfaces and classes for servlet development. It includes Servlet interface, ServletConfig, ServletContext, RequestDispatcher, and generic servlet classes that form the foundation of Java web application development.

## Key Points

- **Package Name**: jakarta.servlet (changed from javax.servlet in Jakarta EE 9+)
- **Servlet Interface**: Defines lifecycle methods (init, service, destroy)
- **GenericServlet**: Protocol-independent abstract servlet implementation
- **ServletConfig**: Access to servlet initialization parameters
- **ServletContext**: Application-wide context and shared resources
- **RequestDispatcher**: Forward or include other resources
- **ServletRequest and ServletResponse**: Generic request/response interfaces
- **Filter and FilterChain**: Request/response filtering mechanism

## Important Concepts

- jakarta.servlet.http for HTTP-specific classes
- GenericServlet vs HttpServlet: protocol-agnostic vs HTTP-specific
- ServletContext shared across all servlets in web application
- RequestDispatcher.forward() vs include()
- Servlet filters intercept requests before reaching servlet

## Notes

- Remember package name changed to jakarta.servlet in recent versions
- For exams, know key interfaces: Servlet, ServletConfig, ServletContext
- Understand difference between javax (old) and jakarta (new) packages