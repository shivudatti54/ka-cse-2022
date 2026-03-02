# The Life Cycle Of A Servlet

## Introduction

The servlet lifecycle defines the complete sequence of events from the moment a servlet is first loaded into memory until its destruction. Understanding this lifecycle is fundamental to developing robust and efficient Java web applications. The servlet container (such as Apache Tomcat) manages this lifecycle automatically, invoking specific methods at appropriate times that allow developers to initialize resources, process client requests, and clean up before the servlet is removed from service.

The lifecycle of a servlet is controlled by the servlet container, which follows the Jakarta Servlet specification (formerly Java Servlet API). When a servlet is first requested, the container performs three essential operations: loading the servlet class, creating an instance of the servlet, and initializing the servlet by calling its init() method. Throughout the servlet's lifetime, the service() method is called for each client request, and when the servlet is taken out of service, the destroy() method is invoked to perform cleanup operations.

This lifecycle mechanism provides a structured approach to managing web application resources, ensuring that expensive operations like database connections are established once during initialization and released appropriately during destruction. The lifecycle also supports the single-thread model (though deprecated) and load-on-startup features that allow servlets to be initialized when the container starts rather than on first request.

## Key Concepts

### Phase 1: Loading and Instantiation

The servlet container loads the servlet class into memory and creates an servlet instance using the Class.forName() method and the newInstance() method. This occurs either when the container starts (if load-on-startup is configured) or when the first request for that servlet is received. The servlet class must have a no-arg constructor, which the container uses to instantiate the object. Multiple servlets can be instantiated if needed, though typically one instance handles all requests.

### Phase 2: Initialization (init method)

Once instantiated, the container calls the init() method exactly once during the servlet's lifecycle. This method receives a ServletConfig object that contains initialization parameters and a reference to the ServletContext. The init() method should be used to perform one-time initialization operations such as opening database connections, reading configuration files, or establishing resource pools. If initialization fails, the servlet throws an UnavailableException or ServletException, and the servlet will not handle requests.

```java
@Override
public void init(ServletConfig config) throws ServletException {
 super.init(config); // Always call super.init(config)
 String dbURL = getInitParameter("dbURL");
 // Initialize database connection, read configuration, etc.
}
```

### Phase 3: Request Handling (service method)

For each client request, the container calls the service() method, which is the heart of the servlet. The service() method determines the type of HTTP request (GET, POST, PUT, DELETE, etc.) and dispatches the request to the appropriate handler method (doGet(), doPost(), doPut(), doDelete(), etc.). Importantly, the service() method runs in a separate thread for each request, meaning instance variables are shared among concurrent requests, requiring careful synchronization for thread safety.

### Phase 4: Destruction (destroy method)

When the servlet container decides to remove the servlet (such as when the server is shut down or the web application is undeployed), it calls the destroy() method exactly once. This method allows the servlet to release resources such as database connections, close file handles, and save any state that needs persistence. After destroy() is called, the servlet will not handle any new requests. Any pending requests may or may not complete, depending on the container implementation.

```java
@Override
public void destroy() {
 // Close database connections
 // Release resources
 // Log shutdown
}
```

### ServletConfig and ServletContext

**ServletConfig** is unique to each servlet and contains initialization parameters specific to that servlet, defined in the deployment descriptor (web.xml). It provides the getInitParameter() and getServletContext() methods. **ServletContext** represents the web application as a whole and is shared among all servlets within the application. It provides application-wide configuration and allows servlets to communicate with the container.

### Load-On-Startup

The load-on-startup element in web.xml (or @WebServlet annotation) specifies that a servlet should be loaded when the container starts rather than on first request. This is specified as an integer value where lower values indicate higher priority (1 loads before 5). This feature is essential for servlets that perform critical initialization or need to be available immediately.

## Examples

### Example 1: Tracing the Servlet Lifecycle

Consider a servlet that logs each lifecycle method call:

```java
public class LifecycleServlet extends HttpServlet {
 public LifecycleServlet() {
 System.out.println("Constructor: Servlet instance created");
 }

 @Override
 public void init() throws ServletException {
 System.out.println("init(): Servlet initialized");
 }

 @Override
 protected void service(HttpServletRequest req, HttpServletResponse resp)
 throws ServletException, IOException {
 System.out.println("service(): Handling " + req.getMethod() + " request");
 super.service(req, resp);
 }

 @Override
 protected void doGet(HttpServletRequest req, HttpServletResponse resp)
 throws ServletException, IOException {
 resp.getWriter().write("Servlet is alive!");
 }

 @Override
 public void destroy() {
 System.out.println("destroy(): Servlet being destroyed");
 }
}
```

When deployed with load-on-startup=1, the output on server startup shows: Constructor message followed by init() message. Each HTTP request triggers the service() method, and on server shutdown, destroy() is called.

### Example 2: Resource Management in init() and destroy()

A practical example demonstrating proper resource management:

```java
public class DatabaseServlet extends HttpServlet {
 private Connection connection;

 @Override
 public void init(ServletConfig config) throws ServletException {
 try {
 super.init(config);
 String dbUrl = getInitParameter("databaseURL");
 String dbUser = getInitParameter("dbUser");
 String dbPass = getInitParameter("dbPass");

 DriverManager.registerDriver(new com.mysql.cj.jdbc.Driver());
 connection = DriverManager.getConnection(dbUrl, dbUser, dbPass);
 System.out.println("Database connection established");
 } catch (SQLException e) {
 throw new ServletException("Failed to initialize database", e);
 }
 }

 @Override
 protected void doGet(HttpServletRequest req, HttpServletResponse resp)
 throws ServletException, IOException {
 // Use connection to process requests
 }

 @Override
 public void destroy() {
 try {
 if (connection != null && !connection.isClosed()) {
 connection.close();
 System.out.println("Database connection closed");
 }
 } catch (SQLException e) {
 e.printStackTrace();
 }
 }
}
```

### Example 3: Configuring Load-On-Startup

**Using web.xml:**

```xml
<servlet>
 <servlet-name>InitializationServlet</servlet-name>
 <servlet-class>com.example.InitServlet</servlet-class>
 <load-on-startup>1</load-on-startup>
</servlet>
```

**Using Annotation:**

```java
@WebServlet(urlPatterns = "/init", loadOnStartup = 1)
public class InitializationServlet extends HttpServlet {
 // Servlet code
}
```

A load-on-startup value of 0 or negative means the servlet loads on first request. Values 1-10 indicate startup loading order, with 1 being highest priority.

## Exam Tips

1. **Remember the exact sequence**: Constructor → init() → service() → [repeated for each request] → destroy(). The constructor is not part of the formal lifecycle methods but is the first step.

2. **init() is called exactly once**: Unlike service() which is called for every request, init() is called only once during the servlet's lifecycle. Use it for expensive one-time operations.

3. **Always call super.init(config)**: When overriding init(ServletConfig config), you must call super.init(config) first to ensure the ServletConfig is properly stored for later use via getServletConfig().

4. **Thread safety is crucial**: Instance variables are shared among all requests. Use local variables or implement synchronization for thread-safe operations.

5. **destroy() timing is unpredictable**: You cannot rely on destroy() being called (e.g., if the JVM crashes). Do not use it for critical persistence; save data during normal operation.

6. **service() vs doGet()/doPost()**: The service() method dispatches to appropriate doXxx() methods. Override doGet() or doPost() rather than service() unless you need to handle all HTTP methods.

7. **ServletConfig vs ServletContext**: Remember the distinction—ServletConfig is per-servlet, ServletContext is per-web-application. Both are obtained differently and serve different scopes.
