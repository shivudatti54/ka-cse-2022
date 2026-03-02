# Pseudorandom Number Generators (PRNGs) in Cryptography

## 1. Introduction and Formal Definitions

A **Pseudorandom Number Generator (PRNG)** is a deterministic computational procedure that takes as input a seed of length $k$ and produces an arbitrarily long sequence of bits that "appears" random to any efficient observer. Formally, we define a PRNG as a polynomial-time deterministic algorithm $G: \{0,1\}^k \rightarrow \{0,1\}^n$ (where $n \gg k$) such that the output distribution is computationally indistinguishable from the uniform distribution over $\{0,1\}^n$.

In cryptography, PRNGs serve as the backbone for generating cryptographic keys, nonces, initialization vectors (IVs), and padding values. The fundamental requirement is that these generated values must be unpredictable to any adversary with polynomial-time computational resources.

**Definition 1.1 (Statistical Test):** A statistical test $T$ is a probabilistic polynomial-time algorithm that, given an input string $x \in \{0,1\}^*$, outputs either "accept" ( $x$ appears random) or "reject" ( $x$ appears non-random). The advantage of $T$ in distinguishing $G(U_k)$ from $U_n$ is defined as:
$$\text{Adv}_T(G) = \left| \Pr[T(G(U_k)) = 1] - \Pr[T(U_n) = 1] \right|$$

where $U_k$ denotes the uniform distribution over $k$-bit strings.

## 2. Cryptographically Secure PRNGs (CSPRNGs)

A PRNG is **cryptographically secure** if no polynomial-time adversary can distinguish its output from true randomness with non-negligible advantage.

**Definition 2.1 (CSPRNG):** A PRNG $G: \{0,1\}^k \rightarrow \{0,1\}^n$ is a CSPRNG if for every probabilistic polynomial-time distinguisher $D$, there exists a negligible function $\varepsilon(\cdot)$ such that:
$$\text{Adv}_D(G) = \left| \Pr[D(G(U_k)) = 1] - \Pr[D(U_n) = 1] \right| \leq \varepsilon(k)$$

### 2.1 The Next-Bit Test

The **next-bit test** is a fundamental characterization of pseudorandomness. A generator passes the next-bit test if no polynomial-time algorithm can predict the $(i+1)$-th bit given the first $i$ bits, for any $i < n$.

**Theorem 2.1 (Yao, 1982):** A generator passes the next-bit test if and only if it is cryptographically secure.

_Proof Sketch:_ ($\Rightarrow$) If a generator fails the next-bit test, there exists a predictor $P$ that predicts bit $i+1$ from the first $i$ bits with advantage $\delta$. This predictor can be used to construct a distinguisher $D$ with advantage $\delta/2$, contradicting CSPRNG security. ($\Leftarrow$) If a generator is CSPRNG, consider any distinguisher $D$ attempting to predict bit $i+1$. If $D$ succeeds with probability $> 1/2 + \varepsilon$, we can construct an algorithm that breaks the CSPRNG property by using $D$ as a subroutine. $\square$

### 2.2 Forward and Backward Security

**Forward Security (State Compromise):** Even if an adversary learns the current internal state $S_i$, they cannot recover previously generated outputs $Y_1, Y_2, \ldots, Y_{i-1}$. This requires the update function to be one-way:
$$S_{i+1} = f(S_i) \text{ where } f \text{ is computationally hard to invert}$$

**Backward Security (Predictability):** Given the current state $S_i$, the adversary cannot predict future states $S_{i+1}, S_{i+2}, \ldots$ without performing computationally infeasible work.

## 3. Linear Congruential Generators (LCG): Mathematical Analysis

An LCG generates numbers using the recurrence:
$$S_{n+1} = (a \cdot S_n + c) \mod m$$

where $a$ is the multiplier, $c$ is the increment, and $m$ is the modulus.

### 3.1 Period Analysis

The **period** $P$ of an LCG is the length of the sequence before it repeats. The maximum possible period is $m$, achieved only under specific conditions:

**Theorem 3.1:** An LCG achieves full period $m$ if and only if:

1. $\gcd(c, m) = 1$ (increment is coprime to modulus)
2. $a-1$ is divisible by all prime factors of $m$
3. If $m$ is divisible by 4, then $a-1$ is divisible by 4

**Proof:** These are necessary and sufficient conditions for the recurrence to generate all residues modulo $m$ before cycling. $\square$

**Example 3.1:** Consider LCG with parameters $m = 2^{31} - 1$ (Mersenne prime), $a = 48271$ (minimal norm), $c = 0$. This achieves period $P = m - 1 \approx 2.1 \times 10^9$.

### 3.2 Cryptographic Weaknesses

LCGs are **not** suitable for cryptography due to fundamental vulnerabilities:

1. **State Recovery Attack:** Given $S_0$ and parameters $(a, c, m)$, all future outputs are trivially predictable. More critically, given just two consecutive outputs $S_i$ and $S_{i+1}$, we can recover the parameters in polynomial time.

2. **Reduced State Space:** If $m = 2^{31}$, the state space is only $2^{31}$ possible values, vulnerable to exhaustive search.

3. **Spectral Test Failure:** LCGs exhibit hyperplane structure—outputs lie on a finite number of hyperplanes in $d$-dimensional space, causing detectable correlations.

**Theorem 3.2:** Given three consecutive outputs $x_0, x_1, x_2$ from an LCG with $c = 0$, the multiplier $a$ can be recovered as:
$$a \equiv x_1 \cdot x_1^{-1} \pmod{m}$$
where $x_1^{-1}$ is the modular multiplicative inverse of $x_1$ modulo $m$.

## 4. Blum Blum Shub (BBS) Generator

The **Blum Blum Shub** generator provides provable security based on the integer factorization problem.

### 4.1 Algorithm Description

1. Select two large prime numbers $p$ and $q$ such that $p \equiv q \equiv 3 \pmod{4}$.
2. Compute $n = p \times q$ (the Blum integer).
3. Choose a random seed $s$ coprime to $n$; compute $S_0 = s^2 \mod n$.
4. For each iteration $i$:
   - Compute $S_{i+1} = S_i^2 \mod n$
   - Output the least significant bit of $S_i$ (or $\lfloor \log_2(S_i) \rfloor$ bits)

**Output:** $b_i = S_i \mod 2$ (parity bit)

### 4.2 Security Analysis

**Theorem 4.1 (Security of BBS):** If integer factorization is hard, then BBS is a CSPRNG.

_Proof Sketch:_ The security reduction proceeds as follows. Suppose an adversary $A$ can distinguish BBS output from random with advantage $\varepsilon$. We construct a factorization algorithm $F$ that, given $n = pq$, recovers $p$ or $q$:

1. Run $A$ on BBS output, obtaining some information about the state.
2. Use $A$ to compute $S_i$ from outputs, effectively solving the quadratic residue problem.
3. Using the ability to compute quadratic residues, compute $\left(\frac{S_i}{n}\right) = 1$, which reveals whether $S_i$ is a quadratic residue modulo $p$ or $q$.
4. With probability at least $\varepsilon/2$, this reveals one of the prime factors.

Thus, breaking BBS implies efficient factorization, contradicting standard cryptographic assumptions. $\square$

### 4.3 Computational Complexity

- **Per-output complexity:** $O(\log^3 n)$ bit operations (modular squaring)
- **State recovery:** Requires factoring $n$, complexity $O(e^{(1+o(1))(\ln n)^{1/2}(\ln \ln n)^{1/2}})$ using the General Number Field Sieve
- **Output rate:** Slow compared to block cipher-based generators

## 5. Modern CSPRNG Constructions

### 5.1 CTR_MODE_PRNG (Counter Mode PRNG)

This construction uses a block cipher in counter mode:

**Definition:**
$$\text{Output}_i = \text{AES}_K(\text{Counter} + i \mod 2^{128})$$

**Security:** If AES is a PRP (pseudorandom permutation), this construction is a CSPRNG. The proof follows from the indistinguishability of CTR mode from random.

**Theorem 5.1:** If $E_K$ is a secure block cipher, then the CTR_MODE_PRNG is a CSPRNG with advantage bounded by $\mathcal{O}(q^2/2^{128})$ where $q$ is the number of queries.

### 5.2 Hash-Based PRNG (ANSI X9.17)

This construction uses a hash function in feedback mode:

```
K = secret key (of hash function)
V = secret seed value
T = timestamp

S_{i+1} = Hash_K(T ⊕ V)
Output_i = Hash_K(S_{i+1} ⊕ T)
V = S_{i+1}
```

**Security:** Security reduces to the collision resistance and preimage resistance of the underlying hash function.

### 5.3 HMAC-Based PRNG (NIST SP 800-90A)

The NIST recommended construction:

```
K = HMAC(Key, Seed)
V = HMAC(K, 0x01)
for each request:
    V = HMAC(K, V)
    Output = V
    K = HMAC(K, V ⊕ 0x02)
    V = HMAC(K, V)
```

## 6. Seed Entropy Requirements

The security of any CSPRNG is contingent on the entropy of its seed.

**Definition 6.1 (Entropy):** For a random variable $X$ with probability distribution $P_X$, the min-entropy is:
$$H_\infty(X) = -\log_2\left(\max_{x} \Pr[X = x]\right)$$

**Theorem 6.1:** A CSPRNG requires a seed with at least 128 bits of entropy to achieve 128-bit security.

_Proof:_ If the seed has entropy $H < 128$, an adversary can exhaustively search the seed space in $2^H$ operations, achieving advantage $1$ with work $2^H$. For 128-bit security, we require $2^{128}$ work, hence $H \geq 128$. $\square$

**Seed Sources:**

- Hardware random number generators (thermal noise, radioactive decay)
- Environmental randomness (keyboard timing, mouse movements)
- /dev/urandom (Linux), CryptGenRandom (Windows)

## 7. Numerical Problems and Applications

### Problem 7.1: LCG Period Calculation

Given LCG parameters $m = 31$, $a = 3$, $c = 5$, determine the period starting from seed $S_0 = 1$.

**Solution:**

- $S_1 = (3 \times 1 + 5) \mod 31 = 8$
- $S_2 = (3 \times 8 + 5) \mod 31 = 29$
- $S_3 = (3 \times 29 + 5) \mod 31 = 31$
- $S_3 = 0 \mod 31$
- $S_4 = (3 \times 0 + 5) \mod 31 = 5$

Continuing, we find the period is 30 (full period since $\gcd(5, 31) = 1$).

### Problem 7.2: BBS Security Parameter

If $n = 391 = 17 \times 23$, show that BBS with this $n$ is insecure.

**Solution:**
Since we know the factorization $17 \times 23$, we can compute quadratic residues modulo 17 and modulo 23 separately using the Chinese Remainder Theorem, breaking the generator in polynomial time.

### Problem 7.3: CTR Mode Advantage Bound

Given AES-128 in CTR mode generating $q = 2^{40}$ blocks, compute the distinguishing advantage bound.

**Solution:**
Using Theorem 5.1: $\text{Adv} \leq q^2/2^{128} = 2^{80}/2^{128} = 2^{-48}$

This is negligible, confirming security for this number of queries.

## 8. Practical Considerations

### 8.1 Dual_EC_DRBG Controversy

The Dual Elliptic Curve Deterministic Random Bit Generator (Dual_EC_DRBG), standardized by NIST, was found to contain a potential backdoor. This highlights the importance of:

- Open-source algorithm design
- Peer review of cryptographic standards
- Verification of seed inputs

### 8.2 Recommended Generators

- **Linux:** ChaCha20-based /dev/urandom
- **Windows:** CryptGenRandom with AES-256
- **Java:** SecureRandom with SHA1PRNG or NativePRNG
- **Cryptographic Libraries:** libsodium's randombytes_implementation()
