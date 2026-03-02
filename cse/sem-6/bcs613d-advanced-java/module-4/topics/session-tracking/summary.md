# Session Tracking

## Overview

Session tracking maintains user state across multiple HTTP requests in stateless HTTP protocol. Servlets support four session tracking techniques: cookies, URL rewriting, hidden form fields, and HttpSession API, enabling personalized user experiences, shopping carts, and authentication persistence.

## Key Points

- **Cookies**: Small data pieces stored on client, sent with each request
- **URL Rewriting**: Append session ID to URLs (jsessionid parameter)
- **Hidden Form Fields**: Embed session data in hidden HTML form inputs
- **HttpSession**: Servlet API providing session object for storing user data
- **session.getAttribute()**: Retrieve session attribute by name
- **session.setAttribute()**: Store attribute in session
- **session.getId()**: Get unique session identifier
- **session.invalidate()**: Destroy session and remove all attributes

## Important Concepts

- HTTP is stateless, session tracking adds state
- HttpSession preferred method (most powerful and convenient)
- Sessions timeout after inactivity period (default 30 minutes)
- URL rewriting works when cookies disabled
- Session stored on server, cookie contains only session ID

## Notes

- Remember four techniques: cookies, URL rewriting, hidden fields, HttpSession
- For exams, know HttpSession methods: getAttribute(), setAttribute(), invalidate()
- Practice implementing login functionality using HttpSession
