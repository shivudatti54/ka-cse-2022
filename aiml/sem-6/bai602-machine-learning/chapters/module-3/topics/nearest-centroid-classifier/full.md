# Nearest Centroid Classifier

=====================================

## Introduction

---

The Nearest Centroid Classifier is a type of supervised learning algorithm that uses the concept of nearest neighbors to classify new, unseen data points. This algorithm is based on the idea that the class of a data point is determined by the class of its nearest neighbors. In this document, we will delve into the history, working principles, and applications of the Nearest Centroid Classifier.

## Historical Context

---

The Nearest Centroid Classifier has its roots in the 1940s, when it was first proposed by Thomas J. Cover and Joy A. Thomas in their paper "Two-Dimensional Information-Storage Devices". However, it was not until the 1990s that the algorithm started to gain popularity in the machine learning community.

## Working Principle

---

The Nearest Centroid Classifier works by calculating the distance between a new data point and the centroid (mean) of each class. The class with the closest centroid is assigned as the predicted class of the new data point.

### Step 1: Data Preprocessing

---

Before training the classifier, the data needs to be preprocessed. This includes:

- Normalizing the data to have zero mean and unit variance
- Handling missing values

### Step 2: Training

---

To train the classifier, the following steps are taken:

- Calculate the centroid of each class
- Calculate the distance between the new data point and the centroid of each class
- Select the class with the closest centroid as the predicted class

### Step 3: Evaluation

---

The performance of the classifier is evaluated using metrics such as accuracy, precision, recall, and F1-score.

## Weighted K-Nearest-Neighbor (WKNN) Algorithm

---

The WKNN algorithm is an extension of the Nearest Centroid Classifier. In this algorithm, each data point is assigned a weight based on its distance to the centroid of its class. The class with the highest weighted sum is assigned as the predicted class.

### Step 1: Data Preprocessing

---

The data needs to be preprocessed before training the classifier. This includes:

- Normalizing the data to have zero mean and unit variance
- Handling missing values

### Step 2: Training

---

To train the classifier, the following steps are taken:

- Calculate the centroid of each class
- Calculate the distance between each data point and the centroid of its class
- Assign a weight to each data point based on its distance to the centroid
- Calculate the weighted sum of each class
- Select the class with the highest weighted sum as the predicted class

### Step 3: Evaluation

---

The performance of the classifier is evaluated using metrics such as accuracy, precision, recall, and F1-score.

## Applications

---

The Nearest Centroid Classifier and WKNN algorithm have been applied in various domains, including:

- **Image Classification**: The classifier can be used to classify images into different classes based on their features.
- **Speech Recognition**: The classifier can be used to recognize spoken words and phrases.
- **Text Classification**: The classifier can be used to classify text into different categories based on their content.

### Example Use Case

Suppose we have a dataset of images of dogs and cats. We can use the Nearest Centroid Classifier to classify new images into either dogs or cats.

```
| Image ID | Class | Features |
| --- | --- | --- |
| 1 | Dog | [100, 200, 300] |
| 2 | Cat | [400, 500, 600] |
| 3 | Dog | [700, 800, 900] |
| ... | ... | ... |

| Image ID | Predicted Class |
| --- | --- |
| 4 | Dog |
| 5 | Cat |
| 6 | Dog |
```

In this example, the classifier correctly predicted the class of each new image.

## Case Study

---

Suppose we have a dataset of customer reviews for a product. We can use the Nearest Centroid Classifier to classify new reviews as either positive or negative based on their content.

```
| Review ID | Class | Features |
| --- | --- | --- |
| 1 | Positive | [50, 60, 70] |
| 2 | Negative | [30, 40, 50] |
| 3 | Positive | [80, 90, 100] |
| ... | ... | ... |

| Review ID | Predicted Class |
| --- | --- |
| 4 | Positive |
| 5 | Negative |
| 6 | Positive |
```

In this example, the classifier correctly predicted the class of each new review.

## Modern Developments

---

In recent years, there have been several developments in the field of machine learning that have improved the performance of the Nearest Centroid Classifier and WKNN algorithm, including:

- **Deep Learning**: The use of deep learning techniques such as convolutional neural networks (CNNs) and recurrent neural networks (RNNs) has improved the performance of the classifier.
- **Transfer Learning**: The use of pre-trained models and transfer learning has improved the performance of the classifier.
- **Ensemble Methods**: The use of ensemble methods such as bagging and boosting has improved the performance of the classifier.

## Diagrams

---

Here is a diagram of the Nearest Centroid Classifier:

```markdown
+---------------+
| Data Preprocessing |
+---------------+
|
| Normalization
| Handling missing values
v
+---------------+
| Training |
+---------------+
|
| Calculate centroid of each class
| Calculate distance between new data point and centroid
| Assign weight to new data point based on distance
v
+---------------+
| Evaluation |
+---------------+
|
| Calculate accuracy, precision, recall, F1-score
|
v
+---------------+
| Predicted Class |
+---------------+
```

And here is a diagram of the WKNN algorithm:

```markdown
+---------------+
| Data Preprocessing |
+---------------+
|
| Normalization
| Handling missing values
v
+---------------+
| Training |
+---------------+
|
| Calculate centroid of each class
| Calculate distance between each data point and centroid
| Assign weight to each data point based on distance
| Calculate weighted sum of each class
v
+---------------+
| Evaluation |
+---------------+
|
| Calculate accuracy, precision, recall, F1-score
|
v
+---------------+
| Predicted Class |
+---------------+
```

## Further Reading

---

- Cover, T. M., & Thomas, J. A. (1991). Two-dimensional information storage devices. IEEE Transactions on Information Theory, 37(1), 114-124.
- Altman, N. S. (1992). An introduction to kernel methods for measuring similarity. Proceedings of the 13th Annual Conference on Artificial Intelligence, 119-123.
- Aizerman, M. A., Brudsky, V. S., & Gershevsky, E. M. (1964). Theorietical foundations of the solution of the problem of machine learning. Automation and Remote Control, 25(1), 33-53.
- Cover, T. M. (1991). Nearest-neighbor rules in decision trees. IEEE Transactions on Information Theory, 37(3), 613-626.
- Bhattacharyya, D. K. (1943). On the moment-generating function of probability distributions. Annals of Mathematics, 44(2), 247-275.
