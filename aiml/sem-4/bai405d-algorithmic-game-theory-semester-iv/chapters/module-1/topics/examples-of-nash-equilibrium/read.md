Of course. Here is a comprehensive educational note on "Examples of Nash Equilibrium" tailored for  engineering students, formatted in Markdown.

---

# **Module 1: Examples of Nash Equilibrium**

**Course:** Algorithmic Game Theory (Semester IV)

## **1. Introduction**

In non-cooperative game theory, a **Nash Equilibrium (NE)** is a fundamental solution concept. It describes a stable state in a strategic game where no player can unilaterally change their strategy to achieve a better payoff, assuming all other players keep their strategies unchanged. In simpler terms, it's a set of strategies where everyone is making the best possible decision they can, given the decisions everyone else is making. This module provides a clear understanding of NE through practical examples.

## **2. Core Concepts: Revisiting the Definition**

Formally, a Nash Equilibrium is defined as:

*   In a game with `n` players, a strategy profile (s₁*, s₂*, ..., sₙ*) constitutes a Nash Equilibrium if for every player `i`:
    **uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*)** for every possible strategy `sᵢ` available to player `i`.

Where:
*   `sᵢ*` is the equilibrium strategy of player `i`.
*   `s₋ᵢ*` represents the strategies of all other players *except* `i` at equilibrium.
*   `uᵢ` is the payoff (or utility) function for player `i`.

This means that player `i` has no incentive to deviate from `sᵢ*` because no other strategy would yield a higher payoff, given what the others are doing.

## **3. Illustrative Examples**

### **Example 1: The Prisoner's Dilemma**

This is the classic example used to introduce Nash Equilibrium.

*   **Scenario:** Two criminals are arrested and held in separate cells. They cannot communicate. The prosecutor offers each a deal.
*   **Strategies:** Each player has two choices: **Cooperate (C)** (stay silent) or **Defect (D)** (betray the other).

The payoff matrix is as follows (values represent years in prison, so a *higher* number is *worse*):

| | **Prisoner B: Cooperate (C)** | **Prisoner B: Defect (D)** |
| :--- | :---: | :---: |
| **Prisoner A: Cooperate (C)** | (-1, -1) | (-10, 0) |
| **Prisoner A: Defect (D)** | (0, -10) | (-5, -5) |

*   **Analysis:** Let's find the Nash Equilibrium.
    *   If A thinks B will Cooperate (C), A's best response is to Defect (D) (0 > -1).
    *   If A thinks B will Defect (D), A's best response is still to Defect (D) (-5 > -10).
    *   The same logic holds symmetrically for Player B.
*   **Conclusion:** The strategy profile **(Defect, Defect)** is the **only Nash Equilibrium**, yielding (-5, -5). Even though both players would be better off with (-1, -1) if they both cooperated, the incentive to betray the other is too strong. This highlights that an NE is not necessarily the best overall outcome (it is not *Pareto efficient*).

### **Example 2: The Battle of the Sexes**

This game models a coordination game with two possible equilibria.

*   **Scenario:** A couple wants to spend the evening together but has different preferences on the activity: one prefers Football (F), the other prefers Opera (O).
*   **Strategies:** Go to the **Football (F)** game or go to the **Opera (O)**.

The payoff matrix (higher is better):

| | **Partner 2: Football (F)** | **Partner 2: Opera (O)** |
| :--- | :---: | :---: |
| **Partner 1: Football (F)** | (3, 2) | (0, 0) |
| **Partner 1: Opera (O)** | (0, 0) | (2, 3) |

*   **Analysis:**
    *   If Partner 2 goes to Football (F), Partner 1's best response is to also go to Football (F) (3 > 0).
    *   If Partner 2 goes to Opera (O), Partner 1's best response is to also go to Opera (O) (2 > 0).
    *   The same logic applies for Partner 2.
*   **Conclusion:** This game has **two pure-strategy Nash Equilibria**: **(Football, Football)** and **(Opera, Opera)**. There is no dominant strategy. The challenge becomes *which* equilibrium to coordinate on, a common problem in network and routing games studied in computer science.

### **Example 3: Matching Pennies (A Zero-Sum Game)**

This is a classic example of a game with **no pure-strategy Nash Equilibrium**.

*   **Scenario:** Two players each choose to show Heads (H) or Tails (T). Player 1 wins if they match; Player 2 wins if they do not.
*   **Strategies:** Choose **Heads (H)** or **Tails (T)**.

Payoff matrix (points won by Player 1; Player 2's payoff is the negative):

| | **Player 2: Heads (H)** | **Player 2: Tails (T)** |
| :--- | :---: | :---: |
| **Player 1: Heads (H)** | (+1, -1) | (-1, +1) |
| **Player 1: Tails (T)** | (-1, +1) | (+1, -1) |

*   **Analysis:** Check every strategy profile:
    *   (H, H): Player 2 would deviate to T for a better payoff.
    *   (H, T): Player 1 would deviate to T for a better payoff.
    *   (T, H): Player 1 would deviate to H for a better payoff.
    *   (T, T): Player 2 would deviate to H for a better payoff.
*   **Conclusion:** There is **no pure-strategy Nash Equilibrium**; no stable outcome exists where no player wants to change. However, a **mixed-strategy Nash Equilibrium** does exist, where each player randomizes their choice (e.g., plays H or T with 50% probability each).

## **4. Key Points & Summary**

| Key Point | Description |
| :--- | :--- |
| **Definition** | A stable state where no player can benefit by unilaterally changing their strategy. |
| **Not Always Optimal** | NE does not guarantee the best collective outcome (e.g., Prisoner's Dilemma). |
| **Uniqueness** | A game can have **zero** (Matching Pennies), **one** (Prisoner's Dilemma), or **multiple** (Battle of the Sexes) Nash Equilibria. |
| **Pure vs. Mixed** | A **Pure Strategy NE** uses a specific action. A **Mixed Strategy NE** uses a probability distribution over actions (guaranteed to exist by Nash's Theorem). |
| **Algorithmic Importance** | Finding Nash Equilibria is a core computational problem. Its complexity (being PPAD-complete for general games) is a key topic in Algorithmic Game Theory. |

---