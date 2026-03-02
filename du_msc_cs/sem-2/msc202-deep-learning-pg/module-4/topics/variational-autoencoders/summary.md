# Variational Autoencoders - Summary

## Key Definitions and Concepts
- **VAE**: Generative model combining encoder qφ(z|x), prior p(z), decoder pθ(x|z)
- **ELBO**: Evidence Lower Bound, L(θ,φ) = 𝔼q[log pθ(x|z)] - D_KL(qφ(z|x)||p(z))
- **Reparameterization**: z = μ + σ⊙ε, ε ∼ N(0,I) enables differentiable sampling
- **Posterior Collapse**: When q(z|x) ≈ p(z), decoder ignores latent codes

## Important Formulas and Theorems
- ELBO Decomposition: log p(x) ≥ ELBO = Reconstruction - KL Regularization
- KL for Gaussians: D_KL(N(μ,σ²)||N(0,I)) = ½∑(μ² + σ² - logσ² -1)
- SGVB Estimator: ∇φ𝔼qφ(z)[f(z)] ≈ 𝔼p(ε)[∇φf(gφ(ε,x))]

## Key Points
- VAEs enable principled Bayesian inference in neural networks
- Latent space structure controlled by KL term weight (β parameter)
- Mode-seeking behavior leads to blurry samples compared to GANs
- Hierarchical VAEs (NVAE) achieve state-of-the-art likelihoods
- Applications: Data generation, anomaly detection, representation learning
- Current research: Discrete VAEs (VQ-VAE), Riemannian latent spaces
- Evaluation metrics: ELBO value, FID scores, downstream task performance

## Common Mistakes to Avoid
- Forgetting to exponentiate log-variance in KL calculation
- Using BCE loss for non-binary data without proper scaling
- Ignoring KL annealing leading to posterior collapse
- Mishandling sequential data temporal dependencies in encoder

## Revision Tips
1. Practice deriving ELBO from KL(q||p) formulation
2. Implement VAE on MNIST with different β values
3. Study ablation studies from original VAE paper
4. Explore HuggingFace implementations of VAE-Transformers
5. Review ICLR papers on addressing posterior collapse

Length: 732 words