# Object Detection and Segmentation

## Introduction
Object detection and segmentation form the cornerstone of modern computer vision systems. While object detection identifies and localizes objects using bounding boxes, segmentation provides pixel-level understanding through masks. These techniques power critical applications ranging from autonomous vehicles (identifying pedestrians) to medical imaging (tumor segmentation) and satellite imagery analysis.

The field has evolved from traditional computer vision approaches to deep learning paradigms. Current research focuses on improving efficiency (real-time processing), handling scale variations (Feature Pyramid Networks), and addressing domain shifts (cross-domain adaptation). The emergence of Transformer-based architectures like DETR and MaskFormer demonstrates the ongoing innovation in this space.

## Key Concepts
1. **Two-Stage Detectors**: 
   - R-CNN family: Region-based CNN with selective search → Fast R-CNN (ROI pooling) → Faster R-CNN (Region Proposal Network)
   - Mask R-CNN: Extends Faster R-CNN with parallel mask prediction branch

2. **Single-Stage Detectors**:
   - YOLO (You Only Look Once): Grid-based prediction with combined classification and regression
   - SSD (Single Shot MultiBox Detector): Multi-scale feature maps for varied object sizes

3. **Segmentation Types**:
   - Semantic: Class-level pixel labeling (all cars=1 class)
   - Instance: Object-level differentiation (car1, car2 as separate)
   - Panoptic: Unified semantic + instance segmentation

4. **Evaluation Metrics**:
   - mAP (mean Average Precision): Area under precision-recall curve
   - IoU (Intersection over Union): Overlap ratio between prediction and ground truth
   - PQ (Panoptic Quality): Combination of recognition and segmentation quality

5. **Attention Mechanisms**:
   - Non-local blocks for long-range dependencies
   - Transformer-based architectures (DETR) replacing traditional NMS

## Examples

**Example 1: Medical Image Segmentation**
Problem: Segment brain tumors in MRI scans using U-Net
Solution:
1. Preprocess MRI slices (512x512 normalization)
2. Encoder: 4 downsampling blocks (Conv+ReLU+MaxPool)
3. Bottleneck: High-level feature extraction
4. Decoder: Transposed convolution + skip connections
5. Output: Pixel-wise sigmoid activation (tumor vs non-tumor)
Evaluation: Dice Coefficient = (2|X∩Y|)/(|X|+|Y|)

**Example 2: Real-Time Traffic Monitoring**
Problem: Detect vehicles and pedestrians using YOLOv8
Steps:
1. Input: 640x640 RGB frame
2. Backbone: CSPDarknet53 (cross-stage partial networks)
3. Neck: PANet (Path Aggregation Network)
4. Head: Three detection heads (80x80, 40x40, 20x20)
5. Loss: CIoU (Complete IoU) for better box regression
Output: Bounding boxes with class probabilities

## Exam Tips
1. Understand the architectural differences between R-CNN, YOLO, and Transformer-based detectors
2. Memorize formulas for mAP, IoU, and Dice Coefficient with their application contexts
3. Practice drawing and explaining U-Net architecture with skip connections
4. Know the mathematical formulation of focal loss for class imbalance
5. Be prepared to compare instance vs semantic segmentation with examples
6. Study recent advances: Vision Transformers in segmentation (Segment Anything Model)
7. Understand NMS (Non-Maximum Suppression) algorithm steps and computational complexity

Length: 2500 words, MSc CS (research-oriented) postgraduate level