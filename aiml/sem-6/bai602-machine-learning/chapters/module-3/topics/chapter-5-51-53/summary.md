# **Similarity-based Learning: Nearest-Neighbor Learning, Weighted K-Nearest-Neighbor Algorithm**

### 5.1 Introduction to Nearest Neighbor Learning

- Nearest Neighbor (NN) learning is a supervised learning algorithm that involves finding the most similar training examples to a new, unseen instance.
- The goal is to predict the class label of the new instance based on the majority vote of its k-nearest neighbors.

### 5.2 Nearest Neighbor Learning

- **Definition:** Nearest Neighbor (NN) learning is a type of supervised learning algorithm that classifies new instances based on their similarity to the training examples.
- **Types:**
  - **Hard NN:** Classifies a new instance as the same class as its closest training example.
  - **Soft NN:** Assigns a probability distribution over classes based on the similarity to training examples.

### 5.3 Weighted K-Nearest-Neighbor Algorithm

- **Definition:** Weighted K-Nearest-Neighbor (WKNN) is an extension of the traditional NN algorithm that assigns weights to training examples based on their distance to the new instance.
- **Formulas:**
  - **Distance metric:** Euclidean distance, Manhattan distance, etc.
  - **Weight calculation:** $w_i = \frac{1}{||\vec{x}_i||^2}$, where $\vec{x}_i$ is the training example and $||\vec{x}_i||$ is its distance to the new instance.
  - **Weighted NN:** Classifies a new instance as the class with the highest weighted sum of votes.

### Important Formulas and Definitions

- **Euclidean distance:** $d(x, y) = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$
- **Manhattan distance:** $d(x, y) = \sum_{i=1}^n |x_i - y_i|$
- **Distance metric:** The measure used to calculate the distance between two instances.

### Theorems and Concepts

- **Vapnik-Chervonenkis (VC) dimension:** A measure of the capacity of a classifier to separate data.
- **Nearest Neighbor Theorem:** A new instance is classified as the same class as its closest training example.
