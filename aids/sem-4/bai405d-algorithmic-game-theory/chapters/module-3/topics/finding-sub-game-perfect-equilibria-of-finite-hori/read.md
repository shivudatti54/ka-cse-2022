# Finding Sub-Game Perfect Equilibria of Finite Horizon Games: Backward Induction

=====================================================

## Introduction

---

Backward induction is a powerful technique for finding sub-game perfect equilibria in finite horizon games. This method involves working backwards from the final stages of the game to determine the optimal strategy for each player at each stage.

## Definition of Backward Induction

---

Backward induction is a recursive procedure for finding the equilibrium strategies of a finite horizon game. It works by assuming that the game is divided into stages, and that the optimal strategy for each player at each stage is to choose the action that maximizes the expected payoff at that stage.

## The Backward Induction Procedure

---

1. **Identify the stages**: Divide the game into stages, where each stage represents a single decision period for the players.
2. **Determine the optimal action at the last stage**: At the last stage of the game, the players know the outcome of the game and can determine the optimal action to take.
3. **Work backwards to the first stage**: Starting from the last stage, work backwards to the first stage, assuming that the players have made optimal decisions at each stage.
4. **Repeat the process**: Continue working backwards until you reach the first stage, where the players make their first decision.

## Key Concepts

---

- **Sub-game perfect equilibrium**: A strategy profile that maximizes the expected payoff for each player, assuming that each player knows the strategies of the other players.
- **Backward induction tree**: A diagram that illustrates the recursive process of backward induction.
- **Transition probability**: The probability that a particular action will lead to a particular outcome.
- **Expected payoff**: The average payoff that a player can expect to receive from a particular action.

## Example

---

Suppose we have a two-player game with two stages. The players have the following strategies:

|          | Stage 1 | Stage 2 |
| -------- | ------- | ------- |
| Player 1 | A       | B       |
| Player 2 | C       | D       |

The transition probabilities are as follows:

|          | Stage 1        | Stage 2        |
| -------- | -------------- | -------------- |
| Player 1 | A: 0.6, B: 0.4 | B: 0.7, A: 0.3 |
| Player 2 | C: 0.4, D: 0.6 | D: 0.8, C: 0.2 |

Using backward induction, we can determine the optimal action for each player at each stage.

- **Stage 2**: Player 2 knows that Player 1 will choose action A with probability 0.6 and action B with probability 0.4. Player 2 wants to maximize their expected payoff, which is 10 when they choose action C and -5 when they choose action D. Therefore, Player 2 chooses action C.
- **Stage 1**: Player 1 knows that Player 2 will choose action C with probability 0.6 and action D with probability 0.4. Player 1 wants to maximize their expected payoff, which is 15 when they choose action A and -10 when they choose action B. Therefore, Player 1 chooses action A.

The resulting equilibrium strategy profile is (A, C), which can be found by following the backward induction tree:

```mermaid
graph LR
    A[Player 1 chooses A] --> B[Player 2 chooses C]
    B --> C[Player 1 chooses A]
```

## Code Implementation

---

Here is a Python implementation of the backward induction algorithm:

```python
def backward_induction(transitions, payoffs):
    # Initialize the number of stages
    n = len(payoffs)

    # Initialize the equilibrium strategy profile
    equilibrium_strategy = [[None for _ in range(len(payoffs))] for _ in range(n)]

    # Determine the optimal action at the last stage
    for i in range(n-1, -1, -1):
        for j in range(len(payoffs[i])):
            # Determine the optimal action for player i
            max_payoff = float('-inf')
            optimal_action = None
            for action in range(len(payoffs[i])):
                expected_payoff = 0
                for k in range(len(payoffs[i])):
                    expected_payoff += transitions[i][j][k] * payoffs[i][k]
                if expected_payoff > max_payoff:
                    max_payoff = expected_payoff
                    optimal_action = action

            # Update the equilibrium strategy profile
            equilibrium_strategy[i][j] = optimal_action

    return equilibrium_strategy

# Example usage
transitions = [
    [[0.6, 0.4], [0.7, 0.3]],
    [[0.4, 0.6], [0.8, 0.2]]
]
payoffs = [
    [15, -10],
    [10, -5]
]

equilibrium_strategy = backward_induction(transitions, payoffs)
print(equilibrium_strategy)
```

## Conclusion

---

Backward induction is a powerful technique for finding sub-game perfect equilibria in finite horizon games. By working backwards from the final stages of the game, we can determine the optimal strategy for each player at each stage. The resulting equilibrium strategy profile can be used to make predictions about the behavior of the players in the game.
