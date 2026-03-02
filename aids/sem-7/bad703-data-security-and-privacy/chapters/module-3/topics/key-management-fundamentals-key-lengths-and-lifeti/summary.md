# **Key Management Fundamentals**

### Definitions

- **Key**: A string of characters used for encryption and decryption
- **Key management**: The process of creating, distributing, managing, and controlling keys
- **Key lifecycle**: The entire life cycle of a key, from generation to revocation and disposal

### Key Management Fundamentals

- **Key management principles**:
  - Confidentiality
  - Integrity
  - Availability
- **Key management models**:
  - Hierarchical model
  - Centralized model
  - Distributed model

### Key Lengths and Lifetimes

- **Key length**:
  - Measured in bits (e.g., 128, 256, 384)
  - Determines the number of possible key combinations
- **Key lifetime**:
  - The period during which a key is considered secure
  - Can be fixed or dynamic

### Key Generation

- **Key generation algorithms**:
  - Random number generator (RNG)
  - Hash function
  - Diffie-Hellman key exchange
- **Key generation principles**:
  - Unpredictability
  - Uniformity

### Key Establishment

- **Key establishment protocols**:
  - Diffie-Hellman key exchange
  - RSA key exchange
  - Elliptic Curve Diffie-Hellman key exchange
- **Key establishment principles**:
  - Mutual authentication
  - Secure key exchange

### Key Storage

- **Key storage methods**:
  - Symmetric key storage
  - Asymmetric key storage
- **Key storage principles**:
  - Confidentiality
  - Integrity

### Key Usage

- **Key usage guidelines**:
  - Use of keys for encryption and decryption
  - Use of keys for digital signatures
- **Key usage principles**:
  - Separation of duties
  - Key rotation

### Governing Key Management

- **Key management policies**:
  - Key generation policies
  - Key distribution policies
  - Key revocation policies
- **Key management frameworks**:
  - NIST Special Publication 800-57
  - ISO/IEC 9796-1

### Important Formulas and Theorems

- **Diffie-Hellman key exchange**:
  - $g^{ab} = g^{ac} \mod p$
- **RSA encryption**:
  - $c = m^e \mod n$
- **Hash function**:
  - $h(x) = F(x) \mod m$
