# Pattern Classification and the Minimum Distance Classifier

## Introduction to Pattern Classification

Pattern classification is a fundamental concept in computer vision and machine learning. It is the process of assigning a physical object or an event to one of several pre-defined categories or _classes_. This object or event is represented by a set of measurements, known as a **pattern**.

The goal is to design a **classifier**—a system that can automatically assign these patterns to their correct classes based on their features.

**Key Terminology:**

- **Pattern:** An n-dimensional vector of feature measurements, often represented as a point in an n-dimensional space called the **feature space**. For example, `x = [feature1, feature2, ..., feature_n]`.
- **Class:** A category or label (e.g., 'cat', 'dog', 'apple', 'orange').
- **Feature:** A measurable property of the phenomenon being observed (e.g., color histogram, texture, area, perimeter).
- **Feature Vector:** The ordered set of features representing a pattern.
- **Classifier:** A function or algorithm that maps a feature vector to a class label.
- **Training:** The process of teaching a classifier using labeled data (patterns with known class labels).
- **Testing:** The process of evaluating the classifier's performance on unseen data.

## The Pattern Classification Pipeline

The process of pattern classification typically involves the following stages, from the raw input image to the final classified output:

```
+-------------+      +-------------------+      +-----------------+      +------------------+
|   Raw Input | -->  | Pre-processing &  | -->  |   Feature       | -->  |   Classification |
|   Image     |      | Segmentation      |      |   Extraction    |      |                  |
+-------------+      +-------------------+      +-----------------+      +------------------+
         |                    |                           |                         |
     Acquisition        Noise reduction,          Calculate descriptors     Assign a class label
                     isolate Region of Interest   (e.g., area, shape)        based on features
```

**1. Pre-processing and Segmentation:** The input image is first cleaned (noise removal) and then segmented to isolate the objects of interest from the background. Morphological operations like erosion, dilation, opening, and closing are crucial here.

**2. Feature Extraction:** This is the most critical step. Descriptive, measurable, and discriminative properties (**features**) are calculated from the segmented object. These features should be:

- **Invariant:** Unchanged by transformations like rotation, scaling, or translation.
- **Discriminative:** Able to differentiate between objects of different classes.
  Common features include geometric properties (area, perimeter, compactness), moment invariants, and texture descriptors.

**3. Classification:** The extracted feature vector is fed into a classifier, which compares it to known patterns and assigns a class label.

## Introduction to Classifiers

A classifier defines **decision boundaries** in the feature space that separate the regions belonging to different classes. The complexity of these boundaries depends on the classifier used.

```
Feature 2
    ^
    |    Class A    |    Class B
    |     o o       |      x x
    |   o     o     |    x     x
    |     o   o     |      x x
    |       o       |        x
    +---------------|--------------> Feature 1
            Decision Boundary
```

_ASCII Diagram 1: A simple linear decision boundary separating two classes._

## The Minimum Distance Classifier (MDC)

The Minimum Distance Classifier is one of the simplest and most intuitive classification algorithms. It operates on a very straightforward principle: **an unknown pattern belongs to the class whose representative is closest to it.**

### How it Works

1.  **Training Phase:** For each class, compute a **prototype** or a representative vector. The most common prototype is the **mean vector** (centroid) of all training patterns belonging to that class.
    - Let `μ₁, μ₂, ..., μ_c` be the mean vectors for classes `1, 2, ..., C`.

2.  **Classification Phase:** For an unknown pattern vector `x`:
    a. Calculate the distance between `x` and every class prototype `μ_i`.
    b. Assign `x` to the class `j` for which this distance is minimized.

    `Assign x to Class j if d(x, μ_j) = min_{i=1,...,C} d(x, μ_i)`

### Distance Metrics

The choice of distance metric `d(x, μ)` is crucial. The most common metric is the **Euclidean Distance**.

- **Euclidean Distance:** The straight-line distance between two points in space.
  `d_euclidean(x, μ) = √( (x₁ - μ₁)² + (x₂ - μ₂)² + ... + (x_n - μ_n)² )`

- **Manhattan Distance:** The sum of absolute differences.
  `d_manhattan(x, μ) = |x₁ - μ₁| + |x₂ - μ₂| + ... + |x_n - μ_n|`

- **Mahalanobis Distance:** A more sophisticated metric that accounts for correlations between features and different scales. It is statistically more efficient.
  `d_mahalanobis(x, μ) = √( (x - μ)^T Σ^{-1} (x - μ) )` where `Σ` is the covariance matrix.

For the basic MDC, Euclidean distance is most frequently used.

### Geometric Interpretation

The decision boundary created by the MDC consists of hyperplanes that are perpendicular bisectors of the lines joining the prototype points. The resulting decision regions are **Voronoi cells** in the feature space, where each cell contains all points closer to one prototype than to any other.

```
Prototype for Class A (μ_A)
          o
          | \
          |   \
          |     \    Perpendicular
          |       \   Bisector
          |         \
----------+----------- Decision Boundary
          |         /
          |       /
          |     /    Perpendicular
          |   /       Bisector
          | /
          o
    Prototype for Class B (μ_B)
```

_ASCII Diagram 2: Decision boundary as a perpendicular bisector between two prototypes._

### Advantages and Disadvantages

| Advantage                                               | Disadvantage                                                                      |
| :------------------------------------------------------ | :-------------------------------------------------------------------------------- |
| **Simple** to understand and implement.                 | Assumes classes are **spherical** and of **similar size**.                        |
| **Fast** training and classification.                   | Performs poorly if classes are **not linearly separable** or have complex shapes. |
| Works well when classes are compact and well-separated. | The simple mean prototype is sensitive to **outliers** in the training data.      |

## Step-by-Step Numerical Example

Let's classify an unknown pattern `x = [4, 3]` using two classes.

**Training Data:**

- **Class 1 (ω₁):** [1, 2], [2, 1], [2, 3]
- **Class 2 (ω₂):** [4, 5], [5, 4], [5, 5]

**Step 1: Compute Prototypes (Mean Vectors)**

- `μ₁ = [ (1+2+2)/3 , (2+1+3)/3 ] = [5/3, 6/3] = [1.67, 2.00]`
- `μ₂ = [ (4+5+5)/3 , (5+4+5)/3 ] = [14/3, 14/3] = [4.67, 4.67]`

**Step 2: Calculate Euclidean Distance from `x` to each prototype**

- `d(x, μ₁) = √( (4 - 1.67)² + (3 - 2.00)² ) = √( (2.33)² + (1.00)² ) = √(5.4289 + 1) = √6.4289 ≈ 2.54`
- `d(x, μ₂) = √( (4 - 4.67)² + (3 - 4.67)² ) = √( (-0.67)² + (-1.67)² ) = √(0.4489 + 2.7889) = √3.2378 ≈ 1.80`

**Step 3: Assign the Pattern**
Since `d(x, μ₂) ≈ 1.80` is less than `d(x, μ₁) ≈ 2.54`, we assign the unknown pattern `x = [4, 3]` to **Class 2 (ω₂)**.

## Relationship to Morphology and Feature Extraction

The Minimum Distance Classifier sits at the end of a processing chain that starts with morphological operations.

1.  **Morphological Processing** (e.g., erosion, dilation) is used to clean up a segmented image, remove noise, and separate touching objects. This creates a clean, distinct Region of Interest (ROI) for each object.
2.  **Feature Extraction** then calculates descriptive numerical values from these clean ROIs. Examples include:
    - **Area:** Number of pixels in the region.
    - **Perimeter:** Length of the boundary of the region.
    - **Compactness:** (Perimeter²) / Area (a shape descriptor; circle has minimal compactness).
    - **Moment Invariants:** Features invariant to rotation, scale, and translation.
3.  These extracted features form the pattern vector `x` which is the input to the classifier.

## Exam Tips

1.  **Understand the Pipeline:** Be able to describe the full workflow from image to classification, explaining the role of morphology and feature extraction.
2.  **Prototype Calculation:** You will almost certainly be asked to calculate a class mean prototype from a set of sample points.
3.  **Distance Calculation:** Practice calculating Euclidean (and sometimes Manhattan) distance. Remember the formula.
4.  **Draw the Diagram:** For 2D examples, sketching the feature space with points and the decision boundary can help visualize the problem and avoid calculation errors.
5.  **Know the Limitations:** Always be prepared to discuss the advantages and disadvantages of the MDC, especially its assumption of spherical classes. Contrast it with more complex classifiers that can handle non-linear boundaries.
6.  ** Terminology:** Be precise with terms like _pattern_, _feature vector_, _class_, _prototype_, and _classifier_.
