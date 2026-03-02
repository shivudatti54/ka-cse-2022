# Multi-Arm Bandit Problem and RL Problem Types

## Overview

The Multi-Armed Bandit (MAB) problem is a foundational RL problem where an agent must choose between K arms with unknown reward probabilities, balancing exploration (learning) and exploitation (using best-known information).

## Key Points

- **MAB Definition**: K arms, unknown reward distributions, T rounds, goal to maximize cumulative reward

- **Explore-Exploit Tradeoff**: Core dilemma between trying new options (exploration) vs. using best-known option (exploitation)

- **Epsilon-Greedy**: With probability ε explore randomly, else exploit best-known arm. Simple but doesn't distinguish exploration quality.

- **UCB Formula**: UCB(a) = Q(a) + c√(ln(t)/N(a)). Exploration bonus decreases for well-explored arms. Theoretically optimal regret.

- **Thompson Sampling**: Bayesian approach. Sample from posterior distributions, select arm with highest sample. Adapts naturally to uncertainty.

## Important Concepts

- **Regret**: Difference between optimal arm performance and agent's performance

- **K-Arms**: Number of available actions/choices

- **Confidence Parameter (c)**: Controls exploration bonus in UCB, typically √2

## Notes

- Epsilon-Greedy: ε is exploration probability (typically 0.1)
- UCB: No parameters to tune, theoretical guarantees
- Thompson Sampling: Best practical performance in many settings
- MAB is a special case of RL with no state (single decision point)
