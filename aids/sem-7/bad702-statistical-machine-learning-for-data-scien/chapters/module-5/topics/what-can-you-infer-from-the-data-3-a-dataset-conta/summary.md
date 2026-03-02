# **Revision Notes: Inferring Insights from a Car Model Dataset**

### Key Points

- **Dataset**: Contains information about car models, including:
  - Engine size (in Liters)
  - Fuel efficiency (miles per gallon)
- **Inferable Insights**: Use statistical machine learning techniques to extract meaningful information from the data.
- **Discriminant Analysis**: A supervised learning approach used to classify car models based on their characteristics.

### Important Formulas and Definitions

- **Covariance Matrix**: A matrix that describes the variance and covariance between features.
  - Formula: `Cov(X) = E[(X - E(X))(X - E(X))^T]`
- **Fisher's Linear Discriminant**: A linear transformation that maximizes the between-class scatter and minimizes the within-class scatter.
  - Formula: `F = W^T \* Cov(X) \* W`, where `W` is the eigenvector of the covariance matrix.
- **Generalized Linear Models (GLMs)**: A family of linear models that can handle non-normal response variables.
  - Formula: `g(\mu) = X\beta + \epsilon`, where `g` is the link function, `X` is the design matrix, and `\epsilon` is the error term.

### Theorems and Concepts

- **Principal Component Analysis (PCA)**: A dimensionality reduction technique that projects data onto a lower-dimensional space.
- **Bayes' Theorem**: A fundamental principle in probability theory that describes the probability of an event based on prior knowledge and new data.
- **Decision Boundary**: A hyperplane or surface that separates classes in a discriminant analysis model.

### Key Takeaways

- Use covariance matrix and Fisher's Linear Discriminant to analyze and classify car models.
- Apply GLMs to model response variables that are not normally distributed.
- Leverage PCA to reduce dimensionality and visualize high-dimensional data.
