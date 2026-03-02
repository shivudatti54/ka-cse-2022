# **20.3 Data Encryption**

### Definition

Data encryption is the process of converting plaintext data into unreadable ciphertext to protect it from unauthorized access. It involves the use of algorithms and cryptographic techniques to transform the data into a secure format.

### Types of Encryption

- **Symmetric Key Encryption**: Uses the same key for encryption and decryption.
- **Asymmetric Key Encryption**: Uses a pair of keys, one public and one private, for encryption and decryption.

### Encryption Techniques

- **Block Cipher**: Divides plaintext into fixed-length blocks and encrypts each block independently.
- **Stream Cipher**: Encrypts plaintext in a continuous stream of bits.

### Challenges

- **Key Management**: Secure key generation, distribution, and revocation.
- **Computational Complexity**: Encryption and decryption processes can be computationally intensive.

### Real-World Applications

- **Secure Online Transactions**: Encryption is used to protect credit card information and other sensitive data.
- **Secure Communication**: Encryption is used to protect email, instant messaging, and voice communications.

### Example of Symmetric Key Encryption

Suppose we want to encrypt the plaintext message "HELLO" using the AES symmetric key encryption algorithm.

| Step | Operation          | Plaintext                | Ciphertext                                                                                                                        |
| ---- | ------------------ | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Divide into blocks | HELLO                    | 4 blocks                                                                                                                          |
| 2    | Initialize key     | AES-256                  |                                                                                                                                   |
| 3    | Encrypt each block | 0x48 0x65 0x6c 0x6c 0x6f | 0x8d 0x0c 0x31 0x5e 0x6c 0x9e                                                                                                     |
| 4    | Combine blocks     |                          | 0x8d 0x0c 0x31 0x5e 0x6c 0x9e 0x3c 0x6c 0x2c 0x6f 0x5c 0x65 0x63 0x6f 0x72 0x6e 0x6d 0x5a 0x44 0x61 0x6e 0x67 0x65 0x72 0x34 0x34 |

# **20.4 Data Masking**

### Definition

Data masking is a technique used to protect sensitive data by replacing it with dummy or placeholder data. The goal is to prevent unauthorized access to sensitive information while still allowing authorized access to the data.

### Types of Data Masking

- **Field-Based Masking**: Replaces sensitive data in specific fields or columns.
- **Record-Based Masking**: Replaces entire records or rows of data.
- **Row-Level Masking**: Replaces specific rows of data based on conditions.

### Techniques

- **Hashing**: Uses algorithms to transform sensitive data into a fixed-length string of characters.
- **Encryption**: Uses algorithms to transform sensitive data into unreadable ciphertext.
- **Pseudonymization**: Replaces sensitive data with a unique identifier or pseudonym.

### Benefits

- **Reduced Risk**: Protects sensitive data from unauthorized access.
- **Compliance**: Helps organizations meet regulatory requirements for data protection.
- **Improved Security**: Enhances overall security posture by reducing the risk of data breaches.

### Example of Data Masking

Suppose we want to mask sensitive credit card numbers in a database.

| Field            | Value                |
| ---------------- | -------------------- |
| Card Number      | ****\*\*\*\*****1234 |
| Last Four Digits | 2345                 |

In this example, the sensitive credit card number is masked with asterisks (\*), and the last four digits are displayed to allow for easy identification of the card number.
