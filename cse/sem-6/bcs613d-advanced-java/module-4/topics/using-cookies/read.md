# Using Cookies in Java Servlets

## Introduction to Cookies

Cookies are small pieces of data that a web server sends to a client's web browser, which the browser stores and sends back to the server with subsequent requests. In Java Servlets, the **Cookie class** (javax.servlet.http.Cookie) provides methods to create, read, modify, and manage cookies for session tracking and storing user preferences.

Cookies are one of the earliest and most widely used mechanisms for maintaining state in web applications. Unlike server-side session tracking, cookies store data on the client side, making them lightweight for the server but requiring careful handling due to security and privacy concerns.

## Why Use Cookies?

**Key Benefits:**

1. **Client-Side Storage**: Data stored on user's browser, reducing server memory usage
2. **Persistent State**: Can persist data across browser sessions
3. **User Preferences**: Store theme, language, settings without server load
4. **Automatic Transmission**: Browser automatically sends cookies with each request
5. **Multiple Users**: Each user has their own cookies

**Common Use Cases:**

- Remember user login (Remember Me feature)
- Store user preferences (theme, language, timezone)
- Track shopping cart items
- Store session identifiers
- Analytics and tracking
- Personalization

## Cookie Basics

### Cookie Structure

A cookie consists of:

- **Name**: Identifier for the cookie
- **Value**: Data stored in the cookie
- **Domain**: Domain that can access the cookie
- **Path**: URL path where cookie is valid
- **Max Age**: Lifetime of the cookie in seconds
- **Secure Flag**: Send only over HTTPS
- **HttpOnly Flag**: Inaccessible to JavaScript

## Creating Cookies in Java

### Basic Cookie Creation

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

@WebServlet("/createCookie")
public class CreateCookieServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 // Create a new cookie with name and value
 Cookie cookie = new Cookie("username", "JohnDoe");

 // Add cookie to the response
 response.addCookie(cookie);

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();
 out.println("<html><body>");
 out.println("<h2>Cookie created successfully!</h2>");
 out.println("<p>Cookie Name: username</p>");
 out.println("<p>Cookie Value: JohnDoe</p>");
 out.println("</body></html>");
 }
}
```

### Creating Multiple Cookies

```java
@WebServlet("/createMultipleCookies")
public class MultipleCookiesServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 // Create multiple cookies
 Cookie usernameCookie = new Cookie("username", "alice");
 Cookie themeCookie = new Cookie("theme", "dark");
 Cookie languageCookie = new Cookie("language", "en");

 // Add all cookies to response
 response.addCookie(usernameCookie);
 response.addCookie(themeCookie);
 response.addCookie(languageCookie);

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();
 out.println("<html><body>");
 out.println("<h2>Multiple cookies created!</h2>");
 out.println("</body></html>");
 }
}
```

## Reading Cookies

### Retrieving Cookies from Request

```java
@WebServlet("/readCookies")
public class ReadCookiesServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();

 out.println("<html><body>");
 out.println("<h2>Cookies Received:</h2>");

 // Get all cookies from the request
 Cookie[] cookies = request.getCookies();

 if (cookies != null && cookies.length > 0) {
 out.println("<table border='1'>");
 out.println("<tr><th>Cookie Name</th><th>Cookie Value</th></tr>");

 for (Cookie cookie : cookies) {
 String name = cookie.getName();
 String value = cookie.getValue();

 out.println("<tr>");
 out.println("<td>" + name + "</td>");
 out.println("<td>" + value + "</td>");
 out.println("</tr>");
 }

 out.println("</table>");
 } else {
 out.println("<p>No cookies found!</p>");
 }

 out.println("</body></html>");
 }
}
```

### Finding a Specific Cookie

```java
@WebServlet("/findCookie")
public class FindCookieServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 String cookieToFind = "username";
 String cookieValue = getCookieValue(request, cookieToFind);

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();

 out.println("<html><body>");
 if (cookieValue != null) {
 out.println("<h2>Cookie Found!</h2>");
 out.println("<p>" + cookieToFind + " = " + cookieValue + "</p>");
 } else {
 out.println("<h2>Cookie Not Found!</h2>");
 out.println("<p>No cookie named '" + cookieToFind + "'</p>");
 }
 out.println("</body></html>");
 }

 // Helper method to find cookie by name
 private String getCookieValue(HttpServletRequest request, String cookieName) {
 Cookie[] cookies = request.getCookies();

 if (cookies != null) {
 for (Cookie cookie : cookies) {
 if (cookie.getName().equals(cookieName)) {
 return cookie.getValue();
 }
 }
 }
 return null; // Cookie not found
 }
}
```

## Cookie Attributes and Methods

### Setting Cookie Attributes

```java
@WebServlet("/cookieAttributes")
public class CookieAttributesServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 Cookie cookie = new Cookie("userPreferences", "theme=dark;lang=en");

 // Set maximum age (in seconds)
 // Positive: Persistent cookie (stored on disk)
 // Negative: Session cookie (deleted when browser closes)
 // Zero: Delete cookie immediately
 cookie.setMaxAge(7 * 24 * 60 * 60); // 7 days

 // Set domain - cookie sent to all subdomains
 cookie.setDomain(".example.com");

 // Set path - cookie sent only to this path and subdirectories
 cookie.setPath("/app");

 // Secure flag - cookie sent only over HTTPS
 cookie.setSecure(true);

 // HttpOnly flag - cookie not accessible via JavaScript
 cookie.setHttpOnly(true);

 // Add cookie to response
 response.addCookie(cookie);

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();
 out.println("<html><body>");
 out.println("<h2>Cookie with attributes created!</h2>");
 out.println("<p>Max Age: 7 days</p>");
 out.println("<p>Secure: true</p>");
 out.println("<p>HttpOnly: true</p>");
 out.println("</body></html>");
 }
}
```

### Cookie Methods Reference

```java
Cookie cookie = new Cookie("name", "value");

// Setting attributes
cookie.setMaxAge(3600); // Lifetime in seconds
cookie.setPath("/myapp"); // Path scope
cookie.setDomain("example.com"); // Domain scope
cookie.setSecure(true); // HTTPS only
cookie.setHttpOnly(true); // No JavaScript access
cookie.setComment("User preference cookie"); // Description
cookie.setValue("newValue"); // Update value

// Getting attributes
String name = cookie.getName();
String value = cookie.getValue();
int maxAge = cookie.getMaxAge();
String path = cookie.getPath();
String domain = cookie.getDomain();
boolean isSecure = cookie.getSecure();
boolean isHttpOnly = cookie.isHttpOnly();
String comment = cookie.getComment();
int version = cookie.getVersion();
```

## Cookie Lifetime Management

### Session Cookies (Temporary)

Session cookies exist only for the current browser session and are deleted when the browser closes.

```java
@WebServlet("/sessionCookie")
public class SessionCookieServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 // Create a session cookie (no setMaxAge or negative value)
 Cookie sessionCookie = new Cookie("sessionData", "temporaryValue");
 sessionCookie.setMaxAge(-1); // Session cookie (deleted on browser close)

 response.addCookie(sessionCookie);

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();
 out.println("<html><body>");
 out.println("<h2>Session Cookie Created</h2>");
 out.println("<p>This cookie will be deleted when you close your browser.</p>");
 out.println("</body></html>");
 }
}
```

### Persistent Cookies

Persistent cookies remain stored on the user's device for a specified duration.

```java
@WebServlet("/persistentCookie")
public class PersistentCookieServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 // Create a persistent cookie (30 days)
 Cookie persistentCookie = new Cookie("userPreference", "darkTheme");
 persistentCookie.setMaxAge(30 * 24 * 60 * 60); // 30 days in seconds

 response.addCookie(persistentCookie);

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();
 out.println("<html><body>");
 out.println("<h2>Persistent Cookie Created</h2>");
 out.println("<p>This cookie will last for 30 days.</p>");
 out.println("</body></html>");
 }
}
```

### Deleting Cookies

To delete a cookie, set its max age to zero and add it to the response.

```java
@WebServlet("/deleteCookie")
public class DeleteCookieServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 String cookieToDelete = request.getParameter("name");

 if (cookieToDelete != null) {
 // Create cookie with same name
 Cookie cookie = new Cookie(cookieToDelete, "");
 cookie.setMaxAge(0); // Set max age to 0 to delete
 cookie.setPath("/"); // Must match original path

 response.addCookie(cookie);
 }

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();
 out.println("<html><body>");
 out.println("<h2>Cookie Deleted</h2>");
 out.println("<p>Cookie '" + cookieToDelete + "' has been removed.</p>");
 out.println("</body></html>");
 }
}
```

## Practical Examples

### Example 1: Remember Me Login

```java
@WebServlet("/rememberMeLogin")
public class RememberMeLoginServlet extends HttpServlet {
 protected void doPost(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 String username = request.getParameter("username");
 String password = request.getParameter("password");
 String rememberMe = request.getParameter("rememberMe");

 // Validate credentials (simplified)
 if (validateUser(username, password)) {
 // Create session
 HttpSession session = request.getSession();
 session.setAttribute("username", username);

 // If "Remember Me" is checked, create persistent cookie
 if (rememberMe != null && rememberMe.equals("on")) {
 Cookie userCookie = new Cookie("rememberedUser", username);
 userCookie.setMaxAge(30 * 24 * 60 * 60); // 30 days
 userCookie.setHttpOnly(true);
 userCookie.setSecure(true);
 response.addCookie(userCookie);
 }

 response.sendRedirect("dashboard.jsp");
 } else {
 response.sendRedirect("login.jsp?error=invalid");
 }
 }

 private boolean validateUser(String username, String password) {
 // Database validation
 return true; // Simplified
 }
}

// Check for remembered user on login page
@WebServlet("/checkRememberedUser")
public class CheckRememberedUserServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 String rememberedUser = getCookieValue(request, "rememberedUser");

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();

 out.println("<html><body>");
 out.println("<h2>Login</h2>");

 if (rememberedUser != null) {
 out.println("<p>Welcome back, " + rememberedUser + "!</p>");
 out.println("<form method='post' action='rememberMeLogin'>");
 out.println("Username: <input type='text' name='username' value='" +
 rememberedUser + "'><br>");
 } else {
 out.println("<form method='post' action='rememberMeLogin'>");
 out.println("Username: <input type='text' name='username'><br>");
 }

 out.println("Password: <input type='password' name='password'><br>");
 out.println("<input type='checkbox' name='rememberMe'> Remember Me<br>");
 out.println("<input type='submit' value='Login'>");
 out.println("</form>");
 out.println("</body></html>");
 }

 private String getCookieValue(HttpServletRequest request, String cookieName) {
 Cookie[] cookies = request.getCookies();
 if (cookies != null) {
 for (Cookie cookie : cookies) {
 if (cookie.getName().equals(cookieName)) {
 return cookie.getValue();
 }
 }
 }
 return null;
 }
}
```

### Example 2: Visit Counter

```java
@WebServlet("/visitCounter")
public class VisitCounterServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 int visitCount = 1;

 // Check for existing visit count cookie
 Cookie[] cookies = request.getCookies();
 if (cookies != null) {
 for (Cookie cookie : cookies) {
 if (cookie.getName().equals("visitCount")) {
 visitCount = Integer.parseInt(cookie.getValue()) + 1;
 break;
 }
 }
 }

 // Create/update cookie with new count
 Cookie visitCookie = new Cookie("visitCount", String.valueOf(visitCount));
 visitCookie.setMaxAge(365 * 24 * 60 * 60); // 1 year
 response.addCookie(visitCookie);

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();
 out.println("<html><body>");
 out.println("<h2>Welcome!</h2>");
 out.println("<p>You have visited this page " + visitCount + " time(s).</p>");
 out.println("</body></html>");
 }
}
```

### Example 3: Last Visit Timestamp

```java
@WebServlet("/lastVisit")
public class LastVisitServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 String lastVisitTime = getCookieValue(request, "lastVisit");

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();
 out.println("<html><body>");
 out.println("<h2>Last Visit Tracker</h2>");

 if (lastVisitTime != null) {
 out.println("<p>Your last visit: " + lastVisitTime + "</p>");
 } else {
 out.println("<p>This is your first visit!</p>");
 }

 // Set current time as last visit
 String currentTime = new java.util.Date().toString();
 Cookie lastVisitCookie = new Cookie("lastVisit", currentTime);
 lastVisitCookie.setMaxAge(365 * 24 * 60 * 60); // 1 year
 response.addCookie(lastVisitCookie);

 out.println("</body></html>");
 }

 private String getCookieValue(HttpServletRequest request, String cookieName) {
 Cookie[] cookies = request.getCookies();
 if (cookies != null) {
 for (Cookie cookie : cookies) {
 if (cookie.getName().equals(cookieName)) {
 return cookie.getValue();
 }
 }
 }
 return null;
 }
}
```

### Example 4: Theme Preference

```java
@WebServlet("/themeSelector")
public class ThemeSelectorServlet extends HttpServlet {
 protected void doPost(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 String selectedTheme = request.getParameter("theme");

 // Store theme preference in cookie
 Cookie themeCookie = new Cookie("userTheme", selectedTheme);
 themeCookie.setMaxAge(365 * 24 * 60 * 60); // 1 year
 themeCookie.setPath("/");
 response.addCookie(themeCookie);

 response.sendRedirect("homepage");
 }
}

@WebServlet("/homepage")
public class HomepageServlet extends HttpServlet {
 protected void doGet(HttpServletRequest request, HttpServletResponse response)
 throws ServletException, IOException {

 String theme = getCookieValue(request, "userTheme");
 if (theme == null) {
 theme = "light"; // Default theme
 }

 response.setContentType("text/html");
 PrintWriter out = response.getWriter();

 String backgroundColor = theme.equals("dark") ? "#333" : "#fff";
 String textColor = theme.equals("dark") ? "#fff" : "#000";

 out.println("<html>");
 out.println("<head><style>");
 out.println("body { background-color: " + backgroundColor +
 "; color: " + textColor + "; }");
 out.println("</style></head>");
 out.println("<body>");
 out.println("<h1>Homepage</h1>");
 out.println("<p>Current theme: " + theme + "</p>");
 out.println("<form method='post' action='themeSelector'>");
 out.println("<select name='theme'>");
 out.println("<option value='light'>Light</option>");
 out.println("<option value='dark'>Dark</option>");
 out.println("</select>");
 out.println("<input type='submit' value='Change Theme'>");
 out.println("</form>");
 out.println("</body></html>");
 }

 private String getCookieValue(HttpServletRequest request, String cookieName) {
 Cookie[] cookies = request.getCookies();
 if (cookies != null) {
 for (Cookie cookie : cookies) {
 if (cookie.getName().equals(cookieName)) {
 return cookie.getValue();
 }
 }
 }
 return null;
 }
}
```

## Cookie Limitations and Considerations

### Size and Number Limitations

- **Maximum cookie size**: 4KB (4096 bytes)
- **Maximum cookies per domain**: Typically 20-50 (browser-dependent)
- **Maximum total cookies**: Typically 300 (browser-dependent)

### Cookie Naming Rules

```java
// Valid cookie names
Cookie cookie1 = new Cookie("username", "john");
Cookie cookie2 = new Cookie("user_preference", "value");
Cookie cookie3 = new Cookie("SESSION_ID", "12345");

// Invalid cookie names (will cause exceptions)
// Cookie badCookie1 = new Cookie("user name", "john"); // No spaces
// Cookie badCookie2 = new Cookie("user,name", "john"); // No commas
// Cookie badCookie3 = new Cookie("user;name", "john"); // No semicolons
```

### Encoding Special Characters

```java
import java.net.URLEncoder;
import java.net.URLDecoder;

// Encoding cookie value
String value = "user@example.com";
String encodedValue = URLEncoder.encode(value, "UTF-8");
Cookie cookie = new Cookie("email", encodedValue);
response.addCookie(cookie);

// Decoding cookie value
String decodedValue = URLDecoder.decode(cookie.getValue(), "UTF-8");
```

## Security Considerations

### 1. Secure Attribute

```java
// Always use secure flag for sensitive cookies
Cookie cookie = new Cookie("authToken", "secureToken123");
cookie.setSecure(true); // Sent only over HTTPS
response.addCookie(cookie);
```

### 2. HttpOnly Attribute

```java
// Prevent JavaScript access to cookies
Cookie cookie = new Cookie("sessionId", "abc123");
cookie.setHttpOnly(true); // Not accessible via document.cookie
response.addCookie(cookie);
```

### 3. Never Store Sensitive Data

```java
// NEVER DO THIS
// Cookie badCookie = new Cookie("password", "userPassword123");

// DO THIS INSTEAD
Cookie goodCookie = new Cookie("sessionId", generateSecureToken());
```

### 4. Domain and Path Restrictions

```java
Cookie cookie = new Cookie("data", "value");
cookie.setDomain(".mysite.com"); // Available to all subdomains
cookie.setPath("/secure"); // Available only under /secure path
response.addCookie(cookie);
```

## Common Mistakes to Avoid

### 1. Forgetting to Check for Null

```java
// Wrong: NullPointerException if no cookies
Cookie[] cookies = request.getCookies();
for (Cookie cookie : cookies) { // Error if cookies is null
 // Process cookie
}

// Correct
Cookie[] cookies = request.getCookies();
if (cookies != null) {
 for (Cookie cookie : cookies) {
 // Process cookie
 }
}
```

### 2. Not Setting Path When Deleting

```java
// Wrong: Cookie might not be deleted if path doesn't match
Cookie cookie = new Cookie("name", "");
cookie.setMaxAge(0);
response.addCookie(cookie);

// Correct: Set same path as original cookie
Cookie cookie = new Cookie("name", "");
cookie.setMaxAge(0);
cookie.setPath("/"); // Match original path
response.addCookie(cookie);
```

### 3. Storing Too Much Data

```java
// Bad: Exceeds 4KB limit
String largeData = generateLargeString(5000);
Cookie cookie = new Cookie("data", largeData); // May fail silently

// Good: Store reference, keep data server-side
String userId = "12345";
Cookie cookie = new Cookie("userId", userId);
```

### 4. Not URL Encoding Special Characters

```java
// Wrong: Special characters cause issues
Cookie cookie = new Cookie("email", "user@example.com"); // @ may cause issues

// Correct: URL encode the value
String encodedEmail = URLEncoder.encode("user@example.com", "UTF-8");
Cookie cookie = new Cookie("email", encodedEmail);
```

## Exam Tips

1. **Cookie class**: Know the constructor `new Cookie(name, value)`
2. **Key methods**: `setMaxAge()`, `setPath()`, `setDomain()`, `setSecure()`, `setHttpOnly()`
3. **Reading cookies**: Use `request.getCookies()` which returns `Cookie[]` (can be null)
4. **Adding cookies**: Use `response.addCookie(cookie)`
5. **Deleting cookies**: Set `maxAge` to 0 and add to response
6. **Session vs Persistent**: Negative maxAge = session, positive = persistent
7. **Security flags**: `setSecure(true)` for HTTPS, `setHttpOnly(true)` to prevent JavaScript access
8. **Size limits**: 4KB per cookie, ~20-50 cookies per domain
9. **Path scope**: Cookie sent only to matching path and subdirectories
10. **Common use cases**: Remember me, visit counter, preferences, theme

**Sample Exam Questions:**

- Write code to create and read a cookie
- Implement a visit counter using cookies
- Delete a specific cookie
- Create a "Remember Me" feature
- Set cookie attributes (maxAge, path, domain, secure)
- Handle missing cookies (null check)
- Store and retrieve user preferences
- Explain difference between session and persistent cookies

### Further Reading

Refer to your prescribed textbook and official course materials.
