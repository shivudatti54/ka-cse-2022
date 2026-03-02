# Class Balancing & Outlier Detection

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

In the realm of Machine Learning, the success of any predictive model heavily depends on the quality and characteristics of the data it learns from. Two fundamental challenges that practitioners frequently encounter are **class imbalance** and the presence of **outliers**. These issues, if not addressed properly, can severely degrade model performance and lead to biased or unreliable predictions.

This study material provides an in-depth exploration of both topics as outlined in the Delhi University NEP 2024 UGCF syllabus for BSc (Hons) Computer Science. By understanding these techniques, you will be equipped to build more robust, accurate, and fair machine learning models suitable for real-world applications.

### Real-World Relevance

Consider the following scenarios:

- **Fraud Detection**: In a dataset of 100,000 credit card transactions, only 200 might be fraudulent (0.2%). A naive model predicting all transactions as "legitimate" would achieve 99.8% accuracy but fail completely at detecting fraud.
- **Medical Diagnosis**: Rare diseases affect a small percentage of the population. An imbalanced dataset could cause a model to ignore rare but critical conditions.
- **Network Security**: Cyber attacks are rare events compared to normal traffic. Without proper handling, intrusion detection systems would miss actual threats.
- **Quality Control in Manufacturing**: Defective products are outliers in a sea of acceptable items. Detecting these anomalies is crucial for maintaining standards.

These examples underscore why mastering class balancing and outlier detection is essential for any aspiring data scientist or machine learning engineer.

---

## 2. The Class Imbalance Problem

### 2.1 What is Class Imbalance?

Class imbalance occurs when the distribution of classes in a dataset is significantly skewed. In binary classification, this typically means one class (the **minority class**) has far fewer samples than the other class (the **majority class**). The imbalance ratio (majority:minority) can range from moderate (10:1) to extreme (1000:1).

### 2.2 Why Does Class Imbalance Occur?

| Reason | Example |
|--------|---------|
| **Inherent rarity** | Fraudulent transactions, rare diseases |
| **Data collection bias** | Survey data from easily accessible groups |
| **Temporal dynamics** | Customer churn datasets where churners are naturally fewer |
| **Classification costs** | Medical tests where positive cases are costly to obtain |

### 2.3 Consequences of Ignoring Class Imbalance

1. **Biased Models**: The model becomes biased toward the majority class
2. **High Accuracy Illusion**: Accuracy can be misleading (e.g., 99% accuracy when only 1% is positive)
3. **Poor Minority Class Performance**: Recall, precision, and F1-score for minority class suffer
4. **Decision Boundary Shift**: The decision boundary shifts toward the minority class region

### 2.4 Evaluation Metrics for Imbalanced Data

When dealing with imbalanced datasets, traditional accuracy is insufficient. Consider these metrics:

- **Confusion Matrix**: Breaks down predictions into True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN)
- **Precision**: Of all positive predictions, how many are actually positive?
- **Recall (Sensitivity)**: Of all actual positives, how many did we correctly identify?
- **F1-Score**: Harmonic mean of precision and recall
- **AUC-ROC**: Area Under the Receiver Operating Characteristic Curve
- **Cohen's Kappa**: Agreement measure accounting for chance

---

## 3. Class Balancing Techniques

### 3.1 Oversampling

Oversampling involves increasing the number of samples in the minority class to balance the dataset.

#### 3.1.1 Random Oversampling

This technique randomly duplicates minority class samples until the classes are balanced.

**Advantages**: Simple to implement, preserves all original information
**Disadvantages**: Can lead to overfitting due to repeated samples

```python
import numpy as np
from sklearn.datasets import make_classification
from collections import Counter

# Create an imbalanced dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15,
                           n_redundant=5, weights=[0.9, 0.1], random_state=42)

print("Original class distribution:", Counter(y))
# Output: Original class distribution: Counter({0: 900, 1: 100})

# Random oversampling
from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X, y)

print("After random oversampling:", Counter(y_resampled))
# Output: After random oversampling: Counter({0: 900, 1: 900})
```

#### 3.1.2 SMOTE (Synthetic Minority Over-sampling Technique)

SMOTE generates synthetic samples for the minority class by interpolating between existing minority samples and their k-nearest neighbors.

**How SMOTE Works**:
1. For each minority sample, find its k nearest minority neighbors
2. Randomly select one or more neighbors
3. Generate new samples along the line connecting the original sample and the neighbor

**Advantages**: Reduces overfitting by generating synthetic samples, not just duplicating
**Disadvantages**: Can create noise if samples are near class boundaries

```python
from imblearn.over_sampling import SMOTE

# Apply SMOTE
smote = SMOTE(random_state=42, k_neighbors=5)
X_smote, y_smote = smote.fit_resample(X, y)

print("After SMOTE:", Counter(y_smote))
# Output: After SMOTE: Counter({0: 900, 1: 900})

# Visualizing SMOTE (conceptual)
print("\nSMOTE generates synthetic samples by interpolating between")
print("minority class samples and their k-nearest neighbors.")
```

#### 3.1.3 SMOTE Variants

| Technique | Description | Use Case |
|-----------|-------------|----------|
| **SMOTE-NC** | Handles categorical features | Mixed data types |
| **SMOTE-Borderline** | Focuses on boundary samples | Better separation |
| **SMOTE-ENN** | Combines SMOTE withEdited Nearest Neighbor cleaning | Noisy datasets |
| **ADASYN** | Adaptive synthetic sampling based on density | Highly imbalanced |

```python
# Example with BorderlineSMOTE
from imblearn.over_sampling import BorderlineSMOTE

bsmote = BorderlineSMOTE(random_state=42, k_neighbors=5)
X_bs, y_bs = bsmote.fit_resample(X, y)

print("After BorderlineSMOTE:", Counter(y_bs))
```

### 3.2 Undersampling

Undersampling reduces the number of majority class samples to match the minority class.

#### 3.2.1 Random Undersampling

Randomly removes majority class samples until balanced.

**Advantages**: Simple, reduces training time
**Disadvantages**: May discard important information from majority class

```python
from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler(random_state=42)
X_under, y_under = rus.fit_resample(X, y)

print("After random undersampling:", Counter(y_under))
# Output: After random undersampling: Counter({0: 100, 1: 100})
```

#### 3.2.2 NearMiss

NearMiss selects majority samples based on their proximity to minority samples using k-NN.

```python
from imblearn.under_sampling import NearMiss

nm = NearMiss(version=1, n_neighbors=3)
X_nm, y_nm = nm.fit_resample(X, y)

print("After NearMiss:", Counter(y_nm))
```

#### 3.2.3 Tomek Links

Tomek Links identifies pairs of nearest neighbors from different classes and removes majority samples.

```python
from imblearn.under_sampling import TomekLinks

tl = TomekLinks()
X_tl, y_tl = tl.fit_resample(X, y)

print("After Tomek Links:", Counter(y_tl))
```

### 3.3 Hybrid Approaches

Combining oversampling and undersampling often yields better results.

#### 3.3.1 SMOTETomek

Combines SMOTE with Tomek Links for cleaning.

```python
from imblearn.combine import SMOTETomek

stk = SMOTETomek(random_state=42)
X_stk, y_stk = stk.fit_resample(X, y)

print("After SMOTETomek:", Counter(y_stk))
```

#### 3.3.2 SMOTEENN

Combines SMOTE with Edited Nearest Neighbors for cleaning.

```python
from imblearn.combine import SMOTEENN

senn = SMOTEENN(random_state=42)
X_senn, y_senn = senn.fit_resample(X, y)

print("After SMOTEENN:", Counter(y_senn))
```

### 3.4 Ensemble Methods

#### 3.4.1 Balanced Bagging

Uses bagging with balanced subsets.

```python
from imblearn.ensemble import BalancedBaggingClassifier
from sklearn.tree import DecisionTreeClassifier

bbc = BalancedBaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=10,
    random_state=42
)
bbc.fit(X_train, y_train)
```

#### 3.4.2 EasyEnsemble

Creates multiple balanced subsets of the majority class.

```python
from imblearn.ensemble import EasyEnsembleClassifier

eec = EasyEnsembleClassifier(n_estimators=10, random_state=42)
eec.fit(X_train, y_train)
```

---

## 4. Outlier Detection

### 4.1 What are Outliers?

Outliers are data points that significantly differ from other observations. They can indicate measurement errors, rare events, or novel phenomena. Outlier detection (also called anomaly detection) is crucial in fraud detection, network intrusion detection, fault diagnosis, and many other domains.

### 4.2 Statistical Methods

#### 4.2.1 Z-Score Method

The Z-score measures how many standard deviations a data point is from the mean:

$$Z = \frac{x - \mu}{\sigma}$$

Typically, points with |Z| > 3 are considered outliers.

**Advantages**: Simple, fast, works well for normally distributed data
**Disadvantages**: Sensitive to extreme values (mean and std affected by outliers)

```python
import numpy as np
import pandas as pd

# Sample data
data = np.array([10, 12, 14, 15, 14, 13, 12, 11, 100, 13, 14, 15])
data_df = pd.DataFrame(data, columns=['value'])

# Calculate Z-scores
mean = data_df['value'].mean()
std = data_df['value'].std()
data_df['z_score'] = (data_df['value'] - mean) / std

# Identify outliers (|Z| > 2)
outliers_zscore = data_df[np.abs(data_df['z_score']) > 2]
print("Outliers using Z-score (threshold=2):")
print(outliers_zscore)
# The value 100 will be identified as an outlier

# Using scipy
from scipy import stats

z_scores = np.abs(stats.zscore(data))
outliers = np.where(z_scores > 2)
print("\nOutlier indices:", outliers[0])
```

#### 4.2.2 IQR (Interquartile Range) Method

IQR is the difference between the 75th and 25th percentiles:

$$IQR = Q3 - Q1$$

Outliers are defined as values below Q1 - 1.5×IQR or above Q3 + 1.5×IQR.

**Advantages**: Robust to outliers, works well for skewed data
**Disadvantages**: May miss outliers in small datasets

```python
# IQR Method
Q1 = data_df['value'].quantile(0.25)
Q3 = data_df['value'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")

outliers_iqr = data_df[(data_df['value'] < lower_bound) | 
                        (data_df['value'] > upper_bound)]
print("\nOutliers using IQR:")
print(outliers_iqr)
```

### 4.3 Machine Learning Methods

#### 4.3.1 Isolation Forest

Isolation Forest isolates observations by randomly selecting features and split values. Outliers are easier to isolate (require fewer splits).

**How It Works**:
1. Build random decision trees
2. Randomly select a feature and split value
3. Outliers have shorter path lengths in the tree
4. Anomaly score = average path length / expected path length

**Advantages**: Efficient for high-dimensional data, doesn't require distance calculations
**Disadvantages**: May not work well with local density variations

```python
from sklearn.ensemble import IsolationForest
import numpy as np

# Create sample data with outliers
np.random.seed(42)
X_normal = np.random.normal(loc=0, scale=1, size=(300, 2))
X_outliers = np.random.normal(loc=5, scale=1, size=(20, 2))
X = np.vstack([X_normal, X_outliers])

# Fit Isolation Forest
iso_forest = IsolationForest(contamination=0.06, random_state=42)
predictions = iso_forest.fit_predict(X)

# -1 indicates outliers, 1 indicates inliers
outliers = X[predictions == -1]
inliers = X[predictions == 1]

print(f"Number of outliers detected: {len(outliers)}")
print(f"Number of inliers: {len(inliers)}")

# Get anomaly scores
scores = iso_forest.decision_function(X)
print(f"\nAnomaly scores (lower = more anomalous):")
print(f"Min score: {scores.min():.4f}, Max score: {scores.max():.4f}")
```

#### 4.3.2 DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

DBSCAN clusters points based on density. Points in low-density regions (noise) are considered outliers.

**How It Works**:
1. Core points: Points with ≥ min_samples neighbors within ε distance
2. Border points: Reachable from core points but not core themselves
3. Noise points: Not reachable from any core point

**Advantages**: Can find clusters of arbitrary shape, doesn't require pre-specifying number of clusters
**Disadvantages**: Sensitive to parameter selection (ε, min_samples)

```python
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np

# Create sample data with outliers
np.random.seed(42)
# Normal cluster
X_cluster = np.random.randn(200, 2) * 0.5 + [0, 0]
# Outliers
X_outliers = np.random.uniform(-5, 5, size=(20, 2))
X = np.vstack([X_cluster, X_outliers])

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=5)
labels = dbscan.fit_predict(X_scaled)

# -1 label indicates outliers (noise)
outliers_dbscan = X[labels == -1]
print(f"Number of outliers detected by DBSCAN: {len(outliers_dbscan)}")
print(f"Number of clusters: {len(set(labels)) - (1 if -1 in labels else 0)}")
```

### 4.4 Comparing Outlier Detection Methods

| Method | Best For | Limitations | Type |
|--------|----------|--------------|------|
| Z-Score | Normal distributions, known variance | Affected by outliers | Statistical |
| IQR | Skewed data, known distributions | May miss extreme outliers | Statistical |
| Isolation Forest | High-dimensional data, large datasets | Local density issues | ML-based |
| DBSCAN | Arbitrary shaped clusters | Parameter sensitivity | ML-based |
| Local Outlier Factor | Varying densities | Computational cost | ML-based |

---

## 5. Practical Example: Combining Class Balancing and Outlier Detection

In real-world scenarios, you often need to handle both issues simultaneously. Here's a comprehensive pipeline:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Step 1: Generate synthetic imbalanced dataset with outliers
np.random.seed(42)
# Normal class (majority)
X_majority = np.random.randn(1000, 4) * 2 + [10, 20, 30, 40]
y_majority = np.zeros(1000)
# Minority class with some outliers
X_minority = np.random.randn(100, 4) * 2 + [15, 25, 35, 45]
# Add outliers to minority
X_outliers = np.random.uniform(20, 60, size=(10, 4))
X_minority = np.vstack([X_minority, X_outliers])
y_minority = np.ones(110)

# Combine
X = np.vstack([X_majority, X_minority])
y = np.concatenate([y_majority, y_minority])

print("Original class distribution:", np.bincount(y.astype(int)))

# Step 2: Remove outliers (assuming we know which are true anomalies)
iso_forest = IsolationForest(contamination=0.01, random_state=42)
outlier_mask = iso_forest.fit_predict(X)
X_clean = X[outlier_mask == 1]
y_clean = y[outlier_mask == 1]

print("After outlier removal:", np.bincount(y_clean.astype(int)))

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_clean, y_clean, test_size=0.2, random_state=42, stratify=y_clean
)

# Step 4: Apply SMOTE to training data only
smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

print("After SMOTE:", np.bincount(y_train_balanced.astype(int)))

# Step 5: Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_balanced)
X_test_scaled = scaler.transform(X_test)

# Step 6: Train model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train_balanced)

# Step 7: Evaluate
y_pred = model.predict(X_test_scaled)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
```

---

## 6. Key Takeaways

### Class Balancing

1. **Class imbalance** occurs when one class significantly outnumbers another, leading to biased models
2. **Oversampling** (SMOTE, ADASYN) generates synthetic minority samples through interpolation
3. **Undersampling** (Random, NearMiss, Tomek Links) reduces majority class samples
4. **Hybrid methods** (SMOTETomek, SMOTEENN) combine both approaches for better results
5. **Ensemble methods** (BalancedBagging, EasyEnsemble) use multiple balanced subsets
6. Always apply balancing **only to training data**, not test data
7. Use appropriate metrics (F1-score, AUC-ROC) rather than accuracy

### Outlier Detection

1. **Outliers** are data points significantly different from others and may indicate errors or anomalies
2. **Z-score** works well for normally distributed data but is sensitive to extreme values
3. **IQR method** is robust to outliers and works with skewed distributions
4. **Isolation Forest** efficiently detects outliers in high-dimensional data through random partitioning
5. **DBSCAN** identifies outliers as noise points in low-density regions
6. The choice of method depends on data characteristics, dimensionality, and domain context
7. Handle outliers carefully—sometimes they contain valuable information

---

## 7. Assessment Section

### Multiple Choice Questions (MCQs)

**Question 1:** In a dataset with 1000 negative samples and 10 positive samples, what is the imbalance ratio?
- a) 1:10
- b) 10:1
- c) 100:1
- d) 1000:10

**Question 2:** Which metric is most appropriate for evaluating a model on imbalanced data?
- a) Accuracy
- b) Precision
- c) F1-Score
- d) Both b and c

**Question 3:** SMOTE stands for:
- a) Synthetic Minority Oversampling Technique
- b) Simplified Minority Over-sampling Technique
- c) Statistical Minority Oversampling Technique
- d) Standard Minority Oversampling Technique

**Question 4:** What is the primary disadvantage of random oversampling?
- a) It removes important information
- b) It can lead to overfitting
- c) It is computationally expensive
- d) It only works with numerical data

**Question 5:** In the IQR method for outlier detection, outliers are values below:
- a) Q1 - IQR
- b) Q1 - 1.5 × IQR
- c) Q1 - 2 × IQR
- d) Q1 - 3 × IQR

**Question 6:** Isolation Forest is based on the principle that:
- a) Outliers are denser than inliers
- b) Outliers are easier to isolate than normal points
- c) Outliers have higher variance
- d) Outliers are always far from the mean

**Question 7:** In DBSCAN, what label is assigned to outlier points?
- a) 0
- b) 1
- c) -1
- d) None

**Question 8:** Which technique should be used AFTER applying SMOTE to clean up noisy samples?
- a) RandomUnderSampler
- b) NearMiss
- c) Tomek Links
- d) BorderlineSMOTE

**Question 9:** When applying class balancing, which data should be balanced?
- a) Test set only
- b) Training set only
- c) Both training and test sets
- d) Neither

**Question 10:** A Z-score of -2.5 indicates the data point is:
- a) 2.5 standard deviations above the mean
- b) 2.5 standard deviations below the mean
- c) 2.5 times the mean
- d) 0.25 standard deviations below the mean

**Question 11:** EasyEnsemble is an example of:
- a) Oversampling technique
- b) Undersampling technique
- c) Ensemble technique for imbalanced data
- d) Feature selection technique

**Question 12:** The contamination parameter in Isolation Forest represents:
- a) The expected proportion of outliers in the data
- b) The number of trees to build
- c) The maximum depth of each tree
- d) The random state for reproducibility

---

### Flashcards

| Term | Definition |
|------|------------|
| **Class Imbalance** | A condition where the distribution of classes in a dataset is significantly skewed |
| **Minority Class** | The class with fewer samples in an imbalanced dataset |
| **SMOTE** | Synthetic Minority Over-sampling Technique - generates synthetic minority samples through interpolation |
| **Oversampling** | Technique to increase minority class samples to balance the dataset |
| **Undersampling** | Technique to reduce majority class samples to balance the dataset |
| **Z-Score** | Number of standard deviations a data point is from the mean |
| **IQR** | Interquartile Range - difference between 75th and 25th percentiles |
| **Outlier** | A data point that significantly differs from other observations |
| **Isolation Forest** | An algorithm that isolates outliers by random partitioning |
| **DBSCAN** | Density-based clustering algorithm that identifies noise points as outliers |
| **Precision** | Proportion of true positive predictions among all positive predictions |
| **Recall (Sensitivity)** | Proportion of actual positives correctly identified |
| **F1-Score** | Harmonic mean of precision and recall |
| **AUC-ROC** | Area Under the Receiver Operating Characteristic Curve |
| **Tomek Links** | Pairs of nearest neighbors from different classes used for cleaning |
| **SMOTETomek** | Hybrid method combining SMOTE with Tomek Links |
| **Contamination** | Expected proportion of outliers in the data |
| **Core Point** | In DBSCAN, a point with at least min_samples neighbors within ε distance |
| **Noise Point** | In DBSCAN, a point not reachable from any core point |
| **BalancedBaggingClassifier** | Ensemble method using bagging with balanced subsets |

---

## 8. References and Further Reading

1. Chawla, N.V., et al. (2002). "SMOTE: Synthetic Minority Over-sampling Technique." *JAIR*.
2. Liu, F.T., et al. (2008). "Isolation Forest." *Proceedings of the 8th IEEE International Conference on Data Mining*.
3. Ester, M., et al. (1996). "A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases." *KDD*.
4. Delhi University NEP 2024 UGCF Syllabus - Machine Learning Paper
5. Scikit-learn Documentation: Imbalanced-learn
6. Python Data Science Handbook by Jake VanderPlas

---

*This study material is prepared in accordance with the BSc (Hons) Computer Science curriculum under NEP 2024 UGCF at Delhi University.*