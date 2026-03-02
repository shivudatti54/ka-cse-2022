# **Pure Equilibrium when Randomization is Allowed**

## **Introduction**

In algorithmic game theory, a pure equilibrium is a strategy profile where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. However, when randomization is allowed, players can assign probabilities to their strategies, making the game more complex. In this section, we will explore pure equilibrium in games with randomization.

## **Definition**

A pure equilibrium with randomization is a strategy profile where no player can improve their expected payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged and assigning probabilities to their actions.

## **Key Concepts**

- **Mixed Strategy**: A probability distribution over a set of pure strategies.
- **Randomization**: Assigning probabilities to pure strategies.
- **Pure Equilibrium with Randomization**: A strategy profile where no player can improve their expected payoff by unilaterally changing their strategy.

## **Example: Coin Toss Game**

Suppose two players, Alice and Bob, play a game where they simultaneously toss a coin. The payoff matrix is as follows:

|             | Heads | Tails |
| ----------- | ----- | ----- |
| Alice Heads | 1, 1  | 0, 0  |
| Alice Tails | 0, 0  | 1, 1  |
| Bob Heads   | 0, 0  | 1, 1  |
| Bob Tails   | 1, 1  | 0, 0  |

In this game, Alice and Bob can assign probabilities to their actions, such as Heads or Tails. A pure equilibrium with randomization occurs when the expected payoff for each player is the same, regardless of their strategy.

## **Finding Pure Equilibrium with Randomization**

To find the pure equilibrium with randomization, we need to find the probability distribution over the pure strategies that maximizes the expected payoff for each player.

For Alice, the expected payoff can be calculated as follows:

- Heads: 1 \* P(Heads) + 0 \* P(Tails) = P(Heads)
- Tails: 0 \* P(Heads) + 1 \* P(Tails) = P(Tails)

Since the expected payoff for Alice is the same in both cases, we can set P(Heads) = P(Tails).

Similarly, for Bob, the expected payoff can be calculated as follows:

- Heads: 1 \* P(Heads) + 1 \* P(Tails) = P(Heads) + P(Tails)
- Tails: 0 \* P(Heads) + 1 \* P(Tails) = P(Tails)

Again, since the expected payoff for Bob is the same in both cases, we can set P(Heads) = P(Tails).

## **Solution**

Since P(Heads) = P(Tails), we can conclude that the probability of each action is 1/2.

Therefore, the pure equilibrium with randomization is:

- Alice: Heads with probability 1/2 and Tails with probability 1/2
- Bob: Heads with probability 1/2 and Tails with probability 1/2

In this example, both Alice and Bob have the same expected payoff, and no player can improve their payoff by unilaterally changing their strategy.

## **Conclusion**

In conclusion, pure equilibrium with randomization is a strategy profile where no player can improve their expected payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged and assigning probabilities to their actions. By analyzing the expected payoff for each player, we can find the probability distribution over the pure strategies that maximizes the payoff for each player.

## **Key Takeaways**

- A pure equilibrium with randomization is a strategy profile where no player can improve their expected payoff by unilaterally changing their strategy.
- To find the pure equilibrium with randomization, we need to find the probability distribution over the pure strategies that maximizes the expected payoff for each player.
- By analyzing the expected payoff for each player, we can conclude that the probability of each action is 1/2 in the case of the Coin Toss Game.
