# Revision Notes: The Prisoner's Dilemma

=============================================

## Introduction

---

The Prisoner's Dilemma is a fundamental concept in Game Theory, illustrating the conflict between individual and group rationality.

## Key Points

---

- **Definition:** A game theory problem where two prisoners must decide whether to cooperate or betray each other, with each prisoner's action affecting the outcome.
- **Game Matrix:**

  |               | Betray | Cooperate |
  | ------------- | ------ | --------- |
  | **Betray**    | (5, 5) | (3, 1)    |
  | **Cooperate** | (1, 3) | (0, 0)    |

- **Payoff Matrix:**

  |               | Betray                       | Cooperate                    |
  | ------------- | ---------------------------- | ---------------------------- |
  | **Betray**    | Prisoner 1: 5, Prisoner 2: 5 | Prisoner 1: 3, Prisoner 2: 1 |
  | **Cooperate** | Prisoner 1: 1, Prisoner 2: 3 | Prisoner 1: 0, Prisoner 2: 0 |

- **Nash Equilibrium:** A state in which no player can improve their payoff by unilaterally changing their strategy, assuming the other player's strategy remains the same.
- **Pareto Optimality:** A state in which no player can improve their payoff without making another player worse off.
- **Dominant Strategy:** A strategy that is the best choice regardless of the other player's action.

## Formulas and Theorems

---

- **Nash Equilibrium Formula:** \( (S*1, S_2) \) is a Nash Equilibrium if and only if:
  \( \max*{S*1} \left( \max*{S*2} \left[ u(S_1, S_2) \right] \right) = \max*{S*2} \left( \max*{S_1} \left[ u(S_1, S_2) \right] \right) \)
- **Pareto Optimality Theorem:** A state is Pareto Optimal if and only if no player can improve their payoff without making another player worse off.

## Important Concepts

---

- **Cooperation vs. Defection:** The choice between cooperating (working together) and defecting (betraying each other).
- **Individual Rationality vs. Group Rationality:** The conflict between individual rationality (choosing the best action for oneself) and group rationality (choosing the action that benefits both players).
- **Mutual Benefit vs. Mutual Defeat:** The contrast between outcomes where both players benefit and outcomes where both players are worse off.

## Study Tips

---

- Understand the game matrix and payoff matrix to visualize the game's structure.
- Recognize the Nash Equilibrium and Pareto Optimality concepts to identify optimal strategies.
- Analyze the dominant strategy to determine the best choice for each player.
- Practice solving the Prisoner's Dilemma to develop problem-solving skills.
