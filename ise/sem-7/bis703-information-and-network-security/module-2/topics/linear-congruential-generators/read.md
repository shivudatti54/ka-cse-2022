# Linear Congruential Generators (LCGs)


## Table of Contents

- [Linear Congruential Generators (LCGs)](#linear-congruential-generators-lcgs)
- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
  - [Properties and Behavior](#properties-and-behavior)
- [Example](#example)
- [Key Points & Summary](#key-points--summary)

**Subject:** Cryptography & Network Security
**Module:** Module 2 (10 hours)
**Topic:** Pseudo-Random Number Generators (PRNGs)

## Introduction

In cryptography, randomness is not a luxury but a necessity. Secure protocols rely on random numbers for generating keys, initialization vectors, nonces, and for various probabilistic algorithms. However, generating true, unpredictable randomness with a deterministic computer is a challenge. This is where **Pseudo-Random Number Generators (PRNGs)** come in. They are algorithms that produce a sequence of numbers that _appear_ random but are actually determined by a small initial value, known as a **seed**.

One of the oldest, simplest, and most well-known PRNGs is the **Linear Congruential Generator (LCG)**. While largely considered insecure for modern cryptographic applications, understanding LCGs is fundamental. They provide a clear model for how deterministic processes can emulate randomness and illustrate critical concepts like periodicity and predictability that are crucial for evaluating more complex PRNGs.

## Core Concepts

An LCG generates a sequence of pseudo-random numbers using a linear recurrence relation. The formula that defines the sequence is:

`Xₙ₊₁ = (a * Xₙ + c) mod m`

Where:

- `Xₙ` is the current value in the sequence (the seed for the first value, `X₀`).
- `a` is the **multiplier** (a non-zero integer).
- `c` is the **increment**.
- `m` is the **modulus** (`m > 0`).
- `mod` is the modulo operation, which ensures the result is always between `0` and `m-1`.

The sequence of numbers `X₀, X₁, X₂, ..., Xₙ` is the output. To get numbers in a desired range (e.g., between `0` and `1`), `Xₙ` is often divided by `m`.

### Properties and Behavior

The quality and security of an LCG are entirely determined by the choice of parameters `a`, `c`, and `m`.

1.  **Periodicity:** Since the calculation is done `mod m`, the sequence can only take on `m` distinct values (from `0` to `m-1`). Therefore, the sequence _must_ eventually repeat itself. The length of this cycle before repetition begins is called the **period**. A good LCG has a period that is long enough for its intended application. For a well-chosen set of parameters, the maximum possible period is `m`. This is achieved if:
    - `c` and `m` are **coprime** (their greatest common divisor is 1).
    - `a - 1` is divisible by all prime factors of `m`.
    - If `m` is a multiple of 4, then `a - 1` must also be a multiple of 4.

2.  **Predictability and Security:** LCGs are **highly predictable**. If an attacker observes a few consecutive values from the sequence, they can easily solve for the parameters `a`, `c`, and `m`, and then predict all future values. This makes classic LCGs **cryptographically insecure** and unsuitable for generating keys or nonces in secure systems. Their primary use today is in non-cryptographic applications like simulations and shuffling algorithms where predictability is not a concern.

## Example

Let's create a simple LCG with the following parameters:

- Modulus, `m = 9`
- Multiplier, `a = 2`
- Increment, `c = 5`
- Seed, `X₀ = 1`

Let's generate the sequence:
`X₁ = (2 * 1 + 5) mod 9 = 7 mod 9 = 7`
`X₂ = (2 * 7 + 5) mod 9 = 19 mod 9 = 1`
`X₃ = (2 * 1 + 5) mod 9 = 7 mod 9 = 7`

We see that the sequence `[1, 7, 1, 7, ...]` has a very short period of just 2. This is a terrible PRNG due to poor parameter choice. Let's try a better one.

Let's use parameters from the widely used `rand()` function in older C libraries:

- `m = 2³¹`
- `a = 1103515245`
- `c = 12345`
- `X₀ = 123456789`

`X₁ = (1103515245 * 123456789 + 12345) mod 2³¹`
This will produce a 31-bit number. The next number is calculated from this result. This LCG has a much longer period (up to `2³¹`) and is sufficient for basic applications, but remains cryptographically insecure.

## Key Points & Summary

| Key Point                  | Description                                                                                                                                                       |
| :------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definition**             | An LCG is a simple PRNG defined by the recurrence relation `Xₙ₊₁ = (a * Xₙ + c) mod m`.                                                                           |
| **Deterministic**          | The sequence is completely determined by the seed value `X₀`. The same seed produces the same sequence every time.                                                |
| **Periodicity**            | The sequence will eventually repeat. A good LCG has a long period, ideally equal to the modulus `m`.                                                              |
| **Predictability**         | LCGs are highly predictable. Knowing a few consecutive outputs allows an attacker to deduce the parameters and predict the entire sequence.                       |
| **Cryptographic Security** | **LCGs are not cryptographically secure.** They should never be used for generating encryption keys, nonces, or any other security-critical random values.        |
| **Legacy Use**             | They are still found in non-security contexts like numerical simulations, Monte Carlo methods, and basic programming language functions (e.g., `rand()`).         |
| **Modern Replacements**    | Cryptographically Secure PRNGs (CSPRNGs), such as those based on cryptographic hash functions (SHA-256) or block ciphers (AES) in counter mode, are used instead. |

**In summary,** while Linear Congruential Generators are a foundational concept for understanding pseudo-randomness, their predictability makes them obsolete for modern network security and cryptography. They serve as an important historical lesson on the properties that define a weak random number generator.
