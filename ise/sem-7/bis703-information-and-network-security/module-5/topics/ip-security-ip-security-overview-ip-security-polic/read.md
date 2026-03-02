# **IP Security: Study Material**


## Table of Contents

- [**IP Security: Study Material**](#ip-security-study-material)
- [**Module: 10 hours**](#module-10-hours)
  - [Introduction to IP Security](#introduction-to-ip-security)
  - [IP Security Policy](#ip-security-policy)
  - [Encapsulating Security Payload (ESP)](#encapsulating-security-payload-esp)
  - [Combining Security Associations (SA)](#combining-security-associations-sa)
  - [Internet Key Exchange (IKE)](#internet-key-exchange-ike)

## **Module: 10 hours**

### Introduction to IP Security

#### Overview of IP Security

IP Security (IPSec) is a suite of protocols used to secure Internet Protocol (IP) communications over the internet. It provides confidentiality, integrity, and authentication of data packets. IPSec is used to protect data from unauthorized access, tampering, and eavesdropping.

#### Importance of IP Security

- Protects data from unauthorized access and tampering
- Ensures data integrity and authenticity
- Provides confidentiality and encryption
- Essential for securing data transmitted over the internet

### IP Security Policy

#### Definition

IP Security Policy (IPSP) is a set of rules that defines how IPSec protocols are used to secure IP communications. IPSP includes policies for key management, tunnel mode, and encryption.

#### Key Components of IP Security Policy

- **Key Management**: Defines how encryption keys are generated, distributed, and managed.
- **Tunnel Mode**: Determines whether IPsec packets are encapsulated in a new IP packet or not.
- **Encryption**: Defines the encryption algorithm and key length used to protect data.

#### Example of IP Security Policy

| Policy         | Description                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Key Management | Use RSA keys with a key size of 2048 bits. Generate keys using a private key and distribute them using a key exchange protocol. |
| Tunnel Mode    | Use IPsec transport mode to encapsulate IP packets.                                                                             |
| Encryption     | Use AES-256-CBC encryption algorithm with a key size of 256 bits.                                                               |

### Encapsulating Security Payload (ESP)

#### Definition

Encapsulating Security Payload (ESP) is a protocol used in IPSec to provide confidentiality and integrity of IP packets. ESP encrypts the payload of IP packets and adds a header to the packet.

#### Key Components of ESP

- **Encryption**: Uses the AES algorithm with a key size of 128, 192, or 256 bits.
- **Authentication**: Uses the HMAC-SHA-256 algorithm with a key size of 128, 192, or 256 bits.
- **Padding**: Adds padding to the packet to ensure that it is a multiple of the block size.

#### Example of ESP

| Protocol       | Description                                                                   |
| -------------- | ----------------------------------------------------------------------------- |
| Encryption     | Uses AES-256-CBC encryption algorithm.                                        |
| Authentication | Uses HMAC-SHA-256 algorithm.                                                  |
| Padding        | Adds padding to the packet to ensure that it is a multiple of the block size. |

### Combining Security Associations (SA)

#### Definition

Combining Security Associations (SA) is a process in IPSec that combines multiple security associations to create a single SA. This allows multiple protocols to be used together to provide additional security.

#### Key Components of Combining SA

- **SA Types**: Includes SA types such as IPsec transport mode, IPsec tunnel mode, and ESP.
- **SA Algorithms**: Uses encryption and authentication algorithms such as AES and HMAC-SHA-256.
- **SA Key Sizes**: Uses key sizes such as 128, 192, or 256 bits.

#### Example of Combining SA

| SA Type              | Description                                                                      |
| -------------------- | -------------------------------------------------------------------------------- |
| IPsec Transport Mode | Uses ESP to encapsulate IP packets.                                              |
| IPsec Tunnel Mode    | Uses ESP to encapsulate IP packets.                                              |
| SA Algorithms        | Uses AES-256-CBC encryption algorithm and HMAC-SHA-256 authentication algorithm. |
| SA Key Sizes         | Uses key sizes of 128, 192, or 256 bits.                                         |

### Internet Key Exchange (IKE)

#### Definition

Internet Key Exchange (IKE) is a protocol used in IPSec to establish and manage IPsec security associations. IKE is used to negotiate key exchange and establish IPsec SA.

#### Key Components of IKE

- **Key Exchange**: Uses the Diffie-Hellman key exchange algorithm to establish a shared secret key.
- **Authentication**: Uses the RSA or Diffie-Hellman key exchange algorithm to authenticate the peer.
- **Encryption**: Uses the AES algorithm to encrypt the key exchange.

#### Example of IKE

| Protocol       | Description                                     |
| -------------- | ----------------------------------------------- |
| Key Exchange   | Uses the Diffie-Hellman key exchange algorithm. |
| Authentication | Uses the RSA algorithm.                         |
| Encryption     | Uses AES-256-CBC encryption algorithm.          |
