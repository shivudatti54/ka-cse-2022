# **JSP Tags, Variables and Objects, Methods, Control Statements, Loops, Request String, Parsing Other Information, User Sessions, Cookies, Session Object**

## **JSP Tags**

JSP tags are used to add dynamic content to a JavaServer Pages (JSP) document. They allow developers to insert data from a Java source file into an HTML document.

### Example of JSP tag:

```jsp
<html>
  <body>
    <h1><%= name %></h1>
  </body>
</html>
```

In this example, `name` is a variable declared in the Java source file that is being used to display the username in the HTML document.

## **Variables and Objects**

Variables and objects are used to store and manipulate data in a JSP document.

### Example of Variables:

```jsp
<%
  String name = "John Doe";
  int age = 30;
%>

<html>
  <body>
    <h1>Hello, <%= name %>!</h1>
    <p>You are <%= age %> years old.</p>
  </body>
</html>
```

In this example, two variables `name` and `age` are declared and used to display the username and age in the HTML document.

## **Methods**

Methods are used to encapsulate code in a JSP document. They can be used to perform complex operations and to reduce code duplication.

### Example of Methods:

```jsp
<%
  public String getGreeting(String name) {
    return "Hello, " + name + "!";
  }
%>

<html>
  <body>
    <h1><%= getGreeting("John") %></h1>
  </body>
</html>
```

In this example, a method `getGreeting` is declared to take a `name` parameter and return a greeting message. The method is then called in the HTML document to display the greeting.

## **Control Statements**

Control statements are used to control the flow of execution in a JSP document. They can be used to handle errors, perform conditional checks, and repeat code.

### Example of Control Statements:

```jsp
<%
  if (age > 18) {
    out.println("You are an adult.");
  } else {
    out.println("You are not an adult.");
  }
%>

<html>
  <body>
    <p>Are you an adult? <%= (age > 18) ? "Yes" : "No" %></p>
  </body>
</html>
```

In this example, an `if` statement is used to check if the user is an adult based on their age. The result is then displayed in the HTML document.

## **Loops**

Loops are used to repeat code in a JSP document. They can be used to iterate over collections of data and to perform repetitive tasks.

### Example of Loops:

```jsp
<%
  for (int i = 0; i < 5; i++) {
    out.println("Iteration " + (i + 1));
  }
%>

<html>
  <body>
    <p>Repeating the loop 5 times:</p>
    <ul>
    <% for (int i = 0; i < 5; i++) { %>
    <li>Iteration <%= (i + 1) %></li>
    <% } %>
    </ul>
  </body>
</html>
```

In this example, a `for` loop is used to repeat a block of code 5 times. The loop is also used in a nested `for` loop to display a list of iterations.

## **Request String**

The request string is a string that contains the data sent by the client in an HTTP request. It can be accessed using the `request` object.

### Example of Request String:

```jsp
<%
  String message = request.getParameter("message");
  out.println(message);
%>

<html>
  <body>
    <form action="" method="get">
      <input type="text" name="message">
      <input type="submit" value="Submit">
    </form>
    <p>Message: <%= message %></p>
  </body>
</html>
```

In this example, a form is used to send a message to the server. The message is then accessed using the `request` object and displayed in the HTML document.

## **Parsing Other Information**

JSP documents can be used to parse other information such as query strings, cookies, and session attributes.

### Example of Parsing Query Strings:

```jsp
<%
  String query = request.getParameter("query");
  out.println(query);
%>

<html>
  <body>
    <form action="" method="get">
      <input type="text" name="query">
      <input type="submit" value="Submit">
    </form>
    <p>Query: <%= query %></p>
  </body>
</html>
```

In this example, a form is used to send a query string to the server. The query string is then accessed using the `request` object and displayed in the HTML document.

## **User Sessions**

User sessions are used to store data about a user's interactions with a web application. They can be used to track user activity and to personalize the user experience.

### Example of User Sessions:

```jsp
<%
  HttpSession session = request.getSession();
  String username = session.getAttribute("username");
  out.println(username);
%>

<html>
  <body>
    <form action="" method="post">
      <input type="text" name="username">
      <input type="submit" value="Submit">
    </form>
    <p>Username: <%= username %></p>
  </body>
</html>
```

In this example, a form is used to send a username to the server. The username is then stored in the user's session and displayed in the HTML document.

## **Cookies**

Cookies are used to store small amounts of data on a user's browser. They can be used to track user activity and to personalize the user experience.

### Example of Cookies:

```jsp
<%
  Cookie cookie = request.getCookie("username");
  out.println(cookie.getValue());
%>

<html>
  <body>
    <form action="" method="post">
      <input type="text" name="username">
      <input type="submit" value="Submit">
    </form>
    <p>Username: <%= cookie.getValue() %></p>
  </body>
</html>
```

In this example, a form is used to send a username to the server. The username is then stored in a cookie and displayed in the HTML document.

## **Session Object**

The session object is a Java object that represents a user's session. It can be used to store data about a user's interactions with a web application.

### Example of Session Object:

```jsp
<%
  HttpSession session = request.getSession();
  session.put("username", "John Doe");
  out.println(session.getAttribute("username"));
%>

<html>
  <body>
    <p>Username: <%= session.getAttribute("username") %></p>
  </body>
</html>
```

In this example, a username is stored in the user's session and displayed in the HTML document.
