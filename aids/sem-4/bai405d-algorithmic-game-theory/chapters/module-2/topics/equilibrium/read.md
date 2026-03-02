# Equilibrium

## Table of Contents

- [Introduction](#introduction)
- [Defining Equilibrium](#defining-equilibrium)
- [Types of Equilibrium](#types-of-equilibrium)
- [Nash Equilibrium](#nash-equilibrium)
- [Mixed Strategy Nash Equilibrium](#mixed-strategy-nash-equilibrium)
- [Examples and Applications](#examples-and-applications)

## Introduction

In algorithmic game theory, equilibrium refers to a state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. This concept is crucial in understanding the behavior of players in strategic games, where players make decisions based on the actions of others.

## Defining Equilibrium

An equilibrium is a state where:

- No player can improve their payoff by changing their strategy.
- All players are playing their best response to the strategies of the other players.

## Types of Equilibrium

There are two main types of equilibrium:

- **Pareto Equilibrium**: A state where no player can improve their payoff without making another player worse off.
- **Nash Equilibrium**: A state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged.

## Nash Equilibrium

A Nash Equilibrium is a strategic concept that was introduced by John Nash in the 1950s. It states that:

- No player can improve their payoff by changing their strategy, assuming all other players keep their strategies unchanged.
- All players are playing their best response to the strategies of the other players.

Example:

Suppose two players, Alice and Bob, play a game where they simultaneously decide whether to choose option A or option B. The payoffs are as follows:

| Alice | Bob | Payoff |
| ----- | --- | ------ |
| A     | A   | 10     |
| A     | B   | 8      |
| B     | A   | 9      |
| B     | B   | 6      |

The Nash Equilibrium in this game is (A, A), where both Alice and Bob choose option A, because neither can improve their payoff by changing their strategy.

## Mixed Strategy Nash Equilibrium

A Mixed Strategy Nash Equilibrium is a refinement of the Nash Equilibrium concept. It states that:

- No player can improve their payoff by changing their strategy, assuming all other players keep their strategies unchanged.
- All players are playing a mixed strategy, which means they have a probability distribution over their possible actions.

Example:

Suppose two players, Alice and Bob, play a game where they simultaneously decide whether to choose option A or option B. The payoffs are as follows:

| Alice | Bob | Payoff |
| ----- | --- | ------ |
| A     | A   | 10     |
| A     | B   | 8      |
| B     | A   | 9      |
| B     | B   | 6      |

A Mixed Strategy Nash Equilibrium in this game is a strategy where Alice chooses option A with probability 1/2 and option B with probability 1/2, and Bob chooses option A with probability 2/3 and option B with probability 1/3.

## Examples and Applications

Equilibrium has many applications in algorithmic game theory, including:

- **Bargaining games**: Where players negotiate over a division of resources.
- **Auction games**: Where players bid on a good or service.
- **Election games**: Where players vote for a candidate.

In conclusion, equilibrium is a fundamental concept in algorithmic game theory that helps us understand the behavior of players in strategic games. By understanding equilibrium, we can develop strategies that maximize payoffs and minimize losses.
