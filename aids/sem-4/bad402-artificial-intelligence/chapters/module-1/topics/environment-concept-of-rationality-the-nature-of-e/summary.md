# **Environment, Concept of Rationality, The Nature of Environment, The Structure of Agents**

### Environment

- **Definition**: The external world that interacts with an agent
- **Types of Environments**:
  - **Fully observable**: Agent can observe the state of the environment
  - **Partially observable**: Agent cannot observe the state of the environment
  - **Simple**: Environment has a limited state space
  - **Complex**: Environment has a large state space
- **Notions of Environment**:
  - **State**: The current situation of the environment
  - **Action**: The action taken by the agent
  - **Transition**: The change in the state of the environment after an action is taken

### Concept of Rationality

- **Definition**: An agent's decision-making process is guided by a rational strategy that maximizes its expected reward
- **Key Concepts**:
  - **Utility**: A measure of the desirability of an outcome
  - **Expected Utility**: The average utility of an action over all possible outcomes
  - **Optimality**: A decision that maximizes the expected utility
- **Theorems**:
  - **Pareto Optimality**: A decision that is optimal for one agent is also optimal for all agents
  - **Game Theory**: A study of strategic decision-making in situations where the outcome depends on the actions of multiple agents

### The Nature of Environment

- **Types of Environments**:
  - **Discrete**: Environment has a countable number of states
  - **Continuous**: Environment has a uncountable number of states
- **Notions of Environment**:
  - **Deterministic**: Environment's next state is completely determined by its current state and the action taken
  - **Stochastic**: Environment's next state is uncertain and depends on random variables

### The Structure of Agents

- **Types of Agents**:
  - **Simple Reflex Agents**: Agents make decisions based on a set of pre-defined rules
  - **Model-Based Reflex Agents**: Agents maintain a model of the environment and use it to make decisions
  - **Model-Based Rational Agents**: Agents use game theory and optimization techniques to make decisions
- **Notions of Agents**:
  - **State**: The current situation of the agent
  - **Action**: The action taken by the agent
  - **Goal**: The desired outcome of the agent

Formulas:

- Utility: U(s, a) = Σ[r(s, a, t+1)] \* p(s, a, t+1)
- Expected Utility: EU(s, a) = Σ[U(s, a)] \* p(s, a)
- Optimality: Optimal(s, a) = maxEU(s, a)
