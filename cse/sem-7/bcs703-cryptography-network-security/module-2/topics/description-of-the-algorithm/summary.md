# Description of the Algorithm - Summary

## Key Definitions

- **Pseudorandom Number Generator (PRNG):** A deterministic algorithm that produces a sequence of numbers from an initial seed value, appearing statistically random to a computationally bounded observer.

- **Seed:** The initial random value used to initialize the internal state of a PRNG; must be drawn from a high-entropy source.

- **Internal State:** The memory maintained by a PRNG between output generations, updated through each iteration of the algorithm.

- **State Transition Function:** The mathematical function that computes the next internal state from the current state.

- **Output Function:** The function that derives the pseudorandom output from the current internal state.

- **Period:** The length of the output sequence before it begins to repeat; determined by the state space size and transition function properties.

## Important Formulas

- **State Transition:** S(i+1) = f(S(i)) — computes next state from current state
- **Output Generation:** O(i) = g(S(i)) — produces pseudorandom output from current state
- **Maximum Period:** For n-bit state, maximum period is 2^n
- **CTR Mode PRNG:** Output(i) = AES_ENC(Key, Counter + i)

## Key Points

1. A PRNG consists of three main elements: seed initialization, state transition function, and output function.

2. The internal state must be sufficiently large (minimum 128 bits, preferably 256 bits) to prevent exhaustive search attacks.

3. Cryptographically secure PRNGs require that computing the next state from current state is easy, but computing previous states is computationally infeasible.

4. The output function often uses cryptographic primitives (hash functions, block ciphers) to ensure output appears random.

5. Forward security ensures that compromising the current state does not reveal previously generated outputs.

6. Truncating the output (using fewer bits than the underlying primitive produces) increases security by making state recovery harder.

7. The period of a PRNG is bounded by the size of its internal state; larger states allow longer sequences before repetition.

## Common Mistakes

1. **Using LCGs for security purposes:** Linear Congruential Generators are predictable due to their linear structure and must never be used in cryptographic applications.

2. **Insufficient seed entropy:** Using predictable or low-entropy seeds (like system time) defeats the entire security of the PRNG.

3. **Confusing PRNG with TRNG:** Failing to recognize that PRNGs are deterministic and can be reproduced if the seed is known.

4. **Ignoring state management:** Not properly securing the internal state can lead to state compromise and prediction attacks.

5. **Underestimating state size requirements:** Using too-small state sizes (e.g., 32-bit) makes brute-force attacks on the state space trivial for modern computers.