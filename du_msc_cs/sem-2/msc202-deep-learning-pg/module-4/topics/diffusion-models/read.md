# Diffusion Models

## Introduction
Diffusion models have emerged as a powerful class of generative models that achieve state-of-the-art results in image synthesis, audio generation, and molecular design. These models work by gradually denoising data through an iterative process, inspired by non-equilibrium thermodynamics. Unlike GANs which use adversarial training, diffusion models employ a principled probabilistic framework that offers stable training and high sample quality.

The importance of diffusion models lies in their theoretical foundations and practical applications. They provide explicit likelihood estimation while maintaining sample diversity, addressing key limitations of previous generative approaches. Recent advancements like Denoising Diffusion Probabilistic Models (DDPM) and Diffusion Implicit Models (DDIM) have demonstrated superior performance in tasks ranging from text-to-image generation (e.g., DALL-E 2) to drug discovery.

From a research perspective, diffusion models bridge concepts from stochastic differential equations, variational inference, and deep learning. Their mathematical rigor makes them particularly suitable for academic investigation, while their practical effectiveness ensures real-world relevance in industries like healthcare, entertainment, and materials science.

## Key Concepts
1. **Forward Diffusion Process**: 
   - Gradually adds Gaussian noise to data over T timesteps
   - Defined by variance schedule β₁,...,β_T
   - q(xₜ|xₜ₋₁) = N(xₜ; √(1-βₜ)xₜ₋₁, βₜI)

2. **Reverse Process**:
   - Neural network (ϵθ) learns to denoise samples
   - pθ(xₜ₋₁|xₜ) = N(xₜ₋₁; μθ(xₜ,t), Σθ(xₜ,t))
   - Uses reparameterization trick for stable training

3. **Evidence Lower Bound (ELBO)**:
   - Training objective derived from variational inference
   - L = E[log pθ(x₀) - D_KL(q(x₁:T|x₀) || pθ(x₁:T|x₀))]

4. **Noise Schedule**:
   - Cosine schedule often outperforms linear for better sample quality
   - Critical for balancing noise addition/removal rates

5. **Accelerated Sampling**:
   - DDIM enables deterministic sampling with fewer steps
   - Knowledge distillation techniques for faster inference

## Examples

**Example 1: Forward Process Calculation**
Given x₀ = [1.2, -0.5], β₁=0.1, compute x₁:
```
x₁ = √(1-β₁)x₀ + √β₁ε
   = √0.9*[1.2, -0.5] + √0.1*N(0,I)
   ≈ [1.131, -0.474] + [0.316*0.32, 0.316*(-0.05)]
   ≈ [1.234, -0.490]
```

**Example 2: Reverse Process Sampling**
At step t=50 with x₅₀ = [0.8, -0.3], predict x₄₉:
```
εθ = neural_net(x₅₀, t=50) → [0.12, -0.08]
μθ = (x₅₀ - β₅₀/√(1-ᾱ₅₀) * εθ)/√(1-β₅₀)
x₄₉ = μθ + σ₅₀*z (z ∼ N(0,I))
```

**Example 3: Training Loss Computation**
For input x₀, random t=200:
1. Sample ε ∼ N(0,I)
2. Compute xₜ = √ᾱₜ x₀ + √(1-ᾱₜ) ε
3. Predict εθ = model(xₜ, t)
4. Loss = ||ε - εθ||²

## Exam Tips
1. Focus on deriving the ELBO objective from variational principles
2. Understand the role of the noise schedule in training stability
3. Be prepared to compare diffusion models with VAEs and GANs
4. Memorize key formulas: forward process q(xₜ|xₜ₋₁) and reverse process pθ
5. Practice converting between α (cumulative product) and β notations
6. Study accelerated sampling techniques (DDIM, PLMS)
7. Know recent applications like Stable Diffusion and Imagen