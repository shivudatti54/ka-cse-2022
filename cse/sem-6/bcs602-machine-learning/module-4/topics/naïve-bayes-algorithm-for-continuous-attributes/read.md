# Naïve Bayes Algorithm for Continuous Attributes

## 1. Introduction

The Naïve Bayes algorithm is a probabilistic supervised learning method widely employed for classification tasks. While conceptually straightforward, it demonstrates remarkable effectiveness across numerous real-world applications, particularly in text classification, spam detection, and medical diagnosis. This study material focuses specifically on the Naïve Bayes classifier adapted for continuous (numerical) attributes, which requires fundamentally different computational approaches compared to categorical features.

Understanding the distinction between handling discrete and continuous attributes is crucial. For discrete (categorical) features, we compute probabilities by counting occurrences in the training data. However, continuous attributes present a challenge: the probability of observing any exact value is effectively zero due to the infinite possible values a continuous variable can assume. This necessitates the use of probability density functions (PDFs) rather than discrete probability distributions.

## 2. Theoretical Foundation

### 2.1 Bayes Theorem Revisited

Bayes theorem provides the mathematical framework for the Naïve Bayes classifier. For a classification problem with feature vector **X** = (x₁, x₂, ..., xₙ) and class variable Y, Bayes theorem states:

$$P(Y = y | \mathbf{X} = \mathbf{x}) = \frac{P(\mathbf{X} = \mathbf{x} | Y = y) \cdot P(Y = y)}{P(\mathbf{X} = \mathbf{x})}$$

In practice, we compute the posterior probability P(Y|X) proportional to the likelihood P(X|Y) multiplied by the prior P(Y), since the denominator P(X) remains constant across all classes:

$$P(Y = y | \mathbf{X} = \mathbf{x}) \propto P(Y = y) \prod_{i=1}^{n} P(X_i = x_i | Y = y)$$

The classifier selects the class with the highest posterior probability:

$$\hat{y} = \arg\max_{y} P(Y = y) \prod_{i=1}^{n} P(X_i = x_i | Y = y)$$

### 2.2 The Independence Assumption

The "naïve" aspect of Naïve Bayes stems from the conditional independence assumption: all features are assumed statistically independent of each other given the class. While this assumption rarely holds in practice, the algorithm often performs surprisingly well despite violations, particularly when the dependencies are similar across classes or when partial dependence information is captured by individual features.

## 3. Handling Continuous Attributes

### 3.1 Probability Density Function (PDF)

For continuous attributes, we cannot compute P(X = x | Y = y) directly through counting. Instead, we model the class-conditional probability using a probability density function f(x | y), where:

$$P(a \leq X \leq b | Y = y) = \int_{a}^{b} f(x | y) \, dx$$

The PDF satisfies the non-negativity condition f(x) ≥ 0 and integrates to unity over the entire domain.

### 3.2 Gaussian (Normal) Distribution

The Gaussian (Normal) distribution is the most common assumption for continuous features in Naïve Bayes classification. The univariate Gaussian probability density function is:

$$f(x | \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$$

Where:

- μ (mu) = mean of the feature for a given class
- σ² (sigma squared) = variance of the feature for a given class
- σ = standard deviation

For each class y, we estimate the parameters μ_y and σ_y² from the training data using maximum likelihood estimation:

$$\mu_y = \frac{1}{n_y} \sum_{x_i \in y} x_i$$

$$\sigma_y^2 = \frac{1}{n_y} \sum_{x_i \in y} (x_i - \mu_y)^2$$

### 3.3 Gaussian Naïve Bayes Classification

The Gaussian Naïve Bayes classifier computes the class-conditional density for each feature assuming a Gaussian distribution:

$$P(X_i = x_i | Y = y) = \frac{1}{\sqrt{2\pi\sigma_{iy}^2}} \exp\left(-\frac{(x_i - \mu_{iy})^2}{2\sigma_{iy}^2}\right)$$

Where μ*{iy} and σ*{iy}² are the mean and variance of feature Xᵢ for class y.

## 4. Worked Example

Consider a binary classification problem predicting loan approval (Approved/Rejected) based on two continuous features: Income (in thousands) and Credit Score.

**Training Data:**

| Income | Credit Score | Class    |
| ------ | ------------ | -------- |
| 45     | 650          | Rejected |
| 52     | 680          | Rejected |
| 80     | 720          | Approved |
| 90     | 750          | Approved |
| 48     | 660          | Rejected |
| 85     | 730          | Approved |

**Step 1: Compute Class Priors**

- P(Approved) = 3/6 = 0.5
- P(Rejected) = 3/6 = 0.5

**Step 2: Compute Feature Statistics per Class**

For class "Approved":

- μ_Income = (80 + 90 + 85) / 3 = 85
- σ²_Income = ((80-85)² + (90-85)² + (85-85)²) / 3 = 16.67
- μ_Credit = (720 + 750 + 730) / 3 = 733.33
- σ²_Credit = ((720-733.33)² + (750-733.33)² + (730-733.33)²) / 3 = 155.56

For class "Rejected":

- μ_Income = (45 + 52 + 48) / 3 = 48.33
- σ²_Income = ((45-48.33)² + (52-48.33)² + (48-48.33)²) / 3 = 8.89
- μ_Credit = (650 + 680 + 660) / 3 = 663.33
- σ²_Credit = ((650-663.33)² + (680-663.33)² + (660-663.33)²) / 3 = 155.56

**Step 3: Classify New Instance (Income=70, Credit=700)**

Compute log-likelihoods to avoid numerical underflow:

For "Approved":
$$f(Income=70 | \mu=85, \sigma^2=16.67) = \frac{1}{\sqrt{2\pi(16.67)}} \exp\left(-\frac{(70-85)^2}{2(16.67)}\right) \approx 0.029$$
$$f(Credit=700 | \mu=733.33, \sigma^2=155.56) = \frac{1}{\sqrt{2\pi(155.56)}} \exp\left(-\frac{(700-733.33)^2}{2(155.56)}\right) \approx 0.023$$
$$\log P(Approved) + \log P(X|Approved) = \log(0.5) + \log(0.029) + \log(0.023) \approx -9.93$$

For "Rejected":
$$f(Income=70 | \mu=48.33, \sigma^2=8.89) \approx 0.0003$$
$$f(Credit=700 | \mu=663.33, \sigma^2=155.56) \approx 0.025$$
$$\log P(Rejected) + \log P(X|Rejected) = \log(0.5) + \log(0.0003) + \log(0.025) \approx -14.21$$

Since -9.93 > -14.21, the prediction is **Approved**.

## 5. Implementation in Python

```python
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Sample dataset: Income, CreditScore -> Approval (1=Approved, 0=Rejected)
X = np.array([
 [45, 650], [52, 680], [80, 720], [90, 750], [48, 660], [85, 730],
 [55, 670], [75, 710], [95, 760], [42, 640], [88, 740], [60, 690]
])
y = np.array([0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Initialize and train Gaussian Naïve Bayes
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Predict
y_pred = gnb.predict(X_test)

# Evaluate
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Rejected', 'Approved']))
```

## 6. Advantages, Limitations, and Evaluation

### 6.1 Advantages

- **Computational Efficiency**: Training and prediction are O(n·d) where n is samples and d is features
- **Handles High Dimensionality**: Performs well with many features, even with limited training data
- **Probabilistic Interpretation**: Provides calibrated probability estimates
- **Robust to Irrelevant Features**: Feature weights diminish for irrelevant attributes

### 6.2 Limitations

- **Independence Assumption**: Performance degrades when features exhibit strong correlations
- **Gaussian Assumption**: Real data may not follow normal distributions
- **Zero Probability Problem**: Features never seen with a class require smoothing (Laplace correction)
- **Feature Selection Sensitivity**: Performance depends heavily on relevant feature selection

### 6.3 Performance Evaluation Metrics

For comprehensive evaluation, employ multiple metrics:

- **Accuracy**: Proportion of correct predictions
- **Precision**: Of predicted positives, how many are truly positive
- **Recall (Sensitivity)**: Of actual positives, how many were identified
- **F1-Score**: Harmonic mean of precision and recall
- **Confusion Matrix**: Tabular representation of actual vs predicted classes

## 7. Conclusion

The Gaussian Naïve Bayes classifier extends the Naïve Bayes methodology to continuous attributes by assuming a normal distribution for class-conditional feature densities. While the independence and Gaussian assumptions represent simplifications of reality, the algorithm's computational efficiency, robustness, and competitive performance make it a valuable baseline classifier. Understanding when these assumptions hold or violate significantly informs model selection decisions in practical machine learning applications.
