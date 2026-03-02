# Reading Servlet Parameters

### Introduction

In Java Servlets, parameters are used to pass data between the client and the server. Servlet parameters are used in the URL to pass data from the client to the server. In this topic, we will learn how to read servlet parameters from the URL.

### What are Servlet Parameters?

- Servlet parameters are used to pass data between the client and the server.
- They are used in the URL to pass data from the client to the server.
- Servlet parameters are also known as query parameters or URL parameters.

### Request Object and Parameters

The request object contains the servlet parameters. The request object has a method called `getParameter()` which is used to get the value of a servlet parameter.

### How to Read Servlet Parameters

To read servlet parameters, you need to create an instance of the `HttpServletRequest` object. The `HttpServletRequest` object has a method called `getParameter()` which is used to get the value of a servlet parameter.

Here is an example of how to read servlet parameters:

```java
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class ReadServletParameters extends HttpServlet {
 @Override
 protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 String name = req.getParameter("name");
 String age = req.getParameter("age");

 System.out.println("Name: " + name);
 System.out.println("Age: " + age);
 }
}
```

In the above example, we are reading two servlet parameters `name` and `age` from the URL.

### Key Concepts

- **HttpServletRequest**: The request object that contains the servlet parameters.
- **getParameter()**: The method of the request object that is used to get the value of a servlet parameter.
- **URL**: The URL contains the servlet parameters.
- **Query Parameters**: The servlet parameters are also known as query parameters or URL parameters.

### Handling Multiple Parameters

If you need to handle multiple parameters, you can use a loop to iterate over the parameters.

Here is an example of how to handle multiple parameters:

```java
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class ReadServletParameters extends HttpServlet {
 @Override
 protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 String name = req.getParameter("name");
 String age = req.getParameter("age");

 if (name != null && age != null) {
 System.out.println("Name: " + name);
 System.out.println("Age: " + age);
 } else {
 System.out.println("Name and Age are not provided.");
 }
 }
}
```

In the above example, we are checking if both `name` and `age` parameters are provided before printing their values.

### Handling Parameters with Different Data Types

Servlet parameters can have different data types such as string, integer, boolean, etc.

Here is an example of how to handle parameters with different data types:

```java
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class ReadServletParameters extends HttpServlet {
 @Override
 protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
 String name = req.getParameter("name");
 int age = Integer.parseInt(req.getParameter("age"));
 boolean isAdmin = req.getParameter("isAdmin").equals("true");

 System.out.println("Name: " + name);
 System.out.println("Age: " + age);
 System.out.println("Is Admin: " + isAdmin);
 }
}
```

In the above example, we are parsing the `age` parameter to an integer and checking the `isAdmin` parameter to a boolean value.
