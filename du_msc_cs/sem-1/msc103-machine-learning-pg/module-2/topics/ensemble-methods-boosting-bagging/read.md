# Ensemble Methods: Boosting and Bagging

## Introduction
Ensemble methods represent a paradigm shift in machine learning where multiple models are strategically combined to solve complex prediction problems. These techniques have become fundamental in modern ML due to their ability to enhance prediction accuracy, reduce overfitting, and handle diverse data types. The University of Delhi's MSc CS program emphasizes these methods due to their dominance in competitive data science (Kaggle competitions) and industry applications (fraud detection, recommendation systems).

Boosting and bagging constitute two principal approaches with distinct philosophical foundations. While bagging (Bootstrap Aggregating) focuses on variance reduction through parallel model training, boosting sequentially builds models that correct predecessors' errors. Recent research directions like gradient boosting machines (GBM) and adaptive boosting variants demonstrate their continued relevance in deep learning era.

## Key Concepts
1. **Bootstrap Aggregating (Bagging)**
   - Creates multiple subsets via bootstrap sampling (random selection with replacement)
   - Trains base learners (typically decision trees) on each subset
   - Final prediction through majority voting (classification) or averaging (regression)
   - Key Algorithm: Random Forest (with feature bagging for decorrelation)

2. **Boosting Framework**
   - Iterative correction of previous models' errors
   - Weighted training instances: misclassified points get higher weights
   - Adaptive Boosting (AdaBoost): Exponential loss minimization
   - Gradient Boosting Machines (GBM): Generalizes boosting via gradient descent

3. **Theoretical Foundations**
   - Bias-Variance Tradeoff: Bagging reduces variance, boosting reduces bias
   - PAC Learning Framework for boosting's error bounds
   - Recent Advancements: XGBoost (regularized gradient boosting), CatBoost (categorical handling)

4. **Stacking & Blending**
   - Meta-learning approach combining diverse base models
   - Uses cross-validated predictions as features for meta-model

## Examples

**Example 1: AdaBoost Implementation**
Problem: Classify XOR dataset with 4 points: (0,0)→0, (1,1)→0, (0,1)→1, (1,0)→1

Solution:
1. Initialize weights: w_i = 1/4 for all
2. First weak classifier (vertical line x=0.5):
   - Misclassifies (0,1) and (1,0)
   - Error ε = 0.5
   - α = 0.5 * ln((1-ε)/ε) = 0
   (Reinitialize weights as equal)
3. Second classifier (horizontal line y=0.5):
   - Perfect separation
   - Final model combines both with updated α weights

**Example 2: Random Forest Feature Importance**
Dataset: Boston Housing (13 features)
Implementation:
1. Grow 100 trees with max_depth=5
2. Calculate mean decrease in impurity (MDI):
   - CRIM (0.24), RM (0.18), LSTAT (0.31)
3. Out-of-bag error estimation: 2.85 vs linear regression's 3.12

**Example 3: Gradient Boosting for Imbalanced Data**
Problem: Fraud detection (1:100 class ratio)
Solution:
1. Use XGBoost with scale_pos_weight=100
2. Custom asymmetric loss function penalizing FN more than FP
3. SHAP values for explainability: top features = transaction_frequency, geo_velocity

## Exam Tips
1. Always contrast bagging/boosting: parallel vs sequential, homogeneous vs weighted models
2. Memorize AdaBoost's weight update rule: α_t = ½ ln[(1-ε_t)/ε_t]
3. For numerical problems, practice GBM's pseudo-residual calculation
4. Understand when to prefer Random Forest (high variance data) vs XGBoost (structured data)
5. Recent research focus: Neural Network ensembles, Bayesian interpretation of boosting
6. Always mention computational aspects: bagging's parallelizability vs boosting's sequential nature
7. Prepare case studies: Netflix Prize (ensemble of ensembles), COVID-19 prediction models