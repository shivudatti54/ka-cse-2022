# The Jakarta Servlet HTTP Package

=====================================

## Overview

---

The Jakarta Servlet HTTP package is a Java class library that provides the core functionality for building web applications using the Java Servlet Technology. It is part of the Java EE platform and is used to create servlets, which are Java classes that run on a web server to handle HTTP requests.

## Definitions

---

- **Servlet**: A Java class that implements the servlet interface and extends the HttpServlet class. Servlets are used to handle HTTP requests and responses.
- **HTTP Request**: An HTTP request is a message sent by a client (usually a web browser) to a server, containing information about the request, such as the HTTP method (e.g., GET, POST), the URL, and any query parameters.
- **HTTP Response**: An HTTP response is a message sent by a server to a client, containing the result of the request, such as the HTTP status code, headers, and the response body.

## Key Concepts

---

- **Servlet Life Cycle**: The servlet life cycle refers to the sequence of events that a servlet goes through when it is created, initialized, serviced, and destroyed.
- **HTTP Methods**: HTTP methods are used to specify the type of HTTP request being made. The most common HTTP methods are:
  - GET
  - POST
  - PUT
  - DELETE
  - PATCH
- **HTTP Status Codes**: HTTP status codes are used to indicate the result of an HTTP request. Common HTTP status codes include:
  - 200 OK
  - 404 Not Found
  - 500 Internal Server Error

## Classes and Interfaces

---

### HttpServlet

The HttpServlet class is the most commonly used servlet class. It extends the HttpServlet class and provides a basic implementation for handling HTTP requests.

### HttpServletRequest

The HttpServletRequest class represents the HTTP request being made. It provides methods for accessing request parameters, headers, and other information.

### HttpServletResponse

The HttpServletResponse class represents the HTTP response being sent. It provides methods for setting response headers, writing response bodies, and other information.

### ServletRequest andServletResponse

The ServletRequest and ServletResponse interfaces represent the servlet request and response objects. They provide methods for accessing and manipulating request and response information.

## Methods

---

### doGet() and doPost()

The doGet() and doPost() methods are used to handle HTTP GET and POST requests, respectively. These methods are overridden in the HttpServlet class and provide a basic implementation for handling requests.

### getParameter() and getParameterNames()

The getParameter() and getParameterNames() methods are used to access request parameters. The getParameter() method returns the value of a request parameter, while the getParameterNames() method returns an array of request parameter names.

### setHeader() and getHeader()

The setHeader() and getHeader() methods are used to set and get response headers. The setHeader() method sets the value of a response header, while the getHeader() method returns the value of a response header.

### write() and getWriter()

The write() and getWriter() methods are used to write response bodies. The write() method writes the response body, while the getWriter() method returns a writer object for writing the response body.

## Example

---

Below is an example of a simple servlet that handles HTTP GET and POST requests:

```java
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // Handle HTTP GET request
        String name = req.getParameter("name");
        String message = "Hello, " + name + "!";
        resp.getWriter().println(message);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // Handle HTTP POST request
        String name = req.getParameter("name");
        String message = "Hello, " + name + "!";
        resp.getWriter().println(message);
    }
}
```

In this example, the HelloServlet extends the HttpServlet class and provides implementations for the doGet() and doPost() methods. The doGet() method handles HTTP GET requests, while the doPost() method handles HTTP POST requests.
