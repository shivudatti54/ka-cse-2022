# Weighted KNN and Nearest Centroid Classifier

## Introduction to Similarity-Based Learning

Similarity-based learning algorithms are foundational approaches in machine learning that classify or predict based on the similarity between data points. Unlike parametric models that learn specific parameters from training data, these methods rely directly on the stored training instances to make predictions. Two important algorithms in this category are the **Weighted K-Nearest Neighbors (KNN)** and the **Nearest Centroid Classifier**.

## K-Nearest Neighbors (KNN) Recap

Before diving into weighted KNN, let's briefly review standard KNN:

**Standard KNN Algorithm:**
1. Store all training data points with their labels
2. For a new query point, calculate distances to all stored points
3. Select the K nearest neighbors (smallest distances)
4. Assign the most common class among these neighbors

```
Query Point (Q)
    |
    |  Calculate distances: d(Q, P₁), d(Q, P₂), ..., d(Q, Pₙ)
    |
    v
Find K smallest distances
    |
    |  Identify classes of K nearest points
    |
    v
Majority vote → Predicted Class
```

The standard KNN gives equal weight to all neighbors, regardless of their distance from the query point.

## Weighted K-Nearest Neighbors

### Concept and Motivation

**Weighted KNN** enhances the standard algorithm by assigning different weights to neighbors based on their distance from the query point. The fundamental idea is that closer neighbors should have more influence on the prediction than farther ones.

### Mathematical Formulation

In weighted KNN for classification, the predicted class is determined by:

ŷ = argmaxₖ(∑ᵢ wᵢ × I(yᵢ = k))

Where:
- ŷ is the predicted class
- k ranges over all possible classes
- wᵢ is the weight of the i-th neighbor
- I() is the indicator function (1 if true, 0 otherwise)
- yᵢ is the class of the i-th neighbor

### Weighting Schemes

Several weighting functions can be used:

1. **Inverse Distance Weighting**: wᵢ = 1 / d(Q, Pᵢ)
2. **Inverse Squared Distance**: wᵢ = 1 / d(Q, Pᵢ)²
3. **Exponential Decay**: wᵢ = exp(-α × d(Q, Pᵢ))
4. **Gaussian Kernel**: wᵢ = exp(-d(Q, Pᵢ)² / (2σ²))

### Algorithm Steps

```
Query Point (Q)
    |
    |  Calculate distances to all training points
    |
    v
Select K nearest neighbors
    |
    |  Calculate weights based on distance
    |
    v
Weighted vote → Predicted Class
```

### Example

Consider a binary classification problem with classes Red and Blue. For a query point, we find 5 nearest neighbors:

| Neighbor | Distance | Class | Weight (1/distance) |
|----------|----------|-------|---------------------|
| 1        | 1.0      | Red   | 1.00                |
| 2        | 1.5      | Red   | 0.67                |
| 3        | 2.0      | Blue  | 0.50                |
| 4        | 2.5      | Blue  | 0.40                |
| 5        | 3.0      | Blue  | 0.33                |

Total weight for Red: 1.00 + 0.67 = 1.67  
Total weight for Blue: 0.50 + 0.40 + 0.33 = 1.23  

Despite having more Blue neighbors (3 vs 2), the weighted KNN would predict Red because the closer neighbors (which have higher weights) are Red.

### Advantages of Weighted KNN

- More accurate predictions when closer neighbors are more relevant
- Reduces the influence of outliers that might be among the K neighbors
- Provides smoother decision boundaries

### Disadvantages

- More computationally intensive due to weight calculations
- Sensitive to the choice of weighting function
- Still suffers from the curse of dimensionality like standard KNN

## Nearest Centroid Classifier

### Concept and Motivation

The **Nearest Centroid Classifier** (also known as Rocchio classifier) is a simpler similarity-based approach that represents each class by its centroid (mean vector) rather than storing all individual instances.

### Mathematical Formulation

For each class c, compute the centroid:
μ_c = (1/n_c) × ∑ᵢ xᵢ where yᵢ = c

Where:
- μ_c is the centroid of class c
- n_c is the number of instances in class c
- xᵢ are the feature vectors of instances in class c

For a new query point Q, the predicted class is:
ŷ = argmin_c d(Q, μ_c)

### Algorithm Steps

```
Training Phase:
    For each class:
        Calculate centroid (mean of all points in class)
    
    Store all centroids

Prediction Phase:
    For query point Q:
        Calculate distances to all class centroids
        Assign class of the nearest centroid
```

### Example

Consider a 2D dataset with two classes:

Class A points: (1,1), (1,2), (2,1)  
Centroid A: ((1+1+2)/3, (1+2+1)/3) = (1.33, 1.33)

Class B points: (4,4), (5,5), (4,5), (5,4)  
Centroid B: ((4+5+4+5)/4, (4+5+5+4)/4) = (4.5, 4.5)

For query point Q = (2,2):
d(Q, A) = √((2-1.33)² + (2-1.33)²) = √(0.45 + 0.45) = √0.9 ≈ 0.95  
d(Q, B) = √((2-4.5)² + (2-4.5)²) = √(6.25 + 6.25) = √12.5 ≈ 3.54

Q is closer to centroid A, so predicted class is A.

### Advantages of Nearest Centroid Classifier

- Extremely fast prediction (only compare to centroids)
- Memory efficient (only store centroids, not all data points)
- Robust to noise as centroids average out outliers
- Works well when classes are roughly spherical and well-separated

### Disadvantages

- Sensitive to class imbalance (larger classes dominate centroid position)
- Fails when classes have complex shapes (non-spherical distributions)
- Cannot capture multimodal class distributions

## Comparison of Algorithms

| Aspect | Standard KNN | Weighted KNN | Nearest Centroid |
|--------|--------------|--------------|------------------|
| **Storage** | All training data | All training data | Only centroids |
| **Prediction Speed** | Slow (O(nd)) | Slower (O(nd + K)) | Fast (O(cd)) |
| **Memory Usage** | High | High | Low |
| **Handles Complex Boundaries** | Yes | Yes | No |
| **Sensitive to Noise** | Yes | Less sensitive | Robust |
| **Handles Multimodal Data** | Yes | Yes | No |
| **Parameter Tuning** | K value | K value + weighting function | None |

Where:
- n = number of training points
- d = dimensionality
- K = number of neighbors
- c = number of classes

## Implementation Considerations

### Distance Metrics

The choice of distance metric significantly impacts both algorithms:

1. **Euclidean Distance**: d(x,y) = √(∑(xᵢ - yᵢ)²)
2. **Manhattan Distance**: d(x,y) = ∑|xᵢ - yᵢ|
3. **Cosine Similarity**: cos(θ) = (x·y)/(||x|| ||y||)
4. **Minkowski Distance**: (∑|xᵢ - yᵢ|^p)^(1/p)

### Feature Scaling

Both algorithms are sensitive to feature scales. Normalization is crucial:

1. **Min-Max Scaling**: x' = (x - min)/(max - min)
2. **Z-score Normalization**: x' = (x - μ)/σ

### Parameter Selection

For weighted KNN:
- Optimal K can be found using cross-validation
- Weighting function should be chosen based on problem characteristics

## Real-World Applications

**Weighted KNN:**
- Recommender systems (closer neighbors have more influence)
- Medical diagnosis (recent similar cases more relevant)
- Fraud detection (similar transaction patterns)

**Nearest Centroid:**
- Document classification (each document represented as TF-IDF vector)
- Customer segmentation (group customers by average behavior)
- Image recognition (when classes have characteristic average features)

## Exam Tips

1. **Remember the key difference**: Weighted KNN gives more influence to closer neighbors, while standard KNN treats all neighbors equally.

2. **For calculation questions**: Always show your work step by step, especially when computing distances and weights.

3. **When to use which algorithm**: 
   - Use KNN when you have enough data and computational resources
   - Use weighted KNN when closer neighbors should matter more
   - Use nearest centroid when you need fast predictions and memory efficiency

4. **Watch for trick questions**: Nearest centroid assumes classes are spherical and may fail for complex distributions.

5. **Parameter selection**: Be prepared to discuss how you would choose K or weighting functions in practice.

6. **Comparison questions**: Focus on storage requirements, prediction speed, and ability to handle complex decision boundaries.

7. **Implementation details**: Always mention the importance of feature scaling for distance-based algorithms.