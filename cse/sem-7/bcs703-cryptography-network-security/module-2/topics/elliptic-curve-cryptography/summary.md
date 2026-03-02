# Elliptic Curve Cryptography - Summary

## Key Definitions and Concepts

- **Elliptic Curve**: Algebraic curve defined by `y² = x³ + ax + b` over a finite field (prime or binary)
- **Point Addition**: Geometric operation to add two points on the curve, resulting in a third point
- **Scalar Multiplication**: Repeated addition of a point to itself (`kP = P + P + ... + P` k times)
- **ECDLP**: Elliptic Curve Discrete Logarithm Problem - foundation of ECC security
- **Base Point (G)**: Predefined generator point on the curve used for key generation
- **ECDSA**: Elliptic Curve Digital Signature Algorithm used in Bitcoin/TLS
- **Finite Field**: Set of integers modulo prime p (Fₚ) where operations are performed

## Important Formulas and Theorems

1. **Elliptic Curve Equation**:
   ```
   y² ≡ x³ + ax + b (mod p)  # Prime field
   y² + xy = x³ + ax² + b    # Binary field
   ```
2. **Point Addition**:
   - If P ≠ Q:  
     `m = (y₂ - y₁)/(x₂ - x₁)`  
     `x₃ = m² - x₁ - x₂`  
     `y₃ = m(x₁ - x₃) - y₁`
   - If P = Q (Point Doubling):  
     `m = (3x₁² + a)/(2y₁)`
3. **Order (n)**: Integer where `nG = O` (point at infinity)
4. **Key Generation**:  
   `Public Key = d × G` (d = private key, 1 < d < n-1)

## Key Points

- ECC provides equivalent security to RSA with **smaller key sizes** (256-bit ECC ≈ 3072-bit RSA)
- Operations occur in **finite fields** to prevent floating-point inaccuracies
- **Three main operations**: Point addition, point doubling, scalar multiplication
- Used in **TLS 1.3**, **Bitcoin** (secp256k1 curve), and secure messaging apps
- Security relies on **ECDLP hardness** - no efficient algorithm to find k given kG and G
- **NIST-approved curves**: P-256, P-384, P-521 for different security levels
- Requires careful **curve parameter selection** to avoid weak curves
- **Two main implementations**: ECDH (key exchange) and ECDSA (signatures)

## Common Mistakes to Avoid

1. Assuming ECC keys work like RSA keys (ECC uses **point coordinates**, not prime factors)
2. Forgetting to apply **modular inverse** when calculating slope (m) in point addition
3. Using simple addition for scalar multiplication (`3P ≠ P+P+P` mathematically - requires doubling+addition)
4. Omitting **curve parameters** when writing answers (a, b, p, G, n must be specified)

## Revision Tips

1. **Practice point operations** with sample values:  
   Example: Compute P+Q where P=(2,4), Q=(5,1) on curve y² = x³ + 2x + 3 mod 7
2. **Create comparison table** ECC vs RSA: Key sizes, speed, security assumptions
3. **Memorize 3 real-world applications**: SSL/TLS, cryptocurrency, IoT security
4. **Understand ECDSA workflow**:
   - Signature: (r,s) where r = x-coordinate of kG
   - Verification: Check if r ≡ x-coordinate of (s⁻¹(zG + rQ)) mod n
