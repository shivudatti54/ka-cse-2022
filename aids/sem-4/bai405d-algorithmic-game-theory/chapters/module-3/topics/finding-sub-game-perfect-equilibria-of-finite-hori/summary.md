# Finding Sub-Game Perfect Equilibria of Finite Horizon Games: Backward Induction

===========================================================

### Key Points

- **Definition:** Sub-game perfect equilibrium is a Nash equilibrium that holds in each sub-game (sub-game proper) of the original game.
- **Backward Induction (BI):** A method for finding the optimal strategy for each player in a finite horizon game.

### Important Formulas and Definitions

- ** backward induction formula:**
  ```
  V(S) = max_{x} [r(x) + β ∑[V(S')]]
  ```
  where V(S) is the value of the state S, r(x) is the payoff of action x, β is the discount factor, and S' are the successor states.
- **Bellman Equation:**
  ```
  V(S) = max_{x} [r(x) + β V(S')]
  ```
  where V(S) is the value of the state S, r(x) is the payoff of action x, and V(S') are the values of the successor states.
- **Sub-game Perfect Equilibrium (SGPE):** A Nash equilibrium that holds in each sub-game of the original game.

### Theorems and Important Concepts

- **Nash Equilibrium (NE):** A state where no player can improve their payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged.
- **Finite Horizon Game:** A game with a finite number of stages or periods.
- **Backward Induction Theorem:** In a finite horizon game, the optimal strategy for each player can be found by working backwards from the last stage to the first stage.

### Key Concepts to Remember

- Backward induction is a method for finding the optimal strategy in a finite horizon game.
- Sub-game perfect equilibrium is a Nash equilibrium that holds in each sub-game of the original game.
- The backward induction formula and Bellman equation are used to find the value of each state in the game.
