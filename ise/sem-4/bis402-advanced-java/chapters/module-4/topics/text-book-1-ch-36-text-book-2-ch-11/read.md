# Advanced Java: Introducing Servlets

=====================================

## Module Overview

---

In this module, we will introduce the concept of servlets, a fundamental component of Java-based web applications. We will cover the background of servlets, the life cycle of a servlet, and how to use Tomcat for servlet development.

## Background

---

### What are Servlets?

---

A servlet is a small Java program that runs on a web server, responding to HTTP requests and sending HTTP responses. Servlets are the primary component of the Java Servlet Technology, a Java-based web application framework.

### History of Servlets

---

The concept of servlets was first introduced in the late 1990s by Sun Microsystems. The first version of the Java Servlet API was released in 1999, and since then, servlets have become a standard component of web application development.

## The Life Cycle of a Servlet

---

### What is the Life Cycle of a Servlet?

---

The life cycle of a servlet refers to the sequence of events that a servlet goes through as it is created, initialized, and executed.

### Life Cycle Phases

---

Here are the main phases of the servlet life cycle:

- **Load**: The servlet is loaded into memory by the servlet container.
- **Init**: The servlet is initialized, and the servlet initialization method (init()) is called.
- **Service**: The servlet is requested by the servlet container, and the service() method is called.
- **Destroy**: The servlet is unloaded from memory.

### Example of Servlet Life Cycle

---

Here is an example of a servlet that demonstrates the life cycle phases:

```java
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class HelloWorldServlet extends HttpServlet {
    @Override
    public void init() throws ServletException {
        System.out.println("Servlet initialized");
    }

    @Override
    public void service(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        System.out.println("Servlet requested");
        response.sendError(HttpServletResponse.SC_OK);
    }

    @Override
    public void destroy() {
        System.out.println("Servlet destroyed");
    }
}
```

In this example, the servlet prints a message to the console at each phase of the life cycle.

## Using Tomcat for Servlet Development

---

### What is Tomcat?

---

Tomcat is an open-source servlet container that runs on a Java Runtime Environment (JRE). It is a popular choice for servlet development due to its ease of use and flexibility.

### Installing Tomcat

---

To install Tomcat, follow these steps:

1.  Download the Tomcat installation package from the official Tomcat website.
2.  Extract the package to a directory on your computer.
3.  Configure Tomcat to use the `java` command-line tool to run the servlet container.

### Example Servlet Deployment

---

Here is an example of how to deploy a servlet using Tomcat:

1.  Create a new servlet class, such as `HelloWorldServlet.java`.
2.  Compile the servlet class using the `javac` command-line tool.
3.  Create a new `WEB-INF` directory in the Tomcat `webapps` directory.
4.  Place the compiled servlet class in the `WEB-INF` directory.
5.  Configure the `web.xml` file to point to the servlet class.

### Example `web.xml` File

---

Here is an example of a `web.xml` file that points to the `HelloWorldServlet` class:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app version="3.1" xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
         http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd">
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

In this example, the `web.xml` file points to the `HelloWorldServlet` class and maps it to the `/hello` URL pattern.
