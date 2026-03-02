# Elliptic Curve Cryptography (ECC)

## Introduction to ECC

Elliptic Curve Cryptography (ECC) is a public-key cryptography approach based on the algebraic structure of elliptic curves over finite fields. ECC provides the same level of security as traditional asymmetric algorithms like RSA but with significantly smaller key sizes, making it more efficient in terms of computation, storage, and bandwidth.

The fundamental security of ECC relies on the Elliptic Curve Discrete Logarithm Problem (ECDLP), which is considered computationally infeasible to solve with current technology. This mathematical hardness forms the basis for various cryptographic applications including key exchange, digital signatures, and encryption.

## Mathematical Foundations

### What is an Elliptic Curve?

An elliptic curve is a set of points satisfying a specific mathematical equation. For cryptography, we typically use curves defined over finite fields (prime fields or binary fields). The standard Weierstrass equation for an elliptic curve is:

y² = x³ + ax + b

Where:

- x and y are coordinates of points on the curve
- a and b are coefficients that define the curve's shape
- The curve must satisfy the condition 4a³ + 27b² ≠ 0 to avoid singular points

```
Example elliptic curve: y² = x³ - 3x + 3
 ^
 | .
 | . .
 | . .
 | . .
 | . .
 | . .
 |. .
 ---+------------->
 | .
 | .
 | .
 | .
 | .
 | .
 | .
```

### Finite Fields

In cryptography, we work with elliptic curves over finite fields (also called Galois fields). This means that the coordinates x and y are elements of a finite set rather than real numbers. The most common finite fields are:

1. **Prime fields (Fₚ)**: Where p is a prime number, and arithmetic operations are performed modulo p
2. **Binary fields (F₂ᵐ)**: Where elements are represented as binary polynomials of degree less than m

### Group Operations on Elliptic Curves

Elliptic curves form an abelian group under point addition. The group operation has geometric interpretations:

#### Point Addition (P + Q = R)

Given two distinct points P and Q on the curve, we can find their sum R by:

1. Drawing a line through P and Q
2. Finding the third point where this line intersects the curve
3. Reflecting this point across the x-axis

```
Point Addition:
 ^
 | P R
 | \ /
 | \ /
 | X
 | / \
 | / \
 | Q R'
 |
---+---------------->
```

#### Point Doubling (P + P = 2P)

When adding a point to itself, we use the tangent line at P:

1. Draw the tangent line at P
2. Find the second intersection point with the curve
3. Reflect this point across the x-axis

```
Point Doubling:
 ^
 | 2P
 | |
 | |
 | P
 | /
 | /
 | /
 | /
 | /
 |
---+---------------->
```

#### Identity Element and Inverse

The point at infinity (O) serves as the identity element for the group. For any point P, P + O = P.

The inverse of a point P = (x, y) is -P = (x, -y mod p). Adding a point and its inverse gives the identity element: P + (-P) = O.

### Scalar Multiplication

The fundamental operation in ECC is scalar multiplication: kP = P + P + ... + P (k times), where k is an integer and P is a point on the curve.

This operation is computationally efficient in one direction (calculating kP given k and P) but computationally difficult to reverse (finding k given P and kP). This one-way function forms the basis of ECC's security.

## ECC Cryptosystems

### Elliptic Curve Diffie-Hellman (ECDH)

ECDH is an elliptic curve variant of the Diffie-Hellman key exchange protocol. It allows two parties to establish a shared secret over an insecure channel.

**ECDH Key Exchange Process:**

1. Both parties agree on an elliptic curve E and a base point G on that curve
2. Alice generates a private key dₐ (a random integer) and computes her public key Qₐ = dₐ × G
3. Bob generates a private key d_b (a random integer) and computes his public key Q_b = d_b × G
4. They exchange public keys
5. Alice computes the shared secret S = dₐ × Q_b
6. Bob computes the shared secret S = d_b × Qₐ
7. Both arrive at the same shared secret because dₐ × (d_b × G) = d_b × (dₐ × G)

```
ECDH Flow:
Alice Public Channel Bob
dₐ (private) E, G (public) d_b (private)
Qₐ = dₐ × G (public) ----- Qₐ ----->
 <---- Q_b ----- Q_b = d_b × G (public)
S = dₐ × Q_b S = d_b × Qₐ
(Shared Secret) (Shared Secret)
```

### Elliptic Curve Digital Signature Algorithm (ECDSA)

ECDSA is the elliptic curve variant of the Digital Signature Algorithm (DSA), used for creating and verifying digital signatures.

**ECDSA Signature Generation:**

1. Select a random integer k where 1 ≤ k ≤ n-1 (n is the order of the base point G)
2. Compute (x₁, y₁) = k × G
3. Let r = x₁ mod n (if r = 0, choose a different k)
4. Compute s = k⁻¹ (H(m) + d × r) mod n (where d is the private key, H(m) is the hash of the message)
5. The signature is (r, s)

**ECDSA Signature Verification:**

1. Verify that r and s are integers in the range [1, n-1]
2. Compute w = s⁻¹ mod n
3. Compute u₁ = H(m) × w mod n
4. Compute u₂ = r × w mod n
5. Compute (x₁, y₁) = u₁ × G + u₂ × Q (where Q is the public key)
6. The signature is valid if r ≡ x₁ mod n

## ECC Parameters and Standards

### Standardized Curves

Various organizations have standardized specific elliptic curves for cryptographic use:

**NIST Curves:**

- P-192, P-224, P-256, P-384, P-521 (Prime field curves)
- B-163, B-233, B-283, B-409, B-571 (Binary field curves)

**Other Standards:**

- Curve25519 (Used in OpenSSH, Signal Protocol)
- secp256k1 (Used in Bitcoin and Ethereum)
- Brainpool curves (Alternative to NIST curves)

### Domain Parameters

An ECC cryptosystem is defined by its domain parameters:

1. The field size and representation (prime p or integer m for binary field)
2. The coefficients a and b of the elliptic curve equation
3. The base point G = (x_G, y_G) generating a cyclic subgroup
4. The order n of G (a prime number)
5. The cofactor h = #E(F)/n (where #E(F) is the number of points on the curve)

## Security Considerations

### Advantages of ECC

1. **Smaller Key Sizes**: ECC provides equivalent security with much smaller keys compared to RSA
2. **Faster Computation**: ECC operations are generally faster than equivalent RSA operations
3. **Lower Power Consumption**: Important for mobile and IoT devices
4. **Bandwidth Efficiency**: Smaller keys and signatures reduce transmission requirements

### Key Size Comparison

| Security Level (bits) | RSA Key Size (bits) | ECC Key Size (bits) |
| --------------------- | ------------------- | ------------------- |
| 80                    | 1024                | 160                 |
| 112                   | 2048                | 224                 |
| 128                   | 3072                | 256                 |
| 192                   | 7680                | 384                 |
| 256                   | 15360               | 521                 |

### Potential Attacks

1. **Pollard's Rho Algorithm**: The best known generic attack on ECDLP with complexity O(√n)
2. **MOV Attack**: Reduces ECDLP to discrete logarithm in an extension field (works for certain curves)
3. **Weil and Tate Pairing Attacks**: Similar to MOV attack
4. **Side-Channel Attacks**: Timing attacks, power analysis, fault injection
5. **Invalid Curve Attacks**: Exploiting implementation errors in point validation

### Curve Selection Considerations

1. **Avoid Weak Curves**: Some curves have properties that make them vulnerable to specific attacks
2. **Randomized Curves**: Preferably use curves with coefficients generated verifiably at random
3. **Rigidity**: Curves with rigid design process (like Curve25519) avoid suspicion of backdoors
4. **Standard Compliance**: Use curves from reputable standards like NIST, Brainpool, or CFRG

## Implementation Aspects

### Point Representation

Different point representations offer trade-offs between storage and computation:

1. **Affine Coordinates**: (x, y) - requires field inversions, which are expensive
2. **Projective Coordinates**: (X, Y, Z) where x = X/Z, y = Y/Z - avoids inversions during intermediate calculations
3. **Jacobian Coordinates**: (X, Y, Z) where x = X/Z², y = Y/Z³ - efficient for point doubling
4. **Compressed Points**: Store only x-coordinate and a sign bit for y - reduces storage requirements

### Efficient Algorithms

1. **Double-and-Add**: Basic method for scalar multiplication (similar to square-and-multiply in RSA)
2. **Window Methods**: Precompute multiples of P to reduce the number of additions
3. **Montgomery Ladder**: Resistant to timing attacks and simple power analysis
4. **Twisted Edwards Curves**: Allow complete addition formulas without special cases

## Applications of ECC

1. **SSL/TLS**: ECC cipher suites for secure web browsing
2. **Bitcoin and Cryptocurrencies**: ECDSA for transaction signatures
3. **Secure Messaging**: Signal Protocol uses Curve25519 for key agreement
4. **IoT Devices**: Low-power cryptography for constrained devices
5. **Government Systems**: Suite B cryptography includes ECC algorithms
6. **Mobile Devices**: Efficient cryptography for smartphones and tablets

## Exam Tips

1. **Understand the Mathematics**: Focus on group operations, point addition, and scalar multiplication
2. **Key Size Comparisons**: Memorize the RSA vs ECC key size equivalents for different security levels
3. **Algorithm Differences**: Be able to explain how ECDH and ECDSA work, including their steps
4. **Security Considerations**: Know the advantages of ECC and potential attack vectors
5. **Implementation Aspects**: Understand why different coordinate systems are used and their trade-offs
6. **Standard Curves**: Be familiar with common curve names like P-256, Curve25519, and secp256k1
7. **Practice Calculations**: Work through simple examples of point addition and scalar multiplication on small curves
