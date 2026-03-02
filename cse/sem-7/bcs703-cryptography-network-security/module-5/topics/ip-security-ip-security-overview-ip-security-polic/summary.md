# **IP Security: Revision Notes**

### IP Security Overview

- IP Security is a framework for securing Internet Protocol (IP) communications
- Ensures confidentiality, integrity, and authenticity of data
- Based on the concept of encrypting data before transmission
- Uses various protocols and mechanisms to achieve security

### IP Security Policy

- Definition: A set of rules and procedures for managing and enforcing IP security policies
- Includes policies for access control, authentication, and authorization
- Ensures that security settings are consistent and enforceable across the network

### Encapsulating Security Payload (ESP)

- Protocol used for encrypting and authenticating IP packets
- Provides confidentiality, integrity, and authenticity of data
- Uses symmetric key cryptography (AES, DES, etc.)
- ESP protocol is used for IKE (Internet Key Exchange) to establish a security association

### Combining Security Associations

- Combining multiple security associations into a single association
- Allows for flexibility in security settings
- Enables grouping of multiple IPsec policies together
- Used for scalability and simplification of security management

### Internet Key Exchange (IKE)

- Protocol used for establishing, managing, and maintaining IPsec security associations
- Ensures secure exchange of encryption keys between parties
- Uses Diffie-Hellman key exchange and RSA keys for key exchange
- IKE is used for ESP and IPSec protocols

### Important Formulas and Definitions

- **Encryption**: Converting plaintext into ciphertext using an encryption algorithm
- **Decryption**: Converting ciphertext into plaintext using a decryption algorithm
- **Symmetric key**: A secret key used for both encryption and decryption
- **Asymmetric key**: A pair of keys used for encryption and decryption (public and private keys)
- **Diffie-Hellman key exchange**: A key exchange protocol for establishing a shared secret key between parties
- **IKE protocol**: Internet Key Exchange protocol for establishing and managing IPsec security associations

### Important Theorems

- **Kerckhoffs' Principle**: Encryption should be secure even if the attacker knows the encryption algorithm and has access to the plaintext.
