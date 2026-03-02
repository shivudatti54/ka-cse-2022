# AI Security: Adversarial ML - Summary

## Key Definitions and Concepts
- **Adversarial Example**: Input modified to cause model error
- **ε-Perturbation**: Allowed modification magnitude (ℓ_p norms)
- **Transferability**: Attack effectiveness across models
- **Robust Accuracy**: Performance under worst-case perturbations

## Important Formulas and Theorems
- FGSM: _x' = x + ε·sign(∇ₓL(x,y))_
- PGD Update: _x^{t+1} = Π_{B_ε(x)}(x^t + α·sign(∇ₓL))_
- Certified Radius (Cohen et al.): _R = σΦ⁻¹(p_A - p_B)_
- Min-Max Robustness: _min_θ 𝔼_{(x,y)}[max_δ L(θ,x+δ,y)]_

## Key Points
- White-box attacks leverage gradient information; black-box uses transferability
- Adversarial training improves robustness but reduces clean accuracy
- Certified defenses provide mathematical guarantees but are computationally intensive
- Model stealing enables IP theft and reconnaissance for future attacks
- Adaptive attacks bypass 89% of published defenses (Carlini et al. 2023)
- Differential privacy enhances membership inference resistance
- Hardware-level vulnerabilities (e.g., RowHammer) enable physical attacks

## Common Mistakes to Avoid
- Assuming black-box attacks are less effective than white-box
- Confusing detection rate with robustness improvement
- Overlooking temporal aspects in poisoning attacks (data drift)
- Ignoring attack transferability in distributed learning systems

## Revision Tips
- Create attack-defense matrices comparing ℓ_p bounds and computational costs
- Practice deriving FGSM/PGD updates from first principles
- Study recent ICLR papers on adaptive attack benchmarks
- Use MNIST/CIFAR-10 to implement basic attack/defense pipelines
- Memorize key statistical bounds for randomized smoothing