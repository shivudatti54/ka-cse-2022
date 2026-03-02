# Cryptographic Protocols: Protocol Basics

### Protocol Basics

- **Objective**: Ensure secure communication between parties
- **Key Concepts**:
  - **Security**: Ability of a protocol to prevent unauthorized access
  - **Confidentiality**: Protecting the confidentiality of exchanged information
  - **Integrity**: Ensuring the accuracy and authenticity of exchanged information
  - **Authenticity**: Verifying the identity of communicating parties
- **Basic Protocol Structure**:
  - **Components**:
    - **Sender**
    - **Receiver**
    - **Channel** (Communication medium)
  - **Functions**:
    - **Encryption**: Converting plaintext to ciphertext
    - **Decryption**: Converting ciphertext to plaintext
    - **Authentication**: Verifying the identity of communicating parties
    - **Digital Signature**: Verifying the authenticity of a message

### From Objectives to a Protocol

- **Steps to Develop a Protocol**:
  - **Problem Definition**: Identify the security requirements and threats
  - **Protocol Definition**: Define the communication structure and security functions
  - **Security Analysis**: Analyze the protocol for potential vulnerabilities
  - **Implementation**: Implement the protocol using cryptographic techniques
  - **Testing**: Test the protocol for security and functionality

### Analysing a Simple Protocol

- **Symmetric Key Protocol**:
  - **Key Exchange**: Establishing a shared secret key
  - **Encryption**: Encrypting plaintext using the shared key
  - **Decryption**: Decrypting ciphertext using the shared key
- **Example Protocol**: RSA (Rivest-Shamir-Adleman) Protocol
  - **Key Exchange**: Using RSA to establish a shared secret key
  - **Encryption**: Encrypting plaintext using RSA
  - **Decryption**: Decrypting ciphertext using RSA

### Authentication and Key Establishment Protocols

- **Authentication Protocols**:
  - **Types**:
    - **Static Key Authentication**: Using a shared secret key
    * **Example**: RSA protocol
    - **Dynamic Key Authentication**: Establishing a new shared secret key
    * **Example**: Diffie-Hellman key exchange
  - **Key Establishment Protocols**:
    - **Diffie-Hellman Key Exchange**: Establishing a shared secret key
    * **Key Exchange Algorithm**: Diffie-Hellman
    - **Key Agreement Algorithm**: RSA

## Important Formulas and Definitions

- ** xor operation**: Bitwise exclusive or operation (a ⊕ b)
- **Hash function**: A one-way function that maps input to output (h(x))
- **Digital Signature**: A message authentication code (MAC) with encryption (r, s = H(m, s))
