# The Life Cycle Of A Servlet - Summary

## Key Definitions

- **Servlet Lifecycle**: The complete sequence of events from servlet class loading to its destruction, managed by the servlet container
- **ServletConfig**: An object containing initialization parameters specific to a single servlet
- **ServletContext**: An object representing the web application as a whole, shared among all servlets
- **Load-On-Startup**: A configuration that specifies when a servlet should be loaded (at container startup or on first request)
- **Thread Safety**: The property of a servlet ensuring correct behavior when handling multiple concurrent requests

## Important Formulas

- Lifecycle sequence: `Loading → Instantiation → init() → service() → destroy()`
- Service method dispatch: `service() calls doGet()/doPost() based on HTTP method`
- Load-on-startup priority: Lower integer = higher priority (1 loads before 10)

## Key Points

1. The servlet container manages the entire lifecycle automatically, invoking init() once, service() for each request, and destroy() once
2. The init(ServletConfig config) method should call super.init(config) to preserve the configuration object
3. Instance variables in a servlet are NOT thread-safe; they are shared across all concurrent requests
4. ServletConfig provides per-servlet initialization parameters; ServletContext provides application-wide parameters
5. Load-on-startup allows servlets to initialize at container startup rather than on first request (useful for critical resources)
6. The destroy() method may not be called in abnormal shutdown scenarios; avoid relying on it for critical operations
7. The service() method automatically dispatches to appropriate doXxx() methods based on the HTTP request type
8. A servlet can be configured with multiple URL patterns but uses the same single instance
9. Initialization parameters can be set in web.xml or using @WebServlet annotation
10. The ServletContext can be used for inter-servlet communication and sharing application-wide resources

## Common Mistakes

1. **Forgetting to call super.init(config)**: This breaks getServletConfig() functionality throughout the servlet
2. **Using instance variables without synchronization**: Leads to race conditions and data corruption under concurrent requests
3. **Performing expensive operations in doGet/doPost**: These should be done once in init(), not on every request
4. **Confusing ServletConfig and ServletContext**: Using the wrong scope causes parameter retrieval to fail
5. **Not handling initialization failures properly**: Throwing ServletException prevents the servlet from handling requests