# Session Tracking in Java Servlets

## Introduction to Session Tracking

Session tracking (also called session management) is a mechanism used in web applications to maintain state and identify users across multiple HTTP requests. Since HTTP is a **stateless protocol**, each request from a client to a server is treated as an independent transaction with no memory of previous interactions. Session tracking techniques enable web applications to remember user information, shopping cart contents, login status, and other data throughout a user's visit.

In Java Servlets, session tracking is essential for creating interactive, personalized web applications. Without session tracking, a web application would have no way to know that multiple requests came from the same user, making it impossible to implement features like user authentication, shopping carts, personalized content, or multi-page forms.

## Why Session Tracking is Needed

**Problems with HTTP's Statelessness:**

1. **No User Identity**: Server cannot identify which requests belong to which user
2. **No Data Persistence**: User data is lost between requests
3. **No Context**: Cannot maintain workflow across multiple pages
4. **No Personalization**: Cannot customize experience based on user preferences

**Example Scenario:**

```
User logs in → Request 1 (username: john, password: ****)
User views profile → Request 2 (server doesn't know who this is!)
User updates settings → Request 3 (server still doesn't know!)
```

Session tracking solves this by creating a unique identifier for each user's session and associating data with that identifier.

## Session Tracking Techniques in Java

Java Servlets provide four primary techniques for session tracking:

1. **Cookies**
2. **URL Rewriting**
3. **Hidden Form Fields**
4. **HttpSession API** (Most common and preferred)

## 1. HttpSession Interface - The Primary Mechanism

The **HttpSession interface** is the most powerful and commonly used mechanism for session tracking in Java servlets. It provides a way to identify a user across multiple requests and store user-specific data on the server side.

### Creating and Accessing Sessions

**Obtaining an HttpSession object:**

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class SessionDemoServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 // Get existing session or create a new one if it doesn't exist
 HttpSession session = request.getSession();

 // Get existing session only (returns null if no session exists)
 HttpSession existingSession = request.getSession(false);

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();

 if (session.isNew()) {
 out.println("<h2>Welcome! New session created.</h2>");
 } else {
 out.println("<h2>Welcome back! Existing session found.</h2>");
 }
 }
}
```

**Key Methods:**

- **`request.getSession()`**: Returns the current session, creating a new one if needed
- **`request.getSession(true)`**: Same as `getSession()` - creates session if not exists
- **`request.getSession(false)`**: Returns existing session or null (doesn't create new)

### Session Attributes - Storing and Retrieving Data

You can store any Java object in a session using attributes.

**Storing Data in Session:**

```java
@WebServlet("/login")
public class LoginServlet extends HttpServlet {
 protected void doPost(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 String username = request.getParameter("username");
 String password = request.getParameter("password");

 // Validate credentials (simplified)
 if (authenticateUser(username, password)) {
 HttpSession session = request.getSession();

 // Store user data in session
 session.setAttribute("username", username);
 session.setAttribute("loginTime", new java.util.Date());
 session.setAttribute("role", "ADMIN");

 response.sendRedirect("dashboard.jsp");
 } else {
 response.sendRedirect("login.jsp?error=invalid");
 }
 }

 private boolean authenticateUser(String username, String password) {
 // Database validation logic
 return true; // Simplified
 }
}
```

**Retrieving Data from Session:**

```java
@WebServlet("/dashboard")
public class DashboardServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 HttpSession session = request.getSession(false);
 response.setContentType("text/html");
 PrintWriter out = response.getWriter();

 if (session != null && session.getAttribute("username") != null) {
 String username = (String) session.getAttribute("username");
 String role = (String) session.getAttribute("role");

 out.println("<html><body>");
 out.println("<h1>Welcome, " + username + "!</h1>");
 out.println("<p>Your role: " + role + "</p>");
 out.println("</body></html>");
 } else {
 response.sendRedirect("login.jsp");
 }
 }
}
```

### Important HttpSession Methods

```java
HttpSession session = request.getSession();

// Storing attributes
session.setAttribute("key", valueObject);

// Retrieving attributes
Object value = session.getAttribute("key");
String username = (String) session.getAttribute("username");

// Removing attributes
session.removeAttribute("key");

// Get session ID
String sessionId = session.getId();

// Get creation time (milliseconds since epoch)
long creationTime = session.getCreationTime();

// Get last accessed time
long lastAccessTime = session.getLastAccessedTime();

// Check if session is new
boolean isNew = session.isNew();

// Set maximum inactive interval (seconds)
session.setMaxInactiveInterval(1800); // 30 minutes

// Get maximum inactive interval
int interval = session.getMaxInactiveInterval();

// Invalidate session (logout)
session.invalidate();

// Get all attribute names
java.util.Enumeration<String> names = session.getAttributeNames();
while (names.hasMoreElements()) {
 String name = names.nextElement();
 System.out.println(name + " = " + session.getAttribute(name));
}
```

## Session Lifecycle

### 1. Session Creation

```java
@WebServlet("/firstVisit")
public class FirstVisitServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 HttpSession session = request.getSession(); // Creates new session

 if (session.isNew()) {
 // Initialize session data
 session.setAttribute("visitCount", 1);
 session.setAttribute("firstVisit", new java.util.Date());
 }
 }
}
```

### 2. Session Usage

```java
@WebServlet("/page")
public class PageServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 HttpSession session = request.getSession(false);

 if (session != null) {
 // Update visit count
 Integer visitCount = (Integer) session.getAttribute("visitCount");
 if (visitCount == null) {
 visitCount = 1;
 } else {
 visitCount++;
 }
 session.setAttribute("visitCount", visitCount);

 response.getWriter().println("Visit count: " + visitCount);
 }
 }
}
```

### 3. Session Timeout

Sessions can timeout due to inactivity. You can configure timeout in two ways:

**Programmatically:**

```java
// Set timeout to 20 minutes (1200 seconds)
session.setMaxInactiveInterval(1200);

// Set to never timeout (not recommended)
session.setMaxInactiveInterval(-1);
```

**In web.xml:**

```xml
<web-app>
 <session-config>
 <!-- Timeout in minutes -->
 <session-timeout>30</session-timeout>
 </session-config>
</web-app>
```

### 4. Session Invalidation (Logout)

```java
@WebServlet("/logout")
public class LogoutServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 HttpSession session = request.getSession(false);

 if (session != null) {
 // Get username before invalidating
 String username = (String) session.getAttribute("username");
 System.out.println("User " + username + " logged out");

 // Invalidate session
 session.invalidate();
 }

 response.sendRedirect("login.jsp?message=logout");
 }
}
```

## Complete Shopping Cart Example

```java
// Product class
class Product {
 private String name;
 private double price;

 public Product(String name, double price) {
 this.name = name;
 this.price = price;
 }

 public String getName() { return name; }
 public double getPrice() { return price; }
}

// Add to cart servlet
@WebServlet("/addToCart")
public class AddToCartServlet extends HttpServlet {
 protected void doPost(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 String productName = request.getParameter("product");
 double price = Double.parseDouble(request.getParameter("price"));

 HttpSession session = request.getSession();

 // Get or create cart
 List<Product> cart = (List<Product>) session.getAttribute("cart");
 if (cart == null) {
 cart = new ArrayList<>();
 session.setAttribute("cart", cart);
 }

 // Add product to cart
 cart.add(new Product(productName, price));

 response.sendRedirect("cart.jsp");
 }
}

// View cart servlet
@WebServlet("/viewCart")
public class ViewCartServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 HttpSession session = request.getSession(false);
 response.setContentType("text/html");
 PrintWriter out = response.getWriter();

 out.println("<html><body>");
 out.println("<h2>Your Shopping Cart</h2>");

 if (session != null) {
 List<Product> cart = (List<Product>) session.getAttribute("cart");

 if (cart != null && !cart.isEmpty()) {
 double total = 0;

 out.println("<table border='1'>");
 out.println("<tr><th>Product</th><th>Price</th></tr>");

 for (Product product : cart) {
 out.println("<tr>");
 out.println("<td>" + product.getName() + "</td>");
 out.println("<td>$" + product.getPrice() + "</td>");
 out.println("</tr>");
 total += product.getPrice();
 }

 out.println("</table>");
 out.println("<h3>Total: $" + total + "</h3>");
 } else {
 out.println("<p>Your cart is empty.</p>");
 }
 }

 out.println("</body></html>");
 }
}
```

## User Authentication Example

```java
@WebServlet("/secureLogin")
public class SecureLoginServlet extends HttpServlet {
 protected void doPost(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 String username = request.getParameter("username");
 String password = request.getParameter("password");

 // Validate credentials
 if (validateCredentials(username, password)) {
 // Create new session
 HttpSession session = request.getSession(true);

 // Store user information
 session.setAttribute("username", username);
 session.setAttribute("authenticated", true);
 session.setAttribute("loginTime", new java.util.Date());

 // Set session timeout (30 minutes)
 session.setMaxInactiveInterval(1800);

 // Redirect to dashboard
 response.sendRedirect("dashboard");
 } else {
 // Redirect back to login with error
 response.sendRedirect("login.jsp?error=invalid");
 }
 }

 private boolean validateCredentials(String username, String password) {
 // Database validation logic
 return true; // Simplified
 }
}

// Protected page servlet
@WebServlet("/dashboard")
public class DashboardServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 HttpSession session = request.getSession(false);

 // Check if user is authenticated
 if (session == null || session.getAttribute("authenticated") == null) {
 response.sendRedirect("login.jsp");
 return;
 }

 Boolean authenticated = (Boolean) session.getAttribute("authenticated");
 if (!authenticated) {
 response.sendRedirect("login.jsp");
 return;
 }

 // User is authenticated, show dashboard
 String username = (String) session.getAttribute("username");
 response.setContentType("text/html");
 PrintWriter out = response.getWriter();

 out.println("<html><body>");
 out.println("<h1>Welcome, " + username + "!</h1>");
 out.println("<p>You are logged in.</p>");
 out.println("<a href='logout'>Logout</a>");
 out.println("</body></html>");
 }
}
```

## URL Rewriting (Alternative Technique)

URL rewriting appends the session ID to every URL when cookies are disabled.

```java
@WebServlet("/urlRewriting")
public class URLRewritingServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 HttpSession session = request.getSession();
 session.setAttribute("username", "John");

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();

 // Encode URLs with session ID
 String url1 = response.encodeURL("page1.jsp");
 String url2 = response.encodeURL("page2.jsp");

 out.println("<html><body>");
 out.println("<h2>Session ID: " + session.getId() + "</h2>");
 out.println("<a href='" + url1 + "'>Page 1</a><br>");
 out.println("<a href='" + url2 + "'>Page 2</a>");
 out.println("</body></html>");
 }
}
```

**Note**: The `encodeURL()` method automatically appends `;jsessionid=...` to URLs if cookies are disabled.

## Hidden Form Fields (Alternative Technique)

```java
// First servlet
@WebServlet("/step1")
public class Step1Servlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();

 out.println("<html><body>");
 out.println("<form action='step2' method='post'>");
 out.println("Name: <input type='text' name='name'><br>");
 out.println("<input type='submit' value='Next'>");
 out.println("</form>");
 out.println("</body></html>");
 }
}

// Second servlet
@WebServlet("/step2")
public class Step2Servlet extends HttpServlet {
 protected void doPost(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 String name = request.getParameter("name");

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();

 out.println("<html><body>");
 out.println("<form action='step3' method='post'>");
 out.println("Email: <input type='text' name='email'><br>");
 // Hidden field to carry data from previous step
 out.println("<input type='hidden' name='name' value='" + name + "'>");
 out.println("<input type='submit' value='Finish'>");
 out.println("</form>");
 out.println("</body></html>");
 }
}
```

## Session Security Best Practices

### 1. Always Validate Sessions

```java
HttpSession session = request.getSession(false);
if (session == null || session.getAttribute("authenticated") == null) {
 response.sendRedirect("login.jsp");
 return;
}
```

### 2. Regenerate Session ID After Login

```java
// After successful authentication
HttpSession oldSession = request.getSession(false);
if (oldSession != null) {
 oldSession.invalidate();
}

// Create new session with new ID
HttpSession newSession = request.getSession(true);
newSession.setAttribute("username", username);
```

### 3. Use HTTPS for Sensitive Data

Configure session cookies to be secure (only transmitted over HTTPS):

```xml
<session-config>
 <cookie-config>
 <secure>true</secure>
 <http-only>true</http-only>
 </cookie-config>
</session-config>
```

### 4. Set Appropriate Timeouts

```java
// Shorter timeout for sensitive applications
session.setMaxInactiveInterval(900); // 15 minutes
```

## Common Mistakes to Avoid

### 1. Not Checking for Null Session

```java
// Wrong: May throw NullPointerException
HttpSession session = request.getSession(false);
String username = (String) session.getAttribute("username"); // Error if session is null

// Correct
HttpSession session = request.getSession(false);
if (session != null) {
 String username = (String) session.getAttribute("username");
}
```

### 2. Not Casting Retrieved Attributes

```java
// Wrong: ClassCastException
Integer count = session.getAttribute("count"); // Returns Object

// Correct
Integer count = (Integer) session.getAttribute("count");
```

### 3. Forgetting to Invalidate on Logout

```java
// Always invalidate session on logout
session.invalidate();
```

### 4. Storing Too Much Data in Session

```java
// Bad: Storing large objects affects performance
session.setAttribute("largeDataSet", hugeDatabaseQuery());

// Good: Store only necessary data
session.setAttribute("userId", userId);
```

## Exam Tips

1. **Understand the need**: Know why session tracking is needed (HTTP statelessness)
2. **HttpSession methods**: Memorize key methods like `getAttribute()`, `setAttribute()`, `invalidate()`
3. **Session lifecycle**: Understand creation, usage, timeout, and invalidation
4. **Session vs Request scope**: Session persists across requests, request scope is single request
5. **getSession(true) vs getSession(false)**: Know the difference and when to use each
6. **Security concerns**: Session hijacking, fixation, timeout configuration
7. **Alternative techniques**: Know URL rewriting and hidden form fields as alternatives
8. **Common use cases**: Shopping cart, user authentication, multi-step forms
9. **Session timeout**: Both programmatic (`setMaxInactiveInterval`) and configuration (`web.xml`)
10. **Thread safety**: Sessions are shared across requests, be careful with concurrent modifications

**Sample Exam Questions:**

- Implement a login system using HttpSession
- Create a page counter that tracks user visits
- Build a shopping cart using session tracking
- Explain the difference between `getSession()` and `getSession(false)`
- Write code to check if a user is authenticated
- Implement logout functionality
- Configure session timeout in web.xml
- Handle session expiration gracefully

### Further Reading

Refer to your prescribed textbook and official course materials.
