# Simple Servlet

### Overview

- A Simple Servlet is a server-side Java program that extends the HTTP protocol to create dynamic web applications.
- It is a Java class that implements the `Servlet` interface and is typically deployed on a web server.

### Key Concepts

- **Servlet Life Cycle**: The sequence of events that occur when a servlet is deployed and accessed by a web browser.
  - 1.  `INIT`: Initialization phase
  - 2.  ` service`: Service phase
  - 3.  `DESTROY`: Destruction phase
- **Request and Response**: The servlet processes HTTP requests and generates HTTP responses.
- **Servlet Mapping**: The mapping of a servlet to a specific URL or context path.

### Important Terms

- **Servlet Container**: The software that hosts and manages servlets, such as Tomcat.
- **Context Path**: The prefix of the URL that identifies the servlet.
- **Servlet Class**: The Java class that implements the `Servlet` interface.

### Key Formulas and Definitions

- **HTTP Request Method**: The method used to access a servlet, such as `GET`, `POST`, `PUT`, etc.
- **HTTP Status Code**: A three-digit code that indicates the outcome of an HTTP request.
  - 200 (OK)
  - 404 (Not Found)
  - 500 (Internal Server Error)

### Theorems and Principles

- **Separation of Concerns**: The principle of separating the presentation layer from the business logic layer.
- **Single Responsibility Principle**: The principle of assigning a single responsibility to a servlet.

### Revision Tips

- Understand the servlet life cycle and its phases.
- Know how to handle HTTP requests and responses.
- Familiarize yourself with servlet mapping and context paths.
- Review important terms and definitions.
