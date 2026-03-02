# Web Security Considerations

=====================================

### Overview

Web security considerations encompass the threats, vulnerabilities, and protective measures relevant to securing web-based systems and communications. Understanding the landscape of web threats and the layered security approaches (network, transport, and application layer) is essential for building secure web applications and services.

### Key Points

- **Confidentiality:** Ensuring that sensitive data is accessible only to authorized parties
- **Integrity:** Guaranteeing that data has not been altered during transmission or storage
- **Availability:** Ensuring that web services remain accessible to legitimate users
- **Authentication:** Verifying the identity of users and systems before granting access
- **Non-repudiation:** Preventing denial of actions performed by a user or system
- **Threats:** Eavesdropping, man-in-the-middle attacks, denial of service, cross-site scripting, SQL injection
- **SSL/TLS:** Primary transport-layer protocol for securing web communications (HTTPS)
- **Defense in Depth:** Layered security approach combining multiple protective mechanisms

### Important Concepts

- Web security operates at multiple layers: network (firewalls, IDS), transport (SSL/TLS), and application (input validation, authentication)
- The CIA triad (Confidentiality, Integrity, Availability) forms the foundation of web security
- HTTPS uses SSL/TLS to encrypt communication between browsers and web servers
- Common web vulnerabilities include XSS, CSRF, SQL injection, and session hijacking
- Security measures include encryption, access controls, input validation, and security auditing

### Notes

- Be able to list and explain the main categories of web security threats
- Understand how SSL/TLS provides confidentiality and integrity at the transport layer
- Know the difference between passive attacks (eavesdropping) and active attacks (modification, DoS)
- For exams, emphasize the layered security approach and the role of each layer in web protection
