# **Public-Key Management: Revision Notes**

### Definitions and Concepts

- **Public-Key**: A pair of keys, one public and one private, used for encryption and decryption.
- **Certificate**: A digital document that binds a public key to its owner's identity.
- **Certificate Lifecycle**: The process of issuing, using, and revoking certificates.

### Certification of Public Keys

- **Certificate Authorities (CAs)**: Issuers of digital certificates.
- **Public Key Infrastructure (PKI)**: A system of public-key cryptography.
- **Key Exchange**: Methods for securely exchanging public keys.

### The Certificate Lifecycle

- **Certificate Issuance**:
  - Registration: Requester registers for a certificate.
  - Verification: CA verifies requester's identity.
  - Signing: CA signs certificate with its private key.
- **Certificate Use**:
  - End-use: Certificate is used for encryption and decryption.
  - Revocation: Certificate is marked as revoked.
- **Certificate Revocation**:
  - Revocation Request: Certificate is marked as revoked.
  - Revocation List (CRL): List of revoked certificates.

### Public-Key Management Models

- **Hierarchical PKI**: A hierarchical structure of CAs.
- **Flat PKI**: A flat structure without hierarchical relationships.
- **Hybrid PKI**: Combination of hierarchical and flat PKIs.

### Alternative Approaches

- **Public-Key Cryptography without Certification Authorities (PKC)**: No CA is required.
- **Certificateless Public-Key Cryptography**: No CA is required.

### Important Formulas and Theorems

- **RSA Algorithm**: A widely used public-key encryption algorithm.
  - Encryption: $c = m^e \mod n$
  - Decryption: $m = c^d \mod n$
- **Digital Signature**: A method of verifying the authenticity of a message.
  - Signature: $\sigma = m^s \mod n$
  - Verification: $\sigma \equiv m^d \mod n$

Note: This summary is a concise revision guide and is not intended to be a comprehensive treatment of the topic.
