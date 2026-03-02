# Stationary Distribution & Absorbing States in Markov Chains

## Introduction

In Module 2 of Mathematics for Computer Science, we explore how Markov Chains model systems that transition between states with given probabilities. Two fundamental concepts for understanding the long-term behavior of these systems are the **Stationary Distribution** and **Absorbing States**. These are crucial for applications like Google's PageRank algorithm (stationary distribution) and modeling user behavior in software (absorbing states).

## Core Concepts

### 1. Stationary Distribution (or Steady-State Distribution)

For a Markov chain with transition probability matrix `P`, a probability distribution `π` is called a **stationary distribution** if:
**π = πP**

This means that if the system is in distribution `π` at time `n`, it will remain in `π` at time `n+1` and all future steps. The system has reached a steady state.

**Key Condition:** A Markov chain must be **regular** (or ergodic) to have a unique stationary distribution. A chain is regular if some power of its transition matrix `P^k` has all **positive entries** (i.e., > 0). This means it's possible to get from any state to any other state in `k` steps.

**How to Find It:**
The stationary distribution `π = [π₁, π₂, ..., πₙ]` is found by solving the system of equations derived from:
1.  **π = πP**
2.  **π₁ + π₂ + ... + πₙ = 1** (The probabilities must sum to 1)

This is a system of linear equations, making it a perfect application of the linear algebra you've previously studied.

#### Example:
Consider a simple weather model with states {Sunny, Cloudy}. The transition matrix is: