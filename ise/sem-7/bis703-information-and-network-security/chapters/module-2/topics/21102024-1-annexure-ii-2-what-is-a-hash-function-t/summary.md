# Hash Functions and the Birthday Problem

### Key Concepts

- **Hash Function**: A one-way function that maps a variable-length input (e.g., a string or data) to a fixed-size output (e.g., a hash value or digest).
  - Definition: A hash function takes an input message and produces a fixed-size output, known as a message digest or hash value.
  - Formula: `h(x) = m + c \* f(x)`, where `h(x)` is the hash value, `m` is the modulus, `c` is a coefficient, and `f(x)` is the hash function.
- **Collision**: When two different input messages produce the same output hash value.
- **Birthday Problem**: A problem in probability theory that illustrates the concept of hash functions and collisions.

### Key Formulas and Definitions

- **Hash Function Formula**: `h(x) = m + c \* f(x)`, where `h(x)` is the hash value, `m` is the modulus, `c` is a coefficient, and `f(x)` is the hash function.
- **Collision Probability**: The probability that two different input messages produce the same output hash value.
- **Birthday Problem Formula**: `P(collision) = 1 - (1 - 1/n)^k`, where `P(collision)` is the probability of collision, `n` is the number of possible hash values, and `k` is the number of input messages.

### Key Theorems

- **Second Preimage Lemma**: Given a hash function and a message `x`, there exists at least one other message `y ≠ x` such that `h(x) = h(y)`.
- **Birthday Paradox**: The probability of at least two people sharing the same birthday in a group of `n` people is greater than 50% when `n` is around 23.

### Important Notes

- Hash functions are one-way, meaning it's computationally infeasible to recover the original input message from the hash value.
- Hash functions are non-invertible, meaning it's computationally infeasible to find two different input messages with the same hash value.
- The birthday problem is a classic example of the "birthday problem" in probability theory, which illustrates the concept of hash functions and collisions.
