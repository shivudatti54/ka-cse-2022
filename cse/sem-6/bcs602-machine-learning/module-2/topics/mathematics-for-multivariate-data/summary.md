# Mathematics for Multivariate Data

## Overview

Machine learning algorithms are built on mathematical foundations requiring solid understanding of linear algebra, calculus, and probability. These mathematical tools—vectors/matrices for data representation, eigenvalues/eigenvectors for structure, gradients for optimization, and probability for uncertainty—are the language in which every ML algorithm is written.

## Key Points

- **Vector Operations**: Addition, scalar multiplication, dot product x·y (measures similarity), norm ||x|| (magnitude); dot product underpins linear regression, SVMs, cosine similarity
- **Matrix Operations**: Addition, scalar multiplication, multiplication (row-by-column), transpose A^T (rows↔columns); dataset is matrix (rows=observations, columns=features)
- **Matrix Inverse**: A\*A⁻¹=I; exists when det(A)≠0; used in normal equation w=(X^TX)⁻¹X^Ty and Mahalanobis distance
- **Eigenvalues/Eigenvectors**: Av=λv; eigenvectors are directions preserved under transformation, eigenvalues are scaling factors; found by solving det(A-λI)=0
- **Positive Definite**: x^TAx>0 for all non-zero x; equivalent to all eigenvalues >0; covariance matrices must be positive semi-definite
- **SVD**: A=UΣV^T; decomposes any matrix into orthogonal matrices and singular values; used for dimensionality reduction, recommender systems
- **Gradient**: ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]; points in direction of steepest ascent; gradient descent: w = w - α\*∇L(w)
- **Bayes' Theorem**: P(A|B) = P(B|A)\*P(A)/P(B); relates posterior, likelihood, prior, evidence; foundation of Naive Bayes and Bayesian inference

## Important Concepts

- Transpose properties: (A^T)^T=A, (AB)^T=B^TA^T; covariance matrix Σ=(1/(n-1))X^TX
- Determinant for 2×2: det([[a,b],[c,d]]) = ad-bc; appears in multivariate normal PDF
- Eigenvalues in ML: PCA (eigenvectors=principal components, eigenvalues=variance explained), neural network stability
- SVD works on any matrix (not just square); singular values are square roots of eigenvalues of A^TA
- Gradient descent learning rate: too large→overshooting, too small→slow convergence; gradient=0 at minima/maxima/saddle points
- Conditional probability: P(A|B) = P(A∩B)/P(B); joint probability: P(A∩B) for independent events = P(A)\*P(B)

## Notes

- Eigenvalue computation is common - practice 2×2 and 3×3 matrices: det(A-λI)=0, solve characteristic polynomial, find eigenvectors
- 2×2 inverse formula: A⁻¹ = 1/(ad-bc)\*[[d,-b],[-c,a]] - frequently asked
- Explain gradient descent algorithm and write update rule w=w-α\*∇L(w) with learning rate effect
- Bayes' theorem: memorize formula, practice numerical problems (disease testing is classic pattern)
- Connect math to ML: eigenvalues→PCA, gradient→neural network training, Bayes→Naive Bayes classifier
- SVD works on any matrix unlike eigendecomposition (square only); components are U, Σ, V^T
- Positive definite test: all eigenvalues >0; covariance matrices always positive semi-definite
