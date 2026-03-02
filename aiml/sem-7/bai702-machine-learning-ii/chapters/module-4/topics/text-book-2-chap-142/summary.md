# **Text Book 2: Chap 14.2 Revision Notes**

**Module:** 21102024
**Topic:** Text Book 2: Chap 14.2

**Key Points:**

- **K-Nearest Neighbors (KNN)**:
  - An instance-based learning algorithm.
  - Predicts the class of a new instance by finding the k most similar instances in the training set.
- **Distance Metrics**:
  - Euclidean Distance: √((x2 - x1)^2 + (y2 - y1)^2)
  - Manhattan Distance: |x2 - x1| + |y2 - y1|
  - Minkowski Distance: (|x2 - x1|^p + |y2 - y1|^p)^(1/p)
- **Weighted KNN**:
  - Assigns weights to instances based on their relevance to the new instance.
- **KNN Algorithm**:
  - Train a model by storing the training data.
  - Use the model to predict the class of new instances.
- **Advantages**:
  - Simple to implement.
  - Handles non-linear relationships.

**Important Formulas and Definitions:**

- **Class Weight**: w = (1 / (1 + e^(-D))) where D is the distance between the new instance and the instances in the training set.
- **Similarity Measure**: s = (1 / (1 + e^(-D))) where D is the distance between the new instance and the instances in the training set.

**Theorem:**

- **KNN Theorem**: When the training data is small, KNN is a good approximation to other machine learning algorithms.

**Quick Revision Tips:**

- Remember the distance metrics used in KNN.
- Understand the concept of weighted KNN.
- Practice implementing the KNN algorithm.
