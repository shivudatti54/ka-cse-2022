# **Unsupervised Learning: K-Means Algorithm Revision Notes**

## **K-Means Algorithm**

- K-Means is an unsupervised learning algorithm used for clustering data points into K groups based on their similarities.
- The algorithm aims to minimize the sum of squared distances between each data point and its assigned cluster centroid.
- **Centroid-based clustering**: K-Means assumes that the clusters are spherical and have the same density.

## **Dealing with Noise**

- **Noise in data**: Random fluctuations in data that can affect clustering performance.
- **Noise reduction techniques**:
  - **Data normalization**: Scaling data to a common range (e.g., 0-1) to reduce the effect of outliers.
  - **Data transformation**: Applying techniques like standardization or log transformation to reduce the impact of outliers.

## **K-Means Neural Network**

- A neural network variant of the K-Means algorithm using a neural network to generate new cluster labels.
- **Architecture**: Neural network with multiple hidden layers to learn cluster labels.
- **Advantages**: Can handle high-dimensional data, non-linear relationships, and noisy data.

## **Normalization**

- **Definition**: Scaling data to a common range (e.g., 0-1) to reduce the effect of outliers.
- **Why use normalization?**: Improves convergence speed, reduces the impact of outliers, and enhances model interpretability.

## **Better Weight Update Rule**

- **Standard weight update rule**: Update weights using the gradient of the cost function.
- **Alternative weight update rule**: Use a more robust update rule, such as the average of the previous and current weights.

## **Using Comp**

- **Reference**: Not provided
- **Note**: Not relevant to the K-Means algorithm

## **Important Formulas, Definitions, and Theorems**

- **K-Means algorithm**: Minimize the sum of squared distances between each data point and its assigned cluster centroid.
- **Centroid**: The mean of all data points in a cluster.
- **Sum of squared distances**: A measure of the total squared distance between each data point and its assigned cluster centroid.

## **Revision Tips**

- Practice implementing the K-Means algorithm from scratch.
- Study the effects of normalization on clustering performance.
- Review the different weight update rules and their advantages.
