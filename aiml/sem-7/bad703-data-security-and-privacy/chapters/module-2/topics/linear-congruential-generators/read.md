# Linear Congruential Generators (LCGs)

## Introduction

In the domain of **Data Security and Privacy**, random numbers are fundamental. They are the building blocks for cryptographic keys, initialization vectors, nonces, and simulation inputs. However, generating truly random numbers with a deterministic computer is a challenge. **Pseudo-Random Number Generators (PRNGs)** are algorithms designed to solve this by producing sequences of numbers that *appear* random. The **Linear Congruential Generator (LCG)** is one of the oldest and simplest classes of PRNGs. While not suitable for modern high-security cryptography due to its predictability, understanding LCGs is crucial as it introduces core concepts of periodicity, seed, and state that underpin more complex PRNGs.

## Core Concepts

An LCG generates a sequence of pseudo-random numbers using a linear recurrence relation. The formula that defines the sequence is:

`Xₙ₊₁ = (a * Xₙ + c) mod m`

Where:
*   **`Xₙ`**: The current value in the sequence (the *state*). This is also the "random" number output.
*   **`a`**: The *multiplier* (a positive integer).
*   **`c`**: The *increment* (a positive integer). If `c = 0`, the generator is called a *Multiplicative Congruential Generator (MCG)*.
*   **`m`**: The *modulus* (a positive integer, `m > 0`). The modulus defines the upper bound for the numbers generated; the values will be in the range `[0, m-1]`.
*   **`X₀`**: The *seed*. This is the initial starting value (`X₀`) that kick-starts the entire sequence. The entire sequence is deterministic based on this seed.

### How it Works

1.  **Initialization:** The algorithm is initialized with a starting seed value `X₀`.
2.  **Generation:** The next value `X₁` is calculated as `(a * X₀ + c) mod m`.
3.  **Output:** `X₁` is returned as the first pseudo-random number.
4.  **Iteration:** The process repeats, using `X₁` to calculate `X₂`, and so on. The value `Xₙ` becomes the state for the next calculation.

The "randomness" comes from the modulo operation (`mod m`), which introduces a non-linear wrap-around effect.

### Properties and Considerations

*   **Periodicity:** An LCG's sequence is **not truly random**; it is periodic. After a certain number of values, the sequence will repeat itself entirely. A good LCG is designed to have a **full period**, meaning it cycles through all possible values (`0` to `m-1`) before repeating. The maximum possible period is `m`.
*   **Choosing Parameters (`a`, `c`, `m`):** The choice of parameters is critical for the quality of the random sequence. A poor choice leads to a short, predictable period. The Hull-Dobell Theorem provides conditions for achieving a full period:
    1.  `c` and `m` are relatively prime (i.e., `gcd(c, m) = 1`).
    2.  `a - 1` is divisible by all prime factors of `m`.
    3.  If `m` is divisible by 4, then `a - 1` must also be divisible by 4.
*   **Predictability and Security Flaw:** The major weakness of LCGs for cryptography is their **predictability**. If an attacker observes a few consecutive outputs, they can easily solve for the parameters `a`, `c`, and `m` using algebra, allowing them to reconstruct the entire past and future sequence. This makes them completely insecure for cryptographic purposes like key generation.

## Example

Let's define a simple LCG with parameters:
*   `a = 5`
*   `c = 3`
*   `m = 16`
*   Seed `X₀ = 2`

Let's generate the sequence:

`X₁ = (5 * 2 + 3) mod 16 = 13 mod 16 = **13**`
`X₂ = (5 * 13 + 3) mod 16 = 68 mod 16 = **4**`  (since 16 * 4 = 64, 68 - 64 = 4)
`X₃ = (5 * 4 + 3) mod 16 = 23 mod 16 = **7**`
`X₄ = (5 * 7 + 3) mod 16 = 38 mod 16 = **6**`
`X₅ = (5 * 6 + 3) mod 16 = 33 mod 16 = **1**`

The sequence so far is: **2 (seed)**, 13, 4, 7, 6, 1, ...

Continuing this process, the full sequence of 16 numbers (period = 16) will be:
**2, 13, 4, 7, 6, 1, 8, 11, 10, 5, 12, 15, 14, 9, 0, 3,** and then it repeats from 2.

## Key Points & Summary

*   **Function:** An LCG is a simple PRNG defined by the recurrence relation `Xₙ₊₁ = (a * Xₙ + c) mod m`.
*   **Deterministic:** The sequence is entirely determined by the **seed** value (`X₀`). Using the same seed will always produce the same sequence.
*   **Periodic:** The sequence will eventually repeat. A primary design goal is to maximize this period.
*   **Parameters Matter:** The choice of `a`, `c`, and `m` drastically affects the quality and period length of the generated sequence.
*   **Not Cryptographically Secure:** Due to their high predictability, basic LCGs are **unsuitable for cryptographic applications** like encryption or key generation. They are often used in applications where security is not a concern, such as simulations and shuffling algorithms.
*   **Historical Significance:** LCGs are historically important and form the basis for understanding more modern and secure PRNGs like the **Mersenne Twister** and cryptographically secure PRNGs (CSPRNGs) found in operating systems (`/dev/urandom`).