**Annexure-II 2 Similarity-based Learning: Nearest-Neighbor Learning, Weighted K-Nearest-Neighbor Algorithm, Nearest Centroid Classifier, Locally Weighted**

**Introduction**

Similarity-based learning is a fundamental concept in machine learning, which involves training models to learn patterns and relationships between data points based on their similarities. In this annexure, we will delve into four popular similarity-based learning techniques: Nearest-Neighbor Learning, Weighted K-Nearest-Neighbor Algorithm, Nearest Centroid Classifier, and Locally Weighted. These techniques have been widely used in various applications, including classification, regression, and clustering.

**Nearest-Neighbor Learning**

Nearest-Neighbor Learning, also known as K-Nearest Neighbor (KNN), is a classic similarity-based learning algorithm. The idea behind KNN is to classify new data points by finding the k most similar data points in the training set and using them to make a prediction.

### How KNN Works

1. **Distance Calculation**: The algorithm calculates the distance between the new data point and all data points in the training set using a distance metric such as Euclidean distance, Manhattan distance, or Minkowski distance.
2. **K-Nearest Neighbors**: The algorithm identifies the k data points with the smallest distances to the new data point.
3. **Voting**: The algorithm assigns the label of the most frequent class among the k-nearest neighbors to the new data point.

### Advantages and Disadvantages

Advantages:

- Simple to implement
- Handles high-dimensional data well
- Robust to noise and outliers

Disadvantages:

- Computationally expensive for large datasets
- Sensitive to hyperparameter tuning (k)

### Example

Suppose we have a dataset of images of dogs and cats, and we want to classify a new image as either a dog or a cat. We use KNN with k=5 and calculate the Euclidean distance between the new image and all images in the training set. The 5 nearest neighbors are:

- 3 images of dogs
- 2 images of cats

We assign the label "dog" to the new image since there are more neighbors of the same class.

**Weighted K-Nearest-Neighbor Algorithm**

The Weighted K-Nearest-Neighbor Algorithm is an extension of the basic KNN algorithm. In this algorithm, each data point is assigned a weight based on its distance to the new data point. The weights are used to calculate the final prediction.

### How W-KNN Works

1. **Distance Calculation**: The algorithm calculates the distance between the new data point and all data points in the training set using a distance metric such as Euclidean distance, Manhattan distance, or Minkowski distance.
2. **Weight Calculation**: The algorithm assigns a weight to each data point based on its distance to the new data point. The weights are calculated using a function such as the inverse distance or the exponential function.
3. **Weighted Sum**: The algorithm calculates the weighted sum of the labels of the k-nearest neighbors.

### Advantages and Disadvantages

Advantages:

- Handles high-dimensional data well
- Robust to noise and outliers

Disadvantages:

- Computationally expensive for large datasets
- Sensitive to hyperparameter tuning (k and weights)

### Example

Suppose we have a dataset of images of dogs and cats, and we want to classify a new image as either a dog or a cat. We use W-KNN with k=5 and calculate the Euclidean distance between the new image and all images in the training set. The weights are calculated using the inverse distance function. The 5 nearest neighbors are:

- 3 images of dogs (distance 0.1, weight 0.9)
- 2 images of cats (distance 0.5, weight 0.5)

We calculate the weighted sum of the labels:

(3 x 0.9 x 1) + (2 x 0.5 x 0) = 2.7

We assign the label "dog" to the new image since the weighted sum is greater than 0.5.

**Nearest Centroid Classifier**

The Nearest Centroid Classifier is another similarity-based learning algorithm. In this algorithm, the centroid of each class is calculated, and the new data point is assigned to the class with the closest centroid.

### How NC Works

1. **Centroid Calculation**: The algorithm calculates the centroid of each class by taking the mean of all data points in the class.
2. **Distance Calculation**: The algorithm calculates the distance between the new data point and the centroids of all classes.
3. **Assignment**: The algorithm assigns the label of the class with the smallest distance to the new data point.

### Advantages and Disadvantages

Advantages:

- Simple to implement
- Robust to noise and outliers

Disadvantages:

- Computationally expensive for high-dimensional data
- Sensitive to hyperparameter tuning (number of clusters)

### Example

Suppose we have a dataset of images of dogs and cats, and we want to classify a new image as either a dog or a cat. We use NC with k=5 and calculate the Euclidean distance between the new image and the centroids of the two classes. The centroids are:

- Dog: (100, 100, 100)
- Cat: (50, 50, 50)

The 5 nearest neighbors are:

- 3 images of dogs (distance 0.1, centroid (102, 102, 102))
- 2 images of cats (distance 0.5, centroid (52, 52, 52))

We assign the label "dog" to the new image since the centroid of the dog class is closer.

**Locally Weighted**

Locally Weighted is a technique used in similarity-based learning to reduce the impact of noisy or outlier data points. In this technique, the weights of the data points are adjusted based on their proximity to the new data point.

### How LW Works

1. **Distance Calculation**: The algorithm calculates the distance between the new data point and all data points in the training set using a distance metric such as Euclidean distance, Manhattan distance, or Minkowski distance.
2. **Weight Calculation**: The algorithm assigns a weight to each data point based on its distance to the new data point. The weights are adjusted based on the density of the data points in the neighborhood of the new data point.
3. **Weighted Sum**: The algorithm calculates the weighted sum of the labels of the k-nearest neighbors.

### Advantages and Disadvantages

Advantages:

- Robust to noise and outliers
- Handles high-dimensional data well

Disadvantages:

- Computationally expensive for large datasets
- Sensitive to hyperparameter tuning (k and density function)

### Example

Suppose we have a dataset of images of dogs and cats, and we want to classify a new image as either a dog or a cat. We use LW with k=5 and calculate the Euclidean distance between the new image and all images in the training set. The weights are adjusted based on the density of the data points in the neighborhood of the new data point. The 5 nearest neighbors are:

- 3 images of dogs (distance 0.1, weight 0.9)
- 2 images of cats (distance 0.5, weight 0.1)

We calculate the weighted sum of the labels:

(3 x 0.9 x 1) + (2 x 0.1 x 0) = 2.7

We assign the label "dog" to the new image since the weighted sum is greater than 0.5.

**Case Studies**

1. **Image Classification**: In image classification, similarity-based learning techniques such as KNN, W-KNN, NC, and LW can be used to classify images into different categories.
2. **Time Series Forecasting**: In time series forecasting, similarity-based learning techniques such as KNN and LW can be used to predict future values based on the patterns and relationships in the data.
3. **Recommendation Systems**: In recommendation systems, similarity-based learning techniques such as KNN and LW can be used to recommend products or services based on the preferences and behavior of users.

**Applications**

1. **Computer Vision**: Similarity-based learning techniques such as KNN and NC can be used in computer vision applications such as image classification, object detection, and image segmentation.
2. **Natural Language Processing**: Similarity-based learning techniques such as KNN and LW can be used in natural language processing applications such as text classification, sentiment analysis, and topic modeling.
3. **Bioinformatics**: Similarity-based learning techniques such as KNN and NC can be used in bioinformatics applications such as protein classification, gene expression analysis, and genome assembly.

**Further Reading**

- **Book:** "Pattern Recognition and Machine Learning" by Christopher M. Bishop
- **Paper:** "A Study on the Performance of K-Nearest Neighbors Algorithm" by Y. Liu and W. Lin
- **Online Course:** "Machine Learning" by Andrew Ng on Coursera
- **Website:** "scikit-learn" by Sebastian Raschka

**Conclusion**

Similarity-based learning techniques such as Nearest-Neighbor Learning, Weighted K-Nearest-Neighbor Algorithm, Nearest Centroid Classifier, and Locally Weighted are widely used in various applications, including classification, regression, and clustering. These techniques have been shown to be effective in handling high-dimensional data and robust to noise and outliers. However, they also have some limitations, such as computational complexity and sensitivity to hyperparameter tuning. By understanding the strengths and weaknesses of these techniques, we can choose the best approach for our specific problem.
