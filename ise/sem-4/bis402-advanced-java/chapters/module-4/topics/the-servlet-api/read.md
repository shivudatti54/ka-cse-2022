# Introduction to Servlets

## 1. What are Servlets?

Servlets are Java programs that run on a web server or application server and act as a middle layer between requests coming from web browsers or other HTTP clients and databases or applications on the HTTP server. They provide a component-based, platform-independent method for building web applications.

**Key Characteristics:**

- Server-side technology
- Extend the capabilities of servers
- Handle client requests and generate dynamic responses
- Platform-independent (Java-based)
- Efficient and scalable

```
+-------------+    HTTP Request    +-------------+    Process    +-----------+
| Web Browser | -----------------> |   Servlet   | ------------> | Database/ |
|   (Client)  | <----------------- |  (Server)   | <------------ |  Backend  |
+-------------+    HTTP Response   +-------------+    Data       +-----------+
```

## 2. Servlet Lifecycle

The servlet lifecycle is managed by the servlet container (like Tomcat) and consists of three main methods:

### 2.1. init() Method

```java
public void init(ServletConfig config) throws ServletException {
    // Initialization code
}
```

- Called once when the servlet is first loaded
- Used for one-time initialization activities
- Receives ServletConfig object containing initialization parameters

### 2.2. service() Method

```java
public void service(ServletRequest req, ServletResponse res)
    throws ServletException, IOException {
    // Handle requests
}
```

- Called for each client request
- Determines the type of request (GET, POST, etc.) and calls appropriate doXXX() method
- Can handle multiple requests simultaneously (thread-safe)

### 2.3. destroy() Method

```java
public void destroy() {
    // Cleanup code
}
```

- Called once when the servlet is being taken out of service
- Used for cleanup activities like closing database connections

**Lifecycle Diagram:**

```
Servlet Class Loaded
       |
       v
   init() called (once)
       |
       v
 service() called (for each request)
       |
       v
 destroy() called (once during shutdown)
```

## 3. Setting Up Tomcat Server

Apache Tomcat is an open-source implementation of Java Servlet and JavaServer Pages technologies.

### Installation Steps:

1. Download Tomcat from Apache website
2. Set JAVA_HOME environment variable
3. Extract Tomcat to desired directory
4. Configure CATALINA_HOME environment variable
5. Start Tomcat using startup.bat (Windows) or startup.sh (Linux)

### Directory Structure:

```
webapps/
└── YourWebApp/
    ├── WEB-INF/
    │   ├── web.xml (Deployment Descriptor)
    │   └── classes/ (Servlet classes)
    └── index.html (Welcome file)
```

## 4. Servlet API and Jakarta Packages

The Servlet API provides interfaces and classes for writing servlets. With Java EE's move to the Eclipse Foundation, packages changed from `javax.servlet` to `jakarta.servlet`.

### Core Interfaces and Classes:

- `Servlet`: Base interface
- `GenericServlet`: Protocol-independent implementation
- `HttpServlet`: HTTP-specific implementation
- `ServletRequest`/`HttpServletRequest`: Request objects
- `ServletResponse`/`HttpServletResponse`: Response objects

**Package Comparison Table:**
| Java EE Version | Package Name | Status |
|-----------------|--------------------|---------------|
| Java EE 8 | javax.servlet._ | Legacy |
| Jakarta EE 9+ | jakarta.servlet._ | Current |

## 5. HTTP Request and Response Handling

### 5.1. HTTP Methods

```java
public class MyServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request,
                        HttpServletResponse response)
        throws ServletException, IOException {
        // Handle GET requests
    }

    protected void doPost(HttpServletRequest request,
                         HttpServletResponse response)
        throws ServletException, IOException {
        // Handle POST requests
    }
}
```

### 5.2. Request Parameters

```java
String username = request.getParameter("username");
String[] hobbies = request.getParameterValues("hobbies");
```

### 5.3. Response Handling

```java
response.setContentType("text/html");
PrintWriter out = response.getWriter();
out.println("<html><body>");
out.println("<h1>Hello World</h1>");
out.println("</body></html>");
```

## 6. Session Tracking

HTTP is stateless, but servlets provide several mechanisms for session tracking:

### 6.1. Cookies

```java
// Creating cookies
Cookie userCookie = new Cookie("username", "john");
userCookie.setMaxAge(60*60*24); // 1 day
response.addCookie(userCookie);

// Reading cookies
Cookie[] cookies = request.getCookies();
```

### 6.2. URL Rewriting

```java
String url = response.encodeURL("nextPage.jsp");
out.println("<a href='" + url + "'>Next Page</a>");
```

### 6.3. Hidden Form Fields

```html
<input type="hidden" name="sessionid" value="12345" />
```

### 6.4. HttpSession Interface

```java
// Getting session
HttpSession session = request.getSession(true);

// Storing attributes
session.setAttribute("user", userObject);

// Retrieving attributes
User user = (User) session.getAttribute("user");

// Invalidating session
session.invalidate();
```

**Session Tracking Methods Comparison:**
| Method | Pros | Cons |
|------------------|-------------------------------|-------------------------------|
| Cookies | Simple, client-side storage | Browser may disable cookies |
| URL Rewriting | Works without cookies | URLs become long and ugly |
| Hidden Fields | Works with forms | Only works with form submits |
| HttpSession | Most powerful, server-side | Requires session management |

## 7. Deployment Descriptor (web.xml)

The web.xml file configures servlet deployment:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee
         https://jakarta.ee/xml/ns/jakartaee/web-app_5_0.xsd"
         version="5.0">

    <servlet>
        <servlet-name>MyServlet</servlet-name>
        <servlet-class>com.example.MyServlet</servlet-class>
    </servlet>

    <servlet-mapping>
        <servlet-name>MyServlet</servlet-name>
        <url-pattern>/myservlet</url-pattern>
    </servlet-mapping>

    <session-config>
        <session-timeout>30</session-timeout>
    </session-config>
</web-app>
```

## 8. Basic Servlet Example

```java
package com.example;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;

public class HelloServlet extends HttpServlet {

    public void init() throws ServletException {
        // Initialization code
    }

    protected void doGet(HttpServletRequest request,
                        HttpServletResponse response)
        throws ServletException, IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        String name = request.getParameter("name");
        if (name == null) name = "Guest";

        out.println("<html>");
        out.println("<head><title>Hello Servlet</title></head>");
        out.println("<body>");
        out.println("<h1>Hello, " + name + "!</h1>");
        out.println("</body>");
        out.println("</html>");
    }

    public void destroy() {
        // Cleanup code
    }
}
```

## 9. Servlet vs CGI Comparison

| Aspect      | Servlet                     | CGI (Common Gateway Interface) |
| ----------- | --------------------------- | ------------------------------ |
| Process     | Runs in same process        | New process for each request   |
| Performance | Faster (thread-based)       | Slower (process-based)         |
| Platform    | Platform-independent (Java) | Platform-dependent             |
| Memory      | Shares memory               | Separate memory per process    |
| Scalability | Highly scalable             | Less scalable                  |

## Exam Tips

1. **Lifecycle Methods**: Remember init() is called once, service() for each request, destroy() at shutdown
2. **Thread Safety**: Servlets are multithreaded - be careful with instance variables
3. **HTTP Methods**: doGet() for data retrieval, doPost() for data submission
4. **Session Tracking**: Understand all four methods and when to use each
5. **Packages**: Remember the shift from javax.servlet to jakarta.servlet
6. **Deployment**: Understand web.xml structure and annotations
7. **Performance**: Servlets are faster than CGI due to thread reuse
8. **Error Handling**: Always handle exceptions properly in servlets
