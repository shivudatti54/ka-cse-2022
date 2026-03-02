# Identity and Credential Management

## Introduction

Identity and Credential Management forms the cornerstone of modern information security systems. In an era where digital transactions, cloud services, and interconnected systems dominate organizational infrastructure, the ability to accurately verify user identities and securely manage their credentials has become paramount. For students pursuing Computer Science at the University of Delhi, understanding this domain is essential not only for academic success but also for building robust security solutions in their professional careers.

Identity Management (IdM) encompasses the policies, processes, and technologies that establish, maintain, and terminate user identities across an enterprise. Credential Management, a subset of IdM, deals specifically with the creation, storage, validation, and lifecycle management of authentication credentials such as passwords, digital certificates, tokens, and biometric data. Together, these disciplines address the fundamental security question: "Is the user who they claim to be?"

The significance of identity and credential management extends far beyond simple password handling. In the context of DU's B.Sc. (H) Computer Science curriculum, this topic connects to broader concepts including cryptography, network security, access control models, and secure software development. With cyberattacks becoming increasingly sophisticated—leveraging phishing, credential stuffing, and identity theft—organizations face unprecedented challenges in protecting their digital assets. Effective identity and credential management serves as the first line of defense against unauthorized access.

## Key Concepts

### Digital Identity

A digital identity represents an individual or entity in the digital realm. It consists of attributes that collectively define a user, including username, email, employee ID, role, department, and behavioral patterns. Digital identities can be user-centric (controlled by the individual), organization-centric (managed by enterprises), or device-centric (associated with IoT devices). Understanding the distinction between identity, authentication, and authorization is crucial: identity answers "who are you?", authentication proves "are you really who you claim to be?", and authorization determines "what can you do?"

### Authentication Factors

Authentication methods are categorized into three primary factors:

1. **Something You Know**: Passwords, PINs, security questions. These are the most common but vulnerable to guessing, phishing, and shoulder surfing.

2. **Something You Have**: Smart cards, hardware tokens (RSA SecurID, YubiKey), software tokens, mobile phones. These provide additional security through physical possession.

3. **Something You Are**: Biometric modalities including fingerprint, facial recognition, iris scanning, voice recognition, and behavioral biometrics (keystroke dynamics, gait analysis).

Multi-Factor Authentication (MFA) combines two or more factors, significantly enhancing security. The principle of defense in depth dictates that compromising multiple independent authentication factors is substantially more difficult than breaking a single factor.

### Credential Storage and Security

Storing credentials securely is critical. Plaintext storage is unacceptable—compromised databases expose all user credentials. The standard approach involves:

- **Salting**: Adding random data (salt) before hashing to prevent rainbow table attacks
- **Bcrypt, Argon2, PBKDF2**: Modern key derivation functions designed to resist brute-force attacks through computational complexity
- **Hashing**: One-way functions like SHA-256 that transform passwords into fixed-length digests

Password-based key derivation functions (PBKDF2, Argon2) incorporate salting and iterative hashing to make brute-force attacks computationally expensive. Argon2, winner of the Password Hashing Competition (2015), is particularly recommended for modern applications due to its memory-hard properties.

### Access Control Models

Identity management integrates closely with access control:

- **DAC (Discretionary Access Control)**: Owners discretionarily grant access to resources
- **MAC (Mandatory Access Control)**: System enforces access based on classification levels (military, government use)
- **RBAC (Role-Based Access Control)**: Access permissions based on organizational roles—most common in enterprise environments
- **ABAC (Attribute-Based Access Control)**: Access decisions based on user attributes, resource attributes, and environmental conditions

RBAC simplifies administration by assigning permissions to roles rather than individual users. When employees change roles, their access rights are updated by changing role assignments.

### Identity Federation and SSO

Single Sign-On (SSO) allows users to authenticate once and access multiple applications. Federation extends SSO across organizational boundaries using trust relationships. Key protocols include:

- **SAML 2.0**: XML-based framework for exchanging authentication and authorization data
- **OpenID Connect**: OAuth 2.0-based identity layer providing authentication
- **OAuth 2.0**: Authorization framework enabling third-party access without sharing credentials

These protocols enable scenarios where users from one organization can access resources in another without separate credentials, while maintaining security and privacy.

### Credential Lifecycle Management

Credentials require comprehensive lifecycle management:

1. **Creation**: Enforcing password complexity, issuing certificates, provisioning tokens
2. **Storage**: Secure hashing, certificate storage in hardware security modules (HSMs)
3. **Usage**: Monitoring for anomalies, session management, credential masking
4. **Rotation**: Regular password changes, certificate renewal, token reissuance
5. **Termination**: Prompt revocation upon employment termination or role change

## Examples

### Example 1: Implementing Secure Password Storage

Consider a web application storing user passwords. The developer must implement proper hashing:

```python
import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Usage
password = "SecureP@ssw0rd!"
hashed_pw = hash_password(password)
# Store hashed_pw in database

# Verification during login
if verify_password(password, hashed_pw):
    print("Authentication successful")
```

This implementation uses bcrypt with automatic salting, making rainbow table attacks ineffective. For enhanced security, applications should also implement rate limiting to prevent brute-force attacks.

### Example 2: Designing RBAC for a University System

A DU college needs to implement access control for its examination system:

| Role | Permissions |
|------|-------------|
| Student | View own marks, register for courses |
| Professor | Enter marks, view course students |
| Department Head | Approve grades, generate reports |
| Admin | Manage users, configure system |

Using RBAC, when a teaching assistant is appointed:
- Create TA role with appropriate permissions
- Assign the user to the TA role
- User inherits all TA permissions automatically

When the TA becomes a permanent professor:
- Remove TA role assignment
- Add Professor role
- Access rights update automatically

This approach reduces administrative overhead and improves security through consistent permission management.

### Example 3: OAuth 2.0 Authorization Flow

When a user logs into a third-party application using Google:

1. **User** clicks "Login with Google"
2. **Application** redirects to Google's authorization server with client_id and requested scopes
3. **User** authenticates with Google and consents to share requested information
4. **Google** redirects back to application with authorization code
5. **Application** exchanges code for access token (and optionally refresh token)
6. **Application** uses access token to request user profile from Google

This flow never exposes the user's Google credentials to the third-party application, enhancing security while enabling convenient authentication.

## Exam Tips

1. **Distinguish between Identification, Authentication, and Authorization**: Identification presents identity (username), authentication proves identity (password), and authorization defines access rights. Exams frequently test these conceptual distinctions.

2. **MFA Implementation**: Understand why multi-factor authentication using two factors from the same category (e.g., two passwords) provides weaker security than factors from different categories.

3. **Password Hashing Algorithms**: Know the properties of bcrypt, Argon2, and PBKDF2—specifically why simple hashing (SHA-256) without salting or iteration is insecure for password storage.

4. **OAuth vs. OpenID Connect vs. SAML**: Remember that OAuth is for authorization (what you can do), OpenID Connect adds authentication (who you are) on top of OAuth, and SAML is an older XML-based alternative to OIDC.

5. **RBAC Advantages**: Be prepared to explain why role-based access control is preferred over assigning permissions directly to users—benefits include simplified administration, easier compliance auditing, and reduced human error.

6. **Credential Theft Vectors**: Understand common attack vectors—phishing, credential stuffing (using leaked passwords across sites), keyloggers, and man-in-the-middle attacks—and corresponding countermeasures.

7. **Session Management**: Know secure session practices: secure and HttpOnly cookies, session timeout, regeneration of session IDs after authentication, and proper session termination on logout.

8. **Zero Trust Architecture**: The emerging principle of "never trust, always verify" assumes no implicit trust based on network location—understand its implications for identity management.