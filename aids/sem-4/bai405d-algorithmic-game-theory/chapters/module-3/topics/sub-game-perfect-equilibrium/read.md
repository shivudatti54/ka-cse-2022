# Sub-Game Perfect Equilibrium

=====================================

## Introduction

---

Sub-game perfect equilibrium is a concept in game theory that extends the idea of Nash equilibrium to situations where there are multiple sub-games or sub-sets of players. This concept is particularly useful in situations where the game is divided into smaller, independent sub-games, and the players' actions in one sub-game do not affect the outcome of the other sub-games.

## Definition

---

Sub-game perfect equilibrium is defined as a strategy profile where no player can improve their payoff by unilaterally changing their strategy, given the strategies of the other players.

### Formal Definition

Let G = (N, S, T, u) be a game, where:

- N is the set of players
- S is the set of strategies for each player
- T is the transition function that specifies the next stage of the game given the current state and the actions taken by the players
- u is the payoff function that specifies the payoff for each player given their strategy and the actions taken by the other players

A sub-game perfect equilibrium is a strategy profile π = (π1, ..., πn) where for each sub-game G' = (N', S', T', u'), the following holds:

- No player can improve their payoff by unilaterally changing their strategy in G'
- The players' actions in one sub-game do not affect the outcome of the other sub-games

## Key Concepts

---

- **Sub-game**: A sub-game is a subset of the original game, where the players' actions in one sub-game do not affect the outcome of the other sub-games.
- **Independent sub-games**: A set of sub-games is said to be independent if the players' actions in one sub-game do not affect the outcome of the other sub-games.
- **Nash equilibrium**: A strategy profile where no player can improve their payoff by unilaterally changing their strategy, given the strategies of the other players.
- **Perfect equilibrium**: A strategy profile where no player can improve their payoff by unilaterally changing their strategy, given the strategies of the other players, and the players' actions in one sub-game do not affect the outcome of the other sub-games.

## Examples

---

### Example 1: Two Players

Consider a game with two players, Alice and Bob, who play a two-stage game. In the first stage, Alice chooses between two strategies, A or B, and in the second stage, Bob chooses between two strategies, X or Y, based on Alice's choice. The payoff function is as follows:

|                      | Bob's Strategy (X) | Bob's Strategy (Y) |
| -------------------- | ------------------ | ------------------ |
| Alice's Strategy (A) | (2, 2)             | (3, 1)             |
| Alice's Strategy (B) | (1, 3)             | (0, 4)             |

The sub-game perfect equilibrium is the strategy profile where Alice chooses strategy A and Bob chooses strategy X. This is because, given the strategies of the other player, Alice cannot improve her payoff by unilaterally changing her strategy, and the same applies to Bob.

### Example 2: Multiple Players

Consider a game with three players, Alice, Bob, and Charlie, who play a three-stage game. In the first stage, Alice and Bob choose between two strategies, A or B, and in the second stage, Charlie chooses between two strategies, X or Y, based on Alice's and Bob's choices. In the third stage, the players' actions are determined by the outcomes of the previous stages. The payoff function is as follows:

|                                             | Charlie's Strategy (X) | Charlie's Strategy (Y) |
| ------------------------------------------- | ---------------------- | ---------------------- |
| Alice's Strategy (A) and Bob's Strategy (A) | (4, 4, 4)              | (2, 2, 2)              |
| Alice's Strategy (B) and Bob's Strategy (B) | (2, 2, 2)              | (0, 0, 0)              |
| Alice's Strategy (A) and Bob's Strategy (B) | (1, 1, 1)              | (3, 3, 3)              |
| Alice's Strategy (B) and Bob's Strategy (A) | (3, 3, 3)              | (1, 1, 1)              |

The sub-game perfect equilibrium is the strategy profile where Alice and Bob both choose strategy A, and Charlie chooses strategy X. This is because, given the strategies of the other players, Alice and Bob cannot improve their payoff by unilaterally changing their strategy, and the same applies to Charlie.

## Conclusion

---

Sub-game perfect equilibrium is a concept in game theory that extends the idea of Nash equilibrium to situations where there are multiple sub-games or sub-sets of players. This concept is useful in situations where the game is divided into smaller, independent sub-games, and the players' actions in one sub-game do not affect the outcome of the other sub-games. The key concepts of sub-game perfect equilibrium include sub-games, independent sub-games, Nash equilibrium, and perfect equilibrium. The examples provided demonstrate how to apply the concept of sub-game perfect equilibrium to real-world games.
