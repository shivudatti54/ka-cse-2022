# Multivariate Statistics

## Overview

Multivariate statistics provides formal mathematical techniques for analyzing data with multiple variables simultaneously. These techniques form the mathematical backbone of many machine learning algorithms, from linear regression to clustering, providing tools for understanding complex multivariate datasets.

## Key Points

- **Mean Vector**: Column vector containing mean of each variable; μ = [X̄1, X̄2, ..., X̄p]; serves as center of gravity for multivariate data
- **Covariance Matrix**: p×p symmetric matrix where diagonal = variances, off-diagonal = covariances; Σ = [[Var(X1), Cov(X1,X2)], [Cov(X2,X1), Var(X2)]]; positive semi-definite
- **Correlation Matrix**: Standardized covariance matrix with values in [-1,+1]; diagonal = 1; r(Xi,Xj) = Cov(Xi,Xj)/(σi\*σj); identifies multicollinearity
- **Mahalanobis Distance**: D = sqrt[(x-μ)'Σ⁻¹(x-μ)]; scale-invariant, accounts for correlations; elliptical contours vs circular Euclidean
- **Multivariate Normal Distribution**: f(x) defined by mean vector μ and covariance matrix Σ; ellipsoidal contours; central to Gaussian Naive Bayes, GMM, LDA
- **Principal Components**: Uncorrelated directions of maximum variance; eigenvectors of covariance matrix; PC1 = max variance direction

## Important Concepts

- Covariance matrix is symmetric and positive semi-definite with size p×p where p is number of variables
- Mahalanobis distance advantages: scale-invariant, handles correlations, equal distance contours are ellipsoidal not circular
- Multivariate normal fully characterized by two parameters: mean vector (location) and covariance matrix (shape/spread)
- Hotelling's T² test: multivariate extension of t-test; controls Type I error when testing multiple variables simultaneously
- MANOVA vs ANOVA: MANOVA handles multiple dependent variables accounting for correlations; test statistics include Wilks' Lambda, Pillai's Trace

## Notes

- Know how to construct covariance matrix from data - step-by-step computation frequently asked
- Understand difference: covariance (scale-dependent) vs correlation (standardized to [-1,+1])
- Explain Mahalanobis distance advantages using scale-invariance and correlation-awareness arguments
- Multivariate normal needs two parameters (mean vector, covariance matrix) with ellipsoidal contours
- Hotelling's T² vs t-test: multiple variables tested simultaneously with controlled Type I error
- PCs are eigenvectors of covariance matrix, PC1 captures maximum variance
- MANOVA advantage: handles correlated dependent variables simultaneously
