# Security Design Principles

## Comprehensive Study Material for GE8A Information Security

---

## 1. Introduction

### 1.1 What are Security Design Principles?

Security Design Principles are fundamental guidelines that inform the creation of secure systems. These principles represent time-tested wisdom accumulated from decades of experience in designing, implementing, and maintaining secure computing systems. They serve as the foundation upon which robust security architectures are built.

### 1.2 Why These Principles Matter

In today's interconnected digital world, cyberattacks are becoming increasingly sophisticated. From ransomware attacks on hospitals to data breaches at major corporations, the need for secure system design has never been more critical. The principles outlined in this material provide a systematic approach to thinking about security—transforming it from an afterthought into a fundamental design requirement.

For students at Delhi University studying under NEP 2024, understanding these principles is essential not only for passing examinations but also for building a career in cybersecurity or software development where security is paramount.

### 1.3 Historical Context

Many of these principles were articulated by saltzer and Schroeder in their seminal 1975 paper "The Protection of Information in Computer Systems." Despite being nearly five decades old, these principles remain remarkably relevant and form the core of modern security design.

---

## 2. Core Security Design Principles

### 2.1 Least Privilege (or Least Authority)

**Definition:** Every program, user, and process should operate using the minimum set of privileges necessary to complete its job. No component should be granted more access than absolutely required.

**Detailed Explanation:**

Least Privilege is perhaps the most fundamental security design principle. It limits the potential damage from accidents, errors, or malicious activities by restricting access rights to the minimum necessary.

**Key Aspects:**
- **User Level:** Users should have only the permissions needed for their specific job function
- **Process Level:** Programs should run with the minimum permissions required
- **Temporal Aspect:** Privileges should be granted only for the duration needed
- **Administrative Access:** Even administrators should use lower-privilege accounts for routine work

**Real-World Example:**

Consider a hospital information system where different roles require different access levels:

```python
# Example: Implementing Least Privilege in a hospital system
class UserRole:
    """Define roles with minimum necessary permissions"""
    
    def __init__(self, role_name, permissions):
        self.role_name = role_name
        self.permissions = permissions  # Only what they NEED

class HospitalSystem:
    """
    Least Privilege Example: Different roles have different access levels
    - Receptionist: Can view patient appointments, NOT medical records
    - Nurse: Can view and update vital signs, NOT financial data
    - Doctor: Can view and update full medical records
    - Billing: Can view financial data, NOT medical records
    """
    
    # Instead of granting ALL access to everyone, granular permissions
    PERMISSIONS = {
        'view_appointments': ['receptionist', 'nurse', 'doctor'],
        'view_medical_records': ['nurse', 'doctor'],
        'update_vital_signs': ['nurse', 'doctor'],
        'update_medical_records': ['doctor'],
        'view_billing': ['billing', 'accountant'],
        'process_payments': ['accountant'],
    }
    
    @staticmethod
    def check_permission(user_role, required_permission):
        """Verify user has ONLY the permission they need"""
        allowed_roles = HospitalSystem.PERMISSIONS.get(required_permission, [])
        return user_role in allowed_roles

# Demonstration
receptionist = UserRole('receptionist', ['view_appointments'])
doctor = UserRole('doctor', ['view_appointments', 'view_medical_records', 
                             'update_vital_signs', 'update_medical_records'])

# Doctor tries to access billing (should be DENIED)
print(f"Doctor accessing billing: {HospitalSystem.check_permission(doctor.role_name, 'view_billing')}")  # False

# Receptionist tries to access medical records (should be DENIED)
print(f"Receptionist accessing medical records: {HospitalSystem.check_permission(receptionist.role_name, 'view_medical_records')}")  # False
```

### 2.2 Defense in Depth (Layered Security)

**Definition:** Security should not rely on a single layer of protection. Multiple security mechanisms should be implemented so that if one layer fails, others continue to provide protection.

**Detailed Explanation:**

Defense in Depth recognizes that no single security measure is perfect. By implementing multiple layers of defense, an attacker must bypass all layers to succeed. This is often compared to the security at a medieval castle—multiple walls, moats, guards, and checkpoints.

**Layers of Defense:**
1. **Physical Security:** Locks, security personnel, access controls
2. **Network Security:** Firewalls, intrusion detection systems, VPNs
3. **Operating System Security:** Permissions, patching, hardening
4. **Application Security:** Input validation, secure coding, authentication
5. **Data Security:** Encryption, access controls, backups

**Real-World Example:**

```python
# Example: Defense in Depth for a web application
class WebApplicationSecurity:
    """
    Implementing Defense in Depth: Multiple layers of protection
    """
    
    @staticmethod
    def authenticate_user(username, password):
        """
        Layer 1: Authentication
        Multiple checks before granting access
        """
        # Rate limiting (Layer 1a)
        if RateLimiter.is_blocked(username):
            raise SecurityException("Account temporarily locked")
        
        # Primary authentication (Layer 1b)
        user = Database.get_user(username)
        if not PasswordHasher.verify(password, user.hashed_password):
            AuditLogger.log_failed_login(username)
            raise AuthenticationFailedException()
        
        # Multi-factor authentication (Layer 1c)
        if user.requires_mfa:
            mfa_code = MFAService.send_code(user.phone)
            if not mfa_code.verify(input("Enter MFA code: ")):
                raise AuthenticationFailedException()
        
        return SessionManager.create_session(user)
    
    @staticmethod
    def authorize_request(session, resource):
        """
        Layer 2: Authorization
        Verify permissions at multiple levels
        """
        # Check session validity
        if not SessionManager.is_valid(session):
            raise UnauthorizedException()
        
        # Check resource permissions
        if not PermissionChecker.has_access(session.user, resource):
            AuditLogger.log_unauthorized_access(session.user, resource)
            raise ForbiddenException()
        
        # Check temporal constraints
        if not TimeBasedAccess.is_within_working_hours(session.user):
            raise AccessDeniedException("Outside permitted hours")
        
        return True

# Demonstration of layered approach
print("Layer 1: Authentication with Rate Limiting + Password + MFA")
print("Layer 2: Authorization with Session + Permissions + Time Checks")
print("Layer 3: Input Validation + Output Encoding + SQL Injection Prevention")
print("Layer 4: HTTPS + Security Headers + CSRF Tokens")
print("Layer 5: Logging + Monitoring + Incident Response")
```

### 2.3 Separation of Duties (or Segregation of Duties)

**Definition:** No single individual or component should have complete control over a critical process. Important tasks should be divided among multiple parties so that collusion would be required to compromise the system.

**Detailed Explanation:**

Separation of Duties is designed to prevent fraud and error by ensuring that no single person has complete control over a sensitive operation. This principle is fundamental in financial systems, healthcare, and government operations.

**Applications:**
- Financial transactions requiring multiple approvals
- System administration tasks divided among team members
- Code changes requiring review before deployment
- Access to sensitive data requiring multiple authorizations

**Real-World Example:**

```python
# Example: Separation of Duties in a banking system
class BankingSystemWithSeparation:
    """
    Separation of Duties: No single person can complete a transaction
    """
    
    def __init__(self):
        self.pending_transactions = []
        self.approvals = {}  # transaction_id -> set of approvers
    
    def initiate_transfer(self, from_account, to_account, amount, initiator):
        """
        Step 1: Initiator creates transaction (cannot approve their own)
        """
        if not self.has_permission(initiator, 'initiate_transfer'):
            raise PermissionDenied("Cannot initiate transfers")
        
        transaction = {
            'id': self.generate_transaction_id(),
            'from': from_account,
            'to': to_account,
            'amount': amount,
            'initiated_by': initiator,
            'status': 'pending_approval'
        }
        
        self.pending_transactions.append(transaction)
        AuditLogger.log(f"Transaction {transaction['id']} initiated by {initiator}")
        
        return transaction['id']
    
    def approve_transfer(self, transaction_id, approver):
        """
        Step 2: Different person must approve
        """
        transaction = self.get_transaction(transaction_id)
        
        # CANNOT approve your own transaction
        if transaction['initiated_by'] == approver:
            raise SecurityViolation("Cannot approve your own transaction")
        
        if not self.has_permission(approver, 'approve_transfer'):
            raise PermissionDenied("Cannot approve transfers")
        
        # Track approvals
        if transaction_id not in self.approvals:
            self.approvals[transaction_id] = set()
        
        self.approvals[transaction_id].add(approver)
        
        # Need at least 2 different approvers for large amounts
        if transaction['amount'] > 100000:
            if len(self.approvals[transaction_id]) < 2:
                return "Pending additional approval"
        
        # Execute transaction
        self.execute_transaction(transaction)
        return "Transfer completed"
    
    def execute_transaction(self, transaction):
        """Execute only after proper approvals"""
        # Implementation of actual transfer
        AuditLogger.log(f"Transaction {transaction['id']} executed")

# Demonstration
banking = BankingSystemWithSeparation()

# Employee A initiates a large transfer
tx_id = banking.initiate_transfer("ACC001", "ACC002", 500000, "EmployeeA")
print(f"Transaction {tx_id} initiated by EmployeeA")

# Employee A CANNOT approve their own transaction
try:
    banking.approve_transfer(tx_id, "EmployeeA")
except SecurityViolation as e:
    print(f"Security Violation: {e}")

# Employee B approves
result = banking.approve_transfer(tx_id, "EmployeeB")
print(f"First approval: {result}")

# Employee C provides second approval for large amount
result = banking.approve_transfer(tx_id, "EmployeeC")
print(f"Second approval: {result}")
```

### 2.4 Fail Secure (Fail Safe)

**Definition:** When a system fails or encounters an error, it should default to a secure state rather than an insecure one. Systems should fail in a way that preserves security rather than exposing vulnerabilities.

**Detailed Explanation:**

Fail Secure means that any error, malfunction, or unexpected condition should not create a security loophole. The system should "fail closed" rather than "fail open."

**Key Considerations:**
- Default-deny policies (if not explicitly allowed, deny)
- Session termination on errors
- Default to most restrictive permissions
- Graceful degradation while maintaining security

**Real-World Example:**

```python
# Example: Fail Secure in an access control system
class SecureAccessControl:
    """
    Fail Secure: Default to DENY when uncertain
    """
    
    @staticmethod
    def check_file_access(user, file_path, requested_permission):
        """
        Multiple fail-secure checks
        """
        try:
            # Check if user exists
            user_record = UserDatabase.get(user)
            if user_record is None:
                # FAIL SECURE: Default deny for unknown users
                AuditLogger.log(f"Unknown user {user} denied access to {file_path}")
                return AccessResult.DENY
            
            # Check if file exists
            if not FileSystem.exists(file_path):
                # FAIL SECURE: Default deny for non-existent files
                return AccessResult.DENY
            
            # Check permissions
            permission = PermissionManager.get_permission(user, file_path)
            
            if permission is None:
                # FAIL SECURE: Default deny if permission unclear
                AuditLogger.log(f"No explicit permission for {user} on {file_path}")
                return AccessResult.DENY
            
            if not permission.allows(requested_permission):
                # Normal denial
                return AccessResult.DENY
            
            return AccessResult.ALLOW
            
        except DatabaseException as e:
            # FAIL SECURE: On database error, deny access
            AuditLogger.log(f"Database error - failing secure: {e}")
            return AccessResult.DENY
        
        except PermissionException as e:
            # FAIL SECURE: On permission error, deny access
            AuditLogger.log(f"Permission error - failing secure: {e}")
            return AccessResult.DENY
        
        except Exception as e:
            # FAIL SECURE: On ANY unexpected error, deny access
            AuditLogger.log(f"Unexpected error - failing secure: {e}")
            return AccessResult.DENY

# Demonstration
access_control = SecureAccessControl()

# Test various fail-secure scenarios
print("Normal case:", access_control.check_file_access("Alice", "/data/report.txt", "read"))
print("Unknown user:", access_control.check_file_access("Unknown", "/data/report.txt", "read"))
print("Database error simulation:", access_control.check_file_access("Bob", "/data/sensitive.txt", "write"))
```

### 2.5 Economy of Mechanism (Keep it Simple)

**Definition:** Security mechanisms should be as simple as possible. Complex security mechanisms are more likely to contain flaws and are harder to analyze, test, and maintain.

**Detailed Explanation:**

Also known as "KISS" (Keep It Simple, Stupid) applied to security, this principle emphasizes that simpler systems are more secure. Complexity is the enemy of security—each additional line of code, each new feature, and each integration point potentially introduces new vulnerabilities.

**Guidelines:**
- Prefer simple, well-understood algorithms
- Avoid custom cryptography (use standard libraries)
- Minimize the attack surface
- Design for understandability
- Regularly refactor and simplify

**Real-World Example:**

```python
# Example: Economy of Mechanism - Simple vs Complex authentication

# COMPLEX (Violates Economy of Mechanism) - Hard to maintain and secure
class ComplexAuthentication:
    """Over-engineered system with unnecessary complexity"""
    
    def authenticate(self, username, password, token, biometric, 
                     security_question, captcha, ip_blacklist, 
                     geo_location, device_fingerprint, social_login,
                     email_verification, sms_verification):
        # 15+ checks, many redundant
        # Hard to test, maintain, and secure
        # Each point is a potential vulnerability
        pass

# SIMPLE (Follows Economy of Mechanism)
class SimpleSecureAuthentication:
    """
    Economy of Mechanism: Few well-tested components
    """
    
    def __init__(self):
        # Use standard, well-tested components
        self.password_hasher = PasswordHasher()  # Uses bcrypt/argon2
        self.mfa_service = MFAService()  # Standard TOTP
        self.session_manager = SessionManager()  # Secure session handling
    
    def authenticate(self, username, password, mfa_code):
        """
        Simple flow: Password + MFA only
        - Fewer components = fewer vulnerabilities
        - Easier to audit and test
        - Standard implementations used
        """
        # 1. Get user (single query)
        user = self.get_user(username)
        if not user:
            return False
        
        # 2. Verify password (standard library)
        if not self.password_hasher.verify(password, user.hash):
            return False
        
        # 3. Verify MFA (standard TOTP)
        if not self.mfa_service.verify(user.secret, mfa_code):
            return False
        
        # 4. Create session
        return self.session_manager.create(user)
    
    def get_user(self, username):
        """Single responsibility - fetch user"""
        pass

print("Principle: Use standard, well-tested libraries instead of custom code")
print("Fewer lines of code = Fewer potential vulnerabilities")
```

### 2.6 Complete Mediation (Total Mediation)

**Definition:** Every access to a resource must be checked against the access control mechanism. There should be no way to bypass the security controls.

**Detailed Explanation:**

Complete Mediation ensures that every request for a protected resource goes through the security checks. This prevents "corner cases" where certain paths might bypass security controls.

**Key Implementation:**
- Check permissions on every access
- Avoid caching permissions permanently
- Validate at every layer (not just entry point)
- Ensure no direct object references

**Real-World Example:**

```python
# Example: Complete Mediation in a file system
class SecureFileSystem:
    """
    Complete Mediation: Every access is checked
    """
    
    def __init__(self):
        self.file_permissions = {}  # filename -> permissions
        self.audit_log = []
    
    def read_file(self, user, filename):
        """
        Complete Mediation: Every read goes through checks
        No shortcuts, no caching permissions permanently
        """
        # ALWAYS check permissions (even for "trusted" users)
        if not self.check_permission(user, filename, 'read'):
            self.audit_log.append(f"DENIED: {user} read {filename}")
            raise PermissionDenied(f"User {user} cannot read {filename}")
        
        # Log the access
        self.audit_log.append(f"ALLOWED: {user} read {filename}")
        
        # Return file content
        return self.get_file_content(filename)
    
    def write_file(self, user, filename, content):
        """Complete Mediation on write operations"""
        # ALWAYS check
        if not self.check_permission(user, filename, 'write'):
            self.audit_log.append(f"DENIED: {user} write {filename}")
            raise PermissionDenied(f"User {user} cannot write {filename}")
        
        self.audit_log.append(f"ALLOWED: {user} wrote {filename}")
        return self.set_file_content(filename, content)
    
    def check_permission(self, user, filename, operation):
        """
        Centralized permission check - called EVERY time
        """
        # Get fresh permissions from authoritative source
        # Do NOT cache permissions long-term
        permissions = self.file_permissions.get(filename)
        
        if permissions is None:
            # Default: deny if no explicit permissions
            return False
        
        return permissions.allows(user, operation)
    
    # WRONG approach (violates Complete Mediation)
    def read_file_unsafe(self, user, filename):
        """VIOLATION: Bypassing checks"""
        # DON'T do this - direct access without checking
        # This creates a vulnerability
        return self.get_file_content(filename)

# Demonstration
fs = SecureFileSystem()
fs.file_permissions = {
    '/data/public.txt': PermissionSet({'alice': ['read'], 'bob': ['read']}),
    '/data/private.txt': PermissionSet({'alice': ['read', 'write']}),
}

# Every access is mediated
print("Alice reads public:", fs.read_file('alice', '/data/public.txt'))
print("Bob writes public:", fs.write_file('bob', '/data/public.txt', 'data'))  # DENIED
print("Complete Mediation ensures no bypass of security checks")
```

### 2.7 Open Design (Kerckhoffs's Principle)

**Definition:** The security of a system should rely on the secrecy of the keys, not the secrecy of the design or algorithm. The design should be open for scrutiny without compromising security.

**Detailed Explanation:**

Also known as Kerckhoffs's Principle (from 19th century cryptography), this principle states that security systems should be secure even if everything about the system is known, except for the key. This is counterintuitive but proven by history—secret algorithms are rarely secure, while open algorithms (like AES, SHA-256) have withstood intense scrutiny.

**Implications:**
- Use standard, public algorithms and protocols
- Security through obscurity alone is insufficient
- Open source can be more secure than closed source
- Keys should be easily changeable when compromised

### 2.8 Least Common Mechanism (Least Shared Mechanism)

**Definition:** Minimize the amount of mechanism common to multiple users. Sharing mechanisms provide potential channels for information flow that could violate security requirements.

**Detailed Explanation:**

This principle addresses the risk of shared resources. When multiple users share a mechanism (like a utility program or shared memory), there's potential for information leakage or interference.

**Applications:**
- Avoid shared temporary files
- Minimize use of shared libraries for sensitive operations
- Consider separate processes for different security domains
- Avoid storing sensitive data in shared locations

### 2.9 Psychological Acceptability (Usability)

**Definition:** Security mechanisms should not unnecessarily impede the use of the system. Security should be transparent to users when possible and not interfere with legitimate work.

**Detailed Explanation:**

Security that is too cumbersome leads users to find workarounds. If security is too intrusive, users will circumvent it. The best security is that which users don't notice but which still protects them.

**Examples:**
- Single Sign-On (SSO) reducing password fatigue
- Auto-save preventing data loss from frequent re-authentication
- Clear security warnings that help users make informed decisions
- Biometric authentication that is faster than passwords

---

## 3. Applying Security Principles: A Case Study

### 3.1 Scenario: Online Examination System

Let's apply all principles to designing a secure online examination system:

```python
class SecureOnlineExamSystem:
    """
    Comprehensive example applying ALL security design principles
    """
    
    def __init__(self):
        # Least Privilege: Different roles with minimal permissions
        self.role_permissions = {
            'student': ['take_exam', 'view_own_results'],
            'teacher': ['create_exam', 'view_student_answers', 'grade'],
            'admin': ['manage_users', 'configure_system', 'view_all']
        }
        
    # DEFENSE IN DEPTH: Multiple security layers
    def login(self, credentials):
        """Layer 1: Authentication"""
        # Rate limiting
        if self.is_rate_limited(credentials['username']):
            raise AccountLockedException()
        
        # Multi-factor authentication
        if not self.verify_mfa(credentials['username'], credentials['mfa']):
            raise AuthenticationFailedException()
        
        # Session creation
        return self.create_secure_session()
    
    def access_exam(self, session, exam_id):
        """Layer 2: Authorization"""
        # Check session validity
        if not session.is_valid():
            raise SessionExpiredException()
        
        # Check exam permissions
        if not session.user.can_access(exam_id):
            raise PermissionDeniedException()
        
        # Environment checks
        if not self.verify_secure_environment():
            raise SecurityException("Insecure exam environment detected")
    
    # SEPARATION OF DUTIES: Different people do different tasks
    def grade_exam(self, exam_submission):
        """Multiple teachers grade; final grade is aggregated"""
        # One teacher cannot unilaterally change grades
        grade1 = TeacherGrade(exam_submission, self.get_teacher1())
        grade2 = TeacherGrade(exam_submission, self.get_teacher2())
        
        # System calculates final grade (not a single person)
        return self.calculate_final_grade(grade1, grade2)
    
    # FAIL SECURE: Default to secure state
    def process_exam_submission(self, submission):
        """On ANY error, submission is preserved, not lost"""
        try:
            return self.submit(submission)
        except Exception as e:
            # Log error but don't lose student's work
            self.save_pending_submission(submission)
            self.notify_administrator(e)
            raise TemporaryFailureException("Submission saved, please retry")
    
    # ECONOMY OF MECHANISM: Simple, well-tested components
    def encrypt_submission(self, data):
        """Use standard AES, not custom encryption"""
        return AESEncryption.encrypt(data, self.get_key())
    
    # COMPLETE MEDIATION: Every access is checked
    def view_exam_result(self, user, exam_id):
        """Every result view is logged and checked"""
        # Cannot bypass - always check
        if not self.check_permission(user, exam_id, 'view_result'):
            raise PermissionDenied()
        
        self.log_access(user, exam_id, 'view_result')
        return self.get_result(user, exam_id)

print("All 9 principles applied in comprehensive system design")
```

---

## 4. Assessment Items

### 4.1 Multiple Choice Questions (Easy)

1. **Which principle states that users should have only the minimum permissions needed?**
   - a) Defense in Depth
   - b) Least Privilege
   - c) Separation of Duties
   - d) Economy of Mechanism
   
   **Answer:** b) Least Privilege

2. **What does "fail secure" mean?**
   - a) System should always be available
   - b) System should fail in a way that maintains security
   - c) System should fail open by default
   - d) System should never fail
   
   **Answer:** b) System should fail in a way that maintains security

3. **Defense in Depth suggests:**
   - a) Using only one strong security mechanism
   - b) Multiple layers of security controls
   - c) Outsourcing security to third parties
   - d) Using the cheapest security solutions
   
   **Answer:** b) Multiple layers of security controls

### 4.2 Short Answer Questions (Medium)

4. **Explain the concept of Separation of Duties with an example from banking.**
   
   **Answer:** Separation of Duties requires that no single individual has complete control over a critical transaction. In banking, for example, one employee may initiate a wire transfer while a different employee must approve it. This prevents fraud as two different people would need to collude to steal funds. For large transactions, multiple approvals may be required.

5. **Why is Complete Mediation important in file systems?**
   
   **Answer:** Complete Mediation ensures that every access to a file goes through the permission check. Without it, there might be code paths that bypass security checks, creating vulnerabilities. For example, if a program can directly read a file without checking permissions, any vulnerability in that code could expose sensitive data.

### 4.3 Scenario-Based Questions (Hard)

6. **You are designing a hospital information system. A doctor needs access to patient records, but nurses only need access to specific sections. Administrators need full access for system management. Apply the principles of Least Privilege and Separation of Duties to design the access control system.**
   
   **Answer:**
   - **Least Privilege:** Create role-based access with granular permissions:
     - Doctors: Can read/write patient medical records, prescribe medications
     - Nurses: Can read vital signs, update basic patient information
     - Administrators: Can manage user accounts, configure system (NOT access medical records)
   - **Separation of Duties:** 
     - Patient admission and discharge should require different staff
     - Prescribing high-risk medications should require dual authorization
     - Access to billing and medical records should be separate roles

7. **A company's web application was breached because an attacker found an API endpoint that bypassed authentication. The endpoint was created during development and forgotten. Which security design principle was violated? How would you fix this?**
   
   **Answer:** 
   - **Violated Principle:** Complete Mediation (every access must be checked) and Economy of Mechanism (simpler code is more secure)
   - **Fix:**
     - Implement Complete Mediation: All API endpoints must go through authentication middleware
     - Apply Economy of Mechanism: Remove unused endpoints, conduct regular audits
     - Use Defense in Depth: Add API gateway authentication in addition to application-level checks
     - Implement Fail Secure: If authentication middleware fails, deny access by default

### 4.4 Application/Coding Questions (Hard)

8. **Write a Python function that implements fail-secure behavior for a banking transfer. The function should deny the transfer on ANY error (database error, network timeout, validation failure).**
   
   ```python
   def secure_transfer(from_account, to_account, amount):
       """
       Fail Secure: Any error results in denied transfer
       """
       try:
           # Attempt to process transfer
           validate_accounts(from_account, to_account)
           verify_sufficient_funds(from_account, amount)
           check_daily_limit(from_account, amount)
           execute_transfer(from_account, to_account)
           return {"status": "success", "message": "Transfer completed"}
       
       except ValidationError as e:
           # FAIL SECURE: Deny on validation error
           log_failure(f"Validation failed: {e}")
           return {"status": "denied", "reason": "Invalid request"}
       
       except InsufficientFundsError as e:
           # FAIL SECURE: Deny on insufficient funds
           log_failure(f"Insufficient funds: {e}")
           return {"status": "denied", "reason": "Insufficient funds"}
       
       except DatabaseError as e:
           # FAIL SECURE: Deny on database error - never proceed
           log_failure(f"Database error: {e}")
           return {"status": "denied", "reason": "System error"}
       
       except Exception as e:
           # FAIL SECURE: Catch-all for ANY unexpected error
           log_failure(f"Unexpected error: {e}")
           return {"status": "denied", "reason": "System error"}
   ```

9. **Design a role-based access control (RBAC) system that follows Least Privilege and Separation of Duties. Include at least 4 roles with specific permissions.**
   
   ```python
   class RBACSystem:
       """
       RBAC implementing Least Privilege and Separation of Duties
       """
       
       ROLES = {
           'viewer': {
               'permissions': ['read_public_data'],
               'description': 'Can only view public information'
           },
           'editor': {
               'permissions': ['read_public_data', 'write_public_data', 
                              'read_draft_content'],
               'description': 'Can edit public content, not published items'
           },
           'publisher': {
               'permissions': ['read_public_data', 'write_public_data',
                              'read_draft_content', 'publish_content'],
               'description': 'Can publish content, cannot create user accounts'
           },
           'admin': {
               'permissions': ['read_public_data', 'manage_users',
                              'configure_system', 'view_audit_logs'],
               'description': 'System administration, cannot publish content'
               # Note: Separation of Duties - admin cannot publish
           }
       }
       
       @staticmethod
       def check_permission(role, required_permission):
           """Least Privilege: Only grant specific permissions"""
           if role not in RBACSystem.ROLES:
               return False
           return required_permission in RBACSystem.ROLES[role]['permissions']
   
   # Demonstration
   print(RBACSystem.check_permission('viewer', 'publish_content'))  # False
   print(RBACSystem.check_permission('publisher', 'publish_content'))  # True
   # Admin cannot publish (Separation of Duties)
   print(RBACSystem.check_permission('admin', 'publish_content'))  # False
   ```

---

## 5. Key Takeaways

### Summary of Security Design Principles

| Principle | Core Concept | Key Question |
|-----------|--------------|---------------|
| **Least Privilege** | Minimum necessary access | Does this user/process need this permission? |
| **Defense in Depth** | Multiple security layers | What happens if one layer fails? |
| **Separation of Duties** | Split critical tasks | Can one person compromise the system? |
| **Fail Secure** | Default to secure on error | What happens when something goes wrong? |
| **Economy of Mechanism** | Simplicity over complexity | Is this as simple as possible? |
| **Complete Mediation** | Check every access | Can anyone bypass the security checks? |
| **Open Design** | Security through keys, not obscurity | Is the system secure if attackers know everything except keys? |
| **Least Common Mechanism** | Minimize shared resources | Could shared mechanisms leak information? |
| **Psychological Acceptability** | Usable security | Does security hinder legitimate work? |

### Delhi University NEP 2024 Syllabus Alignment

This study material covers the following topics from the GE8A Information Security syllabus:
- Security design principles and their importance
- Implementation of security mechanisms
- Real-world application of security concepts
- Assessment of security architectures

### Final Notes

These principles are interdependent—applying one often reinforces others. For instance, implementing Complete Mediation naturally supports Least Privilege, and Fail Secure complements Defense in Depth.

As you progress in your career, remember that security is not a product but a process. These principles provide guidance, but each system requires thoughtful application of these concepts to its specific context and threats.

---

## References

1. Saltzer, J.H., & Schroeder, M.D. (1975). "The Protection of Information in Computer Systems"
2. ISO/IEC 27001:2022 - Information Security Management Systems
3. OWASP Security Design Principles
4. Delhi University BSc (Hons) Computer Science Syllabus, NEP 2024 - GE8A Information Security

---

*Study Material prepared for Delhi University, NEP 2024, BSc Physical Science (CS)*