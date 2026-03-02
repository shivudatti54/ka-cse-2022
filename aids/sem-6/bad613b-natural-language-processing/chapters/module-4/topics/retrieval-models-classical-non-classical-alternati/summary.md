# **Retrieval Models - Classical, Non-classical, Alternative Models of Information Retrieval**

### Classical Models

- **Coster-Harard Model**:
  - Formula: `P(T | Q) = P(T) * P(Q | T)`
  - Definition: calculates the probability of topic T given query Q
  - Theorem: Bayes' theorem
- **Custer Model**:
  - Formula: `P(T | Q) = P(T) * P(Q | T)`
  - Definition: calculates the probability of topic T given query Q
  - Note: Similar to Coster-Harard Model, but with different query probability calculation

### Non-classical Models

- **Fuzzy Model**:
  - Definition: uses fuzzy logic to represent vague queries
  - Formula: `P(T | Q) = ∫∫ P(T) * P(Q | T) dT dQ`
  - Theorem: fuzzy probability
- **Major Issues in Info**:
  - **Term Frequency-Inverse Document Frequency (TF-IDF)**:
    - Formula: `TF-IDF = TF * IDF`
    - Definition: calculates the importance of a term in a document
  - **Query Expansion**:
    - Definition: expands a query to include related terms

### Alternative Models

- **LSTM Model**:
  - Definition: uses Long Short-Term Memory (LSTM) architecture to represent sequential data
  - Formula: `P(T | Q) = LSTM(Q)`
  - Theorem: LSTM architecture
- **Deep Learning Models**:
  - Definition: uses deep learning techniques such as neural networks and convolutional neural networks (CNNs)
  - Formula: `P(T | Q) = DeepLearningModel(Q)`
  - Theorem: deep learning architecture

### Major Issues in Info

- **Spam and Advertisements**:
  - Definition: uses filters to remove spam and advertisements from search results
  - Formula: `P(T | Q) = P(T) - P(Spam | Q)`
- **Query Optimization**:
  - Definition: optimizes the query to improve search results
  - Formula: `P(T | Q) = OptimizeQuery(Q)`
- **Relevance**:
  - Definition: measures the relevance of search results to a query
  - Formula: `Relevance = P(T | Q) * P(Q | T)`
