# Control Statements - Summary

## Key Definitions and Concepts

- **Scriptlets**: `<% ... %>` blocks embedding Java code in JSP pages for dynamic content.
- **Directives**: `<%@ page %>`, `<%@ include %>`, `<%@ taglib %>` control JSP page behavior.
- **Implicit Objects**: Predefined variables like `request`, `response`, `session`, and `out`.
- **JSTL**: Jakarta Standard Tag Library using `<c:if>`, `<c:forEach>` for control flow without Java code.
- **Cookies**: Client-side storage managed via `response.addCookie()` and `request.getCookies()`.

## Important Formulas and Theorems

- **If-else in Scriptlet**:
  ```jsp
  <% if(user != null) { %>
    <p>Welcome <%= user %></p>
  <% } else { %>
    <p>Guest User</p>
  <% } %>
  ```
- **JSTL Loop**:
  ```jsp
  <c:forEach var="i" begin="1" end="5">
    Item ${i}<br>
  </c:forEach>
  ```
- **Parameter Reading**:
  ```java
  String username = request.getParameter("uname");
  ```
- **Cookie Creation**:
  ```java
  Cookie c = new Cookie("theme", "dark");
  response.addCookie(c);
  ```

## Key Points

1. JSP scriptlets (`<% %>`) execute Java code during page rendering.
2. Use `if-else`/`switch` in scriptlets for conditional HTML rendering.
3. `<%@ page import="..." %>` directive imports Java classes for use in JSP.
4. Nine implicit objects (e.g., `application`, `config`) simplify web development tasks.
5. JSTL requires `<%@ taglib uri="..." prefix="c" %>` declaration.
6. Always URL-encode cookies with `URLEncoder.encode()` for special characters.
7. `do-while` loops in scriptlets ensure at least one iteration.

## Common Mistakes to Avoid

- Forgetting to close scriptlet blocks (`%>`) causing compilation errors.
- Using `==` for string comparison instead of `.equals()` in scriptlets.
- Not initializing variables before use in JSP declarations (`<%! %>`).
- Missing `break` statements in `switch` blocks (fall-through errors).

## Revision Tips

1. Practice writing JSP pages with nested `if-else` and `for` loops.
2. Memorize the syntax for all three JSP directives (`page`, `include`, `taglib`).
3. Create a cheat sheet for implicit objects and their methods (e.g., `request.getParameter()`).
4. Convert scriptlet-based code to JSTL equivalents to understand modern best practices.
