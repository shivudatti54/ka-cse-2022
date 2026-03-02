# Partitional Clustering: K-Means Algorithm

## Introduction to Clustering

Clustering is an **unsupervised learning** technique used to group a set of objects in such a way that objects in the same group (called a cluster) are more similar to each other than to those in other groups. Unlike classification, clustering does not rely on pre-labeled data. The goal is to discover inherent groupings within the data.

### Types of Clustering Approaches

Based on the syllabus, the main clustering approaches are:

1. **Hierarchical Clustering**: Builds a tree of clusters (dendrogram) either through agglomerative (bottom-up) or divisive (top-down) methods.
2. **Partitional Clustering**: Divides data into non-overlapping subsets (clusters) without any hierarchical structure.
3. **Density-based Clustering**: Forms clusters based on regions of high density (e.g., DBSCAN).
4. **Grid-based Clustering**: Quantizes the space into a finite number of cells and works on this quantized space.

This topic focuses on **Partitional Clustering**, specifically the **K-Means** algorithm.

## What is Partitional Clustering?

Partitional clustering aims to partition the data into `k` distinct, non-overlapping clusters. The value of `k` is typically specified by the user. Each data point belongs to exactly one cluster. The quality of a partition is often measured by the within-cluster sum of squares (WCSS), which is the sum of the squared Euclidean distances between each data point and the centroid of its assigned cluster.

## K-Means Algorithm

K-Means is the most popular and simplest partitional clustering algorithm. It is an iterative, centroid-based technique.

### Key Concepts

- **Centroid**: The mean (average) position of all the points in the cluster. It is the prototype or representative point of the cluster.
- **Within-Cluster Sum of Squares (WCSS)**: Also known as inertia or distortion. It is the sum of squared distances from each data point to its assigned centroid. K-Means aims to minimize this value.
  `WCSS = Σ (distance(point, centroid))²` for all points in all clusters.
- **Cluster Assignment**: The process of assigning each data point to the cluster whose centroid is closest (usually by Euclidean distance).

### The K-Means Algorithm Steps

The standard algorithm, often referred to as **Lloyd's algorithm**, proceeds as follows:

1. **Initialization**: Choose `k` initial cluster centroids. This can be done randomly by selecting `k` data points from the dataset or by using smarter methods like **K-Means++** (discussed later).
2. **Assignment Step**: For each data point in the dataset, calculate the distance to each centroid. Assign the data point to the cluster whose centroid is the closest.

```
For each point x_i:
find centroid μ_j that minimizes distance(x_i, μ_j)
assign x_i to cluster C_j
```

3. **Update Step**: Recalculate the centroids for each cluster. The new centroid is the mean of all data points currently assigned to that cluster.

```
For each cluster C_j:
new centroid μ_j = mean of all points in C_j
```

4. **Iteration**: Repeat the Assignment and Update steps until a stopping criterion is met. Common criteria are:

- The centroids no longer change significantly (convergence).
- The assignments of data points to clusters no longer change.
- A maximum number of iterations is reached.

#### ASCII Diagram of K-Means Iterations

```
Iteration 0 (Initialization): Iteration 1 (Assignment): Iteration 1 (Update):

 * * * C1 * * * C1 X---X *
 * * * * * * C2 * * X---X
 * ° * * * ° * * * X---X *
 ° ° * ° ° * C2 ° ° X---X
 ° ° ° ° ° ° X---X ° °

 ° = Data Point C1, C2 = Centroids X = New Centroid

Iteration 2 (Assignment): Final Clusters (Converged):

 C1 X---X * C1 X---X *
 * * X---X C2 * * X---X C2
 * X---X * * X---X *
 X---X ° ° * X---X * * *
 ° ° ° ° * * * *
```

### Choosing the Number of Clusters (k)

Selecting the right `k` is critical and often ambiguous. Since it's an unsupervised problem, there is no single right answer. The **Elbow Method** is a common heuristic used to choose `k`.

- **The Elbow Method**: Run K-Means for a range of `k` values (e.g., 1 to 10). For each `k`, calculate the total WCSS. Plot `k` against WCSS.
- **The "Elbow"**: The plot often shows an arm-shaped curve. The point where the rate of decrease in WCSS sharply changes (the "elbow") is a good candidate for the optimal `k`. After this point, adding more clusters provides diminishing returns.

```
WCSS
 |
 | *
 | *
 | * <---- The "Elbow"
 | *
 | *
 | * *
 | * *
 | * * *
 |___________________________
 k values
```

#### Example Table: WCSS for different k values

| k   | WCSS  |
| --- | ----- |
| 1   | 125.8 |
| 2   | 48.3  |
| 3   | 22.1  |
| 4   | 15.7  |
| 5   | 12.5  |
| 6   | 10.9  |
| 7   | 9.8   |
| 8   | 8.9   |

In this example, the elbow is likely at k=3 or k=4.

### K-Means++: Smarter Initialization

Standard K-Means is sensitive to the initial random placement of centroids, which can lead to suboptimal clustering. **K-Means++** addresses this by spreading out the initial centroids.

**K-Means++ Initialization Steps:**

1. Choose one centroid uniformly at random from the data points.
2. For each remaining data point, calculate the squared distance `D(x)` to the nearest, already chosen centroid.
3. Choose a new data point as the next centroid with a probability proportional to `D(x)²`. This gives points far from existing centroids a higher chance of being selected.
4. Repeat steps 2 and 3 until all `k` centroids are chosen.
5. Proceed with the standard K-Means algorithm (Assignment and Update steps).

K-Me++ leads to faster convergence and often better final results.

## Proximity/Distance Measures

The choice of distance metric is crucial. While Euclidean distance is most common, others can be used based on the data type.

| Distance Metric       | Formula (for points a and b)  | Typical Use Case                                |
| --------------------- | ----------------------------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ |
| **Euclidean**         | `√(Σ(a_i - b_i)²)`            | Physical coordinates, continuous numerical data |
| **Manhattan**         | `Σ\|a_i - b_i\|`              | Grid-like paths, categorical data               |
| **Cosine Similarity** | `(a • b) / (                  |                                                 | a   |     | \*  |     | b   |     | )`  | Text data, document similarity |
| **Jaccard**           | `1 - [\|A ∩ B\| / \|A ∪ B\|]` | Binary or set data                              |

For K-Means, using a metric like cosine similarity requires a modified version (e.g., Spherical K-Means) since the mean may not be appropriate.

## Advantages and Limitations of K-Means

### Advantages

- **Simple and Fast**: Easy to understand and implement. Computationally efficient, even for large datasets (O(n*k*i\*d)), where n=samples, k=clusters, i=iterations, d=dimensions.
- **Scalability**: Works well on large datasets due to its linear complexity.
- **Guaranteed Convergence**: Will always converge to a local minimum of WCSS.

### Limitations and Challenges

- **Sensitivity to Initial Centroids**: Different initializations can lead to different final clusters. Mitigated by K-Means++ and running the algorithm multiple times.
- **Pre-specification of k**: The user must choose the number of clusters `k`, which may not be known beforehand.
- **Sensitivity to Outliers**: Since centroids are means, outliers can drastically pull the centroid away from the true cluster center.
- **Cluster Shape Assumption**: Tends to produce spherical clusters of similar size due to the Euclidean distance metric. It performs poorly on clusters with complex geometric shapes.
- **Not Suitable for Categorical Data**: The mean is not defined for categorical data. Use K-Modes algorithm for categorical data.

## Example Application

**Problem:** Cluster customers of a mall based on their annual income and spending score.
**Data:** Two-dimensional data (Income, Spending Score).
**Process:**

1. Choose `k=5` (assuming we want to identify 5 customer segments).
2. Apply K-Means++ initialization.
3. Run K-Means iterations until convergence.
4. **Resulting Clusters might be:**

- Cluster 1: Low Income, Low Spending (Careful customers)
- Cluster 2: Low Income, High Spending (Unusual pattern, maybe reckless)
- Cluster 3: Medium Income, Medium Spending
- Cluster 4: High Income, Low Spending (Conservative customers)
- Cluster 5: High Income, High Spending (Target customers)

## Exam Tips

1. **Memorize the Steps**: Be able to write down the K-Means algorithm steps (Initialization, Assignment, Update) clearly and concisely. This is a common short-answer question.
2. **Understand WCSS**: The objective function (minimizing WCSS/Inertia) is fundamental. You will likely need to explain it.
3. **Elbow Method**: Be prepared to interpret an elbow plot and explain how it is used to choose `k`.
4. **K-Means vs. K-Means++**: Know the difference. Explain why K-Means++ is generally superior. This is a classic comparison.
5. **Limitations**: Don't just list the limitations; understand _why_ they occur (e.g., why outliers are a problem, why cluster shape is an issue).
6. **Numerical Example**: Be ready to perform a simple K-Means calculation by hand for a very small 2D dataset (2-3 points, 2 clusters). This tests your understanding of the assignment and update steps.
7. **Context is Key**: When answering long questions, relate your answer to the broader context of clustering (unsupervised learning, types of clustering) from the syllabus.
