# Asymmetric Cryptography

## Overview

Elliptic Curve Cryptography (ECC) is the asymmetric cryptography foundation of blockchain, providing security through the Elliptic Curve Discrete Logarithm Problem (ECDLP). ECC offers equivalent security to RSA with significantly smaller key sizes, making it ideal for blockchain's computational and storage constraints.

## Key Points

- **Elliptic Curve Equation**: y² = x³ + ax + b over finite fields with group operations
- **Point Addition**: Geometric operation drawing line through two points, reflecting third intersection point
- **Scalar Multiplication**: kP = P + P + ... + P (k times); easy forward, computationally infeasible to reverse
- **ECDH Key Exchange**: Allows two parties to establish shared secret over insecure channel
- **ECDSA Signatures**: Create and verify digital signatures using elliptic curve mathematics
- **Key Size Advantage**: 256-bit ECC equivalent to 3072-bit RSA in security
- **Standard Curves**: secp256k1 (Bitcoin/Ethereum), Curve25519 (OpenSSH), P-256 (NIST)

## Important Concepts

- Point at infinity (O) serves as identity element for group operations
- Private key is random integer, public key is scalar multiplication result (Q = d × G)
- ECDSA signature (r, s) proves message authorization without revealing private key
- Coordinate systems trade storage for computation: affine, projective, Jacobian
- Side-channel attacks (timing, power analysis) require careful implementation

## Notes

- Understand why scalar multiplication is one-way function (security basis)
- Memorize key size comparisons at different security levels (80, 112, 128, 192, 256 bits)
- Know ECDSA signature generation and verification steps
- Be familiar with secp256k1 curve used in Bitcoin and Ethereum
