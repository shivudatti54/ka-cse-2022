# Object Detection with R-CNN and YOLO - Summary

## Key Definitions and Concepts
- **mAP**: Area under precision-recall curve averaged across classes
- **Anchor Box**: Predefined bounding box templates for aspect ratio handling
- **ROI Pooling**: Spatial feature extraction from arbitrary regions
- **Feature Pyramid**: Multi-scale representation for detecting various object sizes

## Important Formulas and Theorems
- **IoU**: Area of overlap / Area of union
- **YOLO Loss**: λ_coord∑(coord_error) + ∑(obj_conf_error) + λ_noobj∑(noobj_conf_error) + ∑(class_error)
- **NMS Algorithm**: 1. Sort boxes by confidence 2. Remove boxes with IoU > threshold

## Key Points
- R-CNN uses region proposals → High accuracy but slow
- YOLO uses grid-based prediction → Real-time performance
- Faster R-CNN integrates RPN with detection network
- YOLOv3+ uses feature pyramids for multi-scale detection
- mAP@0.5:0.95 is standard evaluation metric
- Anchor boxes handle aspect ratio variations
- Current research focuses on transformer-based detectors

## Common Mistakes to Avoid
- Confusing R-CNN's selective search with Faster R-CNN's RPN
- Ignoring the importance of NMS in final detection quality
- Miscalculating IoU for partially overlapping boxes
- Overlooking the trade-off between input resolution and FPS

## Revision Tips
- Create comparison tables: R-CNN vs Fast R-CNN vs Faster R-CNN vs YOLO
- Practice mAP calculation with sample detection results
- Memorize YOLO's output tensor dimensions for different grid sizes
- Study ablation studies from original papers to understand design choices
- Implement simple version of NMS from scratch in Python

Length: 650 words