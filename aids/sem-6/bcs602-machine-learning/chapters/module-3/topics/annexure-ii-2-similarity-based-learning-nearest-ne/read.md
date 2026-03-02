# **Similarity-based Learning: Nearest-Neighbor Learning, Weighted K-Nearest-Neighbor Algorithm, Nearest Centroid Classifier, Locally Weighted**

## **Introduction**

Similarity-based learning is a type of supervised learning where the algorithm learns from patterns in the data by comparing instances to their neighbors. This approach is useful when the data is high-dimensional and the relationships between features are complex. The four key concepts in similarity-based learning are Nearest-Neighbor Learning, Weighted K-Nearest-Neighbor Algorithm, Nearest Centroid Classifier, and Locally Weighted.

## **Nearest-Neighbor Learning**

- **Definition:** Nearest-Neighbor Learning is a type of supervised learning where the algorithm makes predictions based on the majority vote of its k-nearest neighbors.
- **How it works:**
  1.  Calculate the distance between the sample and all other samples in the training data.
  2.  Select the k samples with the smallest distances (nearest neighbors).
  3.  Calculate the majority vote of the nearest neighbors.
  4.  Assign the predicted class label based on the majority vote.
- **Example:** In a handwritten digit recognition problem, the algorithm can use the nearest-neighbor learning approach to predict the digit by finding the k nearest neighbors in the training data and assigning the class label based on the majority vote.

## **Weighted K-Nearest-Neighbor Algorithm**

- **Definition:** The Weighted K-Nearest-Neighbor Algorithm is an extension of the traditional K-Nearest-Neighbor Algorithm where the weights of the nearest neighbors are assigned based on their distance from the sample.
- **How it works:**
  1.  Calculate the distance between the sample and all other samples in the training data.
  2.  Assign weights to the nearest neighbors based on their distance from the sample.
  3.  Calculate the weighted sum of the nearest neighbors.
  4.  Assign the predicted class label based on the weighted sum.
- **Example:** In a medical diagnosis problem, the weighted K-Nearest-Neighbor Algorithm can be used to predict the presence of a disease by assigning weights to the nearest neighbors based on their distance from the sample.

## **Nearest Centroid Classifier**

- **Definition:** The Nearest Centroid Classifier is a type of supervised learning where the algorithm makes predictions based on the class centroid of the nearest neighbors.
- **How it works:**
  1.  Calculate the mean of each feature for each class in the training data.
  2.  Calculate the distance between the sample and the class centroids.
  3.  Select the class with the smallest distance as the predicted class label.
- **Example:** In a color classification problem, the Nearest Centroid Classifier can be used to predict the color by selecting the class with the smallest distance to the sample.

## **Locally Weighted**

- **Definition:** Locally Weighted is a type of supervised learning where the weights of the nearest neighbors are assigned based on the local density of the sample.
- **How it works:**
  1.  Calculate the local density of the sample based on the feature values.
  2.  Assign weights to the nearest neighbors based on their local density.
  3.  Calculate the weighted sum of the nearest neighbors.
  4.  Assign the predicted class label based on the weighted sum.
- **Example:** In a speech recognition problem, the locally weighted approach can be used to predict the spoken word by assigning weights to the nearest neighbors based on the local density of the sample.

## **Key Concepts**

- **Distance metric:** A function that calculates the distance between two vectors, such as Euclidean distance or Manhattan distance.
- **Weighted sum:** A mathematical operation that calculates the sum of weighted values, where the weights are assigned based on certain criteria.
- **Local density:** A measure of the density of the sample in a local neighborhood, which can be used to assign weights to the nearest neighbors.
- **Class centroid:** The mean of each feature for each class in the training data, which can be used to select the class with the smallest distance as the predicted class label.
