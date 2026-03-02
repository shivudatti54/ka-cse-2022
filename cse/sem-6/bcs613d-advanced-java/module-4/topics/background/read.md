# Servlet Background

## Introduction to Server-Side Web Technologies

The World Wide Web initially consisted of static HTML pages served by web servers. As the need for dynamic, interactive web applications grew, various server-side technologies evolved to generate content on-the-fly based on user requests, database queries, and business logic.

Understanding this evolution is crucial to appreciate why Java Servlets were developed and how they addressed the limitations of earlier approaches.

## The Evolution of Dynamic Web Content

### Static Web Pages (Early 1990s)

In the early days of the web, all content was static HTML:

```
Client (Browser) → HTTP Request → Web Server → Static HTML File → HTTP Response → Client
```

The web server simply located the requested file and sent it back. No processing or customization was possible.

### CGI (Common Gateway Interface)

CGI was the first widely adopted standard for generating dynamic web content:

```
Client → Web Server → Fork New Process → Execute CGI Program → Generate HTML → Response → Client
```

**How CGI Works:**

1. Web server receives a request for a CGI resource
2. Server creates a **new operating system process** for the CGI program
3. Request data is passed via environment variables and standard input
4. CGI program (often Perl, C, or Python) processes the request
5. Output is sent back as HTTP response
6. The process is **terminated** after each request

**CGI Limitations:**

- **Performance**: New process created for every request (expensive)
- **Scalability**: Hundreds of concurrent users means hundreds of processes
- **Resource intensive**: Each process has its own memory space
- **No session management**: No built-in way to track user sessions
- **Platform dependent**: CGI programs often tied to specific OS

### Server-Side Scripting (Late 1990s)

Technologies like PHP and ASP embedded scripts within HTML pages, reducing overhead but still lacking Java's portability and enterprise features.

## Introduction to Java Servlets

**Java Servlets** were developed by Sun Microsystems as a server-side technology that runs within a Java Virtual Machine (JVM) on the web server. They addressed all major CGI limitations.

### What is a Servlet?

A Servlet is a **Java class** that:

- Extends the capabilities of a web server
- Handles client requests (typically HTTP)
- Generates dynamic responses (usually HTML)
- Runs within a **servlet container** (web container)

```java
public class HelloServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request,
 HttpServletResponse response)
 throws ServletException, IOException {
 response.setContentType("text/html");
 PrintWriter out = response.getWriter();
 out.println("<h1>Hello, World!</h1>");
 }
}
```

## Servlet Container (Web Container)

The servlet container is the runtime environment that manages servlets. It is a component of the web server or application server.

### Container Responsibilities

| Responsibility           | Description                                             |
| ------------------------ | ------------------------------------------------------- |
| **Lifecycle Management** | Loads, instantiates, initializes, and destroys servlets |
| **Request Routing**      | Maps incoming URLs to appropriate servlets              |
| **Threading**            | Creates threads for concurrent request handling         |
| **Security**             | Enforces security constraints defined in web.xml        |
| **Session Management**   | Provides HttpSession API for state management           |

### Popular Servlet Containers

1. **Apache Tomcat** - Most widely used, lightweight
2. **Jetty** - Embedded-friendly, used in many frameworks
3. **GlassFish** - Full Jakarta EE reference implementation
4. **WildFly** - Full-featured application server (formerly JBoss)

## Servlet vs CGI Comparison

| Feature                | CGI                              | Servlet                     |
| ---------------------- | -------------------------------- | --------------------------- |
| **Execution Model**    | New process per request          | Thread per request          |
| **Performance**        | Slow (process creation overhead) | Fast (thread reuse)         |
| **Memory**             | Separate memory per process      | Shared JVM memory           |
| **Persistence**        | Terminated after each request    | Persistent in memory        |
| **Platform**           | Often OS-dependent               | Platform-independent (Java) |
| **Session Management** | None built-in                    | HttpSession API             |
| **Scalability**        | Poor                             | Excellent                   |
| **Language**           | Any (Perl, C, Python)            | Java                        |

## HTTP Request-Response Model

Servlets operate within the HTTP request-response paradigm:

```
1. Client sends HTTP Request
 ├── Request Method (GET, POST, PUT, DELETE)
 ├── Request URL
 ├── Headers (Content-Type, Accept, etc.)
 └── Body (for POST/PUT)

2. Servlet Container receives request
 ├── Creates HttpServletRequest object
 ├── Creates HttpServletResponse object
 └── Invokes appropriate servlet method

3. Servlet processes request
 ├── Reads request parameters
 ├── Performs business logic
 └── Writes response

4. Response sent to client
 ├── Status Code (200 OK, 404 Not Found, etc.)
 ├── Response Headers
 └── Response Body (HTML, JSON, etc.)
```

### HTTP Methods

| Method | Purpose          | Servlet Method |
| ------ | ---------------- | -------------- |
| GET    | Retrieve data    | doGet()        |
| POST   | Submit data      | doPost()       |
| PUT    | Update resource  | doPut()        |
| DELETE | Remove resource  | doDelete()     |
| HEAD   | Get headers only | doHead()       |

## Deployment Descriptor (web.xml)

The web.xml file configures the web application:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee" version="4.0">

 <servlet>
 <servlet-name>HelloServlet</servlet-name>
 <servlet-class>com.example.HelloServlet</servlet-class>
 </servlet>

 <servlet-mapping>
 <servlet-name>HelloServlet</servlet-name>
 <url-pattern>/hello</url-pattern>
 </servlet-mapping>

</web-app>
```

## Web Application Directory Structure

```
myapp/
├── WEB-INF/
│ ├── web.xml (Deployment descriptor)
│ ├── classes/ (Compiled servlet classes)
│ │ └── com/example/
│ │ └── HelloServlet.class
│ └── lib/ (JAR dependencies)
├── index.html (Static files)
├── css/
├── js/
└── images/
```

## Summary

Java Servlets represent a significant advancement over CGI and earlier server-side technologies. By leveraging the JVM's threading model, platform independence, and rich API, servlets provide a robust foundation for building scalable, high-performance web applications. The servlet container manages the complexity of lifecycle, threading, and security, allowing developers to focus on business logic.
