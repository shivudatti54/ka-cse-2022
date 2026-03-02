# Chapman-Kolmogorov & Classification of States

## Introduction

The **Chapman-Kolmogorov equations** and **classification of states** are fundamental concepts in the study of **stochastic processes**, particularly **Markov chains**. These concepts are essential for modeling random phenomena in computing, such as algorithm analysis, network traffic, and queueing systems. This summary aligns with the Delhi University BSc (Hons) Computer Science NEP 2024 syllabus for the Probability for Computing course.

---

## Chapman-Kolmogorov Equations

The Chapman-Kolmogorov (C-K) equations provide a mathematical framework for understanding how probabilities evolve in stochastic processes over time.

- **Definition**: For a stochastic process with states *i, j, k* at times *m, r, n* (where *m < r < n*), the C-K equation states:
  
  **Pᵢⱼⁿ = Σₖ Pᵢᵣᵏ × Pₖᵣⁿ**
  
  This expresses the probability of transitioning from state *i* at time *m* to state *j* at time *n* as a sum over all possible intermediate states *k*.

- **Key Points**:
  - Fundamental to computing **n-step transition probabilities**
  - Enables calculation of probabilities across multiple time steps
  - Forms the theoretical basis for Markov chain analysis
  - Applies to both discrete and continuous-time stochastic processes

---

## Classification of States in Markov Chains

State classification helps analyze the long-term behavior of Markov chains.

### 1. Based on Recurrence

- **Transient States**: States that may never be visited again after leaving; expected number of visits is finite
- **Recurrent States**: States that will definitely be visited infinitely often; expected return time is finite

### 2. Based on Periodicity

- **Periodic State**: Can only be visited at regular intervals (period *d > 1*)
- **Aperiodic State**: Can be visited at irregular intervals (period *d = 1*)

### 3. Based on Accessibility

- **Absorbing State**: A state *i* where Pᵢᵢ = 1 (once entered, cannot leave)
- **Communicating States**: States *i* and *j* communicate (i ↔ j) if it's possible to reach *j* from *i* and vice versa

### 4. Ergodic States

- **Ergodic State**: A state that is both **positive recurrent** and **aperiodic**
- **Ergodic Chain**: A Markov chain where all states are ergodic; guarantees limiting distribution exists

---

## Important Theorems

- A finite Markov chain must have at least one recurrent state
- If states *i* and *j* communicate, they have the same period
- An irreducible, aperiodic, positive recurrent Markov chain has a unique stationary distribution

---

## Applications in Computing

- **PageRank algorithm** (Google)
- **Queueing theory** (computer networks)
- **Markov Decision Processes** (AI/ML)
- **Randomized algorithms** analysis

---

## Conclusion

The Chapman-Kolmogorov equations provide the mathematical foundation for analyzing multi-step transitions in stochastic processes, while state classification enables understanding the long-term behavior of Markov chains. These concepts are crucial for computer science applications involving randomness, including network modeling, algorithm design, and artificial intelligence. Mastery of these topics is essential for the Delhi University examination under the NEP 2024 framework.