# Image Segmentation - Summary

## Key Definitions and Concepts
- Semantic Segmentation: Classifies each pixel into categories
- Instance Segmentation: Distinguishes individual object instances
- Panoptic Segmentation: Combines semantic + instance segmentation
- Over-segmentation: Excessive region splitting (common in watershed)

## Important Formulas and Theorems
- Otsu's Variance: σ² = ω₀ω₁(μ₀-μ₁)²
- Dice Coefficient: DC = 2TP/(2TP + FP + FN)
- Mumford-Shah Functional: E = ∫(I - u)²dx + μ∫|\∇u|²dx + ν|Γ|
- CRF Energy: E(x) = ∑ψᵢ(xᵢ) + ∑ψᵢⱼ(xᵢ,xⱼ)

## Key Points
- Thresholding works best with bimodal histograms
- U-Net's skip connections preserve spatial details
- Transformers outperform CNNs in long-range dependencies
- Graph cuts require proper seed initialization
- Active contours need careful energy function design
- Instance segmentation requires mask prediction (Mask R-CNN)
- Weakly supervised methods use image-level labels

## Common Mistakes to Avoid
- Applying Otsu to non-bimodal images without preprocessing
- Ignoring class imbalance in medical segmentation
- Using Euclidean distance for color clustering without normalization
- Forgetting to apply morphological post-processing

## Revision Tips
1. Create flashcards for segmentation metrics formulas
2. Practice implementing GrabCut algorithm from scratch
3. Study ablation studies from DeepLabv3+ paper
4. Use PyTorch's torchvision.models.segmentation for quick experiments