# Using Cookies

## Overview

Cookies are small pieces of data stored on the client browser and sent with each HTTP request to maintain state across multiple requests. Servlets use the Cookie class to create, send, and retrieve cookies for implementing session tracking, user preferences, and personalization features.

## Key Points

- **Cookie Class**: javax.servlet.http.Cookie for creating cookies
- **Constructor**: new Cookie(String name, String value)
- **response.addCookie()**: Send cookie to client browser
- **request.getCookies()**: Retrieve all cookies from client request
- **setMaxAge()**: Set cookie expiration time in seconds
- **setValue()**: Change cookie value
- **getName() and getValue()**: Retrieve cookie name and value
- **setPath()**: Specify URL path where cookie is valid
- **Session vs Persistent**: Session cookies deleted when browser closes, persistent have expiration

## Important Concepts

- Cookies stored on client side, sent with each request
- Maximum size typically 4KB per cookie
- Limited number of cookies per domain
- Use for session tracking, preferences, shopping cart
- Security considerations: can be disabled, modified by user

## Notes

- Remember cookies sent from server to client, then back with each request
- For exams, know how to create cookie, set properties, and add to response
- Understand setMaxAge(-1) creates session cookie, positive value creates persistent
