# Public Key Cryptanalysis

## Introduction

Public key cryptanalysis refers to the study of mathematical and computational techniques used to break or compromise public key cryptographic systems. Unlike symmetric cryptography where the primary concern is key recovery, public key cryptanalysis focuses on exploiting the underlying mathematical problems upon which these cryptosystems are built. The security of most public key cryptosystems relies on the computational hardness of certain mathematical problems such as integer factorization, discrete logarithm computation, and elliptic curve discrete logarithm problems. This chapter examines the major cryptanalytic techniques used against RSA, Diffie-Hellman, and elliptic curve cryptosystems, providing both theoretical understanding and practical insights into attack complexities.

The fundamental premise of public key cryptography is that certain mathematical operations are easy to perform in one direction but computationally infeasible to reverse without secret information. Cryptanalysis seeks to either completely break a system (recover the private key) or partially break it (recover plaintext from ciphertext without the key). Understanding these attack methodologies is essential for both security professionals designing cryptographic systems and auditors evaluating their security margins. The relationship between key size and computational security follows carefully studied bounds, and cryptanalysis provides the mathematical foundations for establishing these security parameters.

Modern cryptanalysis has evolved beyond purely mathematical attacks to include implementation-based attacks that exploit side-channel information, protocol attacks that target weaknesses in how cryptographic primitives are combined, and chosen ciphertext attacks that leverage properties of specific decryption operations. A comprehensive understanding of public key cryptanalysis requires familiarity with both the mathematical foundations of these attacks and the practical considerations of their real-world applicability.

## Key Concepts

### Integer Factorization Problem (IFP)

The security of RSA rests on the computational difficulty of factoring large composite numbers into their prime factors. Given a modulus $n = p \times q$ where $p$ and $q$ are large primes, the goal of an attacker is to recover either the primes themselves or the private exponent $d$ from the public key $(e, n)$. The most efficient known factorization algorithms include the General Number Field Sieve (GNFS), which currently holds the record for factoring RSA-like numbers. The GNFS has a sub-exponential complexity of approximately $\exp((\sqrt[3]{64/9} + o(1))(\ln n)^{1/3}(\ln\ln n)^{2/3})$, making it infeasible to break RSA with sufficiently large key sizes.

**Pollard's Rho Algorithm** provides an example of a factorization method with exponential complexity. The algorithm uses Floyd's cycle detection technique to find a non-trivial factor of $n$. The algorithm works by iterating a function $f(x) = x^2 + 1 \pmod n$ starting from two sequences, and when these sequences collide modulo a non-trivial factor, factoring is achieved. The expected running time is $O(\sqrt{p})$ where $p$ is the smallest prime factor, making it effective for finding small factors but impractical for large composite moduli with large prime factors.

**Fermat's Factorization Method** exploits the representation of $n$ as a difference of squares: $n = x^2 - y^2 = (x+y)(x-y)$. Starting from $\lceil\sqrt{n}\rceil$ and incrementing $x$ until $x^2 - n$ becomes a perfect square, we obtain $y = \sqrt{x^2 - n}$. This method is efficient when $p$ and $q$ are close together, which is why RSA implementations require primes of approximately equal size. The complexity is $O((q-p)/2)$ operations, becoming trivial when the primes are sufficiently close.

### Discrete Logarithm Problem (DLP)

The discrete logarithm problem forms the security foundation for Diffie-Hellman key exchange and the Digital Signature Algorithm (DSA). Given a prime $p$, a generator $g$ of the multiplicative group $\mathbb{Z}_p^*$, and a value $h = g^x \pmod p$, the goal is to compute $x = \log_g h$. The security assumes that no efficient algorithm exists for this problem for sufficiently large $p$, with the best known attacks being the Giant-Step Baby-Step (GSBS) algorithm and the Index Calculus method.

The **Baby-Step Giant-Step (BSGS) algorithm** achieves $O(\sqrt{m})$ time and space complexity for a group of order $m$. It works by precomputing a table of baby steps $\{g^j \mid 0 \leq j < \sqrt{m}\}$ and then testing giant steps $h \cdot g^{-i\sqrt{m}}$ for matches in the table. This algorithm establishes that the discrete logarithm problem requires at least $O(\sqrt{m})$ operations, providing a lower bound for key size selection.

The **Index Calculus Method** achieves sub-exponential complexity similar to integer factorization. For groups $\mathbb{Z}_p^*$, this method involves selecting a factor base of small primes, solving linear equations modulo $p$ to find logarithms of factor base elements, and then expressing the target as a product of factor base elements to compute its discrete logarithm. This makes larger key sizes necessary for security against this attack.

### Elliptic Curve Discrete Logarithm Problem (ECDLP)

Elliptic curve cryptography achieves equivalent security to traditional public key systems with significantly smaller key sizes due to the hardness of the elliptic curve discrete logarithm problem. Given points $P$ and $Q = kP$ on an elliptic curve, computing $k$ is believed to require fully exponential time. The MOV attack reduces the ECDLP to a DLP in an extension field for certain special curves, but for properly selected curves, no sub-exponential attacks are known.

### Attacks on RSA

**Wiener's Attack** exploits small private exponents. When the private exponent $d$ satisfies $d < n^{1/4}/3$, Wiener's algorithm using continued fractions can recover $d$ from the public exponent $e$. The attack succeeds because approximations to $e/n$ provide information about $d/k$ where $k = (ed - 1)/\phi(n)$. Modern RSA implementations ensure $d$ is sufficiently large to resist this attack, typically requiring $d > n^{1/4}$.

** Hastad's Broadcast Attack** applies when the same message is encrypted with the same public exponent to multiple recipients. If the same plaintext $M$ is encrypted with the same exponent $e$ to $e$ different recipients having coprime moduli $n_1, n_2, ..., n_e$, the attacker can recover $M$ using the Chinese Remainder Theorem since $M^e \pmod{n_i}$ values are known for all $i$. Padding with random padding prevents this attack, which is why OAEP padding is recommended.

** Coppersmith's Method** is a powerful lattice-based attack that can find small roots of polynomial equations modulo $n$. This technique can be used to factor $n$ given partial knowledge of the primes or to recover plaintext from RSA with low exponent padding weaknesses. The method uses lattice reduction techniques to solve for small solutions to modular equations.

### Side-Channel Attacks

**Timing Attacks** exploit variations in execution time during cryptographic operations. For RSA, the sliding window exponentiation and Montgomery multiplication implementations may leak information through timing variations that reveal bits of the private key. Attacks like Kocher's timing attack can recover the entire private key by carefully measuring decryption times for thousands of chosen ciphertexts.

**Power Analysis Attacks** monitor power consumption during cryptographic operations. Simple Power Analysis (SPA) can reveal bit patterns in private operations, while Differential Power Analysis (DPA) uses statistical methods to extract secret information from multiple traces. These attacks are particularly relevant for smart cards and embedded devices where physical access enables detailed measurement.

## Examples

**Example 1: Fermat Factorization on Weak RSA Modulus**

Consider $n = 1649$. Using Fermat's method:

- $\lceil\sqrt{1649}\rceil = 41$
- $41^2 - 1649 = 1681 - 1649 = 32$ (not a square)
- $42^2 - 1649 = 1764 - 1649 = 115$ (not a square)
- $43^2 - 1649 = 1849 - 1649 = 200$ (not a square)
- $44^2 - 1649 = 1936 - 1649 = 287$ (not a square)
- $45^2 - 1649 = 2025 - 1649 = 376$ (not a square)
- $46^2 - 1649 = 2116 - 1649 = 467$ (not a square)
- $47^2 - 1649 = 2209 - 1649 = 560$ (not a square)
- $48^2 - 1649 = 2304 - 1649 = 655$ (not a square)
- $49^2 - 1649 = 2401 - 1649 = 752$ (not a square)
- $50^2 - 1649 = 2500 - 1649 = 851$ (not a square)
- $51^2 - 1649 = 2601 - 1649 = 952$ (not a square)
- $52^2 - 1649 = 2704 - 1649 = 1055$ (not a square)
- $53^2 - 1649 = 2809 - 1649 = 1160$ (not a square)
- $54^2 - 1649 = 2916 - 1649 = 1267$ (not a square)
- $55^2 - 1649 = 3025 - 1649 = 1376$ (not a square)
- $56^2 - 1649 = 3136 - 1649 = 1487$ (not a square)
- $57^2 - 1649 = 3249 - 1649 = 1600 = 40^2$

Thus $x = 57$, $y = 40$, giving factors: $n = (57+40)(57-40) = 97 \times 17 = 1649$.

This demonstrates how Fermat factorization succeeds when prime factors are close.

**Example 2: Wiener's Attack on Small Private Exponent**

Given public key $(e, n) = (17993, 90581)$, Wiener's attack proceeds as follows:

- Compute continued fraction expansion of $e/n = 17993/90581$
- The convergents provide approximations $k/d$ where $k = (ed-1)/\phi(n)$
- Testing convergents, we find $d = 601$ satisfies $ed - 1$ being divisible by $\phi(n)$
- Verification: $601 \times 17993 = 10823493$, and $\phi(n) = n - p - q + 1 = 90581 - 277 - 281 + 1 = 90024$
- Since $10823493 \equiv 90024 \times 120 + 90024 = 10802880 + 90024 = 10892904$... (calculation continues)

The attack successfully recovers the small private exponent, demonstrating why minimum bounds on $d$ are essential.

**Example 3: Baby-Step Giant-Step for Discrete Log**

To solve $2^x \equiv 15 \pmod{47}$:

- Let $m = \lceil\sqrt{46}\rceil = 7$
- Compute baby steps: $2^0=1, 2^1=2, 2^2=4, 2^3=8, 2^4=16, 2^5=32, 2^6=17$
- Compute giant steps: $15 \cdot (2^{-7})^i \pmod{47}$ for $i = 0, 1, 2, ...$
- For $i = 1$: $15 \cdot (2^{-7}) = 15 \cdot 30 = 21$ (no match)
- For $i = 3$: $15 \cdot (2^{-21}) = 15 \cdot 25 = 19$ (no match)
- Continuing, we find $x = 26$ since $2^{26} \equiv 15 \pmod{47}$

This example illustrates the algorithm's mechanics for small parameters.

## Exam Tips

1. **Key Size Recommendations**: Understand the relationship between security levels and key sizes. RSA-2048 provides approximately 112 bits of security, while ECC-256 provides equivalent security with much smaller keys (roughly 256-bit keys for 128-bit security).

2. **Attack Applicability**: Different attacks apply under different conditions. Fermat factorization only works when primes are close; Wiener's attack requires small private exponents; timing attacks require physical proximity and multiple measurements.

3. **Padding Essentiality**: Always emphasize that raw RSA without padding is insecure. OAEP padding prevents Hastad's attack, while PSS padding provides security against chosen ciphertext attacks.

4. **Mathematical Foundations**: Understand the reductions between problems. Breaking RSA with small $e$ or small $d$ does not necessarily lead to factoring, but certain conditions do enable such reductions.

5. **Implementation Attacks**: Side-channel attacks often succeed against theoretically secure systems. Power analysis and timing attacks are practical threats requiring physical access but can completely compromise otherwise secure implementations.

6. **Protocol Attacks**: The man-in-the-middle attack on Diffie-Hellman demonstrates that cryptographic primitives alone do not guarantee security; authenticated key exchange protocols are necessary.

7. **Quantum Threat**: Be aware that Shor's algorithm threatens all integer factorization and discrete logarithm-based systems, driving interest in post-quantum cryptography.
