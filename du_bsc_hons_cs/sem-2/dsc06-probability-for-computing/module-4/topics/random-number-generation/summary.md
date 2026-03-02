# Random Number Generation - Summary

## Key Definitions and Concepts

- **Random Number Generation (RNG)**: The process of generating a sequence of numbers that lack any discernible pattern, essential for simulations, cryptography, and statistical sampling.

- **True Random Number Generator (TRNG)**: Generates random numbers from physical phenomena (thermal noise, radioactive decay) that are inherently unpredictable; requires specialized hardware.

- **Pseudo-Random Number Generator (PRNG)**: Mathematical algorithm producing deterministic sequences that appear random; given the same seed, always produces identical sequences.

- **Seed**: Initial value that starts a PRNG; determines the entire sequence of "random" numbers generated.

- **Period**: Length of sequence before a PRNG begins repeating; longer periods are preferable for large-scale simulations.

## Important Formulas and Theorems

- **LCG Recurrence Relation**: Xₙ₊₁ = (a × Xₙ + c) mod m
  - Where a = multiplier, c = increment, m = modulus
  - Output normalized: U = X/m (produces uniform [0,1] values)

- **Chi-Square Test Statistic**: χ² = Σ[(Oᵢ - Eᵢ)²/Eᵢ]
  - Oᵢ = observed frequency in bin i
  - Eᵢ = expected frequency under uniform distribution
  - Degrees of freedom = k - 1 (where k = number of bins)

- **Monte Carlo π Estimation**: π ≈ 4 × (points inside quarter circle) / (total points)

## Key Points

- Computers are deterministic; true randomness requires physical phenomena or careful algorithmic design.

- PRNGs are faster and reproducible but predictable; TRNGs are truly random but slower and require hardware.

- The Linear Congruential Generator (LCG) is the fundamental PRNG algorithm; parameter selection critically affects quality.

- Good RNGs must satisfy: uniformity (even distribution), independence (no correlation), unpredictability, long period, and reproducibility.

- The Chi-Square test validates uniformity; p-value > 0.05 indicates the sequence is consistent with uniformity.

- Python's Mersenne Twister (`random` module) is suitable for simulations; `secrets` module for cryptography.

- Seeding enables reproducibility—essential for debugging and scientific experiment replication.

## Common Mistakes to Avoid

- Confusing TRNG and PRNG: PRNGs are NOT truly random despite appearing so—they are deterministic.

- Incorrect chi-square interpretation: A LOW chi-square value and HIGH p-value indicate good uniformity (not the reverse).

- Using system time as seed in cryptographic applications—it creates predictable sequences vulnerable to attack.

- Ignoring period limitations: Using an LCG with period m=2^16 for 100,000 samples guarantees repeated values and biased results.

- Believing "more complex algorithm = better randomness"—simpler LCGs with well-chosen parameters often outperform complex algorithms.

## Revision Tips

1. **Practice LCG calculations**: Manually compute 3-4 iterations of an LCG with given parameters to internalize the algorithm.

2. **Memorize the five properties** of good RNGs and be ready to explain each with an example.

3. **Understand p-value interpretation**: Remember—high p-value = no evidence against null hypothesis = numbers appear uniform.

4. **Know the trade-offs**: When asked "PRNG vs TRNG," explain both directions: reproducibility/speed vs true unpredictability.

5. **Connect to applications**: Link each concept to real applications—cryptography (needs TRNG), simulation (needs long period PRNG), statistical sampling (needs reproducibility).