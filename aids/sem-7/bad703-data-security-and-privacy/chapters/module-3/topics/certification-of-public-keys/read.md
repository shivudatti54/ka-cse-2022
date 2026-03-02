# Module 3: Certification of Public Keys

## Introduction

In the world of asymmetric cryptography, your public key is meant to be shared with the world. But how can someone be sure that a public key truly belongs to the person or entity it claims to? This is the fundamental problem of **trust** in digital communication. Without a mechanism to verify authenticity, an attacker could easily substitute their own public key for a legitimate one (a Man-in-the-Middle attack). **Public Key Certification** is the process that solves this problem by binding a public key to an identity, creating trust in the digital realm.

## Core Concepts

### 1. Digital Certificates

A **Digital Certificate** (or public key certificate) is a digital document that acts like a digital passport. It uses a digital signature to bind a public key with an identity—such as a person, organization, or website.

The most common standard for digital certificates is **X.509**. An X.509 certificate contains crucial information, including:
*   **Subject:** The entity whose identity is being certified (e.g., ".ac.in").
*   **Subject's Public Key:** The core piece of information being certified.
*   **Issuer:** The Certificate Authority that created and signed the certificate.
*   **Validity Period:** The start and end dates for which the certificate is valid.
*   **Digital Signature:** The signature of the Issuer (CA) over the entire certificate content.

### 2. Certificate Authority (CA)

A **Certificate Authority (CA)** is a trusted third-party entity that issues and manages digital certificates. Its role is central to the Public Key Infrastructure (PKI). Users must trust the CA's public key implicitly (it is often pre-installed in operating systems and browsers).

The process works as follows:
1.  An entity generates a key pair and creates a **Certificate Signing Request (CSR)**, which includes its public key and identity information.
2.  The CA verifies the applicant's identity through various means (e.g., checking domain ownership, legal documents).
3.  Once verified, the CA creates the digital certificate, signs it with its own **private key**, and sends it back to the applicant.

### 3. Verification and the Chain of Trust

When you receive a digital certificate (e.g., when connecting to a secure website), your software ( browser) must verify it. The verification process is crucial:

1.  **Check Signature:** The software uses the CA's well-known **public key** to verify the signature on the certificate. A valid signature proves the certificate was issued by the trusted CA and has not been tampered with.
2.  **Check Validity:** The software checks that the current date and time are within the certificate's validity period.
3.  **Check Revocation:** The software may check if the certificate has been revoked (e.g., because the private key was compromised) by consulting a **Certificate Revocation List (CRL)** or using the **Online Certificate Status Protocol (OCSP)**.

For efficiency and scalability, trust is often hierarchical, forming a **chain of trust**.
*   A **Root CA** is at the top of the hierarchy. Its public key is pre-trusted.
*   The Root CA can issue certificates for **Intermediate CAs**.
*   The Intermediate CA then issues the **end-entity certificate** (e.g., for a website).
Your software verifies the entire chain: it checks the website's certificate is signed by the Intermediate CA's private key, and then checks that the Intermediate CA's certificate is signed by the Root CA's private key.

### Example: HTTPS/SSL

When you visit `https://.ac.in`:
1.  The  web server sends its X.509 certificate to your browser.
2.  Your browser checks if the certificate was signed by a trusted CA (e.g., DigiCert, Let's Encrypt).
3.  It verifies the CA's signature on the certificate.
4.  It checks the certificate's validity period and ensures it's for the correct domain (`.ac.in`).
5.  If all checks pass, your browser trusts the server's public key. It then uses this key to establish a secure encrypted session (SSL/TLS) for all subsequent communication.

## Key Points / Summary

*   **Purpose:** Public key certification solves the problem of trusting that a public key belongs to its claimed owner.
*   **Digital Certificate:** An electronic document that binds a public key to an identity, signed by a trusted authority. The X.509 standard is most common.
*   **Certificate Authority (CA):** A trusted third-party entity responsible for verifying identities and issuing digital certificates.
*   **Verification:** Clients verify a certificate by checking the CA's digital signature, its validity period, and its revocation status.
*   **Chain of Trust:** A hierarchical model where root CAs trust intermediate CAs, which in turn trust end-entities, allowing for scalable trust.
*   **Application:** This mechanism is the foundation for secure web browsing (HTTPS), secure email (S/MIME), and many other secure online services.