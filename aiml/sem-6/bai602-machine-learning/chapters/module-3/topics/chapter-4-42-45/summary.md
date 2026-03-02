# **Similarity-based Learning: Nearest-Neighbor Learning, Weighted K-Nearest-Neighbor Algorithm**

### Chapter-4 (4.2-4.5) Revision Notes

#### 4.2 Nearest-Neighbor Learning

- Definition: A supervised learning algorithm that makes predictions based on the class label of the most similar instance in the training dataset.
- Types:
  - Soft nearest neighbor (SNN): assigns a probability to each class label
  - Hard nearest neighbor (HNN): assigns a single class label
- Key Concepts:
  - Distance metrics (Euclidean, Manhattan, etc.)
  - K-Nearest Neighbor (KNN) algorithm

#### 4.3 Weighted K-Nearest-Neighbor Algorithm

- Definition: A variation of KNN that assigns different weights to each instance based on its similarity to the query instance.
- Formulas:
  - Weighted KNN distance: $d_i = w_i \cdot d_i^{(KNN)}$
  - Weighted KNN classification: $y = \arg\max_{y \in Y} \sum_{i=1}^{K} w_i \cdot f_i(y)$
- Key Concepts:
  - Weight assignment techniques (linear, exponential, etc.)
  - Classifier selection (Bayes, logistic regression, etc.)

#### 4.4 k-Nearest Neighbor Algorithm

- Definition: A supervised learning algorithm that makes predictions based on the majority vote of the k most similar instances.
- Formulas:
  - k-NN distance: $d_i = \sqrt{\sum_{j=1}^{m} (x_{ij} - x_{ij})^2}$
  - k-NN classification: $y = \arg\max_{y \in Y} \sum_{i=1}^{k} f_i(y)$
- Key Concepts:
  - k value selection
  - Instance selection

#### 4.5 Evaluation of k-Nearest Neighbor Algorithms

- Definition: A set of metrics used to evaluate the performance of k-NN algorithms.
- Metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Mean Squared Error (MSE)
  - Mean Absolute Error (MAE)
- Key Concepts:
  - Cross-validation
  - Overfitting

#### Important Formulas and Definitions

- Euclidean distance: $d(x, y) = \sqrt{\sum_{i=1}^{m} (x_i - y_i)^2}$
- Manhattan distance: $d(x, y) = \sum_{i=1}^{m} |x_i - y_i|$
- Bayes classifier: $P(y|x) = \frac{P(x|y)P(y)}{\sum_{y \in Y} P(x|y)P(y)}$
