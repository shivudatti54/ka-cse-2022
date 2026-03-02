# **IP Security Revision Notes**

### Overview

- **IP Security (IPSec)**: A suite of protocols that provides security for IP communications.
- **Goals**: Ensure confidentiality, integrity, and authenticity of IP packets.

### IP Security Policy

- **Security Policy**: A set of rules that define how IPsec will be used to protect IP communications.
- **Policy Identifiers (PIs)**: Unique identifiers for each security policy.
- **SA/DP**: Security Associations (SA) and Delete Process (DP) manage policy identifiers.

### Encapsulating Security Payload (ESP)

- **ESP**: A transport-layer protocol that encrypts and authenticates IP packets.
- **ESP Header**: 8-byte header that contains encryption, integrity, and authentication information.
- **ESP Payload**: The original IP packet payload, encrypted and authenticated.

### Combining Security Associations

- **Multi-Path Security**: Combining multiple security associations to provide additional security.
- **SA/DP**: Security Associations (SA) and Delete Process (DP) manage combined security associations.

### Internet Key Exchange (IKE)

- **IKE**: A key management protocol that negotiates and manages IPsec security associations.
- **Phase 1**: Establishes the security association (SA) and authenticates the peers.
- **Phase 2**: Negotiates the encryption and authentication algorithms.

**Important Formulas and Definitions**

- **Modulo Operation**: Used to calculate the encryption key.
- **Diffie-Hellman Key Exchange**: A key agreement protocol used in IKE.
- **Public-Key Cryptography**: A method of cryptography that uses a pair of keys (public and private).

**Key Theorems**

- **Diffie-Hellman Theorem**: A theorem that proves the security of the Diffie-Hellman key exchange.
- **RSA Theorem**: A theorem that proves the security of the RSA encryption algorithm.

**Revision Tips**

- Familiarize yourself with the IPsec architecture and protocols (ESP, IKE, etc.).
- Understand the importance of security policies and key management in IPsec.
- Practice calculating encryption keys and managing security associations.
