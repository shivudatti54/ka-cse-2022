# Safe Program Coding - Summary

## Key Definitions and Concepts

- **Secure Coding**: Writing programs that resist security vulnerabilities through defensive programming techniques
- **OWASP Top 10**: Standard documentation of the most critical web application security risks
- **Input Validation**: Checking that data conforms to expected formats before processing
- **Input Sanitization**: Removing or encoding dangerous characters from user input
- **Parameterized Queries**: Database queries where user data is passed as parameters, not concatenated
- **Defense in Depth**: Multiple layers of security controls protecting a system
- **Least Privilege**: Running code with minimum necessary permissions
- **XSS (Cross-Site Scripting)**: Injecting malicious scripts into web pages viewed by other users

## Important Formulas and Techniques

- **Password Hashing**: Use bcrypt.hashpw() with gensalt() for hashing, bcrypt.checkpw() for verification
- **HTML Encoding**: html.escape() in Python converts special characters to safe HTML entities
- **SQL Parameters**: Use ? placeholders with tuple parameters in execute() statements
- **Secure Session ID**: Use secrets.token_urlsafe(32) for cryptographically random session identifiers

## Key Points

- Never trust user input — always validate and sanitize on the server side
- Use parameterized queries exclusively to prevent SQL injection
- Hash passwords with bcrypt or Argon2, never use MD5 or SHA-256 directly
- Apply output encoding based on context (HTML, URL, JavaScript)
- Implement proper session management with secure, HttpOnly cookies
- Follow least privilege — code should only have necessary permissions
- Keep all dependencies and libraries updated to patch known vulnerabilities
- Log security events without exposing sensitive data in logs
- Use prepared statements for all database operations
- Validate file uploads carefully — check type, size, and content

## Common Mistakes to Avoid

- Using string concatenation or f-strings for SQL queries
- Storing passwords with fast hashing algorithms (MD5, SHA-256)
- Relying solely on client-side validation for security
- Displaying raw user input without encoding
- Using predictable session identifiers
- Storing sensitive data in URLs or logs
- Trusting third-party components without verification

## Revision Tips

1. Remember the mantra: "Filter input, escape output" for most vulnerabilities
2. Understand that client-side validation is for UX, server-side is for security
3. Practice identifying vulnerable code and writing secure alternatives
4. Memorize why parameterized queries prevent SQL injection
5. Review OWASP Top 10 categories and know at least one example of each