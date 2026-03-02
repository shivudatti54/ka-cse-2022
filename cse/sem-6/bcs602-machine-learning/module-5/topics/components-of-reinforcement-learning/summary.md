# Components of Reinforcement Learning

## Overview

Reinforcement Learning involves an agent learning to make optimal decisions through interaction with an environment, receiving rewards for its actions, and learning from the cumulative outcomes.

## Key Components

- **Agent**: The learner that makes decisions and learns from environment feedback
- **Environment**: The external world the agent interacts with
- **State**: Current situation/configuration of the environment from agent's view
- **Action**: Choices available to the agent that affect the environment
- **Reward**: Immediate feedback signal indicating the quality of an action
- **Policy**: Strategy mapping states to actions (deterministic or stochastic)
- **Value Function**: Estimates expected long-term cumulative rewards from a state
- **Model**: Optional component predicting state transitions and rewards for planning

## Important Concepts

- Reward provides immediate feedback; value function estimates long-term outcomes
- Model-based RL uses environment models; model-free RL learns directly from experience
- The RL loop: State observation → Action selection → Reward reception → State update → Policy improvement

## Notes

- Policy is the core component the agent learns
- Value functions are used to evaluate and improve policies
- Not all RL systems include a model component
