# Equilibrium in a Single Population

## Introduction

In the realm of algorithmic game theory, equilibrium refers to a state where no rational player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. This concept is crucial in understanding the behavior of players in strategic games, where the outcome depends on the actions of multiple agents. In this chapter, we will delve into the concept of equilibrium in a single population, exploring its historical context, theoretical foundations, and applications.

## Historical Context

The concept of equilibrium in game theory dates back to the works of John von Neumann and Oskar Morgenstern in the 1940s. They introduced the concept of a stable state where no player can improve their payoff by changing their strategy, assuming all other players keep their strategies unchanged. This idea has since been developed and refined by other researchers, leading to the modern concept of Nash equilibrium.

## Nash Equilibrium

A Nash equilibrium is a state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. In a game with multiple players, a Nash equilibrium is a set of strategies, one for each player, that satisfies the following condition:

- No player can improve their payoff by unilaterally changing their strategy.
- No player can improve their payoff by coordinating their strategy with other players.

Mathematically, a Nash equilibrium can be represented as a tuple (σ1, σ2, ..., σn), where σi is the strategy of player i, and σj is the strategy of player j for j ≠ i.

## Example: The Prisoner's Dilemma

The Prisoner's Dilemma is a classic game in which two prisoners, A and B, are given the following options:

|                             | Prisoner B stays silent       | Prisoner B betrays            |
| --------------------------- | ----------------------------- | ----------------------------- |
| **Prisoner A stays silent** | A and B both get 2 years      | A gets 1 year, B gets 3 years |
| **Prisoner A betrays**      | A gets 3 years, B gets 1 year | A and B both get 1 year       |

In this game, the Nash equilibrium is (betray, betray), where both prisoners betray each other, resulting in both getting a mediocre outcome (1 year in prison).

## Mixed Strategy Nash Equilibrium

In some games, it may not be possible to find a pure strategy Nash equilibrium, where all players use a single strategy. In this case, the mixed strategy Nash equilibrium is used. A mixed strategy is a probability distribution over the player's possible strategies.

Mathematically, a mixed strategy Nash equilibrium can be represented as (σ1, σ2, ..., σn), where σi is the probability distribution over the strategies of player i.

## Example: The Rock-Paper-Scissors Game

In the Rock-Paper-Scissors game, two players, A and B, can choose one of three strategies: rock, paper, or scissors. The payoffs for each player are as follows:

|                               | Player A chooses rock | Player A chooses paper | Player A chooses scissors |
| ----------------------------- | --------------------- | ---------------------- | ------------------------- |
| **Player B chooses rock**     | A and B tie           | B wins                 | A wins                    |
| **Player B chooses paper**    | A wins                | A and B tie            | B wins                    |
| **Player B chooses scissors** | A wins                | B wins                 | A and B tie               |

In this game, the mixed strategy Nash equilibrium is (1/3, 1/3, 1/3), where both players choose each strategy with probability 1/3. This equilibrium is stable because no player can improve their payoff by unilaterally changing their strategy.

## Applications

Nash equilibrium has numerous applications in various fields, including:

1.  **Economics**: Nash equilibrium is used to analyze the behavior of firms in oligopolistic markets.
2.  **Biology**: Nash equilibrium is used to model the behavior of individuals in evolutionary games.
3.  **Computer Science**: Nash equilibrium is used in game theory and artificial intelligence to model the behavior of agents in strategic games.
4.  **Politics**: Nash equilibrium is used to analyze the behavior of nations in international relations.

## Case Studies

1.  **The Bertrand Paradox**: In this game, two firms, A and B, compete on price. The payoffs for each firm are as follows:

    |                         | Firm A raises price                 | Firm A lowers price                 |
    | ----------------------- | ----------------------------------- | ----------------------------------- |
    | **Firm B raises price** | Firm A earns $100, Firm B earns $80 | Firm A earns $80, Firm B earns $100 |
    | **Firm B lowers price** | Firm A earns $80, Firm B earns $100 | Firm A earns $100, Firm B earns $80 |

    In this game, the Nash equilibrium is (raise, raise), where both firms raise their price. However, this equilibrium is not stable, as a decrease in price by one firm can lead to an increase in price by the other firm, resulting in a higher payoff.

    To find a stable equilibrium, we need to find a mixed strategy Nash equilibrium. In this case, the mixed strategy Nash equilibrium is (0.5, 0.5), where each firm raises its price with probability 0.5.

2.  **The Ultimatum Game**: In this game, two players, A and B, are offered a sum of money, $10. Player A proposes a split of the money, and player B can either accept or reject the proposal. The payoffs for each player are as follows:

    |                      | Player A proposes (x, y)                  | Player A proposes (x, 0)              |
    | -------------------- | ----------------------------------------- | ------------------------------------- |
    | **Player B accepts** | Player A earns $x, Player B earns $10 - x | Player A earns $10, Player B earns $0 |
    | **Player B rejects** | Player A earns $0, Player B earns $10     | Player A earns $0, Player B earns $10 |

    In this game, the Nash equilibrium is (0, 10), where player A proposes a split of the money where player B earns nothing. However, this equilibrium is not stable, as player B can reject the proposal and earn $10.

    To find a stable equilibrium, we need to find a mixed strategy Nash equilibrium. In this case, the mixed strategy Nash equilibrium is (0.5, 0.5), where each player proposes a split of the money with probability 0.5.

## Conclusion

In conclusion, equilibrium in a single population is a fundamental concept in algorithmic game theory. It refers to a state where no rational player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. The Nash equilibrium is a specific type of equilibrium that is stable and Pareto optimal. Mixed strategy Nash equilibrium is used when a pure strategy Nash equilibrium is not possible. Nash equilibrium has numerous applications in various fields, including economics, biology, computer science, and politics.

## Further Reading

- von Neumann, J., & Morgenstern, O. (1944). Theory of games and economic behavior.
- Nash, J. F. (1950). The bargaining problem. Econometrica, 18(2), 155-162.
- Aumann, R. J., & Mas-Colell, A. (1995). Game theory. In G. J. Brown & J. F. Davis (Eds.), The handbook of game theory (pp. 1-42).
- Myerson, R. B. (2008). Game theory: Analysis of conflict. Princeton University Press.
