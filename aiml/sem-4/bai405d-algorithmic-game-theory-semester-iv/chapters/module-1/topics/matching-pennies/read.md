Of course. Here is a comprehensive educational note on "Matching Pennies" for  Engineering students, formatted as requested.

# Module 1: Matching Pennies - A Zero-Sum Game

## 1. Introduction

In the study of Algorithmic Game Theory, we often begin with simple games that illustrate foundational concepts. **Matching Pennies** is one such classic, two-player, strategic game. It serves as a perfect model for a **strictly competitive** or **zero-sum game**, where one player's gain is exactly equal to the other player's loss. Its simplicity makes it an excellent tool for understanding core ideas like pure and mixed strategies, the concept of a **Nash Equilibrium**, and why such an equilibrium doesn't always exist in pure strategies.

## 2. Core Concepts Explained

### The Game Setup
*   **Players:** Two players, often called Player 1 (Row) and Player 2 (Column).
*   **Actions/Strategies:** Each player has two possible moves: show **Heads (H)** or show **Tails (T)**.
*   **Objective:** The players simultaneously choose and reveal their move. The payoff depends on whether the choices match.
    *   Player 1 wins if the pennies **match** (both Heads or both Tails).
    *   Player 2 wins if the pennies **do not match** (one Heads, one Tails).

This creates a direct conflict of interest, defining it as a zero-sum game.

### Payoff Matrix Representation
The game is best represented by a payoff matrix. By convention, the payoff values in the cells are `(a, b)`, where:
*   `a` is the payoff for the row player (Player 1).
*   `b` is the payoff for the column player (Player 2).

Since it's a zero-sum game, we can simplify the matrix by noting that `b = -a`. A common representation uses +1 for a win and -1 for a loss.

|                       | Player 2: Heads | Player 2: Tails |
| :-------------------- | :-------------: | :-------------: |
| **Player 1: Heads**   |    (+1, -1)     |    (-1, +1)     |
| **Player 1: Tails**   |    (-1, +1)     |    (+1, -1)     |

**Interpretation:**
*   The cell (Heads, Heads): Pennies match. Player 1 wins (+1), Player 2 loses (-1).
*   The cell (Heads, Tails): Pennies do not match. Player 1 loses (-1), Player 2 wins (+1).
*   The cell (Tails, Heads): Pennies do not match. Player 1 loses (-1), Player 2 wins (+1).
*   The cell (Tails, Tails): Pennies match. Player 1 wins (+1), Player 2 loses (-1).

### Lack of Pure Strategy Nash Equilibrium
A **Nash Equilibrium (NE)** is a set of strategies where no player can benefit by unilaterally changing their strategy, given the other player's strategy remains the same.

Let's see if Matching Pennies has a pure strategy NE (where players choose a single action with 100% probability):
*   If Player 1 chooses Heads, Player 2's best response is Tails (to win).
*   If Player 2 chooses Tails, Player 1's best response is Tails (to win).
*   If Player 1 chooses Tails, Player 2's best response is Heads.
*   If Player 2 chooses Heads, Player 1's best response is Heads.

There is **no stable outcome** where both players are playing a best response to each other's pure strategy. Each player always has an incentive to change their move to beat the opponent. Therefore, **no pure strategy Nash equilibrium exists**.

### Mixed Strategy Nash Equilibrium
Since no pure strategy works, players must randomize their actions to become unpredictable. This is a **mixed strategy**.

*   **Mixed Strategy:** A strategy where a player chooses among their pure strategies according to a probability distribution.
*   **Goal:** Choose a probability that makes the opponent **indifferent** between their own pure strategies. This means the opponent's expected payoff is the same no matter what pure strategy they choose, removing any incentive to exploit a predictable pattern.

**Calculating the Mixed Strategy NE:**
Let:
*   `p` = probability that Player 1 chooses Heads. Then, (1 - `p`) is the probability he chooses Tails.
*   `q` = probability that Player 2 chooses Heads. Then, (1 - `q`) is the probability he chooses Tails.

Player 2 wants to make Player 1 indifferent between playing Heads and Tails.
*   **Expected Payoff for Player 1 if he plays Heads:**
    `E1(H) = (q)(+1) + (1 - q)(-1) = 2q - 1`
*   **Expected Payoff for Player 1 if he plays Tails:**
    `E1(T) = (q)(-1) + (1 - q)(+1) = 1 - 2q`

To make Player 1 indifferent: `E1(H) = E1(T)`
`2q - 1 = 1 - 2q`
`4q = 2`
`q = 1/2`

Player 1 wants to make Player 2 indifferent between playing Heads and Tails.
*   **Expected Payoff for Player 2 if he plays Heads:**
    `E2(H) = (p)(-1) + (1 - p)(+1) = 1 - 2p`
*   **Expected Payoff for Player 2 if he plays Tails:**
    `E2(T) = (p)(+1) + (1 - p)(-1) = 2p - 1`

To make Player 2 indifferent: `E2(H) = E2(T)`
`1 - 2p = 2p - 1`
`4p = 2`
`p = 1/2`

**The Mixed Strategy Nash Equilibrium** is for both players to randomize perfectly: each player chooses Heads with a probability of **1/2** and Tails with a probability of **1/2**.

## 3. Example
Imagine this as a simplified security game:
*   **Player 1 (Attacker)** wants to breach a system through Port A (Heads) or Port B (Tails).
*   **Player 2 (Defender)** must choose which port to defend.
*   The Attacker wins if they attack an undefended port (a match, as the defender guessed wrong).
*   The Defender wins if they defend the port being attacked (a mismatch).

The only sustainable strategy is for both to randomize their choices perfectly. Any predictable pattern (e.g., the defender always protecting Port A) can be exploited by the attacker.

## 4. Key Points & Summary

*   **Definition:** Matching Pennies is a two-player, zero-sum game with no pure strategy Nash Equilibrium.
*   **Core Concept:** The game is inherently adversarial, with players' interests diametrically opposed.
*   **Nash Equilibrium:** An equilibrium **does not exist in pure strategies**. The only Nash Equilibrium is in **mixed strategies**.
*   **Mixed Strategy Solution:** Both players must randomize their moves, choosing each action with a probability of **0.5** to make the opponent indifferent and to avoid being predictable.
*   **Significance:** It is a foundational model for understanding conflicts of interest, randomization in strategic settings, and the application of mixed strategies, which are crucial in fields like cybersecurity, economics, and randomized algorithms.