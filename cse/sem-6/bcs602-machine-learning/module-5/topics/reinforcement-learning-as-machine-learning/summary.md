# Reinforcement Learning in ML Taxonomy

## Overview

Reinforcement Learning (RL) is one of the three fundamental paradigms in machine learning, alongside supervised and unsupervised learning. RL differs fundamentally by learning through interaction with an environment rather than from labeled data or hidden patterns.

## Key Differences

- **Supervised Learning**: Learns from labeled data with direct feedback; each prediction is independent
- **Unsupervised Learning**: Discovers patterns in unlabeled data without feedback
- **RL**: Learns through trial-and-error interaction; receives scalar rewards; decisions affect future states

## Core Characteristics of RL

- **Learning via Interaction**: Agent learns by interacting with environment
- **Delayed Rewards**: Consequences of actions may not be immediate
- **Sequential Decisions**: Each action influences future states and opportunities
- **Exploration-Exploitation Trade-off**: Must balance trying new actions vs using known good actions

## When to Use RL

Use reinforcement learning when:

- Problem involves sequential decision-making
- No labeled dataset exists but environment is available
- Rewards are delayed or sparse
- Goal is to maximize long-term cumulative reward

## Important Concepts

- **Agent**: The learner/decision-maker
- **Environment**: System the agent interacts with
- **Policy**: Strategy for choosing actions
- **Reward**: Immediate feedback signal
- **Value Function**: Long-term return estimate
