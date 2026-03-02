# SQL Injection Attacks

## Introduction

SQL Injection represents one of the most critical and prevalent vulnerabilities in web application security. It occurs when an attacker manipulates the input fields of a web application to interfere with the queries that the application makes to its database. This attack technique exploits security weaknesses in the application's database layer, allowing attackers to view, modify, or delete sensitive data that they should not have access to.

The significance of SQL injection in the context of information security cannot be overstated. According to the Open Web Application Security Project (OWASP), SQL injection has consistently ranked among the top ten most critical web application security risks for over a decade. In 2021, it held the third position in the OWASP Top 10 list. The consequences of a successful SQL injection attack can be devastating - from unauthorized access to millions of user credentials to complete database takeover and potential server compromise.

For University of Delhi students pursuing Computer Science, understanding SQL injection is essential not only for defensive security (building secure applications) but also for ethical hacking and penetration testing roles. This topic forms a crucial part of the information security curriculum and is highly relevant in today's digital landscape where data breaches can cause massive financial and reputational damage to organizations.

## Key Concepts

### What is SQL Injection?

SQL injection is a code injection technique that exploits security vulnerabilities in an application's database layer. It occurs when user input is incorrectly filtered or not strongly typed, allowing attackers to inject malicious SQL statements into the application's SQL queries. These injected statements can manipulate the logic of the original query, enabling unauthorized data access or administrative operations.

### How SQL Injection Works

The fundamental principle behind SQL injection involves understanding how SQL queries are constructed. When a web application needs to authenticate a user, it typically constructs a SQL query like:

```sql
SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
```

If the application directly incorporates user input into this query without proper sanitization, an attacker can input special SQL characters to modify the query's logic. For example, entering `' OR '1'='1` as the username would transform the query into:

```sql
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = ''
```

Since `'1'='1'` is always true, this authentication bypass succeeds, granting the attacker access without valid credentials.

### Types of SQL Injection

**1. In-Band SQL Injection**
This is the most common type where the attacker uses the same communication channel to launch the attack and retrieve results. It has two sub-types:
- **Error-based**: The attacker induces database errors to gather information about the structure
- **Union-based**: The attacker uses the UNION SQL operator to combine恶意 queries with legitimate ones

**2. Blind SQL Injection**
When the application does not display SQL errors but behaves differently based on true/false conditions, attackers use blind SQL injection. They infer information by observing the application's response patterns. For example:
```sql
' AND 1=1-- (results in true condition)
' AND 1=2-- (results in false condition)
```

**3. Out-of-Band SQL Injection**
This technique uses different channels for the attack and retrieving results, useful when in-band methods are not possible. It often relies on database features like database features or HTTP requests to exfiltrate data.

### SQL Injection Attack Vectors

Attackers can inject malicious SQL through various input points:
- **Form inputs**: Login forms, search boxes, feedback forms
- **URL parameters**: GET requests with query parameters
- **Cookies**: Stored client-side data
- **HTTP headers**: User-Agent, Referer fields
- **Application logic**: Stored procedures and triggers

### Impact of SQL Injection

The consequences of SQL injection attacks include:
- **Authentication bypass**: Accessing accounts without valid credentials
- **Data exfiltration**: Reading sensitive information from databases
- **Data modification**: Updating or deleting data
- **Database takeover**: Executing administrative operations
- **System compromise**: In some cases, executing operating system commands

### Prevention Techniques

**1. Parameterized Queries (Prepared Statements)**
Using parameterized queries ensures that user input is treated as data, not executable code:

```python
# Vulnerable (Python)
query = "SELECT * FROM users WHERE id = " + user_input

# Secure (Python with parameterized query)
query = "SELECT * FROM users WHERE id = %s"
cursor.execute(query, (user_input,))
```

**2. Stored Procedures**
Using pre-defined database procedures with strict parameter types can reduce injection risks, though they are not foolproof if not implemented correctly.

**3. Input Validation**
Validating and sanitizing all user inputs against strict patterns helps prevent malicious input from reaching the database.

**4. Escaping User Inputs**
Database-specific escaping functions can neutralize special characters in user input.

**5. Least Privilege Principle**
Database accounts should have minimum necessary permissions, limiting damage if an injection succeeds.

**6. Web Application Firewalls (WAF)**
WAFs can detect and block known SQL injection patterns, providing an additional layer of defense.

## Examples

### Example 1: Authentication Bypass

Consider a PHP login form with the following vulnerable code:

```php
$username = $_POST['username'];
$password = $_POST['password'];
$query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = mysqli_query($conn, $query);
```

**Attack Input:**
- Username: `admin'--`
- Password: `anything`

**Resulting Query:**
```sql
SELECT * FROM users WHERE username='admin'--' AND password='anything'
```

The `--` comment syntax comments out everything after it, making the password check irrelevant. This grants admin access.

**Secure Version:**
```php
$stmt = $conn->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
$stmt->bind_param("ss", $username, $password);
$stmt->execute();
```

### Example 2: Union-Based Data Extraction

An attacker targets a search functionality with this vulnerable query:
```sql
SELECT id, name, price FROM products WHERE name LIKE '%search_term%'
```

**Attack Input:** `' UNION SELECT username, password, 3 FROM users--`

**Modified Query:**
```sql
SELECT id, name, price FROM products WHERE name LIKE '%' UNION SELECT username, password, 3 FROM users--%'
```

This combines the product search with a complete dump of user credentials.

### Example 3: Blind SQL Injection in Boolean-Based Attack

Consider a vulnerable URL: `http://example.com/product.php?id=1`

The attacker tests conditions:
- `http://example.com/product.php?id=1 AND 1=1` → Page loads normally (True)
- `http://example.com/product.php?id=1 AND 1=2` → Page shows error or different content (False)

**Extracting Database Version:**
Using ASCII and SUBSTRING functions:
- `id=1 AND ASCII(SUBSTRING((SELECT database()),1,1))>64` → True (first letter ASCII > 64)
- Iterating through ASCII values reveals the database name character by character

## Exam Tips

1. **Remember the definition**: SQL injection is a code injection technique that exploits vulnerabilities in database layer input handling.

2. **Know the three main types**: In-Band (Error-based, Union-based), Blind, and Out-of-Band SQL injection.

3. **Understand the root cause**: SQL injection occurs when user input is concatenated directly into SQL queries without proper sanitization or parameterization.

4. **Prevention is key**: Memorize at least three prevention techniques: parameterized queries, input validation, and least privilege principle.

5. **Know the OWASP context**: SQL injection consistently appears in OWASP Top 10 web application security risks.

6. **Comment characters matter**: Remember that `--` (double dash) is used to comment out the rest of the SQL query in many databases.

7. **Real-world impact**: Be prepared to explain the potential consequences of SQL injection attacks on organizations.

8. **Code examples**: Understand both vulnerable and secure code patterns, especially for login authentication scenarios.

9. **Difference between types**: Know how blind SQL injection differs from regular injection - it doesn't rely on visible error messages but infers information from application behavior.

10. **Defense in depth**: Remember that multiple security measures (WAF, parameterized queries, least privilege) should be used together for comprehensive protection.