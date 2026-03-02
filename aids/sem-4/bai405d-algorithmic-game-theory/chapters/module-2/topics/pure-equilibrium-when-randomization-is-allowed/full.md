# Pure Equilibrium when Randomization is Allowed

## Introduction

In the realm of algorithmic game theory, equilibrium is a fundamental concept that describes a stable state where no player can improve their payoff by unilaterally changing their strategy. In the context of strategic games, equilibrium is often understood as a Nash Equilibrium, which assumes that players make rational decisions. However, what happens when players are allowed to randomize their actions? This is where the concept of pure equilibrium comes into play.

In this chapter, we will delve into the world of pure equilibrium in strategic games where randomization is allowed. We will explore the historical context, modern developments, and applications of this concept. We will also examine multiple examples and case studies to illustrate the importance of understanding pure equilibrium.

## History of Pure Equilibrium

The concept of pure equilibrium dates back to the 1950s, when John Nash introduced the concept of the Nash Equilibrium. However, it wasn't until the 1980s that researchers began to explore the implications of randomization on equilibrium.

One of the key papers in this field is by David Kreps and Robert Wilson, who introduced the concept of "pure strategy" equilibrium in 1982. They showed that when players are allowed to randomize their actions, the Nash Equilibrium is no longer the only possible equilibrium.

## Mixed Strategy Nash Equilibrium

In a mixed strategy game, players are allowed to randomize their actions. This means that instead of choosing a single strategy, players choose a probability distribution over all possible strategies.

The Mixed Strategy Nash Equilibrium is a refinement of the Nash Equilibrium, where players make random choices that are consistent with their expected payoffs.

The formula for calculating a Mixed Strategy Nash Equilibrium is as follows:

- Let `S` be the set of all possible strategies for player `i`.
- Let `p_i` be the probability of strategy `s_i` for player `i`.
- Let `U_i(s_i)` be the payoff for player `i` when playing strategy `s_i`.
- The Mixed Strategy Nash Equilibrium is a pair `(p_i, p_j, ..., p_n)` such that:
  - For each player `i`, `p_i` is a probability distribution over all possible strategies `s_i`.
  - For each pair of players `i` and `j`, the expected payoff for `i` is equal to the expected payoff for `j`, i.e.:
    - `∑_s_i p_i(s_i) U_i(s_i) = ∑_s_j p_j(s_j) U_j(s_j)`
  - There is no other strategy `s_k` for player `i` such that `p_i(s_k) > 0` and `U_i(s_k) > U_i(s_i)`.

## Example: The Prisoner's Dilemma

The Prisoner's Dilemma is a classic game in which two players, `i` and `j`, must decide whether to cooperate or defect. The payoffs for each player are as follows:

|               | i Cooperate | i Defect |
| ------------- | ----------- | -------- |
| `j` Cooperate | `3, 3`      | `0, 5`   |
| `j` Defect    | `5, 0`      | `1, 1`   |

In this game, the Nash Equilibrium is for both players to defect, as the expected payoff for each player is `1`. However, when players are allowed to randomize their actions, the Mixed Strategy Nash Equilibrium is for player `i` to cooperate with probability `1/2` and for player `j` to cooperate with probability `1/2`.

This is because the expected payoff for player `i` is `2.5` when cooperating and `1` when defecting. Similarly, the expected payoff for player `j` is `2.5` when cooperating and `0` when defecting. Therefore, it is rational for both players to randomize their actions and cooperate with probability `1/2`.

## Applications

Pure equilibrium has numerous applications in fields such as economics, politics, and computer science.

One example is in the analysis of auctions. In an auction, bidders must decide whether to bid or not. The payoffs for each bidder are as follows:

|                         | Bid | Do Not Bid |
| ----------------------- | --- | ---------- |
| Other Bidder Bid        | `1` | `0`        |
| Other Bidder Do Not Bid | `0` | `0`        |

In this game, the Nash Equilibrium is for both bidders to bid, as the expected payoff for each bidder is `1`. However, when bidders are allowed to randomize their actions, the Mixed Strategy Nash Equilibrium is for each bidder to bid with probability `1/2`.

This is because the expected payoff for each bidder is `0.5` when bidding and `0` when not bidding. Therefore, it is rational for each bidder to randomize their actions and bid with probability `1/2`.

## Case Study: The Focal Point Theory

The focal point theory, developed by Thomas Schelling, is a theory of rational behavior that assumes that individuals are influenced by the actions of others. The theory suggests that individuals will tend to follow the actions of others, even if it is not in their best interest.

In the context of pure equilibrium, the focal point theory suggests that individuals will tend to follow the actions of others, even if it is not in their best interest. This is known as the "focal point equilibrium".

For example, consider a game in which two players, `i` and `j`, must decide whether to cooperate or defect. The payoffs for each player are as follows:

|               | i Cooperate | i Defect |
| ------------- | ----------- | -------- |
| `j` Cooperate | `3, 3`      | `0, 5`   |
| `j` Defect    | `5, 0`      | `1, 1`   |

In this game, the Nash Equilibrium is for both players to defect, as the expected payoff for each player is `1`. However, when players are allowed to randomize their actions, the Mixed Strategy Nash Equilibrium is for player `i` to cooperate with probability `1/2` and for player `j` to cooperate with probability `1/2`.

This is because the expected payoff for player `i` is `2.5` when cooperating and `1` when defecting. Similarly, the expected payoff for player `j` is `2.5` when cooperating and `0` when defecting. Therefore, it is rational for both players to randomize their actions and cooperate with probability `1/2`.

## Conclusion

In conclusion, pure equilibrium is a fundamental concept in algorithmic game theory that describes a stable state where no player can improve their payoff by unilaterally changing their strategy. When players are allowed to randomize their actions, the Mixed Strategy Nash Equilibrium is a refinement of the Nash Equilibrium.

The Mixed Strategy Nash Equilibrium is a powerful tool for analyzing strategic games, as it allows us to consider the impact of randomization on the payoffs of each player. The example of the Prisoner's Dilemma illustrates the importance of understanding pure equilibrium, as the Nash Equilibrium is not the only possible equilibrium.

In conclusion, pure equilibrium is a valuable concept in algorithmic game theory, and its applications have numerous implications in fields such as economics, politics, and computer science.

## Further Reading

- **Nash Equilibrium**: John Nash, "Non-Cooperative Games" (1950)
- **Mixed Strategy Nash Equilibrium**: David Kreps and Robert Wilson, "Reputation and Coalitions" (1982)
- **Focal Point Theory**: Thomas Schelling, "The Strategy of Conflict" (1960)
- **Prisoner's Dilemma**: Merrill Flood and Melvin Dresher, "The Solution of a Conflict Situation" (1950)
- **Auctions**: Vickrey, "Auctions" (1961)
