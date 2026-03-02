# Support Vector Machine (SVM)

## Introduction
Support Vector Machine (SVM) is a powerful supervised learning algorithm used for **classification and regression** tasks. Developed in the 1990s, SVMs are particularly effective in high-dimensional spaces and are widely used in pattern recognition, image classification, and bioinformatics. In the context of Delhi University syllabus (NEP 2024 UGCF), SVM represents a core topic in Machine Learning under unit covering classification algorithms.

---

## Key Concepts

- **Hyperplane**: The decision boundary that separates different classes in the feature space. In 2D, it's a line; in 3D, a plane.
- **Support Vectors**: The data points closest to the hyperplane that define the margin. These are the critical training examples.
- **Margin**: The distance between the hyperplane and the nearest support vectors. **Maximum Margin Classifier** aims to maximize this distance for better generalization.
- **Linear SVM**: Used when data is linearly separable (can be separated by a straight line/plane).
- **Non-linear SVM**: Used when data is not linearly separable; employs the **Kernel Trick** to map data to higher dimensions.

---

## Working Principle

1. Identify the optimal hyperplane that maximizes the margin between classes
2. Support vectors determine the position of this hyperplane
3. For non-linear data, kernel functions transform the feature space to make classes separable

---

## Kernel Functions

- **Linear Kernel**: `K(x, y) = x · y` — Used for linearly separable data
- **Polynomial Kernel**: `K(x, y) = (γx·y + r)^d` — Captures interactions between features
- **RBF (Radial Basis Function) Kernel**: `K(x, y) = exp(-γ||x - y||²)` — Most commonly used; handles non-linear relationships
- **Sigmoid Kernel**: Similar to neural network activation

---

## Advantages

- Effective in high-dimensional spaces
- Memory efficient (uses support vectors only)
- Robust against overfitting, especially in high dimensions
- Versatile through kernel functions

---

## Limitations

- Not suitable for large datasets (quadratic training complexity)
- Sensitive to feature scaling
- Performance depends on kernel choice and hyperparameters (C, γ)
- Does not provide probability estimates directly

---

## Applications

- Text and document classification
- Image recognition and computer vision
- Handwriting recognition (e.g., postal services)
- Bioinformatics (protein classification)
- Face detection systems

---

## Conclusion
SVM remains a fundamental algorithm in machine learning due to its strong theoretical foundation and excellent performance in various domains. Understanding the concept of maximum margin, support vectors, and kernel functions is essential for both theoretical exams and practical implementation. For Delhi University students, focus on the mathematical formulation of the hyperplane, kernel trick, and comparative analysis with other classifiers like Naive Bayes and Decision Trees.

**Key Reference**: Unit-III of DU B.Sc. (H) Computer Science NEP 2024 Syllabus — Supervised Learning Algorithms