# **Similarity-based Learning: Nearest-Neighbor Learning (5.5-5.7)**

## **Key Points**

- **Nearest-Neighbor Learning**:
  - A supervised learning algorithm that classifies new instances based on their similarity to existing instances in a training set.
  - Each new instance is compared to every instance in the training set, and the most similar one is chosen as the class label.
- **Weighted K-Nearest-Neighbor (WKNN) Algorithm**:
  - An extension of K-Nearest-Neighbor algorithm that assigns weights to each nearest neighbor based on their similarity.
  - The weighted sum of the class labels of the nearest neighbors is used to predict the class label of a new instance.

## **Formulas and Definitions**

- **Distance Metrics**:
  - Euclidean Distance: $d(x, y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + ... + (x_n - y_n)^2}$
  - Manhattan Distance: $d(x, y) = |x_1 - y_1| + |x_2 - y_2| + ... + |x_n - y_n|$
- **Similarity Measure**:
  - Cosine Similarity: $\cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$, where $\mathbf{u}$ and $\mathbf{v}$ are vectors representing the instances.
- **Theorem**:
  - **Vapnik-Chervonenkis (VC) Dimension**: A measure of the capacity of a classifier to separate data points.

## **Important Concepts**

- **Kernel Methods**: A class of algorithms that use kernel functions to transform the data into a higher-dimensional space, allowing for non-linear classification.
- **Overfitting**: When a model is too complex and fits the training data too closely, resulting in poor performance on new, unseen data.
