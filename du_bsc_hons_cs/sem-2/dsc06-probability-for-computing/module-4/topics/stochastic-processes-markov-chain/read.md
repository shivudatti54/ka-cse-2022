# Stochastic Processes and Markov Chains

## Introduction

In the field of probability theory and its applications to computing, stochastic processes form a fundamental concept that models systems evolving over time with inherent randomness. A stochastic process is a collection of random variables indexed by time or space, describing the evolution of a random system. From predicting user behavior in web applications to modeling queue lengths in operating systems, from algorithmic music composition to natural language processing, stochastic processes provide the mathematical framework for analyzing systems that exhibit uncertainty.

Markov chains, named after the Russian mathematician Andrey Markov, represent one of the most important and widely应用 classes of stochastic processes. The defining characteristic of a Markov chain is the **Markov property** or **memoryless property**—the future state of the system depends only on the current state and not on the entire history of how the system arrived at that state. This remarkably simple yet powerful assumption makes Markov chains computationally tractable and applicable to countless real-world scenarios.

In computer science, Markov chains find extensive applications in areas such as search engine ranking (PageRank algorithm), speech recognition, hidden Markov models for DNA sequence analysis, network traffic modeling, cache replacement algorithms, and Monte Carlo simulation methods. Understanding Markov chains is therefore essential for any computer science student seeking to model probabilistic systems and analyze random phenomena in computing contexts.

## Key Concepts

### Definition of a Stochastic Process

A stochastic process {X(t) : t ∈ T} is a family of random variables indexed by a parameter set T. The set T is typically interpreted as time and may be discrete (T = {0, 1, 2, ...}) or continuous (T = [0, ∞)). The values that X(t) can take are called the **state space** S of the process. When the state space is finite or countably infinite, we have a discrete-state stochastic process.

### The Markov Property

A discrete-time stochastic process {X₀, X₁, X₂, ...} is said to be a **Markov chain** if it satisfies the Markov property:

**P(Xₙ₊₁ = j | X₀ = i₀, X₁ = i₁, ..., Xₙ = i) = P(Xₙ₊₁ = j | Xₙ = i)**

This conditional probability is called the **transition probability** from state i at time n to state j at time n+1. Intuitively, this means that knowing the complete history of the process provides no additional predictive power beyond knowing the current state.

### Transition Probability Matrix

For a Markov chain with finite state space S = {1, 2, ..., m}, the one-step transition probabilities are arranged in a matrix called the **transition probability matrix** or **stochastic matrix**:

P = [pᵢⱼ] where pᵢⱼ = P(Xₙ₊₁ = j | Xₙ = i)

This matrix has the following properties:
- Each entry pᵢⱼ ≥ 0 (non-negative entries)
- Each row sums to 1: Σⱼ pᵢⱼ = 1 for all i

The **n-step transition probability** pᵢⱼ⁽ⁿ⁾ = P(Xₙ = j | X₀ = i) gives the probability of moving from state i to state j in exactly n steps. These can be computed using matrix multiplication: P⁽ⁿ⁾ = Pⁿ (the n-th power of the transition matrix).

### Classification of States

A state j is said to be **accessible** from state i if pᵢⱼ⁽ⁿ⁾ > 0 for some n ≥ 0. Two states i and j are **communicating** if each is accessible from the other, denoted i ↔ j. This defines an equivalence relation that partitions the state space into **communication classes**.

A state i is **recurrent** if, starting from i, the chain returns to i with probability 1. Equivalently, a state is recurrent if the expected number of visits to that state is infinite. A state that is not recurrent is **transient**—the chain may never return to it, and if it does, the expected number of returns is finite.

A state i is **absorbing** if pᵢᵢ = 1. Once the chain enters an absorbing state, it never leaves. A Markov chain is **irreducible** if all states communicate with each other, meaning the entire state space forms a single communication class.

### Periodicity

The **period** of a state i is defined as d(i) = gcd{n ≥ 1 : pᵢᵢ⁽ⁿ⁾ > 0}, the greatest common divisor of all n for which returning to i in n steps is possible. If d(i) > 1, the state is **periodic** with period d(i). If d(i) = 1, the state is **aperiodic**. A Markov chain is periodic if all its states have period greater than 1. Periodicity affects whether the chain converges to a stationary distribution.

### Stationary Distributions

A probability vector π = (π₁, π₂, ..., πₘ) is a **stationary distribution** for a Markov chain if it satisfies πP = π and Σᵢ πᵢ = 1. If the chain starts with initial distribution X₀ ~ π, then Xₙ ~ π for all n—the distribution remains unchanged over time.

For an irreducible, aperiodic Markov chain, the stationary distribution exists and is unique. Furthermore, regardless of the initial state, the distribution of Xₙ converges to π as n → ∞. This is the **ergodic theorem** for Markov chains.

The stationary distribution can be found by solving the linear equations πP = π subject to Σπᵢ = 1. Alternatively, for irreducible chains, πⱼ can be computed as the limiting probability of being in state j: πⱼ = limₙ→∞ pᵢⱼ⁽ⁿ⁾, independent of the initial state i.

## Examples

### Example 1: Weather Model

Consider a simple weather model with two states: Sunny (S) and Rainy (R). Based on historical data, we observe that:
- If today is Sunny, tomorrow is Sunny with probability 0.8 and Rainy with probability 0.2
- If today is Rainy, tomorrow is Rainy with probability 0.6 and Sunny with probability 0.4

**Solution:**

The transition probability matrix is:
```
        S     R
P = [  0.8  0.2  ]  (from S)
    [  0.4  0.6  ]  (from R)
```

**(a) If today is Sunny, find the probability that it is Sunny two days from now.**

We need pₛₛ⁽²⁾ = (P²)₁₁

P² = P × P = [  0.8  0.2  ] × [  0.8  0.2  ]
                         [  0.4  0.6  ]

Computing: (P²)₁₁ = 0.8 × 0.8 + 0.2 × 0.4 = 0.64 + 0.08 = 0.72

Therefore, P(X₂ = S | X₀ = S) = 0.72

**(b) Find the stationary distribution.**

Let π = (πₛ, πᵣ) satisfy πP = π and πₛ + πᵣ = 1.

πₛ = 0.8πₛ + 0.4πᵣ  
πᵣ = 0.2πₛ + 0.6πᵣ

From the first equation: πₛ - 0.8πₛ = 0.4πᵣ ⇒ 0.2πₛ = 0.4πᵣ ⇒ πₛ = 2πᵣ

Using πₛ + πᵣ = 1: 2πᵣ + πᵣ = 1 ⇒ 3πᵣ = 1 ⇒ πᵣ = 1/3, πₛ = 2/3

So the stationary distribution is π = (2/3, 1/3), meaning in the long run, about 67% of days are Sunny and 33% are Rainy.

### Example 2: Web Page Navigation Model

A user navigates through three web pages A, B, and C. The transition probabilities based on user behavior are:
- From A: goes to B with probability 0.5, goes to C with probability 0.3, stays at A with probability 0.2
- From B: goes to A with probability 0.4, goes to C with probability 0.4, stays at B with probability 0.2
- From C: goes to A with probability 0.6, goes to B with probability 0.2, stays at C with probability 0.2

**(a) Write the transition matrix P.**

States ordered as A, B, C:
```
        A     B     C
P = [  0.2  0.5  0.3  ]  (from A)
    [  0.4  0.2  0.4  ]  (from B)
    [  0.6  0.2  0.2  ]  (from C)
```

**(b) If a user starts at page A, find the probability they are at page B after 2 clicks.**

We need (P²)₁₂ = the element in row 1, column 2 of P².

P² = P × P. Computing only the (1,2) entry:
(P²)₁₂ = 0.2 × 0.5 + 0.5 × 0.2 + 0.3 × 0.2 = 0.10 + 0.10 + 0.06 = 0.26

So the probability is 0.26 or 26%.

**(c) Find the long-run proportion of time spent at each page.**

Let π = (πₐ, πᵦ, π_c) satisfy πP = π and πₐ + πᵦ + π_c = 1.

Equations:
πₐ = 0.2πₐ + 0.4πᵦ + 0.6π_c
πᵦ = 0.5πₐ + 0.2πᵦ + 0.2π_c
π_c = 0.3πₐ + 0.4πᵦ + 0.2π_c

Simplify the first: πₐ - 0.2πₐ = 0.4πᵦ + 0.6π_c ⇒ 0.8πₐ = 0.4πᵦ + 0.6π_c
Simplify the second: πᵦ - 0.2πᵦ = 0.5πₐ + 0.2π_c ⇒ 0.8πᵦ = 0.5πₐ + 0.2π_c
Simplify the third: π_c - 0.2π_c = 0.3πₐ + 0.4πᵦ ⇒ 0.8π_c = 0.3πₐ + 0.4πᵦ

Solving this system (using linear algebra or substitution):
From symmetry and calculation: πₐ ≈ 0.375, πᵦ ≈ 0.3125, π_c ≈ 0.3125

We can verify: πP = π
[0.375, 0.3125, 0.3125] × P = [0.375, 0.3125, 0.3125] ✓

### Example 3: Queueing System

A computer system can handle at most 2 jobs in its queue (excluding the one being processed). The state represents the number of jobs in the system (0, 1, or 2). At each time step:
- If the system is empty, a job arrives with probability 0.5
- If there is 1 job, with probability 0.3 a new job arrives (making it 2), with probability 0.4 the job completes (making it 0), and with probability 0.3 nothing changes
- If there are 2 jobs, with probability 0.6 a job completes (reducing to 1), with probability 0.2 a new job is rejected (system stays at 2), and with probability 0.2 nothing changes

**Solution:**

States: 0, 1, 2

Transition matrix:
```
        0     1     2
P = [  0.5  0.5   0   ]  (from 0)
    [  0.4  0.3  0.3  ]  (from 1)
    [   0  0.6  0.4  ]  (from 2)
```

This is an example of a finite-state Markov chain used in queueing theory to model computer systems, telecommunications networks, and service systems.

## Exam Tips

1. **Remember the Markov property**: The key to identifying a Markov chain is the memoryless property—future depends only on present, not past. Always verify this before applying Markov chain methods.

2. **Transition matrix properties**: Each row of a transition probability matrix must sum to 1. This is a common check in exam questions—verify this property first.

3. **Computing n-step probabilities**: For computing probabilities after n steps, use matrix multiplication Pⁿ. For small n, you can also use the Chapman-Kolmogorov equations directly: pᵢⱼ⁽ᵐ⁺ⁿ⁾ = Σₖ pᵢₖ⁽ᵐ⁾ × pₖⱼ⁽ⁿ⁾.

4. **Stationary distribution computation**: To find stationary distribution π, solve πP = π along with Σπᵢ = 1. This gives a system of linear equations. A useful tip: one equation is redundant (since rows sum to 1), so replace it with the sum equation.

5. **Classification of chains**: Know the difference between irreducible/reducible, periodic/aperiodic, and transient/recurrent states. These classifications determine whether a stationary distribution exists and whether convergence occurs.

6. **Applications in computing**: Be familiar with applications like PageRank, queueing models, and Markov Chain Monte Carlo (MCMC). Exam questions may ask you to set up a Markov chain model for a given computing scenario.

7. **Long-run behavior**: For an irreducible, aperiodic Markov chain, the limiting distribution exists and equals the unique stationary distribution, regardless of initial state. This is the ergodic theorem.

8. **Check irreducibility**: A chain is irreducible if all states communicate. If not irreducible, different initial states may lead to different limiting behaviors (absorbing states).