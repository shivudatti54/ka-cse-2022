# **One-time Pad Revision Notes**

### Definitions

- **One-time Pad**: A cryptographic technique that uses a random and unique key that is as long as the message being encrypted.
- **Key exchange**: The process of securely exchanging the one-time pad key between parties.

### Important Formulas and Theorems

- **Hash function**: A one-way function that takes input data of any size and produces a fixed-size string of characters, known as a message digest.
- **Block cipher**: A type of encryption algorithm that operates on fixed-length blocks of data.
- **Vigenère cipher**: A polyalphabetic substitution cipher that uses a keyword to encrypt and decrypt messages.

### Key Points

- **One-time Pad Properties**:
  - Unbreakable without the key
  - No storage of the key is required
  - Any length of message can be encrypted
- **Key Exchange Methods**:
  - Public-key cryptography (e.g., RSA)
  - Quantum key distribution (QKD)
- **Advantages**:
  - Unbreakable encryption
  - Secure key exchange
- **Disadvantages**:
  - Requires secure key exchange
  - Difficult to implement in practice

### Important Concepts

- **Confusion-Diffusion Theory**: A method of designing block ciphers that ensures no single bit of the plaintext can be related to any single bit of the ciphertext.
- **Key size**: The number of bits in the one-time pad key.
- **Key renewal**: The process of generating a new one-time pad key for each message.

### Key Theorems

- **Frequency analysis theorem**: States that any linear transformation can be represented by a linear equation, allowing for cryptanalysis.
- **Probabilistic encryption theorem**: States that if a cryptosystem can be broken with probability less than 1/2, it is not secure.

### Quick Revision Tips

- One-time pad is unbreakable without the key
- Key exchange is critical to its security
- Difficult to implement in practice due to key exchange requirements
- Confusion-diffusion theory is used to design block ciphers.
