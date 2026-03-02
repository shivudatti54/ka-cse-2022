# Distribution of Public Keys

=====================================

### Overview

Secure distribution of public keys is a critical challenge in asymmetric cryptography. Without proper authentication, an attacker can substitute their own public key and perform man-in-the-middle attacks. The main solutions include public announcements, publicly available directories, Public Key Infrastructure (PKI) with digital certificates, and the Web of Trust model.

### Key Points

- **Core Problem:** Binding a public key to its true owner to prevent impersonation attacks
- **Public Announcement:** Simplest method; user broadcasts key publicly; no authentication -- insecure and impractical
- **Public Directory:** Centralized trusted directory of {name, public_key} pairs; single point of failure if compromised
- **PKI (Public Key Infrastructure):** Standard solution using Certification Authorities (CAs) to issue signed digital certificates
- **Digital Certificate:** A digitally signed document (X.509 format) binding a public key to an identity
- **Certification Authority (CA):** Trusted third party that verifies identity and signs certificates with its private key
- **Web of Trust:** Decentralized model (used in PGP) where users sign each other's keys; less scalable than PKI
- **Trust Store:** Browsers come with pre-installed root CA public keys to verify website certificates

### Important Concepts

- PKI workflow: User creates CSR -> CA verifies identity -> CA creates and signs X.509 certificate -> User distributes certificate
- Certificate verification: Recipient checks CA's digital signature on the certificate using CA's trusted public key
- HTTPS example: Browser receives SSL/TLS certificate, verifies CA signature from trust store, then trusts the public key
- Man-in-the-middle attack: Possible when public key authenticity is not verified (public announcement method)

### Notes

- Know all four distribution methods and their relative strengths and weaknesses
- PKI with X.509 certificates is the most important method for exam purposes
- Understand the difference between centralized PKI (CAs) and decentralized Web of Trust (PGP)
- Be prepared to draw or describe the certificate signing and verification process
