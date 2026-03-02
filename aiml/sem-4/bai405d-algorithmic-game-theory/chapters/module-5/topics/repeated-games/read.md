# Repeated Games

=====================================

## Introduction

---

Repeated games are a type of game where two or more players interact with each other over multiple rounds or periods. The term "repeated" emphasizes that the game is not played only once, but rather multiple times, often with a common stage game. This concept is crucial in algorithmic game theory, as it allows us to analyze strategic decision-making in situations where players have incomplete information and cannot observe their opponent's previous actions.

## Definition

---

A repeated game consists of the following components:

- **Stage game**: A single game played between two players, with each player making a strategy choice.
- **Common knowledge**: Players assume that the game is repeated multiple times, and that the opponent's strategy will be chosen at each stage.
- **Perfect information**: Players have complete knowledge of the game's rules, their opponent's strategy, and the payoffs associated with each possible action.

## Key Concepts

---

- **Nash Equilibrium**: A stable state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged.
- **Reputation**: A player's perceived character or track record, which influences their opponent's strategy choice.
- **Signaling**: A situation where a player transmits information to their opponent through their actions, which can affect the opponent's strategy choice.

### Types of Repeated Games

- **Finite Horizon Game**: A repeated game with a finite number of stages.
- **Infinite Horizon Game**: A repeated game with an infinite number of stages.
- **Zero-Sum Game**: A repeated game where one player's gain is equal to the other player's loss.

## Equilibrium in Repeated Games

---

### Nash Equilibrium in Repeated Games

In a repeated game, a Nash equilibrium occurs when no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. This can lead to multiple equilibria, depending on the game's structure and the number of stages.

### Repetition and the Nash Equilibrium

Repetition in a repeated game can lead to a Nash equilibrium, where players choose strategies that are optimal given the opponent's previous actions. However, if the game is repeated indefinitely, the Nash equilibrium may not be stable, as players can adjust their strategies to take advantage of their opponent's past behavior.

## Signaling and Reputation

---

Signaling is an important aspect of repeated games, as players can use their actions to communicate information to their opponent. This can influence their opponent's strategy choice, potentially leading to a more stable equilibrium.

- **Signaling**: A situation where a player transmits information to their opponent through their actions.
- **Reputation**: A player's perceived character or track record, which influences their opponent's strategy choice.

## Example: Prisoner's Dilemma

---

The Prisoner's Dilemma is a classic example of a repeated game. Two prisoners are given the opportunity to confess or remain silent. If both prisoners confess, they receive a moderate sentence. If one prisoner confesses and the other remains silent, the confessor receives a light sentence, while the silent prisoner receives a harsh sentence. If both prisoners remain silent, they receive a light sentence.

In this game, the Nash equilibrium is for both prisoners to confess. However, if the game is repeated, the prisoners may be able to improve their payoffs by cooperating and remaining silent.

### Solution to the Prisoner's Dilemma

One solution to the Prisoner's Dilemma is the **Prisoner's Dilemma Solution**, where both prisoners choose a strategy that maximizes their expected payoff.

- **Prisoner's Dilemma Solution**: A strategy where both prisoners choose to remain silent.

## Conclusion

---

Repeated games are a powerful tool for analyzing strategic decision-making in algorithmic game theory. By understanding the key concepts, including Nash equilibrium, repetition, signaling, and reputation, we can better analyze the behavior of players in repeated games. The Prisoner's Dilemma is a classic example of a repeated game, highlighting the importance of cooperation and communication in achieving a more stable outcome.
