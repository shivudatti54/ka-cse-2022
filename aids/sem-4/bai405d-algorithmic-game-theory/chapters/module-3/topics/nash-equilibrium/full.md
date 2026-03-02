# Nash Equilibrium

## Introduction

The Nash equilibrium is a fundamental concept in game theory, named after John Nash, who introduced it in the 1950s. It is a stable state in a game where no player can improve their payoff (or outcome) by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. In this deep dive, we will explore the concept of Nash equilibrium, its historical context, and its applications in various fields.

### Historical Context

In 1950, John Nash was working on a thesis at Princeton University, where he was studying the behavior of players in non-cooperative games. He was particularly interested in understanding how players can make rational decisions in situations where the outcome depends on the actions of multiple players. Nash's work was influenced by the works of von Neumann and Morgenstern, who had developed the concept of expected utility theory.

Nash's breakthrough came when he realized that, in a game, players can achieve a stable outcome by making decisions that are based on their own payoffs, rather than on the payoffs of other players. This led to the development of the Nash equilibrium, which is a concept that has been widely used in game theory and beyond.

### Mathematical Definition

A Nash equilibrium is a state in a game where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. Mathematically, a Nash equilibrium can be defined as follows:

Let G = (N, A, u) be a game, where N is the set of players, A is the set of possible actions for each player, and u is the payoff function.

A Nash equilibrium is a pair (s, c) where s ∈ S and c ∈ C, such that:

- s ∈ S is a strategy profile, where each player i has a strategy s_i.
- c ∈ C is a payoff vector, where each player i has a payoff c_i.

If player i can improve their payoff by changing their strategy, then (s, c) is not a Nash equilibrium.

### Examples

Let's consider a simple example to illustrate the concept of Nash equilibrium.

**Example 1: Prisoner's Dilemma**

Suppose two prisoners, A and B, are arrested and interrogated separately by the police. The payoff matrix for this game is as follows:

|               | B stays quiet | B confesses |
| ------------- | ------------- | ----------- |
| A stays quiet | A: 3, B: 3    | A: 0, B: 5  |
| A confesses   | A: 5, B: 0    | A: 2, B: 2  |

The Nash equilibrium in this game is (A stays quiet, B stays quiet), where both prisoners choose to stay quiet, because if either of them confesses, the other prisoner will get a higher payoff.

**Example 2: Ultimatum Game**

Suppose two players, Alice and Bob, are given an amount of money to split between them. Alice proposes a split, and Bob can either accept or reject the proposal. The payoff matrix for this game is as follows:

|                  | Bob accepts       | Bob rejects       |
| ---------------- | ----------------- | ----------------- |
| Alice's proposal | Alice: 10, Bob: 0 | Alice: 0, Bob: 10 |
| Alice's proposal | Alice: 5, Bob: 5  | Alice: 0, Bob: 0  |

The Nash equilibrium in this game is (Alice's proposal: 5:5, Bob rejects), where Alice proposes a split of 5:5, and Bob rejects the proposal, because he can get a higher payoff by rejecting the proposal.

### Applications

Nash equilibrium has been widely used in various fields, including:

- **Economics**: Nash equilibrium is used to analyze the behavior of firms and consumers in oligopolistic markets.
- **Politics**: Nash equilibrium is used to analyze the behavior of governments and international relations.
- **Computer Science**: Nash equilibrium is used in game theory and artificial intelligence to analyze the behavior of agents in complex systems.
- **Biology**: Nash equilibrium is used to analyze the behavior of individuals in evolutionary games.

### Diagrams

Here is a diagram that illustrates the concept of Nash equilibrium:

```markdown
+---------------+
| Player 1 |
+---------------+
| Strategy |
| A, B, C,... |
+---------------+
| Payoff Matrix |
| u(A,B), u(A,C),... |
+---------------+
| Nash Equilibrium|
| s, c |
+---------------+
```

In this diagram, the player is represented by a box, the strategy is represented by a set of arrows, the payoff matrix is represented by a table, and the Nash equilibrium is represented by a pair of a strategy profile and a payoff vector.

### Case Studies

Here are a few case studies that illustrate the application of Nash equilibrium:

- **Oligopolistic Market**: Suppose two firms, Firm A and Firm B, are competing in a market for a particular product. The payoff matrix for this game is as follows:

|                        | Firm A increases price   | Firm A decreases price   |
| ---------------------- | ------------------------ | ------------------------ |
| Firm B increases price | Firm A: 100, Firm B: 100 | Firm A: 50, Firm B: 200  |
| Firm B decreases price | Firm A: 200, Firm B: 50  | Firm A: 100, Firm B: 100 |

The Nash equilibrium in this game is (Firm B decreases price, Firm A decreases price), where both firms decrease their prices, because if either of them increases their prices, the other firm can get a higher payoff.

- **International Relations**: Suppose two countries, Country A and Country B, are negotiating a trade agreement. The payoff matrix for this game is as follows:

|                             | Country A signs agreement      | Country A rejects agreement    |
| --------------------------- | ------------------------------ | ------------------------------ |
| Country B signs agreement   | Country A: 100, Country B: 100 | Country A: 50, Country B: 200  |
| Country B rejects agreement | Country A: 200, Country B: 50  | Country A: 100, Country B: 100 |

The Nash equilibrium in this game is (Country B rejects agreement, Country A rejects agreement), where both countries reject the agreement, because if either of them signs the agreement, the other country can get a higher payoff.

### Conclusion

The Nash equilibrium is a fundamental concept in game theory that describes a stable state in a game where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. It has been widely used in various fields, including economics, politics, computer science, and biology. The concept of Nash equilibrium has been extensively studied and has been applied to a wide range of problems.

### Further Reading

- Nash, J. F. (1950). Equilibrium points in n-person games. Proceedings of the National Academy of Sciences, 36(1), 48-49.
- von Neumann, J., & Morgenstern, O. (1944). Theory of Games and Economic Behavior. Princeton University Press.
- Aumann, R. J. (1974). Subjective probability and game theory. Mathematical Programming, 1(1), 1-18.
- Myerson, R. B. (1978). Nash Equilibrium in Infinite Games. Bell Journal of Economics, 9(2), 322-337.

Note: The above references are a selection of the most influential works on game theory and Nash equilibrium.
