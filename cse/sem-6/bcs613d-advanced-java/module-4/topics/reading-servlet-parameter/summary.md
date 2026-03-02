# Reading Servlet Parameter

### Overview

- A servlet can access request parameters using the `HttpServletRequest` object.
- Parameters can be accessed using the `getParameter()` method.

### Key Points

- `HttpServletRequest` object has a `getParameter()` method to access request parameters.
- `getParameter()` method takes a string parameter representing the parameter name.
- Returns the value of the parameter as a `String` object.
- Can access request parameters using `getParameterMap()` method.
- Can access request parameters using `getParameterNames()` method.
- Can access request parameters using `request.getParameterMap()` method.
- Can access request parameters using `request.getParameterNames()` method.

### Important Formulas/Definitions/Theorems

- No specific formulas or definitions relevant to reading servlet parameters.
- Theorem: A servlet can access request parameters using the `HttpServletRequest` object.

### Example Code

```java
import javax.servlet.http.HttpServletRequest;

public class ServletExample {
    public void doGet(HttpServletRequest request, HttpServletResponse response) {
        String paramName = "parameterName";
        String paramValue = request.getParameter(paramName);
        System.out.println("Parameter: " + paramName + " = " + paramValue);
    }
}
```

### Revision Notes

- `getParameter()` method is used to access request parameters.
- `getParameterMap()` and `getParameterNames()` methods are used to access request parameters in a different way.
- The `HttpServletRequest` object is used to access request parameters.
- The `getParameter()` method returns a `String` object representing the parameter value.
