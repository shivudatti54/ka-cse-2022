# Public Key Encryption

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University

---

## 1. Introduction to Public Key Encryption

### 1.1 The Need for Asymmetric Cryptography

Traditional **symmetric encryption** uses a single secret key for both encryption and decryption. While efficient, it introduces a fundamental problem: **key distribution**. Before secure communication can begin, both parties must somehow exchange the secret key securely. In a network with n users, approximately n(n-1)/2 unique keys are needed, making key management exponentially complex as the system grows.

**Public Key Encryption**, also known as **Asymmetric Cryptography**, revolutionizes this by using **two mathematically related keys**:

- **Public Key**: Freely distributed and used for encryption
- **Private Key**: Kept secret and used for decryption

This elegant solution, conceived by Whitfield Diffie and Martin Hellman in 1976 (published as "New Directions in Cryptography"), addresses the key distribution problem while enabling digital signatures and authentication mechanisms.

### 1.2 Real-World Relevance

Public key encryption forms the backbone of modern digital security:

| Application | How Public Key Encryption is Used |
|-------------|-----------------------------------|
| **Secure Web Browsing (HTTPS)** | SSL/TLS certificates use public key encryption to establish secure connections |
| **Digital Signatures** | Authenticate document origin and integrity |
| **Email Encryption (PGP, S/MIME)** | Ensure confidentiality of electronic correspondence |
| **Cryptocurrency** | Bitcoin and other cryptocurrencies rely on elliptic curve cryptography for wallet security |
| **Online Banking** | Secure transaction authentication |
| **VPN Connections** | Key exchange for establishing encrypted tunnels |

---

## 2. Fundamental Mathematical Concepts

### 2.1 One-Way Functions

A **one-way function** is easy to compute in one direction but computationally infeasible to reverse:

- **Forward direction**: f(x) → y (easy)
- **Reverse direction**: y → x (hard)

**Example**: Multiplication of two large prime numbers is easy, but factoring the product back to original primes is computationally hard for large numbers.

### 2.2 Trapdoor Functions

A **trapdoor one-way function** is a one-way function that becomes reversible if you possess a specific piece of information (the trapdoor):

```
f(x, trapdoor) → x (easy with trapdoor)
f(x) → y (hard without trapdoor)
```

This trapdoor is the **private key** in public key cryptosystems.

### 2.3 Number Theory Foundations

Understanding public key encryption requires familiarity with these mathematical concepts:

- **Modular Arithmetic**: Operations performed with a fixed modulus n
  - Example: 17 mod 5 = 2
  
- **Euler's Totient Function φ(n)**: Counts integers from 1 to n that are coprime to n
  - For prime p: φ(p) = p - 1
  - For pq (where p and q are primes): φ(pq) = (p-1)(q-1)

- **Greatest Common Divisor (gcd)**: Two numbers are coprime if gcd(a, b) = 1

- **Modular Inverse**: a⁻¹ mod n such that (a × a⁻¹) ≡ 1 (mod n)

---

## 3. RSA Algorithm — The Cornerstone of Public Key Encryption

### 3.1 Historical Background

RSA (Rivest-Shamir-Adleman) was developed in 1977 by Ron Rivest, Adi Shamir, and Leonard Adleman at MIT. It remains the most widely used public key cryptosystem, securing billions of transactions daily.

### 3.2 RSA Key Generation

**Step 1: Select Two Large Primes**
Choose two distinct large prime numbers, p and q.

**Step 2: Compute n (Public Modulus)**
```
n = p × q
```
n is made public and forms part of the encryption/decryption process.

**Step 3: Compute Euler's Totient**
```
φ(n) = (p - 1) × (q - 1)
```

**Step 3: Choose Public Exponent e**
Select an integer e such that:
- 1 < e < φ(n)
- gcd(e, φ(n)) = 1 (e and φ(n) are coprime)

Common choices for e: 3, 17, 65537 (chosen for efficiency)

**Step 4: Compute Private Exponent d**
Find d such that:
```
(e × d) mod φ(n) = 1
```
Or equivalently:
```
d ≡ e⁻¹ (mod φ(n))
```

**Result:**
- **Public Key**: (e, n)
- **Private Key**: (d, n)

### 3.3 RSA Encryption and Decryption

**Encryption (using Public Key):**
```
Ciphertext = Plaintext^e mod n
```
Where plaintext is converted to an integer m such that 0 ≤ m < n.

**Decryption (using Private Key):**
```
Plaintext = Ciphertext^d mod n
```

### 3.4 Mathematical Proof (Why RSA Works)

The security of RSA relies on the **mathematical relationship** between the keys:

Given: n = p × q, and d ≡ e⁻¹ (mod φ(n))

By Euler's theorem, for any integer m coprime to n:
```
m^φ(n) ≡ 1 (mod n)
```

Since d ≡ e⁻¹ (mod φ(n)), we can write:
```
e × d = 1 + k × φ(n) for some integer k
```

Therefore:
```
(m^e)^d ≡ m^(1+k×φ(n)) ≡ m × (m^φ(n))^k ≡ m × 1^k ≡ m (mod n)
```

This proves that decryption successfully recovers the original message.

### 3.5 Numerical Example

Let's work through a small-scale example:

**Key Generation:**
1. Select primes: p = 3, q = 11
2. Compute n = 3 × 11 = 33
3. Compute φ(n) = (3-1)(11-1) = 2 × 10 = 20
4. Choose e = 3 (gcd(3, 20) = 1 ✓)
5. Find d: 3 × d ≡ 1 (mod 20)
   - 3 × 7 = 21 ≡ 1 (mod 20)
   - Therefore, d = 7

**Keys:**
- Public Key: (e=3, n=33)
- Private Key: (d=7, n=33)

**Encryption:**
Message m = 2
```
C = 2^3 mod 33 = 8 mod 33 = 8
```

**Decryption:**
```
M = 8^7 mod 33
8^2 = 64 ≡ 31 mod 33
8^4 ≡ 31^2 = 961 ≡ 25 mod 33
8^7 = 8^4 × 8^2 × 8^1 ≡ 25 × 31 × 8 ≡ 25 × 248 ≡ 25 × 26 ≡ 650 ≡ 2 mod 33
```
Original message recovered: 2 ✓

### 3.6 Security of RSA

RSA security relies on:

1. **Integer Factorization Problem**: Hard to factor large n into p and q
2. **Current Recommendations**:
   - Minimum key size: 2048 bits (recommended for long-term security)
   - For quantum resistance: 4096 bits or post-quantum algorithms

**Attacks on RSA:**
- **Brute Force**: Try all possible factors (infeasible for large keys)
- **Timing Attacks**: Exploit decryption time variations
- ** chosen Ciphertext Attacks (CCA)**: Use decryption oracle

---

## 4. ElGamal Encryption Algorithm

### 4.1 Overview

Developed by Taher ElGamal in 1985, ElGamal is based on the **discrete logarithm problem**. Unlike RSA, it produces ciphertext that is twice the size of the plaintext.

### 4.2 Key Generation

1. Select a large prime p
2. Choose a generator g (primitive root of p)
3. Select private key x such that 1 < x < p-1
4. Compute public key y = g^x mod p
5. Public Key: (p, g, y), Private Key: x

### 4.3 Encryption and Decryption

**Encryption:**
```
Choose random k (1 < k < p-1) where gcd(k, p-1) = 1
c1 = g^k mod p
c2 = (m × y^k) mod p
Ciphertext: (c1, c2)
```

**Decryption:**
```
m = c2 × (c1^x)^(-1) mod p
```
Since (c1^x) = (g^k)^x = g^(kx) = y^k

### 4.4 Numerical Example

**Setup:**
- p = 23
- g = 5 (generator)
- Private key: x = 7
- Public key: y = 5^7 mod 23 = 78125 mod 23 = 17

**Keys:**
- Public: (p=23, g=5, y=17)
- Private: x = 7

**Encryption (message m = 13):**
- Choose k = 5
- c1 = 5^5 mod 23 = 3125 mod 23 = 20
- c2 = 13 × 17^5 mod 23
  - 17^2 = 289 ≡ 13 mod 23
  - 17^4 ≡ 13^2 = 169 ≡ 8 mod 23
  - 17^5 ≡ 8 × 17 = 136 ≡ 18 mod 23
  - c2 = 13 × 18 = 234 ≡ 4 mod 23

- Ciphertext: (20, 4)

**Decryption:**
- c1^x = 20^7 mod 23
- 20^2 = 400 ≡ 8 mod 23
- 20^4 ≡ 8^2 = 64 ≡ 18 mod 23
- 20^7 = 20^4 × 20^2 × 20 ≡ 18 × 8 × 20 ≡ 2880 ≡ 6 mod 23
- Inverse of 6 mod 23: 6 × 4 = 24 ≡ 1, so inverse = 4
- m = 4 × 4 = 16 ≡ 16 mod 23

Wait, let me recalculate:
- m = c2 × (c1^x)^(-1) mod 23
- (c1^x) = 6, inverse of 6 is 4
- m = 4 × 4 = 16

Original message: 13 ≠ 16 — There's an error in calculation. Let me recalculate:

c2 = 13 × 17^5 mod 23
17^5: 17^2 = 289 ≡ 289 - 276 = 13
17^4 = 13^2 = 169 ≡ 169 - 161 = 8
17^5 = 17^4 × 17 = 8 × 17 = 136 ≡ 136 - 115 = 21
c2 = 13 × 21 = 273 ≡ 273 - 253 = 20

Ciphertext: (20, 20)

Decryption:
c1^x = 20^7 mod 23
20^2 = 400 ≡ 400 - 368 = 32 ≡ 9
Wait, 400 - 23×17 = 400 - 391 = 9

20^4 ≡ 9^2 = 81 ≡ 12
20^7 = 20^4 × 20^2 × 20 ≡ 12 × 9 × 20 = 2160 ≡ 2160 - 23×93 = 2160 - 2139 = 21

Inverse of 21 mod 23: 21 × 11 = 231 ≡ 1, so inverse = 11
m = 20 × 11 = 220 ≡ 220 - 207 = 13 ✓

---

## 5. Elliptic Curve Cryptography (ECC)

### 5.1 Introduction

ECC represents the next generation of public key cryptography. It provides equivalent security to RSA with significantly smaller key sizes, making it ideal for mobile devices and constrained environments.

### 5.2 Mathematical Foundation

An **elliptic curve** is defined by the equation:
```
y² = x³ + ax + b (mod p)
```
Where 4a³ + 27b² ≠ 0 (to avoid singular points)

### 5.3 Key Advantages of ECC

| Security Level | RSA Key Size | ECC Key Size |
|----------------|--------------|--------------|
| 80 bits        | 1024 bits    | 160 bits     |
| 128 bits       | 3072 bits    | 256 bits     |
| 256 bits       | 15360 bits   | 512 bits     |

**Advantages:**
- Smaller key sizes → faster computation
- Lower storage requirements
- Ideal for mobile and IoT devices
- Used in: Bitcoin, SSL/TLS, Smart Cards

### 5.4 ECC in Practice

Common elliptic curves:
- P-256 (NIST recommended)
- Curve25519 (modern, efficient)

**Example Use Case:**
The Bitcoin cryptocurrency uses **secp256k1** curve for digital signatures:
```
y² = x³ + 7 (mod p)
```
where p = 2^256 - 2^32 - 977

---

## 6. Public Key Infrastructure (PKI)

### 6.1 The Trust Problem

Public keys must be authenticated — how do you know a public key truly belongs to the claimed entity? This is the **key distribution problem** solved by PKI.

### 6.2 Components of PKI

**1. Digital Certificates**
A digital certificate binds a public key to an entity's identity, signed by a trusted Certificate Authority (CA).

X.509 Certificate Structure:
- Version
- Serial Number
- Signature Algorithm
- Issuer Name
- Validity Period
- Subject Name
- Subject Public Key
- Extensions

**2. Certificate Authorities (CA)**
Trusted third parties that issue and manage digital certificates:
- Root CAs: Self-signed, trusted implicitly
- Intermediate CAs: Certificates issued by root CAs
- End-entity certificates: Issued to organizations/individuals

**3. Certificate Chain (Chain of Trust)**
```
Root CA Certificate
    ↓ signs
Intermediate CA Certificate
    ↓ signs
End-Entity Certificate (e.g., google.com)
```

**4. Registration Authority (RA)**
Verifies identity before certificate issuance

**5. Certificate Revocation List (CRL) / OCSP**
Mechanisms to revoke compromised certificates

### 6.3 TLS/SSL Handshake (PKI in Action)

```
Client                                    Server
  |                                          |
  |----------- Client Hello ---------------→|
  |                                          |
  |←---------- Server Hello ----------------|
  |          (Certificate)                   |
  |                                          |
  |          (Key Exchange)                  |
  |                                          |
  |----------- Finished --------------------|
  |                                          |
  |←----------- Finished -------------------|
  |                                          |
  |======= Encrypted Data ==================|
```

---

## 7. Sample Code Implementations

### 7.1 RSA Implementation in Python

```python
import math
import random

def is_prime(n, k=40):
    """Miller-Rabin primality test"""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    """Generate a random prime number"""
    while True:
        p = random.getrandbits(bits)
        p |= (1 << (bits - 1)) | 1  # Set MSB and LSB to 1
        if is_prime(p):
            return p

def extended_gcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    """Compute modular multiplicative inverse"""
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

def generate_rsa_keys(bits=512):
    """Generate RSA key pair"""
    # Generate two primes
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    
    # Compute n and phi
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose public exponent
    e = 65537  # Common choice
    
    # Compute private exponent
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)

def rsa_encrypt(plaintext, public_key):
    """RSA Encryption"""
    e, n = public_key
    # Convert characters to numbers and encrypt
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    """RSA Decryption"""
    d, n = private_key
    # Decrypt and convert back to characters
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Demo
if __name__ == "__main__":
    print("Generating 512-bit RSA keys...")
    public_key, private_key = generate_rsa_keys(512)
    print(f"Public Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")
    
    message = "Hello DU"
    print(f"\nOriginal Message: {message}")
    
    ciphertext = rsa_encrypt(message, public_key)
    print(f"Encrypted: {ciphertext}")
    
    decrypted = rsa_decrypt(ciphertext, private_key)
    print(f"Decrypted: {decrypted}")
```

### 7.2 ElGamal Implementation in Python

```python
import random
import math

def is_prime(n):
    """Basic primality test"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_generator(p):
    """Find a generator for the multiplicative group Zp*"""
    if not is_prime(p):
        return None
    
    # Factorize p-1
    factors = []
    n = p - 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        factors.append(n)
    
    # Find generator
    for g in range(2, p):
        is_gen = True
        for factor in factors:
            if pow(g, (p - 1) // factor, p) == 1:
                is_gen = False
                break
        if is_gen:
            return g
    return None

def generate_elgamal_keys(p=None):
    """Generate ElGamal key pair"""
    if p is None:
        # Use a smaller prime for demonstration
        p = 23
    
    g = find_generator(p)
    x = random.randint(2, p - 2)  # Private key
    y = pow(g, x, p)              # Public key
    
    return (p, g, y), x

def elgamal_encrypt(message, public_key, k=None):
    """ElGamal Encryption"""
    p, g, y = public_key
    
    # Choose random k
    if k is None:
        k = random.randint(2, p - 2)
    
    # Ensure k is coprime to p-1
    while math.gcd(k, p - 1) != 1:
        k = random.randint(2, p - 2)
    
    c1 = pow(g, k, p)
    m = ord(message)
    c2 = (m * pow(y, k, p)) % p
    
    return c1, c2

def elgamal_decrypt(c1, c2, private_key, p):
    """ElGamal Decryption"""
    x = private_key
    
    # Compute c1^x
    s = pow(c1, x, p)
    
    # Find modular inverse of s
    s_inv = pow(s, -1, p)
    
    m = (c2 * s_inv) % p
    return chr(m)

# Demo
if __name__ == "__main__":
    print("Generating ElGamal keys...")
    public_key, private_key = generate_elgamal_keys(23)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    message = "A"
    print(f"\nOriginal Message: {message}")
    
    c1, c2 = elgamal_encrypt(message, public_key, k=5)
    print(f"Encrypted (c1, c2): ({c1}, {c2})")
    
    decrypted = elgamal_decrypt(c1, c2, private_key, public_key[0])
    print(f"Decrypted: {decrypted}")
```

---

## 8. Important Numerical Problems

### 8.1 RSA Numerical Problems

**Problem 1:** Given p = 7, q = 11, e = 13, find the private key d and demonstrate encryption/decryption of message m = 5.

**Solution:**
- n = 7 × 11 = 77
- φ(n) = (7-1)(11-1) = 6 × 10 = 60
- Need d such that 13 × d ≡ 1 (mod 60)
- 13 × 37 = 481 ≡ 1 (mod 60)
- d = 37

Encryption: C = 5^13 mod 77 = ?

**Problem 2:** Using RSA with p = 5, q = 11, e = 3:
(a) Compute n, φ(n), and d
(b) Encrypt m = 9
(c) Decrypt the ciphertext

**Solution:**
(a) n = 55, φ(n) = 40, d = 27 (since 3 × 27 = 81 ≡ 1 mod 40)
(b) C = 9^3 mod 55 = 729 mod 55 = 14
(c) M = 14^27 mod 55 = 9 ✓

### 8.2 ElGamal Numerical Problems

**Problem 1:** In ElGamal with p = 19, g = 2, private key x = 9:
(a) Compute public key y
(b) Encrypt message m = 5 using k = 5
(c) Decrypt the ciphertext

**Solution:**
(a) y = 2^9 mod 19 = 512 mod 19 = 18
(b) c1 = 2^5 mod 19 = 32 mod 19 = 13
    c2 = 5 × 18^5 mod 19
    18^2 = 324 ≡ 1 mod 19
    18^4 ≡ 1 mod 19
    18^5 ≡ 18 mod 19
    c2 = 5 × 18 = 90 ≡ 15 mod 19
    Ciphertext: (13, 15)
(c) Decryption: m = 15 × (13^9)^(-1) mod 19 = 5 ✓

---

## 9. Multiple Choice Questions (University Level)

### Section A: Theoretical Questions

**Q1.** In RSA, if p = 7 and q = 11, what is the value of φ(n)?
- (a) 70
- (b) 77
- (c) 60
- (d) 40

**Q2.** The security of RSA is based on:
- (a) Discrete logarithm problem
- (b) Integer factorization problem
- (c) Elliptic curve discrete logarithm
- (d) Hash collision problem

**Q3.** Which of the following is NOT a property of a trapdoor one-way function?
- (a) Easy to compute in forward direction
- (b) Hard to compute in reverse without trapdoor
- (c) Easy to reverse with trapdoor information
- (d) The trapdoor is made public

**Q4.** In ElGamal encryption, the ciphertext consists of:
- (a) Single component
- (b) Two components (c1, c2)
- (c) Three components
- (d) Variable length

**Q5.** Which algorithm provides equivalent security to RSA with smaller key sizes?
- (a) AES
- (b) DES
- (c) ECC
- (d) SHA-256

### Section B: Application-Based Questions

**Q6.** If RSA uses p = 3, q = 11, e = 3, and message m = 2, what is the ciphertext?
- (a) 6
- (b) 8
- (c) 27
- (d) 2

**Q7.** A digital certificate typically follows which standard?
- (a) X.500
- (b) X.509
- (c) X.600
- (d) X.700

**Q8.** In a PKI hierarchy, which entity verifies identity before certificate issuance?
- (a) CA
- (b) RA
- (c) CRL
- (d) OCSP

**Q9.** The value of φ(21) is:
- (a) 18
- (b) 12
- (c) 20
- (d) 6

**Q10.** In ECC, the key size for 128-bit security compared to RSA is approximately:
- (a) 3072 bits vs 256 bits
- (b) 2048 bits vs 224 bits
- (c) 256 bits vs 3072 bits
- (d) 512 bits vs 15360 bits

### Section C: Advanced Questions

**Q11.** What is the minimum recommended RSA key size for long-term security?
- (a) 512 bits
- (b) 1024 bits
- (c) 2048 bits
- (d) 4096 bits

**Q12.** Which attack exploits variations in decryption time?
- (a) Brute force attack
- (b) Timing attack
- (c) Chosen ciphertext attack
- (d) Birthday attack

**Q13.** In ElGamal, the value k (random exponent) must satisfy:
- (a) k > n
- (b) gcd(k, p-1) = 1
- (c) k = p-1
- (d) k < √p

**Q14.** Which component of PKI maintains a list of revoked certificates?
- (a) CA
- (b) RA
- (c) CRL
- (d) CSR

**Q15.** The public exponent e in RSA is commonly chosen as 65537 because:
- (a) It is prime
- (b) It provides fast encryption (square-and-multiply)
- (c) It is the smallest valid value
- (d) It has no special reason

---

## 10. Key Takeaways

### Core Concepts
1. **Public Key Encryption** solves the key distribution problem of symmetric cryptography by using mathematically related key pairs
2. **One-way functions** and **trapdoor functions** form the mathematical foundation
3. **RSA** remains the most widely deployed public key cryptosystem

### RSA Algorithm
4. **Key Generation**: Select primes p, q → compute n = pq and φ(n) → choose e (coprime to φ(n)) → find d = e⁻¹ mod φ(n)
5. **Security**: Based on integer factorization being computationally hard
6. **Current Standards**: Minimum 2048-bit keys recommended

### Other Algorithms
7. **ElGamal**: Based on discrete logarithm problem, produces ciphertext twice the plaintext size
8. **ECC**: Provides equivalent security with smaller keys (256-bit ECC ≈ 3072-bit RSA)

### PKI and Applications
9. **Digital Certificates** (X.509) bind public keys to entity identities
10. **Certificate Authorities (CAs)** are trusted third parties that issue certificates
11. **PKI** enables secure web browsing (HTTPS), digital signatures, and authenticated key exchange

### Practical Considerations
12. **Hybrid Systems**: Combine asymmetric (key exchange) + symmetric (bulk encryption) for efficiency
13. **Key Management**: Private keys must be protected; compromise breaks security
14. **Quantum Threat**: Future quantum computers may break RSA/ECC; post-quantum cryptography being developed

---

## References and Further Reading

1. Stallings, W. — *Cryptography and Network Security: Principles and Practice*
2. Katz, J., Lindell, Y. — *Introduction to Modern Cryptography*
3. RFC 3447 — PKCS #1: RSA Cryptography Specifications Version 2.2
4. NIST Special Publication 800-57 — Recommendation for Key Management
5. Delhi University BSc (Hons) Computer Science Syllabus — Information Security (NEP 2024 UGCF)

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University as per NEP 2024 UGCF guidelines.*