Of course. Here is a comprehensive educational note on "Introduction to Strategic Games" for  Engineering students, formatted as requested.

# Module 1: Introduction to Strategic Games

## 1. Introduction

Algorithmic Game Theory (AGT) sits at the fascinating intersection of computer science, economics, and mathematics. It studies the behavior of strategic agents in interactive settings and the algorithms that govern or analyze these situations. This module begins with the most fundamental model in game theory: the **Strategic Game** (or Normal-Form Game). It provides the foundation for analyzing scenarios where multiple decision-makers (players) interact, and each player's outcome depends not only on their own decision but also on the decisions of others.

## 2. Core Concepts

### What is a Strategic Game?

A strategic game is a model of interactive decision-making characterized by three key components:
1.  **Players:** A finite set of participants (e.g., `Player 1, Player 2, ..., Player n`).
2.  **Actions/Strategies:** Each player has a set of possible actions or strategies they can choose from. For example, a player's action set could be {`Cooperate`, `Defect`} or {`Up`, `Down`}.
3.  **Payoffs:** For each possible combination of actions—one for each player—a payoff (or utility) is defined for every player. Payoffs quantify the benefit a player receives from a particular outcome.

### Formal Definition

A strategic game with `n` players is defined by:
*   The set of players: $N = \{1, 2, ..., n\}$
*   For each player $i \in N$, a non-empty set of actions $A_i$
*   For each player $i \in N$, a payoff function $u_i : A_1 \times A_2 \times ... \times A_n \rightarrow \mathbb{R}$

The central problem in a strategic game is: **Given that all players are rational and want to maximize their own payoff, what action will each player choose?**

### Dominant Strategy

A strategy is a **dominant strategy** for a player if it yields a higher payoff than any other strategy, *regardless of what the other players do*. Formally, a strategy $s_i \in A_i$ is dominant for player `i` if:
$$u_i(s_i, a_{-i}) > u_i(s_i', a_{-i})$$
for every strategy $s_i' \neq s_i$ and for every possible combination of the other players' actions, denoted by $a_{-i}$.

If a player has a dominant strategy, a rational player will always choose it.

### Nash Equilibrium (NE)

The most crucial solution concept in game theory is the **Nash Equilibrium (NE)**, named after mathematician John Nash. It is a state where no player can unilaterally change their strategy to get a better payoff, given the strategies chosen by all other players.

Formally, a strategy profile $a^* = (a_1^*, a_2^*, ..., a_n^*)$ is a Nash Equilibrium if for every player $i \in N$,
$$u_i(a_i^*, a_{-i}^*) \geq u_i(a_i, a_{-i}^*)$$
for every action $a_i \in A_i$.

In simpler terms, in a NE, everyone is simultaneously making their best possible move, knowing the moves of everyone else. A game can have zero, one, or multiple Nash Equilibria.

## 3. Examples

### 1. Prisoner's Dilemma (The Classic Example)

**Scenario:** Two suspects are arrested. The prosecutors offer each a deal: testify against the other (**Defect**) or remain silent (**Cooperate**).

*   **Players:** Prisoner 1, Prisoner 2.
*   **Actions:** Each player's action set is {Cooperate, Defect}.
*   **Payoffs:** Represented as (Prisoner 1's payoff, Prisoner 2's payoff).

|                       | Prisoner 2: Cooperate | Prisoner 2: Defect |
| :-------------------- | :-------------------: | :----------------: |
| **Prisoner 1: Cooperate** |       (-1, -1)        |     (-3, 0)        |
| **Prisoner 1: Defect**    |       (0, -3)         |     (-2, -2)       |

**Analysis:**
*   **Dominant Strategy:** For each player, **Defecting** always gives a better payoff regardless of the other's choice. Defecting is a dominant strategy.
*   **Nash Equilibrium:** The strategy profile (Defect, Defect) with payoffs (-2, -2) is the only Nash Equilibrium. Even though (Cooperate, Cooperate) yields a better collective outcome (-1, -1), each player has an incentive to deviate unilaterally for a personal gain.

### 2. Coordination Game (Battle of the Sexes)

**Scenario:** A couple wants to spend the evening together but has different preferences: one prefers Football (F), the other prefers Opera (O).

*   **Players:** Partner 1, Partner 2.
*   **Actions:** {Football, Opera}.

|                    | Partner 2: Football | Partner 2: Opera |
| :----------------- | :-----------------: | :--------------: |
| **Partner 1: Football** |      (2, 1)         |     (0, 0)       |
| **Partner 1: Opera**    |      (0, 0)         |     (1, 2)       |

**Analysis:**
*   **Dominant Strategy:** Neither player has a dominant strategy. The best choice depends entirely on what the other does.
*   **Nash Equilibrium:** This game has **two pure-strategy Nash Equilibria**: (Football, Football) and (Opera, Opera). In both states, no single player would be better off by changing their action alone.

## 4. Key Points & Summary

*   **Strategic Form:** A game defined by players, actions, and payoffs. It is used to model one-shot interactions where players act simultaneously or without knowing others' choices.
*   **Rationality:** The core assumption is that players are rational and will act to maximize their own payoff.
*   **Dominant Strategy:** A powerful concept where one strategy is always best, simplifying the decision-making process.
*   **Nash Equilibrium (NE):** The central solution concept. It represents a stable state where no player has an incentive to deviate unilaterally. It is a consistent prediction of the outcome of a strategic game.
*   **AGT Perspective:** From an algorithmic viewpoint, we are interested in questions like: How do players compute their best response? Can we compute all Nash Equilibria efficiently? How do we design systems (auctions, networks) where strategic behavior leads to good outcomes? These questions form the basis of further study in AGT.