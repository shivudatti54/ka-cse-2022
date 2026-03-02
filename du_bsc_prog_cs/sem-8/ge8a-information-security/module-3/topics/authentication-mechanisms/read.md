# Authentication Mechanisms

## Comprehensive Study Material for GE8A Information Security

### BSc Physical Science (CS) – Delhi University, NEP 2024

---

## Table of Contents

1. [Introduction to Authentication](#1-introduction-to-authentication)
2. [Fundamentals of Authentication](#2-fundamentals-of-authentication)
3. [Password-Based Authentication](#3-password-based-authentication)
4. [Multi-Factor Authentication (MFA)](#4-multi-factor-authentication-mfa)
5. [Password Hashing and Storage](#5-password-hashing-and-storage)
6. [Certificate-Based Authentication](#6-certificate-based-authentication)
7. [Biometric Authentication](#7-biometric-authentication)
8. [Session Management](#8-session-management)
9. [OAuth 2.0](#9-oauth-20)
10. [SAML (Security Assertion Markup Language)](#10-saml-security-assertion-markup-language)
11. [Kerberos Authentication Protocol](#11-kerberos-authentication-protocol)
12. [Real-World Examples and Implementation](#12-real-world-examples-and-implementation)
13. [Assessment Questions](#13-assessment-questions)
14. [Key Takeaways](#14-key-takeaways)

---

## 1. Introduction to Authentication

### What is Authentication?

Authentication is the process of verifying the identity of a user, device, or system before granting access to protected resources. It answers the fundamental question: **"Who are you?"** and forms the first line of defense in any security system.

### Real-World Relevance

In today's digital landscape, authentication mechanisms protect:

- **Banking transactions** - Your ATM card and PIN verify your identity before allowing withdrawals
- **Social media accounts** - Login credentials protect your personal data
- **E-commerce platforms** - Authentication prevents unauthorized purchases
- **Corporate networks** - Employees authenticate to access confidential business data
- **Government services** - Aadhaar and digital identity systems rely on robust authentication

For Delhi University students, understanding authentication is crucial because:

1. It is a core topic in the GE8A Information Security syllabus under NEP 2024
2. Cybersecurity careers require deep understanding of authentication mechanisms
3. Every software application students build will require authentication
4. Modern cloud services and DevOps roles demand expertise in authentication protocols

### Authentication vs. Authorization

| Aspect | Authentication | Authorization |
|--------|---------------|---------------|
| Question | "Who are you?" | "What can you access?" |
| Process | Identity verification | Access control |
| Example | Entering password | Checking user permissions |
| Phase | First (before authorization) | Second (after authentication) |

---

## 2. Fundamentals of Authentication

Authentication factors are categorized into three main types:

### 2.1 Authentication Factors

**Factor 1: Something You Know**
- Passwords, PINs, security questions
- Knowledge-based authentication

**Factor 2: Something You Have**
- Smart cards, security tokens, mobile phones
- Hardware or software tokens

**Factor 3: Something You Are**
- Fingerprints, facial recognition, iris scans
- Biometric characteristics

**Factor 4: Somewhere You Are**
- Geographic location, IP address
- Location-based authentication

### 2.2 Authentication Strength

The strength of authentication depends on:
- Number of factors used
- Complexity of each factor
- Implementation security
- Resistance to attacks

---

## 3. Password-Based Authentication

### Overview

Password-based authentication is the most common and traditional method where users prove their identity by providing a secret string (password) known only to them.

### How It Works

```
User Registration:
1. User creates account with username/email
2. User enters password
3. System hashes password and stores hash (NOT plaintext)
4. System stores salt for each user

Login Process:
1. User enters username and password
2. System hashes entered password
3. System compares hash with stored hash
4. If match → Access granted; If mismatch → Access denied
```

### Password Policy Best Practices

- Minimum 12 characters (NIST recommends 8+)
- Mix of uppercase, lowercase, numbers, and symbols
- No composition rules (users choose stronger passwords)
- Prevent common passwords (dictionary attacks)
- No periodic password changes without reason
- Allow paste in password fields (managers)

### Vulnerabilities

1. **Brute Force Attacks** - Trying all possible combinations
2. **Dictionary Attacks** - Using common words
3. **Rainbow Table Attacks** - Pre-computed hash tables
4. **Phishing** - Deceptive login pages
5. **Keyloggers** - Malware capturing keystrokes
6. **Shoulder Surfing** - Visual observation

---

## 4. Multi-Factor Authentication (MFA)

### What is MFA?

MFA requires two or more different types of authentication factors, significantly increasing security. Even if an attacker steals a password, they cannot access the account without the additional factors.

### Types of MFA

**Two-Factor Authentication (2FA):**
- Password + SMS code
- Password + Authenticator app
- Password + Hardware token

**Three-Factor Authentication:**
- Password + Fingerprint + Hardware token

### Common MFA Methods

1. **SMS-based 2FA**
   - System sends 6-digit code via SMS
   - Vulnerable to SIM swapping attacks

2. **TOTP (Time-based One-Time Password)**
   - Uses algorithms like TOTP (RFC 6238)
   - Code changes every 30 seconds
   - Google Authenticator, Authy apps

3. **Push Notification**
   - Sends approval request to registered device
   - More secure than SMS

4. **Hardware Tokens**
   - YubiKey, RSA SecurID
   - Most secure but costs money

### MFA Implementation Flow

```
User Login Flow with MFA:
1. User enters username + password
2. Server validates credentials
3. Server prompts for second factor
4. User provides second factor (token, biometric)
5. Server validates second factor
6. If both valid → Grant access
```

---

## 5. Password Hashing and Storage

### Why Hashing?

Storing passwords in plaintext is a critical security flaw. If the database is compromised, all passwords are exposed. **Hashing** transforms passwords into fixed-length strings that cannot be reversed.

### Hashing vs. Encryption

| Hashing | Encryption |
|---------|------------|
| One-way function | Two-way function |
| Cannot recover original | Can decrypt to original |
| Fixed output size | Variable output size |
| Same input = same hash | Same input = different ciphertext (with salt/IV) |

### Salt: Preventing Rainbow Table Attacks

A **salt** is a random value unique to each user, added before hashing:

```python
import hashlib
import secrets

def hash_password(password):
    # Generate unique salt for each user
    salt = secrets.token_hex(16)
    
    # Combine salt and password
    salted_password = salt + password
    
    # Hash with SHA-256
    hash_value = hashlib.sha256(salted_password.encode()).hexdigest()
    
    # Store: salt$hash
    return f"{salt}${hash_value}"

def verify_password(stored_value, entered_password):
    # Split stored value
    salt, stored_hash = stored_value.split('$')
    
    # Hash entered password with same salt
    entered_hash = hashlib.sha256((salt + entered_password).encode()).hexdigest()
    
    # Compare
    return entered_hash == stored_hash

# Example usage
stored = hash_password("SecurePass123!")
print(f"Stored: {stored}")
print(f"Match: {verify_password(stored, 'SecurePass123!')}")
```

### Modern Hashing Algorithms

1. **bcrypt** - Adaptive cost, includes salt
2. **Argon2** - Winner of Password Hashing Competition (2015)
3. **PBKDF2** - Widely used, configurable iterations
4. **scrypt** - Memory-hard function

### Argon2 Implementation

```python
import argon2

def hash_password_argon2(password):
    ph = argon2.PasswordHasher(
        time_cost=2,
        memory_cost=65536,
        parallelism=1,
        hash_len=32,
        salt_len=16
    )
    return ph.hash(password)

def verify_password_argon2(hash_string, password):
    ph = argon2.PasswordHasher()
    try:
        ph.verify(hash_string, password)
        return True
    except:
        return False

# Example
password_hash = hash_password_argon2("MySecurePassword!")
print(f"Hash: {password_hash}")
print(f"Valid: {verify_password_argon2(password_hash, 'MySecurePassword!')}")
```

---

## 6. Certificate-Based Authentication

### Overview

Certificate-based authentication uses digital certificates to verify identity. These certificates are issued by trusted Certificate Authorities (CAs) and contain the user's public key and identity information.

### Components

1. **Digital Certificate** - Electronic document containing:
   - User's public key
   - User's identity information
   - CA's digital signature
   - Validity period
   - Serial number

2. **Certificate Authority (CA)** - Trusted third party that issues certificates
   - Root CAs (top-level)
   - Intermediate CAs

3. **Public Key Infrastructure (PKI)** - Framework for managing certificates

### How Certificate Authentication Works

```
1. User requests certificate from CA
2. CA verifies user's identity
3. CA issues certificate with user's public key
4. User presents certificate during authentication
5. Server verifies:
   - Certificate is signed by trusted CA
   - Certificate is not expired/revoked
   - Certificate matches user identity
6. Access granted
```

### Certificate Types

- **SSL/TLS Certificates** - For websites
- **Client Certificates** - For user authentication
- **Code Signing Certificates** - For software
- **SMIME Certificates** - For email

### Mutual TLS (mTLS)

Both client and server authenticate each other using certificates:

```python
# Python SSL/TLS Server with client certificate verification
import ssl
import socket

# Create SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

# Load server certificate
context.load_cert_chain(
    certfile="server.crt",
    keyfile="server.key"
)

# Require client certificates
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations("ca.crt")

# Bind to port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('0.0.0.0', 8443))
    sock.listen(1)
    
    with context.wrap_socket(sock, server_side=True) as ssock:
        print("Client connected:", ssock.getpeercert())
```

---

## 7. Biometric Authentication

### Overview

Biometric authentication uses unique physiological or behavioral characteristics to verify identity. These include fingerprints, facial recognition, voice patterns, iris scans, and more.

### Types of Biometrics

**Physiological Biometrics:**
- Fingerprint
- Facial recognition
- Iris/retina scan
- Hand geometry

**Behavioral Biometrics:**
- Voice recognition
- Keystroke dynamics
- Gait analysis
- Signature verification

### Advantages and Limitations

| Advantages | Limitations |
|------------|-------------|
| Cannot be forgotten | False acceptance/rejection rates |
| Cannot be shared | Privacy concerns |
| Always available | Spoofing attacks |
| High convenience | Physical changes (aging, injury) |
| Difficult to forge | Cost of implementation |

### Implementation Considerations

1. **False Acceptance Rate (FAR)** - Probability of unauthorized access
2. **False Rejection Rate (FRR)** - Probability of denying legitimate user
3. **Equal Error Rate (EER)** - Point where FAR = FRR
4. **Liveness Detection** - Prevent fake biometrics (photos, molds)

### Facial Recognition Example

```python
# Simple conceptual example using face_recognition library
import face_recognition
import numpy as np

# Load known faces
def load_known_faces():
    # Load and encode known images
    known_encodings = []
    known_names = []
    
    # Load multiple known faces
    obama_image = face_recognition.load_image_file("obama.jpg")
    obama_encoding = face_recognition.face_encodings(obama_image)[0]
    known_encodings.append(obama_encoding)
    known_names.append("Barack Obama")
    
    return known_encodings, known_names

def authenticate_user(image_path, known_encodings, known_names):
    # Load unknown image
    unknown_image = face_recognition.load_image_file(image_path)
    unknown_encodings = face_recognition.face_encodings(unknown_image)
    
    if len(unknown_encodings) == 0:
        return "No face detected", False
    
    # Compare with known faces
    for unknown_encoding in unknown_encodings:
        matches = face_recognition.compare_faces(
            known_encodings, 
            unknown_encoding
        )
        
        if True in matches:
            matched_name = known_names[matches.index(True)]
            return f"Authenticated as: {matched_name}", True
    
    return "Unknown user", False

# Usage
encodings, names = load_known_faces()
result, success = authenticate_user("test_face.jpg", encodings, names)
print(result)
```

---

## 8. Session Management

### What is Session Management?

After authentication, applications create sessions to maintain user state. Session management handles creating, maintaining, and terminating these sessions securely.

### Session Token Generation

```python
import secrets
import time

def generate_session_token():
    """Generate cryptographically secure session token"""
    return secrets.token_urlsafe(32)

def create_session(user_id):
    """Create session for authenticated user"""
    session_id = generate_session_token()
    session_data = {
        'user_id': user_id,
        'created_at': time.time(),
        'last_activity': time.time(),
        'ip_address': None,  # Set from request
        'user_agent': None   # Set from request
    }
    return session_id, session_data

# Example session creation
session_token, session = create_session(user_id=12345)
print(f"Session Token: {session_token}")
print(f"Session Data: {session}")
```

### Session Security Best Practices

1. **Use secure, random tokens** - `secrets.token_urlsafe()` in Python
2. **Set HttpOnly cookies** - Prevent JavaScript access (XSS protection)
3. **Set Secure cookies** - Only send over HTTPS
4. **Implement session timeout** - Auto-expire after inactivity
5. **Regenerate session ID** - After authentication (prevent fixation)
6. **Store sessions securely** - Server-side, encrypted if possible

### Session Fixation vs. Session Hijacking

**Session Fixation:**
- Attacker obtains a session ID
- Tricks victim into using this ID
- After victim logs in, attacker uses same ID

**Prevention:**
```python
def login_user(user_id):
    """Login with session regeneration"""
    # Invalidate old session
    if 'session_id' in session:
        delete_session(session['session_id'])
    
    # Create new session
    new_session_id = generate_session_token()
    session['session_id'] = new_session_id
    session['user_id'] = user_id
    
    return new_session_id
```

### Session Timeout Implementation

```python
import time

SESSION_TIMEOUT = 1800  # 30 minutes

def is_session_valid(session):
    """Check if session is still valid"""
    current_time = time.time()
    last_activity = session.get('last_activity', 0)
    
    # Check timeout
    if current_time - last_activity > SESSION_TIMEOUT:
        return False
    
    # Update last activity
    session['last_activity'] = current_time
    return True

def check_session(request, session):
    """Middleware to check session validity"""
    if not is_session_valid(session):
        # Clear session
        clear_session(session)
        return False, "Session expired"
    
    return True, "Valid session"
```

---

## 9. OAuth 2.0

### Overview

OAuth 2.0 is an authorization framework that enables applications to obtain limited access to user accounts on third-party services. It delegates user authentication to the service hosting the account.

### Key Concepts

- **Resource Owner** - The user
- **Client** - Application requesting access
- **Authorization Server** - Handles authentication
- **Resource Server** - Hosts protected resources
- **Access Token** - Short-lived token granting access
- **Refresh Token** - Long-lived token to obtain new access tokens

### OAuth 2.0 Flow

```
1. User clicks "Login with Google"
2. Application redirects to Google's authorization server
3. User logs in to Google (if not already logged in)
4. Google asks: "Allow [App] to access your profile?"
5. User approves
6. Google redirects back to app with authorization code
7. App exchanges code for access token
8. App uses access token to fetch user profile
9. User is logged in
```

### OAuth Implementation Example

```python
import requests
from urllib.parse import urlencode

# OAuth 2.0 Configuration
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://localhost:8000/callback"
AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
SCOPES = ["openid", "email", "profile"]

def get_authorization_url():
    """Generate authorization URL for user redirect"""
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "access_type": "offline"  # Get refresh token
    }
    return f"{AUTH_URL}?{urlencode(params)}"

def exchange_code_for_tokens(code):
    """Exchange authorization code for access token"""
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI
    }
    
    response = requests.post(TOKEN_URL, data=data)
    return response.json()

def get_user_info(access_token):
    """Fetch user information using access token"""
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers=headers
    )
    return response.json()

# Usage Flow
# 1. Redirect user to get_authorization_url()
# 2. Get authorization code from redirect
# 3. Exchange code for tokens
# tokens = exchange_code_for_tokens(authorization_code)
# 4. Get user info
# user = get_user_info(tokens['access_token'])
# print(f"Logged in as: {user['email']}")
```

### OAuth Security Considerations

- Use PKCE (Proof Key for Code Exchange) for public clients
- Validate redirect URIs strictly
- Keep client secrets secure
- Use short-lived access tokens
- Implement refresh token rotation

---

## 10. SAML (Security Assertion Markup Language)

### Overview

SAML is an XML-based standard for exchanging authentication and authorization data between parties, commonly used in Single Sign-On (SSO) implementations for enterprise applications.

### SAML Components

1. **Identity Provider (IdP)** - Authenticates users (e.g., Okta, Active Directory)
2. **Service Provider (SP)** - Application user wants to access
3. **SAML Assertion** - XML document containing authentication result

### SAML Authentication Flow

```
1. User tries to access Service Provider (SP)
2. SP detects user not authenticated
3. SP redirects to Identity Provider (IdP) with SAML Request
4. User authenticates with IdP
5. IdP sends SAML Response (containing assertion) to SP
6. SP validates assertion
7. User accesses SP
```

### SAML Assertion Structure

```xml
<saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
                ID="_some_unique_id"
                Version="2.0"
                IssueInstant="2024-01-15T10:00:00Z">
    
    <saml:Issuer>https://idp.example.com</saml:Issuer>
    
    <saml:Subject>
        <saml:NameID>user@example.com</saml:NameID>
    </saml:Subject>
    
    <saml:Conditions NotBefore="2024-01-15T10:00:00Z"
                     NotOnOrAfter="2024-01-15T11:00:00Z">
    </saml:Conditions>
    
    <saml:AuthnStatement AuthnInstant="2024-01-15T10:00:00Z">
        <saml:AuthnContext>
            <saml:AuthnContextClassRef>
                urn:oasis:names:tc:SAML:2.0:ac:classes:Password
            </saml:AuthnContextClassRef>
        </saml:AuthnContext>
    </saml:AuthnStatement>
    
    <saml:AttributeStatement>
        <saml:Attribute Name="email">
            <saml:AttributeValue>user@example.com</saml:AttributeValue>
        </saml:Attribute>
    </saml:AttributeStatement>
    
</saml:Assertion>
```

### SAML vs OAuth 2.0

| Aspect | SAML | OAuth 2.0 |
|--------|------|-----------|
| Format | XML | JSON |
| Size | Larger | Smaller |
| Complexity | More complex | Simpler |
| Use Case | Enterprise SSO | API access, Mobile apps |
| Token Type | SAML Assertion | Access Token |
| Browser | Browser-based | More flexible |

---

## 11. Kerberos Authentication Protocol

### Overview

Kerberos is a network authentication protocol designed for client-server applications, using symmetric-key cryptography. It's the default authentication for Windows Active Directory domains.

### Key Concepts

- **Ticket-Granting Ticket (TGT)** - Initial ticket from KDC
- **Ticket-Granting Server (TGS)** - Issues service tickets
- **Key Distribution Center (KDC)** - Central authentication server
- **Principal** - User or service identity
- **Realm** - Kerberos domain

### Kerberos Authentication Flow

```
1. User logs in to workstation
2. Client requests TGT from KDC
3. KDC verifies credentials, issues TGT
4. Client stores TGT (encrypted with user key)

5. User wants to access service (e.g., file server)
6. Client sends TGT to TGS with service name
7. TGS verifies TGT, issues service ticket
8. Client presents service ticket to service
9. Service validates ticket, grants access
```

### Kerberos Messages

```
AS-REQ: Client → KDC (Authentication Service Request)
AS-REP: KDC → Client (Authentication Service Reply)
TGS-REQ: Client → KDC (Ticket-Granting Service Request)
TGS-REP: KDC → Client (Ticket-Granting Service Reply)
AP-REQ: Client → Service (Application Request)
AP-REP: Service → Client (Application Reply)
```

### Kerberos Advantages

1. **Mutual Authentication** - Both client and server verify each other
2. **Single Sign-On** - One login accesses multiple services
3. **Secure Tickets** - Encrypted, time-limited credentials
4. **No Password Transmitted** - Never sent over network

### Kerberos Security Considerations

- KDC is single point of failure
- Requires time synchronization (within 5 minutes)
- Vulnerable to password brute force if compromised
- Must protect TGT (ticket-granting ticket)

---

## 12. Real-World Examples and Implementation

### Example 1: Complete Login System with Password Hashing

```python
import hashlib
import secrets
import time
from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class User:
    username: str
    password_hash: str
    salt: str
    email: str

class SecureAuthSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.sessions: Dict[str, Dict] = {}
    
    def hash_password(self, password: str, salt: str) -> str:
        """Hash password with salt using SHA-256"""
        combined = salt + password
        for _ in range(100000):  # Iterations for key stretching
            combined = hashlib.sha256(combined.encode()).hexdigest()
        return combined
    
    def register(self, username: str, password: str, email: str) -> bool:
        """Register new user"""
        if username in self.users:
            return False
        
        # Generate unique salt
        salt = secrets.token_hex(16)
        
        # Hash password
        password_hash = self.hash_password(password, salt)
        
        # Store user
        self.users[username] = User(username, password_hash, salt, email)
        return True
    
    def login(self, username: str, password: str) -> Optional[str]:
        """Authenticate user and create session"""
        if username not in self.users:
            return None
        
        user = self.users[username]
        password_hash = self.hash_password(password, user.salt)
        
        if password_hash != user.password_hash:
            return None
        
        # Create session
        session_token = secrets.token_urlsafe(32)
        self.sessions[session_token] = {
            'username': username,
            'created_at': time.time(),
            'last_activity': time.time()
        }
        
        return session_token
    
    def verify_session(self, session_token: str) -> Optional[str]:
        """Verify session and return username"""
        if session_token not in self.sessions:
            return None
        
        session = self.sessions[session_token]
        
        # Check timeout (30 minutes)
        if time.time() - session['last_activity'] > 1800:
            del self.sessions[session_token]
            return None
        
        # Update last activity
        session['last_activity'] = time.time()
        
        return session['username']
    
    def logout(self, session_token: str):
        """Terminate session"""
        if session_token in self.sessions:
            del self.sessions[session_token]

# Example Usage
auth = SecureAuthSystem()

# Register
auth.register("student1", "SecurePass123!", "student@du.ac.in")
print("User registered successfully")

# Login
token = auth.login("student1", "SecurePass123!")
print(f"Login successful, token: {token[:20]}...")

# Verify session
username = auth.verify_session(token)
print(f"Session valid for: {username}")

# Logout
auth.logout(token)
print("Logged out")
```

### Example 2: Flask Application with MFA

```python
from flask import Flask, request, session, jsonify
import secrets
import pyotp
import hashlib

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# In-memory storage (use database in production)
users = {}
mfa_secrets = {}

def hash_password(password):
    """Simple password hash (use bcrypt in production)"""
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']
    
    if username in users:
        return jsonify({'error': 'User exists'}), 400
    
    # Store user with hashed password
    users[username] = hash_password(password)
    
    # Generate MFA secret
    mfa_secret = pyotp.random_base32()
    mfa_secrets[username] = mfa_secret
    
    # Generate QR code URI for authenticator apps
    totp_uri = pyotp.totp.TOTP(mfa_secret).provisioning_uri(
        name=username,
        issuer_name="DU Security App"
    )
    
    return jsonify({
        'message': 'User registered',
        'mfa_secret': mfa_secret,
        'setup_uri': totp_uri
    })

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    mfa_code = data.get('mfa_code')
    
    # Verify password
    if users.get(username) != hash_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401
    
    # Verify MFA if enabled
    if username in mfa_secrets:
        if not mfa_code:
            return jsonify({'mfa_required': True}), 200
        
        totp = pyotp.TOTP(mfa_secrets[username])
        if not totp.verify(mfa_code):
            return jsonify({'error': 'Invalid MFA code'}), 401
    
    # Create session
    session['user'] = username
    return jsonify({'message': 'Login successful'})

@app.route('/protected', methods=['GET'])
def protected():
    if 'user' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    return jsonify({
        'message': 'Access granted',
        'user': session['user']
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

## 13. Assessment Questions

### Multiple Choice Questions (20 Questions)

1. **Which of the following is NOT an authentication factor?**
   - a) Something you know
   - b) Something you have
   - c) Something you want
   - d) Something you are

2. **What does MFA stand for?**
   - a) Multiple Factor Authentication
   - b) Multi-Factor Authentication
   - c) Main Factor Authentication
   - d) Manual Factor Authentication

3. **Which hashing algorithm was winner of the Password Hashing Competition?**
   - a) bcrypt
   - b) SHA-256
   - c) Argon2
   - d) PBKDF2

4. **In OAuth 2.0, what token is used to access protected resources?**
   - a) Authorization Code
   - b) Refresh Token
   - c) Access Token
   - d) Identity Token

5. **What is the purpose of a salt in password hashing?**
   - a) To encrypt the password
   - b) To make rainbow table attacks ineffective
   - c) To verify the password
   - d) To store the password

6. **Which protocol is commonly used for Single Sign-On in enterprises?**
   - a) OAuth 2.0
   - b) SAML
   - c) Kerberos
   - d) All of the above

7. **What is session fixation?**
   - a) Stealing a session token
   - b) Setting a known session ID before user logs in
   - c) Expiring a session
   - d) Creating multiple sessions

8. **Which is NOT a biometric authentication method?**
   - a) Fingerprint
   - b) Password
   - c) Facial recognition
   - d) Iris scan

9. **In Kerberos, what does KDC stand for?**
   - a) Key Distribution Center
   - b) Kerberos Data Center
   - c) Key Data Controller
   - d) Kernel Data Cache

10. **What is the purpose of a digital certificate?**
    - a) To encrypt data
    - b) To verify identity using public key cryptography
    - c) To store passwords
    - d) To manage sessions

11. **Which HTTP flag prevents XSS from accessing session cookies?**
    - a) Secure
    - b) HttpOnly
    - c) SameSite
    - d) All of the above

12. **What type of attack uses pre-computed hash tables?**
    - a) Brute force
    - b) Rainbow table
    - c) Dictionary
    - d) Phishing

13. **In SAML, which entity authenticates the user?**
    - a) Service Provider
    - b) Identity Provider
    - c) Certificate Authority
    - d) Relying Party

14. **What is the recommended minimum password length according to NIST?**
    - a) 6 characters
    - b) 8 characters
    - c) 12 characters
    - d) 16 characters

15. **Which OAuth 2.0 flow is recommended for mobile apps?**
    - a) Authorization Code
    - b) Implicit
    - c) PKCE
    - d) Client Credentials

16. **What does TOTP stand for?**
    - a) Time-based One-Time Password
    - b) Token-based One-Time Password
    - c) Temporary One-Time Password
    - d) Transferable One-Time Password

17. **Which is a disadvantage of biometric authentication?**
    - a) Cannot be forgotten
    - b) Privacy concerns
    - c) Always available
    - d) Easy to implement

18. **What is mutual TLS?**
    - a) TLS with two servers
    - b) Both client and server authenticate each other
    - c) TLS with two certificates
    - d) Two-way encryption

19. **In Kerberos, what is a principal?**
    - a) Authentication server
    - b) User or service identity
    - c) Encryption key
    - d) Ticket

20. **What should be done after successful login to prevent session fixation?**
    - a) Keep same session ID
    - b) Regenerate session ID
    - c) Delete session
    - d) Share session

### Fill in the Blanks (10 Questions)

1. The three main authentication factors are knowledge, possession, and ______________.

2. A ______________ is a random value added to passwords before hashing to prevent rainbow table attacks.

3. In OAuth 2.0, the token used to obtain new access tokens is called ______________.

4. SAML stands for Security ______________ Markup Language.

5. The KDC in Kerberos issues tickets called ______________ tickets.

6. HttpOnly cookies cannot be accessed by ______________.

7. The EER in biometrics stands for Equal ______________ Rate.

8. PKCE is used with OAuth 2.0 for ______________ clients.

9. TOTP codes typically change every ______________ seconds.

10. The False Acceptance Rate in biometrics measures ______________ access probability.

### Short Answer Questions (10 Questions)

1. Explain the difference between authentication and authorization.

2. Describe how password hashing with salt prevents rainbow table attacks.

3. List three best practices for secure session management.

4. Compare OAuth 2.0 and SAML in terms of their primary use cases.

5. Explain the Kerberos authentication flow in brief.

6. What are the advantages of multi-factor authentication over single-factor?

7. Describe how TOTP (Time-based OTP) works.

8. What is the purpose of HttpOnly and Secure flags in cookies?

9. Explain the concept of mutual TLS authentication.

10. Discuss the security considerations when implementing biometric authentication.

### Long Answer Questions (5 Questions)

1. **Q:** Describe the complete authentication process in OAuth 2.0, including all the tokens involved and their purposes. Also explain two security improvements that should be implemented.

2. **Q:** A company wants to implement Single Sign-On (SSO) for their employees. Compare and contrast SAML and OAuth 2.0 for this use case, and recommend which one they should use with justification.

3. **Q:** Explain the working of Kerberos authentication protocol, including the role of TGT, TGS, and KDC. Also discuss its advantages and limitations.

4. **Q:** Design a secure authentication system for a banking application that requires:
   - Password-based authentication
   - Multi-factor authentication using TOTP
   - Secure session management
   - Protection against common attacks (brute force, session hijacking)

5. **Q:** Discuss the various password hashing algorithms and explain why Argon2 is recommended over older algorithms like MD5 and SHA-1. Include code examples of proper password hashing implementation.

### Flashcards (15 Key Terms)

| Term | Definition |
|------|------------|
| Authentication | Process of verifying identity of a user |
| Authorization | Process of determining what a user can access |
| MFA | Authentication using multiple factors |
| Salt | Random value added to passwords before hashing |
| OAuth 2.0 | Authorization framework for delegated access |
| SAML | XML-based standard for SSO |
| Kerberos | Network authentication protocol using tickets |
| Session | Server-side storage of user authentication state |
| TOTP | Time-based one-time password algorithm |
| Biometrics | Authentication using physical/behavioral traits |
| PKI | Public Key Infrastructure for certificates |
| CA | Certificate Authority that issues certificates |
| HttpOnly | Cookie flag preventing JavaScript access |
| TGT | Ticket-Granting Ticket in Kerberos |
| FAR | False Acceptance Rate in biometrics |

---

## 14. Key Takeaways

### Core Concepts

1. **Authentication verifies identity** - It answers "Who are you?" while authorization answers "What can you do?"

2. **Authentication factors** - Three main types: something you know (password), something you have (token), something you are (biometrics)

3. **Password security** - Always hash passwords with unique salts; never store plaintext; use modern algorithms like Argon2 or bcrypt

4. **MFA is essential** - Multi-factor authentication significantly reduces account compromise even when passwords are leaked

5. **Session security** - Generate random session IDs, use HttpOnly/Secure flags, implement timeouts, regenerate after login

### Protocol Comparison

| Protocol | Primary Use | Format | Best For |
|----------|-------------|--------|----------|
| OAuth 2.0 | Authorization | JSON | API access, mobile apps |
| SAML | SSO | XML | Enterprise single sign-on |
| Kerberos | Network auth | Tickets | Windows Active Directory |

### Implementation Best Practices

1. **Never store plaintext passwords** - Always hash with salt
2. **Use HTTPS everywhere** - Never transmit credentials unencrypted
3. **Implement rate limiting** - Prevent brute force attacks
4. **Use secure session tokens** - Cryptographically random
5. **Enable MFA** - Especially for sensitive accounts
6. **Validate certificates** - In certificate-based auth
7. **Implement proper logout** - Clear all session data

### Common Attacks to Protect Against

- Brute force attacks → Rate limiting, account lockout
- Rainbow tables → Use unique salts
- Session hijacking → HttpOnly, Secure flags, regeneration
- Phishing → User education, MFA
- Credential stuffing → Unique passwords, MFA
- Session fixation → Regenerate session after login

### Delhi University NEP 2024 Focus Areas

From the GE8A Information Security syllabus:
- Understanding authentication mechanisms is crucial for exam success
- Focus on password hashing, MFA, OAuth, and session management
- Know the differences between authentication protocols
- Be able to explain security considerations for each mechanism
- Practice implementation examples as seen in this material

---

*Document prepared for BSc Physical Science (CS), Delhi University, NEP 2024*
*Subject: GE8A Information Security - Authentication Mechanisms*

**Word Count: Approximately 3,200 words**