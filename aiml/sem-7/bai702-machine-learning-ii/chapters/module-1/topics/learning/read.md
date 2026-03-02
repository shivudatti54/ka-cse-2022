# Q-Learning

## Introduction

Q-Learning is a model-free, **off-policy** temporal difference (TD) learning algorithm. It learns the optimal action-value function Q\* directly, without needing a model of the environment and regardless of the policy being followed.

## The Q-Learning Update Rule

```
Q(S_t, A_t) <- Q(S_t, A_t) + alpha * [R_{t+1} + gamma * max_a Q(S_{t+1}, a) - Q(S_t, A_t)]
```

Where:

- **alpha**: Learning rate (0 < alpha <= 1)
- **gamma**: Discount factor
- **max*a Q(S*{t+1}, a)**: Maximum Q-value over all actions in the next state
- **TD target**: R*{t+1} + gamma \* max_a Q(S*{t+1}, a)
- **TD error**: TD target - Q(S_t, A_t)

## Key Properties

### Off-Policy Learning

- Q-learning learns about the **greedy policy** (max_a Q)
- Can follow any policy (e.g., epsilon-greedy) while learning
- The behavior policy (data collection) differs from the target policy (what we're learning)

### Model-Free

- Does not require knowledge of transition probabilities P(s'|s,a)
- Does not require knowledge of reward function R(s,a,s')
- Learns directly from experience (samples)

### Convergence Guarantees

Under certain conditions, Q-learning converges to Q\*:

- All state-action pairs are visited infinitely often
- Learning rate decreases appropriately: sum(alpha) = infinity, sum(alpha^2) < infinity
- Example: alpha_n = 1/n for the n-th visit

## Q-Learning Algorithm

```
Initialize Q(s,a) arbitrarily for all s,a
Initialize Q(terminal, .) = 0

For each episode:
    Initialize state S

    For each step:
        Choose A from S using policy derived from Q (e.g., epsilon-greedy)
        Take action A, observe R, S'

        Q(S,A) <- Q(S,A) + alpha * [R + gamma * max_a Q(S',a) - Q(S,A)]

        S <- S'
    Until S is terminal
```

## Comparison with Dynamic Programming

| Aspect         | Dynamic Programming    | Q-Learning               |
| -------------- | ---------------------- | ------------------------ |
| Model Required | Yes                    | No                       |
| Updates        | Sweeps over all states | Sample-based             |
| Bootstrapping  | Uses true transitions  | Uses sampled transitions |
| Exploration    | Not needed             | Required                 |

## Hyperparameters

### Learning Rate (alpha)

- Too high: Unstable learning, oscillations
- Too low: Very slow learning
- Common values: 0.1 to 0.001
- Often decayed over time

### Exploration Parameter (epsilon)

- Balances exploration and exploitation
- Usually decayed: start at 0.1-1.0, decay to 0.01
- Higher values for more exploration

### Discount Factor (gamma)

- Problem-dependent
- Typically 0.9 to 0.99
- Lower for faster convergence, higher for long-term planning

## Practical Considerations

### Q-Table Representation

For discrete state-action spaces:

```
Q = array of shape (n_states, n_actions)
Q[s, a] = Q-value for state s, action a
```

### Handling Large State Spaces

- Function approximation (e.g., neural networks -> DQN)
- State aggregation
- Tile coding

### Common Issues

1. **Maximization bias**: Overestimation of Q-values
2. **Slow convergence**: May need many samples
3. **Limited to discrete actions**: Cannot directly handle continuous actions

## Summary

- Q-learning is off-policy TD learning
- Updates toward maximum next Q-value
- Converges to optimal Q\* under proper conditions
- Model-free: learns from experience
- Foundation for Deep Q-Networks (DQN)
