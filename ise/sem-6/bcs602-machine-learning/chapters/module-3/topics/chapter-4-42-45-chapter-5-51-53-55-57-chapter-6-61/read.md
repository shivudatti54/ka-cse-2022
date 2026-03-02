# **Machine Learning Study Material**

## **Chapter 4: Supervised Learning (4.2-4.5)**

### 4.2 Linear Regression

---

Linear regression is a type of supervised learning algorithm used to predict a continuous output variable based on one or more input features. It is a linear model that tries to find the best-fitting line between the input features and the output variable.

**Key Concepts:**

- **Linear Model:** A linear model is a mathematical model that describes a relationship between the input features and the output variable using a linear equation.
- **Coefficients:** Coefficients are the weights or slopes of the input features in the linear equation.
- **Intercept:** The intercept is the constant term in the linear equation.

**Example:**

Suppose we have a dataset of exam scores and hours studied, and we want to predict the exam score based on the number of hours studied. We can use linear regression to model the relationship between the two variables.

| Hours Studied | Exam Score |
| ------------- | ---------- |
| 2             | 80         |
| 4             | 90         |
| 6             | 96         |
| 8             | 100        |

Using linear regression, we can fit a line to the data and predict the exam score for a student who studied for 5 hours.

### 4.3 Logistic Regression

---

Logistic regression is a type of supervised learning algorithm used to predict a categorical output variable based on one or more input features. It is a linear model that tries to find the best-fitting function between the input features and the output variable.

**Key Concepts:**

- **Logistic Function:** The logistic function is a mathematical function that maps the input features to a probability between 0 and 1.
- **Coefficients:** Coefficients are the weights or slopes of the input features in the logistic function.
- **Intercept:** The intercept is the constant term in the logistic function.

**Example:**

Suppose we have a dataset of customers who are likely to buy a product based on their age and income, and we want to predict whether they will buy the product or not. We can use logistic regression to model the relationship between the two variables.

| Age | Income | Will Buy |
| --- | ------ | -------- |
| 25  | 50000  | Yes      |
| 35  | 75000  | No       |
| 40  | 100000 | Yes      |
| 50  | 150000 | Yes      |

Using logistic regression, we can fit a function to the data and predict whether a customer will buy the product or not based on their age and income.

### 4.4 Decision Trees

---

Decision trees are a type of supervised learning algorithm used to predict a categorical output variable based on a set of input features. They are a tree-like model that tries to find the best-fitting decision at each node.

**Key Concepts:**

- **Root Node:** The root node is the topmost node in the tree that represents the input features.
- **Child Nodes:** The child nodes are the nodes that branch out from the root node based on the input features.
- **Leaf Nodes:** The leaf nodes are the nodes that represent the predicted output variable.

**Example:**

Suppose we have a dataset of customers who are likely to buy a product based on their age, income, and education level, and we want to predict whether they will buy the product or not. We can use decision trees to model the relationship between the variables.

| Age | Income | Education   | Will Buy |
| --- | ------ | ----------- | -------- |
| 25  | 50000  | High School | No       |
| 35  | 75000  | College     | Yes      |
| 40  | 100000 | Master's    | Yes      |
| 50  | 150000 | Ph.D.       | Yes      |

Using decision trees, we can fit a tree to the data and predict whether a customer will buy the product or not based on their age, income, and education level.

### 4.5 k-Nearest Neighbors (k-NN)

---

k-NN is a type of supervised learning algorithm used to predict a categorical output variable based on the majority vote of the k nearest neighbors.

**Key Concepts:**

- **Nearest Neighbors:** The nearest neighbors are the data points that are closest to the new input features.
- **Majority Vote:** The majority vote is the predicted output variable based on the majority of the nearest neighbors.

**Example:**

Suppose we have a dataset of customers who are likely to buy a product based on their age, income, and education level, and we want to predict whether they will buy the product or not. We can use k-NN to model the relationship between the variables.

| Age | Income | Education   | Will Buy |
| --- | ------ | ----------- | -------- |
| 25  | 50000  | High School | No       |
| 35  | 75000  | College     | Yes      |
| 40  | 100000 | Master's    | Yes      |
| 50  | 150000 | Ph.D.       | Yes      |

Using k-NN, we can fit a model to the data and predict whether a customer will buy the product or not based on their age, income, and education level.

## **Chapter 5: Unsupervised Learning (5.1-5.3, 5.5-5.7)**

### 5.1 Clustering

---

Clustering is a type of unsupervised learning algorithm used to group similar data points into clusters.

**Key Concepts:**

- **Cluster:** A cluster is a group of data points that are similar to each other.
- **Distance Metric:** The distance metric is a function that measures the distance between two data points.
- **Centroid:** The centroid is the center of the cluster.

**Example:**

Suppose we have a dataset of customers who have different demographics, and we want to group them into clusters based on their age, income, and education level. We can use clustering to model the relationship between the variables.

| Age | Income | Education   |
| --- | ------ | ----------- |
| 25  | 50000  | High School |
| 35  | 75000  | College     |
| 40  | 100000 | Master's    |
| 50  | 150000 | Ph.D.       |
| 25  | 50000  | High School |
| 35  | 75000  | College     |
| 40  | 100000 | Master's    |
| 50  | 150000 | Ph.D.       |

Using clustering, we can fit a model to the data and group the customers into clusters based on their age, income, and education level.

### 5.2 Dimensionality Reduction

---

Dimensionality reduction is a type of unsupervised learning algorithm used to reduce the number of features in a dataset while preserving the most important information.

**Key Concepts:**

- **Principal Component Analysis (PCA):** PCA is a technique used to reduce the dimensionality of a dataset by projecting the data onto a lower-dimensional space.
- **Singular Value Decomposition (SVD):** SVD is a technique used to reduce the dimensionality of a dataset by decomposing the data into three matrices.

**Example:**

Suppose we have a dataset of images that we want to reduce the dimensionality of while preserving the most important information. We can use PCA or SVD to model the relationship between the images.

### 5.3 k-Means

---

k-Means is a type of unsupervised learning algorithm used to group similar data points into clusters.

**Key Concepts:**

- **Cluster:** A cluster is a group of data points that are similar to each other.
- **Distance Metric:** The distance metric is a function that measures the distance between two data points.
- **Centroid:** The centroid is the center of the cluster.

**Example:**

Suppose we have a dataset of customers who have different demographics, and we want to group them into clusters based on their age, income, and education level. We can use k-Means to model the relationship between the variables.

| Age | Income | Education   |
| --- | ------ | ----------- |
| 25  | 50000  | High School |
| 35  | 75000  | College     |
| 40  | 100000 | Master's    |
| 50  | 150000 | Ph.D.       |
| 25  | 50000  | High School |
| 35  | 75000  | College     |
| 40  | 100000 | Master's    |
| 50  | 150000 | Ph.D.       |

Using k-Means, we can fit a model to the data and group the customers into clusters based on their age, income, and education level.

### 5.5 Principal Component Analysis (PCA)

---

PCA is a technique used to reduce the dimensionality of a dataset by projecting the data onto a lower-dimensional space.

**Key Concepts:**

- **Eigenvalues:** Eigenvalues are the values that represent the amount of variance explained by each principal component.
- **Eigenvectors:** Eigenvectors are the vectors that represent the directions of the principal components.
- **Principal Components:** Principal components are the new features that are created by projecting the data onto the lower-dimensional space.

**Example:**

Suppose we have a dataset of images that we want to reduce the dimensionality of while preserving the most important information. We can use PCA to model the relationship between the images.

### 5.6 k-Medoids

---

k-Medoids is a type of unsupervised learning algorithm used to group similar data points into clusters.

**Key Concepts:**

- **Cluster:** A cluster is a group of data points that are similar to each other.
- **Distance Metric:** The distance metric is a function that measures the distance between two data points.
- **Medoid:** The medoid is the data point that represents the center of the cluster.

**Example:**

Suppose we have a dataset of customers who have different demographics, and we want to group them into clusters based on their age, income, and education level. We can use k-Medoids to model the relationship between the variables.

| Age | Income | Education   |
| --- | ------ | ----------- |
| 25  | 50000  | High School |
| 35  | 75000  | College     |
| 40  | 100000 | Master's    |
| 50  | 150000 | Ph.D.       |
| 25  | 50000  | High School |
| 35  | 75000  | College     |
| 40  | 100000 | Master's    |
| 50  | 150000 | Ph.D.       |

Using k-Medoids, we can fit a model to the data and group the customers into clusters based on their age, income, and education level.

### 5.7 Hierarchical Clustering

---

Hierarchical clustering is a type of unsupervised learning algorithm used to group similar data points into clusters.

**Key Concepts:**

- **Cluster:** A cluster is a group of data points that are similar to each other.
- **Distance Metric:** The distance metric is a function that measures the distance between two data points.
- **Hierarchical Tree:** A hierarchical tree is the structure that represents the clusters.

**Example:**

Suppose we have a dataset of customers who have different demographics, and we want to group them into clusters based on their age, income, and education level. We can use hierarchical clustering to model the relationship between the variables.

| Age | Income | Education   |
| --- | ------ | ----------- |
| 25  | 50000  | High School |
| 35  | 75000  | College     |
| 40  | 100000 | Master's    |
| 50  | 150000 | Ph.D.       |
| 25  | 50000  | High School |
| 35  | 75000  | College     |
| 40  | 100000 | Master's    |
| 50  | 150000 | Ph.D.       |

Using hierarchical clustering, we can fit a model to the data and group the customers into clusters based on their age, income, and education level.

## **Chapter 6: Model Evaluation (6.1, 6.2)**

### 6.1 Evaluation Metrics

---

Evaluation metrics are used to measure the performance of a machine learning model.

**Key Concepts:**

- **Accuracy:** Accuracy is the proportion of correct predictions made by the model.
- **Precision:** Precision is the proportion of true positives among all predicted positives.
- **Recall:** Recall is the proportion of true positives among all actual positives.
- **F1-score:** F1-score is the harmonic mean of precision and recall.

**Example:**

Suppose we have a dataset of customers who have different demographics, and we want to evaluate the performance of a machine learning model that predicts whether they will buy a product or not. We can use metrics such as accuracy, precision, recall, and F1-score to measure the performance of the model.

| Predicted Class | Actual Class | Accuracy | Precision | Recall | F1-score |
| --------------- | ------------ | -------- | --------- | ------ | -------- |
| Buy             | Buy          | 0.8      | 0.7       | 0.9    | 0.8      |
| Buy             | Not Buy      | 0.2      | 0.3       | 0.2    | 0.2      |
| Not Buy         | Buy          | 0.2      | 0.3       | 0.2    | 0.2      |
| Not Buy         | Not Buy      | 0.8      | 0.7       | 0.9    | 0.8      |

Using the metrics, we can evaluate the performance of the model and identify areas for improvement.

### 6.2 Cross-Validation

---

Cross-validation is a technique used to evaluate the performance of a machine learning model on unseen data.

**Key Concepts:**

- **Fold:** A fold is a subset of the data used to train the model.
- **Validation Set:** The validation set is the subset of the data used to evaluate the model.
- **K-Fold Cross-Validation:** K-fold cross-validation is a technique used to evaluate the performance of the model by training and evaluating the model on k folds of the data.

**Example:**

Suppose we have a dataset of customers who have different demographics, and we want to evaluate the performance of a machine learning model that predicts whether they will buy a product or not. We can use k-fold cross-validation to train and evaluate the model on k folds of the data.

| Fold | Training Set | Validation Set |
| ---- | ------------ | -------------- |
| 1    | 80%          | 20%            |
| 2    | 70%          | 30%            |
| 3    | 60%          | 40%            |
| 4    | 50%          | 50%            |
| 5    | 40%          | 60%            |

Using k-fold cross-validation, we can train and evaluate the model on k folds of the data and evaluate its performance.
