# Markov Decision Process

## Introduction

Markov Decision Process (MDP) is a mathematical framework that forms the theoretical foundation for reinforcement learning. It provides a formal way to model decision-making in situations where outcomes are partly random and partly under the control of a decision-maker. MDPs are extensively used in various real-world applications including robotics, game playing, autonomous vehicles, resource management, and economic modeling.

The concept was introduced by Richard Bellman in the 1950s and has since become a cornerstone in the field of artificial intelligence and machine learning. Understanding MDPs is essential for any student of machine learning because they provide the underlying mathematical structure that allows us to formulate and solve sequential decision-making problems systematically. The framework enables us to compute optimal policies that maximize cumulative rewards over time, which is the fundamental goal of reinforcement learning.

In this topic, we will explore the components of MDP, the mathematical formulation, and the key concepts that enable us to solve decision-making problems. We will also examine the Bellman equations, which are central to finding optimal solutions in MDPs.

## Key Concepts

### 1. Markov Property

The Markov property is the fundamental assumption underlying MDPs. It states that the future state of a system depends only on the current state and not on the sequence of states that preceded it. Mathematically, this is expressed as:

**P(Sₜ₊₁ | Sₜ, Sₜ₋₁, ..., S₀) = P(Sₜ₊₁ | Sₜ)**

This property implies that the current state contains all relevant information about the future, making the problem computationally tractable. In practical terms, this means we don't need to remember the entire history of states to make optimal decisions; we only need to know where we are currently.

### 2. Components of MDP

An MDP is formally defined as a tuple (S, A, P, R, γ) where:

**S (States):** A finite set of possible states in the environment. For example, in a grid world, S might contain all possible grid positions.

**A (Actions):** A finite set of actions that the agent can take. These are the decisions available to the agent at each state.

**P (Transition Probability):** The state transition probability function P(s'|s, a) represents the probability of moving from state s to state s' when taking action a. This captures the stochastic nature of the environment.

**R (Reward):** The reward function R(s, a, s') gives the immediate reward received when transitioning from state s to state s' by taking action a. Alternatively, it can be defined as R(s, a) or R(s).

**γ (Discount Factor):** The discount factor γ ∈ [0, 1] determines the importance of future rewards. A lower discount factor makes the agent prioritize immediate rewards, while a higher value makes it consider future rewards more heavily.

### 3. Policy

A policy π is a mapping from states to actions. It defines the behavior of the agent. There are two types of policies:

**Deterministic Policy:** π(s) = a, which specifies a particular action for each state.

**Stochastic Policy:** π(a|s) = P(a|s), which gives the probability of taking action a when in state s.

The goal of reinforcement learning is to find an optimal policy π\* that maximizes the expected cumulative reward.

### 4. Value Function

The value function estimates how good it is to be in a particular state. There are two types:

**State Value Function Vπ(s):** The expected return when starting from state s and following policy π.

Vπ(s) = Eπ[Gₜ | Sₜ = s] = Eπ[Σₖ=₀^∞ γᵏRₜ₊ₖ₊₁ | Sₜ = s]

**Action Value Function Qπ(s, a):** The expected return when starting from state s, taking action a, and then following policy π.

Qπ(s, a) = Eπ[Gₜ | Sₜ = s, Aₜ = a] = Eπ[Σₖ=₀^∞ γᵏRₜ₊ₖ₊₁ | Sₜ = s, Aₜ = a]

### 5. Bellman Equations

The Bellman equations are fundamental to solving MDPs. They express the value functions recursively in terms of immediate rewards and future values.

**Bellman Equation for Vπ:**

Vπ(s) = Σₐ π(a|s) Σₛ' P(s'|s, a)[R(s, a, s') + γVπ(s')]

**Bellman Equation for Qπ:**

Qπ(s, a) = Σₛ' P(s'|s, a)[R(s, a, s') + γ Σₐ' π(a'|s')Qπ(s', a')]

### 6. Optimal Value Functions and Optimal Policy

The optimal state value function V\*(s) gives the maximum expected return achievable from state s:

V*(s) = maxₐ Σₛ' P(s'|s, a)[R(s, a, s') + γV*(s')]

The optimal action value function Q\*(s, a) is:

Q*(s, a) = Σₛ' P(s'|s, a)[R(s, a, s') + γ maxₐ' Q*(s', a')]

The optimal policy π\* always chooses actions that maximize the Q-value:

π*(s) = argmaxₐ Q*(s, a)

## Examples

### Example 1: Simple Grid World

Consider a 2×2 grid world with the following layout:

```
+---+---+
| A | B |
+---+---+
| C | D |
+---+---+
```

States: S = {A, B, C, D}
Actions: A = {Up, Down, Left, Right}
Rewards: -1 for each move (to encourage shortest path), +10 for reaching goal state D

Assume γ = 0.9 and deterministic transitions (moving off-grid leaves state unchanged).

From state A, if we take action "Right", we go to state B with reward -1.
V(A) = max over actions of [R + γV(next state)]
= max{-1 + 0.9(V(B)), -1 + 0.9(V(A)), -1 + 0.9(V(C)), -1 + 0.9(V(A))}

This simple example illustrates how we compute values by considering all possible actions and their consequences.

### Example 2: Computing Q-Values

Given an MDP with:

- Two states: S₁, S₂
- Two actions: a₁, a₂
- P(s'|s, a): Deterministic - taking a₁ from S₁ goes to S₂ with probability 1
- R(s, a, s'): +5 when going to S₂
- γ = 0.5

Calculate Q(S₁, a₁):
Q(S₁, a₁) = R + γ × max Q(S₂, a)
= 5 + 0.5 × max(Q(S₂, a₁), Q(S₂, a₂))

If we know Q(S₂, a₁) = 3 and Q(S₂, a₂) = 1:
Q(S₁, a₁) = 5 + 0.5 × max(3, 1) = 5 + 0.5 × 3 = 6.5

### Example 3: Finding Optimal Policy

Consider a vending machine MDP:

- States: {No Coin, Has Coin}
- Actions: {Insert Coin, Press Button, Do Nothing}
- Rewards: +5 for getting soda (transition with Press Button when Has Coin)
- γ = 0.9

Optimal policy:

- At "No Coin" state: Insert Coin (to reach "Has Coin")
- At "Has Coin" state: Press Button (to get reward)

This demonstrates how the optimal policy guides the agent toward maximizing cumulative rewards.

## Exam Tips

1. **Understand the Markov Property**: Remember it states that future depends only on the present state, not the past history. This is frequently tested in university exams.

2. **Memorize the MDP Tuple**: The tuple (S, A, P, R, γ) is essential. Know what each component represents.

3. **Bellman Equations are Key**: Both value function and Q-function Bellman equations are important. Practice writing them from memory.

4. **Discount Factor Purpose**: Understand why γ ∈ [0, 1] is used - it ensures finite values and models preference for immediate rewards.

5. **Difference Between V and Q**: V(s) is the value of being in a state, while Q(s, a) is the value of taking a specific action from that state.

6. **Optimal Policy Relationship**: The optimal policy is derived from the optimal Q-function: π*(s) = argmaxₐ Q*(s, a).

7. **Solve Simple MDP Problems**: Be prepared to compute values for simple deterministic MDPs with 2-3 states.

8. **Know the Connection to RL**: Understand that reinforcement learning algorithms (like Q-learning, Policy Iteration) are methods to solve MDPs when the model is unknown.
