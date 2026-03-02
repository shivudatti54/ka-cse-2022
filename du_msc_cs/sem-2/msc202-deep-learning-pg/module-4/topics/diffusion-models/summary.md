# Diffusion Models - Summary

## Key Definitions and Concepts
- **Forward Process**: Markov chain gradually adding Gaussian noise
- **Reverse Process**: Learned denoising via parameterized transitions
- **ELBO**: Variational lower bound used as training objective
- **ᾱₜ**: Cumulative product of (1-βₜ) terms
- **Score Matching**: Alternative perspective using ∇ₓ log pₜ(x)

## Important Formulas and Theorems
- Forward process: q(xₜ|x₀) = N(xₜ; √ᾱₜ x₀, (1-ᾱₜ)I)
- Simplified loss: 𝔼[||ε - εθ(xₜ,t)||²]
- Sampling update: xₜ₋₁ = 1/√αₜ (xₜ - βₜ/√(1-ᾱₜ) εθ) + σₜ z
- DDIM sampling: xₜ₋₁ = √ᾱₜ₋₁ (xₜ/√ᾱₜ - √(1-ᾱₜ - σₜ²) εθ) + √σₜ² ε

## Key Points
- Diffusion models operate through iterative refinement
- Training involves predicting noise at each timestep
- The variance schedule critically impacts performance
- Accelerated sampling enables practical applications
- Connections exist to score-based generative models
- Current SOTA in many generative tasks
- Active research areas: 3D generation, discrete data

## Common Mistakes to Avoid
- Confusing αₜ (1-βₜ) with ᾱₜ (product of α's)
- Neglecting the importance of proper noise scheduling
- Assuming reverse process variances are learnable (often fixed)
- Overlooking temperature parameters in sampling

## Revision Tips
1. Derive the ELBO loss step-by-step from variational principles
2. Implement a basic diffusion model from scratch
3. Compare linear vs cosine schedules through ablation studies
4. Create formula flashcards for key equations
5. Study the DDPM and DDIM papers side-by-side