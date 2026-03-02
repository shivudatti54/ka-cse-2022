# RSA Algorithm: A Cornerstone of Public Key Cryptography

## Introduction to Public Key Cryptography

Public Key Cryptography, also known as asymmetric cryptography, represents a fundamental shift from the classical symmetric encryption techniques covered in Module-1. Unlike symmetric ciphers like DES, Caesar, or Hill ciphers, which use a single shared key for both encryption and decryption, asymmetric cryptography employs a pair of mathematically related keys:

*   A **Public Key**: Used for encryption. This key can be freely distributed to anyone.
*   A **Private Key**: Used for decryption. This key is kept secret by the owner.

This model solves the critical **key distribution problem** inherent in symmetric systems. The RSA algorithm, named after its inventors **Rivest, Shamir, and Adleman** (1977), is the most widely used implementation of public key cryptography. It facilitates:
*   **Encryption/Decryption**: Securing message confidentiality.
*   **Digital Signatures**: Providing authentication, non-repudiation, and message integrity.

## Mathematical Foundations of RSA

The security of RSA relies on the computational difficulty of specific mathematical problems.

### 1. Prime Numbers and Coprimality
A **prime number** is a natural number greater than 1 that has no positive divisors other than 1 and itself. RSA's security is based on using two large prime numbers. Two numbers are **coprime** (or relatively prime) if their Greatest Common Divisor (GCD) is 1. For example, GCD(15, 28) = 1, so they are coprime.

### 2. Euler's Totient Function φ(n)
Euler's totient function, φ(n), is crucial for RSA. It is defined as the number of positive integers less than `n` that are coprime to `n`.
*   For a prime number `p`: φ(p) = p - 1.
*   For the product of two distinct primes `p` and `q`: φ(n) = φ(p*q) = (p-1)(q-1). This is because the numbers that are *not* coprime to `n` are multiples of `p` and `q`.

**Example**: Let p=3, q=5. Then n=15. φ(15) = φ(3)*φ(5) = (3-1)*(5-1) = 2*4 = 8. The numbers coprime to 15 are: 1, 2, 4, 7, 8, 11, 13, 14.

### 3. The Core Problem: Integer Factorization
RSA's security hinges on the **Integer Factorization Problem**: it is computationally easy to multiply two large primes, `p` and `q`, to get `n`, but it is computationally infeasible to factorize a large composite number `n` back into its prime factors `p` and `q`. This is a **one-way function**.

## The RSA Algorithm: Step-by-Step

The algorithm involves three main processes: Key Generation, Encryption, and Decryption.

### 1. Key Generation
This process creates the public and private key pair.

1.  **Select two large prime numbers**: Choose two large, random prime numbers, `p` and `q`.
2.  **Compute n**: Calculate `n = p * q`. This `n` is the modulus for both the public and private keys. Its length in bits is the **key length** (e.g., 2048, 4096).
3.  **Compute φ(n)**: Calculate Euler's totient function for `n`: `φ(n) = (p-1)(q-1)`.
4.  **Choose public exponent `e`**: Select an integer `e` such that:
    *   1 < e < φ(n)
    *   `e` is coprime to φ(n) (i.e., GCD(e, φ(n)) = 1).
    *   Common choices are 3 or 65,537 (2^16 + 1) for efficiency reasons in encryption.
5.  **Determine private exponent `d`**: Calculate `d` as the **modular multiplicative inverse** of `e modulo φ(n)`. This means:
    *   `d ≡ e⁻¹ mod φ(n)`
    *   Or, more clearly: `(d * e) mod φ(n) = 1`

The **Public Key** is the pair `(e, n)`.
The **Private Key** is the pair `(d, n)`.

**Key Generation Example**:
1.  Let p = 61, q = 53 (small primes for demonstration).
2.  n = p * q = 61 * 53 = **3233**
3.  φ(n) = (61-1)(53-1) = 60 * 52 = **3120**
4.  Choose e such that 1 < e < 3120 and coprime to 3120. Let e = **17**.
5.  Find d such that (d * 17) mod 3120 = 1.
    *   d = **2753** (since 2753 * 17 = 46801, and 46801 mod 3120 = 1).

Public Key: (17, 3233)
Private Key: (2753, 3233)

### 2. Encryption
To encrypt a plaintext message `M` (where `M` is an integer representing the data, and `M < n`), the sender uses the recipient's public key `(e, n)` and computes the ciphertext `C`:
**C = Mᵉ mod n**

**Encryption Example**:
Let the plaintext M = 65 (the ASCII value for 'A').
Using public key (e=17, n=3233):
C = 65¹⁷ mod 3233
Calculating this: 65¹⁷ is a huge number, but we compute the modulus step-by-step efficiently. The result is **2790**.
So, ciphertext C = 2790.

### 3. Decryption
To decrypt the ciphertext `C`, the recipient uses their private key `(d, n)` and computes:
**M = Cᵈ mod n**

**Decryption Example**:
Using private key (d=2753, n=3233) and ciphertext C=2790:
M = 2790²⁷⁵³ mod 3233
Again, this seems daunting, but modular exponentiation makes it feasible. The result is **65**, which is the original plaintext.

```
+----------------+     Public Key (e,n)     +-----------------+
| SENDER         | ---------------------->  | RECIPIENT       |
|                |                          |                 |
| M = Plaintext  |                          | Private Key (d) |
| C = Mᵉ mod n   |                          | M = Cᵈ mod n    |
+----------------+     Ciphertext (C)       +-----------------+
                          -------->
```

## RSA for Digital Signatures

The same principle can be reversed to create digital signatures, providing authentication and non-repudiation.

1.  **Signing**: The sender uses their *own private key* to encrypt a hash of the message.
    *   Signature S = Hash(M)ᵈ mod n
2.  **Verification**: The receiver uses the sender's *public key* to decrypt the signature and compares it to their own calculation of the message hash.
    *   If Hash(M) == Sᵉ mod n, the signature is verified.

```
+----------------+     Public Key (e,n)     +-----------------+
| SIGNER         | ---------------------->  | VERIFIER       |
|                |                          |                 |
| M = Message    |                          |                 |
| S = H(M)ᵈ mod n|                          | Check: H(M) ≟ Sᵉ mod n |
+----------------+     Message + S          +-----------------+
                          -------->
```

## Practical Considerations and Security

*   **Key Size**: The security of RSA depends on the key length. 1024-bit keys are now considered breakable with sufficient resources. 2048-bit is a current minimum standard, with 4096-bit recommended for long-term security.
*   **Padding**: Raw RSA (as described above) is deterministic and vulnerable to attacks. In practice, schemes like **OAEP (Optimal Asymmetric Encryption Padding)** or **PSS (Probabilistic Signature Scheme)** are used to add randomness and security before the modular exponentiation step.
*   **Computational Cost**: RSA operations (encryption/decryption, signing/verification) are computationally expensive compared to symmetric encryption. It is often used to securely exchange a symmetric session key (like an AES key), which is then used to encrypt the actual bulk data. This is called a **hybrid cryptosystem**.

### Comparison of RSA and Symmetric Ciphers (e.g., AES)

| Feature | RSA (Asymmetric) | AES (Symmetric) |
| :--- | :--- | :--- |
| **Key Type** | Public/Private Key Pair | Single Shared Secret Key |
| **Key Distribution** | Solves the key exchange problem | Difficult; requires secure channel |
| **Speed** | Slow (due to complex math) | Very Fast (optimized for hardware) |
| **Primary Use** | Key exchange, digital signatures, encrypting small data | Bulk data encryption |
| **Key Length** | 2048+ bits for security | 128/256 bits for security |

## Exam Tips

1.  **Memorize the Formulas**: Be able to write down the key generation, encryption, and decryption formulas without hesitation. `C = Mᵉ mod n` and `M = Cᵈ mod n` are the core.
2.  **Practice a Numerical Example**: You will almost certainly be asked to work through a small-scale example (like the one with p=61, q=53). Practice this repeatedly until you can do it quickly and accurately. Remember the steps: calculate `n`, calculate `φ(n)`, choose `e`, find `d`.
3.  **Understand "Why"**: Don't just memorize steps. Understand that `d` is the modular inverse of `e` and why Euler's theorem makes the decryption process work. Be prepared to explain the integer factorization problem.
4.  **Know the Applications**: Be ready to explain how RSA is used for both encryption and digital signatures, and why hybrid systems (RSA + AES) are common.
5.  **Security Factors**: Be prepared to discuss what makes RSA secure (large prime factorization) and what potential weaknesses are (small `e` attacks, side-channel attacks, need for proper padding).