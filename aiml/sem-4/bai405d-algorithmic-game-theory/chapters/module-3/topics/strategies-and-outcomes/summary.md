# Strategies and Outcomes

### Definitions

- **Strategy**: A decision-maker's plan of action in a game.
- **Outcome**: The result of a game, achieved by a player's strategy.

### Key Concepts

- **Nash Equilibrium**: A stable state where no player can improve their outcome by unilaterally changing their strategy.
  - Formulated by John Nash: `NE = argmax_{s} min_{t} U(s,t)`
- **Pareto Optimality**: A state where no player can improve their outcome without making another player worse off.
  - Formulated by Vilfredo Pareto: `PO = (s,t) ∈ S × T | ∃j∈J ∃k∈J (U_j(s,t)>U_j(s',t') ∧ U_k(s,t)>U_k(s,t'))`
- **Mixed Strategy**: A strategy that uses probability to describe the probability of choosing each action.
  - Formulated by John Nash: `MS = (p_1, ..., p_n) ∈ [0,1]^n | ∑_{i=1}^n p_i = 1`

### Game Types

- **Zero-Sum Game**: The sum of players' outcomes is zero.
  - Example: Prisoner's Dilemma
- **Non-Zero Sum Game**: The sum of players' outcomes is not zero.
  - Example: Ultimatum Game

### Theorems

- **Nash Bargaining Problem**: A two-player game where one player offers a payoff to the other player, and the other player must decide whether to accept or reject.
  - Formulated by John Nash: `∃α∈[0,1] | U_i(α)=U_i(α')`
- **Prisoner's Dilemma**: A zero-sum game where two prisoners must decide whether to cooperate or defect.
  - Formulated by Merrill Flood and Melvin Dresher: `U(F, F) = 3, U(F, D) = 1, U(D, F) = 1, U(D, D) = 0`

### Important Formulas

- **Expected Utility**: The expected outcome of a strategy given a probability distribution.
  - Formulated by John von Neumann: `EU(s) = ∑_{t} p_t U(s,t)`
- **Payoff Matrix**: A table that describes the payoffs for each possible combination of strategies.
  - Example: Prisoner's Dilemma payoff matrix
