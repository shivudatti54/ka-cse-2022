# Authentication Mechanisms
**Ge8A Information Security | BSc Physical Science (CS) | Delhi University, NEP 2024**

---

## Introduction

Authentication is the process of verifying the identity of a user, device, or system before granting access to resources. It forms the first line of defense in information security, ensuring that only legitimate users can access sensitive data and systems. According to the Delhi University syllabus, understanding authentication mechanisms is essential for securing information systems.

---

## Key Concepts

### 1. Authentication vs Authorization vs Identification
- **Identification**: Claiming an identity (username)
- **Authentication**: Proving the claimed identity (password, biometric)
- **Authorization**: Determining access rights after authentication

### 2. Authentication Factors

| Factor Type | Examples |
|-------------|----------|
| **Something You Know** | Password, PIN, security questions |
| **Something You Have** | Smart card, token, mobile phone |
| **Something You Are** | Fingerprint, iris scan, facial recognition |
| **Somewhere You Are** | Location-based authentication, IP address |

### 3. Types of Authentication

**Single-Factor Authentication (SFA)**
- Uses only one factor (e.g., password only)
- Least secure, vulnerable to attacks

**Multi-Factor Authentication (MFA)**
- Combines two or more factors
- Significantly enhances security
- Examples: ATM (card + PIN), online banking (password + OTP)

### 4. Common Authentication Mechanisms

- **Password-Based Authentication**: Traditional method using secret words/phrases
- **Token-Based Authentication**: Hardware tokens (RSA SecurID) or software tokens (authenticator apps)
- **Biometric Authentication**: Physiological (fingerprint, iris) and behavioral (keystroke dynamics)
- **Certificate-Based Authentication**: Digital certificates (PKI) for identity verification
- **Single Sign-On (SSO)**: Allows one set of credentials to access multiple applications

### 5. Authentication Protocols & Standards

- **Kerberos**: Network authentication protocol using tickets
- **OAuth 2.0**: Authorization framework for secure API access
- **OpenID Connect**: Identity layer on top of OAuth 2.0
- **SAML**: XML-based standard for exchanging authentication data

### 6. Password Security Best Practices

- Minimum length (8+ characters)
- Mix of uppercase, lowercase, numbers, and symbols
- Regular password changes
- Avoid dictionary words and personal information
- Use password managers
- Implement account lockout policies

---

## Conclusion

Authentication mechanisms are fundamental to information security. The evolution from simple passwords to multi-factor and biometric authentication reflects the increasing sophistication of cyber threats. For the Ge8A examination, students must understand the various authentication factors, mechanisms, and protocols, along with their practical applications in securing information systems.

---

*Quick Revision Tip: Remember authentication factors using the acronym "KHAW" (Know, Have, Are, Where) and focus on the difference between SFA and MFA for exam success.*