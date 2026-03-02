# Using Tomcat for Servlet Development

## Introduction

Apache Tomcat is an open-source Java Servlet Container that implements core Java EE (Jakarta EE) specifications for web development. As the reference implementation for Java Servlets and JSP, Tomcat provides the essential runtime environment where servlets execute and handle HTTP requests/responses.

Tomcat's importance stems from its lightweight architecture, ease of configuration, and widespread industry adoption. Over 60% of Java web applications use Tomcat as their deployment platform (2023 JetBrains survey). For students, mastering Tomcat is critical because:

1. It demonstrates practical implementation of servlet lifecycle concepts
2. exams frequently test deployment descriptors and directory structures
3. Real-world systems like banking portals and e-commerce platforms rely on Tomcat

This module bridges theoretical servlet concepts with hands-on implementation. You'll learn to deploy WAR files, configure web.xml, and use Tomcat Manager – skills directly applicable in software engineering roles.

## Key Concepts

### 1. Tomcat Directory Structure

```
tomcat/
├── bin/ # Startup/shutdown scripts
├── conf/ # Configuration files (server.xml, web.xml)
├── logs/ # Access logs and error logs
├── webapps/ # Deployed applications (WAR files expand here)
├── work/ # Temporary files and compiled JSPs
└── lib/ # Shared libraries (JDBC drivers etc.)
```

### 2. Web Application Structure

```
MyWebApp.war
│
├── WEB-INF/
│ ├── web.xml # Deployment descriptor
│ ├── classes/ # Compiled servlets
│ └── lib/ # Dependency JARs
│
├── index.jsp # Public resources
└── images/logo.png # Accessible directly
```

### 3. Deployment Methods

1. **Manual Deployment**: Copy WAR file to `webapps/`

```bash
cp StudentApp.war $CATALINA_HOME/webapps/
```

2. **Tomcat Manager**: Web-based GUI at `http://localhost:8080/manager`
3. **IDE Integration**: Direct deployment from Eclipse/IntelliJ

### 4. Servlet Mapping in web.xml

```xml
<servlet>
 <servlet-name>LoginServlet</servlet-name>
 <servlet-class>com..LoginServlet</servlet-class>
</servlet>

<servlet-mapping>
 <servlet-name>LoginServlet</servlet-name>
 <url-pattern>/login</url-pattern>
</servlet-mapping>
```

### 5. Tomcat Manager Application

- Access via `http://localhost:8080/manager/html`
- Requires user role `manager-gui` in `conf/tomcat-users.xml`
- Features: Start/Stop apps, Deploy WAR, Session statistics

### 6. Debugging Common Issues

1. **ClassNotFoundException**: Check if servlet class is in `WEB-INF/classes/`
2. **404 Errors**: Verify URL mapping in web.xml
3. **Port Conflicts**: Change connector port in `conf/server.xml`

```xml
<Connector port="8585" protocol="HTTP/1.1" ... />
```

## Examples

### Example 1: Basic Servlet Deployment

**Step 1:** Create Servlet Class

```java
import jakarta.servlet.*;
import jakarta.servlet.http.*;

public class HelloServlet extends HttpServlet {
 protected void doGet(HttpServletRequest req, HttpServletResponse res)
 throws ServletException, IOException {
 res.setContentType("text/html");
 PrintWriter out = res.getWriter();
 out.println("<h1> Servlet Demo</h1>");
 }
}
```

**Step 2:** Compile and Create Directory Structure

```
MyApp/
└── WEB-INF/
 ├── web.xml
 └── classes/
 └── HelloServlet.class
```

**Step 3:** Create web.xml

```xml
<web-app>
 <servlet>
 <servlet-name>Hello</servlet-name>
 <servlet-class>HelloServlet</servlet-class>
 </servlet>

 <servlet-mapping>
 <servlet-name>Hello</servlet-name>
 <url-pattern>/hello</url-pattern>
 </servlet-mapping>
</web-app>
```

**Step 4:** Deploy and Test

```bash
jar cvf MyApp.war *
cp MyApp.war $CATALINA_HOME/webapps/
# Access via http://localhost:8080/MyApp/hello
```

### Example 2: Using Tomcat Manager

1. Create `manager` user in `conf/tomcat-users.xml`:

```xml
<user username="admin" password="admin123" roles="manager-gui"/>
```

2. Deploy WAR via Manager:

- Navigate to http://localhost:8080/manager/html
- Upload WAR file under "Deploy directory or WAR file"

3. Verify deployment in "Applications" list

## Real-World Applications

1. **E-Commerce**: Flipkart uses Tomcat clusters for high traffic handling
2. **Banking**: Axis Bank's net banking portal runs on Tomcat 10
3. **IoT Systems**: Tomcat's lightweight nature suits embedded device dashboards

## Exam Tips

1. **WAR Structure**: Always mention WEB-INF/classes and web.xml locations
2. **Port Configuration**: Remember server.xml contains Connector port setting
3. **Error Codes**:

- 404: Check URL mapping and WAR deployment
- 500: Servlet compilation errors (check logs)

4. **Servlet Lifecycle**: Tomcat controls init(), service(), destroy()
5. **Security**: Tomcat users are defined in tomcat-users.xml with role assignments
6. **JSP Compilation**: Compiled files appear in work/Catalina/localhost/
7. **Deployment Methods**: WAR vs exploded directory (faster for development)

**Common Questions**:

- "Explain Tomcat directory structure with diagram (5 marks)"
- "Steps to configure a servlet in web.xml (3 marks)"
- "Difference between Apache HTTP Server and Tomcat (2 marks)"
