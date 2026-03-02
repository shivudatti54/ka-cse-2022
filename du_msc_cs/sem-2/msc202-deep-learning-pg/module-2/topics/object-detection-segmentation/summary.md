# Object Detection and Segmentation - Summary

## Key Definitions and Concepts
- Bounding Box Regression: Offset prediction for object localization
- ROI Align: Precise region feature extraction without quantization
- Anchor Boxes: Predefined aspect ratios for object proposals
- Non-Max Suppression: Eliminate overlapping predictions
- Transposed Convolution: Learnable upsampling operation

## Important Formulas and Theorems
- mAP = 1/N ∑ₖ APₖ (N classes, AP=area under PR curve)
- IoU = (Area of Overlap)/(Area of Union)
- Focal Loss: FL(pₜ) = -αₜ(1-pₜ)^γ log(pₜ)
- Dice Loss: 1 - (2|X∩Y| + ε)/(|X| + |Y| + ε)
- CIoU Loss: 1 - IoU + (ρ²(b,bᵍ)/c²) + αv

## Key Points
- Mask R-CNN adds mask head parallel to existing detection heads
- YOLOv8 introduces anchor-free split head design
- Vision Transformers process images as sequence of patches
- Domain Adaptive Faster R-CNN uses adversarial feature alignment
- Panoptic Quality = (Segmentation Quality × Recognition Quality)^0.5
- Depthwise separable convolutions reduce computational cost
- Knowledge distillation improves small model performance

## Common Mistakes to Avoid
- Confusing semantic segmentation with instance segmentation
- Forgetting to apply sigmoid/softmax in final layer
- Ignoring class imbalance in loss function selection
- Miscalculating mAP by using incorrect IoU thresholds

## Revision Tips
1. Create comparison tables: R-CNN vs YOLO vs DETR
2. Practice mAP calculation with sample detection results
3. Implement simplified U-Net using PyTorch
4. Study ablation studies from Mask R-CNN paper
5. Explore COCO dataset evaluation protocols

Length: 650 words