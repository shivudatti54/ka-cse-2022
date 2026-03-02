# Tiger Hash

### Overview

Tiger Hash is a one-way password hashing algorithm designed to be slow and computationally expensive, making it more resistant to brute-force attacks.

### Definitions

- **Tiger Hash**: A one-way password hashing algorithm.
- **Hash function**: A mathematical function that takes input data of any size and produces a fixed-size output.

### Important Formulas and Theorems

- **Tiger Hash formula**: `H = hash((password || salt) || n)` where:
  - `H` is the output hash
  - `password` is the password to be hashed
  - `salt` is a random value added to the password for uniqueness
  - `n` is a constant value (e.g. 1)
- **Keccak-256**: A cryptographic hash function used in Tiger Hash.

### Key Points

- **Design goals**:
  - Slow and computationally expensive
  - Resistant to brute-force attacks
- **Security benefits**:
  - Prevents rainbow table attacks
  - Prevents pre-computed hash table attacks
- **Implementation**:
  - Typically used in combination with other security measures (e.g. salting, iteration count)
- **Advantages**:
  - High entropy output
  - Resistant to side-channel attacks
- **Disadvantages**:
  - Slow performance
  - May require additional memory and processing power
