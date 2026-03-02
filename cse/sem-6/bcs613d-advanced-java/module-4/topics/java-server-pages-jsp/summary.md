# Java Server Pages (JSP) - Summary

## Key Definitions and Concepts

- **JSP**: Server-side technology to create dynamic web content by embedding Java in HTML
- **JSP Lifecycle**: Translation → Compilation → Instantiation → Execution → Destruction
- **JSP Elements**:
  - **Scriptlets**: `<% Java code %>` for embedding logic
  - **Declarations**: `<%! variable/method %>` for class-level members
  - **Expressions**: `<%= expression %>` to output values
  - **Directives**: `<%@ page/import/include %>` for page configuration
- **Implicit Objects**: Predefined variables like `request`, `response`, `session`, `out`
- **JSTL**: JSP Standard Tag Library for common tasks (loops, conditionals)

## Important Syntax and Directives

```jsp
<%-- Declaration --%>
<%! int counter = 0; %>

<%-- Scriptlet --%>
<% String user = request.getParameter("user"); %>

<%-- Expression --%>
Current time: <%= new java.util.Date() %>

<%-- Page Directive --%>
<%@ page import="java.util.ArrayList" %>

<%-- Include Directive --%>
<%@ include file="header.html" %>

<%-- JSTL Core Tag --%>
<c:forEach items="${users}" var="u">
```

## Key Points

1. JSP pages are compiled into servlets by the web container
2. Three main lifecycle phases: `jspInit()`, `_jspService()`, `jspDestroy()`
3. 9 implicit objects: `request`, `response`, `out`, `session`, `application`, `config`, `pageContext`, `page`, `exception`
4. JSP supports three types of tags: Scripting, Directive, Action
5. Expression Language (EL) simplifies data access: `${user.name}`
6. Use JSTL to avoid scriptlets and separate logic from presentation
7. JSP acts as the View component in MVC architecture
8. `page` directive defines attributes like contentType and errorPage
9. Session tracking can be implemented using `session` object or cookies
10. JSP comments: `<%-- comment --%>` (not visible in client-side HTML)

## Common Mistakes to Avoid

1. Mixing business logic in JSP (should use servlets/JavaBeans instead)
2. Forgetting to close tags: `<% %>` instead of `<% %>`
3. Using scriptlets instead of EL/JSTL, leading to unmaintainable code
4. Not handling session timeouts in JSP pages using `session.setMaxInactiveInterval()`

## Revision Tips

1. Practice writing JSP pages with all 3 element types (declaration, scriptlet, expression)
2. Memorize the JSP lifecycle phases and their equivalent servlet methods
3. Create a cheat sheet of JSTL core tags: `<c:if>`, `<c:forEach>`, `<c:choose>`
4. Understand the difference between:
   - `<%@ include %>` (compile-time) vs `<jsp:include>` (runtime)
   - `pageContext` vs `session` vs `application` scopes
