# Finding Sub-Game Perfect Equilibria of Finite Horizon Games: Backward Induction

## Abstract

This document provides a comprehensive overview of finding sub-game perfect equilibria in finite horizon games using backward induction. We will delve into the historical context, theoretical foundations, and practical applications of this powerful game theory concept.

## Historical Context

The concept of backward induction was first introduced by John von Neumann and Oskar Morgenstern in their seminal book "Theory of Games and Economic Behavior" (1944). However, it was not until the 1950s and 1960s that the concept gained significant attention in the field of game theory.

In the 1950s, Alan Turing published a series of papers on the topic of formal systems and the reducibility of decision problems. One of his papers, "On Computable Numbers" (1936), laid the foundation for the development of computer-assisted solutions to game theory problems.

The 1960s saw the rise of dynamic programming, which provided a mathematical framework for solving problems with multiple stages and uncertain outcomes. Donald Blackwell's paper "Theories of Games of Chances" (1956) is a seminal work in this area.

## Modern Developments

In recent years, the field of game theory has experienced significant advancements in the development of computational algorithms for solving finite horizon games. Some notable contributions include:

1. **Computationally efficient algorithms**: Researchers have developed efficient algorithms for solving finite horizon games, such as the "Forward-Induction Algorithm" (FIA) and the "Dynamic Programming Algorithm" (DPA).
2. **Machine learning applications**: The application of machine learning techniques, such as reinforcement learning and deep reinforcement learning, has led to significant improvements in the solution of finite horizon games.
3. **Real-world applications**: The development of computational algorithms for solving finite horizon games has led to numerous real-world applications in fields such as finance, economics, and computer science.

## Theoretical Foundations

A finite horizon game is a two-player game where each player has a finite number of stages or periods to make decisions. The objective of the game is to maximize the payoff or utility over the entire horizon.

**Game Theory Framework**

A finite horizon game can be modeled using a game theory framework, which consists of the following components:

1. **Strategies**: A set of actions or choices that each player can take.
2. **Payoffs**: A set of numerical values that each player receives for each possible combination of strategies.
3. **Game tree**: A tree-like structure that represents the possible sequences of events and payoffs.

**Backward Induction**

Backward induction is a technique for solving finite horizon games by working backwards from the last stage to the first stage. The basic idea is to assume that the players will make rational decisions at each stage, and then use this assumption to derive the optimal strategy for each stage.

**Formulating the Problem**

The problem of finding a sub-game perfect equilibrium can be formulated as follows:

1. **Stage 1**: Each player chooses a strategy from the set of available strategies.
2. **Stage 2**: Each player observes the outcome of the previous stage and chooses a strategy from the set of available strategies.
3. **Stage 3**: Each player observes the outcome of the previous stages and chooses a strategy from the set of available strategies.
4. **...**
5. **Stage n**: Each player observes the outcome of all previous stages and chooses a strategy from the set of available strategies.

**Finding the Sub-Game Perfect Equilibrium**

The sub-game perfect equilibrium can be found using the following steps:

1. **Work backwards**: Start from the last stage and work backwards to the first stage.
2. **Derive the optimal strategy**: At each stage, derive the optimal strategy by assuming that the players will make rational decisions.
3. **Combine the strategies**: Combine the optimal strategies from each stage to obtain the overall strategy.

**Example**

Consider a simple finite horizon game with two players, Alice and Bob. The game has two stages, and the payoffs are as follows:

|                      | Alice's Strategy 1 | Alice's Strategy 2 |
| -------------------- | ------------------ | ------------------ |
| **Bob's Strategy 1** | (0, 0)             | (5, 0)             |
| **Bob's Strategy 2** | (0, 5)             | (10, 0)            |

We want to find the sub-game perfect equilibrium. By working backwards from the last stage, we can derive the optimal strategy for Alice:

- At stage 2, Alice's optimal strategy is to choose Strategy 1 if Bob chooses Strategy 1, and Strategy 2 if Bob chooses Strategy 2.
- At stage 1, Alice's optimal strategy is to choose Strategy 1 if Bob chooses Strategy 1.

By combining the optimal strategies from each stage, we obtain the overall strategy:

- Alice chooses Strategy 1 if Bob chooses Strategy 1, and Strategy 2 if Bob chooses Strategy 2.

The sub-game perfect equilibrium is (1, 1), where Alice and Bob both choose Strategy 1.

## Applications

Backward induction has numerous applications in various fields, including:

1. **Finance**: Backward induction can be used to model and solve problems in finance, such as investment and portfolio management.
2. **Economics**: Backward induction can be used to model and solve problems in economics, such as market equilibrium and optimal policy.
3. **Computer Science**: Backward induction can be used to model and solve problems in computer science, such as decision-making and optimization.

## Case Studies

1. **The Prisoner's Dilemma**

The Prisoner's Dilemma is a classic game theory problem that illustrates the use of backward induction. The problem is as follows:

|                           | Prisoner 1 Cooperates | Prisoner 1 Defects |
| ------------------------- | --------------------- | ------------------ |
| **Prisoner 2 Cooperates** | (3, 3)                | (0, 5)             |
| **Prisoner 2 Defects**    | (5, 0)                | (1, 1)             |

Using backward induction, we can derive the optimal strategy for each prisoner, and obtain the sub-game perfect equilibrium (1, 1).

2. **The Monty Hall Problem**

The Monty Hall Problem is a classic probability problem that illustrates the use of backward induction. The problem is as follows:

|                 | Monty Reveal Door 1 | Monty Reveal Door 2 |
| --------------- | ------------------- | ------------------- |
| **Your Choice** | (1/3, 1/3)          | (1/3, 1/3)          |

Using backward induction, we can derive the optimal strategy for the contestant, and obtain the sub-game perfect equilibrium (1/3, 1/3).

## Conclusion

Backward induction is a powerful technique for solving finite horizon games and finding sub-game perfect equilibria. By working backwards from the last stage to the first stage, we can derive the optimal strategy for each player, and obtain the overall strategy. Backward induction has numerous applications in various fields, including finance, economics, and computer science.

## Further Reading

- **Von Neumann, J., & Morgenstern, O. (1944). Theory of Games and Economic Behavior.** Princeton University Press.
- **Blackwell, D. (1956). Theories of Games of Chances.** Annals of Mathematics, 64(1), 1-67.
- **Myerson, R. B. (1978). Large Games: Analysis of Optimal Strategies and Their Computation.** Wiley.
- **Fudenberg, D., & Tirole, J. (1991). Game Theory.** MIT Press.
- **Aumann, R. J., & Mas-Colell, A. (2000). Game Theory.** Elsevier.

## Diagrams

Here is a diagram illustrating the stages of a finite horizon game:

```
         +---------------+
         |  Stage 1  |
         +---------------+
                  |
                  |
                  v
         +---------------+
         |  Stage 2  |
         +---------------+
                  |
                  |
                  v
         +---------------+
         |  Stage 3  |
         +---------------+
                  |
                  |
                  v
         +---------------+
         |  Stage n  |
         +---------------+
```

This diagram shows the possible stages of a finite horizon game, where each stage represents a decision point for the players. The players' strategies are determined by their observations of the previous stages, and the overall strategy is obtained by combining the optimal strategies from each stage.
