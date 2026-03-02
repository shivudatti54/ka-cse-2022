# Hierarchical Clustering Algorithms

## Introduction to Hierarchical Clustering

Hierarchical clustering is a powerful unsupervised machine learning technique used to build a hierarchy of clusters. Unlike partitional clustering methods like K-means that require specifying the number of clusters beforehand, hierarchical clustering creates a tree-like structure (dendrogram) that shows the relationships between data points at various levels of granularity.

This approach is particularly valuable when:

- The true number of clusters is unknown
- You need to understand the data structure at multiple resolutions
- You want to visualize the relationships between data points

## Key Concepts and Terminology

### Dendrogram

A dendrogram is a tree-like diagram that records the sequences of merges or splits in hierarchical clustering. The vertical axis represents the distance or dissimilarity between clusters, while the horizontal axis shows the data points.

```
Example Dendrogram Structure:

Height/Distance
 |
 | ┌─── Cluster E
 | ┌───┤
 | │ └─── Cluster F
 |┌───┤
 ││ └─── Cluster G
 ││
 ││ ┌─── Cluster A
 ││ ┌───┤
 ││ │ └─── Cluster B
 │└───┤
 │ │ ┌─── Cluster C
 │ └───┤
 │ └─── Cluster D
 |
 +─────────────────────────────
 Data Points/Clusters
```

### Proximity Measures

The choice of distance metric significantly impacts clustering results:

| Distance Metric | Formula            | When to Use                              |
| --------------- | ------------------ | ---------------------------------------- |
| Euclidean       | √(Σ(x_i - y_i)²)   | Default choice for continuous data       |
| Manhattan       | Σ\|x_i - y_i\|     | Less sensitive to outliers               |
| Cosine          | (x·y)/(\|x\|\|y\|) | For text/data with magnitude differences |
| Mahalanobis     | √((x-y)ᵀS⁻¹(x-y))  | Accounts for correlated features         |

## Types of Hierarchical Clustering

### Agglomerative (Bottom-Up) Approach

This is the most common hierarchical clustering method. It starts with each data point as its own cluster and repeatedly merges the closest pairs of clusters until only one cluster remains.

**Algorithm Steps:**

1. Start with N clusters, each containing one data point
2. Compute the proximity matrix containing distances between all clusters
3. Find the two closest clusters and merge them
4. Update the proximity matrix to reflect the new cluster distances
5. Repeat steps 3-4 until only one cluster remains

### Divisive (Top-Down) Approach

This approach starts with all data points in one cluster and recursively splits the most heterogeneous cluster until each data point is in its own cluster.

**Algorithm Steps:**

1. Start with one cluster containing all data points
2. Identify the cluster that is most suitable for splitting
3. Split the selected cluster into two subclusters
4. Repeat steps 2-3 until each data point is in its own cluster

## Cluster Linkage Methods

The linkage method determines how the distance between clusters is calculated, which significantly affects the clustering results.

### Single Linkage (Nearest Neighbor)

The distance between two clusters is defined as the minimum distance between any two points in the different clusters.

```
Cluster A: • • •
Cluster B: • • •

Distance = minimum distance between any red and blue point
```

**Advantages:** Can detect non-elliptical shapes
**Disadvantages:** Sensitive to noise and outliers; can cause "chaining"

### Complete Linkage (Farthest Neighbor)

The distance between two clusters is defined as the maximum distance between any two points in the different clusters.

```
Cluster A: • • •
Cluster B: • • •

Distance = maximum distance between any red and blue point
```

**Advantages:** Creates compact, spherical clusters
**Disadvantages:** Breaks large clusters; sensitive to outliers

### Average Linkage

The distance between two clusters is defined as the average distance between all pairs of points in the different clusters.

```
Cluster A: • • •
Cluster B: • • •

Distance = average of all distances between red and blue points
```

**Advantages:** Compromise between single and complete linkage
**Disadvantages:** Computationally more expensive

### Ward's Method

Minimizes the total within-cluster variance. The distance between two clusters is how much the sum of squares would increase if they were merged.

**Formula:** Δ(A,B) = Σ‖x - m\_{A∪B}‖² - Σ‖x - m_A‖² - Σ‖x - m_B‖²
where m is the centroid of each cluster

**Advantages:** Tends to create clusters of approximately equal size
**Disadvantages:** Sensitive to outliers

## Implementation Example

Let's walk through a simple agglomerative clustering example with 5 data points: A(1,1), B(2,1), C(4,3), D(5,4), E(6,5)

**Step 1: Compute initial distance matrix (Euclidean distance):**

```
 A B C D E
A 0 1 3.6 5 7.1
B 1 0 2.8 4.2 6.1
C 3.6 2.8 0 1.4 2.8
D 5 4.2 1.4 0 1.4
E 7.1 6.1 2.8 1.4 0
```

**Step 2: Merge closest clusters (A and B, distance = 1)**
**Step 3: Update distance matrix using single linkage:**

```
 AB C D E
AB 0 2.8 4.2 6.1
C 2.8 0 1.4 2.8
D 4.2 1.4 0 1.4
E 6.1 2.8 1.4 0
```

**Step 4: Merge next closest (C and D, distance = 1.4)**
**Continue until all points are in one cluster**

The resulting dendrogram would show the merging sequence and distances.

## Comparison of Hierarchical Clustering Methods

| Method           | Complexity  | Best Use Case                | Limitations                         |
| ---------------- | ----------- | ---------------------------- | ----------------------------------- |
| Single Linkage   | O(n²)       | Detecting elongated clusters | Chaining effect, sensitive to noise |
| Complete Linkage | O(n²)       | Compact, spherical clusters  | Breaks large clusters               |
| Average Linkage  | O(n² log n) | Balanced approach            | Computationally expensive           |
| Ward's Method    | O(n²)       | Minimizing variance          | Sensitive to outliers               |
| Centroid Method  | O(n²)       | Similar to average linkage   | Can cause inversions in dendrogram  |

## Applications of Hierarchical Clustering

### Biological Sciences

- Phylogenetic tree construction to show evolutionary relationships
- Gene expression analysis to identify co-expressed genes
- Taxonomy classification of organisms

### Social Sciences

- Customer segmentation for marketing strategies
- Demographic analysis for policy planning
- Social network analysis to identify communities

### Information Retrieval

- Document clustering for topic modeling
- Search result organization
- Content recommendation systems

### Computer Science

- Image segmentation in computer vision
- Anomaly detection in network security
- Software module organization

## Advantages and Disadvantages

### Advantages

- No need to specify number of clusters beforehand
- Provides hierarchical structure that can be viewed at different levels
- Easy to interpret through dendrogram visualization
- Can handle any shape of similarity or distance matrix

### Disadvantages

- High computational complexity (O(n²) to O(n³))
- Sensitive to noise and outliers
- Once a merge is done, it cannot be undone (greedy algorithm)
- Different linkage methods can produce very different results

## Practical Considerations

### Data Preprocessing

- Standardize/normalize data when features have different scales
- Handle missing values appropriately
- Consider dimensionality reduction for high-dimensional data

### Determining the Number of Clusters

While hierarchical clustering doesn't require pre-specifying k, you often need to choose a cutoff point:

1. **Elbow Method:** Look for where the rate of distance increase changes sharply
2. **Domain Knowledge:** Use subject matter expertise
3. **Cluster Stability:** Analyze how clusters change with different samples

### Implementation in Python

```python
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

# Generate linkage matrix
Z = linkage(X, 'ward')

# Plot dendrogram
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data point index')
plt.ylabel('Distance')
plt.show()
```

## Exam Tips

1. **Understand Linkage Methods:** Be prepared to explain the differences between single, complete, average, and Ward's linkage methods with examples.

2. **Dendrogram Interpretation:** Practice reading dendrograms to determine cluster membership at different distance thresholds.

3. **Complexity Analysis:** Remember that hierarchical clustering has O(n²) to O(n³) complexity, making it unsuitable for very large datasets.

4. **Comparison Questions:** Be ready to compare hierarchical clustering with partitional methods like K-means in terms of advantages, disadvantages, and appropriate use cases.

5. **Distance Metrics:** Different distance metrics (Euclidean, Manhattan, Cosine) can produce different results—understand when to use each.

6. **Practical Application:** Think about real-world scenarios where hierarchical structure would be beneficial (e.g., biological taxonomy, organizational charts).

7. **Algorithm Steps:** Be able to walk through the step-by-step process of agglomerative clustering, including updating the distance matrix after each merge.
