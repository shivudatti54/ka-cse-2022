# Revision Notes: Servlets

=====================================

## Text Book 1: Ch 36

---

### Servlet Life Cycle

- Servlet life cycle consists of 6 phases:
  - Initialization
  - Startup
  - Service
  - Destruction
  - Request and Response
  - Idle

### Servlet Context

- Servlet context:
  - Container-provided instance of `ServletContext`
  - Used to share data between servlets
  - Can be accessed through `ServletContext` object

### Servlet Config

- Servlet configuration:
  - Specifies servlet metadata
  - Used to configure servlet behavior
  - Can be specified in `web.xml` file

### Servlet Mapping

- Servlet mapping:
  - Maps servlet URLs to servlet classes
  - Can be specified in `web.xml` file

### Important Servlet Concepts

- **Servlet Filter**: intercepts incoming requests and responses
- **Servlet Listener**: listens for servlet-related events
- **Singleton Pattern**: ensures only one instance of servlet is created

## Text Book 2: Ch 11

---

### Servlet Request and Response Objects

- `HttpServletRequest`:
  - Represents incoming HTTP request
  - Provides access to request parameters and headers
- `HttpServletResponse`:
  - Represents outgoing HTTP response
  - Provides access to response status code and headers

### Request and Response Cycles

- Request cycle:
  - Request is received by servlet
  - Servlet processes request
  - Response is generated
- Response cycle:
  - Response is sent to client

### Important Servlet Request and Response Concepts

- **Request Dispatch**: maps request to servlet
- **Response Writing**: writes response to output stream

### Important Servlet API Methods

- `doGet()`: called when GET request is received
- `doPost()`: called when POST request is received
