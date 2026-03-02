# Purpose: Stationary Distribution of Regular Markov Chains and Absorbing States

## Why This Topic Matters for BCS301

This topic is one of the most important and most frequently examined parts of **Module 2: Probability and Statistics** in the BCS301 (Mathematics for Computer Science) syllabus. It represents the culmination of the Markov chain sequence that builds through stochastic matrices, transition probabilities, and regular matrices.

## Exam Relevance and Marks

- **Direct questions** on stationary distributions and absorbing states appear in nearly every BCS301 examination.
- Questions typically carry **8 to 10 marks** each, making this topic worth up to **20 marks** in a single paper.
- Common exam patterns include:
  - "Find the stationary distribution of the given transition matrix" (8 marks)
  - "Define absorbing state. Find the fundamental matrix and expected absorption time" (10 marks)
  - "Compare regular and absorbing Markov chains" (8 marks)
- The numerical problems (finding stationary distributions, computing fundamental matrices) are considered **high-scoring** because they follow a systematic procedure.

## What Students Must Be Able To Do

1. **Define** stationary distribution and write the equation pi \* P = pi with normalization.
2. **Solve** for stationary distributions of 2x2 and 3x3 transition matrices.
3. **Identify** absorbing states from a transition matrix (look for p_ii = 1).
4. **Write** the canonical form of an absorbing chain and compute the fundamental matrix N = (I - Q)^(-1).
5. **Calculate** expected absorption times (row sums of N) and absorption probabilities (B = N \* R).
6. **Distinguish** between regular and absorbing Markov chains and their long-term behaviors.

## Connection to Other Module 2 Topics

This topic directly depends on and extends:

- **Stochastic Matrices** -- understanding row-sum = 1 property
- **Regular Stochastic Matrices** -- the regularity condition guarantees uniqueness of stationary distributions
- **Higher Transition Probabilities** -- P^k convergence behavior
- **Probability Vectors** -- stationary distribution is a special probability vector

## Practical Significance for CSE Students

Understanding these concepts is essential for computer science applications including Google's PageRank algorithm, reinforcement learning, queueing theory in operating systems, network protocol analysis, and natural language processing with Hidden Markov Models.
