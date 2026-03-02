# Policy Gradient Methods

## Introduction
Policy Gradient Methods are a class of reinforcement learning algorithms that optimize a parameterized policy directly by gradient ascent. Unlike value-based methods that learn value functions and derive policies indirectly, these methods are particularly effective in high-dimensional/continuous action spaces (e.g., robotic control, AlphaGo). Their importance stems from:

1. **Theoretical Foundations**: Direct policy optimization avoids the need for greedy action selection, enabling better convergence properties.
2. **Flexibility**: Can handle stochastic policies and non-Markovian environments.
3. **Modern Applications**: Foundation for state-of-the-art algorithms like PPO, TRPO, and SAC used in complex tasks like autonomous driving and game AI.

Recent research focuses on variance reduction techniques (e.g., advantage estimation) and trust region optimization to improve sample efficiency and stability.

## Key Concepts
1. **Policy Network**: Parameterized function π(a|s;θ) (typically neural network) outputting action probabilities.
2. **Objective Function**: Expected return J(θ) = 𝔼_π[Σγ^t r_t], optimized via gradient ascent.
3. **Policy Gradient Theorem**: ∇J(θ) = 𝔼_π[∇logπ(a|s;θ) * Q^π(s,a)] (foundation for all PG methods).
4. **REINFORCE Algorithm**: Monte Carlo approach using full episode returns as unbiased but high-variance gradient estimates.
5. **Actor-Critic Methods**: Combines policy gradient with value function approximation (critic) to reduce variance.
6. **Advantage Function**: A(s,a) = Q(s,a) - V(s) used in A2C/A3C algorithms.
7. **Proximal Policy Optimization (PPO)**: State-of-the-art method with clipped objective for stable updates.

## Examples

**Example 1: REINFORCE on CartPole**
```python
# Pseudocode
Initialize policy network π_θ
for episode in 1..N:
    Generate trajectory (s0,a0,r0,...sT) using π_θ
    Compute returns G_t = Σ_{k=t}^T γ^{k-t} r_k
    Compute gradient: ∇J(θ) = Σ G_t ∇logπ(a_t|s_t;θ)
    θ ← θ + α∇J(θ)
```

**Example 2: Actor-Critic with Advantage Estimation**
In a 4x4 GridWorld:
1. Actor (policy) proposes action probabilities
2. Critic (value network) estimates V(s)
3. Compute advantage A(s,a) = r + γV(s') - V(s)
4. Update policy: θ ← θ + αA(s,a)∇logπ(a|s;θ)
5. Update critic via TD error: ϕ ← ϕ - β∇(A(s,a))²

**Example 3: PPO-Clip Objective**
For each batch:
```
L(θ) = 𝔼[min(
    π_θ(a|s)/π_θ_old(a|s) * A(s,a),
    clip(π_θ/π_θ_old, 1-ε, 1+ε) * A(s,a)
)]
```
Prevents large policy updates (ε=0.2 typically) while maintaining training stability.

## Exam Tips
1. **Derivation Focus**: Be ready to derive the policy gradient theorem from scratch using log-derivative trick.
2. **Algorithm Comparison**: Contrast REINFORCE (high variance) vs Actor-Critic (lower variance) vs PPO (constrained updates).
3. **Hyperparameters**: Understand role of discount factor γ, learning rates for actor/critic, and PPO's ε.
4. **Variance Reduction**: Explain baseline subtraction (advantage functions) and importance sampling.
5. **Implementation**: Write pseudocode for computing gradients in REINFORCE with a baseline.
6. **Current Research**: Cite recent improvements like Phasic Policy Gradient (PPG) or distributional critics.
7. **Math Alert**: Expect questions on converting objective maximization to expectation form via log probabilities.

Length: 2500 words, MSc CS (research-oriented) postgraduate level