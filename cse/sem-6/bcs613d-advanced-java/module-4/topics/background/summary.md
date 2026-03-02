# Servlet Background

## Overview

Servlets are Java programs that run on web servers to handle HTTP requests and generate dynamic web content. Introduced as part of Java EE, servlets provide a robust, platform-independent alternative to CGI scripts, offering better performance, session management, and integration with Java ecosystem.

## Key Points

- **Server-Side Technology**: Runs on web server, not client browser
- **Platform Independent**: Write once, run on any servlet container
- **Better than CGI**: Single process handles multiple requests, no process overhead
- **HTTP Protocol**: Handles GET, POST, PUT, DELETE requests
- **Servlet Container**: Tomcat, Jetty, GlassFish manage servlet lifecycle
- **Java EE Standard**: Part of Jakarta EE (formerly Java EE) specification
- **Dynamic Content**: Generates HTML, XML, JSON responses dynamically
- **Session Management**: Built-in support for tracking user sessions

## Important Concepts

- Servlet vs CGI: servlets more efficient, persistent
- Container manages lifecycle: init(), service(), destroy()
- Thread-based architecture for concurrent requests
- Integration with JSP for presentation layer
- Servlet API provides HttpServletRequest and HttpServletResponse

## Notes

- Remember servlets run on server, not in browser
- For exams, know advantages over CGI: performance, session management, portability
- Understand servlet container role in lifecycle management
