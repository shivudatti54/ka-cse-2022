# Multimodal AI - Summary

## Key Definitions and Concepts

- **Multimodal AI**: AI systems that process and integrate information from multiple sensory modalities (vision, language, audio, etc.) to form unified understanding
- **Joint Representations**: Projections of all modalities into a shared embedding space for direct comparison
- **Coordinated Representations**: Separate embedding spaces for each modality with learned alignment functions between them
- **CLIP (Contrastive Language-Image Pre-training)**: A model that learns to align images and text using contrastive learning on image-text pairs
- **Vision-Language Models (VLMs)**: Large models combining visual encoders with language models for multimodal understanding
- **Multimodal Fusion**: Techniques for combining information from different modalities—early fusion (raw features), late fusion (output combination), cross-attention fusion

## Important Formulas and Theorems

- **Contrastive Loss (InfoNCE)**: L = -log(exp(sim(img, txt)+ / τ) / Σexp(sim(img, txt') / τ)) — maximizes similarity for matched pairs, minimizes for mismatched
- **Cosine Similarity**: sim(img, txt) = (img · txt) / (||img|| × ||txt||) — measures directional alignment in embedding space
- **Zero-shot Classification**: Given class labels as text embeddings, select argmax of similarity between image embedding and all text embeddings

## Key Points

- CLIP demonstrated that language supervision from web-scale data enables powerful visual representations without human annotations
- Modern VLMs combine frozen pretrained components (CLIP encoders + LLMs) with minimal additional training through projection layers
- Cross-attention mechanisms allow dynamic interaction between modalities rather than fixed fusion rules
- Multimodal hallucination (generating descriptions not present in images) remains a significant challenge
- LLaVA training involves two stages: alignment pretraining followed by instruction tuning
- Contrastive learning benefits significantly from large batch sizes to provide diverse negative examples
- Medical AI applications benefit from combining imaging data with clinical notes for comprehensive diagnosis

## Common Mistakes to Avoid

- Confusing CLIP's zero-shot capability with actual visual understanding—CLIP relies on semantic overlap between training and test concepts
- Misunderstanding early vs. late fusion—early fusion combines before processing, late fusion combines outputs after separate processing
- Overlooking computational requirements—multimodal models with billions of parameters require substantial GPU memory
- Assuming multimodal models truly "understand" images—they statistically correlate patterns without grounded comprehension

## Revision Tips

1. Draw architecture diagrams for CLIP, LLaVA, and cross-attention mechanisms to visualize information flow
2. Implement contrastive loss calculations on small examples to understand the optimization objective
3. Review recent VLM papers (LLaVA, MiniGPT-4, BLIP-2) to understand evolution of techniques
4. Practice explaining why different fusion approaches suit different modality characteristics
5. Focus on understanding the connection between training objectives (contrastive, captioning, instruction tuning) and emergent capabilities