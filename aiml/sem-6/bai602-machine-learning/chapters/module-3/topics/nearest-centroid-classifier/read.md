# **Nearest Centroid Classifier**

## **Introduction**

The Nearest Centroid Classifier is a type of supervised learning algorithm used for classification problems. It is based on the concept of finding the closest class centroid to the new, unseen data point. This classifier is widely used in various domains, including image and speech recognition.

## **Key Concepts**

- **Centroid**: The mean value of a set of data points in a particular feature space.
- **Distance Measure**: A function that measures the distance between two data points.
- **Nearest Neighbor**: A data point that is closest to the new, unseen data point.
- **K-Nearest Neighbors (KNN)**: A supervised learning algorithm that finds the K nearest neighbors to the new data point.

## **How Nearest Centroid Classifier Works**

1.  **Training Phase**: The classifier is trained on a labeled dataset, where each sample is associated with a class label.
2.  **Feature Extraction**: The dataset is preprocessed to extract relevant features from the data points.
3.  **Centroid Calculation**: The centroid of each class is calculated by taking the mean of the feature values for all samples in that class.
4.  **Distance Calculation**: The distance between the new data point and each class centroid is calculated using a chosen distance measure (e.g., Euclidean distance).
5.  **Classification**: The class with the minimum distance to the new data point is selected as the predicted class label.

## **Types of Nearest Centroid Classifiers**

- **Soft Nearest Centroid (SNC)**: The classifier assigns a probability to each class based on the distance to the class centroid.
- **Hard Nearest Centroid (HNC)**: The classifier assigns a class label based on the closest class centroid.

## **Advantages and Disadvantages**

- **Advantages**:
  - Simple to implement
  - Fast computation
  - Can be used for high-dimensional data
- **Disadvantages**:
  - Sensitive to noise in the data
  - May not perform well with non-linear relationships between features and classes

## **Example Use Case**

Suppose we have a dataset of images of different animals, and we want to classify a new, unseen image into one of the five classes (dog, cat, bird, fish, and elephant). We can use the Nearest Centroid Classifier to find the closest class centroid to the new image and assign it to the corresponding class.

## **Code Implementation**

Here's an example code implementation of the Nearest Centroid Classifier in Python using scikit-learn library:

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Load the dataset
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

# Train the classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# Make predictions
y_pred = knn.predict(X)

# Calculate accuracy
accuracy = accuracy_score(y, y_pred)
print("Accuracy:", accuracy)

# Use the classifier to make a prediction on a new data point
new_data = np.array([[5.1, 3.5, 1.4, 0.2]])
predicted_class = knn.predict(new_data)
print("Predicted Class:", predicted_class)
```

In this example, we use the K-Nearest Neighbors algorithm to implement the Nearest Centroid Classifier. We train the classifier on the Iris dataset and evaluate its performance using accuracy score. Finally, we use the classifier to make a prediction on a new data point.
