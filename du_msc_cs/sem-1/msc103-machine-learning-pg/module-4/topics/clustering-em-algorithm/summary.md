# Clustering: EM Algorithm - Summary

## Key Definitions and Concepts
- **Latent Variables**: Unobserved variables explaining data structure
- **Responsibility**: γ(z_nk) = P(z_k=1|x_n), cluster membership probability
- **Q-function**: Expected complete-data log likelihood
- **GMM**: p(x) = Σ_{k=1}^K π_k N(x|μ_k,Σ_k)

## Important Formulas and Theorems
- **E-Step**: γ(z_nk) = π_k N(x_n|μ_k,Σ_k) / Σ_j π_j N(x_n|μ_j,Σ_j)
- **M-Step Updates**:
  μ_k = (Σ_n γ(z_nk)x_n)/N_k
  Σ_k = (Σ_n γ(z_nk)(x_n-μ_k)(x_n-μ_k)^T)/N_k
  π_k = N_k/N
  where N_k = Σ_n γ(z_nk)
- **ELBO**: log p(X|θ) ≥ Q(θ,θ⁰) + H(q) (Evidence Lower Bound)

## Key Points
- EM guarantees monotonic improvement in observed-data likelihood
- Computational complexity O(NKT) for N points, K clusters, T iterations
- Sensitive to initialization; common to use K-means++ for starting values
- Handles missing data through marginalization in E-step
- Bayesian variants using MAP estimation prevent singular covariance
- Recent applications in NLP (topic models) and genomics (haplotype phasing)
- Parallel EM implementations exist for distributed computing

## Common Mistakes to Avoid
- Forgetting to normalize responsibilities during E-step
- Assuming EM always finds global maximum (it doesn't)
- Using EM with improper covariance matrices (needs regularization)
- Ignoring computational complexity in high dimensions

## Revision Tips
1. Practice deriving M-step updates for different covariance types
2. Implement EM for 2D data with visualization of responsibility changes
3. Compare log-likelihood trajectories with different initializations
4. Study connection to variational inference frameworks
5. Review recent papers on EM acceleration techniques (e.g., ECM, SEM)