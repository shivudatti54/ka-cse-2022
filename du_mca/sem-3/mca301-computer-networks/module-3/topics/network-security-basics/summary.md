# Network Security Basics - Summary

## Key Definitions and Concepts
- CIA Triad: Confidentiality (encryption), Integrity (hashes), Availability (redundancy)
- VPN: Secure tunnel between networks using encryption/authentication
- Zero Trust Model: "Never trust, always verify" approach
- Man-in-the-Middle (MitM): Interception of communication between two parties

## Important Formulas and Theorems
- RSA Encryption: c ≡ m^e mod n (ciphertext = plaintext^public_key mod modulus)
- SHA-256: Merkle-Damgård construction with 64-round compression
- Diffie-Hellman: Key exchange using (g^a mod p)^b mod p = g^ab mod p
- Birthday Attack Complexity: O(√(2^n)) for n-bit hash

## Key Points
- Always use AES-256 for sensitive data instead of DES/3DES
- Stateful firewalls track connection states; packet filters don't
- IPsec uses ESP (Encapsulating Security Payload) for encryption
- Multi-factor authentication > Single-factor for critical systems
- Certificate Authorities (CA) validate digital identities
- WPA3 uses Simultaneous Authentication of Equals (SAE) protocol
- OWASP Top 10 includes injection attacks and broken authentication

## Common Mistakes to Avoid
- Confusing authentication (who you are) with authorization (what you can do)
- Using ECB mode in block cipher implementations (vulnerable to patterns)
- Neglecting certificate expiration dates in PKI management
- Assuming HTTPS alone guarantees website security (misses server-side vulnerabilities)

## Revision Tips
1. Create a CIA triad matrix for different attack types
2. Practice OpenSSL commands for certificate generation
3. Diagram IPsec tunnel vs transport modes
4. Memorize port numbers: SSH-22, HTTPS-443, RADIUS-1812
5. Use Wireshark to analyze TLS handshake packets