# Support Vector Machine (SVM)

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University

---

## 1. Introduction and Real-World Relevance

**Support Vector Machine (SVM)** is one of the most powerful and elegant supervised learning algorithms in the field of Machine Learning. Developed in the 1990s by Vladimir Vapnik and his colleagues, SVMs have become a cornerstone technique for both classification and regression tasks. The algorithm's theoretical foundation in statistical learning theory and its remarkable empirical performance have made it a staple in the toolkit of data scientists and machine learning practitioners.

### Real-World Applications

SVMs are extensively used across various domains:

- **Medical Diagnosis**: Classifying tumors as malignant or benign based on diagnostic features
- **Face Recognition**: Identifying faces in images for security systems
- **Text Categorization**: Spam detection, sentiment analysis, and document classification
- **Bioinformatics**: Protein classification and gene expression analysis
- **Finance**: Credit scoring and stock market prediction
- **Handwriting Recognition**: OCR (Optical Character Recognition) systems
- **Image Classification**: Satellite imagery analysis and object detection

### Delhi University Syllabus Context

This topic aligns with the **Machine Learning** paper under the NEP 2024 UGCF curriculum for BSc (Hons) Computer Science. Students are expected to understand the theoretical foundations, mathematical formulations, and practical implementation of SVMs.

---

## 2. Understanding SVM: The Basic Concept

### 2.1 The Intuition

The fundamental idea behind SVM is elegantly simple yet powerful: **find the optimal hyperplane that maximally separates different classes of data points.**

Consider a binary classification problem where we have two classes of points (let's call them Class +1 and Class -1). The goal is to find a decision boundary (hyperplane) that separates these classes with the maximum margin possible.

```
        •                    •
    •       •          •        •
            •  ●●●●●●●●  •
        •       •          •        •
                •                    •
                        
    ←—— Margin —→ ←—— Margin —→
                    ↑
              Optimal Hyperplane
```

### 2.2 Key Terminology

- **Hyperplane**: A decision boundary that separates classes in feature space. In n-dimensional space, it's an (n-1)-dimensional subspace.
- **Support Vectors**: The data points that lie closest to the hyperplane. These are the critical elements—removing them would change the position of the hyperplane.
- **Margin**: The distance between the hyperplane and the nearest data points (support vectors). SVM maximizes this margin.
- **Linearly Separable**: A dataset where a straight line (or hyperplane) can perfectly separate the classes.

---

## 3. Mathematical Formulation

### 3.1 Hard Margin SVM

For a linearly separable dataset, the hard margin SVM seeks to find the hyperplane that maximizes the geometric margin while correctly classifying all training examples.

**The Hyperplane Equation:**

For a feature vector **x** with dimensions, the hyperplane is defined as:

$$w \cdot x + b = 0$$

Where:
- **w** = weight vector (normal to the hyperplane)
- **b** = bias term

**Classification Rule:**

$$f(x) = \text{sign}(w \cdot x + b)$$

**Constraints:**

For a training set with labels $y_i \in \{-1, +1\}$:

$$y_i(w \cdot x_i + b) \geq 1 \quad \forall i$$

This ensures that all points are correctly classified and lie on or beyond the margin boundaries.

**The Optimization Problem:**

Maximize the margin $\frac{2}{||w||}$, which is equivalent to minimizing $||w||^2$:

$$\min_{w,b} \frac{1}{2} ||w||^2$$

subject to: $y_i(w \cdot x_i + b) \geq 1$ for all $i$

### 3.2 Soft Margin SVM (The Real-World Solution)

In practice, datasets are rarely perfectly linearly separable. Noise, outliers, and overlapping classes are common. **Soft Margin SVM** addresses this by allowing some misclassification errors.

The optimization problem becomes:

$$\min_{w,b,\xi} \frac{1}{2} ||w||^2 + C \sum_{i=1}^{n} \xi_i$$

subject to: $y_i(w \cdot x_i + b) \geq 1 - \xi_i$ and $\xi_i \geq 0$ for all $i$

Where:
- **$\xi_i$ (xi)**: Slack variables that allow points to violate the margin constraint
- **C**: Regularization parameter (NOT to be confused with L1/L2 regularization in other algorithms)

### 3.3 Understanding the C Parameter

The **C parameter** is the key regularization term in SVM:

- **Small C**: Large margin, more misclassifications allowed (high bias, low variance)
- **Large C**: Small margin, fewer misclassifications allowed (low bias, high variance)

```
        C = 0.01 (Large Margin)              C = 100 (Small Margin)
        
    •       •          •              •   •
            •  ●●●●  •                  •
        •       •          •        •
                                    
    ←——— Margin ———→            ← Margin →

    More tolerant of              Strictly separates
    errors                        classes
```

**Important Note**: Unlike L1 (Lasso) or L2 (Ridge) regularization in linear regression, SVM does not use L1/L2 penalties. The C parameter in SVM is a **margin vs. misclassification trade-off parameter**, not a traditional L1/L2 regularizer. This is a common misconception that needs to be avoided.

---

## 4. The Dual Problem

### 4.1 From Primal to Dual

The primal optimization problem (what we've defined so far) can be transformed into its **dual formulation** using Lagrangian multipliers. The dual problem is often easier to solve and, more importantly, allows us to apply the **kernel trick**.

**The Lagrangian:**

$$L(w, b, \alpha) = \frac{1}{2}||w||^2 - \sum_{i=1}^{n}\alpha_i[y_i(w \cdot x_i + b) - 1]$$

Where $\alpha_i \geq 0$ are the Lagrange multipliers.

**The Dual Problem:**

$$\max_{\alpha} \sum_{i=1}^{n}\alpha_i - \frac{1}{2}\sum_{i=1}^{n}\sum_{j=1}^{n}\alpha_i\alpha_j y_i y_j (x_i \cdot x_j)$$

subject to:
- $\sum_{i=1}^{n}\alpha_i y_i = 0$
- $\alpha_i \geq 0$ for all $i$

### 4.2 Key Properties of the Dual Solution

1. **Support Vectors**: Only data points with $\alpha_i > 0$ are support vectors. These are the only points that matter for the final decision boundary.
2. **Sparsity**: Most $\alpha_i$ values will be zero, meaning most training examples don't affect the solution.
3. **Kernel Trick**: The dual formulation involves dot products $x_i \cdot x_j$, which can be replaced with kernel functions $K(x_i, x_j)$.

### 4.3 The Final Decision Function

Once we solve the dual problem and obtain $\alpha_i$ values:

$$f(x) = \text{sign}\left(\sum_{i=1}^{n}\alpha_i y_i K(x_i, x) + b\right)$$

---

## 5. The Kernel Trick

The **kernel trick** is what makes SVM extraordinarily powerful. It allows SVM to learn non-linear decision boundaries without explicitly transforming data to higher dimensions.

### 5.1 Why Kernels?

Sometimes, data that is not linearly separable in its original space becomes linearly separable when mapped to a higher-dimensional space. For example, points on a 2D circle cannot be separated linearly, but in 3D (with the third dimension being $x_1^2 + x_2^2$), they can be.

### 5.2 Common Kernel Functions

**1. Linear Kernel:**
$$K(x_i, x_j) = x_i \cdot x_j$$

Best for: High-dimensional data (text classification, gene expression)

**2. Polynomial Kernel:**
$$K(x_i, x_j) = (x_i \cdot x_j + c)^d$$

Where $c$ is a constant and $d$ is the degree.

Best for: Image recognition with moderate dimensions

**3. Radial Basis Function (RBF) / Gaussian Kernel:**
$$K(x_i, x_j) = \exp\left(-\frac{||x_i - x_j||^2}{2\sigma^2}\right)$$

Or equivalently using gamma $\gamma = \frac{1}{2\sigma^2}$:
$$K(x_i, x_j) = \exp(-\gamma ||x_i - x_j||^2)$$

**Key Parameters:**
- **$\gamma$ (gamma)**: Defines how far the influence of a single training example reaches
  - High gamma: Close influence (overfitting risk)
  - Low gamma: Far influence (underfitting risk)

Best for: Most practical applications, especially when relationship is unknown

**4. Sigmoid Kernel:**
$$K(x_i, x_j) = \tanh(\alpha x_i \cdot x_j + c)$$

Similar to a neural network activation function.

### 5.3 Choosing the Right Kernel

| Kernel | When to Use |
|--------|-------------|
| Linear | High-dimensional data, large number of features |
| RBF | Default choice, non-linear relationships, unknown structure |
| Polynomial | When you suspect specific polynomial relationships |

---

## 6. SVM for Regression (SVR)

While SVM is primarily known for classification, it can also be used for regression tasks. **Support Vector Regression (SVR)** adapts the SVM principle to predict continuous values.

### 6.1 The SVR Concept

Instead of finding a hyperplane that separates classes, SVR finds a hyperplane that fits within a margin of tolerance (called the **epsilon tube**):

```
                    Predicted Value
                          ↑
                    ┌─────┼─────┐
                    │  ●  │  ●  │  ← Outside ε-tube: penalty applies
                    │ ●●● │ ●●● │
        ────────────┼─────┼─────┼───────────────
                    │  ●  │  ●  │
                    └─────┼─────┘
                          ↓
                    Actual Value

        ←—— ε (epsilon) ——→
```

### 6.2 SVR Mathematical Formulation

$$\min_{w,b,\xi,\xi^*} \frac{1}{2}||w||^2 + C \sum_{i=1}^{n}(\xi_i + \xi_i^*)$$

subject to:
- $y_i - (w \cdot x_i + b) \leq \epsilon + \xi_i$
- $(w \cdot x_i + b) - y_i \leq \epsilon + \xi_i^*$
- $\xi_i, \xi_i^* \geq 0$

Where:
- **$\epsilon$ (epsilon)**: The width of the tube
- **$\xi_i, \xi_i^*$**: Slack variables for points above and below the tube
- **C**: Regularization parameter controlling trade-off between tube width and penalty

---

## 7. Multi-class Classification Strategies

SVM is inherently binary (two-class) classifier. For multi-class problems, we use strategies to combine multiple binary SVMs.

### 7.1 One-vs-All (OvA) / One-vs-Rest (OvR)

**Strategy**: Train K binary SVMs (where K is the number of classes).

- SVM 1: Class 1 vs. Classes 2, 3, ..., K
- SVM 2: Class 2 vs. Classes 1, 3, ..., K
- ... and so on

**Prediction**: Apply all K classifiers; the one with highest decision value wins.

**Advantages**:
- Only K classifiers needed
- Simple to implement

**Disadvantages**:
- Class imbalance in training sets
- Ambiguous regions where multiple classes might win

### 7.2 One-vs-One (OvO)

**Strategy**: Train K(K-1)/2 binary SVMs, one for each pair of classes.

For 4 classes: 6 classifiers
- Class 1 vs. Class 2
- Class 1 vs. Class 3
- Class 1 vs. Class 4
- Class 2 vs. Class 3
- Class 2 vs. Class 4
- Class 3 vs. Class 4

**Prediction**: Each classifier votes for one class; the class with most votes wins.

**Advantages**:
- Faster training (smaller datasets per classifier)
- No class imbalance problem

**Disadvantages**:
- More classifiers to train (K(K-1)/2)

---

## 8. Implementation with Python

### 8.1 Example 1: SVM Classification on the Wine Dataset

```python
"""
SVM Classification Example - Wine Dataset
Delhi University - Machine Learning Lab
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Load the wine dataset
wine = load_wine()
X = wine.data
y = wine.target

print("Wine Dataset Information:")
print(f"Features: {X.shape[1]}")
print(f"Samples: {X.shape[0]}")
print(f"Classes: {np.unique(y)}")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Feature scaling is crucial for SVM!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Grid Search for hyperparameter tuning
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': ['scale', 'auto', 0.1, 0.01],
    'kernel': ['rbf', 'linear', 'poly']
}

print("\nPerforming Grid Search for optimal hyperparameters...")
grid_search = GridSearchCV(
    SVC(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(X_train_scaled, y_train)

print(f"\nBest Parameters: {grid_search.best_params_}")
print(f"Best CV Score: {grid_search.best_score_:.4f}")

# Train the best model
best_svm = grid_search.best_estimator_
y_pred = best_svm.predict(X_test_scaled)

# Evaluation
print("\n" + "="*50)
print("CLASSIFICATION REPORT")
print("="*50)
print(classification_report(y_test, y_pred, target_names=wine.target_names))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Support Vectors Analysis
print(f"\nNumber of Support Vectors: {best_svm.n_support_}")
print(f"Total Support Vectors: {sum(best_svm.n_support_)}")
```

### 8.2 Example 2: SVM Regression (SVR) on Synthetic Data

```python
"""
SVR Example - Predicting House Prices
Delhi University - Machine Learning Lab
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Generate synthetic housing data
np.random.seed(42)
n_samples = 200

# Features: Size (sq ft), Number of bedrooms, Age of house
size = np.random.uniform(500, 3000, n_samples)
bedrooms = np.random.randint(1, 6, n_samples)
age = np.random.randint(0, 50, n_samples)

# Target: Price (in lakhs) - with some noise
price = (0.05 * size + 2 * bedrooms - 0.1 * age + 
         np.random.normal(0, 5, n_samples) + 50)

# Create feature matrix
X = np.column_stack([size, bedrooms, age])
y = price

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features (important for SVR!)
scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_train_scaled = scaler_X.fit_transform(X_train)
X_test_scaled = scaler_X.transform(X_test)

y_train_scaled = scaler_y.fit_transform(y_train.reshape(-1, 1)).ravel()
y_test_scaled = scaler_y.transform(y_test.reshape(-1, 1)).ravel()

# Train SVR with RBF kernel
svr_rbf = SVR(kernel='rbf', C=100, gamma='scale', epsilon=0.1)
svr_rbf.fit(X_train_scaled, y_train_scaled)

# Predict
y_pred_scaled = svr_rbf.predict(X_test_scaled)
y_pred = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1)).ravel()

# Evaluation Metrics
print("="*50)
print("SVR Model Performance - House Price Prediction")
print("="*50)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f} Lakhs")
print(f"Mean Absolute Error (MAE): {mae:.2f} Lakhs")
print(f"R² Score: {r2:.4f}")

# Compare with Linear Regression
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train_scaled, y_train_scaled)
y_pred_lr = lr.predict(X_test_scaled)
r2_lr = r2_score(y_test_scaled, y_pred_lr)

print(f"\nComparison with Linear Regression R²: {r2_lr:.4f}")
print(f"SVR R²: {r2:.4f}")

# Visualize predictions vs actual
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred, alpha=0.6, edgecolors='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Price (Lakhs)')
plt.ylabel('Predicted Price (Lakhs)')
plt.title('SVR: Actual vs Predicted House Prices')

plt.subplot(1, 2, 2)
residuals = y_test - y_pred
plt.scatter(y_pred, residuals, alpha=0.6, edgecolors='k')
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Price (Lakhs)')
plt.ylabel('Residuals (Lakhs)')
plt.title('Residual Plot')

plt.tight_layout()
plt.savefig('svr_housing_results.png', dpi=150)
plt.show()

# Support Vectors in SVR
print(f"\nNumber of Support Vectors: {svr_rbf.n_support_}")
print(f"Total Support Vectors: {sum(svr_rbf.n_support_)}")
print(f"Percentage of training data as SVs: {sum(svr_rbf.n_support_)/len(y_train)*100:.1f}%")
```

---

## 9. Advantages and Disadvantages

### Advantages

1. **Effective in High Dimensions**: SVM performs well even when the number of features exceeds the number of samples
2. **Memory Efficient**: Only support vectors are stored in the final model
3. **Versatile**: Through kernel trick, can model complex non-linear relationships
4. **Robust**: Less prone to overfitting compared to some other algorithms, especially in high-dimensional spaces
5. **Well-Theorized**: Strong statistical foundation provides guarantees on performance

### Disadvantages

1. **Scalability**: Training time is between O(n²) and O(n³), making it slow on large datasets
2. **Kernel Selection**: Choosing the right kernel and hyperparameters requires expertise
3. **Sensitivity to Scaling**: Requires feature scaling (StandardScaler)
4. **No Probability Estimates**: Direct SVM gives class labels; probabilities require additional computation
5. **Not Suitable for Noisy Data**: Performance degrades with significant overlap between classes

---

## 10. Key Takeaways

1. **SVM Fundamentals**: Support Vector Machine finds the optimal hyperplane that maximizes the margin between classes, with support vectors being the critical data points defining this boundary.

2. **Mathematical Foundation**: The optimization problem minimizes $\frac{1}{2}||w||^2$ subject to classification constraints, transforming into the dual problem involving Lagrange multipliers ($\alpha_i$).

3. **Soft Margin & Regularization**: The C parameter controls the trade-off between maximizing margin and minimizing classification errors. Small C = larger margin (more tolerance); Large C = smaller margin (less tolerance).

4. **Kernel Trick**: The kernel function allows SVM to learn non-linear decision boundaries by implicitly mapping data to higher dimensions without explicit transformation.

5. **Kernel Selection**: Linear kernel for high-dimensional text data; RBF (Gaussian) kernel as the default choice for most non-linear problems; polynomial kernel for specific polynomial relationships.

6. **SVR for Regression**: Support Vector Regression uses an epsilon-insensitive tube to capture the trend while being robust to outliers within the tube.

7. **Multi-class Strategies**: One-vs-All (K classifiers) and One-vs-One (K(K-1)/2 classifiers) extend binary SVM to multi-class problems.

8. **Implementation Essentials**: Always scale features using StandardScaler, use GridSearchCV for hyperparameter tuning (C, gamma, kernel), and analyze support vectors to understand model complexity.

---

## 11. Multiple Choice Questions (Application & Analysis Level)

### Section A: Theoretical Concepts

**Question 1.** In a hard margin SVM, which of the following statements is TRUE about support vectors?

A) They are the farthest points from the decision boundary  
B) They lie exactly on the margin boundaries  
C) They are always misclassified  
D) They determine the bias term only  

**Answer: B** — Support vectors are the data points that lie exactly on the margin boundaries (where $y_i(w \cdot x_i + b) = 1$). These are the critical points that define the optimal hyperplane.

---

**Question 2.** If you increase the regularization parameter C in a soft margin SVM, what happens to the model?

A) Margin becomes wider, model becomes more regularized  
B) Margin becomes narrower, model allows fewer misclassifications  
C) The bias term becomes zero  
D) The kernel function changes automatically  

**Answer: B** — Increasing C penalizes misclassifications more heavily, forcing the model to create a narrower margin to correctly classify more training points. This reduces bias but increases variance.

---

**Question 3.** Which kernel function is typically used as the default in SVM implementations and works well for most non-linear classification problems?

A) Linear kernel  
B) Polynomial kernel  
C) Sigmoid kernel  
D) RBF (Radial Basis Function) kernel  

**Answer: D** — The RBF kernel is the default choice because it can model complex non-linear relationships without requiring explicit feature engineering, and it has only one key hyperparameter (gamma) to tune.

---

**Question 4.** In SVR (Support Vector Regression), what does the epsilon (ε) parameter represent?

A) The regularization parameter controlling model complexity  
B) The width of the epsilon-insensitive tube  
C) The kernel coefficient  
D) The learning rate  

**Answer: B** — Epsilon defines the width of the tube around the regression line. Points within this tube incur zero loss; only points outside the tube contribute to the error.

---

**Question 5.** What is the time complexity of training an SVM?

A) O(n)  
B) O(n log n)  
C) O(n²) to O(n³)  
D) O(1)  

**Answer: C** — SVM training involves solving a quadratic programming problem with complexity between O(n²) and O(n³), where n is the number of training samples. This makes SVM less scalable to very large datasets.

---

### Section B: Practical & Analytical

**Question 6.** You have a dataset with 10,000 features and only 500 samples. Which SVM configuration would you most likely use?

A) SVM with RBF kernel, high gamma  
B) SVM with linear kernel  
C) SVM with polynomial kernel, degree 10  
D) SVM with sigmoid kernel  

**Answer: B** — With high-dimensional data where features > samples (p >> n), a linear kernel is preferred. The linear kernel is less prone to overfitting in very high dimensions and is computationally efficient.

---

**Question 7.** After training an SVM model, you find that 80% of your training data are support vectors. What does this indicate?

A) The model is perfect  
B) The data is likely not linearly separable, and the model is struggling  
C) The C parameter was too small  
D) The kernel used was too complex  

**Answer: B** — A very high proportion of support vectors (often > 50%) suggests the model is close to the data points and may be overfitting. This often happens when the data is not well-separated or the hyperparameters need tuning.

---

**Question 8.** For a multi-class classification problem with 5 classes, how many binary SVM classifiers are needed for the One-vs-One strategy?

A) 5  
B) 10  
C) 15  
D) 25  

**Answer: B** — One-vs-One requires K(K-1)/2 classifiers = 5(4)/2 = 10 classifiers.

---

**Question 9.** In SVR, if you set epsilon (ε) to 0, what happens?

A) The model becomes identical to linear regression  
B) The model becomes less robust to outliers  
C) The model ignores all training points  
D) The model becomes too regularized  

**Answer: B** — With ε = 0, there's no tolerance tube; any deviation from the predicted value incurs a penalty. This makes SVR behave similarly to standard MSE regression and less robust to outliers.

---

**Question 10.** Which of the following statements about the gamma parameter in RBF kernel is CORRECT?

A) High gamma means each support vector has a wide influence  
B) Low gamma means each support vector has a local influence  
C) Gamma is independent of model complexity  
D) Low gamma typically leads to overfitting  

**Answer: D** — High gamma means the influence of each training example is very local (short radius), creating a complex, wiggly decision boundary that can overfit. Low gamma means wider influence, smoother decision boundaries, and potential underfitting.

---

### Section C: Debugging & Optimization

**Question 11.** Your SVM model is overfitting. Which combination of hyperparameter changes would MOST likely help?

A) Increase C, increase gamma  
B) Decrease C, decrease gamma  
C) Increase C, decrease gamma  
D) Decrease C, increase gamma  

**Answer: B** — To reduce overfitting: decrease C (more regularization, wider margin) and decrease gamma (wider influence, smoother decision boundary).

---

**Question 12.** Why is feature scaling (StandardScaler) essential before applying SVM?

A) It reduces the number of features  
B) SVM is sensitive to feature scales; unscaled features can cause the optimizer to be biased toward features with larger magnitudes  
C) It removes outliers from the data  
D) Scaling is not important for SVM  

**Answer: B** — SVM optimizes based on distances (dot products in feature space). Features with larger scales would dominate the distance calculations, leading to biased models. StandardScaler ensures all features contribute equally.

---

**Question 13.** You want to apply SVM to a problem where the relationship between input and output is polynomial of degree 3. Which is the BEST approach?

A) Use RBF kernel  
B) Explicitly transform features to include polynomial terms, then use linear kernel  
C) Use polynomial kernel with degree 3  
D) Use sigmoid kernel  

**Answer: C** — A polynomial kernel of degree 3 can capture polynomial relationships of that degree directly without explicit feature transformation, thanks to the kernel trick.

---

**Question 14.** In a soft margin SVM, the slack variables ($\xi_i$) represent:

A) The distance from each point to the hyperplane  
B) The extent to which each point violates the margin constraint  
C) The number of support vectors  
D) The kernel function parameter  

**Answer: B** — Slack variables ($\xi_i$) measure how much a data point violates the margin constraint. When $\xi_i > 0$, the point is on the wrong side of the margin or misclassified.

---

**Question 15.** Compared to One-vs-All, the One-vs-One strategy for multi-class SVM:

A) Requires fewer total classifiers when K is large  
B) Trains each classifier on the full dataset  
C) Trains each classifier only on data from two classes  
D) Always gives better accuracy  

**Answer: C** — One-vs-One trains K(K-1)/2 classifiers, each using only the data points from the two relevant classes, making each training problem smaller and often faster.

---

*End of Study Material*

---

**References:**

1. Vapnik, V. N. (1995). *The Nature of Statistical Learning Theory*. Springer.
2. Cortes, C., & Vapnik, V. (1995). Support-vector networks. *Machine Learning*, 20(3), 273-297.
3. Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, 2011.
4. Delhi University NEP 2024 UGCF Syllabus - Machine Learning Paper.