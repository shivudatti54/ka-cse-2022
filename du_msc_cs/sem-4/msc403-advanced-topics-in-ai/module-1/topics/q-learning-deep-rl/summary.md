# Q-Learning and Deep RL - Summary

## Key Definitions and Concepts
- **Q-Value**: Expected cumulative reward from taking action a in state s
- **TD Error**: δ = r + γmaxQ(s',a') - Q(s,a)
- **Experience Replay**: Dataset of transitions for decorrelated training
- **Target Network**: Stable Q-value estimator updated periodically

## Important Formulas and Theorems
- **Q-Update**: Q(s,a) ← Q(s,a) + α[r + γmaxₐ’ Q(s’,a’) - Q(s,a)]
- **DQN Loss**: L(θ) = E[(r + γmaxₐ’ Q_target(s’,a’; θ⁻) - Q(s,a; θ))²]
- **Double DQN Update**: y = r + γQ_target(s’, argmaxₐ Q(s’,a; θ); θ⁻)
- **Convergence Theorem**: Tabular Q-Learning converges to optimal Q* if all state-action pairs visited infinitely often

## Key Points
- Q-Learning is model-free and off-policy
- DQN requires two key innovations: experience replay and target networks
- Overestimation bias arises from max operator in Q-Learning
- Prioritized replay focuses on high-error transitions
- Partial observability requires history-based approaches
- Current research extends to distributional RL and meta-learning
- Real-world applications need careful reward shaping

## Common Mistakes to Avoid
- Confusing SARSA with Q-Learning (on-policy vs off-policy)
- Forgetting to clip rewards in DQN implementations
- Neglecting exploration strategies in continuous spaces
- Misinterpreting convergence guarantees in function approximation

## Revision Tips
1. Practice deriving Q-Learning update from Bellman equation
2. Compare architecture diagrams of DQN variants
3. Code simple DQN implementations from scratch
4. Study seminal papers: Mnih et al. 2015 (Nature DQN), Rainbow DQN
5. Use MDP toolkits like OpenAI Gym for visualization