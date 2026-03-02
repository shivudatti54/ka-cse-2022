# Servlet and JSP Methods

## Introduction to Servlet and JSP Methods

Servlet and JSP methods form the backbone of Java web application development, providing structured mechanisms to handle HTTP requests, process business logic, and generate dynamic responses. These methods implement the core functionality specified in the Jakarta Servlet API and JSP specifications, making them essential for students studying Advanced Java.

In servlet programming, methods like `init()`, `service()`, and `destroy()` define the lifecycle of a web component. JSP (JavaServer Pages) extends this with its own lifecycle methods like `jspInit()` and `jspDestroy()`, while using special tags and scriptlets to embed Java logic in HTML. Understanding these methods is critical for developing exam-ready web applications that follow proper MVC architecture.

Key importance areas:

1. Handling GET/POST requests through `doGet()` and `doPost()`
2. Managing application state with cookies via `addCookie()`
3. Accessing request parameters using `getParameter()`
4. Implementing JSP lifecycle hooks
5. Using implicit objects in JSP like `request` and `response`

## Servlet Lifecycle Methods

### 1. init() Method

```java
public void init(ServletConfig config) throws ServletException {
 super.init(config);
 // Initialization code
}
```

- First method called by container
- Executed only once during servlet initialization
- Used for resource allocation (database connections, config loading)

### 2. service() Method

```java
protected void service(HttpServletRequest req, HttpServletResponse res)
 throws ServletException, IOException {
 // Request dispatching logic
}
```

- Handles all client requests
- Delegates to doGet()/doPost() based on HTTP method
- Override with caution (usually better to override specific methods)

### 3. destroy() Method

```java
public void destroy() {
 // Cleanup code
}
```

- Called before servlet removal from memory
- Used for resource deallocation
- Guaranteed execution only once

## HTTP Handler Methods

### doGet()

```java
protected void doGet(HttpServletRequest request,
 HttpServletResponse response)
 throws ServletException, IOException {
 // Handle GET requests
}
```

- Processes HTTP GET requests
- Parameters visible in URL
- Limited data capacity (URL length restrictions)

### doPost()

```java
protected void doPost(HttpServletRequest request,
 HttpServletResponse response)
 throws ServletException, IOException {
 // Handle POST requests
}
```

- Processes form submissions
- Parameters sent in request body
- No size limitations
- More secure for sensitive data

## JSP Lifecycle Methods

### jspInit()

```java
<%!
 public void jspInit() {
 // Initialization code
 }
%>
```

- Called when JSP is first loaded
- Similar to servlet's init()
- Declared using declaration tags (<%! %>)

### \_jspService()

```java
// Auto-generated method
public void _jspService(HttpServletRequest request,
 HttpServletResponse response)
 throws ServletException, IOException {
 // JSP processing logic
}
```

- Automatically created by JSP container
- Contains all JSP page logic
- Never overridden directly

## Key Servlet API Methods

### Reading Parameters

```java
String username = request.getParameter("uname");
String[] hobbies = request.getParameterValues("hobbies");
```

- `getParameter()`: Returns single value parameter
- `getParameterValues()`: Returns array for multi-value parameters

### Cookie Handling

```java
// Creating cookie
Cookie userCookie = new Cookie("lastVisit", new Date().toString());
response.addCookie(userCookie);

// Reading cookies
Cookie[] cookies = request.getCookies();
```

- `addCookie()`: Adds cookie to response
- `getCookies()`: Retrieves all cookies from request

## JSP Tag Methods

### Scriptlet Tags

```jsp
<%
 int count = 0;
 count++;
 out.print("Page visits: " + count);
%>
```

- Embeds Java code in JSP
- Becomes part of \_jspService()

### Expression Tags

```jsp
Current time: <%= new java.util.Date() %>
```

- Outputs expression result
- Automatically converts to String

## Examples

### Example 1: Complete Servlet with GET/POST Handling

```java
public class LoginServlet extends HttpServlet {

 public void init() { /* DB connection setup */ }

 protected void doPost(HttpServletRequest request,
 HttpServletResponse response)
 throws ServletException, IOException {

 String user = request.getParameter("username");
 String pass = request.getParameter("password");

 if(authenticate(user, pass)) {
 Cookie authCookie = new Cookie("auth", "true");
 response.addCookie(authCookie);
 response.sendRedirect("welcome.jsp");
 } else {
 response.sendError(HttpServletResponse.SC_UNAUTHORIZED);
 }
 }

 public void destroy() { /* Close DB connection */ }
}
```

### Example 2: JSP Page with Lifecycle Methods

```jsp
<%@ page import="java.util.Date" %>
<%!
 private int accessCount = 0;

 public void jspInit() {
 log("JSP initialized");
 }
%>

<%
 accessCount++;
 Date now = new Date();
%>

<html>
<body>
 <p>Page accessed <%= accessCount %> times</p>
 <p>Current time: <%= now %></p>
</body>
</html>

<%!
 public void jspDestroy() {
 log("JSP destroyed");
 }
%>
```

## Exam Tips

1. **Lifecycle Order**: Remember init() → service() → destroy() sequence. For JSP: jspInit() → \_jspService() → jspDestroy()
2. **GET vs POST**:

- GET: Bookmarkable, parameters in URL, limited size
- POST: Secure data, parameters in body, no size limits

3. **Cookie Methods**: Use response.addCookie() to send, request.getCookies() to retrieve
4. **Parameter Handling**: Always check for null values with getParameter()
5. **JSP Translation**: Understand that JSPs become servlets (\_jspService() method)
6. **HTTP Status Codes**: Know common codes - 200 (OK), 404 (Not Found), 500 (Internal Error)
7. **Servlet Config**: Difference between ServletConfig (per-servlet) and ServletContext (application-wide)

## Real-World Applications

1. **E-commerce**: Session tracking using cookies for shopping carts
2. **Banking Systems**: Secure form handling with POST method
3. **Social Media**: Dynamic content generation using JSP scriptlets
4. **APIs**: RESTful services using doGet()/doPost()/doPut()/doDelete()

## Architectural Diagram (Text Description)

**Servlet Request Flow:**

1. Client sends HTTP request
2. Web server routes to servlet container
3. Container calls service() method
4. service() delegates to doGet()/doPost()
5. Servlet processes request using parameters
6. Generates response (HTML/JSON/XML)
7. Response sent back to client

**JSP Translation Process:**

1. JSP file created with HTML/Java mix
2. Container translates to servlet (.java)
3. Servlet compiled to .class
4. Container loads servlet class
5. Lifecycle methods executed
6. \_jspService() generates dynamic content
