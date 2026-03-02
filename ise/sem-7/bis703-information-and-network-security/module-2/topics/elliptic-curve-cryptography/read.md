# Elliptic Curve Cryptography


## Table of Contents

- [Elliptic Curve Cryptography](#elliptic-curve-cryptography)
- [Introduction](#introduction)
- [Mathematical Foundations](#mathematical-foundations)
  - [Elliptic Curve Definition](#elliptic-curve-definition)
  - [Group Law Operations](#group-law-operations)
- [Key Generation](#key-generation)
- [ECDSA Digital Signature](#ecdsa-digital-signature)
  - [Signature Generation](#signature-generation)
  - [Signature Verification](#signature-verification)
- [Encryption Schemes](#encryption-schemes)
  - [ECIES (Elliptic Curve Integrated Encryption Scheme)](#ecies-elliptic-curve-integrated-encryption-scheme)
- [Security Considerations](#security-considerations)
- [Examples](#examples)
  - [Example 1: Point Addition](#example-1-point-addition)
  - [Example 2: ECDSA Signature](#example-2-ecdsa-signature)
- [Real-World Applications](#real-world-applications)
- [Exam Tips](#exam-tips)
- [Diagrams (Textual Description)](#diagrams-textual-description)

## Introduction

Elliptic Curve Cryptography (ECC) is a modern public-key cryptographic system that offers equivalent security to traditional systems like RSA with significantly smaller key sizes. Developed independently by Neal Koblitz and Victor S. Miller in 1985, ECC has become essential for resource-constrained environments due to its computational efficiency and storage advantages.

The security of ECC relies on the intractability of the Elliptic Curve Discrete Logarithm Problem (ECDLP) - finding integer k given points P and Q = kP on the curve. A 256-bit ECC key provides comparable security to a 3072-bit RSA key, making it ideal for mobile devices, IoT systems, and blockchain technologies like Bitcoin (which uses ECDSA for transaction signing).

ECC is widely adopted in TLS 1.3, government systems (NSA Suite B), and cryptocurrency protocols. Its mathematical foundation in algebraic geometry allows for efficient implementation of key exchange, digital signatures, and encryption while resisting quantum computing attacks better than classical systems.

## Mathematical Foundations

### Elliptic Curve Definition

An elliptic curve over prime field GF(p) is defined by:

```math
y^2 \equiv x^3 + ax + b \ (\text{mod}\ p)
```

where:

- p > 3 is prime
- 4a³ + 27b² ≢ 0 mod p (non-singularity condition)
- All operations are performed modulo p

**Example Curve (secp256k1 used in Bitcoin):**

```
p = 2^256 - 2^32 - 977
a = 0
b = 7
```

### Group Law Operations

1. **Point Addition (P ≠ Q):**
   - Slope: m = (y₂ - y₁)(x₂ - x₁)⁻¹ mod p
   - x₃ = m² - x₁ - x₂ mod p
   - y₃ = m(x₁ - x₃) - y₁ mod p

2. **Point Doubling (P = Q):**
   - Slope: m = (3x₁² + a)(2y₁)⁻¹ mod p
   - x₃ = m² - 2x₁ mod p
   - y₃ = m(x₁ - x₃) - y₁ mod p

3. **Identity Element:** Point at infinity (O)
4. **Inverse Element:** -(x,y) = (x, -y mod p)

## Key Generation

1. Choose standard domain parameters (p, a, b, G, n, h)
   - G: Base point (generator)
   - n: Order of G (prime)
   - h: Cofactor (h = #E/n)

2. Select private key d: random integer ∈ [1, n-1]

3. Compute public key Q = dG (scalar multiplication)

**Example Parameters (secp256r1):**

```
p = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
a = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC
b = 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B
G = (0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,
     0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
n = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551
```

## ECDSA Digital Signature

### Signature Generation

1. Compute message hash e = H(m)
2. Select random k ∈ [1, n-1]
3. Compute (x₁, y₁) = kG
4. r = x₁ mod n (if r=0, repeat)
5. s = k⁻¹(e + dr) mod n (if s=0, repeat)
6. Signature: (r, s)

### Signature Verification

1. Verify r,s ∈ [1, n-1]
2. Compute e = H(m)
3. w = s⁻¹ mod n
4. u₁ = ew mod n, u₂ = rw mod n
5. (x₁, y₁) = u₁G + u₂Q
6. Accept if r ≡ x₁ mod n

## Encryption Schemes

### ECIES (Elliptic Curve Integrated Encryption Scheme)

1. Key Agreement: Generate ephemeral key pair (k, R=kG)
2. Shared Secret: S = kQ = (x, y)
3. Key Derivation: K = KDF(x || y)
4. Encrypt: C = E_K(M)
5. MAC: T = MAC_K(C)
6. Ciphertext: (R, C, T)

## Security Considerations

1. **ECDLP Hardness:** Best known attack is Pollard's Rho with complexity O(√n)
2. **Safe Curves:** Require prime field, non-singular, large embedding degree
3. **Side-Channel Attacks:** Timing analysis, power analysis countermeasures
4. **Invalid Curve Attacks:** Verify received points are on curve
5. **Quantum Resistance:** ECDLP vulnerable to Shor's algorithm → post-quantum alternatives needed

## Examples

### Example 1: Point Addition

Let E: y² = x³ + 2x + 3 over GF(97)
P = (3,6), Q = (80,87)

1. Compute slope m:
   m = (87 - 6)(80 - 3)⁻¹ mod 97
   = 81 * 77⁻¹ mod 97
   77⁻¹ = 65 (since 77*65 ≡ 1 mod 97)
   m = 81\*65 mod 97 = 5265 mod 97 = 25

2. Compute x₃:
   x₃ = 25² - 3 - 80 mod 97
   = 625 - 83 mod 97
   = 542 mod 97 = 60

3. Compute y₃:
   y₃ = 25(3 - 60) - 6 mod 97
   = 25(-57) - 6 mod 97
   = -1425 - 6 mod 97
   = -1431 mod 97 = 34

Result: P + Q = (60,34)

### Example 2: ECDSA Signature

Parameters: E over GF(23) with a=1, b=1, G=(3,10), n=28
Private key d=7, Q=7G=(19,13)

Sign message m with hash e=12:

1. Choose k=5
2. R = kG = 5(3,10) = (17,9)
3. r = 17 mod 28 = 17
4. s = 5⁻¹(12 + 7*17) mod 28
   5⁻¹ mod 28 = 17 (since 5*17=85≡1 mod 28)
   s = 17*(12+119) = 17*131 = 2227 mod 28 = 15

Signature: (17,15)

Verify:

1. w = 15⁻¹ mod 28 = 15
2. u₁ = 12\*15 mod 28 = 180 mod 28 = 12
3. u₂ = 17\*15 mod 28 = 255 mod 28 = 3
4. Compute 12G + 3Q:
   12G = (4,0), 3Q = 3(19,13) = (17,14)
   Sum = (4,0) + (17,14) = (17,9)
5. r = 17 matches x-coordinate mod 28 → Valid

## Real-World Applications

1. **TLS 1.3:** ECDHE for key exchange, ECDSA for certificates
2. **Bitcoin:** secp256k1 curve for transaction signatures
3. **Secure Boot:** Compact signatures for firmware verification
4. **Wireless Sensors:** ECC-160 for constrained devices
5. **DNSSEC:** Ed25519 (Edwards curve DSA)

## Exam Tips

1. **Key Size Comparison:** Memorize 256-bit ECC ≈ 3072-bit RSA security
2. **ECDLP Definition:** Understand it's the foundation of ECC security
3. **Signature Steps:** Practice ECDSA generation/verification algebra
4. **Point Operations:** Be ready to compute additions/doubling modulo p
5. **Advantages:** List 3 key benefits - smaller keys, faster ops, same security
6. **Parameter Check:** Always verify points are on the curve in exam solutions
7. **Attack Awareness:** Know about side-channel and invalid curve attacks

## Diagrams (Textual Description)

**Elliptic Curve Group Structure:**

- X-Y plot showing curve y² = x³ - x + 1
- Graphical demonstration of point addition: chord-and-tangent method
- Identity element shown as "point at infinity" above the plane

**ECDSA Workflow:**

1. Key Generation (d, Q=dG)
2. Signing: [Message → Hash → (r,s) calculation]
3. Verification: [Signature decomposition → u1G + u2Q → r comparison]

**Key Size Comparison Chart:**
| Security Level | RSA Key Size | ECC Key Size |
|----------------|--------------|--------------|
| 80-bit | 1024 | 160 |
| 128-bit | 3072 | 256 |
| 256-bit | 15360 | 512 |
