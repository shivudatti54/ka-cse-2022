# The RSA Algorithm

## Introduction

The RSA algorithm, named after its inventors Rivest, Shamir, and Adleman (1977), represents one of the most significant breakthroughs in modern cryptography as the first practical public-key cryptosystem. Unlike symmetric key cryptosystems that rely on a shared secret key, RSA enables secure communication between parties who have never met or shared any prior secret information. This fundamental capability addresses the critical key distribution problem that has plagued classical cryptography for centuries. The security of RSA rests upon the computational difficulty of factoring large composite numbers into their prime factors—a problem that has withstood intensive mathematical scrutiny for over four decades.

The RSA algorithm operates on the mathematical principles of modular arithmetic and number theory, specifically leveraging properties of Euler's totient function and the difficulty of the integer factorization problem. When implemented with sufficiently large key sizes, RSA provides robust security for digital communications, electronic commerce, and data protection mechanisms worldwide. Despite the development of alternative public-key systems such as elliptic curve cryptography, RSA remains widely deployed and continues to serve as a cornerstone of modern cryptographic infrastructure, underpinning protocols such as SSL/TLS, digital signatures, and key exchange mechanisms.

## Mathematical Foundations

### Primality and Euler's Totient Function

The RSA algorithm fundamentally depends on properties of prime numbers and modular arithmetic. A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. The RSA key generation process requires the selection of two large prime numbers, typically denoted as $p$ and $q$, which satisfy specific security and efficiency criteria. These primes must be randomly generated, of sufficient size (typically 1024-4096 bits in practice), and should be kept secret.

Euler's totient function, denoted as $\phi(n)$, counts the number of positive integers less than $n$ that are relatively prime to $n$ (i.e., share no common factors with $n$). For a prime number $p$, we have $\phi(p) = p - 1$, as all integers from 1 to $p-1$ are relatively prime to $p$. When $n$ is the product of two distinct primes $p$ and $q$, the totient function yields $\phi(n) = \phi(pq) = (p-1)(q-1) = pq - p - q + 1$. This property is essential for computing the RSA private exponent $d$.

The mathematical relationship governing RSA security arises from the fact that while computing $\phi(n)$ is straightforward when the prime factors $p$ and $q$ are known, determining these factors from $n$ alone becomes computationally infeasible for sufficiently large values. This asymmetry—easy to compute in the forward direction but extraordinarily difficult to reverse—forms the computational basis for RSA's security guarantee.

### Modular Arithmetic and the Extended Euclidean Algorithm

RSA operations occur within the finite cyclic group $\mathbb{Z}_n^*$, consisting of all integers modulo $n$ that have multiplicative inverses. The group has order $\phi(n)$, and for any element $a \in \mathbb{Z}_n^*$, Euler's theorem states that $a^{\phi(n)} \equiv 1 \pmod{n}$. This theorem enables the construction of encryption and decryption exponents that are multiplicative inverses modulo $\phi(n)$.

The Extended Euclidean Algorithm provides the computational mechanism for finding modular multiplicative inverses. Given two integers $a$ and $m$, the algorithm computes $a^{-1} \pmod{m}$ such that $a \cdot a^{-1} \equiv 1 \pmod{m}$. This algorithm runs in $O(\log m)$ time and is essential for computing the private exponent $d$ from the public exponent $e$ and $\phi(n)$. The algorithm also computes the greatest common divisor (GCD), ensuring that $\gcd(e, \phi(n)) = 1$ to guarantee the existence of the modular inverse.

## Key Generation Process

The RSA key generation process consists of five essential steps that produce the public key $(n, e)$ and the private key $(n, d)$. Understanding each step is crucial for both theoretical comprehension and practical implementation.

**Step 1: Prime Selection.** Select two distinct large prime numbers $p$ and $q$ of approximately equal bit-length. These primes should be chosen randomly using a cryptographically secure random number generator. For security, $p$ and $q$ should differ significantly in magnitude, and neither should be of the form $p-1$ or $p+1$ with small factors that would facilitate factorization.

**Step 2: Compute Modulus.** Calculate the RSA modulus $n = p \times q$. The bit-length of $n$ determines the security level—current recommendations specify minimum 2048-bit moduli for long-term security. The modulus $n$ is made public but computing its prime factors would break the system.

**Step 3: Compute Euler's Totient.** Calculate $\phi(n) = (p-1)(q-1)$. This value must remain secret and is used only during key generation. The security assumption states that computing $\phi(n)$ without knowing $p$ and $q$ is equivalent to factoring $n$.

**Step 4: Choose Public Exponent.** Select an integer $e$ such that $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$. The value $e$ is typically chosen as a small prime (commonly 65537 = $2^{16}+1$) for computational efficiency in encryption and signature verification. Smaller values of $e$ (such as 3) offer faster computation but may introduce vulnerabilities in certain padding schemes.

**Step 5: Compute Private Exponent.** Compute the private exponent $d$ as the modular multiplicative inverse of $e$ modulo $\phi(n)$, i.e., find $d$ such that $e \cdot d \equiv 1 \pmod{\phi(n)}$. Using the Extended Euclidean Algorithm, we compute $d = e^{-1} \pmod{\phi(n)}$. The private key consists of the pair $(n, d)$.

### Numerical Example

Consider a simplified example with small primes for illustration purposes. Let $p = 61$ and $q = 53$.

The modulus is $n = 61 \times 53 = 3233$. Euler's totient is $\phi(3233) = (61-1)(53-1) = 60 \times 52 = 3120$.

Choosing $e = 17$, we verify that $\gcd(17, 3120) = 1$. Computing $d$ using the Extended Euclidean Algorithm: $17 \times d \equiv 1 \pmod{3120}$, yielding $d = 2753$ (since $17 \times 2753 = 46801 = 15 \times 3120 + 1$).

The public key is $(n=3233, e=17)$ and the private key is $(n=3233, d=2753)$. For encryption of message $m = 65$: $c = 65^{17} \pmod{3233} = 2790$. For decryption: $m = 2790^{2753} \pmod{3233} = 65$.

## Encryption and Decryption

RSA encryption transforms a plaintext message $m$ (represented as an integer in the range $[0, n-1]$) into ciphertext $c$ using the public key $(n, e)$. The encryption operation computes $c = m^e \pmod{n}$, which can be efficiently performed using modular exponentiation algorithms such as square-and-multiply. The resulting ciphertext $c$ can be securely transmitted over insecure channels, as recovering $m$ from $c$ without the private exponent $d$ requires solving the underlying mathematical problem.

RSA decryption reverses this process using the private key $(n, d)$. The recipient computes $m = c^d \pmod{n}$ to recover the original plaintext. This operation also employs modular exponentiation and is computationally similar to encryption, though the choice of $d$ affects performance. With small public exponents like 65537, encryption is faster than decryption; this asymmetry aligns with scenarios where many parties encrypt data for a single recipient.

### Proof of Correctness

The correctness of RSA decryption follows directly from Euler's theorem. We must prove that for all valid messages $m$, $(m^e)^d \equiv m \pmod{n}$.

Since $e \cdot d \equiv 1 \pmod{\phi(n)}$, there exists an integer $k$ such that $e \cdot d = 1 + k \phi(n)$. Consider two cases:

**Case 1:** $\gcd(m, n) = 1$ (i.e., $m$ is not divisible by $p$ or $q$). Applying Euler's theorem:
$$(m^e)^d = m^{ed} = m^{1+k\phi(n)} = m \cdot (m^{\phi(n)})^k \equiv m \cdot 1^k \equiv m \pmod{n}$$

**Case 2:** $\gcd(m, n) \neq 1$. Since $n = pq$ with distinct primes, $m$ must be a multiple of either $p$ or $q$ (but not both, as that would make $m$ a multiple of $n$, which is excluded by the message space). In this case, the Chinese Remainder Theorem can be applied to show that decryption still succeeds, yielding $m \pmod{n}$.

Thus, RSA decryption correctly recovers the original message for all valid inputs.

## Security Considerations

### Integer Factorization Problem

The security of RSA depends entirely on the computational difficulty of factoring large composite numbers. While no formal proof exists that factorization is inherently hard, extensive empirical evidence spanning decades supports this assumption. The best-known factoring algorithm for general integers, the General Number Field Sieve (GNFS), has exponential complexity in the bit-length of the modulus. For moduli of 2048 bits or larger, even the most powerful supercomputers require impractically large time commitments to factor.

The relationship between key size and security follows approximately exponential growth—a doubling of key size increases the computational work required for factorization by a factor substantially greater than two. Current recommendations suggest 2048-bit keys for medium-term security (through 2030) and 4096-bit keys for long-term protection.

### Padding Schemes and Attack Prevention

Raw RSA encryption exhibits deterministic behavior—encrypting the same message twice with the same key always produces identical ciphertext. This property enables various cryptanalytic attacks and violates semantic security. Furthermore, textbook RSA is vulnerable to chosen-ciphertext attacks (CCA) and mathematical manipulation attacks.

**RSA-OAEP (Optimal Asymmetric Encryption Padding)** addresses these vulnerabilities by adding random padding before encryption. OAEP uses a mask generation function (MGF) based on a hash function to randomize the plaintext, ensuring each encryption produces different ciphertexts. OAEP provides provable security under certain assumptions and is the standard for RSA encryption in modern protocols.

**RSA-PSS (Probabilistic Signature Scheme)** similarly provides padding for RSA signatures, offering provable security and protecting against existential forgery attacks. Both schemes are essential for secure RSA implementations and are mandated by contemporary cryptographic standards such as PKCS#1 v2.2 and TLS 1.3.

### Common Attacks and Key Sizes

Several attacks exploit implementation weaknesses rather than fundamental RSA vulnerabilities. **Timing attacks** measure computation time to extract private key information; constant-time implementations mitigate this risk. **Chosen-ciphertext attacks** (CCA1, CCA2) target specific protocol constructions; padding mechanisms like OAEP provide protection. **Small private exponent attacks** (Wiener's attack) become feasible when $d < n^{1/4}$; maintaining sufficiently large private exponents prevents this vulnerability.

Recommended key sizes evolve with computational advances. NIST guidelines recommend minimum 2048-bit keys through 2030, with 3072-bit or 4096-bit keys for longer security horizons. RSA Security estimates that factoring a 1024-bit RSA modulus requires approximately $10^{20}$ operations—feasible for well-resourced attackers but impractical for most. The 2048-bit modulus provides approximately $10^{30}$ operations, ensuring adequate security for contemporary applications.

## Computational Aspects

RSA operations involve modular exponentiation with exponents of size comparable to the modulus. The computational complexity of modular exponentiation using square-and-multiply is $O(\log e)$ or $O(\log d)$ multiplications, where each multiplication operates on $O(\log n)$ bit operands. Thus, the overall complexity is $O((\log n)^3)$ using naive multiplication, though Karatsuba and FFT-based methods improve practical performance.

Key generation is computationally the most expensive RSA operation, requiring primality testing of candidates. Probabilistic primality tests such as Miller-Rabin provide practical certainty with high probability after a small number of iterations. The Chinese Remainder Theorem (CRT) enables faster decryption by computing modular exponentiation separately modulo $p$ and $q$, reducing computation by approximately a factor of four.

## Exam Tips

1. **Understand the mathematical foundation**: Be thorough with Euler's totient function $\phi(n) = (p-1)(q-1)$ and its role in key generation. The relationship $e \cdot d \equiv 1 \pmod{\phi(n)}$ is fundamental.

2. **Master key generation steps**: Memorize the five-step key generation process: select primes, compute $n$, compute $\phi(n)$, choose $e$, compute $d$.

3. **Practice numerical examples**: Work through complete examples with small primes to understand encryption/decryption operations. Know how to compute modular exponentiation.

4. **Remember the correctness proof**: Understand how Euler's theorem guarantees that decryption reverses encryption. Be able to outline the proof.

5. **Know security assumptions**: The security rests on integer factorization being computationally hard. Understand why knowing $p$ and $q$ breaks RSA.

6. **Padding is essential**: Raw RSA is insecure; understand why padding schemes (OAEP, PSS) are necessary for semantic security and attack prevention.

7. **Key size recommendations**: Know current recommendations (2048-bit minimum through 2030) and understand the relationship between key size and security.

8. **Distinguish RSA applications**: RSA is used for both encryption and digital signatures. The mathematical operation is similar, but keys may be used differently.

9. **Implementation vulnerabilities**: Be aware of timing attacks, small $d$ attacks, and the importance of constant-time implementations.

10. **Protocol usage**: Understand how RSA fits into broader protocols like SSL/TLS, often for key exchange or digital certificates rather than bulk encryption.
