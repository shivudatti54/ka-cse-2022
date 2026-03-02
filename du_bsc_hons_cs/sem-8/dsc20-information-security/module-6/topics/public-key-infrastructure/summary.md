# Public Key Infrastructure (PKI) - Summary

## Key Definitions and Concepts

- **Public Key Infrastructure (PKI):** The framework of roles, policies, hardware, software, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates and manage public-key encryption.

- **Digital Certificate:** An electronic document that binds a public key to an identity, issued by a trusted Certificate Authority using its digital signature.

- **Certificate Authority (CA):** A trusted third party that issues digital certificates after verifying the identity of the requester. Root CAs are trust anchors; intermediate CAs extend trust through certificate chains.

- **Registration Authority (RA):** An entity that performs identity verification before the CA issues a certificate.

- **X.509:** The standard defining the format of digital certificates, including fields for subject, issuer, public key, validity, and signature.

- **Certificate Revocation List (CRL):** A signed list of revoked certificate serial numbers published periodically by the CA.

- **Online Certificate Status Protocol (OCSP):** A real-time protocol for querying certificate revocation status.

## Important Formulas and Techniques

- **Certificate Chain Verification:** Validates each certificate in the chain by verifying the issuer's signature using the issuer's public key, continuing until a trusted root CA is reached.

- **Hostname Verification:** Ensures the certificate's Subject Alternative Name (SAN) or Common Name (CN) matches the domain being accessed.

- **Trust Anchor:** A root CA certificate pre-installed in browsers or operating systems, unconditionally trusted.

## Key Points

- PKI solves the key distribution problem in asymmetric cryptography by providing a mechanism to verify the authenticity of public keys.

- Digital certificates bind public keys to identities through the digital signature of a trusted Certificate Authority.

- Certificate verification involves checking validity period, signature validity, and revocation status (via CRL or OCSP).

- Different certificate types provide different levels of assurance: DV (domain only), OV (organization), EV (extended validation with green bar).

- The hierarchical trust model dominates web PKI, with browser vendors maintaining trust stores of root CAs.

- Certificate revocation is critical for security when private keys are compromised or affiliations change.

- PKI enables HTTPS, secure email, code signing, VPN authentication, and many other security applications.

## Common Mistakes to Avoid

- Confusing the role of RA and CA—remember RA verifies identity, CA issues certificates.

- Assuming certificates are always valid—they can be revoked before expiration.

- Neglecting hostname verification—certificates must match the domain being accessed.

- Believing root CAs are infallible—compromised CAs have issued fraudulent certificates (e.g., DigiNotar breach).

## Revision Tips

1. Draw and trace a complete certificate chain from leaf to root, explaining each verification step.

2. Create a comparison table of CRL vs OCSP, noting latency, freshness, and scalability trade-offs.

3. Practice explaining PKI to a non-technical person—this tests your conceptual clarity.

4. Review real-world PKI incidents (DigiNotar, Symantec distrust) to understand why revocation and trust management matter.

5. Memorize the X.509 certificate structure and the verification process during TLS handshakes.