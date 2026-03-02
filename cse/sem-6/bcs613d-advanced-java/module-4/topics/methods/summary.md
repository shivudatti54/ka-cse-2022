# Servlet and JSP Methods - Summary

## Key Definitions and Concepts

- **Servlet Lifecycle Methods**: `init()`, `service()`, `destroy()` - control creation, request handling, and destruction of servlets
- **HTTP Handler Methods**: `doGet()`, `doPost()`, `doPut()`, `doDelete()` - process specific HTTP request types
- **JSP Lifecycle Methods**: `jspInit()`, `_jspService()`, `jspDestroy()` - equivalent to servlet methods in JSP
- **Cookies**: Client-side data storage using `HttpServletRequest.getCookies()` and `HttpServletResponse.addCookie()`
- **Servlet Parameters**: Retrieved via `request.getParameter("name")` from HTML forms
- **JSP Tags**: `<% %>` (scriptlets), `<%= %>` (expressions), `<%! %>` (declarations)

## Important Formulas and Theorems

```java
// Servlet initialization
public void init(ServletConfig config) throws ServletException

// HTTP GET handler
protected void doGet(HttpServletRequest req, HttpServletResponse res)
    throws ServletException, IOException

// Cookie creation
Cookie cookie = new Cookie("key", "value");
response.addCookie(cookie);

// JSP declaration tag
<%! int counter = 0; %>

// Parameter retrieval
String username = request.getParameter("username");
```

## Key Points

1. Servlets follow **three-phase lifecycle**: initialization → service → destruction
2. `service()` method automatically routes requests to appropriate `doXxx()` methods
3. **GET vs POST**:
   - GET: Parameters visible in URL (bookmarks allowed)
   - POST: Secure parameter transfer (no URL exposure)
4. Always override `doGet()`/`doPost()` instead of `service()` unless creating custom request handling
5. **JSP translation**: Converted to servlet (`.java` file) during first request
6. Cookies require **both response.addCookie() and request.getCookies()** for data persistence
7. Use **JSTL tags** (`<c:out>`, `<c:if>`) instead of scriptlets for cleaner JSP code

## Common Mistakes to Avoid

1. **Overriding service() without super.service()**: Causes doGet()/doPost() to stop working

   ```java
   // Wrong
   protected void service(...) { /* custom code */ }

   // Correct
   protected void service(...) {
       super.service(...);
       /* custom code */
   }
   ```

2. **Confusing GET/POST**: Using GET for sensitive data or POST for bookmarkable pages
3. **Null handling in parameters**: Not checking `request.getParameter()` for null values
4. **JSP scriptlet overuse**: Leads to unmaintainable code (use JSTL/EL instead)

## Revision Tips

1. **Practice method signatures**: Write 5 servlet skeletons with different HTTP methods
2. **Use flashcards** for lifecycle phases:
   - Init: `init()`, one-time setup
   - Service: `service()` → `doXxx()`, handles requests
   - Destroy: `destroy()`, cleanup
3. **Create comparison tables**:
   | Servlet Method | JSP Equivalent |
   |----------------|-------------------|
   | init() | jspInit() |
   | service() | \_jspService() |
   | destroy() | jspDestroy() |
4. **Write cookie workflow**: Diagram request → cookie creation → response → subsequent requests
