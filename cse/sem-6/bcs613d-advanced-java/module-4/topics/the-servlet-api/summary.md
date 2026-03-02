# The Servlet API

## Overview

The Servlet API provides interfaces and classes in javax.servlet and javax.servlet.http packages for developing web applications. Core interfaces include Servlet, ServletConfig, ServletContext while key classes include GenericServlet, HttpServlet, HttpServletRequest, and HttpServletResponse.

## Key Points

- **Servlet Interface**: Root interface with lifecycle methods (init, service, destroy)
- **HttpServlet**: Abstract class extending GenericServlet for HTTP-specific servlets
- **HttpServletRequest**: Provides access to request data, parameters, headers, session
- **HttpServletResponse**: Used to construct HTTP response, set headers, write output
- **ServletConfig**: Provides servlet initialization parameters
- **ServletContext**: Provides application-wide context and shared data
- **RequestDispatcher**: Forward requests to other servlets or JSP pages
- **HttpSession**: Manages user session across multiple requests

## Important Concepts

- Extend HttpServlet for HTTP servlets
- Use request.getParameter() to read form data
- Use response.getWriter() to send HTML output
- ServletContext shared by all servlets in application
- RequestDispatcher for server-side forwarding and including

## Notes

- Remember HttpServlet is abstract class, Servlet is interface
- For exams, know key methods: doGet(), doPost(), getParameter(), getWriter()
- Practice using request and response objects in servlet code
