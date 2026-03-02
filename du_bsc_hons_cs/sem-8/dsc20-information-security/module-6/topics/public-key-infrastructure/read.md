# Public Key Infrastructure (PKI)

## Introduction

In our increasingly digital world, where online transactions, electronic communications, and cloud services have become the norm, ensuring secure communication over insecure networks like the Internet has become paramount. While symmetric cryptography offers speed and efficiency for bulk data encryption, it fails to solve the fundamental problem of key distribution—how do two parties securely exchange a shared secret key? This challenge was elegantly addressed by asymmetric cryptography, but a new problem emerged: how do we trust that a particular public key truly belongs to the claimed entity? Public Key Infrastructure (PKI) is the comprehensive framework designed to solve this trust problem through the use of digital certificates, Certificate Authorities, and established trust models.

PKI forms the backbone of modern internet security, enabling secure e-commerce, online banking, email encryption, and authenticated web browsing. Every time you access a website with HTTPS, send an encrypted email, or sign a digital document, PKI is working behind the scenes to verify identities and establish secure channels. Understanding PKI is essential for any computer science student, as it addresses the critical security requirement of authentication in distributed systems—a core concept in the University of Delhi's Information Security curriculum.

## Key Concepts

### 1. Public Key Cryptography Recap

Before diving into PKI, it is crucial to understand the foundation upon which it builds. Public key cryptography uses key pairs: a private key kept secret by the owner, and a public key distributed freely. What one key encrypts, only the other can decrypt. This enables two fundamental operations: encryption (anyone can encrypt with the recipient's public key) and digital signatures (the owner signs with their private key, verifiable by anyone with their public key). However, the security of these operations depends entirely on the authenticity of the public keys—malicious actors could distribute fake public keys, intercepting communications or impersonating legitimate entities.

### 2. Digital Certificates

A digital certificate is an electronic document that binds a public key to an identity (person, organization, or device). The most common standard is X.509, defined by the ITU-T. A digital certificate contains several critical fields: the subject's identity information (name, organization, email), the subject's public key, the issuer's identity (who signed the certificate), the validity period, serial number, and the issuer's digital signature. The certificate essentially vouches: "I (the issuer) certify that this public key belongs to this identity."

### 3. Certificate Authority (CA)

The Certificate Authority is the cornerstone of PKI trust. A CA is a trusted third party that issues digital certificates after verifying the identity of the requester. CAs can be Root CAs (whose certificates are self-signed and trusted unconditionally) or Intermediate CAs (whose certificates are signed by Root CAs, creating a chain of trust). Popular CAs include DigiCert, Comodo, Let's Encrypt (which offers free certificates), and Government CAs like eMudhra in India. The browser maintains a list of trusted Root CAs, forming the foundation of PKI trust in web browsing.

### 4. Registration Authority (RA)

The Registration Authority acts as an intermediary between the end entity and the CA. The RA is responsible for verifying the identity of certificate requesters before the CA issues a certificate. This verification process varies based on the certificate type: domain validation (DV) certificates only verify domain ownership, while extended validation (EV) certificates require rigorous verification of legal existence and operational identity. The RA performs identity proofing, ensuring that the entity requesting the certificate is who they claim to be.

### 5. Certificate Revocation

Certificates can become invalid before their expiration date due to key compromise, change in affiliation, or other reasons. PKI must provide mechanisms to revoke these certificates and inform relying parties not to trust them.

**Certificate Revocation List (CRL):** A signed list maintained by the CA containing serial numbers of revoked certificates. Clients must download and check this list periodically. The main drawback is latency—a recently revoked certificate might still be considered valid until the next CRL update.

**Online Certificate Status Protocol (OCSP):** A real-time protocol where clients send a certificate's serial number to an OCSP responder, which returns the current status (valid, revoked, or unknown). OCSP provides faster revocation information but adds latency to each verification.

**OCSP Stapling:** An optimization where the web server obtains the OCSP response and "staples" it to the certificate during the TLS handshake, reducing client queries and improving performance.

### 6. Certificate Lifecycle

The certificate lifecycle encompasses several stages: generation (key pair creation and CSR submission), issuance (CA verification and certificate creation), distribution (making the certificate available), validation (checking certificate trust and status during use), renewal (requesting a new certificate before expiration), and revocation (invalidate before expiration when necessary). Managing this lifecycle effectively is crucial for maintaining security.

### 7. Types of Digital Certificates

Different use cases require different certificate types:

- **SSL/TLS Certificates:** Secure web communications, identified by domain names. Includes Domain Validation (DV), Organization Validation (OV), and Extended Validation (EV) certificates.
- **Code Signing Certificates:** Authenticate software publishers and ensure code integrity, preventing malware distribution.
- **S/MIME Certificates:** Secure email encryption and signing.
- **Client Authentication Certificates:** Authenticate users or devices for VPN access, intranet logins.
- **Qualified Certificates:** Used for legal signatures under eIDAS regulations in the EU.

### 8. Trust Models

PKI operates based on trust models that define how trust flows between entities:

- **Hierarchical Trust Model:** A tree structure with a root CA at the top, intermediate CAs below, and end-entity certificates at the bottom. Trust propagates downward—this is the dominant model for web PKI.
- **Web of Trust:** A decentralized model where individuals certify each other's keys (used by PGP/GnuPG). No central authority exists; trust is based on personal relationships.
- **Bridge CA Model:** Uses a central bridge CA that cross-signs certificates from different hierarchies, enabling interoperability.

### 9. PKI Standards

PKI relies on several important standards:

- **X.509:** Defines the certificate format and fields
- **PKCS#10:** Defines the Certificate Signing Request (CSR) format
- **PKCS#7/CMS:** Defines cryptographic message syntax for signed/encrypted data
- **PKCS#12:** Defines a format for storing multiple cryptographic objects (commonly used to export certificate+private key)
- **CRL/OCSP:** Protocols for certificate revocation status

## Examples

### Example 1: SSL/TLS Handshake with Certificate Verification

When a browser connects to https://www.bank.com, the TLS handshake proceeds as follows:

1. **Client Hello:** Browser sends supported cipher suites and random number to server
2. **Server Hello:** Server selects cipher suite and sends its random number
3. **Certificate Exchange:** Server sends its certificate containing its public key and identity (www.bank.com)
4. **Certificate Verification:** Browser performs these steps:
   - Checks if certificate is within validity period
   - Verifies the CA's signature using the CA's public key (stored in browser's trust store)
   - For intermediate CAs, builds and verifies the full certificate chain
   - Performs hostname verification (certificate name matches www.bank.com)
   - Optionally checks revocation status via CRL/OCSP
5. **Key Exchange:** Browser generates a premaster secret, encrypts with server's public key, sends to server
6. **Finished:** Both parties derive session keys and establish secure channel

If any verification step fails, the browser displays a security warning, protecting the user from potential attacks.

### Example 2: Certificate Chain Verification in Practice

Consider a scenario where your browser connects to shop.example.com and receives a certificate chain:

```
Leaf Certificate: shop.example.com (issued by DigiCert SHA2 Extended Validation Server CA)
    |
    |-- Issued by: DigiCert SHA2 Extended Validation Server CA (issued by DigiCert Global Root CA)
        |
        |-- Issued by: DigiCert Global Root CA (self-signed, trust anchor)
```

Verification proceeds:
1. Browser has DigiCert Global Root CA in its trust store (trust anchor)
2. Leaf certificate signature verified using "DigiCert SHA2 Extended Validation Server CA" public key
3. Intermediate CA certificate signature verified using "DigiCert Global Root CA" public key
4. Root CA is self-signed and matches a trust anchor in the browser's store
5. Chain is valid only if all signatures verify and all certificates are within validity

### Example 3: Real-World Application - Online Banking

When you access your bank's website:
- The bank's certificate proves the website's identity (preventing phishing)
- Your browser verifies the certificate chain back to a trusted root CA
- The bank may also request a client certificate for two-factor authentication
- All subsequent communication is encrypted using keys established during the handshake
- The bank's systems log certificate information for audit trails
- If your session involves high-value transactions, the bank might require additional certificate-based authentication

This multi-layered approach ensures that you are communicating with your genuine bank, not an attacker.

## Exam Tips

1. **Understand the difference between symmetric and asymmetric encryption** in the context of key distribution—PKI solves the problem asymmetric cryptography cannot solve alone.

2. **Remember the key X.509 certificate fields:** Subject, Issuer, Public Key, Validity Period, Serial Number, Signature. Be able to explain each.

3. **Know the difference between CRL and OCSP:** CRL is a list downloaded periodically; OCSP is a real-time query. Understand the trade-offs between latency and freshness.

4. **Distinguish between DV, OV, and EV certificates:** DV verifies domain ownership only; OV verifies organization existence; EV requires the most rigorous verification with green address bar in browsers.

5. **Be able to trace a certificate verification chain:** From the end-entity certificate through intermediate CAs to the root CA, explaining how trust is established.

6. **Understand what makes a key pair secure:** Private key must remain secret; public key must be authentic and bound to identity via certificate.

7. **Explain the role of RA vs CA:** RA handles identity verification; CA issues certificates. Know that they can be the same entity or separate.

8. **Real-world examples matter:** Be prepared to explain how PKI is used in HTTPS, email security, code signing, and VPN access.

9. **Know the trust models:** Hierarchical (web PKI), Web of Trust (PGP), and Bridge CA models—understand when each is appropriate.

10. **Certificate lifecycle management is important:** Generation, issuance, distribution, validation, renewal, and revocation—understand the security implications at each stage.