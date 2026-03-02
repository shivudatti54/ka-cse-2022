# Cyclic Codes


## Table of Contents

- [Cyclic Codes](#cyclic-codes)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition and Basic Properties](#definition-and-basic-properties)
  - [Polynomial Representation](#polynomial-representation)
  - [Generator and Parity Check Matrices](#generator-and-parity-check-matrices)
  - [Syndrome Decoding](#syndrome-decoding)
  - [Error Detection with Cyclic Codes](#error-detection-with-cyclic-codes)
- [Examples](#examples)
  - [Example 1: Constructing a Cyclic Code over GF(2)](#example-1-constructing-a-cyclic-code-over-gf2)
  - [Example 2: Syndrome Computation and Error Detection](#example-2-syndrome-computation-and-error-detection)
  - [Example 3: Systematic Encoding](#example-3-systematic-encoding)
- [Exam Tips](#exam-tips)

## Introduction

Cyclic codes represent one of the most important and practical classes of linear block codes in coding theory. Unlike general linear codes, cyclic codes possess a special algebraic structure where any cyclic shift of a valid codeword remains a valid codeword. This property makes them particularly attractive for implementation in hardware using shift registers and feedback connections, which explains their widespread use in real-world applications such as data storage systems, digital communications, and computer networks.

The significance of cyclic codes in modern engineering cannot be overstated. The widely used CRC (Cyclic Redundancy Check) codes, which form the backbone of error detection in Ethernet, ZIP files, PNG images, and countless other protocols, are all based on cyclic code theory. Cyclic codes are also fundamental to the construction of more complex codes like BCH codes and Reed-Solomon codes, which are essential in applications ranging from satellite communications to compact disc technology. Understanding cyclic codes provides the mathematical foundation necessary for grasping these advanced coding schemes.

## Key Concepts

### Definition and Basic Properties

A cyclic code is a linear block code C of length n that satisfies the cyclic shift property: if (c₀, c₁, ..., cₙ₋₁) is a codeword, then (cₙ₋₁, c₀, c₁, ..., cₙ₋₂) obtained by a right cyclic shift by one position is also a codeword. More generally, any cyclic shift of any codeword must remain a codeword. This property follows from the fact that cyclic codes are ideal in the ring Rₙ = GF(q)[x]/(xⁿ - 1), where GF(q) is the finite field of q elements.

For a cyclic code of length n over GF(q), the set of all codewords corresponds to all multiples of a unique monic polynomial g(x) called the generator polynomial, where g(x) divides xⁿ - 1. The degree of g(x) is called the dimension of the code, and the code can correct up to t errors where t depends on the minimum distance of the code.

### Polynomial Representation

In cyclic codes, codewords are represented as polynomials of degree less than n. The polynomial representation provides a powerful algebraic framework for encoding and decoding. A message block of length k is represented as a polynomial m(x) of degree less than k, and the corresponding codeword is obtained by multiplying m(x) by the generator polynomial g(x). The codeword polynomial c(x) = m(x) · g(x) has degree less than n.

The generator polynomial g(x) of a cyclic code of length n and dimension k is the unique monic polynomial of degree n - k that divides xⁿ - 1. If xⁿ - 1 = g(x) · h(x), then h(x) is called the parity check polynomial and has degree k. The parity check matrix can be constructed systematically from h(x), and any polynomial c(x) is a codeword if and only if c(x) · h(x) ≡ 0 mod (xⁿ - 1).

### Generator and Parity Check Matrices

The generator matrix G for a cyclic code can be constructed from the generator polynomial g(x) of degree r = n - k. The first row is g(x), the second row is x·g(x), the third is x²·g(x), and so on until we have k rows. Each row is represented as a coefficient vector of length n. The parity check matrix H can similarly be constructed from the parity check polynomial h(x) or directly from g(x).

For systematic encoding, where the message bits appear unchanged in the codeword, we use the systematic generator matrix formed by placing the k×k identity matrix alongside the generator matrix of the cyclic prefix. Alternatively, systematic encoding can be performed polynomially by computing the remainder when xⁿ⁻ᵏ · m(x) is divided by g(x), then subtracting this remainder.

### Syndrome Decoding

For decoding cyclic codes, we compute the syndrome of the received polynomial r(x) as the remainder when r(x) is divided by g(x). If the syndrome is zero, the received word is a valid codeword. Otherwise, the syndrome indicates the presence of errors. The syndrome polynomial s(x) = r(x) mod g(x) has degree less than the degree of g(x).

For simple cyclic codes like single-error-correcting codes, we can construct a syndrome table that maps each possible syndrome to the corresponding error pattern. More sophisticated decoding algorithms, such as the Meggit decoder, exploit the cyclic structure to simplify the decoding process by iteratively testing whether the current syndrome corresponds to an error in a specific position.

### Error Detection with Cyclic Codes

Cyclic codes are extensively used for error detection due to their excellent detection capabilities. A cyclic code can detect all error patterns of weight less than its minimum distance d. Furthermore, cyclic codes can detect all burst errors of length less than or equal to the degree of the generator polynomial. This makes them ideal for detecting common transmission errors that often occur in bursts.

The CRC-32 code used in Ethernet and many other standards can detect all burst errors of length 32 or less, and has a probability of undetected error of approximately 2⁻³² for random errors, making it extremely reliable for practical applications.

## Examples

### Example 1: Constructing a Cyclic Code over GF(2)

Consider a (7,4) cyclic code over GF(2). The polynomial x⁷ - 1 factors over GF(2) as (x + 1)(x³ + x + 1)(x³ + x² + 1). To construct a cyclic code of dimension k = 4 (so n - k = 3), we need a generator polynomial of degree 3. Taking g(x) = x³ + x + 1, we have a (7,4) cyclic code.

To encode the message m = (1, 0, 1, 1), represented as m(x) = 1 + x² + x³, we compute c(x) = m(x) · g(x) = (1 + x² + x³)(x³ + x + 1). Multiplying: (x³ + x + 1) + (x⁵ + x³ + x²) + (x⁶ + x⁴ + x³) = x⁶ + x⁵ + x⁴ + x² + x + 1.

Thus the codeword is c = (1, 1, 1, 0, 1, 1, 1). This is a systematic code with the message embedded in the first four positions.

### Example 2: Syndrome Computation and Error Detection

Using the same (7,4) cyclic code with g(x) = x³ + x + 1, suppose we receive r = (1, 1, 1, 0, 1, 1, 0), where the last bit may be in error. The received polynomial is r(x) = 1 + x + x² + x³ + x⁴ + x⁵.

To compute the syndrome, divide r(x) by g(x) = x³ + x + 1. Performing polynomial division over GF(2): x⁵ + x⁴ + x³ + x² + x + 1 divided by x³ + x + 1 gives a remainder of x² + x + 1.

Since the syndrome is non-zero (s(x) = x² + x + 1), we know an error has occurred. The error pattern e(x) = x⁶ would give syndrome x² + x + 1, indicating the seventh bit is in error.

### Example 3: Systematic Encoding

For the (7,4) cyclic code with g(x) = x³ + x + 1, perform systematic encoding of message m = (1, 0, 0, 1). First, form m(x) = 1 + x³. Multiply by xⁿ⁻ᵏ = x³: x³ · m(x) = x³ + x⁶.

Now divide by g(x): x⁶ + x³ divided by x³ + x + 1 gives remainder x + 1. The systematic codeword is c(x) = x⁶ + x³ + (x + 1) = x⁶ + x³ + x + 1, giving c = (1, 1, 0, 1, 0, 0, 1).

## Exam Tips

1. **Remember the defining property**: Any cyclic shift of a codeword in a cyclic code must also be a codeword. This is the fundamental property that distinguishes cyclic codes from general linear codes.

2. **Generator polynomial is key**: The generator polynomial g(x) uniquely determines the cyclic code. It must divide xⁿ - 1, and its degree r = n - k gives the number of parity bits.

3. **Understand polynomial arithmetic**: All operations in cyclic codes are performed in the polynomial ring modulo (xⁿ - 1), meaning you must reduce all results modulo this polynomial.

4. **Systematic encoding steps**: For systematic encoding, multiply message polynomial by xⁿ⁻ᵏ, divide by g(x), subtract the remainder, then add to get the final codeword.

5. **Syndrome is the remainder**: The syndrome of a received word is simply the remainder when the received polynomial is divided by the generator polynomial. Zero syndrome means no detected errors.

6. **Minimum distance matters**: The minimum distance d of a cyclic code determines its error-correcting capability t = ⌊(d-1)/2⌋ and error-detecting capability d-1.

7. **Connection to BCH and Reed-Solomon**: Remember that BCH codes and Reed-Solomon codes are subclasses of cyclic codes, making this topic foundational for understanding these advanced codes.

8. **Practical applications**: CRC codes are prime examples of cyclic codes used in practice. Know that CRC-32 uses generator polynomial x³² + x²⁶ + x²³ + x²² + x¹⁶ + x¹² + x¹¹ + x¹⁰ + x⁸ + x⁷ + x⁵ + x⁴ + x² + x + 1.
