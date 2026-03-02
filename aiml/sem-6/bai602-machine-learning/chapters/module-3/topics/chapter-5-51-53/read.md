# **Chapter-5: Similarity-based Learning: Nearest-Neighbor Learning, Weighted K-Nearest-Neighbor Algorithm**

### 5.1: Nearest-Neighbor Learning

#### Definition

Nearest-Neighbor Learning is a type of supervised learning algorithm that classifies new, unseen data points based on their similarity to existing data points in the training set. The algorithm works by finding the closest data point to the new data point and using its class label as the predicted class label.

#### How it Works

1.  **Distance Metric**: A distance metric is used to measure the similarity between data points. Common distance metrics include Euclidean distance, Manhattan distance, and Mahalanobis distance.
2.  **Nearest Neighbor Search**: The algorithm searches for the nearest data point to the new data point in the training set.
3.  **Class Label Prediction**: The class label of the nearest data point is used as the predicted class label for the new data point.

#### Advantages

- Simple to implement
- Handles non-linear relationships between features
- Can be used for classification and regression tasks

#### Disadvantages

- Can be sensitive to noise in the data
- Can be computationally expensive for large datasets

#### Example

Suppose we have a dataset of images of cats and dogs, and we want to classify a new image as either a cat or a dog. The Nearest-Neighbor Learning algorithm would work by finding the nearest image in the training set to the new image and using its class label as the predicted class label. If the nearest image is a cat, the algorithm would predict that the new image is a cat. If the nearest image is a dog, the algorithm would predict that the new image is a dog.

### 5.2: Weighted K-Nearest-Neighbor Algorithm

#### Definition

The Weighted K-Nearest-Neighbor (WKNN) algorithm is an extension of the Nearest-Neighbor Learning algorithm that assigns weights to the nearest neighbors based on their distance to the new data point. The weights are used to determine the importance of each nearest neighbor in the classification decision.

#### How it Works

1.  **Distance Metric**: A distance metric is used to measure the similarity between data points.
2.  **Nearest Neighbor Search**: The algorithm searches for the k nearest neighbors to the new data point in the training set.
3.  **Weight Assignment**: The weights are assigned to the nearest neighbors based on their distance to the new data point. The weights are typically calculated using a decay function, such as the inverse square law.
4.  **Class Label Prediction**: The class label of the nearest neighbors is used to predict the class label of the new data point. The weighted sum of the class labels is calculated and the class with the highest weight is selected as the predicted class label.

#### Advantages

- Can handle noisy data by assigning lower weights to noisy neighbors
- Can handle non-linear relationships between features by using a weighted sum
- Can be used for classification and regression tasks

#### Disadvantages

- Can be computationally expensive for large datasets
- Can be sensitive to the choice of distance metric and weight assignment function

#### Example

Suppose we have a dataset of images of cats and dogs, and we want to classify a new image as either a cat or a dog. The WKNN algorithm would work by finding the k nearest images in the training set to the new image and assigning weights based on their distance to the new image. If the nearest images are all cats, the weights would be high and the algorithm would predict that the new image is a cat. If there are both cats and dogs in the nearest neighbors, the weights would be lower and the algorithm would predict that the new image is more likely to be a dog.

### 5.3: Comparison of Nearest-Neighbor Learning and WKNN

| Algorithm                 | Advantages                                                                  | Disadvantages                                                                                                           |
| ------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Nearest-Neighbor Learning | Simple to implement, handles non-linear relationships between features      | Sensitive to noise in the data, computationally expensive for large datasets                                            |
| WKNN                      | Can handle noisy data, can handle non-linear relationships between features | Computationally expensive for large datasets, sensitive to the choice of distance metric and weight assignment function |

In conclusion, the choice between Nearest-Neighbor Learning and WKNN depends on the specific requirements of the problem. If simplicity and ease of implementation are more important than accuracy, Nearest-Neighbor Learning may be a good choice. However, if handling noisy data and non-linear relationships between features are more important, WKNN may be a better option.
