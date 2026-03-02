# Randomized Algorithm Design

## Introduction
Randomized algorithms leverage probabilistic choices to achieve efficiency gains or simplify complex deterministic approaches. In modern computer science, they form the backbone of critical systems including cryptography (e.g., RSA primality testing), big data processing (Bloom filters), and machine learning (stochastic gradient descent). Unlike deterministic algorithms, they trade absolute certainty for practical efficiency, often achieving polynomial-time solutions for NP-hard problems through approximation.

The theoretical foundation lies in probability theory and computational complexity analysis. From a research perspective, recent advances in quantum-randomized hybrid algorithms and differential privacy mechanisms demonstrate their growing importance. For DU MSc students, mastering this paradigm is essential for tackling cutting-edge problems in distributed systems, optimization, and secure computation.

## Key Concepts
1. **Las Vegas vs Monte Carlo Algorithms**:
   - Las Vegas: Always correct (e.g., Randomized Quicksort), runtime varies
   - Monte Carlo: Bounded runtime, probabilistic correctness (e.g., Miller-Rabin primality test)

2. **Randomization Techniques**:
   - Random sampling (e.g., Reservoir Sampling)
   - Fingerprinting (polynomial identity verification)
   - Randomized rounding (LP relaxation solutions)
   - Hashing (Count-Min Sketch for frequency estimation)

3. **Probabilistic Analysis**:
   - Expected runtime (linearity of expectation)
   - High-probability bounds (Chernoff bounds)
   - Amplification: Boosting success probability via repetition

4. **Derandomization**:
   - Method of conditional probabilities
   - Using pseudorandom generators (Nisan-Wigderson)

## Examples

**1. Randomized QuickSort Analysis**
```python
def quicksort(arr):
    if len(arr) <= 1: return arr
    pivot = random.choice(arr)
    L = [x for x in arr if x < pivot]
    M = [x for x in arr if x == pivot]
    R = [x for x in arr if x > pivot]
    return quicksort(L) + M + quicksort(R)
```
*Analysis*: Expected comparisons = O(n log n). Worst-case O(n²) but probability < 1/n! for adversarial input.

**2. Karger's Min-Cut Algorithm**
1. While >2 vertices remain:
   - Pick random edge (u,v)
   - Contract u and v
2. Return remaining edges as cut

*Success Probability*: At least 2/(n(n-1)). Repeating n² ln n times gives 1 - 1/n success probability.

**3. Bloom Filter Implementation**
Given m bits and k hash functions:
- Insert(x): Set bits h₁(x)...hₖ(x)
- Query(x): Check all k bits

False positive probability = (1 - e^(-kn/m))^k. Optimal k ≈ (m/n) ln 2.

## Exam Tips
1. Always specify whether an algorithm is Las Vegas or Monte Carlo
2. For expectation calculations, use linearity of expectation even with dependencies
3. Memorize key probability bounds: Markov, Chebyshev, Chernoff
4. In derandomization questions, look for existence proofs (probabilistic method)
5. When asked to design, consider: Random sampling vs hashing vs fingerprinting
6. For approximation algorithms, calculate expected approximation ratio
7. Recent DU papers emphasize applications in blockchain (consensus algorithms) and ML (randomized optimization)