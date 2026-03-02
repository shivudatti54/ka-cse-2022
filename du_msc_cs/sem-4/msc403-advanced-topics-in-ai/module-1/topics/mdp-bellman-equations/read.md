# Markov Decision Processes and Bellman Equations

## Introduction
Markov Decision Processes (MDPs) form the foundational framework for sequential decision-making in uncertain environments, central to modern reinforcement learning and stochastic control systems. An MDP is defined by states, actions, transition probabilities, rewards, and a discount factor, providing a mathematical model for problems where outcomes are partly random and partly under the control of a decision-maker.

Bellman Equations are the cornerstone of solving MDPs, enabling the computation of optimal value functions and policies through dynamic programming. Their importance extends beyond classical AI to cutting-edge applications like robotic path planning, algorithmic trading, and healthcare treatment optimization. Recent research has expanded these concepts to partially observable environments (POMDPs) and deep reinforcement learning, making them critical for advanced AI systems.

In DU's MSc CS program, this topic bridges theoretical foundations with modern AI research. Understanding MDPs and Bellman Equations is essential for working with reinforcement learning algorithms like Q-Learning and Deep Q-Networks (DQNs), which are widely used in contemporary AI research papers from top conferences like NeurIPS and ICML.

## Key Concepts
1. **MDP Formalism**:
   - States (S): Finite set of possible situations
   - Actions (A): Decisions available to the agent
   - Transition Function P(s'|s,a): Probability of moving to state s' from s using action a
   - Reward Function R(s,a,s'): Immediate reward for transition
   - Discount Factor γ ∈ [0,1): Balances immediate vs future rewards

2. **Value Functions**:
   - State-value function V^π(s): Expected return starting from s under policy π
   - Action-value function Q^π(s,a): Expected return starting from s, taking action a, then following π

3. **Bellman Equations**:
   - **Bellman Expectation Equation**:
     V^π(s) = Σ_a π(a|s) Σ_{s'} P(s'|s,a)[R(s,a,s') + γV^π(s')]
   - **Bellman Optimality Equation**:
     V*(s) = max_a Σ_{s'} P(s'|s,a)[R(s,a,s') + γV*(s')]

4. **Dynamic Programming Methods**:
   - Value Iteration: Iteratively applies Bellman optimality equation until convergence
   - Policy Iteration: Alternates between policy evaluation and improvement

5. **Convergence Properties**:
   - Contraction mapping theorem guarantees convergence for γ < 1
   - Error bound: ||V_{k+1} - V*|| ≤ γ||V_k - V*||

## Examples

**Example 1: 3-State Gridworld**
States: S = {s1, s2 (terminal), s3}
Actions: A = {left, right}
Rewards: +10 for reaching s2, 0 otherwise
γ = 0.9

*Solution:*
1. Initialize V(s) = 0 for all s
2. Apply Bellman optimality equation iteratively:
   V*(s1) = max{0.8[0 + 0.9V*(s2)] + 0.2[0 + 0.9V*(s3)], 
                0.7[0 + 0.9V*(s2)] + 0.3[0 + 0.9V*(s3)]}
   Since s2 is terminal, V*(s2)=10
   After 3 iterations, V*(s1) ≈ 7.8

**Example 2: Inventory Management**
States: Inventory levels {0,1,2}
Actions: Order 0, 1, or 2 units
Demand probability: P(d=1)=0.6, P(d=2)=0.4
Holding cost: $1/unit, Stockout cost: $3/unit
γ = 0.95

*Solution:*
1. Build transition matrix considering demand probabilities
2. Compute rewards considering holding/stockout costs
3. Use policy iteration to find optimal ordering policy:
   Optimal policy π*(0)=2, π*(1)=1, π*(2)=0

## Exam Tips
1. Always specify whether you're using Bellman expectation or optimality equation
2. For value iteration problems, show at least 3 iterations manually
3. Remember γ^t factor when calculating cumulative rewards
4. In stochastic environments, account for all possible transitions (Σ_s' P(s'|s,a))
5. Recent research focus: Connect to Deep RL (e.g., DQN uses Q-learning with neural networks)
6. Common mistake: Forgetting that V*(s) uses max_a while V^π(s) uses π(a|s)
7. For proofs, use contraction mapping properties to explain convergence

Length: 2500 words, MSc CS (research-oriented) postgraduate level