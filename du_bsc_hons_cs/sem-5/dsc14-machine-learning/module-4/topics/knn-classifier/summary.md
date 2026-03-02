# K-Nearest Neighbors (KNN) Classifier - Summary

## Key Definitions and Concepts

- **KNN (K-Nearest Neighbors)**: A supervised learning algorithm that classifies data points based on the majority class of their K nearest neighbors in the feature space.
- **Lazy Learning**: KNN is called a lazy learner because it doesn't build a model during training; it simply stores the training data and performs computations at prediction time.
- **Instance-Based Learning**: KNN is an instance-based method that uses entire training instances to make predictions.
- **Euclidean Distance**: The straight-line distance between two points: √[Σ(xᵢ - yᵢ)²]
- **Manhattan Distance**: Sum of absolute differences: Σ|xᵢ - yᵢ|
- **Minkowski Distance**: Generalized distance metric with parameter p: (Σ|xᵢ - yᵢ|^p)^(1/p)

## Important Formulas and Theorems

- **Euclidean Distance**: d(x,y) = √(Σᵢ(xᵢ - yᵢ)²)
- **Manhattan Distance**: d(x,y) = Σᵢ|xᵢ - yᵢ|
- **Minkowski Distance**: d(x,y) = (Σᵢ|xᵢ - yᵢ|^p)^(1/p)
- **Weighted KNN Weight**: w = 1/d(x, query) for inverse distance weighting

## Key Points

1. KNN is a simple, non-parametric algorithm useful for pattern recognition and classification tasks.

2. The value of K must be carefully chosen—small K leads to overfitting, large K leads to underfitting.

3. Feature scaling is mandatory for KNN since distance-based calculations are sensitive to feature magnitudes.

4. KNN performs well on low-dimensional data but suffers from the curse of dimensionality in high-dimensional spaces.

5. The algorithm requires no training phase but has O(n×d) prediction complexity.

6. Odd values of K are preferred to avoid tie situations in binary classification.

7. KNN naturally handles multi-class classification through majority voting.

8. Weighted voting gives more importance to closer neighbors, often improving accuracy.

## Common Mistakes to Avoid

1. **Forgetting feature scaling**: Applying KNN without normalization causes features with larger ranges to dominate distance calculations.

2. **Choosing inappropriate K**: Using K=1 can lead to overfitting and sensitivity to noise; using very large K can smooth out important patterns.

3. **Ignoring the curse of dimensionality**: Applying KNN directly to high-dimensional data without dimensionality reduction leads to poor performance.

4. **Assuming KNN has a training phase**: Remember that KNN "stores" data during training but does all computation at prediction time.

## Revision Tips

1. Practice calculating Euclidean and Manhattan distances manually—these are frequently tested in exams.

2. Understand why odd K values are preferred and be able to explain the bias-variance tradeoff for different K values.

3. Remember that KNN is sensitive to: feature scale, irrelevant features, noise in data, and high dimensionality.

4. Review the advantages (simple, no training, handles multi-class) and limitations (slow prediction, memory-intensive) to answer comparison questions effectively.