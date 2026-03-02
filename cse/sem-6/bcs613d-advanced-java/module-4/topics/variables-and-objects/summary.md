# Variables and Objects in JSP - Summary

## Key Definitions and Concepts

- **JSP Variables**: Storage locations declared using `<%! %>` (class-level) or `<% %>` (method-local) tags
- **Implicit Objects**: Predefined objects like `request`, `response`, `session`, `out`, and `application`
- **Object Scopes**:
  - **Page**: Exists only within current page (`pageContext`)
  - **Request**: Available until response is sent (`request`)
  - **Session**: Persists across multiple requests from same user (`session`)
  - **Application**: Shared across all users (`application`)

## Important Formulas and Theorems

```jsp
<%! int counter = 0; %>          // Class-level variable declaration
<%= request.getParameter("id") %> // Access request parameter
<% session.setAttribute("user", name); %> // Session object usage
Cookie c = new Cookie("key","value");
response.addCookie(c);          // Cookie creation
```

## Key Points

1. Use **declaration tags** (`<%! %>`) for member variables, **scriptlets** (`<% %>`) for local variables
2. Four object scopes determine variable lifetime: page < request < session < application
3. Critical implicit objects:
   - `request`: Access HTTP request data (`getParameter()`, `getHeader()`)
   - `response`: Control HTTP response (`sendRedirect()`, `addCookie()`)
   - `session`: Maintain user state across requests (`setAttribute()`, `getAttribute()`)
   - `application`: Store global data (`getServletContext()`)
4. Always initialize objects before use to prevent NullPointerExceptions
5. Cookies require both `response.addCookie()` and `request.getCookies()` for setting/retrieving
6. Use `pageContext.findAttribute()` to search variables across scopes
7. JSP **directives** (`<%@ page %>`) affect object behavior like session participation

## Common Mistakes to Avoid

1. Confusing **page-scoped** variables (reset on refresh) with **session-scoped** variables
2. Declaring variables in scriptlets (`<% %>`) instead of declarations (`<%! %>`), causing thread-safety issues
3. Forgetting to call `session.invalidate()` when implementing logout functionality
4. Not setting cookie path with `cookie.setPath("/")`, leading to cookie visibility issues

## Revision Tips

1. Create a **scope matrix table** comparing page/request/session/application lifetimes
2. Practice writing code snippets for:
   - Accessing form parameters
   - Setting session attributes
   - Creating/reading cookies
3. Memorize the **9 implicit JSP objects**: request, response, out, session, application, config, pageContext, page, exception
4. Study common exam questions about:
   - Difference between `response.sendRedirect()` vs `request.getRequestDispatcher()`
   - Cookie vs Session vs URL rewriting comparison
