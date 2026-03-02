# **Nash Equilibrium**

## **Introduction**

Nash equilibrium is a fundamental concept in game theory, named after John Nash, who introduced it in the 1950s. It is a mathematical framework for analyzing strategic decision-making in situations where multiple individuals or entities have conflicting interests. In this study material, we will explore the concept of Nash equilibrium, its definition, and its applications.

## **Definition**

A Nash equilibrium is a stable state in a game where no player can improve their payoff (or outcome) by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. In other words, it is a situation where:

- No player has an incentive to deviate from their chosen strategy
- All players are satisfied with their chosen strategy

## **Mathematical Definition**

A Nash equilibrium can be formalized as follows:

Let G = (N, X, u) be a game, where:

- N is a set of players
- X is a set of strategies for each player
- u: X × ⋯ × X → ℝ is a payoff function that assigns a real value to each possible combination of strategies

A Nash equilibrium is a probability distribution over strategies, σ = (σ1, ..., σn) ∈ X × ⋯ × X, such that:

- For each player i, σi is the optimal strategy for player i, given the strategies of the other players (i.e., σi = argmax u(σi, σ-1, ..., σn) over X)
- For each pair of players i and j, σi ≠ σj, we have u(σi, σ-1, ..., σn) ≤ u(σj, σ-1, ..., σn)

## **Interpretation**

The Nash equilibrium concept has several intuitive interpretations:

- **No regret**: No player regrets their chosen strategy, as they cannot improve their payoff by changing their strategy.
- **Stability**: The Nash equilibrium is stable, as no player has an incentive to deviate from their chosen strategy.
- **Optimal outcome**: The Nash equilibrium represents an optimal outcome for each player, given the strategies of the other players.

## **Examples**

### Example 1: The Prisoner's Dilemma

Two prisoners, A and B, are arrested and interrogated separately. Each prisoner has two options: to confess or remain silent. The payoff matrix is as follows:

|                               | Prisoner A Confesses                 | Prisoner A Remains Silent            |
| ----------------------------- | ------------------------------------ | ------------------------------------ |
| **Prisoner B Confesses**      | 2 years in prison, 2 years in prison | 1 year in prison, 10 years in prison |
| **Prisoner B Remains Silent** | 10 years in prison, 1 year in prison | 1 year in prison, 1 year in prison   |

The Nash equilibrium occurs when both prisoners confess, as this is the optimal strategy for each prisoner, given the strategy of the other prisoner.

### Example 2: The Ultimatum Game

Two players, Alice and Bob, are offered a sum of money, x. Alice proposes a division of the money, {a, b}, and Bob accepts or rejects the proposal. If Bob rejects, neither Alice nor Bob receives anything. The payoff matrix is as follows:

|                             | Bob Accepts | Bob Rejects |
| --------------------------- | ----------- | ----------- |
| **Alice's Proposal (a, b)** | a, b        | 0           |
| **Alice's Proposal (0, x)** | 0           | x           |

The Nash equilibrium occurs when Alice proposes a division of the money, {x/2, x/2}, as this is the optimal strategy for Alice, given Bob's strategy.

## **Key Concepts**

- **Strategic form**: A representation of a game in terms of the strategies of the players.
- **Payoff function**: A function that assigns a real value to each possible combination of strategies.
- **Optimal strategy**: A strategy that maximizes the payoff for a player, given the strategies of the other players.
- **Stable state**: A state where no player has an incentive to deviate from their chosen strategy.

## **Applications**

Nash equilibrium has numerous applications in various fields, including:

- **Economics**: Game theory is used to model and analyze the behavior of firms and individuals in competitive markets.
- **Politics**: Game theory is used to model and analyze the behavior of nations and international organizations.
- **Computer Science**: Game theory is used to design and analyze algorithms for competitive problems.

## **Conclusion**

Nash equilibrium is a fundamental concept in game theory, providing a mathematical framework for analyzing strategic decision-making in situations where multiple individuals or entities have conflicting interests. Understanding Nash equilibrium is essential for modeling and analyzing complex systems in economics, politics, and computer science.
