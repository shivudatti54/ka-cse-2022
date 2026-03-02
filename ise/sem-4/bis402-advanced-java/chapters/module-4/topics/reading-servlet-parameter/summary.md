# Reading Servlet Parameter

**Definition:** Servlet parameter is a key-value pair that can be accessed and used by a servlet during its execution.

**Key Points:**

- Servlet parameter is stored in the `request` object of the servlet.
- Parameters can be passed to the servlet through HTTP GET or POST methods.
- Parameters can be accessed using `request.getParameter()` method.
- Parameters can be a string, integer, boolean, or other data types.
- `getParameter()` method returns `null` if the parameter is not found.

**Important Formulas and Definitions:**

- **HTTP GET and POST Methods:** HTTP GET method is used to retrieve data from the client, while HTTP POST method is used to send data to the server.
- **Servlet Request Object:** The `request` object is an instance of `HttpServletRequest` that provides access to servlet parameters, headers, and other information.

**Theorems:**

- **The Servlet Request Object is thread-safe**: The `request` object is shared among all threads that execute the servlet.
- **The Servlet Response Object is thread-safe**: The `response` object is shared among all threads that execute the servlet.

**Key Servlet Methods:**

- `request.getParameter(String param-name)`: Returns the value of the servlet parameter with the specified name.

**Revision Tips:**

- Practice accessing servlet parameters using the `request.getParameter()` method.
- Understand the difference between HTTP GET and POST methods.
- Review the `HttpServletRequest` interface and its methods.
