# Nash Equilibrium Payoffs of an Infinitely Repeated Prisoner’s Dilemma

## **Introduction**

The Prisoner's Dilemma is a fundamental game theory concept that has been extensively studied in the field of competitive games. It was first introduced by Merrill Flood and Melvin Dresher in 1950, and later popularized by Albert Tucker. The game is a straightforward one: two players, typically referred to as Prisoners A and B, are arrested and interrogated separately by the police. Each Prisoner has two options: to confess (C) or remain silent (S). The payoffs for each possible combination of actions are as follows:

|                                 | Prisoner B Stays Silent (S) | Prisoner B Confesses (C) |
| ------------------------------- | --------------------------- | ------------------------ |
| **Prisoner A Stays Silent (S)** | A: 3, B: 3                  | A: 0, B: 5               |
| **Prisoner A Confesses (C)**    | A: 5, B: 0                  | A: 1, B: 1               |

The Nash Equilibrium concept is a crucial tool in understanding the behavior of players in a game. It is a state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. In this paper, we will explore the Nash Equilibrium payoffs of an infinitely repeated Prisoner’s dilemma.

## **Historical Context**

The Prisoner's Dilemma was first introduced by Merrill Flood and Melvin Dresher in 1950. They used a simplified version of the game to demonstrate the tension between individual and group rationality. Later, Albert Tucker popularized the game by introducing the concept of a Nash Equilibrium.

The Prisoner's Dilemma has been extensively studied in the field of game theory, and has been applied to various fields, including economics, politics, and biology. It has also been the subject of numerous experiments and simulations.

## **Infinitely Repeated Prisoner’s Dilemma**

In the infinitely repeated Prisoner’s dilemma, the game is repeated an infinite number of times. This means that the players will face many rounds of the game, and will have the opportunity to learn from their past experiences.

Let's consider a simple example to illustrate the infinitely repeated Prisoner’s dilemma. Suppose we have two players, Alice and Bob. They will play the game many times, and will receive the following payoffs:

|                            | Bob Stays Silent (S) | Bob Confesses (C) |
| -------------------------- | -------------------- | ----------------- |
| **Alice Stays Silent (S)** | Alice: 3, Bob: 3     | Alice: 0, Bob: 5  |
| **Alice Confesses (C)**    | Alice: 5, Bob: 0     | Alice: 1, Bob: 1  |

In this example, if Alice and Bob both stay silent, they both receive a payoff of 3. If Alice confesses and Bob stays silent, Alice receives a payoff of 5, while Bob receives a payoff of 0. Similarly, if Alice stays silent and Bob confesses, Alice receives a payoff of 0, while Bob receives a payoff of 5.

## **Nash Equilibrium**

The Nash Equilibrium is a state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged.

In the infinitely repeated Prisoner’s dilemma, the Nash Equilibrium occurs when both players defect (i.e., confess). This is because if both players defect, they both receive a payoff of 1, which is better than the payoff of 0 that they would receive if they both stayed silent.

However, if one player defects and the other stays silent, the silent player receives a payoff of 5, which is better than the payoff of 1 that they would receive if they both defected. Therefore, the silent player will stay silent, and the defecting player will defect.

## **Payoff Matrix**

The payoff matrix for the infinitely repeated Prisoner’s dilemma can be represented as follows:

|                            | Bob Stays Silent (S) | Bob Confesses (C) |
| -------------------------- | -------------------- | ----------------- |
| **Alice Stays Silent (S)** | Alice: 3, Bob: 3     | Alice: 0, Bob: 5  |
| **Alice Confesses (C)**    | Alice: 5, Bob: 0     | Alice: 1, Bob: 1  |

The Nash Equilibrium occurs at the bottom-right corner of the matrix, where both players defect (i.e., Bob confesses, and Alice confessions).

## **Dynamic Programming**

Dynamic programming is a method used to solve problems that involve multiple stages. In the context of the infinitely repeated Prisoner’s dilemma, dynamic programming can be used to find the optimal strategy for each player.

Let's define a function `V(A, B)` that represents the expected payoff for player A, given that player B has strategy `B`. The function `V(A, B)` can be defined recursively as follows:

`V(A, B) = max_{A'} [ A' V(B, A') + (1 - P(C|A, B)) V(S, A') + P(C|A, B) V(C, A') ]`

where `A'` is the strategy of player A, `B'` is the strategy of player B, `P(C|A, B)` is the probability of player A confessing given strategy `B`, and `V(S, A')` and `V(C, A')` are the expected payoffs for player A when playing strategy `S` and `C`, respectively.

## **Solving the Infinitely Repeated Prisoner’s Dilemma**

To solve the infinitely repeated Prisoner’s dilemma, we can use dynamic programming to find the optimal strategy for each player.

Let's define a function `V(A)` that represents the expected payoff for player A. The function `V(A)` can be defined recursively as follows:

`V(A) = max_{B'} [ B' V'(B') + (1 - P(C|A, B')) V(S, A) + P(C|A, B') V(C, A) ]`

where `B'` is the strategy of player B, `V'(B')` is the expected payoff for player B, and `V(S, A)` and `V(C, A)` are the expected payoffs for player A when playing strategy `S` and `C`, respectively.

## **Case Studies**

Here are a few case studies that illustrate the Nash Equilibrium payoffs of an infinitely repeated Prisoner’s dilemma:

- **Case Study 1:** Two prisoners, John and Mike, are arrested and interrogated separately by the police. They have two options: to confess (C) or remain silent (S). The payoffs for each possible combination of actions are as follows:
  | | Mike Stays Silent (S) | Mike Confesses (C) |
  | --- | --- | --- |
  | **John Stays Silent (S)** | John: 3, Mike: 3 | John: 0, Mike: 5 |
  | **John Confesses (C)** | John: 5, Mike: 0 | John: 1, Mike: 1 |
- **Case Study 2:** Two prisoners, Sarah and Tom, are arrested and interrogated separately by the police. They have two options: to confess (C) or remain silent (S). The payoffs for each possible combination of actions are as follows:
  | | Tom Stays Silent (S) | Tom Confesses (C) |
  | --- | --- | --- |
  | **Sarah Stays Silent (S)** | Sarah: 3, Tom: 3 | Sarah: 0, Tom: 5 |
  | **Sarah Confesses (C)** | Sarah: 5, Tom: 0 | Sarah: 1, Tom: 1 |

## **Applications**

The Nash Equilibrium payoffs of an infinitely repeated Prisoner’s dilemma have numerous applications in various fields, including:

- **Economics:** The Prisoner’s dilemma can be used to study the behavior of firms and individuals in a competitive market.
- **Politics:** The Prisoner’s dilemma can be used to study the behavior of politicians and policymakers in a competitive political environment.
- **Biology:** The Prisoner’s dilemma can be used to study the behavior of animals and insects in a competitive environment.

## **Further Reading**

Here are some resources for further reading on the Nash Equilibrium payoffs of an infinitely repeated Prisoner’s dilemma:

- **"Prisoner's Dilemma" by Merrill Flood and Melvin Dresher:** This paper introduces the Prisoner’s dilemma and its variants.
- **"The Nash Equilibrium" by Albert Tucker:** This paper introduces the concept of the Nash Equilibrium and its application to the Prisoner’s dilemma.
- **"Game Theory" by Robert Aumann and Robert Myerson:** This book provides a comprehensive introduction to game theory, including the Prisoner’s dilemma and the Nash Equilibrium.
- **"Prisoner's Dilemma" by David G. Roodman:** This paper provides a detailed analysis of the Prisoner’s dilemma and its variants.

## Conclusion

The Nash Equilibrium payoffs of an infinitely repeated Prisoner’s dilemma are a crucial concept in game theory. The Prisoner’s dilemma is a simple yet powerful game that illustrates the tension between individual and group rationality. The Nash Equilibrium payoffs of an infinitely repeated Prisoner’s dilemma can be used to study the behavior of players in a competitive environment, and have numerous applications in various fields, including economics, politics, and biology.
