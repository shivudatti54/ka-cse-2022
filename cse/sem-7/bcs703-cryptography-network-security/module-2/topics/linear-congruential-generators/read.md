# Linear Congruential Generators (LCGs)

## Introduction

Randomness is a fundamental resource in cryptographic systems. Secure communication protocols require random numbers for key generation, initialization vectors, nonces, salts, and various probabilistic algorithms including digital signature schemes and zero-knowledge proofs. The quality of randomness directly impacts security—predictable random numbers can compromise entire cryptographic systems.

However, deterministic computers cannot generate true randomness. This necessitates **Pseudo-Random Number Generators (PRNGs)**: deterministic algorithms that produce sequences of numbers exhibiting statistical properties similar to random sequences. A PRNG takes a short random **seed** and expands it into a longer sequence that appears random to statistical tests.

The **Linear Congruential Generator (LCG)** represents one of the oldest and most influential PRNG designs. Introduced by Derrick Lehmer in 1949, LCGs remain important for educational purposes and non-cryptographic applications. Studying LCGs illuminates fundamental concepts in random number generation: periodicity, state space, predictability, and the critical distinction between statistical randomness and cryptographic security.

## Mathematical Foundation

### Definition

A Linear Congruential Generator produces a sequence of pseudo-random numbers {X₀, X₁, X₂, ...} using the recurrence relation:

**Xₙ₊₁ = (a × Xₙ + c) mod m**

Where:

- **X₀**: Initial seed value (the state)
- **a**: Multiplier (coefficient)
- **c**: Increment (additive constant)
- **m**: Modulus (m > 0, typically a power of 2 or a prime)
- **mod**: Modular arithmetic operation

The output at each iteration is Xₙ, typically normalized to [0, 1) by dividing by m.

### Classification

LCGs are classified based on the increment parameter:

- **Mixed LCGs**: c ≠ 0 (full linear congruential generator)
- **Multiplicative LCGs**: c = 0 (simplified form, historically significant)

### State Space and Period

Since each state Xₙ takes values in the finite set {0, 1, 2, ..., m-1}, the sequence must eventually repeat. The maximum possible period is m, though achieving this requires careful parameter selection.

## Maximum Period Conditions: Hull-Dobell Theorem

The conditions for achieving maximal period (period = m) are precisely characterized by the **Hull-Dobell Theorem** (1962):

**Theorem**: The LCG defined by Xₙ₊₁ = (aXₙ + c) mod m has full period m if and only if:

1. **gcd(c, m) = 1** (c and m are coprime)
2. **a ≡ 1 (mod p)** for every prime p dividing m
3. **If 4 | m, then a ≡ 1 (mod 4)**

**Proof Sketch**:

_Necessity_ (must hold for full period):

- If gcd(c, m) = d > 1, then Xₙ is always divisible by d, limiting possible values to m/d states.
- If p|m and p∤(a-1), consider the sequence modulo p: Xₙ₊₁ ≡ aXₙ + c (mod p). If a ≠ 1 (mod p), this linear recurrence has at most p distinct states, preventing full period m.
- For m divisible by 4, the multiplicative structure modulo powers of 2 requires a ≡ 1 (mod 4) for full period.

_Sufficiency_ (conditions ensure full period):

- Condition 1 ensures the recurrence can generate all residue classes modulo m.
- Conditions 2 and 3 ensure the multiplicative part a^(n-1) generates all possible multipliers as n varies, preventing premature cycles.

This theorem provides precise guidance for parameter selection in practical LCG implementations.

## Example: Full Period LCG

Consider m = 9, a = 2, c = 5, X₀ = 1:

X₁ = (2 × 1 + 5) mod 9 = 7
X₂ = (2 × 7 + 5) mod 9 = 19 mod 9 = 1

This gives period 2—poor parameters. Applying Hull-Dobell:

- m = 9 = 3², prime factor = 3
- gcd(c, m) = gcd(5, 9) = 1 ✓
- Need a ≡ 1 (mod 3): Choose a = 4
- If 4|m? No, skip condition 3

Let a = 4, c = 5, m = 9, X₀ = 1:
X₁ = (4×1 + 5) mod 9 = 9 mod 9 = 0
X₂ = (4×0 + 5) mod 9 = 5
X₃ = (4×5 + 5) mod 9 = 25 mod 9 = 7
X₄ = (4×7 + 5) mod 9 = 33 mod 9 = 6
X₅ = (4×6 + 5) mod 9 = 29 mod 9 = 2
X₆ = (4×2 + 5) mod 9 = 13 mod 9 = 4
X₇ = (4×4 + 5) mod 9 = 21 mod 9 = 3
X₈ = (4×3 + 5) mod 9 = 17 mod 9 = 8
X₉ = (4×8 + 5) mod 9 = 37 mod 9 = 1

Sequence: [1, 0, 5, 7, 6, 2, 4, 3, 8, 1] — Period = 9 = m ✓

## Practical LCG Parameters

Historical parameters achieving long periods:

| Source               | m       | a     | c   |
| -------------------- | ------- | ----- | --- |
| Numerical Algorithms | 2³¹ - 1 | 16807 | 0   |
| RANDU (IBM)          | 2³¹     | 65539 | 0   |
| VAX                  | 2³¹ - 1 | 69069 | 1   |

Note: RANDU's parameters (a = 65539, m = 2³¹) satisfy Hull-Dobell but fail the **spectral test**, producing correlated outputs visible in three dimensions.

## Spectral Test and Lattice Structure

The **spectral test** (Marsaglia, 1968) analyzes LCG quality by examining the d-dimensional lattice structure of generated vectors. Poor parameters produce vectors lying on few planes, indicating correlations.

For LCGs, the spectral test computes the largest gap between successive hyperplanes containing all points. A good LCG maximizes this distance, approaching random behavior. RANDU's well-known deficiencies illustrate this—consecutive triples lie on only 15 planes in 3D space.

## Cryptographic Weakness and Attack Analysis

LCGs are **inherently cryptographically insecure**. The recurrence is linear, making parameter recovery straightforward from observed outputs.

**Theorem**: Given any three consecutive outputs X₀, X₁, X₂ from an LCG with known modulus m, one can recover the parameters a and c.

**Derivation**:
From recurrence:
X₁ ≡ aX₀ + c (mod m)
X₂ ≡ aX₁ + c (mod m)

Subtracting:
X₂ - X₁ ≡ a(X₁ - X₀) (mod m)

If gcd(X₁ - X₀, m) = 1, we can compute:
a ≡ (X₂ - X₁)(X₁ - X₀)⁻¹ (mod m)

Then c ≡ X₁ - aX₀ (mod m)

Once a and c are known, all future values are trivially predictable.

**Example Attack**:
Given outputs 123, 456, 789 with m = 1000:

- X₁ - X₀ = 456 - 123 = 333
- X₂ - X₁ = 789 - 456 = 333
- gcd(333, 1000) = 1, invertible
- a ≡ 333 × 333⁻¹ ≡ 333 × 3 ≡ 999 ≡ -1 mod 1000
- c ≡ 456 - (-1)(123) ≡ 456 + 123 ≡ 579 mod 1000

Attacker now predicts entire sequence.

## Spectral Test Numerical Example

Consider LCG with m = 2⁵ = 32, a = 3, c = 1, X₀ = 0:

Sequences of consecutive outputs (pairs) form points in 2D:
(0, 1), (1, 4), (4, 13), (13, 40≡8), ...

These points cluster along specific lines, demonstrating poor distribution. The spectral test quantifies this clustering.

## Modern Context and Secure Alternatives

LCGs are suitable for:

- Simulation studies (Monte Carlo methods)
- Randomized algorithms (shuffling, sampling)
- Legacy systems (historical compatibility)

LCGs must NEVER be used for:

- Cryptographic key generation
- Nonce or salt values
- Session identifiers
- Any security-critical randomness

**Cryptographically Secure PRNGs (CSPRNGs)** required for security applications include:

- **Hash-based**: SHA-256 CTR_DRBG
- **Block cipher-based**: AES-CTR_DRBG
- **Number theoretic**: Blum-Blum-Shub (BBS)

These provide computational unpredictability—distinguishing output from true random is computationally infeasible.

## Summary

| Aspect              | LCG Property                             |
| ------------------- | ---------------------------------------- |
| Formula             | Xₙ₊₁ = (aXₙ + c) mod m                   |
| Period              | ≤ m, maximized by Hull-Dobell conditions |
| State Space         | m possible values                        |
| Predictability      | Full parameter recovery from 2-3 outputs |
| Cryptographic Use   | **NOT RECOMMENDED**                      |
| Statistical Quality | Varies; requires spectral testing        |
| Computational Speed | Very fast                                |

Linear Congruential Generators, despite their theoretical importance and historical significance, demonstrate a fundamental principle: **statistical randomness is insufficient for cryptographic security**. The linear structure enabling fast computation also enables efficient prediction, making LCGs unsuitable for modern cryptographic applications where unpredictability is paramount.
