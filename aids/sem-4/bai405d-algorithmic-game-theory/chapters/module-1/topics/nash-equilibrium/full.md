# Nash Equilibrium

## Introduction

Game theory is a branch of mathematics that deals with the study of strategic decision making in situations where the outcome depends on the actions of multiple individuals or parties. The Nash equilibrium is a fundamental concept in game theory that describes a state of balance between the actions of multiple players in a game. It is named after John Nash, who introduced the concept in the 1950s.

## Historical Context

The concept of the Nash equilibrium was first introduced by John Nash in his 1950 paper "Equilibrium Points in N-Person Games". Nash was an American mathematician who is also known for his work on differential geometry and partial differential equations. His work on game theory was groundbreaking, as it provided a mathematical framework for analyzing strategic decision making in competitive situations.

## Definition

A Nash equilibrium is a state of balance between the actions of multiple players in a game, where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. In other words, a Nash equilibrium is a stable state where no player has an incentive to deviate from their strategy, as any deviation would lead to a worse outcome.

## Mathematical Definition

Formally, a Nash equilibrium can be defined as follows:

Let G = (S, U) be a game, where S is the set of strategies available to each player, and U is the payoff function that assigns a payoff to each possible outcome. Let c be a strategy profile, where c = (c1, c2, ..., cn) is a tuple of strategies, one for each player. Then, c is a Nash equilibrium if and only if:

- For each player i, ci is a best response to the strategy profile ci'
- For each player j, cj is not a best response to the strategy profile ci'' where ci'' is identical to ci except for player j

Intuitively, this means that no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. Additionally, no player has an incentive to deviate from their strategy, as any deviation would lead to a worse outcome.

## Examples

### 1. The Prisoner's Dilemma

Consider the classic Prisoner's Dilemma game, where two prisoners must decide whether to cooperate or defect. The payoffs for each outcome are as follows:

|                           | Prisoner 1 Cooperates | Prisoner 1 Defects |
| ------------------------- | --------------------- | ------------------ |
| **Prisoner 2 Cooperates** | (3, 3)                | (0, 5)             |
| **Prisoner 2 Defects**    | (5, 0)                | (1, 1)             |

The Nash equilibrium in this game is (Defect, Defect), as both prisoners defect and get a higher payoff than if they both cooperated.

### 2. The Battle of the Sexes

Consider the Battle of the Sexes game, where two players must choose between playing tennis or golf. The payoffs for each outcome are as follows:

|                     | Player 1 Tennis | Player 1 Golf | Player 2 Tennis | Player 2 Golf |
| ------------------- | --------------- | ------------- | --------------- | ------------- |
| **Player 2 Tennis** | (0, 0)          | (0, 0)        | (-1, -1)        | (-1, -1)      |
| **Player 2 Golf**   | (-1, -1)        | (1, 1)        | (-1, -1)        | (0, 0)        |
| **Player 1 Tennis** | (-1, -1)        | (-1, -1)      | (1, 1)          | (0, 0)        |
| **Player 1 Golf**   | (0, 0)          | (-1, -1)      | (0, 0)          | (1, 1)        |

The Nash equilibrium in this game is (Golf, Tennis), as each player chooses the outcome that maximizes their payoff, given the other player's choice.

## Applications

The Nash equilibrium has numerous applications in various fields, including:

### 1. Economics

The Nash equilibrium is used to analyze competitive markets, where firms compete to maximize their profits. It is also used to study the behavior of oligopolies, where a small number of firms compete to dominate the market.

### 2. Politics

The Nash equilibrium is used to analyze the behavior of nations in international relations, where they must balance their interests and security concerns.

### 3. Biology

The Nash equilibrium is used to study the behavior of evolutionary systems, where organisms must balance their fitness and reproductive success.

### 4. Computer Science

The Nash equilibrium is used in artificial intelligence and machine learning to analyze the behavior of complex systems, where multiple agents must make strategic decisions.

## Case Studies

### 1. The Oligopoly Game

Consider a market with two firms, X and Y, that compete to sell widgets. The payoffs for each outcome are as follows:

|                               | Firm X Produces 100 Units | Firm X Produces 500 Units |
| ----------------------------- | ------------------------- | ------------------------- |
| **Firm Y Produces 100 Units** | (1000, 1000)              | (500, 500)                |
| **Firm Y Produces 500 Units** | (500, 500)                | (0, 0)                    |

The Nash equilibrium in this game is (500 Units, 500 Units), as each firm produces 500 units and gets a higher payoff than if they both produced 100 units.

### 2. The International Relations Game

Consider a game between two nations, A and B, where they must decide whether to cooperate or go to war. The payoffs for each outcome are as follows:

|                          | Nation A Cooperates | Nation A Goes to War |
| ------------------------ | ------------------- | -------------------- |
| **Nation B Cooperates**  | (1000, 1000)        | (0, 0)               |
| **Nation B Goes to War** | (0, 0)              | (-1000, -1000)       |

The Nash equilibrium in this game is (Go to War, Go to War), as each nation goes to war and gets a higher payoff than if they both cooperated.

## Diagrams

### 1. The Prisoner's Dilemma Matrix

The Prisoner's Dilemma matrix is a 2x2 matrix that represents the payoffs for each outcome:

|               | Cooperate | Defect |
| ------------- | --------- | ------ |
| **Cooperate** | (3, 3)    | (0, 5) |
| **Defect**    | (5, 0)    | (1, 1) |

### 2. The Battle of the Sexes Matrix

The Battle of the Sexes matrix is a 4x4 matrix that represents the payoffs for each outcome:

|                     | Player 1 Tennis | Player 1 Golf | Player 2 Tennis | Player 2 Golf |
| ------------------- | --------------- | ------------- | --------------- | ------------- |
| **Player 2 Tennis** | (0, 0)          | (0, 0)        | (-1, -1)        | (-1, -1)      |
| **Player 2 Golf**   | (-1, -1)        | (1, 1)        | (-1, -1)        | (0, 0)        |
| **Player 1 Tennis** | (-1, -1)        | (-1, -1)      | (1, 1)          | (0, 0)        |
| **Player 1 Golf**   | (0, 0)          | (-1, -1)      | (0, 0)          | (1, 1)        |

## Conclusion

The Nash equilibrium is a fundamental concept in game theory that describes a state of balance between the actions of multiple players in a game. It has numerous applications in various fields, including economics, politics, biology, and computer science. The Nash equilibrium is used to analyze competitive markets, study the behavior of nations in international relations, and understand the behavior of evolutionary systems. The concept of the Nash equilibrium is essential for making strategic decisions in complex situations.

## Further Reading

- Nash, J. F. (1950). Equilibrium Points in N-Person Games. Proceedings of the National Academy of Sciences, 36(5), 284-293.
- von Neumann, J., & Morgenstern, O. (1944). Theory of Games and Economic Behavior. Princeton University Press.
- Aumann, R. J. (1974). Subjective Probability and Expected Utility: A General Definition and Representation. Econometrica, 42(5), 933-963.
- Myerson, R. B. (1978). Nash Equilibrium and the Theory of Games. Cambridge University Press.
- Fudenberg, D., & Tirole, J. (1991). Game Theory. MIT Press.
