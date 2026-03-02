# Safe Program Coding

## Introduction

In today's interconnected digital landscape, the security of software applications has become paramount. Safe program coding, also known as secure coding or defensive coding, refers to the practice of writing computer programs in a way that guards against the accidental introduction of security vulnerabilities. As cyberattacks become increasingly sophisticated, the responsibility of building secure systems rests heavily on developers who must incorporate security considerations at every stage of the software development lifecycle.

For University of Delhi students pursuing Computer Science, understanding safe program coding is not just an academic requirement but a critical professional skill. The National Education Policy (NEP) 2024 emphasizes industry-ready skills, and cybersecurity awareness is among the most sought-after competencies in the tech industry. This topic explores the fundamental principles of secure coding, common vulnerabilities that plague software systems, and practical techniques to write robust, attack-resistant code. Whether you are developing web applications, mobile apps, or enterprise software, applying secure coding practices protects both your users and your organization from potential data breaches and financial losses.

## Key Concepts

### 1. OWASP Top 10 Vulnerabilities

The Open Web Application Security Project (OWASP) Top 10 is the de facto standard for understanding the most critical web application security risks. The current version includes:

- **Broken Access Control**: Occurs when users can act outside their intended permissions
- **Cryptographic Failures**: Formerly known as sensitive data exposure, involves improper encryption
- **Injection**: SQL, NoSQL, and command injection when untrusted data is sent to an interpreter
- **Insecure Design**: Missing or ineffective security controls in the architecture
- **Security Misconfiguration**: Improperly configured permissions, outdated components, or verbose error messages
- **Vulnerable and Outdated Components**: Using software with known vulnerabilities
- **Identification and Authentication Failures**: Weak password policies, session management flaws
- **Software and Data Integrity Failures**: Assuming third-party resources are trustworthy without verification
- **Security Logging and Monitoring Failures**: Insufficient logging prevents detection of attacks
- **Server-Side Request Forgery (SSRF)**: Fetching remote resources without validating user-supplied URIs

### 2. Input Validation and Sanitization

One of the most fundamental principles of secure coding is never trusting user input. All data entering a program must be validated before processing. Input validation ensures that data conforms to expected formats, types, and ranges. Sanitization goes a step further by removing or encoding potentially dangerous characters.

**Primary Defense**: Validate on the server side (client-side validation can be bypassed)
**Allowlist Approach**: Define what is permitted rather than what is forbidden
**Context-Aware Encoding**: Encode output based on where data will be displayed (HTML, URL, JavaScript, SQL)

### 3. Authentication and Session Management

Proper authentication mechanisms are crucial for verifying user identities. Common vulnerabilities include:
- Storing passwords without proper hashing (always use bcrypt, Argon2, or PBKDF2)
- Weak password policies
- Predictable session IDs
- Failure to invalidate sessions on logout

Secure session management involves:
- Generating cryptographically random session identifiers
- Setting secure, HttpOnly, and SameSite cookies
- Implementing session timeout
- Regenerating session IDs after authentication

### 4. Least Privilege Principle

Every program, process, or user should operate using the minimum privileges necessary to complete its job. This principle limits the potential damage from successful attacks by restricting access to only what is absolutely required.

### 5. Defense in Depth

Rather than relying on a single security layer, secure coding implements multiple defensive measures. If one control fails, additional layers provide protection. For example, input validation might be bypassed, but parameterized queries provide a second layer of defense against SQL injection.

### 6. Secure Error Handling and Logging

Error messages should reveal minimal information to users while providing enough detail for debugging in development environments. Sensitive information in error messages can aid attackers. Logging should capture security-relevant events without exposing sensitive data like passwords or session tokens.

### 7. Secure File Handling

File operations are common sources of vulnerabilities:
- Path traversal attacks (../../../etc/passwd)
- Unrestricted file upload leading to remote code execution
- Serving files without proper content-type headers

## Examples

### Example 1: Preventing SQL Injection

**Vulnerable Code (Python with SQLite):**
```python
# NEVER USE STRING FORMATTING FOR SQL QUERIES
username = input("Enter username: ")
query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)
```

**Secure Code:**
```python
# Use parameterized queries
username = input("Enter username: ")
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
```

**Explanation**: The parameterized approach ensures that user input is treated as data, not executable code. Even if an attacker enters `' OR '1'='1`, it becomes a literal string to match, not a SQL command.

### Example 2: Secure Password Handling

**Vulnerable Code:**
```python
# Storing passwords in plain text
import hashlib
password = input("Enter password: ")
hashed = hashlib.sha256(password.encode()).hexdigest()  # WRONG!
# SHA-256 is too fast and can be brute-forced
```

**Secure Code:**
```python
import bcrypt
password = input("Enter password: ")
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
# To verify later:
if bcrypt.checkpw(password.encode(), hashed):
    print("Login successful")
```

**Explanation**: bcrypt includes salt (random data to prevent rainbow table attacks) and is deliberately slow (computationally expensive) to resist brute-force attacks. It also handles salting automatically.

### Example 3: Preventing Cross-Site Scripting (XSS)

**Vulnerable Code:**
```python
# Reflecting user input directly in HTML
username = request.params['name']
html_response = f"<h1>Welcome {username}!</h1>"
return html_response
```

**Secure Code:**
```python
import html
username = request.params['name']
# Escape HTML characters
safe_username = html.escape(username)
html_response = f"<h1>Welcome {safe_username}!</h1>"
return html_response
```

**Explanation**: The html.escape() function converts special characters like <, >, &, " to their HTML entity equivalents (&lt;, &gt;, &amp;, &quot;), preventing the browser from interpreting the input as executable script.

## Exam Tips

1. **Always validate input on the server side** — Client-side validation is for user experience only, not security.

2. **Use parameterized queries** for all database operations to prevent SQL injection attacks.

3. **Hash passwords with bcrypt or Argon2** — Never use MD5 or SHA-256 for password storage.

4. **Apply the principle of least privilege** — Code should run with minimum necessary permissions.

5. **Implement defense in depth** — Multiple security layers provide better protection than single controls.

6. **Escape output based on context** — HTML encoding, URL encoding, and JavaScript escaping serve different purposes.

7. **Keep dependencies updated** — Known vulnerabilities in third-party libraries are a major attack vector.

8. **Never expose sensitive information in error messages** — Log internally, show generic messages to users.

9. **Use secure session management** — Cryptographically random IDs, secure cookies, and proper timeout.

10. **Practice secure file handling** — Validate file types, limit upload sizes, and never use user input in file paths.