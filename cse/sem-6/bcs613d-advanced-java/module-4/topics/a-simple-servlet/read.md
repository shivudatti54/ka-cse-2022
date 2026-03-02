# Java Servlets: Foundation of Web Application Development

## Introduction

Java Servlets are server-side Java components that extend the capabilities of web servers by handling HTTP requests and generating dynamic responses. They form the cornerstone of the Java EE (now Jakarta EE) web tier and provide the fundamental architecture upon which modern web frameworks are built.

## Servlet Architecture

The servlet API is defined by the `javax.servlet` and `javax.servlet.http` packages. At the core is the `HttpServlet` class, which extends `GenericServlet` and provides a framework for handling HTTP-specific operations.

### Basic Servlet Structure

```java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class HelloWorldServlet extends HttpServlet {

 // Initialize the servlet (called once per lifecycle)
 @Override
 public void init() throws ServletException {
 super.init();
 }

 // Handle GET requests (default HTTP method for retrieving resources)
 @Override
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 // Set the response content type to HTML
 response.setContentType("text/html;charset=UTF-8");

 // Obtain PrintWriter for writing response body
 PrintWriter out = response.getWriter();

 try {
 // Generate dynamic HTML response
 out.println("<!DOCTYPE html>");
 out.println("<html>");
 out.println("<head>");
 out.println("<title>Simple Servlet</title>");
 out.println("</head>");
 out.println("<body>");
 out.println("<h1>Hello World from my first Servlet!</h1>");
 out.println("</body>");
 out.println("</html>");
 } finally {
 out.close();
 }
 }

 // Handle POST requests (for form submissions)
 @Override
 protected void doPost(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {
 doGet(request, response);
 }

 // Cleanup resources (called once when servlet is destroyed)
 @Override
 public void destroy() {
 super.destroy();
 }
}
```

## Servlet Lifecycle

The servlet lifecycle consists of three primary phases:

1. **Initialization (`init()`)**: Called once when the servlet is first loaded. Used for one-time setup operations.

2. **Request Handling (`service()`)**: The container calls `service()` for each request, which dispatches to `doGet()`, `doPost()`, etc., based on the HTTP method.

3. **Destruction (`destroy()`)**: Called once when the servlet is unloaded, releasing resources.

## Key Components

### HttpServletRequest

Encapsulates all client request data, including:

- Request parameters (`getParameter()`)
- Request headers (`getHeader()`)
- Session information (`getSession()`)
- Request method and URI

### HttpServletResponse

Encapsulates the server's response, including:

- Content type setting (`setContentType()`)
- Response headers
- Output stream (`getWriter()` or `getOutputStream()`)

## Deployment Descriptor (web.xml)

Servlets must be mapped to URLs in the deployment descriptor:

```xml
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
 http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
 version="4.0">

 <servlet>
 <servlet-name>HelloWorldServlet</servlet-name>
 <servlet-class>HelloWorldServlet</servlet-class>
 </servlet>

 <servlet-mapping>
 <servlet-name>HelloWorldServlet</servlet-name>
 <url-pattern>/hello</url-pattern>
 </servlet-mapping>

</web-app>
```

Alternatively, annotations can be used:

```java
@WebServlet("/hello")
public class HelloWorldServlet extends HttpServlet { ... }
```

## HTTP Methods

| Method | Purpose                  | Idempotent |
| ------ | ------------------------ | ---------- |
| GET    | Retrieve resources       | Yes        |
| POST   | Submit data to server    | No         |
| PUT    | Update existing resource | Yes        |
| DELETE | Remove a resource        | Yes        |

## Compilation and Execution

1. Place the servlet class in the `WEB-INF/classes` directory
2. Ensure servlet-api.jar is in the classpath during compilation
3. Deploy to a servlet container (Tomcat, Jetty, etc.)
4. Access via: `http://localhost:8080/context-path/hello`

## Conclusion

This simple servlet demonstrates the core request-response mechanism in Java web development. Understanding these fundamentals is essential as they underpin all modern Java web frameworks, including Spring MVC and Jakarta EE's CDI-based web applications.
