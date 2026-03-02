# Introduction to Artificial Intelligence

=====================================

## Game Playing

---

### 12. Game Playing

### 12.1 Minimax Algorithm

The Minimax algorithm is a recursive algorithm used for decision making in games like chess, checkers, etc. It works by simulating all possible moves and their consequences, and then choosing the move that maximizes the chances of winning.

#### How Minimax Works

- The algorithm starts by selecting a move and then simulating its consequences.
- It then chooses the best move from the consequences, and repeats this process until it reaches a leaf node (i.e., a node with no further consequences).
- The algorithm then backtracks and chooses the move that maximizes the chances of winning.

#### Example: Tic-Tac-Toe

Suppose we are playing Tic-Tac-Toe and we make a move. The Minimax algorithm will simulate all possible responses and their consequences, and then choose the move that maximizes the chances of winning.

| Move | Consequences | Best Move |
| ---- | ------------ | --------- |
| X    | O's response | 1         |
| X    | O's response | 2         |
| ...  | ...          | ...       |

#### Code Implementation

```python
import numpy as np

def minimax(board, depth, is_maximizing):
    if depth == 0 or np.all(np.equal(board, 1)) or np.all(np.equal(board, -1)):
        return evaluate_board(board)

    if is_maximizing:
        best_score = -np.inf
        for i in range(9):
            if board[i] == 0:
                board[i] = 1
                score = minimax(board, depth - 1, False)
                board[i] = 0
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for i in range(9):
            if board[i] == 0:
                board[i] = -1
                score = minimax(board, depth - 1, True)
                board[i] = 0
                best_score = min(score, best_score)
        return best_score

def evaluate_board(board):
    # This function evaluates the board and returns a score
    # A higher score means a better position
    pass
```

### 12.2 Alpha-Beta Pruning

Alpha-Beta pruning is an optimization technique used to speed up the Minimax algorithm. It works by pruning branches of the game tree that will not affect the final decision.

#### How Alpha-Beta Pruning Works

- The algorithm maintains two values: alpha and beta.
- Alpha is the best possible score for the maximizing player, and beta is the best possible score for the minimizing player.
- When the algorithm prunes a branch, it checks if the score of that branch is less than alpha or greater than beta. If it is, the branch can be pruned.

#### Example: Tic-Tac-Toe

```python
def alpha_beta(board, depth, alpha, beta, is_maximizing):
    if depth == 0 or np.all(np.equal(board, 1)) or np.all(np.equal(board, -1)):
        return evaluate_board(board)

    if is_maximizing:
        best_score = -np.inf
        for i in range(9):
            if board[i] == 0:
                board[i] = 1
                score = alpha_beta(board, depth - 1, alpha, beta, False)
                board[i] = 0
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if alpha >= beta:
                    break
        return best_score
    else:
        best_score = np.inf
        for i in range(9):
            if board[i] == 0:
                board[i] = -1
                score = alpha_beta(board, depth - 1, alpha, beta, True)
                board[i] = 0
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if alpha >= beta:
                    break
        return best_score

def evaluate_board(board):
    # This function evaluates the board and returns a score
    # A higher score means a better position
    pass
```

## Natural Language Processing

==========================

### 15. Natural Language Processing

Natural Language Processing (NLP) is the study of how to process and understand human language.

#### Types of NLP

- **Text Classification**: This involves classifying text into predefined categories.
- **Sentiment Analysis**: This involves determining the sentiment of text (positive, negative, neutral).
- **Named Entity Recognition**: This involves identifying named entities in text (people, places, organizations).
- **Language Translation**: This involves translating text from one language to another.

#### Key Concepts

- **Tokenization**: This involves breaking down text into individual words or tokens.
- **Stopwords**: These are common words like "the", "and", etc. that do not add much meaning to the text.
- **Stemming**: This involves reducing words to their base form (e.g., "running" becomes "run").
- **Lemmatization**: This involves reducing words to their base form (e.g., "running" becomes "run").

#### Example: Sentiment Analysis

```python
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def sentiment_analysis(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

text = "I love this product!"
sentiment = sentiment_analysis(text)
print(sentiment)
```

### 15.1 Text Preprocessing

Text preprocessing involves cleaning and normalizing text data.

#### Key Concepts

- **Text Normalization**: This involves normalizing the text to a standard format (e.g., converting all text to lowercase).
- **Tokenization**: This involves breaking down text into individual words or tokens.
- **Stopword Removal**: This involves removing common words like "the", "and", etc. that do not add much meaning to the text.

#### Example: Text Preprocessing

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def text_preprocessing(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return ' '.join(filtered_tokens)

text = "This is an example sentence."
preprocessed_text = text_preprocessing(text)
print(preprocessed_text)
```
