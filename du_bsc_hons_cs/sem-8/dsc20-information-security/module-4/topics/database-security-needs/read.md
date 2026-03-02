# Database Security Needs

## Subject: Information Security | BSc (Hons) Computer Science - Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

Database security refers to the set of controls, policies, and measures designed to protect database management systems (DBMS) from unauthorized access, misuse, malicious attacks, and data breaches. In an era where data is often called the "new oil," databases serve as the central repositories for an organization's most sensitive information—including customer records, financial transactions, intellectual property, and strategic business intelligence.

**Why Database Security Matters in 2024:**

The digital landscape has witnessed unprecedented data growth, with global data creation projected to exceed 180 zettabytes by 2025. For Delhi University students pursuing Computer Science, understanding database security is no longer optional—it is a core competency demanded by the industry. High-profile breaches have demonstrated that inadequate database security can result in:

- **Financial losses:** The average cost of a data breach reached $4.88 million in 2024 (IBM Security Report)
- **Reputational damage:** Companies like Equifax (2017) lost billions in market value after exposing 147 million records
- **Legal consequences:** GDPR violations can impose fines up to €20 million or 4% of global annual revenue
- **Identity theft:** Stolen personal data enables fraudulent activities affecting millions of individuals

This study material aligns with the Delhi University BSc (Hons) Computer Science syllabus under the Information Security paper, covering essential concepts, practical implementations, and assessment preparation.

---

## 2. Fundamental Database Security Concepts

### 2.1 The CIA Triad in Database Context

Database security fundamentally revolves around the **CIA Triad**:

| Principle | Database Application |
|-----------|---------------------|
| **Confidentiality** | Ensuring only authorized users can view sensitive data (encryption, access control) |
| **Integrity** | Preventing unauthorized modification of data (constraints, checksums, triggers) |
| **Availability** | Ensuring authorized users can access data when needed (backups, replication, failover) |

### 2.2 Multi-Layered Security Approach

Modern database security employs a defense-in-depth strategy with multiple layers:

```
┌─────────────────────────────────────────┐
│         Perimeter Security              │
│    (Firewalls, Network Segmentation)    │
├─────────────────────────────────────────┤
│        Database Firewall                │
│   (SQL Firewall, Intrusion Detection)   │
├─────────────────────────────────────────┤
│     Authentication & Authorization      │
│    (RBAC, MFA, Privileged Access)       │
├─────────────────────────────────────────┤
│      Data-Level Protection              │
│  (Encryption, Masking, Tokenization)    │
├─────────────────────────────────────────┤
│      Auditing & Monitoring              │
│   (Logs, Alerts, Compliance Reports)    │
└─────────────────────────────────────────┘
```

---

## 3. Threats to Database Security

### 3.1 Common Threat Vectors

1. **SQL Injection (SQLi)**
   - Attackers manipulate user inputs to execute malicious SQL statements
   - Can lead to data theft, modification, or complete database compromise

2. **Privilege Abuse**
   - Legitimate users exceeding their authorized access levels
   - Insiders with malicious intent or curiosity

3. **Weak Authentication**
   - Default passwords, brute-force vulnerable credentials
   - Lack of multi-factor authentication (MFA)

4. **Data Exfiltration**
   - Advanced Persistent Threats (APTs) slowly extracting data
   - Unencrypted data in transit or at rest

5. **Denial of Service (DoS)**
   - Resource exhaustion through malicious queries
   - Database flooding attacks

6. **Misconfiguration**
   - Default settings left unchanged
   - Unnecessary services running

**Real-World Example: The 2017 Equifax Breach**
The Equifax breach exposed 147 million personal records due to an unpatched Apache Struts vulnerability. Attackers exploited a known vulnerability to inject malicious code, extracting sensitive data including Social Security numbers, birth dates, and addresses. This case emphasizes the critical need for patch management and vulnerability assessment in database systems.

---

## 4. Access Control Mechanisms

### 4.1 Discretionary Access Control (DAC)

In DAC, database owners or users determine who can access specific objects. Each object has an owner who can grant or revoke permissions.

```sql
-- MySQL Example: DAC Implementation
GRANT SELECT, INSERT ON company_db.employees TO 'hr_user'@'localhost';
GRANT ALL PRIVILEGES ON company_db.salary_details TO 'finance_manager'@'localhost';
REVOKE INSERT ON company_db.employees FROM 'temp_user'@'%';
```

### 4.2 Mandatory Access Control (MAC)

In MAC, the system enforces access based on security labels. Users and data objects have classification levels (e.g., Top Secret, Secret, Confidential, Public). This model is commonly used in military and government systems.

### 4.3 Role-Based Access Control (RBAC)

RBAC assigns permissions to roles rather than individual users, simplifying administration.

```sql
-- PostgreSQL Example: RBAC Implementation

-- Create roles
CREATE ROLE analyst;
CREATE ROLE developer;
CREATE ROLE admin;

-- Assign privileges to roles
GRANT SELECT ON ALL TABLES IN SCHEMA public TO analyst;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO developer;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO admin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO admin;

-- Assign roles to users
GRANT analyst TO 'amit_user';
GRANT developer TO 'raj_user';
GRANT admin TO 'database_admin';
```

### 4.4 Attribute-Based Access Control (ABAC)

ABAC makes access decisions based on user attributes, resource attributes, and environmental conditions.

```
User: (role=doctor, department=cardiology, clearance=level3)
Resource: (classification=medical-records, department=cardiology)
Action: READ
Environment: (time=09:00-17:00, location=hospital-network)

Decision: GRANT if user.department matches resource.department
```

---

## 5. Authentication Mechanisms

### 5.1 Password-Based Authentication

The most common method, requiring users to provide correct credentials.

```sql
-- MySQL: Creating users with secure passwords
CREATE USER 'database_user'@'localhost' 
IDENTIFIED BY 'Str0ngP@ssw0rd!2024';

-- Enforce password policy
SET GLOBAL validate_password.policy = 'STRONG';
SET GLOBAL validate_password.length = 12;
```

### 5.2 Multi-Factor Authentication (MFA)

MFA requires two or more verification factors:
- **Something you know** (password, PIN)
- **Something you have** (token, smartphone)
- **Something you are** (fingerprint, facial recognition)

```python
# Python Example: Implementing MFA with TOTP
import pyotp

def generate_totp_secret():
    """Generate a new TOTP secret for user"""
    return pyotp.random_base32()

def verify_totp(token, secret):
    """Verify TOTP token"""
    totp = pyotp.TOTP(secret)
    return totp.verify(token)

# Usage
secret = generate_totp_secret()
print(f"Share this secret with user: {secret}")
# User enters token from authenticator app
is_valid = verify_totp("123456", secret)
```

### 5.3 Certificate-Based Authentication

Uses digital certificates for mutual authentication between client and database server.

### 5.4 Single Sign-On (SSO)

Allows users to authenticate once and access multiple database systems.

---

## 6. SQL Injection: The Persistent Threat

SQL Injection remains one of the most critical web application vulnerabilities. Attackers inject malicious SQL code through user inputs.

### 6.1 Vulnerable Code Example

```python
# VULNERABLE: Never use string formatting for SQL queries
user_input = "' OR '1'='1"  # Malicious input
query = "SELECT * FROM users WHERE username = '" + user_input + "'"
# Executes as: SELECT * FROM users WHERE username = '' OR '1'='1'
# Returns ALL users!
```

### 6.2 Secure Implementation Using Prepared Statements

```python
# SECURE: Using parameterized queries (Prepared Statements)
import sqlite3

def authenticate_user(username, password):
    """Secure user authentication with parameterized queries"""
    conn = sqlite3.connect('application.db')
    cursor = conn.cursor()
    
    # Use ? placeholders - prevents SQL injection
    query = "SELECT user_id, username, role FROM users WHERE username = ? AND password_hash = ?"
    
    # Parameters are safely escaped
    cursor.execute(query, (username, hash_password(password)))
    
    result = cursor.fetchone()
    conn.close()
    return result
```

### 6.3 Types of SQL Injection

| Type | Description | Example |
|------|-------------|---------|
| **In-band** | Attacker uses same channel for attack and results | Union-based, Error-based |
| **Blind** | No visible errors; attacker infers information | Boolean-based, Time-based |
| **Out-of-band** | Different channel for results | DNS exfiltration, HTTP requests |

### 6.4 Prevention Best Practices

1. Use **parameterized queries** or **prepared statements**
2. Employ **stored procedures** with minimal privileges
3. Implement **input validation** and **output encoding**
4. Apply **least privilege** principles to database accounts
5. Use **Web Application Firewalls (WAF)**
6. Conduct regular **penetration testing**

---

## 7. Database Encryption

### 7.1 Encryption at Rest

Protects stored data from physical theft or unauthorized access.

**Transparent Data Encryption (TDE):**
```sql
-- Oracle: Enable TDE
ALTER SYSTEM SET ENCRYPTION KEY AUTHENTICATED BY "admin_password";

-- Create encrypted tablespace
CREATE TABLESPACE encrypted_data 
ENCRYPTION USING 'AES256' 
DEFAULT STORAGE (ENCRYPT);
```

```sql
-- SQL Server: Enable TDE
USE master;
GO
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Str0ngM@sterK3y!';

CREATE CERTIFICATE TDECertificate 
WITH SUBJECT = 'TDE Certificate';

USE your_database;
GO
CREATE DATABASE ENCRYPTION KEY 
WITH ALGORITHM = AES_256 
ENCRYPTION BY SERVER CERTIFICATE TDECertificate;

ALTER DATABASE your_database 
SET ENCRYPTION ON;
```

### 7.2 Encryption in Transit

Secures data moving between client and server using TLS/SSL.

```ini
# MySQL: Enable SSL/TLS
[mysqld]
require_secure_transport = ON
ssl_ca = /path/to/ca-cert.pem
ssl_cert = /path/to/server-cert.pem
ssl_key = /path/to/server-key.pem
```

### 7.3 Encryption Types Comparison

| Type | Algorithm | Use Case | Key Length |
|------|-----------|----------|------------|
| **Symmetric** | AES, 3DES | Bulk data encryption | 128, 192, 256 bits |
| **Asymmetric** | RSA, ECC | Key exchange, digital signatures | 2048, 4096 bits |
| **Hashing** | SHA-256, SHA-3 | Data integrity | Output: 256, 512 bits |
| **Homomorphic** | Paillier, BFV | Computing on encrypted data | Experimental |

### 7.4 Column-Level Encryption

```sql
-- MySQL: AES_ENCRYPT/AES_DECRYPT for sensitive columns
INSERT INTO users (username, ssn_encrypted) 
VALUES ('john_doe', AES_ENCRYPT('123-45-6789', 'encryption_key_256bit'));

SELECT username, AES_DECRYPT(ssn_encrypted, 'encryption_key_256bit') AS ssn 
FROM users;
```

---

## 8. Audit Mechanisms and Monitoring

### 8.1 Database Auditing

Comprehensive logging tracks all database activities for security analysis and compliance.

```sql
-- Oracle: Enable unified auditing
CREATE UNIFIED AUDIT POLICY db_security_policy
  PRIVILEGES CREATE ANY PROCEDURE,
  PRIVILEGES DROP ANY TABLE,
  ACTIONS SELECT ON hr.employees,
  ACTIONS DELETE ON finance.accounts;

AUDIT POLICY db_security_policy;

-- View audit records
SELECT event_timestamp, db_user, action_name, object_name
FROM unified_audit_trail
WHERE event_timestamp > SYSDATE - 7;
```

### 8.2 Audit Log Best Practices

1. **Log all authentication attempts** (success and failure)
2. **Record DDL and DML operations** on sensitive tables
3. **Protect audit logs** from tampering (write-only storage, checksums)
4. **Implement log retention** policies (regulatory compliance)
5. **Use automated alerts** for suspicious activities

### 8.3 Real-Time Monitoring

```python
# Python: Database activity monitoring example
import logging
from datetime import datetime

class DatabaseAuditLogger:
    def __init__(self, log_file):
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def log_query(self, user, query, timestamp=None):
        """Log all database queries"""
        # Mask sensitive data in logs
        masked_query = self.mask_sensitive_data(query)
        logging.info(f"User: {user} | Query: {masked_query}")
    
    def log_authentication(self, username, success, ip_address):
        """Log authentication attempts"""
        status = "SUCCESS" if success else "FAILED"
        logging.warning(f"Auth {status}: User={username}, IP={ip_address}")
    
    def mask_sensitive_data(self, query):
        """Mask potential sensitive data in queries"""
        import re
        # Mask potential credit card numbers
        return re.sub(r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}', '****-****-****-****', query)

# Usage
audit_logger = DatabaseAuditLogger('/var/log/database_audit.log')
audit_logger.log_query('admin_user', "SELECT * FROM customers WHERE ssn='123-45-6789'")
audit_logger.log_authentication('john_doe', True, '192.168.1.100')
```

---

## 9. Compliance and Regulatory Frameworks

### 9.1 GDPR (General Data Protection Regulation)

- Applies to EU citizens' data worldwide
- Key requirements: Consent, data minimization, right to erasure, breach notification (72 hours)

### 9.2 IT Act 2000 (India)

- Section 43A: Compensation for failure to protect data
- Section 72A: Penalty for disclosure of personal information

### 9.3 PCI-DSS

- Standard for organizations handling credit card data
- Requires encryption, access control, regular testing

---

## 10. Key Takeaways

1. **Database security is multidimensional**—it requires layered defenses combining access control, encryption, authentication, and auditing.

2. **SQL injection remains a top threat**—always use parameterized queries/prepared statements; never concatenate user input into SQL strings.

3. **Defense-in-depth is essential**—no single security measure is sufficient; implement multiple overlapping controls.

4. **Encryption protects data at rest and in transit**—use AES-256 for symmetric encryption, TLS 1.3 for data in transit.

5. **RBAC simplifies administration**—assign permissions to roles, then map users to appropriate roles.

6. **Auditing is critical for compliance and forensics**—log all sensitive operations and protect audit trails from tampering.

7. **Regular security assessments**—conduct vulnerability scans, penetration tests, and code reviews.

8. **Compliance frameworks** guide security implementation—understand GDPR, IT Act, and industry-specific requirements.

---

## 11. Assessment Questions

### 11.1 Multiple Choice Questions

**Q1. Which SQL injection type involves no visible error messages and requires the attacker to infer information based on application behavior?**
- a) Error-based SQLi
- b) Union-based SQLi
- c) Blind SQLi
- d) Out-of-band SQLi

**Answer: c) Blind SQLi**

---

**Q2. In the CIA triad, ensuring that data in the database is not modified by unauthorized users relates to:**
- a) Confidentiality
- b) Integrity
- c) Availability
- d) Authentication

**Answer: b) Integrity**

---

**Q3. Which encryption type is MOST appropriate for encrypting large volumes of stored data (encryption at rest)?**
- a) Asymmetric encryption (RSA)
- b) Symmetric encryption (AES)
- c) Hashing (SHA-256)
- d) Digital signatures

**Answer: b) Symmetric encryption (AES)**

---

**Q4. What is the primary advantage of Role-Based Access Control (RBAC) over Discretionary Access Control (DAC)?**
- a) More granular control over individual objects
- b) Simplified administration and easier permission management
- c) Users can grant permissions to other users
- d) No authentication required

**Answer: b) Simplified administration and easier permission management**

---

**Q5. Under GDPR, organizations must report data breaches within how many hours?**
- a) 24 hours
- b) 48 hours
- c) 72 hours
- d) 96 hours

**Answer: c) 72 hours**

---

### 11.2 Short Answer Questions

**Q1. Explain the difference between symmetric and asymmetric encryption. When would you use each?**

*Answer: Symmetric encryption uses the same key for encryption and decryption (e.g., AES), making it fast and suitable for bulk data encryption. Asymmetric encryption uses a public/private key pair (e.g., RSA), suitable for key exchange and digital signatures. For database encryption at rest, symmetric encryption is preferred due to performance; asymmetric is used for secure key distribution.*

---

**Q2. Describe three preventive measures against SQL injection attacks.**

*Answer: (1) Use parameterized queries/prepared statements instead of string concatenation, (2) Implement strict input validation and whitelist approaches, (3) Apply least privilege principles to database accounts, (4) Use stored procedures with limited permissions, (5) Deploy Web Application Firewalls (WAF).*

---

**Q3. What is the purpose of Transparent Data Encryption (TDE)?**

*Answer: TDE encrypts the entire database, including data files, log files, and backup files, at the storage level without requiring changes to existing applications. It protects against physical theft of storage media and ensures data remains encrypted at rest.*

---

### 11.3 Long Answer Questions

**Q1. A retail company stores customer data including credit card information. The database was compromised, and attackers gained access to sensitive customer records. Answer the following:**

- a) Identify at least 5 security controls that should have been implemented to prevent this breach. (10 marks)
- b) Explain how each control would have helped prevent or detected the attack. (10 marks)
- c) What steps should the company take after discovering the breach? (5 marks)

*Answer Guide:*
- a) Controls: (1) Encryption at rest for sensitive data, (2) Strong authentication including MFA, (3) Network segmentation and firewalls, (4) Database activity monitoring, (5) Regular security patches, (6) Principle of least privilege, (7) SQL injection prevention, (8) Regular penetration testing
- b) Each control explanation should relate to specific attack vectors
- c) Steps: Contain breach, assess scope, notify affected customers and regulators (within 72 hours for GDPR), preserve evidence, remediate vulnerabilities, communicate transparently

---

**Q2. Design a comprehensive database security policy for a healthcare organization handling patient records. Include sections on access control, authentication, encryption, auditing, and compliance requirements. (20 marks)**

*Answer Guide: Should cover HIPAA compliance requirements, role-based access for healthcare workers, encryption standards, audit requirements for patient data access, incident response procedures, and regular security assessments.*

---

### 11.4 Practical/Lab-Based Questions

**Q1. Write a Python program that demonstrates:**
- a) A vulnerable login function susceptible to SQL injection
- b) The corrected version using parameterized queries
- c) Code to detect SQL injection patterns in logs

---

**Q2. Using SQL, create a role-based access control system for a university database with the following requirements:**
- Administrator role: Full access to all tables
- Professor role: Can read and update courses and student_grades
- Student role: Can read own grades only
- Staff role: Can read and update student_contact_info only

---

## 12. Flashcards

| Term | Definition |
|------|------------|
| **SQL Injection** | Attack technique where malicious SQL code is inserted into application inputs to manipulate database |
| **CIA Triad** | Confidentiality, Integrity, Availability—three pillars of information security |
| **RBAC** | Role-Based Access Control—permissions assigned to roles, users assigned to roles |
| **TDE** | Transparent Data Encryption—encrypts database files at storage level without application changes |
| **MFA** | Multi-Factor Authentication—requires 2+ verification factors |
| **Prepared Statement** | Pre-compiled SQL template with parameter placeholders—prevents SQL injection |
| **Least Privilege** | Security principle granting minimum permissions necessary for job function |
| **Audit Trail** | Chronological record of database activities for security monitoring and forensics |
| **Data Masking** | Technique to obfuscate sensitive data, showing only non-sensitive portions |
| **Zero Trust** | Security model requiring verification from everyone accessing resources |

---

## 13. References and Further Reading

1. Oracle Database Security Guide (Oracle Documentation)
2. "The Database Hacker's Handbook" by David Litchfield et al.
3. OWASP Top 10 (for SQL Injection)
4. IBM Cost of Data Breach Report 2024
5. NIST Special Publication 800-53 (Security Controls)
6. Delhi University BSc (Hons) CS Syllabus - Information Security Paper

---

*Material prepared for BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)*