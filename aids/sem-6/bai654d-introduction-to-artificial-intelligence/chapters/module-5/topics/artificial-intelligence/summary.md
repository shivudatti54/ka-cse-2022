# Artificial Intelligence - Summary

## Key Definitions and Concepts

- Artificial Intelligence: The branch of computer science focused on creating systems capable of performing tasks requiring human intelligence, including learning, reasoning, problem-solving, perception, and language understanding.

- Intelligent Agent: A system that perceives its environment through sensors and acts upon it through actuators, ranging from simple reflex agents to goal-based and learning agents.

- Heuristic: A technique that speeds up problem solving by trading optimality, completeness, or precision for speed—used in A* search to guide toward solutions efficiently.

- Machine Learning: A subset of AI where systems learn patterns from data rather than following explicit instructions, categorized into supervised, unsupervised, and reinforcement learning.

- Neural Network: An information processing model inspired by biological neural systems, consisting of interconnected layers of nodes (neurons) that learn through weight adjustments during training.

- Backpropagation: An algorithm for training neural networks by computing gradients of the loss function with respect to weights and updating weights to minimize error.

- Knowledge Representation: Formalisms for encoding knowledge about the world in a form that AI systems can process, including logic, semantic networks, production rules, and frames.

## Important Formulas and Theorems

- A* Search: f(n) = g(n) + h(n), where g(n) is the actual cost from start to node n, h(n) is the heuristic estimated cost from n to goal, and f(n) is the total estimated cost. Optimal if h(n) is admissible.

- Minimax: For two-player zero-sum games, the maximizing player seeks maximum value while the minimizing player seeks minimum value. Value(node) = max(successors) if it's the maximizer's turn, min(successors) if it's the minimizer's turn.

- Certainty Factor Combination: CF_combined = CF1 + CF2 × (1 - CF1) when combining evidence from multiple rules.

- Manhattan Distance: |x1-x2| + |y1-y2|, used as an admissible heuristic for grid-based problems like the 8-puzzle.

## Key Points

- AI spans multiple approaches including symbolic AI (logic-based reasoning), connectionism (neural networks), and evolutionary computation, each with distinct strengths.

- Search problems represent solutions as paths through state-space graphs, with different algorithms offering tradeoffs between completeness, optimality, and efficiency.

- Game playing in AI uses game trees and the minimax algorithm, with alpha-beta pruning enabling practical deep search by eliminating irrelevant branches.

- Machine learning dominates modern AI through data-driven learning, with deep learning achieving breakthrough results in image, speech, and language processing.

- Neural networks learn through backpropagation, adjusting connection weights to minimize loss between predicted and actual outputs.

- Expert systems represent early successful AI applications, encoding human expertise as production rules and using inference engines for reasoning.

- Natural language processing faces fundamental challenges including ambiguity, context dependence, and the gap between syntactic structure and semantic meaning.

## Common Mistakes to Avoid

Confusing breadth-first search with depth-first search—BFS explores level by level guaranteeing shortest path but requiring more memory, while DFS goes deep potentially finding solutions faster but without optimality guarantees in unweighted graphs.

Assuming A* search always outperforms other algorithms—while optimal with admissible heuristics, the computational overhead of maintaining the open list can exceed benefits on simple problems.

Forgetting that heuristics must be admissible for A* optimality—using non-admissible heuristics can lead to suboptimal solutions even though search may appear faster.

Overlooking the distinction between classification and regression in machine learning—classification predicts discrete categories while regression predicts continuous values, requiring different algorithms and evaluation metrics.

Neglecting the importance of feature representation in machine learning—algorithms like SVM and neural networks perform dramatically better with appropriate feature engineering or learned representations.

## Revision Tips

Practice implementing search algorithms on paper by tracing through small state spaces—this builds intuition for how algorithms explore problem spaces and where inefficiencies arise.

Work through game tree examples manually, applying minimax at each node and understanding how alpha-beta pruning identifies branches that need not be evaluated.

Review neural network forward propagation calculations, ensuring you understand how weighted sums propagate through layers and how activation functions transform outputs.

Create comparison tables distinguishing different AI approaches—their assumptions, strengths, limitations, and typical application domains make excellent exam preparation.

Connect theoretical concepts to real-world applications—understanding how search enables route planning, how classification enables spam detection, and how neural networks enable image recognition reinforces learning.