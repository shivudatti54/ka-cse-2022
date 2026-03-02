# **4. Read an Unsupervised Dataset and Group the Dataset based on Similarity using K-Means Clustering**

## **Key Points**

- **K-Means Clustering**: An unsupervised learning algorithm that groups similar data points into clusters based on their features.
- **K-Means Algorithm**: Works by:
  - Initializing K centroids randomly
  - Assigning each data point to the closest centroid
  - Updating centroids as the mean of all assigned data points
- **K-Means Clustering Formula**:
  - **Step 1:** Assign each data point to the closest centroid based on Euclidean distance.
  - **Step 2:** Update centroids as the mean of all assigned data points.
  - **Step 3:** Repeat Steps 1-2 until convergence.
- **Definitions**:
  - **Cluster**: A group of similar data points.
  - **Centroid**: The mean of all data points in a cluster.
  - **Distance Metric**: Measures the similarity between data points, e.g. Euclidean distance.
- **Theorems**:
  - **K-Means Convergence Theorem**: The algorithm converges to a local minimum of the sum of squared distances between data points and their assigned centroids.
- **Important Formulas**:
  - **Euclidean Distance**: √((x2 - x1)^2 + (y2 - y1)^2)
  - **Sum of Squared Distances**: ∑(d(x, c)^2) where d(x, c) is the Euclidean distance between x and c.

## **Revision Notes**

- Understand the K-Means algorithm and its steps.
- Know the importance of choosing the right number of clusters (K) for the dataset.
- Understand how to evaluate the quality of clusters using metrics such as silhouette score and calinski-harabasz index.
- Be able to apply K-Means clustering to real-world datasets and interpret the results.
