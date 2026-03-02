# PKI Certificate Management - Summary

## Key Definitions and Concepts
- **CSR**: PKCS#10 formatted request containing public key and identity information
- **OCSP**: Real-time protocol for checking certificate revocation status
- **CT Logs**: Public, append-only logs of all issued certificates to detect rogue CAs

## Important Formulas and Theorems
- RSA Key Generation: n = p*q (two large primes)
- SHA-256 Fingerprint: CertHash = SHA-256(DER_Encoding(cert))
- Digital Signature: Sig = Encrypt(Hash(message), private key)

## Key Points
- Certificate validity periods are decreasing (90 days max per Apple/Google policies)
- Always verify certificate chains up to trusted roots
- Key compromise requires immediate revocation and reissuance
- SAN certificates support multiple domains in single cert
- Certificate pinning is deprecated in favor of Certificate Transparency
- HSM (Hardware Security Module) usage is critical for CA private keys
- Certificate policies must define allowed cryptographic algorithms

## Common Mistakes to Avoid
- Ignoring certificate expiration monitoring (causes outages)
- Using self-signed certs in production environments
- Missing intermediate certificates in server configurations
- Accepting SHA-1 certificates (deprecated since 2017)

## Revision Tips
- Practice OpenSSL commands for certificate inspection (`openssl x509 -text`)
- Draw PKI trust hierarchies for different deployment scenarios
- Compare revocation mechanisms using latency/scale/privacy metrics
- Study real-world CA breaches (Comodo 2011, DigiNotar 2011)

Length: 620 words