# **JSP Tags, Variables and Objects, Methods, Control Statements, Loops, Request String, Parsing, User Sessions, Cookies, Session Object**

## **JSP Tags**

- JSP tags: used to create dynamic web pages
- Types:
  - Expression Language (EL): ${expression}
  - Syntax tags: <tag> content </tag>
  - Expression tags: <%@ page %> directives
- Example: `<h1>${title}</h1>`

## **Variables and Objects**

- Variables: declared using `String`, `int`, `double`, etc.
- Objects: instances of classes, e.g. `Person person = new Person();`
- Scope:
  - Page scope: accessible throughout the page
  - Request scope: accessible throughout the request
  - Session scope: accessible throughout the session
  - Application scope: accessible throughout the application

## **Methods**

- Methods: used to perform actions on variables and objects
- Example: `public String greet() { return "Hello, World!"; }`

## **Control Statements**

- Conditional statements:
  - `if` statements
  - `switch` statements
- Loops:
  - `for` loops
  - `while` loops
  - `do-while` loops

## **Request String**

- Request string: a string representation of the request
- Example: `${requestScope.myVariable}`

## **Parsing**

- Parsing: using regular expressions to extract data from strings
- Example: `String regex = "\\d+"; String match = regex.matcher(request.getParameter("myParameter")).find();`

## **User Sessions**

- User sessions: used to store user-specific data
- Example: `HttpSession session = request.getSession();`

## **Cookies**

- Cookies: used to store small amounts of data
- Example: `Cookie cookie = new Cookie("myCookie", "myValue"); response.addCookie(cookie);`

## **Session Object**

- Session object: a Java object that represents the user's session
- Example: `HttpSession session = request.getSession(); SessionObject obj = session.getObject("myObject");`

## **Important Formulas, Definitions, Theorems**

- None (this is a programming summary)

## **Revision Tips**

- Practice using JSP tags and syntax
- Understand the different scopes of variables and objects
- Learn to use control statements, loops, and parsing techniques
- Understand how to work with user sessions, cookies, and the session object
