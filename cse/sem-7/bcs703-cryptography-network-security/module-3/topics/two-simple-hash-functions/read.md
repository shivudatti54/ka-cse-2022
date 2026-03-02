# Module 3: Two Simple Hash Functions

## Introduction

In the domain of **Cryptography & Network Security**, hash functions serve as fundamental cryptographic primitives essential for ensuring **data integrity**, **authentication**, and **digital signatures**. Unlike encryption mechanisms, hash functions are one-way functions that produce a fixed-size output (message digest) from an arbitrary-length input message. This module provides an in-depth analysis of two historically significant yet cryptographically weak hash function constructions: the Simple Modulo Hash and the Davies-Meyer Hash Function. Understanding these foundational constructions is essential for comprehending the design principles underlying modern secure hash algorithms such as SHA-256 and SHA-3.

## 1. Security Properties of Cryptographic Hash Functions

Before examining specific constructions, we must formally define the three essential security properties that a robust cryptographic hash function must satisfy:

**Definition 1.1 (Pre-image Resistance):** A hash function $H$ is pre-image resistant if, given a hash output $h \in \{0,1\}^n$, finding any message $m$ such that $H(m) = h$ requires approximately $2^n$ computational operations (i.e., exponential in the output length).

**Definition 1.2 (Second Pre-image Resistance):** Given a specific message $m_1$, finding a different message $m_2 \neq m_1$ such that $H(m_1) = H(m_2)$ should require approximately $2^n$ operations.

**Definition 1.3 (Collision Resistance):** Finding any two distinct messages $m_1$ and $m_2$ such that $H(m_1) = H(m_2)$ should require approximately $2^{n/2}$ operations due to the birthday paradox. This is significantly weaker than the previous two properties.

The simple hash functions analyzed in this module fail to satisfy one or more of these fundamental properties, rendering them unsuitable for security-critical applications.

## 2. Simple Modulo Hash Function

### 2.1 Construction and Algorithm

The Simple Modulo Hash represents the most elementary approach to constructing a hash function using basic arithmetic operations. This construction processes the input message in fixed-size blocks and applies iterative compression.

**Algorithm 2.1 (Simple Modulo Hash):**

1. **Input:** Message $M$ of arbitrary length
2. **Block Division:** Split $M$ into blocks $M_1, M_2, ..., M_t$ of fixed size $b$ bits
3. **Initialization:** Set $H_0 = IV$ (Initial Value, typically 0)
4. **Iterative Compression:** For $i = 1$ to $t$:
   $$H_i = (H_{i-1} + M_i) \mod p$$
   where $p$ is a large prime determining the hash output space
5. **Output:** Return $H_t$ as the message digest

**Theorem 2.1 (Weakness Analysis):** The Simple Modulo Hash fails to provide collision resistance.

_Proof:_ Consider the hash function $H(m) = (\sum_{i=1}^{t} M_i) \mod p$. Given any message $M = (M_1, M_2, ..., M_t)$, we can construct a collision by adding $p$ to any block and subtracting $p$ from another block while maintaining the same sum. Specifically, for any valid message, there exist $p^{t-1}$ other messages producing the identical hash due to the linearity of modular addition. Therefore, finding collisions requires only $O(p^{t-1})$ operations, which is polynomial in the input size—far below the $2^{n/2}$ required for secure hash functions. ∎

### 2.2 Worked Numerical Example

**Problem:** Compute the Simple Modulo Hash with $p = 97$ for message "CS" where C=67, S=83 (ASCII values), using IV = 0.

**Solution:**

- Block 1 ($M_1 = 67$): $H_1 = (0 + 67) \mod 97 = 67$
- Block 2 ($M_2 = 83$): $H_2 = (67 + 83) \mod 97 = 150 \mod 97 = 53$

**Final Hash:** 53

**Problem:** Demonstrate a collision for the above hash function.

**Solution:**
Since $H(m) = (67 + 83) \mod 97 = 150 \mod 97 = 53$, any message pair $(x, y)$ satisfying $x + y \equiv 53 \mod 97$ produces a collision. For example:

- Message "AI": A=65, I=73 → $(65+73) \mod 97 = 138 \mod 97 = 41 \neq 53$ (no collision)
- Message "JB": J=74, B=66 → $(74+66) \mod 97 = 140 \mod 97 = 43 \neq 53$ (no collision)
- Message "!!": !=33, !=33 → $(33+33) \mod 97 = 66 \mod 97 = 66 \neq 53$ (no collision)

To find collision: Choose $M_1 = 50$, then $M_2 = (53 - 50) \mod 97 = 3$

- $H = (50 + 3) \mod 97 = 53$ — Collision found!

This demonstrates that finding collisions requires only simple algebraic manipulation.

## 3. Davies-Meyer Hash Function

### 3.1 Construction and Security Analysis

The Davies-Meyer construction represents a more sophisticated approach, leveraging symmetric block ciphers as the core compression component. This construction forms the foundation for many practical hash functions.

**Definition 3.1 (Davies-Meyer Compression Function):** Given a block cipher $E_k(m)$ with key $k$ and block size $n$, the Davies-Meyer compression function $f$ is defined as:
$$f(H_{i-1}, M_i) = E_{M_i}(H_{i-1}) \oplus H_{i-1}$$

where $\oplus$ denotes XOR operation, $H_{i-1}$ is the previous hash value (used as plaintext), and $M_i$ is the current message block (used as encryption key).

**Algorithm 3.1 (Davies-Meyer Hash):**

1. Split message $M$ into blocks $M_1, M_2, ..., M_t$
2. Initialize $H_0 = IV$ (e.g., zero vector)
3. For $i = 1$ to $t$:
   $$H_i = E_{M_i}(H_{i-1}) \oplus H_{i-1}$$
4. Output $H_t$ as the message digest

**Theorem 3.1 (Security Properties):** If the underlying block cipher $E$ is an ideal cipher (i.e., behaves like a random permutation for each key), then the Davies-Meyer construction provides security comparable to the block size $n$.

_Proof Sketch:_ The security of Davies-Meyer relies on the following properties:

- **Pre-image Resistance:** Given $H_i$, recovering $H_{i-1}$ requires inverting the block cipher, which is computationally infeasible for a secure block cipher.
- **Collision Resistance:** A collision $f(x, m) = f(x', m')$ implies $E_m(x) \oplus x = E_m(x') \oplus x'$. This requires finding two inputs to the block cipher that produce a specific XOR relationship—essentially equivalent to breaking the block cipher.
- **Fixed Point Vulnerability:** If $E_{M_i}(H_{i-1}) = H_{i-1}$, then $H_i = H_{i-1}$ (fixed point). While theoretically possible, finding such instances requires approximately $2^{n/2}$ operations for an ideal cipher.

### 3.2 Worked Numerical Example

**Problem:** Given a hypothetical 2-bit block cipher with the following properties:

- Encryption table: $E_{00}(00)=11$, $E_{00}(01)=10$, $E_{00}(10)=00$, $E_{00}(11)=01$
- $E_{01}(00)=10$, $E_{01}(01)=11$, $E_{01}(10)=01$, $E_{01}(11)=00$
- $E_{10}(00)=01$, $E_{10}(01)=00$, $E_{10}(10)=11$, $E_{10}(11)=10$
- $E_{11}(00)=00$, $E_{11}(01)=10$, $E_{11}(10)=01$, $E_{11}(11)=11$

Compute Davies-Meyer hash for message blocks $M_1 = 10$, $M_2 = 01$ with $H_0 = 00$.

**Solution:**

**Round 1:**

- Input: $H_0 = 00$, $M_1 = 10$
- $E_{10}(00) = 01$ (from table)
- $H_1 = 01 \oplus 00 = 01$

**Round 2:**

- Input: $H_1 = 01$, $M_2 = 01$
- $E_{01}(01) = 11$ (from table)
- $H_2 = 11 \oplus 01 = 10$

**Final Hash:** 10 (binary) = 2 (decimal)

### 3.3 Comparative Analysis with Secure Hash Functions

| Property                 | Simple Modulo Hash  | Davies-Meyer                         | SHA-256                       |
| ------------------------ | ------------------- | ------------------------------------ | ----------------------------- |
| **Collision Resistance** | None (O(1) to find) | Depends on cipher                    | $2^{128}$ operations          |
| **Pre-image Resistance** | None                | Moderate                             | $2^{256}$ operations          |
| **Output Size**          | ~log₂(p) bits       | Block cipher size                    | 256 bits                      |
| **Structure**            | Linear              | Non-linear (cipher)                  | Merkle-Damgård + Davies-Meyer |
| **Practical Use**        | None                | Historical (MD5, SHA-1 used similar) | Standards (SHA-2 family)      |

Modern hash functions like SHA-256 employ the Davies-Meyer construction within the Merkle-Damgård structure, but with carefully designed compression functions (not off-the-shelf block ciphers) and significantly larger output sizes to resist birthday attacks.

## Summary

This module examined two fundamental hash function constructions: the Simple Modulo Hash, which fails dramatically due to its linear structure and minimal computational complexity, and the Davies-Meyer construction, which provides substantially stronger security guarantees when combined with a robust block cipher. While neither construction is suitable for direct cryptographic deployment in modern systems, understanding their theoretical foundations and security limitations is essential for appreciating the sophisticated design of contemporary hash functions like SHA-256.
