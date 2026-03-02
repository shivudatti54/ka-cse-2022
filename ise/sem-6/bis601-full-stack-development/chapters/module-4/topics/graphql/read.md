# GraphQL Security Considerations

## 1. Introduction to GraphQL Security

GraphQL is a powerful query language for APIs that provides clients with the ability to request exactly the data they need. However, this power and flexibility introduce unique security challenges that differ from traditional REST APIs. Unlike REST, where endpoints are fixed, a single GraphQL endpoint can be used to fetch vast and complex data structures. This fundamental difference necessitates a shift in security mindset, moving from securing individual endpoints to securing the data graph itself.

**Key Difference from REST:**
In a REST API, a security issue might be limited to a specific endpoint (e.g., `/api/users`). In GraphQL, a vulnerability often affects the entire API because all data is accessible through a single endpoint. A malicious query can potentially access any connected data.

## 2. Common GraphQL Security Vulnerabilities

### 2.1. Injection Attacks

GraphQL is strongly typed, which helps prevent traditional SQL Injection. However, injection risks persist in other forms.

- **SQL Injection:** If a GraphQL resolver directly concatenates user-supplied arguments into a SQL query without parameterization, it is vulnerable.
  - **Example Vulnerable Resolver (Pseudocode):**
    ```javascript
    resolvers.Query.user = (_, { id }) => {
      return db.query(`SELECT * FROM users WHERE id = ${id}`); // UNSAFE!
    };
    ```
  - **Mitigation:** Always use parameterized queries or an ORM that handles sanitization.

- **NoSQL Injection:** If using a NoSQL database like MongoDB, similar injection attacks are possible if user input is passed directly into queries like `find({ "username": input })`.
- **LDAP Injection & Command Injection:** Arguments used in LDAP queries or system commands must be rigorously sanitized.

### 2.2. Authorization and Access Control

This is one of the most critical and common pitfalls in GraphQL.

- **Problem:** GraphQL defines a **schema**, not **authorization rules**. The schema declares what data _exists_, not who can _access_ it. Authorization checks must be implemented manually in the resolvers.
- **Broken Object Level Authorization (BOLA):** A user can access an object they are not authorized for by simply guessing or enumerating its ID.
  - **Example:** A query for `{ user(id: "123") { email } }` might return another user's data if the resolver doesn't check if the authenticated user is authorized to see user 123.
- **Mitigation:** Implement authorization checks in every resolver that fetches a single object by ID. Never assume the client will only request data they are allowed to see.

### 2.3. Denial of Service (DoS) via Malicious Queries

The flexibility of GraphQL allows clients to craft very deep, nested, and complex queries that can overwhelm the server.

- **Alias Abuse:** A client can request the same field hundreds of times with different aliases, forcing the server to execute the same expensive operation repeatedly.
  ```graphql
  query {
    alias1: expensiveField
    alias2: expensiveField
    alias3: expensiveField
    ... # Repeat 1000 times
  }
  ```
- **Deep Nesting:** Exploiting relationships in the schema to create a very deep query that causes recursive database calls or high memory usage.
  ```graphql
  query {
    posts {
      author {
        posts {
          author {
            posts { ... } # Very deep nesting
          }
        }
      }
    }
  }
  ```
- **Batch Queries:** Sending multiple queries in a single request to amplify the load.

### 2.4. Information Disclosure

GraphQL can inadvertently leak information about the schema and data structure.

- **Introspection:** GraphQL's introspection feature allows any client to query the complete schema, including all types, queries, and mutations. This is useful for development but dangerous in production as it provides a blueprint for attackers.
- **Error Handling:** Verbose error messages might reveal stack traces, database structure, or other sensitive information.

## 3. Security Mitigation Strategies and Best Practices

### 3.1. Implement Robust Authorization

A "defense in depth" approach is required.

- **Resolver-Level Authorization:** Perform access control checks within each resolver. This is the most granular and common place to implement it.
  ```javascript
  resolvers.Query.user = async (_, { id }, context) => {
    const requestedUser = await User.findById(id);
    if (context.currentUser.id !== requestedUser.id) {
      throw new ForbiddenError('Access denied');
    }
    return requestedUser;
  };
  ```
- **Layer-Based Authorization:** Use a middleware-style approach before the request even reaches the resolvers (e.g., using GraphQL middleware libraries). This is good for coarse-grained checks.

### 3.2. Prevent DoS Attacks

Protect your server from being overwhelmed by expensive queries.

- **Query Depth Limiting:** Reject queries that exceed a specified depth.

  ```
  Allowed: depth 4
  query { user { posts { comments { author } } } }

  Rejected: depth 6
  query { a { b { c { d { e { f } } } } } }
  ```

- **Query Complexity Analysis:** Assign a cost to each field and reject queries that exceed a total cost threshold. For example, a field that performs a database call has a higher cost than a simple scalar field.
- **Rate Limiting:** More complex than REST. Instead of limiting by endpoint, you must limit by the complexity of the query or by the client's IP/identity. **Calculated Rate Limiting** is often used, where a client is granted a points budget per time window, and each query costs points based on its complexity.
- **Persisted Queries:** Allow the server to pre-define allowed queries. Clients can only execute these pre-approved queries by sending a hash of the query, not the full text. This completely prevents malicious queries.

### 3.3. Sanitize Input and Manage Introspection

- **Input Validation:** Validate all arguments using the built-in GraphQL type system (e.g., `Int`, `String`) and consider additional libraries like `validator` for more complex validation (e.g., email format).
- **Disable Introspection in Production:** Turn off the introspection feature in your production environment to prevent attackers from easily discovering your schema. This is often a simple configuration flag in GraphQL server libraries.
- **Secure Error Handling:** Ensure that in production, GraphQL errors are sanitized. Return generic error messages to the client while logging detailed errors internally for debugging.

### 3.4. Secure the GraphQL Endpoint

- **Avoid Automatic `GET` requests:** GraphQL queries can be sent via HTTP GET (by putting the query in the URL parameters). This can lead to security issues like URLs being logged. It's often safer to only allow POST requests for GraphQL operations.
- **CSRF Protection:** If using cookies for authentication, protect your GraphQL endpoint from Cross-Site Request Forgery attacks, as browsers can automatically include cookies in POST requests. Use CSRF tokens or ensure authentication is done via a header (like `Authorization: Bearer <token>`) that is not automatically sent by browsers.

## 4. Comparison: REST vs. GraphQL Security

| Security Aspect            | REST API                                           | GraphQL API                                                                          |
| :------------------------- | :------------------------------------------------- | :----------------------------------------------------------------------------------- |
| **Attack Surface**         | Multiple endpoints. Vulnerability may be isolated. | Single endpoint. A vulnerability often affects the entire API.                       |
| **DoS Protection**         | Simpler; can rate limit per endpoint.              | Complex; requires depth limiting, complexity analysis, and calculated rate limiting. |
| **Authorization**          | Handled at the endpoint/controller level.          | Must be handled at the individual resolver level for granularity.                    |
| **Information Disclosure** | Limited to the endpoint's documented data.         | Introspection can reveal the entire schema. Errors can be more verbose.              |
| **Caching**                | Easy to implement at the HTTP level (e.g., CDN).   | Difficult; responses are highly dynamic. Often requires persisted queries or APQ.    |

## 5. Diagram: GraphQL Request Flow with Security Checkpoints

```
+-------------------+     +-------------------------+     +-----------------+
|   Client Request  | --> |   GraphQL Server        | --> |   Resolvers     |
| (Query/Mutation)  |     | (Query Processing Layer)|     | (Data Fetching) |
+-------------------+     +-------------------------+     +-----------------+
                             |           |           |            |
                             v           v           v            v
+-----------------------------------------------------------------------------+
|                      SECURITY CHECKPOINTS                                   |
|                                                                             |
| 1. Input Validation & Sanitization                                         |
| 2. Authentication Middleware (Verify JWT, etc.)                           |
| 3. Query Depth & Complexity Analysis (Block malicious queries)             |
| 4. Rate Limiting (Check client's query budget)                             |
| 5. Authorization Checks (In middleware AND/OR individual resolvers)        |
| 6. Secure Error Handling (Sanitize errors before sending response)          |
+-----------------------------------------------------------------------------+
```

## 6. Exam Tips

- **Focus on Authorization:** Remember that GraphQL does **not** handle authorization by itself. You must implement checks in resolvers. This is a very common exam topic.
- **Understand DoS Vectors:** Be prepared to explain how a deeply nested query or alias abuse can cause a DoS attack and how to prevent it (depth limiting, complexity analysis).
- **Introspection is a Double-Edged Sword:** Know that introspection is on by default and why it should be disabled in production to avoid information disclosure.
- **Compare and Contrast:** Be able to clearly articulate the key security differences between GraphQL and REST APIs, especially regarding the attack surface and rate limiting strategies.
- **Think Beyond SQL Injection:** While SQL Injection is a risk, GraphQL's strong typing pushes attackers towards other avenues like DoS and BOLA. Your answers should reflect this broader perspective.
