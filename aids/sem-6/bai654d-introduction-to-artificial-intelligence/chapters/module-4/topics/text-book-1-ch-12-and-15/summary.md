# Text Book 1: Ch 12 and 15

### Game Playing

- **Game Trees**: A decision tree used to represent possible moves in a game.
- **Minimax Algorithm**:
  - Definition: A recursive algorithm used to find the best move in a game.
  - Formula: `minimax(a, b) = min{[max(a, b)]}` (minus the value of the leaves)
  - Time complexity: O(b^d), where d is the depth of the game tree
- **Alpha-Beta Pruning**:
  - Definition: A modification of the Minimax algorithm that reduces the number of nodes to be evaluated.
  - Formula: `minimax(a, b) = min{[alpha, max(a, b)]}` (where alpha is the best value of the opponent's move)
- **Game Value Functions**: Used to assign a value to each node in the game tree.
- **N-Player Games**: Games with multiple players, where each player has its own game tree and value function.

### Natural Language Processing

- **Tokenization**: The process of breaking down text into individual words or tokens.
- **Part-of-Speech (POS) Tagging**: The process of identifying the part of speech (such as noun, verb, adjective, etc.) of each word in a sentence.
- **Named Entity Recognition (NER)**: The process of identifying named entities (such as people, places, organizations) in a sentence.
- **Word Embeddings**: A technique used to represent words as vectors in a high-dimensional space, allowing for semantic comparisons between words.
- **Language Models**: Statistical models used to predict the next word in a sentence, based on the context of the previous words.

## Key Formulas and Theorems

- Minimax Formula: `minimax(a, b) = min{[max(a, b)]}`
- Alpha-Beta Pruning Formula: `minimax(a, b) = min{[alpha, max(a, b)]}`
- Shannon Entropy: `H(P) = -∑(p \* log2(p))`, where p is the probability of each outcome.
