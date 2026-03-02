# The Jakarta Servlet

## Introduction

The Jakarta Servlet package is a Java API that enables developers to create web applications using the Java programming language. This package is a key component of the Java Servlet Technology, which allows developers to create dynamic web content and interact with web servers in a flexible and efficient manner. In this article, we will delve into the world of the Jakarta Servlet package, exploring its history, features, and applications.

## Historical Context

The Java Servlet API was first introduced in 1997 as part of the Java 1.2 platform. The initial release was called "servlet," and it provided a basic set of classes for creating web applications. Over the years, the API has undergone several revisions and updates, with the most recent release being Jakarta EE 9 in 2021.

In 2020, the Oracle Corporation, which previously owned the Servlet API, decided to transfer ownership of the Java Servlet API to the Eclipse Foundation, a non-profit organization that manages the development of several open-source projects. This transfer marked the birth of the Jakarta Servlet API, which is now maintained and updated by the Eclipse Foundation.

## Features of the Jakarta Servlet Package

### 1. Request and Response Objects

The Jakarta Servlet package provides a set of classes for working with HTTP requests and responses. The `HttpServletRequest` and `HttpServletResponse` classes are the core objects for interacting with HTTP requests and responses.

- `HttpServletRequest`: Represents an HTTP request sent by a client to a web server.
- `HttpServletResponse`: Represents an HTTP response sent by a web server to a client.

### 2. Lifecycle Methods

The Jakarta Servlet package provides a set of lifecycle methods that are called at different points in the execution of a servlet. These methods allow developers to perform initialization, initialization, service, and destruction tasks.

- `init()`: Initializes the servlet.
- `service()`: Handles HTTP requests and returns HTTP responses.
- `destroy()`: Destroys the servlet.

### 3. ServletContext and HttpServletRequest Objects

The Jakarta Servlet package provides a set of classes for working with servlet context and HTTP request objects.

- `ServletContext`: Represents the context of a web application.
- `HttpServletRequest`: Represents an HTTP request sent by a client to a web server.

### 4. HTTP Methods

The Jakarta Servlet package provides a set of methods for handling HTTP requests and responses. These methods include:

- `doGET()`: Handles GET requests.
- `doPOST()`: Handles POST requests.
- `doPut()`: Handles PUT requests.
- `doDelete()`: Handles DELETE requests.

### 5. Servlet Container

The Jakarta Servlet package provides a set of classes for working with servlet containers. The most commonly used servlet container is Apache Tomcat.

### 6. Packaging

The Jakarta Servlet package provides a set of annotations for packaging servlets.

### 7. Compatibility

The Jakarta Servlet package provides a set of classes for working with different web containers.

### 8. WebSockets

The Jakarta Servlet package provides a set of classes for working with WebSockets.

### 9. Async Support

The Jakarta Servlet package provides a set of classes for working with asynchronous servlets.

### 10. Security

The Jakarta Servlet package provides a set of classes for working with security features such as authentication and authorization.

## Example Use Case: Hello World Servlet

Here is an example of a simple "Hello World" servlet using the Jakarta Servlet package:

```java
import javax.servlet.*;
import javax.servlet.http.*;

public class HelloWorldServlet extends HttpServlet {
    @Override
    public void init() throws ServletException {
        System.out.println("Servlet initialized");
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<h1>Hello World!</h1>");
    }

    @Override
    public void destroy() {
        System.out.println("Servlet destroyed");
    }
}
```

This servlet extends the `HttpServlet` class and overrides the `doGet()` method to handle HTTP GET requests. The `init()` method is called when the servlet is initialized, and the `destroy()` method is called when the servlet is destroyed.

## Case Study: A Simple Banking System

Here is an example of a simple banking system implemented using the Jakarta Servlet package:

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.*;

public class BankingSystemServlet extends HttpServlet {
    @Override
    public void init() throws ServletException {
        System.out.println("Banking system initialized");
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<h1>Banking System</h1>");
        out.println("<a href='/deposit'>Deposit</a>");
        out.println("<a href='/withdraw'>Withdraw</a>");
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        String action = request.getParameter("action");
        if (action.equals("deposit")) {
            deposit(request, response);
        } else if (action.equals("withdraw")) {
            withdraw(request, response);
        }
    }

    private void deposit(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String accountNumber = request.getParameter("accountNumber");
        String amount = request.getParameter("amount");
        // Deposit logic
        response.sendRedirect("/success");
    }

    private void withdraw(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String accountNumber = request.getParameter("accountNumber");
        String amount = request.getParameter("amount");
        // Withdrawal logic
        response.sendRedirect("/success");
    }

    @Override
    public void destroy() {
        System.out.println("Banking system destroyed");
    }
}
```

This servlet extends the `HttpServlet` class and provides methods for depositing and withdrawing money from accounts. The `doGet()` method is used to handle HTTP GET requests, and the `doPost()` method is used to handle HTTP POST requests.

## Applications of the Jakarta Servlet Package

The Jakarta Servlet package has a wide range of applications in the field of web development. Here are a few examples:

- **Web Applications**: The Jakarta Servlet package is used to create web applications that run on web servers.
- **Enterprise Software**: The Jakarta Servlet package is used to create enterprise software that interacts with databases and other systems.
- **Mobile Applications**: The Jakarta Servlet package can be used to create mobile applications that run on Android and iOS devices.
- **Desktop Applications**: The Jakarta Servlet package can be used to create desktop applications that run on Windows, macOS, and Linux.

## Conclusion

In conclusion, the Jakarta Servlet package is a Java API that enables developers to create web applications using the Java programming language. This package provides a wide range of features, including request and response objects, lifecycle methods, servlet context and HTTP request objects, HTTP methods, servlet container, packaging, compatibility, websockets, async support, and security features. The Jakarta Servlet package has a wide range of applications in the field of web development, including web applications, enterprise software, mobile applications, and desktop applications.

## Further Reading

- [Jakarta Servlet Specification](https://jakarta.ee/specs/servlet/4.0/)
- [Jakarta Servlet API Reference](https://jakarta.ee/docs/servlet/api/)
- [Servlet Tutorial](https://docs.oracle.com/javaee/7/tutorial/doc/servlet.htm)
- [Java Servlet Programming](https://www.amazon.com/Java-Servlet-Programming-Second-Edition/dp/0134685994/)
- [Servlets and JavaServer Pages](https://www.amazon.com/Servlets-JavaServer-Pages-Second-Edition/dp/0134686006/)
