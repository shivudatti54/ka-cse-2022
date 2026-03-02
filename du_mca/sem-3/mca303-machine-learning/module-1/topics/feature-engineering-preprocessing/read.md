# Feature Engineering & Preprocessing

## Introduction
Feature engineering and preprocessing form the foundation of effective machine learning systems. While algorithms get most attention, research shows data quality and feature relevance account for 80% of model success. This process transforms raw data into meaningful representations that capture underlying patterns while addressing real-world data challenges like missing values, outliers, and inconsistent formats.

In DU's MCA program context, mastering these techniques is crucial for developing industry-ready ML solutions. From financial fraud detection to medical diagnosis systems, proper feature handling directly impacts model accuracy and deployment viability. The process includes data cleaning, transformation, construction, and selection - each requiring both statistical understanding and domain knowledge.

Modern applications demand sophisticated handling of diverse data types: temporal sequences in IoT systems, high-dimensional text in NLP, and spatial features in computer vision. This topic bridges theoretical concepts from linear algebra and probability with practical implementation using tools like pandas and scikit-learn.

## Key Concepts

1. **Data Cleaning**
   - Missing Data: Techniques like mean/median imputation, KNN imputation, and predictive modeling
   - Outlier Handling: Z-score methods, IQR ranges, and robust scaling
   - Deduplication: Hashing techniques for big data

2. **Feature Transformation**
   - Normalization: Min-max scaling (0-1 range)
   - Standardization: Z-score normalization (μ=0, σ=1)
   - Log/Power Transforms: For skewed distributions
   - Binning: Converting continuous to categorical features

3. **Feature Construction**
   - Polynomial Features: Creating interaction terms (x₁², x₁x₂)
   - Domain-Specific Features: BMI from height/weight, time-based features
   - Embedding Layers: For deep learning text representations

4. **Feature Selection**
   - Filter Methods: Pearson correlation, χ²-test
   - Wrapper Methods: Forward/backward selection
   - Embedded Methods: Lasso regression, tree importance

5. **Categorical Encoding**
   - One-Hot Encoding: For nominal data
   - Target Encoding: Mean substitution for high-cardinality features
   - Hashing Trick: For memory-constrained systems

6. **Advanced Techniques**
   - Handling Imbalanced Data: SMOTE, ADASYN
   - Temporal Features: Rolling averages, time since events
   - Automated Feature Engineering: Using libraries like FeatureTools

## Examples

**Example 1: Handling Missing Data in Titanic Dataset**
```python
# Load data
df = pd.read_csv('titanic.csv')

# Analyze missingness in Age column
print(df['Age'].isnull().sum())  # 177 missing

# Create indicator feature
df['Age_missing'] = df['Age'].isnull().astype(int)

# MICE imputation
from sklearn.experimental import enable_iterative_imputer
imputer = IterativeImputer(max_iter=10)
df['Age'] = imputer.fit_transform(df[['Age']])
```

**Example 2: Text Feature Extraction with TF-IDF**
```python
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'DU offers MCA program',
    'Machine learning is core in MCA',
    'Feature engineering improves models'
]

tfidf = TfidfVectorizer(stop_words='english')
X = tfidf.fit_transform(corpus)
print(tfidf.get_feature_names_out())
# ['core', 'engineering', 'feature', 'improves', 'learning', 'machine', 'models', 'offers', 'program']
```

**Example 3: Feature Scaling for Housing Prices**
```python
from sklearn.preprocessing import RobustScaler

# Original prices with outliers
prices = [[200000], [300000], [2500000], [180000]]

scaler = RobustScaler(quantile_range=(25, 75))
scaled_prices = scaler.fit_transform(prices)
# Output: [-0.5, 0.0, 10.5, -1.0] 
# Mitigates 2.5M outlier effect
```

## Exam Tips
1. Always mention the train-test split before preprocessing to avoid data leakage
2. For categorical variables with >50 categories, prefer target encoding over one-hot
3. When comparing normalization vs standardization, note that SVM and KNN need standardization
4. SMOTE creates synthetic minority samples using k-NN (typically k=5)
5. PCA is sensitive to scaling - always standardize first
6. L1 regularization (Lasso) performs feature selection by zeroing coefficients
7. Target encoding requires careful validation to prevent overfitting