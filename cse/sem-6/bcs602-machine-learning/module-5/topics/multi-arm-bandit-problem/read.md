# Multi-Arm Bandit Problem and Reinforcement Learning Problem Types

## Introduction

The Multi-Armed Bandit (MAB) problem is one of the most fundamental problems in reinforcement learning and decision theory. Imagine you walk into a casino with multiple slot machines (bandits), each with an unknown probability of giving you a reward. You have a limited number of pulls and must decide which machine to play at each step. This classic dilemma captures the essence of the explore-exploit tradeoff in sequential decision-making.

The name "bandit" comes from the colloquial term for a slot machine (one-armed bandit). When there are multiple arms (machines), it becomes a multi-armed bandit problem. This formulation appears in numerous real-world applications including clinical trials, adaptive routing, recommendation systems, and online advertising.

## Formal Definition of MAB

In the multi-armed bandit problem, we have:

- **K arms**: A set of actions or choices, typically denoted as {1, 2, ..., K}
- **Reward distribution**: Each arm i has an unknown expected reward μ_i (mean) and variance σ_i²
- **Time horizon**: T rounds where we must make decisions
- **Goal**: Maximize total expected reward over T rounds

At each time step t:

1. We select an arm a_t
2. We receive a reward r_t sampled from the distribution of arm a_t
3. We update our knowledge about that arm

The cumulative reward is R = Σ\_{t=1}^{T} r_t, and we aim to minimize **regret** – the difference between our performance and the optimal arm.

## The Explore-Exploit Tradeoff

This is the central challenge in bandit problems:

- **Exploration**: Trying different arms to learn their reward probabilities
- **Exploitation**: Choosing the arm that currently appears best based on observed rewards

If we only explore, we waste opportunities on suboptimal arms. If we only exploit, we might miss better options we haven't discovered. The challenge is balancing these competing objectives optimally.

## Epsilon-Greedy Algorithm

The simplest approach to balance exploration and exploitation:

- With probability ε (epsilon), choose a random arm (exploration)
- With probability 1-ε, choose the arm with highest estimated mean reward (exploitation)

**Algorithm**:

- Estimate Q(a) = average reward observed from arm a
- With probability ε: select random arm
- With probability 1-ε: select arm argmax Q(a)

**Parameters**: ε is typically set between 0.1 and 0.2, or can decay over time.

**Advantages**: Simple to implement, no parameter tuning needed beyond ε.

**Disadvantages**: Doesn't distinguish between well-explored and poorly-explored arms; still explores suboptimal arms with fixed ε.

## Upper Confidence Bound (UCB)

UCB adds an exploration bonus based on uncertainty:

**Formula**: UCB(a) = Q(a) + c × √(ln(t) / N(a))

Where:

- Q(a) = estimated mean reward of arm a
- N(a) = number of times arm a has been selected
- t = current time step
- c = confidence parameter (typically √2)

The second term (exploration bonus) decreases as we learn more about an arm but is larger for less-explored arms. UCB naturally balances exploration and exploitation without a fixed ε parameter.

**Advantages**: Theoretically optimal regret bounds, no parameter to tune.

**Disadvantages**: Assumes bounded rewards, may not perform well with continuous reward distributions.

## Thompson Sampling

A Bayesian approach that maintains probability distributions over arm rewards:

**Algorithm**:

1. For each arm, maintain a prior distribution (typically Beta for binary rewards)
2. Sample one value from each arm's distribution
3. Select the arm with highest sampled value
4. Update the distribution based on observed reward

For binary rewards with Beta prior:

- Arm i: Beta(α_i, β_i) where α = successes + 1, β = failures + 1
- Sample θ_i ~ Beta(α_i, β_i)
- Select arm with max θ_i

**Advantages**: Naturally handles uncertainty, works well in practice, adapts automatically to reward distributions.

**Disadvantages**: More computationally intensive, requires maintaining distributions.

## Reinforcement Learning Problem Types

The MAB problem is a special case of RL. Different problem types vary by information available:

### Multi-Armed Bandit (MAB)

- No state representation
- Single context-free decision point
- Only action matters, not history or environment state
- Example: Which ad to show user

### Contextual Bandit

- Observable context/state before each decision
- Context affects reward probabilities
- Example: Personalized recommendations based on user features

### Episodic RL

- Environment resets after each episode
- Clear episode boundaries
- Agent learns from complete trajectories
- Example: Game playing

### Continuous/Continuing RL

- No episode boundaries
- Continuous interaction with environment
- Example: Robot control in factory

### Partially Observable RL

- State not fully observable
- Must maintain belief state
- Example: Poker, navigation with limited sensors

## Comparison of Bandit Algorithms

| Algorithm         | Exploration         | Best For               | Complexity    |
| ----------------- | ------------------- | ---------------------- | ------------- |
| Epsilon-Greedy    | Fixed random        | Simple baselines       | O(1)          |
| UCB               | Deterministic bonus | Theoretical guarantees | O(K)          |
| Thompson Sampling | Probabilistic       | Practical applications | O(K) sampling |

## Real-World Applications

1. **Clinical Trials**: Testing new drugs while maximizing patient outcomes
2. **Online Advertising**: Selecting ads to maximize click-through rates
3. **Recommendation Systems**: Choosing items to recommend to users
4. **Resource Allocation**: Dynamic routing in networks
5. **A/B Testing**: Optimizing website features

## Conclusion

The Multi-Armed Bandit problem provides a foundational framework for understanding sequential decision-making under uncertainty. The three main algorithms – epsilon-greedy, UCB, and Thompson Sampling – represent different philosophies: simple randomization, confidence-based exploration, and Bayesian posterior sampling. Understanding these algorithms and their tradeoffs is essential for any reinforcement learning practitioner.
