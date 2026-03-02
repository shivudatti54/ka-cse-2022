# **Deep Learning Network for Textual Document Classification**

### Overview

- Classification of textual documents using deep learning networks
- Key concepts: text preprocessing, word embeddings, CNN/LSTM/GRU architectures
- Objective: predict label(s) for a given text document

### Key Points

- **Text Preprocessing**
  - Tokenization: split text into individual words
  - Stopword removal: remove common words (e.g. "the", "and")
  - Stemming/Lemmatization: reduce words to their base form
  - Vectorization: convert text to numerical representation (e.g. bag-of-words, word embeddings)
- **Word Embeddings**
  - Word2Vec: learn vector representations of words from text data
  - GloVe: learn vector representations of words from text data using matrix factorization
- **Deep Learning Architectures**
  - Convolutional Neural Networks (CNNs)
    - Use convolutional and pooling layers to extract features from text data
  - Recurrent Neural Networks (RNNs)
    - Use recurrent and fully connected layers to model sequential dependencies in text data
  - Long Short-Term Memory (LSTM) Networks
    - Use LSTM cells to model long-term dependencies in text data
  - Gated Recurrent Units (GRU) Networks
    - Use GRU cells to model long-term dependencies in text data with fewer parameters
- **Classification Algorithms**
  - Logistic Regression
  - Support Vector Machines (SVMs)
  - K-Nearest Neighbors (KNN)
  - Deep Neural Networks (DNNs)

### Important Formulas and Theorems

- **Logistic Regression**
  - Loss function: $L = -\sum_{i=1}^n [y_i \log(p_i) + (1-y_i) \log(1-p_i)]$
  - Cost function: $J = \frac{1}{2} \sum_{i=1}^n (p_i - y_i)^2$
- **Support Vector Machines (SVMs)**
  - Loss function: $L = \frac{1}{2} ||w||^2$
  - Cost function: $J = C \sum_{i=1}^n [L_i + \gamma r_i]$
- **K-Nearest Neighbors (KNN)**
  - Distance metric: $d(x_i, x) = \|x_i - x\|$
  - Classification: $y = \arg\max_{y \in Y} \sum_{i=1}^K \sigma(d(x_i, x))$

### Recommended Reading

- "Deep Learning" by Ian Goodfellow, Yoshua Bengio, and Aaron Courville
- "Natural Language Processing (almost) from Scratch" by Collobert et al.
- "Text Classification using Deep Neural Networks" by Liu et al.
