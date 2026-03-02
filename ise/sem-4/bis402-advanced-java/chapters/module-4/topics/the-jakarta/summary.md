# **The Jakarta: Revision Notes**

## **Introduction**

- The Jakarta is a popular open-source implementation of the Java Servlet API.
- Developed by the Apache Software Foundation, it provides a scalable and secure platform for developing web applications.

## **Key Features**

- Supports Java 8 and higher versions
- Compatible with most Java Servlet containers
- Provides a robust security framework
- Offers scalability and high-performance capabilities

## **Life Cycle of a Servlet**

- `init()`: Called when the servlet is initialized
- `service()`: Called for each incoming HTTP request
- `destroy()`: Called when the servlet is destroyed

## **Important Formulas/Definitions/Theorems**

- **HTTP Request Methods**: GET, POST, PUT, DELETE, etc.
- **HTTP Status Codes**: 200 OK, 404 Not Found, 500 Internal Server Error, etc.
- **Servlet Request Object**: A container for HTTP request and response objects

## **Key Concepts**

- **Servlet Filters**: Used to intercept and modify HTTP requests and responses
- **Servlet Mappers**: Used to map URLs to servlets
- **Servlet Containers**: Provide a platform for deploying and executing servlets

## **Important API Methods**

- `request.setAttribute()`: Sets an attribute for the request
- `response.sendRedirect()`: Redirects the client to a specified URL
- `response.getWriter()`: Returns a writer for the response
