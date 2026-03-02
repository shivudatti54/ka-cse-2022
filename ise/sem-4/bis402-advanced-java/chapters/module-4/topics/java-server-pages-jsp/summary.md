# **Java Server Pages (JSP) Revision Notes**

### Overview

- Java Server Pages (JSP) is a server-side technology that allows developers to create dynamic web pages.
- JSP is based on the Java Servlet technology and uses Templates to separate presentation logic from business logic.

### Key Features

- **Template-based**: JSP uses a combination of Java code and HTML templates to separate presentation logic from business logic.
- **Server-side scripting**: JSP allows developers to write Java code that interacts with the server and database.
- **Compiled to servlet**: JSP files are compiled to servlets at runtime, which are then executed by the web server.

### JSP Life Cycle

- **Compilation**: JSP file is compiled to servlet code at runtime.
- **Loading**: Compiled servlet is loaded into memory.
- **Initialization**: Servlet is initialized with configuration parameters and resources.
- **Service**: Servlet handles HTTP requests and responses.
- ** Destruction**: Servlet is destroyed when it goes out of scope.

### JSP Directives and Tags

- **%**: Begins a JSP directive or tag.
- **%?=**: Used to import classes or perform other JSP operations.
- **%=${}:**: Used to import variables or perform other JSP operations.
- \*\*%><%`: Used to separate JSP directives or tags.

### JSP Expressions

- **${}`**: Used to display the value of a variable or expression.
- **${!}`**: Used to display the value of a variable or expression without escaping.

### JSP Tags Library

- **c:if**: Used to evaluate a condition and include or exclude content.
- **c:forEach**: Used to iterate over a collection or array.
- **c:choose**: Used to evaluate a condition and include or exclude content.

### Important Formulas, Definitions, and Theorems

- **Page Context**: The context in which a JSP page is executed.
- **Request Object**: An object that represents an HTTP request.
- **Response Object**: An object that represents an HTTP response.
- **Scope**: The lifetime of a variable or object in a JSP page.

Note: This summary is a concise revision guide and is not exhaustive.
