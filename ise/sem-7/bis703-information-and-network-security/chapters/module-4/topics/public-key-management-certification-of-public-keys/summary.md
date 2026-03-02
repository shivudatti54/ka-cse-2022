# **Public-Key Management: Revision Notes**

## **Definitions and Formulas**

- **Public-Key Infrastructure (PKI)**: A system that enables secure communication over the internet using public-key cryptography.
- **Certificate**: A digital document that binds a public key to the identity of its owner.
- **Certificate Authority (CA)**: An entity that issues digital certificates to users.
- **Certificate Revocation List (CRL)**: A list of revoked digital certificates.
- **X.509 Certificate**: A standard certificate format used in PKI.

## **The Certificate Lifecycle**

- **Key Pair Generation**: Creation of a pair of keys (public and private) for a user.
- **Certificate Request**: User requests a digital certificate from a CA.
- **Certificate Issuance**: CA issues a digital certificate to the user.
- **Certificate Signing**: CA verifies the user's identity and signs the certificate.
- **Certificate Deployment**: Certificate is deployed to the user's device or server.
- **Certificate Revocation**: Certificate is revoked by the CA, and it is removed from the CRL.
- **Certificate Renewal**: Certificate is renewed by the user, and the old certificate is revoked.

## **Public-Key Management Models**

- **Hierarchical Model**: A hierarchical structure of CAs, where each CA is subordinate to a higher-level CA.
- **Flat Model**: A flat structure of CAs, where each CA is independent of the others.
- **Hierarchical Model with a Root CA**: A hierarchical structure with a root CA at the top.

## **Alternative Approaches**

- **Self-Signed Certificates**: Certificates that are signed by the user themselves, rather than a CA.
- **Root Certificates**: Certificates that are trusted by default, and are used to establish trust in a root CA.

## **Important Theorems and Concepts**

- **Diffie-Hellman Key Exchange**: A key exchange algorithm that enables secure key exchange between two parties.
- **RSA Algorithm**: A public-key encryption algorithm that is widely used in PKI.
- **Elliptic Curve Cryptography (ECC)**: A public-key encryption algorithm that is more secure than RSA for smaller key sizes.
