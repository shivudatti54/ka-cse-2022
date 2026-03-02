# Game Playing

## Overview

Game playing in AI provides a structured environment for testing decision-making algorithms through well-defined rules and measurable outcomes. Classic algorithms like minimax and alpha-beta pruning enable computers to play optimally in deterministic two-player games, while Monte Carlo Tree Search has revolutionized play in complex games like Go.

## Key Points

- **Game Tree**: Represents all possible moves and states from initial position to terminal states (win/lose/draw)
- **Minimax Algorithm**: Fundamental algorithm assuming both players play optimally, alternating between maximizing and minimizing values
- **Alpha-Beta Pruning**: Optimizes minimax by eliminating branches that cannot affect final decision without changing result
- **Heuristic Evaluation Functions**: Estimate value of non-terminal positions using factors like material advantage, mobility, and position
- **Monte Carlo Tree Search (MCTS)**: Combines tree search with random simulations through selection, expansion, simulation, and backpropagation
- **Perfect vs Imperfect Information**: Chess has perfect information while poker has imperfect information
- **Zero-Sum Games**: One player's gain equals the other's loss, typical of most classic games

## Important Concepts

- Alpha represents best value maximizer can guarantee, beta represents best value minimizer can guarantee
- Pruning occurs when alpha ≥ beta since that branch cannot influence the final decision
- MCTS revolutionized Go by using random playouts rather than exhaustive search
- Historical milestones: Deep Blue (1997), AlphaGo (2016), AlphaGo Zero (2017)

## Notes

- Trace minimax step-by-step alternating between MAX and MIN levels
- Practice alpha-beta pruning showing which branches can be pruned and why
- Understand evaluation function components: material, position, king safety, pawn structure
- Know game classifications: perfect/imperfect information, deterministic/stochastic, zero-sum/non-zero-sum
- Game playing techniques apply beyond games to robotics, business strategy, and decision support systems
