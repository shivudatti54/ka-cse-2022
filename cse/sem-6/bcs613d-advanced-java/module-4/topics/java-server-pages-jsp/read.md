# Java Server Pages (JSP)

## Introduction

Java Server Pages (JSP) is a server-side programming technology that enables creation of dynamic web content using Java within HTML pages. Developed by Sun Microsystems in 1999, JSP simplifies web development by allowing **separation of presentation (HTML) from business logic (Java code)** through its tag-based scripting approach.

JSP operates on the **"Write Once, Run Anywhere"** principle and is compiled into servlets at runtime by the JSP container (like Apache Tomcat). This makes it crucial for building enterprise-scale web applications, particularly in MVC architectures where JSP serves as the **View component**.

Key advantages over plain servlets include:

1. Easier HTML content creation with JSP tags
2. Built-in support for session tracking
3. Automatic availability of **implicit objects** (request, response, session)
4. Integration with JavaBeans and custom tag libraries

## JSP Architecture

### Lifecycle Phases

1. **Translation**: Container converts JSP to servlet (.java)
2. **Compilation**: Servlet is compiled to .class
3. **Initialization**: `jspInit()` called once
4. **Request Handling**: `_jspService()` for each request
5. **Destruction**: `jspDestroy()` during shutdown

```java
// Sample generated servlet structure
public class hello_jsp extends HttpJspBase {
 public void _jspService(HttpServletRequest request,
 HttpServletResponse response)
 throws IOException, ServletException {
 // Implicit objects initialization
 JspWriter out = response.getWriter();
 // HTML generation
 out.print("<html><body>");
 out.print("Hello World!");
 out.print("</body></html>");
 }
}
```

## JSP Elements

### 1. Directives

Control page-level settings:

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" %>
<%@ include file="header.html" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
```

### 2. Declarations

Define variables/methods:

```jsp
<%! int counter = 0; %>
<%! public String getTimestamp() { return new Date().toString(); } %>
```

### 3. Scriptlets

Embed Java code:

```jsp
<%
 String user = request.getParameter("username");
 if(user != null) {
 session.setAttribute("user", user);
 }
%>
```

### 4. Expressions

Output values:

```jsp
Current time: <%= new java.util.Date() %>
User agent: ${header['User-Agent']}
```

### 5. Implicit Objects

Predefined variables available in JSP:

| Object      | Type                | Purpose                 |
| ----------- | ------------------- | ----------------------- |
| request     | HttpServletRequest  | HTTP request data       |
| response    | HttpServletResponse | HTTP response control   |
| session     | HttpSession         | User session management |
| application | ServletContext      | Application-wide data   |
| out         | JspWriter           | Output stream           |

## JSP Tag Libraries

### 1. Standard Actions

```jsp
<jsp:include page="header.jsp" />
<jsp:useBean id="cart" class="com.example.Cart" scope="session"/>
<jsp:setProperty name="cart" property="total" value="1500"/>
```

### 2. JSTL (JSP Standard Tag Library)

```jsp
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<c:forEach items="${products}" var="product">
 <tr>
 <td>${product.name}</td>
 <td><fmt:formatNumber value="${product.price}" type="currency"/></td>
 </tr>
</c:forEach>
```

## Examples

### Example 1: Basic JSP with Form Handling

```jsp
<%-- greeting.jsp --%>
<html>
<body>
 <form action="greeting.jsp" method="post">
 Name: <input type="text" name="username">
 <input type="submit" value="Submit">
 </form>

 <%
 if(request.getMethod().equalsIgnoreCase("POST")) {
 String name = request.getParameter("username");
 if(name != null && !name.isEmpty()) {
 %>
 <h3>Hello <%= name %>!</h3>
 <% }
 }
 %>
</body>
</html>
```

**Output:**

- Displays form on GET request
- Shows personalized greeting after POST

### Example 2: Session Tracking with JSP

```jsp
<%-- cart.jsp --%>
<%@ page import="java.util.ArrayList" %>
<%
 ArrayList<String> items = (ArrayList<String>) session.getAttribute("cart");
 if(items == null) {
 items = new ArrayList<>();
 session.setAttribute("cart", items);
 }

 String newItem = request.getParameter("item");
 if(newItem != null) {
 items.add(newItem);
 }
%>

<html>
<body>
 <h2>Your Cart:</h2>
 <ul>
 <% for(String item : items) { %>
 <li><%= item %></li>
 <% } %>
 </ul>

 <form method="post">
 Add item: <input type="text" name="item">
 <input type="submit" value="Add">
 </form>
</body>
</html>
```

**Output:**

- Maintains shopping cart items across requests using session
- Displays cumulative list of added items

## Real-World Applications

1. E-commerce product catalogs with dynamic pricing
2. Banking portals displaying real-time account data
3. Student information systems showing academic records
4. Social media feeds with personalized content
5. IoT dashboards visualizing sensor data

## Exam Tips

1. **Lifecycle Methods**: Remember `jspInit()`, `_jspService()`, and `jspDestroy()` sequence
2. **Directive Types**: `page`, `include`, `taglib` - know their attributes
3. **Implicit Objects**: Be able to list at least 5 with their types
4. **JSP vs Servlet**: JSP is presentation-centric, servlet is logic-centric
5. **Tag Differences**:

- `<%@ include %>` (compile-time) vs `<jsp:include>` (runtime)
- `<%= %>` vs `${}` (expression vs EL)

6. **Error Handling**: Use `errorPage` directive and `isErrorPage` attribute
7. **Scoping**: Understand page, request, session, application scopes

**Common Questions:**

- Explain JSP lifecycle with diagram
- Difference between JSP scriptlet and expression
- Write JSP code to display database records
- Explain JSTL core tags with examples
- How session tracking works in JSP
