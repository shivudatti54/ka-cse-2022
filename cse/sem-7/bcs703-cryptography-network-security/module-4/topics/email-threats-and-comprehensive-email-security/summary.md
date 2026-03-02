# Email Threats and Comprehensive Email Security - Summary

## Key Definitions and Concepts

- **Phishing**: Fraudulent emails mimicking legitimate sources to steal credentials or install malware
- **Spear Phishing**: Targeted phishing attacks against specific individuals using personalized information
- **Whaling**: Phishing attacks targeting high-level executives
- **Business Email Compromise (BEC)**: Impersonation attacks to trick employees into transferring money or information
- **Email Spoofing**: Forging sender addresses to appear as trusted sources
- **PGP (Pretty Good Privacy)**: End-to-end email encryption using hybrid cryptography and web of trust
- **S/MIME**: Email security standard using X.509 certificates for encryption and digital signatures
- **SPF**: Email authentication protocol verifying authorized sending servers via DNS
- **DKIM**: Cryptographic email authentication verifying message integrity
- **DMARC**: Email authentication policy framework building on SPF and DKIM

## Important Formulas and Concepts

- **PGP Encryption**: Uses hybrid encryption - symmetric key encrypts message, asymmetric encryption protects the symmetric key
- **Digital Signature**: Created with sender's private key, verified with sender's public key
- **SPF Record Format**: `v=spf1 ip4:<IP> include:<domain> ~all`
- **DMARC Policy Levels**: none (monitor), quarantine (spam), reject (block)

## Key Points

1. Over 90% of cyber attacks begin with malicious emails, making email security critical
2. Email threats range from mass phishing campaigns to targeted attacks like BEC
3. End-to-end encryption (PGP/S/MIME) ensures only sender and recipient can read emails
4. Digital signatures provide authentication, integrity, and non-repudiation
5. SPF verifies sending server authorization, DKIM verifies message integrity
6. DMARC provides comprehensive policy enforcement and reporting
7. Secure Email Gateways provide multi-layered protection including spam and malware filtering
8. Multi-Factor Authentication prevents unauthorized access even if passwords are compromised
9. User awareness and training are essential complements to technical security measures

## Common Mistakes to Avoid

1. Assuming spam filters catch all malicious emails - sophisticated attacks bypass automated detection
2. Not verifying email sender addresses - attackers use lookalike domains
3. Clicking links in unexpected or suspicious emails without verification
4. Failing to implement email authentication (SPF/DKIM/DMARC) on organizational domains
5. Using the same password for email and other services - credential reuse increases breach risk

## Revision Tips

1. Practice analyzing email headers to identify spoofed emails
2. Remember the three pillars of email security: confidentiality (encryption), integrity (digital signatures), and authentication (SPF/DKIM/DMARC)
3. Review recent real-world email attack案例 to understand current threat landscape
4. Understand the difference between transport-level encryption (TLS) and end-to-end encryption
5. Be prepared to explain how each email authentication protocol addresses specific security gaps
