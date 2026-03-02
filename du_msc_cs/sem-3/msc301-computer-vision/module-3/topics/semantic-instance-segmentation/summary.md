# Semantic-Instance Segmentation - Summary

## Key Definitions and Concepts
- **Semantic Segmentation**: Pixel-wise classification without instance distinction
- **Instance Segmentation**: Identifies individual object instances
- **Panoptic Quality (PQ)**: Combines recognition (RQ) and segmentation quality (SQ)

## Important Formulas and Theorems
- **mIoU**: \(\frac{1}{C}\sum_{c=1}^C \frac{TP_c}{TP_c + FP_c + FN_c}\)
- **Average Precision**: \(\int_0^1 p(r) dr\) where p(r) is precision-recall curve
- **Dice Coefficient**: \(\frac{2|X \cap Y|}{|X| + |Y|}\)

## Key Points
- Mask R-CNN extends Faster R-CNN with mask prediction branch
- Vision transformers outperform CNNs in long-range context modeling
- Label ambiguity at object boundaries is a major challenge
- COCO and Cityscapes are benchmark datasets
- CRF (Conditional Random Fields) are used for post-processing
- Instance segmentation requires both classification and pixel grouping
- Real-time systems use knowledge distillation (e.g., YOLACT++)

## Common Mistakes to Avoid
- Confusing semantic segmentation metrics with instance-level AP
- Ignoring NMS in object detection pipelines
- Overlooking memory constraints in high-resolution segmentation
- Mishandling overlapping instances in post-processing

## Revision Tips
1. Create comparative tables: FCN vs U-Net vs Mask R-CNN
2. Practice mIoU calculations on sample segmentation maps
3. Review state-of-the-art papers from CVPR 2023/2024
4. Implement a mini Mask R-CNN using PyTorch Lightning