# Overview of Reinforcement Learning

## Introduction to Reinforcement Learning

Reinforcement Learning (RL) is a type of machine learning where an agent learns to make decisions by performing actions in an environment to achieve maximum cumulative reward. Unlike supervised learning with labeled datasets or unsupervised learning that finds hidden patterns, RL operates through trial and error, learning from the consequences of its actions.

**Key distinction**: In RL, there's no supervisor, only a reward signal. Feedback is delayed, not instantaneous. Time matters (sequential data), and the agent's actions affect the subsequent data it receives.

## Core Components of Reinforcement Learning

RL systems consist of four main components:

1. **Agent**: The learner or decision-maker
2. **Environment**: Everything the agent interacts with
3. **Actions**: What the agent can do
4. **Rewards**: Feedback from the environment

```
+----------------+    Action    +-------------+
|                | -----------> |             |
|     Agent      |              | Environment |
|                | <----------- |             |
+----------------+    Reward    +-------------+
```

### States and Observations

- **State (s)**: Complete description of the environment
- **Observation (o)**: Partial description of the state that the agent perceives

### Policy (π)

A policy defines the agent's behavior - it's a mapping from states to actions. It can be:
- **Deterministic**: a = π(s)
- **Stochastic**: π(a|s) = P[A = a|S = s]

### Value Function

The value function vπ(s) predicts the expected cumulative reward from state s, following policy π:
vπ(s) = 𝔼[Gt|St = s] where Gt is the total discounted reward.

### Model

A model predicts what the environment will do next:
- **Transition model**: P[St+1 = s'|St = s, At = a]
- **Reward model**: R(s, a) = 𝔼[Rt+1|St = s, At = a]

## Markov Decision Process (MDP)

MDP provides the mathematical framework for modeling decision-making in RL. An MDP is defined by:

- **States**: S
- **Actions**: A
- **Transition probabilities**: P(s'|s, a)
- **Reward function**: R(s, a, s')
- **Discount factor**: γ ∈ [0, 1]

### Markov Property

"The future is independent of the past given the present"
P[St+1|St] = P[St+1|S1, S2, ..., St]

## Exploration vs Exploitation

The fundamental trade-off in RL:
- **Exploitation**: Make the best decision given current information
- **Exploration**: Gather more information to make better decisions

```
Decision-making process:
+---------------------+
| Current Knowledge   |
| about Environment   |
+---------------------+
           |
           v
+---------------------+
| Choose: Explore     |    OR    | Choose: Exploit    |
| (gather information)|          | (maximize reward) |
+---------------------+          +-------------------+
```

## Multi-Armed Bandit Problem

A simplified RL problem with a single state that demonstrates the exploration-exploitation dilemma.

**Scenario**: Multiple slot machines (bandits) with unknown reward probabilities. The agent must decide which machines to play to maximize cumulative reward.

| Strategy | Approach | Advantage | Disadvantage |
|----------|----------|-----------|--------------|
| ε-Greedy | Choose random action with probability ε, else best action | Simple implementation | Suboptimal exploration |
| Softmax | Action selection based on Boltzmann distribution | Prioritizes promising actions | Temperature parameter tuning |
| UCB | Select action with highest upper confidence bound | Theoretical guarantees | Complex implementation |

## Q-Learning

Q-learning is a model-free RL algorithm that learns the value of action-state pairs.

**Q-function**: Q(s, a) represents the expected cumulative reward from taking action a in state s.

**Update rule**:
Q(s, a) ← Q(s, a) + α [R(s, a) + γ max Q(s', a') - Q(s, a)]
                         a'

Where:
- α: learning rate
- γ: discount factor
- R(s, a): immediate reward
- max Q(s', a'): maximum future reward

```
Q-learning algorithm:
Initialize Q(s, a) arbitrarily
Repeat for each episode:
    Initialize state s
    Repeat for each step of episode:
        Choose action a from s using policy derived from Q
        Take action a, observe r, s'
        Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
        s ← s'
    Until s is terminal
```

## SARSA (State-Action-Reward-State-Action)

SARSA is an on-policy temporal difference learning algorithm.

**Update rule**:
Q(s, a) ← Q(s, a) + α [R(s, a) + γ Q(s', a') - Q(s, a)]

Key difference from Q-learning: SARSA uses the actual next action taken (a'), while Q-learning uses the maximum possible value.

```
SARSA algorithm:
Initialize Q(s, a) arbitrarily
Repeat for each episode:
    Initialize state s
    Choose action a from s using policy derived from Q
    Repeat for each step of episode:
        Take action a, observe r, s'
        Choose action a' from s' using policy derived from Q
        Q(s, a) ← Q(s, a) + α [r + γ Q(s', a') - Q(s, a)]
        s ← s', a ← a'
    Until s is terminal
```

## Comparison: Q-Learning vs SARSA

| Aspect | Q-Learning | SARSA |
|--------|------------|-------|
| Policy Type | Off-policy | On-policy |
| Action Selection | Uses max Q-value for next state | Uses actual next action |
| Exploration | More aggressive | More conservative |
| Safety | May learn risky policies | Learns safer policies |
| Convergence | Guaranteed under certain conditions | Guaranteed under certain conditions |

## Applications of Reinforcement Learning

1. **Game Playing**: AlphaGo, Chess programs
2. **Robotics**: Autonomous navigation, manipulation
3. **Recommendation Systems**: Personalized content delivery
4. **Finance**: Portfolio optimization, trading
5. **Healthcare**: Treatment strategy optimization
6. **Autonomous Vehicles**: Decision-making systems

## Challenges in Reinforcement Learning

1. **Credit Assignment Problem**: Determining which actions led to rewards
2. **Exploration-Exploitation Dilemma**: Balancing between trying new actions and exploiting known good ones
3. **Curse of Dimensionality**: State space grows exponentially with variables
4. **Partial Observability**: Incomplete information about the environment
5. **Delayed Rewards**: Consequences of actions may not be immediate

## Exam Tips

1. **Understand the differences** between RL and other ML paradigms (supervised, unsupervised)
2. **Memorize the key components** of an RL system (agent, environment, actions, rewards)
3. **Practice writing the update rules** for Q-learning and SARSA
4. **Be able to explain** the exploration-exploitation trade-off with examples
5. **Compare and contrast** model-based vs model-free approaches
6. **Understand MDP formulation** for given problems
7. **Know the applications** and limitations of RL in real-world scenarios