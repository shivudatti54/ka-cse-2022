# Variables and Objects in JSP

## Introduction

Java Server Pages (JSP) variables and objects form the backbone of dynamic web content generation in Java-based web applications. Unlike standard Java variables, JSP introduces special handling of variables through scriptlets, declarations, and implicit objects that interact directly with the servlet container.

In JSP, variables can exist in different scopes - page, request, session, and application - determining their accessibility across multiple pages and user sessions. The technology provides nine implicit objects (request, response, session, application, out, config, page, pageContext, and exception) that are automatically available in every JSP page, eliminating the need for explicit declaration.

This concept is vital for students as it bridges servlet programming with presentation-layer development. Understanding JSP variables and objects enables developers to create personalized user experiences, handle form data efficiently, and maintain state across HTTP requests - essential skills for building e-commerce platforms, banking systems, and social media applications.

## JSP Variable Declaration

### Scriptlet Variables

```jsp
<%
 // Local variables in service method
 int counter = 0;
 String username = request.getParameter("user");
%>
```

- Exist within \_jspService() method
- Reinitialized on every request
- Not thread-safe

### Declaration Variables

```jsp
<%!
 // Instance variables of servlet class
 private int totalVisits = 0;
 public void logAccess() {
 // Method logic
 }
%>
```

- Declared using <%! %> syntax
- Become instance variables of generated servlet
- Require synchronization for thread safety

## Variable Scopes

| Scope       | Accessibility         | Typical Use Case               |
| ----------- | --------------------- | ------------------------------ |
| Page        | Current JSP page only | Temporary calculations         |
| Request     | Same request chain    | Form data processing           |
| Session     | User's entire session | Shopping carts, user profiles  |
| Application | All users/sessions    | Global counters, configuration |

## JSP Implicit Objects

### 1. request (HttpServletRequest)

```jsp
<%
 String userID = request.getParameter("uid");
 String[] hobbies = request.getParameterValues("hobbies");
 RequestDispatcher rd = request.getRequestDispatcher("profile.jsp");
%>
```

- Methods: getParameter(), getHeader(), getCookies()

### 2. response (HttpServletResponse)

```jsp
<%
 response.setContentType("application/pdf");
 response.addCookie(new Cookie("lang", "en_US"));
 response.sendRedirect("error.jsp");
%>
```

- Handles output streaming and redirection

### 3. session (HttpSession)

```jsp
<%
 session.setAttribute("cartItems", cart);
 Integer visitCount = (Integer) session.getAttribute("visits");
 session.setMaxInactiveInterval(1800); // 30 minutes
%>
```

- Maintains user-specific state

### 4. application (ServletContext)

```jsp
<%
 application.setAttribute("globalCounter", 0);
 String dbURL = application.getInitParameter("DB_URL");
%>
```

- Shared across all users

## Working with Cookies

### Creating Cookies

```jsp
<%
 Cookie colorPref = new Cookie("theme", "dark");
 colorPref.setMaxAge(604800); // 1 week
 response.addCookie(colorPref);
%>
```

### Reading Cookies

```jsp
<%
 Cookie[] cookies = request.getCookies();
 for(Cookie c : cookies) {
 if(c.getName().equals("theme")) {
 String theme = c.getValue();
 }
 }
%>
```

## Examples

### Example 1: User Login System

```jsp
<%-- login.jsp --%>
<form action="dashboard.jsp" method="post">
 Username: <input type="text" name="uname">
 Password: <input type="password" name="pwd">
 <input type="submit" value="Login">
</form>

<%-- dashboard.jsp --%>
<%
 String username = request.getParameter("uname");
 if(isValidUser(username)) {
 session.setAttribute("loggedUser", username);
 response.sendRedirect("welcome.jsp");
 }
%>
```

### Example 2: Page Visit Counter

```jsp
<%! private int globalCount = 0; %>

<%
 Integer sessionCount = (Integer) session.getAttribute("visits");
 if(sessionCount == null) sessionCount = 0;
 sessionCount++;
 session.setAttribute("visits", sessionCount);

 synchronized(this) {
 globalCount++;
 }
%>

<p>Your visits: <%= sessionCount %></p>
<p>Total visits: <%= globalCount %></p>
```

## JSP Object Lifecycle Diagram

The JSP execution flow involves:

1. Translation to servlet code
2. Compilation to bytecode
3. Initialization (jspInit())
4. Request processing (\_jspService())
5. Destruction (jspDestroy())

Implicit objects are created/destroyed automatically:

- request/response: Per client request
- session: Created on first use
- application: Exists for web app lifetime

## Exam Tips

1. **Implicit Objects Checklist**: Remember all 9 implicit objects - request, response, session, application, out, config, page, pageContext, exception

2. **Scope Priority**: When using findAttribute(), JSP searches scopes in order: page → request → session → application

3. **Cookie Handling**: Always set maxAge for persistent cookies. Session cookies expire when browser closes

4. **Thread Safety**: Declaration variables (<%! %>) require synchronization. Scriptlet variables are thread-safe by nature

5. **JSP-Servlet Relationship**: Remember that JSPs are eventually converted to servlets. session → HttpSession, application → ServletContext

6. **Common Methods**:

- request.getParameterMap()
- response.encodeURL() for session tracking
- session.invalidate()
- application.getRealPath()

7. **Error Handling**: Use exception implicit object only in error pages (isErrorPage="true")

8. **Expression Syntax**: <%= %> automatically converts to String. Equivalent to out.print()

9. **Attribute vs Parameter**: Parameters are read-only (from request), attributes can be set (request.setAttribute())

10. **PageContext Features**: Provides access to all scopes through setAttribute("name", value, PageContext.SESSION_SCOPE)
