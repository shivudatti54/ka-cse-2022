# Description of the RSA Algorithm


## Table of Contents

- [Description of the RSA Algorithm](#description-of-the-rsa-algorithm)
- [Introduction](#introduction)
- [Mathematical Foundations](#mathematical-foundations)
  - [Prime Numbers](#prime-numbers)
  - [Euler's Totient Function φ(n)](#eulers-totient-function-n)
  - [Modular Arithmetic](#modular-arithmetic)
  - [Extended Euclidean Algorithm](#extended-euclidean-algorithm)
- [RSA Algorithm Steps](#rsa-algorithm-steps)
  - [1. Key Generation](#1-key-generation)
  - [2. Encryption](#2-encryption)
  - [3. Decryption](#3-decryption)
- [Proof of Correctness](#proof-of-correctness)
- [Examples](#examples)
  - [Example 1: Textbook RSA](#example-1-textbook-rsa)
  - [Example 2: Realistic Parameters](#example-2-realistic-parameters)
- [Security Considerations](#security-considerations)
- [Real-World Applications](#real-world-applications)
- [Exam Tips](#exam-tips)

## Introduction

The RSA algorithm (1977) revolutionized cryptography by introducing the first practical public-key cryptosystem. Named after Rivest, Shamir, and Adleman, RSA enables secure data transmission through asymmetric cryptography where users have public encryption keys and private decryption keys. Its security relies on the computational difficulty of factoring large integers - a problem that remains intractable despite decades of research.

RSA forms the backbone of modern secure communication systems including SSL/TLS (HTTPS), digital signatures, and secure email. Understanding its algorithmic details is crucial for implementing secure systems and analyzing cryptographic vulnerabilities. The syllabus emphasizes mastery of RSA's mathematical foundations and implementation steps for both theoretical and practical examinations.

## Mathematical Foundations

### Prime Numbers

- **Definition**: Natural numbers >1 divisible only by 1 and themselves
- **Key Property**: Product (n = p×q) of two large primes is easy to compute but extremely hard to factor
- **Example**: 61 and 53 are primes → n = 61×53 = 3233

### Euler's Totient Function φ(n)

- Counts integers <n coprime to n
- **For primes**: φ(p) = p-1
- **For n=pq**: φ(n) = (p-1)(q-1)
- **Example**: φ(3233) = (61-1)(53-1) = 60×52 = 3120

### Modular Arithmetic

- **Modular Inverse**: d ≡ e⁻¹ mod φ(n) exists iff gcd(e, φ(n)) = 1
- **Euler's Theorem**: If a & n coprime, a<sup>φ(n)</sup> ≡ 1 mod n

### Extended Euclidean Algorithm

Finds integers x,y such that:  
ax + by = gcd(a,b)  
Used to compute private key d from e and φ(n)

## RSA Algorithm Steps

### 1. Key Generation

**Step 1**: Choose two large primes p and q

```math
p = 61, q = 53 (example values)
```

**Step 2**: Compute modulus n

```math
n = p × q = 61 × 53 = 3233
```

**Step 3**: Compute φ(n)

```math
φ(n) = (p-1)(q-1) = 60 × 52 = 3120
```

**Step 4**: Choose public exponent e  
Conditions:

1. 1 < e < φ(n)
2. gcd(e, φ(n)) = 1

```math
e = 17 (common choices: 3, 17, 65537)
```

**Step 5**: Compute private key d  
Solve: d ≡ e⁻¹ mod φ(n)  
Using Extended Euclidean Algorithm:  
17d ≡ 1 mod 3120 → d = 2753

**Public Key**: (e, n) = (17, 3233)  
**Private Key**: (d, n) = (2753, 3233)

### 2. Encryption

For plaintext message m < n:

```math
c ≡ m^e mod n
```

**Example**: Encrypt m=65

```math
c = 65¹⁷ mod 3233 = 2790
```

### 3. Decryption

Using private key d:

```math
m ≡ c^d mod n
```

**Example**: Decrypt c=2790

```math
m = 2790²⁷⁵³ mod 3233 = 65
```

## Proof of Correctness

From Euler's Theorem:  
m<sup>kφ(n)+1</sup> ≡ m mod n  
Since ed ≡ 1 mod φ(n), ed = kφ(n)+1  
Thus:  
c<sup>d</sup> ≡ (m<sup>e</sup>)<sup>d</sup> ≡ m<sup>ed</sup> ≡ m mod n

## Examples

### Example 1: Textbook RSA

**Parameters**:  
p=3, q=11, n=33, φ(n)=20  
Choose e=3 → d=7 (since 3×7=21≡1 mod 20)

**Encrypt m=7**:  
c = 7³ mod 33 = 343 mod 33 = 13

**Decrypt c=13**:  
m = 13⁷ mod 33  
= (13²)³ × 13 mod 33  
= (169 mod 33)³ × 13  
= (4³) × 13 = 64 × 13 mod 33  
= 832 mod 33 = 7

### Example 2: Realistic Parameters

**Key Generation**:  
p=101, q=113 → n=11413  
φ(n)=100×112=11200  
Choose e=103  
Compute d ≡ 103⁻¹ mod 11200 = 5327

**Encrypt m=5000**:  
c = 5000¹⁰³ mod 11413  
= 9012 (using square-and-multiply)

**Decrypt c=9012**:  
m = 9012⁵³²⁷ mod 11413 = 5000

## Security Considerations

1. **Factoring Problem**: Security relies on difficulty of factoring n=pq
2. **Key Size**: Minimum 2048-bit recommended (617 decimal digits)
3. **Padding**: Raw RSA is insecure - always use OAEP/PKCS1 v1.5 padding
4. **Side-channel Attacks**: Implementations must prevent timing attacks

## Real-World Applications

1. **SSL/TLS Handshake**: RSA used for key exchange in HTTPS
2. **Digital Signatures**: RSA with SHA-256 for document signing
3. **Secure Email**: PGP and S/MIME use RSA for encryption
4. **SSH Authentication**: Key-based login using RSA key pairs

## Exam Tips

1. **Memorize the 5 Key Generation Steps** in order (p/q → n → φ(n) → e → d)
2. **Always Verify gcd(e, φ(n))=1** when choosing public exponent
3. **Show All Intermediate Steps** for modular exponentiation calculations
4. **Remember φ(n) Formula**: (p-1)(q-1) not p\*q-1
5. **Use Extended Euclidean Algorithm** properly for finding d
6. **State Security Basis** clearly ("Factoring Problem" for 2 marks)
7. **Note Message Limitations**: m must be <n and coprime to n (though latter is probable)
