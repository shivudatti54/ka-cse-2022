# Public Key Infrastructures - Summary

## Core Concepts

Public Key Infrastructure (PKI) is a comprehensive framework enabling asymmetric cryptography at scale through digital certificates. PKI provides entity authentication, data integrity, confidentiality, and non-repudiation in electronic communications.

## Fundamental Components

| Component | Primary Function |
|-----------|------------------|
| Certificate Authority (CA) | Issues and signs digital certificates |
| Registration Authority (RA) | Verifies applicant identity before CA issuance |
| Certificate Repository | Stores and distributes certificates |
| CRL/OCSP | Provides real-time certificate revocation status |
| HSM | Secure private key generation and storage |

## X.509 Certificate Structure

X.509 certificates contain the subject's public key bound to their identity through the CA's digital signature. Key fields include:
- Version, Serial Number, Signature Algorithm
- Issuer and Subject Distinguished Names
- Validity Period (notBefore, notAfter)
- Subject Public Key Info
- Extensions (SAN, Key Usage, Basic Constraints)

## PKI Workflow

Key pair generation → CSR submission → Identity verification (RA) → Certificate issuance (CA) → Certificate deployment → Certificate verification (relying party)

## Key Distribution Comparison

| Aspect | Symmetric | Asymmetric |
|--------|-----------|------------|
| Key Count | n(n-1)/2 for n users | n key pairs for n users |
| Key Exchange | Requires secure channel | Public keys freely distributed |
| Performance | Fast (efficient for bulk data) | Slow (suitable for key exchange) |
| Algorithm | AES, 3DES, ChaCha20 | RSA, ECC, DSA |

## PKI Applications

- SSL/TLS web security
- S/MIME email security
- Code signing
- VPN authentication
- IoT device identity

## Management Considerations

Effective PKI management requires policies for certificate issuance, renewal, revocation handling, key lifecycle, and compliance with organizational security requirements.