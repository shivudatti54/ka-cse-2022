# Elliptic Curve Cryptography

## Introduction

Elliptic Curve Cryptography (ECC) represents one of the most significant advancements in modern asymmetric cryptography, providing equivalent security to traditional public-key systems like RSA while requiring significantly smaller key sizes. The mathematical foundation of ECC lies in the algebraic structure of elliptic curves over finite fields, where the hardness of the Elliptic Curve Discrete Logarithm Problem (ECDLP) provides the security guarantees. ECC was independently proposed by Neal Koblitz and Victor Miller in 1985 and has since become fundamental to contemporary cryptographic protocols including TLS, SSH, and blockchain technologies.

The primary advantage of ECC lies in its efficiency: a 256-bit ECC key provides approximately the same security level as a 3072-bit RSA key. This results in faster computation, reduced bandwidth, and lower computational resource requirements—critical considerations for mobile devices and constrained environments. The mathematical operations underlying ECC involve point addition and scalar multiplication on elliptic curves, which can be efficiently computed using specialized algorithms.

## Key Concepts

### Mathematical Foundation of Elliptic Curves

An elliptic curve is defined by the Weierstrass equation:

$$y^2 = x^3 + ax + b$$

where $a$ and $b$ are constants satisfying $4a^3 + 27b^2 \neq 0$ (the discriminant condition ensures no singularities). Over a finite field $\mathbb{F}_p$ (where $p$ is a prime), the curve consists of all solutions $(x, y) \in \mathbb{F}_p \times \mathbb{F}_p$ together with a special point at infinity $\mathcal{O}$ serving as the identity element.

**Group Structure**: The set of points on an elliptic curve forms an abelian group under a well-defined addition operation. For two distinct points $P = (x_1, y_1)$ and $Q = (x_2, y_2)$, the sum $R = P + Q$ is computed as follows:

For $P \neq Q$ (point addition):
$$\lambda = \frac{y_2 - y_1}{x_2 - x_1} \pmod{p}$$
$$x_3 = \lambda^2 - x_1 - x_2 \pmod{p}$$
$$y_3 = \lambda(x_1 - x_3) - y_1 \pmod{p}$$

For $P = Q$ (point doubling):
$$\lambda = \frac{3x_1^2 + a}{2y_1} \pmod{p}$$
$$x_3 = \lambda^2 - 2x_1 \pmod{p}$$
$$y_3 = \lambda(x_1 - x_3) - y_1 \pmod{p}$$

**Theorem (Group Law)**: The addition operation defined above makes the set $E(\mathbb{F}_p) = \{(x,y) \in \mathbb{F}_p^2 : y^2 = x^3 + ax + b\} \cup \{\mathcal{O}\}$ into an abelian group with identity element $\mathcal{O}$.

_Proof Sketch_: The identity element is the point at infinity $\mathcal{O}$, where $P + \mathcal{O} = P$. For any point $P = (x, y)$, its inverse is $-P = (x, -y)$ since $P + (-P) = \mathcal{O}$. The commutativity is obvious from the formula. Associativity can be verified through algebraic manipulation of the coordinates, though the complete proof requires substantial computation. $\square$

### Elliptic Curve Discrete Logarithm Problem (ECDLP)

The security of ECC rests on the difficulty of the ECDLP: given points $P$ and $Q = kP$ on an elliptic curve, compute the integer $k$. Unlike the continuous case where algorithms like baby-step giant-step apply with complexity $O(\sqrt{n})$, the best-known classical algorithms require exponential time. Shor's algorithm on quantum computers can solve ECDLP in polynomial time, motivating post-quantum cryptography research.

### Key Generation

For key generation in ECC-based systems:

1. Select an elliptic curve $E$ over $\mathbb{F}_p$ with a base point $G$ of prime order $n$
2. Choose a random integer $d$ such that $1 \leq d \leq n-1$
3. Compute public key point $Q = dG$ (scalar multiplication)
4. The private key is $d$; the public key is $Q$

### Elliptic Curve Diffie-Hellman (ECDH)

ECDH enables secure key exchange between two parties:

1. **Alice** selects private key $d_A$ and computes public key $Q_A = d_A \cdot G$
2. **Bob** selects private key $d_B$ and computes public key $Q_B = d_B \cdot G$
3. **Alice** computes shared secret: $S = d_A \cdot Q_B = d_A d_B G$
4. **Bob** computes shared secret: $S = d_B \cdot Q_A = d_A d_B G$

The shared secret $S$ is then used to derive encryption keys.

### Elliptic Curve Digital Signature Algorithm (ECDSA)

ECDSA provides digital signatures using elliptic curves:

**Signing Algorithm**:

1. Compute hash $e = H(m)$
2. Select random nonce $k$ (must be unique and secret)
3. Calculate $r = (kG)_x \pmod{n}$
4. Calculate $s = k^{-1}(e + d \cdot r) \pmod{n}$
5. Signature is $(r, s)$

**Verification Algorithm**:

1. Verify $r, s \in [1, n-1]$
2. Compute $e = H(m)$
3. Calculate $u_1 = e \cdot s^{-1} \pmod{n}$ and $u_2 = r \cdot s^{-1} \pmod{n}$
4. Compute point $P = u_1 G + u_2 Q$
5. Accept signature if $r \equiv P_x \pmod{n}$

**Theorem (ECDSA Correctness)**: If the signature $(r, s)$ is validly generated from private key $d$ and message $m$, verification will always accept.

_Proof_: Given valid signature, $s = k^{-1}(e + dr) \pmod{n}$. Rearranging: $k \equiv s^{-1}(e + dr) \pmod{n}$. During verification:
$$P = s^{-1}eG + s^{-1}drQ = s^{-1}eG + s^{-1}dr(dG) = (s^{-1}(e + dr))G = kG$$
Thus $P_x = r$, and verification succeeds. $\square$

## Examples

### Example 1: Point Addition on Small Curve

Consider $E: y^2 = x^3 + 2x + 2$ over $\mathbb{F}_11$ with $a=2, b=2$. Given points $P = (7, 2)$ and $Q = (8, 3)$, compute $P + Q$:

$$\lambda = \frac{3-2}{8-7} = 1 \pmod{11} = 1$$
$$x_3 = 1^2 - 7 - 8 = -14 \equiv 8 \pmod{11}$$
$$y_3 = 1(7-8) - 2 = -1 - 2 = -3 \equiv 8 \pmod{11}$$

Thus $P + Q = (8, 8)$.

### Example 2: ECDH Key Exchange

With curve parameters $p = 23, a = 1, b = 1, G = (16, 21)$ of order $n = 19$:

- Alice: $d_A = 5 \Rightarrow Q_A = 5G = (13, 14)$
- Bob: $d_B = 7 \Rightarrow Q_B = 7G = (17, 3)$
- Shared secret: $S = 5 \cdot Q_B = 7 \cdot Q_A = (3, 20)$

Both parties derive identical shared secret for key derivation.

### Example 3: ECDSA Signature Generation

For curve with $G = (x_G, y_G)$, private key $d = 12$, message hash $e = 10$, and nonce $k = 5$:

- $r = (kG)_x = 17$ (assuming $(5G)_x = 17$)
- $s = 5^{-1}(10 + 12 \cdot 17) \pmod{n} = 9(10 + 204) = 9(214) \equiv 8 \pmod{n}$

Signature: $(17, 8)$

## Exam Tips

1. **Understand the Group Law**: Memorize both point addition and doubling formulas; these appear frequently in problem sets and exams.

2. **Security Parameter Comparisons**: Remember that 256-bit ECC ≈ 3072-bit RSA ≈ 128-bit symmetric security. This efficiency is a key advantage of ECC.

3. **ECDLP Hardness**: The security of ECC relies on the intractability of ECDLP. Understand why generic discrete logarithm algorithms (baby-step giant-step, Pollard's rho) are less effective on elliptic curves.

4. **Nonce Reuse Vulnerability**: In ECDSA, reusing the same nonce $k$ allows recovery of the private key. This has led to real-world cryptocurrency thefts—understand the mathematical basis: $s_1 - s_2 \equiv k^{-1}(e_1 + dr) - k^{-1}(e_2 + dr) \equiv k^{-1}(e_1 - e_2)$.

5. **Curve Selection**: Different curves offer different properties. NIST curves (P-256) are widely deployed, while Curve25519 provides better implementation security through avoiding exceptional points.

6. **Quantum Vulnerability**: ECC is vulnerable to quantum attacks via Shor's algorithm, unlike symmetric cryptography which only suffers Grover's speedup. Be prepared to discuss post-quantum implications.

7. **Relationship to PRNGs**: While ECC itself is not a PRNG, it can be used to construct cryptographically secure pseudo-random bit generators through scalar multiplication with a random seed point.
