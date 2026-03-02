# Feature Scaling and Selection

## Introduction

In the realm of machine learning, the quality of input data fundamentally determines the performance of any model. Two critical preprocessing techniques that significantly impact model performance are **Feature Scaling** and **Feature Selection**. These techniques address different challenges: scaling ensures that features are on similar scales so that no single feature dominates the learning process, while selection identifies and retains only the most relevant features, reducing noise and computational complexity.

For students preparing for DU semester examinations, understanding when and how to apply these techniques is essential. Real-world datasets, such as those encountered in the famous Iris dataset or housing price prediction problems, often contain features measured in vastly different units—some in thousands (like house prices), others in fractions (like crime rates). Without proper scaling, algorithms like K-Nearest Neighbors, Support Vector Machines, and Neural Networks may produce biased results. Similarly, in high-dimensional datasets with hundreds or thousands of features, feature selection becomes crucial to prevent overfitting and improve model interpretability.

This topic forms the foundation for building robust machine learning pipelines and is frequently tested in both theoretical and practical examinations at Delhi University.

## Key Concepts

### Feature Scaling

Feature scaling transforms the values of features to a specific range or distribution. This is particularly important for distance-based algorithms and gradient descent-based optimization.

**1. Min-Max Scaling (Normalization)**

Min-Max scaling transforms features to a fixed range, typically [0, 1]. The formula is:

$$X_{scaled} = \frac{X - X_{min}}{X_{max} - X_{min}}$$

This technique is particularly useful when:
- The data has known bounds
- You need positive values only
- Algorithms like Neural Networks expect inputs in a specific range

However, Min-Max scaling is sensitive to outliers, as outliers can significantly affect the range.

**2. Standardization (Z-score Normalization)**

Standardization rescales features to have zero mean and unit variance:

$$X_{scaled} = \frac{X - \mu}{\sigma}$$

where μ is the mean and σ is the standard deviation.

This method is preferred when:
- The data follows a Gaussian distribution
- Algorithms assume normally distributed features (like Logistic Regression, Linear Regression)
- Outliers are present (less affected than Min-Max)

**3. Robust Scaling**

Robust scaling uses the interquartile range (IQR) instead of min-max:

$$X_{scaled} = \frac{X - Q_2}{Q_3 - Q_1}$$

This method is highly resistant to outliers and is ideal when your dataset contains significant outliers.

### Feature Selection

Feature selection involves choosing a subset of relevant features for model building. It addresses the "curse of dimensionality" and improves model performance, interpretability, and training speed.

**1. Filter Methods**

Filter methods evaluate feature relevance independently of the machine learning algorithm, using statistical tests:

- **Correlation Coefficient**: Measures linear relationship between features and target. Features highly correlated with the target are selected, while highly correlated feature pairs (r > 0.9) may cause multicollinearity.

- **Chi-Square Test**: Used for categorical features and classification problems. It tests independence between features and the target variable.

- **ANOVA F-test**: Used for continuous features and categorical targets (classification) or continuous targets (regression).

- **Mutual Information**: Measures the dependency between variables, capturing both linear and non-linear relationships.

**2. Wrapper Methods**

Wrapper methods use a machine learning model to evaluate feature subsets. They are computationally expensive but often yield better results:

- **Forward Selection**: Starts with no features and iteratively adds the most significant feature at each step.

- **Backward Elimination**: Starts with all features and iteratively removes the least significant feature.

- **Recursive Feature Elimination (RFE)**: Recursively builds models and removes the weakest features based on model coefficients or feature importance.

**3. Embedded Methods**

Embedded methods perform feature selection during model training, combining the benefits of both filter and wrapper methods:

- **Lasso Regression (L1 Regularization)**: Can shrink some feature coefficients to exactly zero, effectively performing feature selection.

- **Ridge Regression (L2 Regularization)**: Shrinks coefficients but rarely to zero, useful for multicollinearity.

- **Tree-based Feature Importance**: Random Forest and Gradient Boosting provide feature importance scores based on how much each feature contributes to reducing impurity.

**4. Dimensionality Reduction**

While not strictly feature selection, Principal Component Analysis (PCA) transforms features into a smaller set of uncorrelated components:

- PCA projects data onto principal components that capture maximum variance
- Useful when features are highly correlated
- Loses interpretability as original features are transformed

## Examples

### Example 1: Applying Feature Scaling

Consider a housing dataset with two features:
- Area: ranges from 500 to 5000 sq ft
- Price: ranges from ₹10,00,000 to ₹5,00,00,000

**Without scaling**: A distance-based algorithm like KNN would make Area (500-5000) dominate over Price (10L-5Cr) in distance calculations, even though Price might be more predictive.

**With Min-Max Scaling**:
- For a house with Area = 2000 sq ft and Price = ₹2,00,00,000:
  - Area_scaled = (2000 - 500) / (5000 - 500) = 0.375
  - Price_scaled = (20000000 - 1000000) / (50000000 - 1000000) = 0.3877

Both features now contribute equally to the distance calculation.

### Example 2: Filter-based Feature Selection using Correlation

Given a dataset with features: Age, Income, Education_years, Experience, Distance_from_city, and Target: Salary

Correlation with Salary:
- Age: 0.65
- Income: 0.85
- Education_years: 0.72
- Experience: 0.78
- Distance_from_city: -0.12

**Interpretation**: 
- Distance_from_city has very low correlation (|0.12| < 0.3 threshold)
- This feature can be dropped as it provides minimal predictive value
- Other features show strong positive correlation with salary and should be retained

### Example 3: Wrapper Method - Forward Selection

For a binary classification problem with features {F1, F2, F3, F4}:

**Step 1**: Train models with each single feature, select best:
- Model with F1: Accuracy = 0.75
- Model with F2: Accuracy = 0.68
- Model with F3: Accuracy = 0.72
- Model with F4: Accuracy = 0.70
→ Select F1

**Step 2**: Add one more feature to F1:
- F1 + F2: 0.79
- F1 + F3: 0.81 (best)
- F1 + F4: 0.77
→ Add F3

**Step 3**: Continue until no improvement
- F1 + F3 + F2: 0.80 (no improvement)
- F1 + F3 + F4: 0.79 (no improvement)

**Final selection**: {F1, F3}

## Exam Tips

1. **Always scale features for distance-based algorithms** (KNN, SVM, K-Means) and gradient descent-based methods (Neural Networks, Logistic Regression).

2. **Use Standardization when data is normally distributed** and Min-Max when you need bounded values in [0,1].

3. **For datasets with outliers, prefer Robust Scaling** using median and IQR instead of mean and standard deviation.

4. **Correlation threshold of 0.3-0.5** is commonly used in DU exams to determine feature relevance in filter methods.

5. **Lasso (L1) performs feature selection** by setting coefficients to zero, while Ridge (L2) only shrinks coefficients but retains all features.

6. **Wrapper methods are accurate but computationally expensive** - remember this trade-off in exam answers.

7. **PCA is dimensionality reduction, not feature selection** - it creates new components rather than selecting existing features.

8. **Feature selection reduces overfitting** by eliminating noise and irrelevant features, particularly important in high-dimensional datasets.

9. **For tree-based algorithms (Random Forest, XGBoost)**, scaling is NOT required as they are insensitive to feature scales.

10. **In exam questions, always justify your choice** of scaling/selection method based on the algorithm being used and the nature of data.