# Computational Aspects of PRNGs - Summary

## Key Definitions

- **Computational Complexity:** The measure of computational resources (time and space) required to generate pseudorandom sequences.
- **Min-Entropy:** H∞(X) = -log₂(max_x Pr[X=x]), measuring the worst-case unpredictability of a random variable.
- **Next-Bit Test:** A statistical test where an adversary must predict the next bit in the sequence with probability better than 1/2 + ε.
- **Polynomial-Time Adversary:** An algorithm whose running time is bounded by a polynomial in the security parameter.
- **Negligible Function:** A function that decays faster than the inverse of any polynomial.

## Important Formulas

- **Period Bound:** Period ≤ 2^(state_bits) for any deterministic PRNG
- **Birthday Bound:** After 2^(n/2) outputs from period 2^n PRNG, collision probability ≈ 50%
- **BBS Complexity:** O(log³n) per output bit (quadratic residuosity based)
- **LCG Complexity:** O(1) per output (linear recurrence)
- **Entropy Extraction:** Output bits = min-entropy - 2log(1/ε) for ε-statistical security

## Key Points

1. Cryptographic PRNGs require polynomial-time indistinguishability from true random sequences.

2. The state space size directly determines the maximum period—a 128-bit state provides maximum period 2¹²⁸.

3. BBS provides provable security based on quadratic residuosity but at significant computational cost.

4. The next-bit test is the gold standard—passing it implies passing all efficient statistical tests (Yao's Theorem).

5. Hardware PRNGs offer speed advantages while software PRNGs provide flexibility and easier testing.

6. Entropy extraction transforms weak random sources into cryptographically secure seeds using universal hash functions.

7. Block ciphers in counter mode and hash functions provide efficient building blocks for practical PRNG construction.

8. Side-channel considerations (timing, power analysis) affect real-world PRNG implementation security.

## Common Mistakes

1. **Confusing period with security:** A long period is necessary but not sufficient for cryptographic security—LCGs have long periods but are predictable.

2. **Ignoring state management:** Failing to properly initialize and protect PRNG state enables attacks even with theoretically secure algorithms.

3. **Underestimating entropy requirements:** Using insufficient entropy in seeds defeats all subsequent cryptographic operations.

4. **Overlooking implementation vulnerabilities:** Mathematical security proofs assume ideal implementation; practical side-channels often break systems.