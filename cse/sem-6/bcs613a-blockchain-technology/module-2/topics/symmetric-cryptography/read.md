# Symmetric Cryptography

## Introduction

Symmetric cryptography (also known as secret-key cryptography) is the oldest and most widely used form of encryption. In symmetric cryptography, the **same key** is used for both encryption and decryption. Both the sender and receiver must share this secret key through a secure channel before they can communicate securely.

While blockchain primarily relies on asymmetric cryptography for digital signatures and key pairs, symmetric cryptography plays an important supporting role in areas like wallet encryption, secure communication between nodes, and key derivation.

## Fundamental Concepts

### How Symmetric Encryption Works

```
Encryption:
 Plaintext + Secret Key --> [Encryption Algorithm] --> Ciphertext

Decryption:
 Ciphertext + Secret Key --> [Decryption Algorithm] --> Plaintext
```

**Key Properties:**

- Same key encrypts and decrypts
- Both parties must securely share the key beforehand
- Much faster than asymmetric cryptography
- Key distribution is the main challenge

### Symmetric vs Asymmetric Cryptography

| Feature              | Symmetric                    | Asymmetric                       |
| -------------------- | ---------------------------- | -------------------------------- |
| **Keys**             | One shared secret key        | Public + Private key pair        |
| **Speed**            | Very fast (100-1000x faster) | Slower                           |
| **Key Length**       | 128-256 bits typical         | 2048-4096 bits (RSA)             |
| **Key Distribution** | Requires secure channel      | Public key can be shared openly  |
| **Primary Use**      | Bulk data encryption         | Digital signatures, key exchange |
| **Example**          | AES, DES, ChaCha20           | RSA, ECC, ECDSA                  |

## Types of Symmetric Ciphers

### 1. Block Ciphers

Block ciphers encrypt data in fixed-size blocks (e.g., 128 bits). If the data is larger than one block, it is divided into multiple blocks.

**Common Block Ciphers:**

- **AES (Advanced Encryption Standard)**: The most widely used symmetric cipher today
- Block size: 128 bits
- Key sizes: 128, 192, or 256 bits
- Rounds: 10, 12, or 14 (based on key size)
- Used in: TLS/SSL, disk encryption, VPNs, wallet encryption

- **DES (Data Encryption Standard)**: Legacy cipher, now considered insecure
- Block size: 64 bits
- Key size: 56 bits
- Replaced by AES due to small key size

- **3DES (Triple DES)**: Applies DES three times with different keys
- Effective key size: 112 bits
- Being phased out in favor of AES

### 2. Stream Ciphers

Stream ciphers encrypt data one bit or byte at a time, generating a pseudorandom keystream from the key.

**Common Stream Ciphers:**

- **ChaCha20**: Modern stream cipher used in TLS 1.3 and many blockchain applications
- **RC4**: Legacy stream cipher, now deprecated due to vulnerabilities

```
Stream Cipher Operation:
 Key --> [PRNG] --> Keystream
 Plaintext XOR Keystream = Ciphertext
 Ciphertext XOR Keystream = Plaintext
```

## AES (Advanced Encryption Standard)

AES is the gold standard for symmetric encryption and is critical in blockchain ecosystems.

### AES Structure

Each round of AES performs four operations:

1. **SubBytes**: Non-linear substitution using an S-box lookup table
2. **ShiftRows**: Cyclical shifting of rows in the state matrix
3. **MixColumns**: Column-wise mixing using matrix multiplication (skipped in last round)
4. **AddRoundKey**: XOR the state with the round key

```
AES Encryption (10 rounds for AES-128):

Plaintext (128 bits)
 |
 v
[AddRoundKey] <-- Round Key 0
 |
 v
[SubBytes -> ShiftRows -> MixColumns -> AddRoundKey] x 9 rounds
 |
 v
[SubBytes -> ShiftRows -> AddRoundKey] (Final round, no MixColumns)
 |
 v
Ciphertext (128 bits)
```

### AES Key Sizes and Rounds

| AES Variant | Key Size | Number of Rounds | Security Level |
| ----------- | -------- | ---------------- | -------------- |
| AES-128     | 128 bits | 10               | Standard       |
| AES-192     | 192 bits | 12               | High           |
| AES-256     | 256 bits | 14               | Very High      |

## Modes of Operation

Block ciphers need a **mode of operation** to handle data larger than one block.

### ECB (Electronic Codebook)

- Each block encrypted independently with the same key
- **Insecure**: Identical plaintext blocks produce identical ciphertext blocks
- Reveals patterns in data

### CBC (Cipher Block Chaining)

- Each block is XORed with the previous ciphertext block before encryption
- Requires an Initialization Vector (IV) for the first block
- More secure than ECB but cannot be parallelized

### CTR (Counter Mode)

- Converts block cipher into stream cipher using incrementing counter
- Can be parallelized for better performance
- Widely used in modern applications

## Role in Blockchain

### 1. Wallet Encryption

Private keys stored in wallets are encrypted using AES-256 with a user-provided passphrase. This protects private keys at rest.

```
Wallet Encryption:
 User Password --> [Key Derivation (PBKDF2/scrypt)] --> AES Key
 Private Key + AES Key --> [AES-256-CBC] --> Encrypted Private Key
```

### 2. Secure Node Communication

Nodes may use symmetric encryption (via TLS) for peer-to-peer communication after establishing shared keys through asymmetric key exchange.

### 3. Key Derivation

Symmetric key derivation functions like PBKDF2 and scrypt are used to derive cryptographic keys from passwords for wallet access.

### 4. Data Encryption in Private Blockchains

Private and consortium blockchains may encrypt transaction data using AES to maintain confidentiality while preserving integrity through hashing.

## Key Distribution Problem

The fundamental challenge of symmetric cryptography is **key distribution**: how do two parties securely share a secret key? Solutions include:

1. **Diffie-Hellman Key Exchange**: Establishes shared secret over insecure channel
2. **Key Encapsulation**: Use asymmetric crypto to encrypt symmetric keys
3. **Pre-shared Keys**: Keys distributed through a trusted channel
4. **Key Derivation Functions**: Derive keys from shared passwords

In blockchain, this problem is largely solved by using asymmetric cryptography for key exchange and authentication, while symmetric cryptography handles bulk encryption tasks.

## Exam Tips

1. Know the difference between block ciphers and stream ciphers with examples
2. Understand AES key sizes, block size, and number of rounds
3. Be able to compare symmetric and asymmetric cryptography
4. Know the modes of operation (ECB, CBC, CTR) and their security properties
5. Understand how symmetric crypto is used in blockchain wallet encryption
6. Remember: symmetric is fast but has key distribution challenges
