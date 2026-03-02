# SARSA Learning

## Introduction

SARSA learning is a type of reinforcement learning algorithm that is used to learn the optimal policy in a Markov Decision Process (MDP). It is an on-policy, temporal-difference (TD) learning algorithm that learns the value of a policy while also updating the policy itself. In this chapter, we will discuss the SARSA learning algorithm, its components, and how it works.

## Components of SARSA Learning

The SARSA learning algorithm consists of the following components:

- **Agent**: The agent is the entity that interacts with the environment and learns the optimal policy.
- **Environment**: The environment is the external world that the agent interacts with.
- **Actions**: The actions are the decisions made by the agent in the environment.
- **States**: The states are the situations or status of the environment.
- **Reward**: The reward is the feedback received by the agent for taking an action in a state.
- **Policy**: The policy is the mapping from states to actions.
- **Value Function**: The value function is the expected return or utility of taking an action in a state.

## How SARSA Learning Works

The SARSA learning algorithm works as follows:

1. **Initialization**: The agent initializes the policy, value function, and other parameters.
2. **Action Selection**: The agent selects an action based on the current policy and state.
3. **Take Action**: The agent takes the selected action in the environment.
4. **Get Reward**: The agent receives a reward for taking the action.
5. **Next State**: The agent observes the next state of the environment.
6. **Update Value Function**: The agent updates the value function based on the reward and next state.
7. **Update Policy**: The agent updates the policy based on the updated value function.
8. **Repeat**: Steps 2-7 are repeated until convergence or a stopping criterion is reached.

## SARSA Learning Algorithm

The SARSA learning algorithm can be mathematically represented as follows:

- **Value Function Update**: Q(s, a) ← Q(s, a) + α[r + γQ(s', a') - Q(s, a)]
- **Policy Update**: π(s) ← argmax(Q(s, a))

where Q(s, a) is the value function, α is the learning rate, r is the reward, γ is the discount factor, s' is the next state, a' is the next action, and π(s) is the policy.

## Example

Consider a grid world where an agent needs to navigate from the top-left corner to the bottom-right corner. The agent can take four actions: up, down, left, and right. The reward for taking an action is -1, and the reward for reaching the goal is 10. The SARSA learning algorithm can be used to learn the optimal policy in this environment.

## Exam Tips

1. SARSA learning is an on-policy, TD learning algorithm.
2. The SARSA learning algorithm updates the value function and policy simultaneously.
3. The value function update in SARSA learning is Q(s, a) ← Q(s, a) + α[r + γQ(s', a') - Q(s, a)].
4. The policy update in SARSA learning is π(s) ← argmax(Q(s, a)).
5. SARSA learning can be used in both episodic and continuous tasks.
6. The SARSA learning algorithm can be modified to use eligibility traces for more efficient learning.
