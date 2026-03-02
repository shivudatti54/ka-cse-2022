# **Blum Blum Shub Generator**


## Table of Contents

- [**Blum Blum Shub Generator**](#blum-blum-shub-generator)
- [**Introduction**](#introduction)
- [**Theory**](#theory)
  - [Definition](#definition)
  - [Blum Blum Shub Algorithm](#blum-blum-shub-algorithm)
  - [Properties](#properties)
- [**Applications**](#applications)
- [**Key Concepts**](#key-concepts)
- [**Example**](#example)
- [**Code Implementation**](#code-implementation)
- [Example usage:](#example-usage)

## **Introduction**

The Blum Blum Shub (BBS) generator is a type of pseudorandom number generator (PRNG) used in cryptography to generate a sequence of random-looking numbers. It is a stream cipher that uses a combination of modular arithmetic and the properties of prime numbers to produce a sequence of numbers that appear to be randomly distributed.

## **Theory**

### Definition

A pseudorandom number generator (PRNG) is a mathematical algorithm that produces a sequence of numbers that appear to be randomly distributed, but are actually deterministic, meaning that they can be reproduced by applying the same algorithm to the same seed value.

### Blum Blum Shub Algorithm

The Blum Blum Shub algorithm uses a combination of modular arithmetic and the properties of prime numbers to produce a sequence of numbers. The algorithm takes two prime numbers, `p` and `q`, as input, and produces a sequence of numbers using the following formula:

`s_n = (s_{n-1}^2) mod pq`

where `s_n` is the next number in the sequence, `s_{n-1}` is the previous number in the sequence, and `pq` is the product of the two prime numbers.

### Properties

The BBS algorithm has several properties that make it useful for cryptographic applications:

- **Periodicity**: The sequence produced by the BBS algorithm is periodic, meaning that it repeats after a certain number of iterations.
- **Uniformity**: The sequence produced by the BBS algorithm is uniformly distributed, meaning that each number in the sequence is equally likely to appear.
- **Predictability**: The BBS algorithm is predictable, meaning that the next number in the sequence can be calculated given the previous number.

## **Applications**

The Blum Blum Shub generator is used in various cryptographic applications, including:

- **Stream ciphers**: The BBS algorithm is used as a stream cipher to encrypt and decrypt data.
- **Random number generation**: The BBS algorithm is used to generate random numbers for use in cryptographic applications.

## **Key Concepts**

- **Prime numbers**: Prime numbers are numbers that are divisible only by 1 and themselves. The BBS algorithm uses two prime numbers, `p` and `q`.
- **Modular arithmetic**: Modular arithmetic is a system of arithmetic that "wraps around" after reaching a certain value, called the modulus.
- **Periodicity**: Periodicity refers to the repeating pattern of a sequence.
- **Uniformity**: Uniformity refers to the equal likelihood of each number in a sequence.

## **Example**

Suppose we want to use the BBS algorithm to generate a sequence of numbers with `p = 17` and `q = 23`. We start with a seed value `s_0 = 3`. The first few numbers in the sequence are:

`s_1 = (s_0^2) mod pq = (3^2) mod (17 * 23) = 9 mod 391 = 9`

`s_2 = (s_1^2) mod pq = (9^2) mod (17 * 23) = 81 mod 391 = 235`

`s_3 = (s_2^2) mod pq = (235^2) mod (17 * 23) = 55225 mod 391 = 180`

And so on.

## **Code Implementation**

Here is an example implementation of the BBS algorithm in Python:

```python
def blum_blum_shub(p, q, seed):
    pq = p * q
    s = seed
    while True:
        s = (s ** 2) % pq
        yield s

# Example usage:
p = 17
q = 23
seed = 3
generator = blum_blum_shub(p, q, seed)
for i in range(10):
    print(next(generator))
```

This code defines a function `blum_blum_shub` that takes two prime numbers `p` and `q`, and a seed value `seed`, and returns a generator that produces a sequence of numbers using the BBS algorithm. The example usage shows how to use the generator to produce the first 10 numbers in the sequence.
