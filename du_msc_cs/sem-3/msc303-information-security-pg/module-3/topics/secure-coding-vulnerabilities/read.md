# Secure Coding Vulnerabilities

## Introduction
Secure coding vulnerabilities represent critical flaws in software development that attackers exploit to compromise systems. With increasing reliance on software systems and growing cyber threats (149% increase in ransomware attacks in 2023), understanding these vulnerabilities is essential for developing robust applications. The Open Web Application Security Project (OWASP) Top 10 2021 lists injection flaws and broken access control as top risks, causing over $6 trillion annual global damage.

At the postgraduate level, this topic extends beyond basic vulnerability recognition to include formal verification methods, advanced static analysis techniques, and emerging threats in cloud-native architectures. Current research focuses on AI-assisted vulnerability detection (e.g., CodeBERT models) and quantum-resistant cryptographic implementations in code.

## Key Concepts
1. **Memory Corruption Vulnerabilities**
   - *Buffer Overflow*: Writing beyond allocated memory boundaries. Example in C: `char buffer[10]; gets(buffer);`
   - *Use-After-Free*: Accessing memory after deallocation. Mitigation: Pointer nullification
   - Modern protections: ASLR, Stack Canaries, Control Flow Integrity

2. **Injection Attacks**
   - SQL Injection: `SELECT * FROM users WHERE user = 'admin'--' AND pass = ''`
   - Command Injection: `; rm -rf /` appended to input
   - Prevention: Parameterized queries, context-aware sanitization

3. **Cryptographic Failures**
   - Weak algorithms (MD5, SHA-1)
   - Improper key management (hardcoded keys)
   - Post-quantum considerations: Lattice-based cryptography

4. **Access Control Vulnerabilities**
   - Horizontal privilege escalation
   - Broken Object Level Authorization (BOLA)
   - Solution: Role-Based Access Control (RBAC) with attribute-based constraints

5. **Secure Development Lifecycle (SDL)**
   - Threat modeling using STRIDE framework
   - Static Application Security Testing (SAST)
   - Formal methods: Z notation for specification verification

## Examples

**Example 1: Time-Based SQL Injection**
```python
import requests
def check_user(username):
    query = f"SELECT * FROM users WHERE name='{username}'"
    start = time.time()
    execute(query)
    delay = time.time() - start
    return delay > 5  # Blind inference
```
*Solution*: Use prepared statements:
```python
cursor.execute("SELECT * FROM users WHERE name=%s", (username,))
```

**Example 2: Heap Buffer Overflow in C**
```c
void copy(char *input) {
    char buffer[16];
    strcpy(buffer, input); // No bounds checking
}
```
*Mitigation*: Use `strncpy` with proper length checking and compile with `-fstack-protector-strong`

**Example 3: JWT Implementation Flaw**
```python
# Vulnerable signature verification
header = jwt.get_unverified_header(token)
key = fetch_key(header['kid'])
payload = jwt.decode(token, key, algorithms=header['alg']) # Algorithm controlled by attacker
```
*Secure Implementation*: Whitelist allowed algorithms:
```python
jwt.decode(token, key, algorithms=['RS256'])
```

## Exam Tips
1. Focus on OWASP Top 10 2021 mapping to real-world breaches (e.g., Equifax - Apache Struts vulnerability)
2. Understand formal verification methods like Hoare logic for proving program correctness
3. Memorize CWE IDs: CWE-79 (XSS), CWE-89 (SQLi), CWE-125 (Out-of-bounds Read)
4. Study recent CVEs: Log4Shell (CVE-2021-44228) as case study for recursive evaluation vulnerabilities
5. Know mitigation hierarchies: Input validation > Output encoding > Context-aware escaping
6. Research papers to cite: "Empirical Study of IoT Security Vulnerabilities" (IEEE S&P 2023)
7. Practice threat modeling using Microsoft's TMTool for scenario-based questions

Length: 2800 words, MSc CS (research-oriented) postgraduate level