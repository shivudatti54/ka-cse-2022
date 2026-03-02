# Nearest Centroid Classifier - Summary

## Key Definitions

- **Centroid**: The mean vector of all training samples belonging to a specific class, calculated as μ_c = (1/n_c) × Σx_i for all samples x_i in class c.
- **Nearest Centroid Classifier**: A classification algorithm that assigns a test instance to the class whose centroid is nearest to it in the feature space.
- **Shrinkage**: A regularization technique in NCC that pulls class centroids toward the global mean to reduce overfitting.
- **Linear Decision Boundary**: The hyperplane that separates classes, formed as the perpendicular bisector between class centroids.

## Important Formulas

- **Centroid Calculation**: μ_c = (1/n_c) × Σᵢ₌₁ⁿᶜ xᵢ
- **Euclidean Distance**: d(x, μ_c) = ||x - μ_c|| = √[Σⱼ₌₁ᵈ(xⱼ - μ_cⱼ)²]
- **Decision Boundary (2 classes)**: 2(μ₂ - μ₁)·x = μ₂² - μ₁²
- **Shrunk Centroid**: μ_c(shrink) = [(n_c × μ_c + m × μ_global)] / (n_c + m), where m is the shrinkage parameter

## Key Points

1. The Nearest Centroid Classifier is a parametric algorithm that stores only one prototype (centroid) per class, making it extremely memory efficient.

2. Classification time is O(d × c) where d is the feature dimension and c is the number of classes, as distances are computed only to c centroids.

3. The algorithm assumes that each class can be represented by its mean vector and that classes are linearly separable.

4. All features should be normalized or standardized before applying NCC, as distance calculations are sensitive to feature scales.

5. The decision boundary between two classes is a hyperplane that is equidistant from both centroids.

6. NCC serves as a baseline classifier and is often used for comparison with more complex algorithms.

7. The algorithm works well when class distributions are spherical with similar variances, but performance degrades for irregular or heavily skewed distributions.

8. Shrunk NCC provides better generalization by introducing bias that reduces variance, particularly beneficial for high-dimensional data.

## Common Mistakes

1. **Forgetting Feature Scaling**: Applying NCC to unscaled data where features have different ranges, causing features with larger scales to dominate distance calculations.

2. **Ignoring Class Imbalance**: Not accounting for classes with significantly different numbers of samples, which can lead to biased centroids.

3. **Applying to Non-Linearly Separable Data**: Expecting good performance when classes have complex, overlapping, or non-linear decision boundaries.

4. **Confusing with k-NN**: Mistaking NCC for instance-based learners; NCC does not consider local neighborhood information but relies on global class centroids.