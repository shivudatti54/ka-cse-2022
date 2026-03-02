# Overview of Reinforcement Learning

## Overview

Reinforcement Learning (RL) is a machine learning paradigm where an agent learns optimal decision-making through direct interaction with an environment. Unlike supervised learning (learning from labeled data) or unsupervised learning (finding patterns in unlabeled data), RL involves learning from rewards and penalties received through trial-and-error.

## Key Components

- **Agent**: The learning entity that takes actions
- **Environment**: Everything the agent interacts with
- **State (s)**: Current situation representation
- **Action (a)**: Decision made by the agent
- **Reward (r)**: Feedback signal from environment
- **Policy (π)**: Strategy mapping states to actions
- **Value Function**: Expected cumulative return from a state

## Important Concepts

**Trial-and-Error Learning**: The agent explores actions, receives feedback, and gradually learns which actions yield higher rewards. This is the fundamental learning mechanism in RL.

**Exploration vs Exploitation**: A core dilemma where agents must balance trying new actions (exploration) against using known good actions (exploitation). Common strategies include epsilon-greedy, softmax, and UCB.

**Discount Factor (γ)**: A value between 0 and 1 that gives more weight to immediate rewards and ensures finite returns in infinite-horizon tasks.

**Return (G)**: Cumulative sum of rewards, calculated as G*t = R*{t+1} + γR*{t+2} + γ²R*{t+3} + ...

## Notes

- RL is inspired by behavioral psychology
- The agent learns from consequences, not from explicit instruction
- The goal is to maximize cumulative reward over time
- RL has achieved major successes in games, robotics, and autonomous systems
