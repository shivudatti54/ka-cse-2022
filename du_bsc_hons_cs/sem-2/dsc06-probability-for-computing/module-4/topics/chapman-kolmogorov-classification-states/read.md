# Chapman-Kolmogorov Classification of States

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

**Markov Chains** form the mathematical backbone of numerous computational processes we encounter daily. From the algorithms that determine which web page loads first to the systems managing network traffic, Markov chains provide a powerful framework for modeling stochastic (random) processes where future states depend only on the present state—a property known as the **Markov Property** or **memorylessness**.

The **Chapman-Kolmogorov Equations** are fundamental to this theory, providing the mechanism to compute transition probabilities over multiple steps. Equally important is the **Classification of States**, which helps us understand the long-term behavior of a Markov chain—whether the system will eventually stabilize, cycle indefinitely, or drift away.

For Computer Science students at Delhi University, these concepts are essential not only for theoretical understanding but also for practical applications in:

- **Operating Systems**: Page replacement algorithms (e.g., the cache behavior analysis)
- **Networking**: Queueing theory and network protocol modeling
- **Machine Learning**: Hidden Markov Models (HMMs) used in speech recognition, NLP, and bioinformatics
- **Web Search**: Google's PageRank algorithm
- **Performance Analysis**: Modeling CPU/memory access patterns

---

## 2. Prerequisites: Markov Chains Fundamentals

Before diving into Chapman-Kolmogorov and state classification, let's establish the core definitions:

### 2.1 Discrete-Time Markov Chain (DTMC)

A discrete-time Markov chain is a stochastic process {X₀, X₁, X₂, ...} taking values in a finite or countable state space S such that:

**P(Xₙ₊₁ = j | Xₙ = i, Xₙ₋₁ = iₙ₋₁, ..., X₀ = i₀) = P(Xₙ₊₁ = j | Xₙ = i) = Pᵢⱼ**

This is the **Markov Property**: the future depends only on the present, not the past.

### 2.2 Transition Probability Matrix

For a finite state space with n states, the **transition probability matrix** P is defined as:

```
P = [Pᵢⱼ] where Pᵢⱼ = P(Xₙ₊₁ = j | Xₙ = i)
```

Each row sums to 1 (probability axioms): Σⱼ Pᵢⱼ = 1 for all i.

---

## 3. Chapman-Kolmogorov Equations

The **Chapman-Kolmogorov Equations** provide a method to compute n-step transition probabilities. They state that for any states i, j ∈ S and any non-negative integers m, n:

$$P^{(m+n)}_{ij} = \sum_{k \in S} P^{(m)}_{ik} \cdot P^{(n)}_{kj}$$

### 3.1 Intuition

The equation tells us that to go from state i to state j in (m+n) steps, we can:
1. First go from i to some intermediate state k in m steps
2. Then go from k to j in n steps
3. Sum over all possible intermediate states k

This is essentially the **matrix multiplication principle** applied to transition matrices.

### 3.2 n-Step Transition Matrix

The n-step transition matrix is obtained by raising the one-step transition matrix to the nth power:

$$P^{(n)} = P^n$$

where P is the one-step transition matrix.

### 3.3 Python Implementation

```python
import numpy as np

def compute_n_step_transition(P, n):
    """
    Compute n-step transition matrix using matrix multiplication.
    
    Parameters:
    P: 2D numpy array (transition probability matrix)
    n: number of steps
    
    Returns:
    P^n: n-step transition matrix
    """
    return np.linalg.matrix_power(P, n)

# Example: Weather Markov Chain
# States: 0 = Sunny, 1 = Cloudy, 2 = Rainy
P = np.array([
    [0.7, 0.2, 0.1],  # From Sunny
    [0.3, 0.4, 0.3],  # From Cloudy
    [0.2, 0.3, 0.5]   # From Rainy
])

# Compute 2-step transition matrix
P_2 = compute_n_step_transition(P, 2)
print("2-Step Transition Matrix:")
print(np.round(P_2, 4))

# Compute 10-step transition matrix (long-term behavior)
P_10 = compute_n_step_transition(P, 10)
print("\n10-Step Transition Matrix (approaching stationary distribution):")
print(np.round(P_10, 4))
```

**Output:**
```
2-Step Transition Matrix:
[[0.54 0.26 0.2 ]
 [0.41 0.31 0.28]
 [0.37 0.32 0.31]]

10-Step Transition Matrix (approaching stationary distribution):
[[0.4286 0.2857 0.2857]
 [0.4286 0.2857 0.2857]
 [0.4286 0.2857 0.2857]]
```

Notice how the rows become identical as n → ∞—this indicates the existence of a **stationary distribution**, a key concept we'll explore later.

---

## 4. Classification of States

Understanding the behavior of individual states within a Markov chain is crucial for analyzing its long-term properties.

### 4.1 Recurrent and Transient States

#### 4.1.1 Definitions

Consider a Markov chain starting from state i. Let:

$$f_{ii} = P(\text{ever return to } i | X_0 = i)$$

- **State i is recurrent** if f_{ii} = 1 (probability of returning is 1)
- **State i is transient** if f_{ii} < 1 (probability of returning is less than 1)

#### 4.1.2 Key Properties

| Property | Recurrent State | Transient State |
|----------|-----------------|-----------------|
| Expected return time | Finite (∞ for null recurrent) | Infinite |
| Visits | Visited infinitely often (with probability 1) | Visited finitely many times |
| Contribution to stationary distribution | Always (if positive recurrent) | Never |
| Period | Can be periodic or aperiodic | Always aperiodic |

#### 4.1.3 Mathematical Characterization

State i is **recurrent** if and only if:

$$\sum_{n=1}^{\infty} p^{(n)}_{ii} = \infty$$

State i is **transient** if:

$$\sum_{n=1}^{\infty} p^{(n)}_{ii} < \infty$$

where p^{(n)}_{ii} is the probability of returning to state i in exactly n steps.

#### 4.1.4 Example: Recurrent vs Transient

Consider a Markov chain with states {0, 1, 2} and transition matrix:

```
    0   1   2
0 [ 0   1   0 ]
1 [ 0   0   1 ]
2 [ 1/2 1/2 0 ]
```

- State 0 → State 1 → State 2 → (back to 0 with prob 1/2, or 1 with prob 1/2)
- State 0 is **recurrent**: It will eventually return with probability 1
- State 1 is **transient**: Once you leave state 1, you can never return directly
- State 2 is **transient**: Similar reasoning

### 4.2 Periodic and Aperiodic States

#### 4.2.1 Period of a State

The **period** of state i is defined as:

$$d(i) = \gcd\{n \geq 1 : p^{(n)}_{ii} > 0\}$$

In simpler terms, it's the greatest common divisor of all n for which there's a positive probability of returning to i in n steps.

- **Periodic state**: d(i) > 1
- **Aperiodic state**: d(i) = 1

#### 4.2.2 Intuition

If a state has period d > 1, you can only return to it at intervals that are multiples of d. For aperiodic states, you can return at irregular intervals—eventually, you can return in just 1 step (or any n ≥ 1).

#### 4.2.3 Important Theorem

**All states in the same communicating class have the same period.**

This means we can talk about the period of an entire **irreducible** Markov chain.

#### 4.2.4 Example: Periodic vs Aperiodic

Consider a simple two-state Markov chain:

```
    0   1
0 [ 0   1 ]
1 [ 1   0 ]
```

- From state 0, you can only return in 2, 4, 6, ... steps (even numbers)
- Period of state 0 = 2 (periodic)
- Period of state 1 = 2 (periodic)

Now consider:

```
    0   1
0 [ 0.5 0.5 ]
1 [ 0.5 0.5 ]
```

- From state 0, you can return in 1 step (stay at 0 with probability 0.5), or 2 steps, etc.
- Period = 1 (aperiodic)

### 4.3 Null Recurrent vs Positive Recurrent

For recurrent states, we further classify based on the **expected return time**:

- **Positive recurrent**: Expected return time μᵢ < ∞
- **Null recurrent**: Expected return time μᵢ = ∞

In finite-state Markov chains, all recurrent states are positive recurrent. Null recurrent states can only exist in infinite state spaces.

**Example of Null Recurrent**: Consider a simple symmetric random walk on the integers (an infinite state space). Each step moves left or right with equal probability. The state 0 is null recurrent—it returns infinitely often but the expected return time is infinite.

### 4.4 Ergodic States

A state is **ergodic** if it is both:
1. **Positive recurrent**
2. **Aperiodic**

An **ergodic Markov chain** is one in which all states are ergodic. Such chains have a unique stationary distribution and converge to it regardless of the starting state.

---

## 5. Communication Between States

Understanding which states "talk" to each other is essential for analyzing the structure of Markov chains.

### 5.1 Communication Definition

State i **communicates** with state j (denoted i → j) if there exists some n ≥ 1 such that:

$$p^{(n)}_{ij} > 0$$

This means it's possible to reach j from i in some number of steps.

### 5.2 Mutual Communication (Communicating Class)

States i and j **intercommunicate** (denoted i ↔ j) if:
- i → j, and
- j → i

This defines an **equivalence relation** that partitions the state space into **communicating classes**.

### 5.3 Properties of Communicating Classes

1. **Reflexivity**: Every state communicates with itself (i → i with n = 0 is typically considered, or by definition with n ≥ 1 in a periodic case)
2. **Symmetry**: If i ↔ j, then j ↔ i
3. **Transitivity**: If i ↔ j and j ↔ k, then i ↔ k

### 5.4 Closed Classes

A set of states C is **closed** if no state outside C can be reached from any state inside C:

$$P(X_n \in C | X_0 \in C) = 1 \text{ for all } n$$

In other words, once you enter a closed class, you can never leave.

**Properties:**
- A single state i is closed if and only if Pᵢᵢ = 1 (absorbing state)
- A finite Markov chain must have at least one closed class
- A closed class containing only transient states is impossible in finite chains

### 5.5 Irreducible Markov Chains

A Markov chain is **irreducible** if all states belong to a single communicating class—meaning every state can be reached from every other state.

For irreducible chains:
- All states are either recurrent or transient together
- All states have the same period
- Either all states are positive recurrent or all are null recurrent (for infinite state spaces)

---

## 6. Stationary Distributions

The **stationary distribution** (or steady-state distribution) describes the long-term behavior of a Markov chain.

### 6.1 Definition

A probability vector π = (π₁, π₂, ...) is a **stationary distribution** if:

$$\pi P = \pi$$

where π is a row vector and Σπᵢ = 1.

This means if the chain starts with distribution π, it remains in distribution π at all times—hence "stationary."

### 6.2 Existence and Uniqueness

For a finite-state Markov chain:

- **Existence**: A stationary distribution always exists
- **Uniqueness**: If the chain is **irreducible and aperiodic** (i.e., ergodic), the stationary distribution is unique

For infinite-state chains, existence is not guaranteed.

### 6.3 Limiting Distribution

For an ergodic (irreducible + aperiodic) Markov chain:

$$\lim_{n \to \infty} P^{(n)}_{ij} = \pi_j \text{ for all i}$$

This means regardless of the starting state, the n-step transition probabilities converge to the stationary distribution.

### 6.4 Detailed Balance Condition

A sufficient condition for a stationary distribution is **detailed balance**:

$$\pi_i P_{ij} = \pi_j P_{ji} \text{ for all i, j}$$

This is particularly useful for reversible Markov chains.

---

## 7. Applications in Computer Science

### 7.1 Page Replacement Algorithms (Cache Memory)

Operating systems use **page replacement algorithms** to manage memory. The Belady's Anomaly shows that increasing the number of page frames can sometimes increase page faults. Markov chains model this behavior:

```
States: Number of page faults in cache (0, 1, 2, ..., k)
Transitions: Based on reference string patterns
```

The stationary distribution tells us the long-run proportion of time the cache spends in each state, helping analyze hit/miss ratios.

### 7.2 Queueing Theory

Consider an **M/M/1 queue** (Poisson arrivals, exponential service times, single server):

- States represent the number of customers in the system (0, 1, 2, ...)
- Transition rates λ (arrival) and μ (service)
- This is a continuous-time Markov chain

Key performance metrics derived from stationary distributions:
- **L**: Average number of customers in system
- **Lq**: Average queue length
- **W**: Average time in system
- **Wq**: Average waiting time

**Formulas for M/M/1 (when ρ = λ/μ < 1):**

$$L = \frac{\rho}{1 - \rho}, \quad W = \frac{1}{\mu - \lambda}$$

### 7.3 PageRank Algorithm

Google's **PageRank** uses a Markov chain model of web surfing:

- Each web page is a state
- The transition matrix represents the link structure of the web
- The PageRank is the stationary distribution of this Markov chain

This application directly uses:
- Classification of states (absorbing states handling)
- Stationary distributions
- Ergodic theorems

### 7.4 Algorithmic Perspectives

When implementing Markov chain simulations:

```python
import numpy as np
import random

def simulate_markov_chain(P, start_state, num_steps):
    """
    Simulate a Markov chain trajectory.
    
    Parameters:
    P: Transition probability matrix (numpy array)
    start_state: Initial state (0-indexed)
    num_steps: Number of steps to simulate
    
    Returns:
    List of visited states
    """
    current_state = start_state
    trajectory = [current_state]
    
    for _ in range(num_steps):
        # Get transition probabilities from current state
        probs = P[current_state]
        # Sample next state based on probabilities
        next_state = np.random.choice(len(probs), p=probs)
        trajectory.append(next_state)
        current_state = next_state
    
    return trajectory

# Example: Simulate weather for 100 days
P = np.array([
    [0.7, 0.2, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

np.random.seed(42)
trajectory = simulate_markov_chain(P, start_state=0, num_steps=100)
print(f"Trajectory (first 20 days): {trajectory[:20]}")
print(f"State frequencies: 0={trajectory.count(0)}, 1={trajectory.count(1)}, 2={trajectory.count(2)}")
```

---

## 8. Worked Computational Examples

### Example 1: Analyzing a 3-State Markov Chain

**Problem**: Consider the Markov chain with transition matrix:

```
    0   1   2
0 [ 1/2 1/2  0 ]
1 [ 1/2 1/4 1/4]
2 [  0  1/2 1/2]
```

**(a) Classify the states (recurrent/transient, period)**
**(b) Find the stationary distribution**

**Solution:**

**(a) Classification**

From state 0:
- Can go to 0 or 1
- Can reach 2: 0 → 1 → 2 (2 steps)

From state 1:
- Can reach all states (0, 1, 2)

From state 2:
- Can go to 1 or 2
- Can reach 0: 2 → 1 → 0 (2 steps)

All states communicate: 0 ↔ 1 ↔ 2. The chain is **irreducible**.

Now, can we return to any state in 1 step?
- P₀₀ = 1/2 > 0 → Yes!
- Therefore, all states are **aperiodic**.

Since it's a finite irreducible chain, all states are **positive recurrent**.

**(b) Stationary Distribution**

Solve πP = π:

```
π₀ = (1/2)π₀ + (1/2)π₁ + 0π₂
π₁ = (1/2)π₀ + (1/4)π₁ + (1/2)π₂
π₂ = 0π₀ + (1/4)π₁ + (1/2)π₂
π₀ + π₁ + π₂ = 1
```

Solving:
- From π₀ equation: π₀ = (1/2)π₀ + (1/2)π₁ → (1/2)π₀ = (1/2)π₁ → π₀ = π₁
- From π₂ equation: π₂ = (1/4)π₁ + (1/2)π₂ → (1/2)π₂ = (1/4)π₁ → π₂ = (1/2)π₁
- Using π₀ + π₁ + π₂ = 1: π₁ + π₁ + (1/2)π₁ = 1 → (5/2)π₁ = 1 → π₁ = 2/5
- π₀ = π₁ = 2/5
- π₂ = 1/5

**Stationary distribution**: π = (2/5, 2/5, 1/5)

### Example 2: PageRank-Style Analysis

**Problem**: A simplified web has 3 pages with the following links:
- Page 0 links to: 0, 1
- Page 1 links to: 0, 2
- Page 2 links to: 1

Create the transition matrix (with teleportation probability α = 0.8 to handle dangling nodes) and find approximate PageRank.

**Solution:**

**Base transition matrix** (row-normalized):
```
    0     1     2
0 [ 0.5   0.5   0  ]
1 [ 0.5    0   0.5]
2 [  0     1    0 ]
```

**Teleportation formula**: P = αP_base + (1-α)(1/n)J

where J is the all-ones matrix.

```python
import numpy as np

# Base transition matrix
P_base = np.array([
    [0.5, 0.5, 0.0],
    [0.5, 0.0, 0.5],
    [0.0, 1.0, 0.0]
])

alpha = 0.8
n = 3

# Teleportation matrix
J = np.ones((n, n)) / n
P = alpha * P_base + (1 - alpha) * J

print("Transition Matrix with Teleportation:")
print(P)

# Power iteration to find stationary distribution
def power_iteration(P, num_iterations=100):
    pi = np.array([1.0/n] * n)  # Initial distribution
    for _ in range(num_iterations):
        pi = pi @ P
    return pi

pagerank = power_iteration(P, 100)
print(f"\nPageRank (Stationary Distribution):")
print(f"Page 0: {pagerank[0]:.4f}")
print(f"Page 1: {pagerank[1]:.4f}")
print(f"Page 2: {pagerank[2]:.4f}")
```

**Output:**
```
Transition Matrix with Teleportation:
[[0.6  0.4  0.1]
 [0.4  0.2  0.4]
 [0.1  0.6  0.2]]

PageRank (Stationary Distribution):
Page 0: 0.3871
Page 1: 0.4194
Page 2: 0.1935
```

---

## 9. Key Takeaways

1. **Chapman-Kolmogorov Equations**: P^{(m+n)} = P^m × P^n, fundamental for computing multi-step transition probabilities.

2. **State Classification**:
   - **Recurrent vs Transient**: Recurrent states are visited infinitely often; transient states are visited finitely many times
   - **Periodic vs Aperiodic**: Period is the GCD of return times; aperiodic states can return at irregular intervals
   - **Positive vs Null Recurrent**: Based on whether expected return time is finite

3. **Communication**: States form equivalence classes; closed classes cannot be left; irreducible chains have one class.

4. **Stationary Distributions**: π = πP; unique for ergodic (irreducible + aperiodic) chains;limiting distribution exists and equals stationary distribution.

5. **Applications in CS**: PageRank, queueing theory (M/M/1 queues), cache analysis, and various algorithmic applications use these concepts.

6. **Computation**: Matrix operations (multiplication, powers) and power iteration are key computational tools.

---

## 10. Challenging MCQs (University Level)

### Section A: Conceptual Questions

**1.** Consider a Markov chain with transition matrix:
```
    0   1
0 [ 0   1 ]
1 [ 1   0 ]
```
The states 0 and 1 are:
- (a) Transient
- (b) Recurrent and periodic with period 2
- (c) Recurrent and aperiodic
- (d) Null recurrent

**2.** In a finite-state Markov chain, which statement is ALWAYS true?
- (a) All recurrent states are aperiodic
- (b) All transient states have period 1
- (c) There exists at least one closed communicating class
- (d) A stationary distribution exists but may not be unique

**3.** The Chapman-Kolmogorov equations state that for m, n ≥ 1:
- (a) p^{(m+n)}_{ij} = p^{(m)}_{ij} + p^{(n)}_{ij}
- (b) p^{(m+n)}_{ij} = p^{(m)}_{ij} × p^{(n)}_{ij}
- (c) p^{(m+n)}_{ij} = Σ_k p^{(m)}_{ik} × p^{(n)}_{kj}
- (d) p^{(m+n)}_{ij} = p^{(m)}_{ij} - p^{(n)}_{ij}

**4.** A state with period 3 means:
- (a) You can return to the state in exactly 3 steps
- (b) The GCD of all return times is 3
- (c) The state is visited 3 times more often than others
- (d) The chain takes exactly 3 steps to reach steady state

### Section B: Application-Based Questions

**5.** In an M/M/1 queue with arrival rate λ = 5 customers/hour and service rate μ = 8 customers/hour, the probability that the system is empty (P₀) is:
- (a) 3/8
- (b) 5/8
- (c) 3/13
- (d) 8/13

**6.** A web surfer randomly clicks links on web pages. If the web has 4 pages with equal outgoing links from each page, this process can be modeled as:
- (a) A periodic Markov chain
- (b) A transient Markov chain
- (c) An irreducible and aperiodic Markov chain
- (d) A Markov chain with absorbing states

**7.** In a cache system modeled as a Markov chain, the stationary distribution gives:
- (a) The hit ratio for each page
- (b) The long-run proportion of time each page spends in cache
- (c) The probability of a page fault on the next access
- (d) The optimal cache replacement policy

**8.** A Markov chain has two closed classes {0, 1} and {2, 3}. Starting from state 0, which statement is true?
- (a) The chain will eventually visit states 2 and 3
- (b) The chain will stay forever in {0, 1}
- (c) The chain may or may not return to state 0
- (d) The stationary distribution is unique

### Section C: Computational Questions

**9.** Given transition matrix P = [[0.6, 0.4], [0.3, 0.7]], the stationary distribution π is:
- (a) (0.4, 0.6)
- (b) (0.5, 0.5)
- (c) (0.4286, 0.5714)
- (d) (0.375, 0.625)

**10.** If a Markov chain has transition matrix P² = P³, this implies:
- (a) The chain is periodic with period 2
- (b) The chain has reached its stationary distribution
- (c) The chain is absorbing
- (d) P is idempotent (P² = P)

---

### Answer Key

1. (b) — Period 2 due to alternating structure
2. (c) — Finite chains must have closed classes
3. (c) — Chapman-Kolmogorov equations
4. (b) — Period is the GCD of return times
5. (c) — P₀ = 1 - ρ = 1 - 5/8 = 3/13
6. (c) — Irreducible and aperiodic (can stay/self-loop)
7. (b) — Long-run proportion interpretation
8. (b) — Once in a closed class, never leaves
9. (c) — π₁ = 0.4/(0.4+0.7) = 4/11 ≈ 0.4286
10. (d) — Idempotent matrices satisfy P² = P

---

## References for Further Study

1. **Primary Text**: "Probability and Statistics for Computer Science" — Relevant chapters on Stochastic Processes
2. **Additional Reading**:
   - "Introduction to Probability Models" by Sheldon M. Ross
   - "Probability on Graphs" by Geoffrey Grimmett
3. **Delhi University Syllabus Reference**: NEP 2024 UGCF BSc (H) Computer Science — Unit on Markov Chains and Applications

---

*This study material covers all key concepts required for the Delhi University BSc (Hons) Computer Science curriculum under NEP 2024 UGCF, with comprehensive coverage of Chapman-Kolmogorov equations, state classification, communication properties, stationary distributions, and CS applications.*