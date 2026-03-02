# AI Security: Adversarial Machine Learning

## Introduction
Adversarial Machine Learning (AML) represents a critical frontier in AI security, focusing on vulnerabilities inherent in ML systems. As AI adoption accelerates across sectors (healthcare, finance, autonomous systems), understanding adversarial attacks becomes crucial for maintaining system integrity. These attacks exploit model decision boundaries through carefully crafted perturbations, often imperceptible to humans but catastrophic for AI performance.

Current research (ICML 2023, NeurIPS 2022) reveals alarming trends: 1) 92% of production ML models show vulnerability to basic adversarial attacks 2) Adaptive attacks bypass 78% of existing defenses. The arms race between attackers and defenders drives fundamental research in robust learning, differential privacy, and game-theoretic security frameworks.

## Key Concepts
1. **Attack Taxonomies**:
   - **Evasion Attacks**: Test-time input manipulation (e.g., FGSM, PGD)
   - **Poisoning Attacks**: Training data corruption (Label-flipping, Clean-label)
   - **Model Extraction**: Stealing model functionality via API queries

2. **Threat Models**:
   - White-box (Full model knowledge)
   - Black-box (Query access only)
   - Gray-box (Partial knowledge)

3. **Defense Mechanisms**:
   - Adversarial Training (Madry et al. 2018)
   - Gradient Masking (Defensive Distillation)
   - Certified Robustness (Randomized Smoothing)
   - Anomaly Detection (Mahalanobis Distance)

4. **Robustness Metrics**:
   - ℓ_p-norm bounded perturbations (ℓ₂, ℓ_∞)
   - Certified Accuracy vs Empirical Robustness
   - Adaptive Attack Success Rate

## Examples

**Example 1: Fast Gradient Sign Method (FGSM) Attack**
```python
import torch

def fgsm_attack(image, epsilon, data_grad):
    sign_grad = data_grad.sign()
    perturbed_image = image + epsilon * sign_grad
    return torch.clamp(perturbed_image, 0, 1)

# Compute loss and gradients
loss = F.nll_loss(model(images), labels)
model.zero_grad()
loss.backward()
data_grad = images.grad.data

# Generate adversarial example
perturbed_data = fgsm_attack(images, 0.3, data_grad)
```

**Example 2: TrojanNN Poisoning Attack**
1. Attacker embeds trigger pattern (e.g., yellow square) in training images
2. Labels modified to target class for triggered samples
3. Model learns to associate trigger with malicious output
4. At inference, any input with trigger activates backdoor

**Example 3: Certified Defense via Randomized Smoothing**
Given base classifier _f_, smoothed classifier _g_ predicts:
_g(x) = argmax_{c∈Y} ℙ_{δ∼N(0,σ²I)}(f(x+δ)=c)_

Certified radius _R_ = σΦ⁻¹(p_A - p_B) where p_A, p_B are top class probabilities

## Exam Tips
1. Always specify threat model when analyzing attacks/defenses
2. Understand limitations of adversarial training (gradient masking, obfuscated gradients)
3. Memorize key perturbation bounds: FGSM (ℓ_∞), PGD (iterative ℓ_p)
4. Distinguish between empirical and certified defenses
5. Know defense taxonomies: reactive vs proactive, detection vs robustness
6. Be prepared to discuss ethical implications of model extraction
7. Practice calculating certified radii for randomized smoothing