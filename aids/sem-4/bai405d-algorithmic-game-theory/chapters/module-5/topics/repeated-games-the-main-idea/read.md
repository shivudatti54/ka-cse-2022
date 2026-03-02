# Repeated Games: The Main Idea

### Introduction

Repeated games are a fundamental concept in Algorithmic Game Theory, which studies the strategic interactions between players in a sequential decision-making process. In this topic, we will explore the main idea of repeated games, including their definition, types, and key concepts.

### Definition and Overview

A repeated game is a game played multiple times over a finite horizon, where each player makes decisions based on the payoffs from previous periods. The main idea is to analyze the behavior of players when they have multiple opportunities to make decisions and can adjust their strategies accordingly.

### Types of Repeated Games

There are several types of repeated games, including:

- **Zero-Sum Repeated Games**: In these games, one player's gain is equal to the other player's loss. Examples include prisoner's dilemma and hawk-dove games.
- **Non-Zero-Sum Repeated Games**: In these games, the payoffs are not necessarily zero-sum. Examples include auctions and bargaining games.
- **Finite Horizon Repeated Games**: In these games, the number of periods is finite, and the game ends after a fixed number of periods.
- **Infinite Horizon Repeated Games**: In these games, the number of periods is infinite, and the game continues indefinitely.

### Key Concepts

Here are some key concepts related to repeated games:

- **Strategic Subgame Perfect Equilibrium (SSPE)**: A Nash equilibrium that is also a subgame perfect equilibrium, where no player can improve their payoff by unilaterally deviating from their strategy, given the strategies of the other players.
- **Best Response**: The action that maximizes the payoff for a player, given the actions of the other players.
- **Pareto Optimality**: A state where no player can improve their payoff without worsening the payoff of another player.
- **Prisoner's Dilemma**: A classic game where two prisoners have to decide whether to cooperate or defect, with optimal outcomes depending on the actions of the other prisoner.

### Example: Prisoner's Dilemma

The prisoner's dilemma is a classic game that illustrates the concept of repeated games. Two prisoners, A and B, are arrested and interrogated separately. Each prisoner has two options: to confess (C) or to remain silent (S). The payoffs are as follows:

|                                 | Prisoner B stays silent (S) | Prisoner B confesses (C) |
| ------------------------------- | --------------------------- | ------------------------ |
| **Prisoner A stays silent (S)** | A: 3 years, B: 3 years      | A: 10 years, B: 1 year   |
| **Prisoner A confesses (C)**    | A: 1 year, B: 10 years      | A: 5 years, B: 5 years   |

In this game, the optimal strategy for each prisoner is to confess, given that the other prisoner stays silent. However, if both prisoners confess, they both receive a worse outcome. This is an example of a repeated game where the optimal strategy depends on the actions of the other players.

### Conclusion

Repeated games are a fundamental concept in Algorithmic Game Theory, which studies the strategic interactions between players in a sequential decision-making process. Understanding the key concepts and types of repeated games is essential for analyzing the behavior of players in a wide range of applications, from economics and politics to computer science and biology.
