# Security Functional Requirements

## A Comprehensive Study Material for BSc (Hons) Computer Science (NEP 2024 UGCF)

---

## 1. Introduction

In an increasingly interconnected digital world, information security has become a paramount concern for organizations, governments, and individuals alike. **Security Functional Requirements** define the specific security functions that a system, application, or infrastructure must provide to protect information assets from threats and vulnerabilities.

For students at Delhi University studying under the NEP 2024 UGCF curriculum, understanding security functional requirements is essential for designing, implementing, and maintaining secure computing systems. This topic forms a critical component of the Information Security syllabus and has direct relevance to real-world software development and system administration roles.

**Real-World Relevance:**
- **Banking Systems**: Online banking applications must ensure confidentiality of financial data, integrity of transactions, and availability 24/7
- **Healthcare Systems**: Patient records require strict confidentiality and integrity controls under regulations like HIPAA
- **E-Commerce Platforms**: Secure payment processing demands robust authentication and authorization mechanisms
- **Corporate Networks**: Employee access to sensitive data must be controlled through proper authorization policies

---

## 2. Core Security Functional Requirements

The fundamental security functional requirements are often summarized by the **CIA Triad** (Confidentiality, Integrity, Availability), though modern security frameworks expand upon this foundation.

### 2.1 Confidentiality

**Definition**: Confidentiality ensures that information is accessible only to authorized individuals, entities, or processes. It prevents unauthorized disclosure of sensitive data.

**Key Mechanisms**:
- **Encryption**: Converting plaintext data into ciphertext using cryptographic algorithms
- **Access Control Lists (ACLs)**: Defining who can access what resources
- **Data Classification**: Categorizing information based on sensitivity levels
- **Steganography**: Hiding information within other media

**Example Scenario**: In a university examination system, student grades must remain confidential. Only the student, academic administrators, and authorized faculty should access grade information.

```python
# Python example: Simple encryption using Fernet (symmetric encryption)
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt sensitive data (student grades)
sensitive_data = "Student_A: Grade = 95"
encrypted_data = cipher_suite.encrypt(sensitive_data.encode())

# Decrypt data (for authorized access)
decrypted_data = cipher_suite.decrypt(encrypted_data).decode()

print(f"Original: {sensitive_data}")
print(f"Encrypted: {encrypted_data}")
print(f"Decrypted: {decrypted_data}")
```

### 2.2 Integrity

**Definition**: Integrity ensures that information remains accurate, complete, and unaltered except by authorized changes. It protects data from unauthorized modification, deletion, or creation.

**Key Mechanisms**:
- **Hash Functions**: Creating fixed-size digests to verify data integrity (e.g., SHA-256, MD5)
- **Digital Signatures**: Providing authentication and integrity verification
- **Checksums**: Simple error-detection mechanisms
- **Version Control**: Tracking changes to documents and code
- **Audit Trails**: Recording all modifications to data

**Example Scenario**: When a student submits an assignment through the university portal, integrity ensures the submitted file is identical to the original and has not been tampered with during transmission.

```python
# Python example: Verifying file integrity using hash functions
import hashlib
import hmac

def calculate_file_hash(file_path, algorithm='sha256'):
    """Calculate hash of a file to verify integrity"""
    hash_obj = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as f:
        # Read file in chunks to handle large files
        for chunk in iter(lambda: f.read(4096), b''):
            hash_obj.update(chunk)
    
    return hash_obj.hexdigest()

def verify_integrity(original_hash, file_path):
    """Verify if file matches original hash"""
    current_hash = calculate_file_hash(file_path)
    return hmac.compare_digest(original_hash, current_hash)

# Example usage
original_hash = calculate_file_hash('assignment.pdf')
print(f"Original File Hash: {original_hash}")

# Verify later
is_valid = verify_integrity(original_hash, 'assignment.pdf')
print(f"File Integrity Verified: {is_valid}")
```

### 2.3 Availability

**Definition**: Availability ensures that authorized users have timely and reliable access to information and associated resources when needed. It protects against service disruptions and ensures business continuity.

**Key Mechanisms**:
- **Redundancy**: Implementing backup systems, servers, and data centers
- **Load Balancing**: Distributing traffic across multiple servers
- **Failover Systems**: Automatic switching to backup systems during failures
- **DDoS Protection**: Mitigating denial-of-service attacks
- **Regular Maintenance**: Scheduled updates and patches
- **Disaster Recovery Plans**: Procedures for restoring services after catastrophic events

**Example Scenario**: The Delhi University online examination portal must maintain high availability during examination periods when thousands of students simultaneously access the system.

**Real-World Example**: Amazon's AWS provides 99.99% availability for its services through:
- Multiple Availability Zones (data centers)
- Auto-scaling capabilities
- Geographic redundancy
- Service health monitoring

### 2.4 Authentication

**Definition**: Authentication is the process of verifying the identity of a user, device, or system before granting access to resources. It answers the question: "Who are you?"

**Authentication Factors**:

| Factor Type | Examples | Description |
|-------------|----------|-------------|
| **Something You Know** | Password, PIN, Security Questions | Knowledge-based verification |
| **Something You Have** | Smart Card, Token, Mobile Phone | Possession-based verification |
| **Something You Are** | Fingerprint, Face Recognition, Iris Scan | Biometric verification |
| **Somewhere You Are** | Geographic Location, IP Address | Location-based verification |
| **Something You Do** | Keystroke Dynamics, Voice Pattern | Behavioral verification |

**Multi-Factor Authentication (MFA)**: Combining two or more authentication factors for enhanced security.

```python
# Python example: Simple multi-factor authentication simulation
import hashlib
import secrets

class AuthenticationSystem:
    def __init__(self):
        self.users = {}
    
    def register_user(self, username, password, phone_number):
        """Register a new user with password and phone for 2FA"""
        # Hash password before storing
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        self.users[username] = {
            'password_hash': password_hash,
            'phone': phone_number,
            'failed_attempts': 0
        }
        print(f"User {username} registered successfully.")
    
    def authenticate(self, username, password, otp=None):
        """Authenticate user with password and optional OTP"""
        if username not in self.users:
            return False, "User not found"
        
        user = self.users[username]
        
        # Verify password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        if password_hash != user['password_hash']:
            user['failed_attempts'] += 1
            return False, "Invalid password"
        
        # In real system, OTP would be sent to phone
        # For simulation, accept any OTP if provided
        if otp:
            print(f"OTP verification would be sent to {user['phone']}")
        
        # Reset failed attempts on successful login
        user['failed_attempts'] = 0
        return True, "Authentication successful"

# Usage
auth_system = AuthenticationSystem()
auth_system.register_user("student_du", "SecurePass123", "+91-9876543210")

# Successful authentication
success, message = auth_system.authenticate("student_du", "SecurePass123")
print(f"Result: {message}")
```

### 2.5 Authorization

**Definition**: Authorization (also called Access Control) determines what actions an authenticated user is permitted to perform. It answers the question: "What can you do?" Authorization occurs after successful authentication.

**Key Models**:

1. **Discretionary Access Control (DAC)**: Owners determine who can access their resources
2. **Mandatory Access Control (MAC)**: System enforces access based on classification levels (used in military/government)
3. **Role-Based Access Control (RBAC)**: Access is based on user roles within an organization
4. **Attribute-Based Access Control (ABAC)**: Access decisions based on user attributes, resource attributes, and environmental conditions

```python
# Python example: Role-Based Access Control (RBAC) implementation
from enum import Enum
from functools import wraps

class Role(Enum):
    STUDENT = "student"
    FACULTY = "faculty"
    ADMIN = "admin"
    HOD = "hod"

class Permission(Enum):
    VIEW_GRADES = "view_grades"
    MODIFY_GRADES = "modify_grades"
    VIEW_COURSE = "view_course"
    MANAGE_COURSE = "manage_course"
    MANAGE_USERS = "manage_users"
    VIEW_REPORTS = "view_reports"

# Role-Permission mapping
ROLE_PERMISSIONS = {
    Role.STUDENT: [Permission.VIEW_GRADES, Permission.VIEW_COURSE],
    Role.FACULTY: [Permission.VIEW_GRADES, Permission.MODIFY_GRADES, 
                   Permission.VIEW_COURSE, Permission.MANAGE_COURSE],
    Role.HOD: [Permission.VIEW_GRADES, Permission.MODIFY_GRADES,
               Permission.VIEW_COURSE, Permission.MANAGE_COURSE,
               Permission.VIEW_REPORTS],
    Role.ADMIN: [Permission.VIEW_GRADES, Permission.MODIFY_GRADES,
                 Permission.VIEW_COURSE, Permission.MANAGE_COURSE,
                 Permission.MANAGE_USERS, Permission.VIEW_REPORTS]
}

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
    
    def has_permission(self, permission):
        """Check if user has specific permission"""
        return permission in ROLE_PERMISSIONS.get(self.role, [])

def require_permission(permission):
    """Decorator to enforce authorization"""
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if not user.has_permission(permission):
                return f"Access Denied: {permission.value} required"
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

# Example usage
student = User("Rahul", Role.STUDENT)
faculty = User("Dr. Sharma", Role.FACULTY)
admin = User("Admin", Role.ADMIN)

@require_permission(Permission.MODIFY_GRADES)
def modify_student_grade(user, student_id, new_grade):
    return f"Grade modified for {student_id} to {new_grade} by {user.username}"

# Test authorization
print(modify_student_grade(student, "S001", "A"))
print(modify_student_grade(faculty, "S001", "A"))
print(modify_student_grade(admin, "S001", "A"))
```

### 2.6 Non-Repudiation

**Definition**: Non-repudiation ensures that parties in a communication cannot deny their actions or transactions. It provides proof of origin (sender cannot deny sending) and proof of delivery (receiver cannot deny receiving).

**Key Mechanisms**:
- **Digital Signatures**: Cryptographically bind identity to documents
- **Audit Logs**: Immutable records of all actions
- **Time Stamps**: Proving when actions occurred
- **Certificate Authorities (CAs)**: Trusted third parties verifying identities

**Example Scenario**: In online examination submissions, non-repudiation ensures students cannot deny submitting their answers, and the university cannot deny receiving them.

---

## 3. The AAA Framework

The **AAA framework** is a foundational concept in information security that encompasses three interrelated security functions:

### 3.1 Authentication (Who are you?)
- Verifying user identity before granting access
- Uses credentials (passwords, biometrics, tokens)
- First step in secure access control

### 3.2 Authorization (What can you do?)
- Determining user permissions after authentication
- Enforcing access control policies
- Based on roles, attributes, or rules

### 3.3 Accounting (What did you do?)
- Tracking user activities and resource usage
- Creating audit trails and logs
- Enabling monitoring and forensic analysis

**Delhi University Context**: The university examination management system implements AAA to:
- **Authenticate** students via login credentials
- **Authorize** access to specific courses and examination papers
- **Account** for all examination submissions with timestamps and logs

---

## 4. Additional Security Requirements

### 4.1 Privacy
Protecting personal information from unauthorized access and ensuring compliance with data protection regulations (e.g., GDPR, DPDP Act in India).

### 4.2 Accountability
Ensuring actions can be traced to specific users or processes through identification and audit mechanisms.

### 4.3 Secure Design Principles
- **Least Privilege**: Users get minimum necessary permissions
- **Defense in Depth**: Multiple layers of security controls
- **Fail Secure**: Systems fail to a secure state
- **Separation of Duties**: No single person has complete control

---

## 5. Key Takeaways

1. **CIA Triad** forms the foundation: Confidentiality, Integrity, and Availability are the core security functional requirements

2. **Authentication** verifies identity through one or more factors (something you know, have, or are)

3. **Authorization** determines what authenticated users can access and do—it's about permissions and access control

4. **Availability** ensures systems and data are accessible when needed through redundancy, failover, and maintenance

5. **Non-repudiation** provides proof of actions through digital signatures and audit trails

6. **AAA Framework** (Authentication, Authorization, Accounting) comprehensively covers security functional requirements

7. **RBAC** (Role-Based Access Control) is widely used in organizational systems, including educational institutions

8. **Encryption** is essential for protecting confidentiality of data both at rest and in transit

9. **Hash functions** ensure data integrity by detecting any unauthorized modifications

10. Security requirements must be designed into systems from the beginning (Security by Design)

---

## 6. Multiple Choice Questions

**Question 1**: Which security functional requirement ensures that information is accessible only to authorized individuals?
- A) Integrity
- B) Availability
- C) Confidentiality
- D) Authentication

**Answer**: C) Confidentiality

---

**Question 2**: In the AAA framework, what does the "A" in "AAA" stand for when discussing authorization?
- A) Accounting
- B) Auditing
- C) Authentication
- D) Access

**Answer**: C) Authentication (The three A's are Authentication, Authorization, and Accounting)

---

**Question 3**: Which access control model determines access based on user roles within an organization?
- A) DAC (Discretionary Access Control)
- B) MAC (Mandatory Access Control)
- C) RBAC (Role-Based Access Control)
- D) ABAC (Attribute-Based Access Control)

**Answer**: C) RBAC

---

**Question 4**: What type of authentication uses fingerprint or facial recognition?
- A) Something you know
- B) Something you have
- C) Something you are
- D) Somewhere you are

**Answer**: C) Something you are (Biometric)

---

**Question 5**: Which mechanism ensures that a sender cannot deny sending a message?
- A) Encryption
- B) Hashing
- C) Digital Signature
- D) Firewalls

**Answer**: C) Digital Signature

---

## 7. Flashcards

| Term | Definition |
|------|------------|
| **Confidentiality** | Security requirement ensuring data is accessible only to authorized parties |
| **Integrity** | Ensuring data remains accurate and unaltered except by authorized changes |
| **Availability** | Ensuring authorized users have timely access to resources when needed |
| **Authentication** | Process of verifying the identity of a user or system |
| **Authorization** | Process of determining what actions an authenticated user can perform |
| **Non-repudiation** | Ability to prove that an action or transaction occurred |
| **RBAC** | Access control model based on user roles within an organization |
| **MFA** | Authentication using multiple factors (2FA, 3FA) |
| **CIA Triad** | Core security principles: Confidentiality, Integrity, Availability |
| **AAA Framework** | Authentication, Authorization, and Accounting |

---

## 8. Summary for Delhi University Syllabus

This study material covers the **Security Functional Requirements** topic as per the NEP 2024 UGCF syllabus for BSc (Hons) Computer Science. Students should understand:

- The CIA triad and its practical applications
- The distinction between authentication and authorization
- AAA framework implementation in real systems
- Role-based access control with practical examples
- Security mechanisms like encryption, hashing, and digital signatures

**Recommended Further Reading**:
- "Principles of Information Security" by Michael E. Whitman
- "Computer Security: Principles and Practice" by William Stallings
- OWASP Top 10 Security Concepts

---

*This study material contains approximately 2,100 words and covers all key concepts required for the Delhi University BSc (Hons) Information Security curriculum.*