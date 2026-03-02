# Digital Authentication: Password-Based Security

## Introduction

Authentication is the first line of defense in any computer security system. It verifies the identity of a user, process, or device before granting access to protected resources. Among the various authentication mechanisms, password-based authentication remains the most widely deployed method across organizations worldwide, despite the emergence of biometric and multi-factor authentication systems.

Password-based authentication is a type of knowledge-based authentication where users prove their identity by providing something they know—a secret password. This method has been the cornerstone of access control since the early days of computing. The University of Delhi's Computer Science curriculum emphasizes understanding not only how password authentication works but also its vulnerabilities, best practices for implementation, and modern enhancements that make it more secure.

In this module, we will explore the fundamental concepts of password-based authentication, including how passwords are stored, transmitted, and verified. We will also examine common attack vectors and the countermeasures that security professionals employ to protect password-based systems. Understanding these concepts is crucial for any computer science graduate, as password security forms the foundation of most digital security infrastructure.

## Key Concepts

### 1. Authentication Factors

Password-based authentication falls under the "something you know" category of authentication factors. The three primary authentication factors are:

- **Something you know**: Passwords, PINs, security questions
- **Something you have**: Smart cards, tokens, mobile devices
- **Something you are**: Fingerprints, facial recognition, iris scans

Single-factor authentication uses only one of these factors, while multi-factor authentication (MFA) combines two or more factors for enhanced security.

### 2. Password Storage Mechanisms

Modern systems never store passwords in plaintext. Instead, they employ several cryptographic techniques:

**Salting**: A random value (salt) is generated for each user and combined with the password before hashing. This prevents attackers from using pre-computed rainbow tables and ensures that two users with the same password have different stored values.

**Hashing**: Passwords are transformed using one-way cryptographic hash functions. Popular algorithms include:
- **bcrypt**: Designed specifically for password hashing, includes cost factor for computational complexity
- **Argon2**: Winner of the Password Hashing Competition (2015), resistant to GPU-based attacks
- **PBKDF2**: Widely supported, allows configuration of iteration count

**Key Derivation Functions (KDFs)**: Algorithms like PBKDF2, scrypt, and Argon2 deliberately make hashing computationally expensive to thwart brute-force attacks.

### 3. Password Verification Process

When a user attempts to log in, the system performs these steps:
1. User enters username and password
2. System retrieves the stored salt and hash for that username
3. System computes hash(input_password + salt)
4. System compares computed hash with stored hash
5. Access is granted if they match, denied otherwise

### 4. Password Policies

Effective password policies enforce:
- **Minimum length**: At least 8-12 characters recommended
- **Complexity requirements**: Mix of uppercase, lowercase, numbers, and special characters
- **Expiration periods**: Regular password changes (though this is now debated by security experts)
- **History constraints**: Preventing reuse of recently used passwords
- **Account lockout**: Temporary or permanent lockout after failed attempts

### 5. Common Password Attacks

**Brute Force Attack**: Systematically tries every possible password combination. Defense: Account lockout, CAPTCHA, rate limiting.

**Dictionary Attack**: Uses a list of common words and passwords. Defense: Salting, prohibiting common passwords.

**Rainbow Table Attack**: Uses pre-computed hash tables to reverse cryptographic hashes. Defense: Salting, using strong hashing algorithms.

**Credential Stuffing**: Uses stolen username/password pairs from one site to access other sites. Defense: Different passwords for different sites, MFA.

**Phishing**: Deceptive attempts to trick users into revealing passwords. Defense: User education, two-factor authentication.

### 6. Password Managers

Password managers are applications that securely store and generate complex passwords. They encrypt the password vault with a master password, allowing users to maintain unique, strong passwords for each service without remembering them all. Popular options include LastPass, 1Password, Bitwarden, and KeePass.

## Examples

### Example 1: Understanding Salt and Hash

**Problem**: User "alice" has password "secure123". Explain how the system stores this password securely.

**Solution**:

**Step 1: Generate Salt**
The system generates a random 16-byte salt: `s3cur3_s4lt_2024`

**Step 2: Combine Password and Salt**
The system concatenates: `"secure123" + "s3cur3_s4lt_2024"` = `"secure123s3cur3_s4lt_2024"`

**Step 3: Hash the Combined String**
Using bcrypt with cost factor 10:
`hash = bcrypt("secure123s3cur3_s4lt_2024", cost=10)`

**Step 4: Store**
The system stores in the database:
```
Username: alice
Salt: s3cur3_s4lt_2024
Hash: $2b$10$dHJF9KXJ7VHZPVxGKX8mCe... (60-character hash)
```

**Why this is secure**: Even if another user has the same password "secure123", they will have a different salt and thus a completely different hash value. An attacker cannot use a pre-computed rainbow table.

### Example 2: Implementing Password Verification

**Problem**: Write pseudocode for a secure password verification function.

**Solution**:

```python
function verifyPassword(inputPassword, storedSalt, storedHash):
    # Step 1: Combine input password with stored salt
    combined = concatenate(inputPassword, storedSalt)
    
    # Step 2: Hash the combined string using bcrypt
    computedHash = bcryptHash(combined, cost=12)
    
    # Step 3: Use constant-time comparison to prevent timing attacks
    result = constantTimeCompare(computedHash, storedHash)
    
    # Step 4: Return boolean result
    return result
```

**Key security considerations**:
- Constant-time comparison prevents timing attacks where attackers measure response time to deduce the hash
- High cost factor (12) makes brute-force attacks computationally expensive
- Salt is stored alongside the hash (not secret, but unique per user)

### Example 3: Analyzing a Password Policy

**Problem**: A company implements this password policy: minimum 8 characters, must contain uppercase, lowercase, and number, expires every 30 days, cannot reuse last 5 passwords. Evaluate this policy.

**Solution**:

**Strengths**:
- Minimum length ensures basic complexity
- Character requirements increase entropy
- Password history prevents rapid cycling through common passwords

**Weaknesses**:
- **30-day expiration causes user behavior problems**: Users tend to make minor changes like "Password1" → "Password2", making passwords predictable
- **No special character requirement**: Still allows common patterns
- **Creates security fatigue**: Frequent changes lead to weaker passwords
- **No dictionary check**: Doesn't prevent common passwords like "Welcome123"

**Recommendations**:
1. Increase minimum length to 12+ characters
2. Add special character requirement
3. Implement cracklib/dictionary checking to prohibit common passwords
4. Consider moving to 90-day expiration or remove expiration entirely (NIST guidelines)
5. Implement MFA to reduce password dependency

## Exam Tips

1. **Remember the three authentication factors**: Something you know, something you have, something you are. Passwords fall under "something you know."

2. **Never store passwords in plaintext**: This is a fundamental security principle. Always use salted hashes with modern algorithms like bcrypt or Argon2.

3. **Understand why salting prevents rainbow table attacks**: Salting adds random data before hashing, making pre-computed tables useless since each hash requires its own computation.

4. **Know the difference between hashing and encryption**: Hashing is one-way (cannot be reversed); encryption is two-way (can be decrypted with a key). Passwords must be hashed, not encrypted.

5. **Constant-time comparison is essential**: Use constant-time algorithms for comparing hashes to prevent timing attacks that can leak information about the password.

6. **NIST 2017 guidelines recommend**: Minimum 8 characters (64 max), no complexity rules, no mandatory expiration, check against compromised password databases.

7. **Understand credential stuffing**: Attackers use leaked credentials from one site to try on other sites. This is why using unique passwords for each service is critical.

8. **Multi-factor authentication enhances security significantly**: Even if a password is compromised, attackers cannot access the account without the second factor (like a mobile device).

9. **Password managers solve the password reuse problem**: They allow users to have unique, complex passwords for every service without memorization burden.

10. **Common attack vectors to remember**: Brute force, dictionary attacks, rainbow tables, phishing, and shoulder surfing are the primary methods attackers use to compromise passwords.