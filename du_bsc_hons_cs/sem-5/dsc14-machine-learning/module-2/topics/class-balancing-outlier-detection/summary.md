# Class Balancing & Outlier Detection

## Introduction

Class Balancing and Outlier Detection are crucial preprocessing techniques in Machine Learning that significantly impact model performance. Class balancing addresses the problem of imbalanced datasets where certain classes are underrepresented, while outlier detection identifies anomalous data points that can skew results. These techniques are essential for building robust, accurate ML models and are covered in the Delhi University NEP 2024 UGCF syllabus for BSc (Hons) Computer Science.

---

## Key Concepts

### Class Balancing

- **Class Imbalance Problem**: Occurs when the distribution of classes in a dataset is significantly skewed (e.g., fraud detection where fraudulent transactions are rare)
- **Impact**: Models become biased toward majority class, poor recall for minority class
- **Techniques**:
  - **Undersampling**: Reducing majority class samples
  - **Oversampling**: Increasing minority class samples (random oversampling)
  - **SMOTE (Synthetic Minority Over-sampling Technique)**: Generates synthetic samples by interpolating between minority class instances
  - **Class Weights**: Assigning higher weights to minority class during training
  - **Hybrid Methods**: Combining undersampling and oversampling (e.g., SMOTETomek)

### Outlier Detection

- **Definition**: Identifying observations that deviate significantly from the majority of data
- **Types of Outliers**:
  - Point Outliers: Single anomalous data points
  - Contextual Outliers: Anomalous in specific contexts
  - Collective Outliers: Collection of related anomalous data
- **Detection Methods**:
  - **Statistical Methods**: Z-score, IQR (Interquartile Range), Grubbs' test
  - **Distance-Based**: K-Nearest Neighbors distance, Mahalanobis distance
  - **Density-Based**: Local Outlier Factor (LOF), DBSCAN
  - **Machine Learning Approaches**: Isolation Forest, One-Class SVM, Autoencoders
  - **Supervised Methods**: Classification algorithms trained on labeled outlier data

### Relationship Between Class Balancing & Outlier Detection

- Outliers in minority class can be mistaken for noise or may represent critical anomalies
- Proper outlier handling before class balancing improves synthetic sample generation
- Both techniques improve model generalization and reduce bias

---

## Conclusion

Class balancing and outlier detection are essential data preprocessing steps that ensure machine learning models perform accurately across all classes and are not misled by anomalous data. Understanding when and how to apply these techniques is vital for solving real-world problems like fraud detection, medical diagnosis, and network security. Students should practice implementing these methods using Python libraries (imbalanced-learn, scikit-learn) to gain hands-on experience.

---

*Relevant for Delhi University BSc (Hons) CS NEP 2024 UGCF – Machine Learning Unit III & IV*