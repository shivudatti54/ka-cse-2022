# SQL Injection Attacks - Summary

## Key Definitions and Concepts

- **SQL Injection**: A code injection technique that exploits vulnerabilities in an application's database layer by manipulating user input to interfere with SQL queries
- **In-Band SQL Injection**: Most common type using the same channel for attack and data retrieval; includes Error-based and Union-based variants
- **Blind SQL Injection**: Exploits applications that don't display SQL errors; attackers infer information by observing true/false conditions
- **Out-of-Band SQL Injection**: Uses different channels for attack and data exfiltration, useful when in-band methods fail

## Important Formulas and Techniques

- **Parameterized Query Pattern**: `SELECT * FROM users WHERE id = ?` - treats user input as data, not code
- **Authentication Bypass**: Using `' OR '1'='1` or `admin'--` to bypass login checks
- **Union-Based Extraction**: `' UNION SELECT columns FROM other_table--` to extract data from different tables
- **Blind Injection Logic**: Testing conditions like `AND 1=1` (true) vs `AND 1=2` (false) to infer database information

## Key Points

- SQL injection occurs when user input is directly concatenated into SQL queries without sanitization
- The `--` comment syntax is used to truncate queries in many database systems
- Prevention requires parameterized queries, input validation, escaping, and least privilege access
- SQL injection consistently ranks in OWASP Top 10 critical web application security risks
- Attackers can bypass authentication, extract data, modify database contents, or execute administrative operations
- Blind SQL injection works even when error messages are suppressed by observing application behavior changes
- Web Application Firewalls (WAF) provide an additional layer of defense against SQL injection attacks
- Different database systems may use different comment syntax and special characters

## Common Mistakes to Avoid

- **Using string concatenation** for building SQL queries with user input - always use parameterized queries
- **Assuming input validation alone is sufficient** - always use defense in depth with multiple techniques
- **Ignoring error messages** - detailed database errors can aid attackers in information gathering
- **Granting excessive database permissions** to application accounts - follow the principle of least privilege

## Revision Tips

1. Practice identifying vulnerable vs secure code patterns in authentication scenarios
2. Memorize the three main types of SQL injection and how they differ in execution
3. Remember that `--` is the standard SQL comment character that truncates queries
4. Review real-world SQL injection breach case studies to understand practical impacts
5. Write sample vulnerable code and then convert it to secure versions using parameterized queries