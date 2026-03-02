# Computer Vision Applications

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction to Computer Vision

### 1.1 What is Computer Vision?

Computer Vision is a multidisciplinary field of artificial intelligence that enables computers to interpret and understand visual information from the world, much like human vision. It encompasses techniques for acquiring, processing, analyzing, and understanding digital images to extract meaningful information from the physical world. The ultimate goal of computer vision is to automate tasks that the human visual system can perform, often surpassing human accuracy in specific domains.

### 1.2 Real-World Relevance and Applications

Computer vision has become ubiquitous in modern technology, driving innovation across numerous industries:

- **Healthcare**: Medical image analysis for disease diagnosis (X-rays, MRIs, CT scans), diabetic retinopathy detection, and surgical robotics
- **Autonomous Vehicles**: Object detection, lane tracking, and scene understanding for self-driving cars
- **Security and Surveillance**: Face recognition, anomaly detection, and behavior analysis
- **Retail and E-Commerce**: Visual search, product recommendation, and automated checkout systems
- **Agriculture**: Crop monitoring, disease detection, and automated harvesting
- **Manufacturing**: Quality control, defect detection, and robotic assembly
- **Entertainment**: Augmented reality, virtual reality, and video game development

### 1.3 Context in Delhi University Syllabus (NEP 2024 UGCF)

This topic aligns with the **Deep Learning** paper in the BSc (Hons) Computer Science curriculum under NEP 2024 UGCF. Students are expected to understand the fundamental concepts of computer vision, modern neural network architectures, and practical applications. The syllabus emphasizes both theoretical understanding and hands-on implementation skills.

---

## 2. Evolution of Deep Learning in Computer Vision

### 2.1 Early Approaches (Pre-2012)

Traditional computer vision relied on hand-crafted features:

- **SIFT (Scale-Invariant Feature Transform)**: Detects and describes local features
- **HOG (Histogram of Oriented Gradients)**: Captures edge orientations
- **Haar Cascades**: Used for face detection
- **Limitations**: Required extensive feature engineering, lacked generalization

### 2.2 The Deep Learning Revolution (2012-Present)

The introduction of **Convolutional Neural Networks (CNNs)** transformed computer vision:

| Year | Milestone | Significance |
|------|-----------|--------------|
| 1998 | LeNet-5 | First successful CNN for digit recognition |
| 2012 | AlexNet | Won ImageNet competition, sparked deep learning era |
| 2014 | VGGNet, GoogLeNet | Deeper networks, architectural innovations |
| 2015 | ResNet | Residual connections, enabled 100+ layer networks |
| 2017-2020 | EfficientNet, Vision Transformers | Efficiency optimization, attention mechanisms |

---

## 3. Modern Convolutional Neural Network Architectures

### 3.1 LeNet-5 (1998)

The pioneering architecture by Yann LeCun for handwritten digit recognition.

**Architecture:**
- Input: 32×32 grayscale images
- 2 convolutional layers with subsampling
- 2 fully connected layers
- Output: 10 classes

**Key Innovation**: Local receptive fields and weight sharing

### 3.2 AlexNet (2012)

Winner of ILSVRC 2012 with 16.4% top-5 error rate (vs. 26.2% for traditional methods).

**Architecture:**
- 5 convolutional layers
- 3 fully connected layers
- 60 million parameters
- ReLU activation, Dropout, Data augmentation

**Key Innovations**:
- ReLU activation (faster training)
- GPU acceleration
- Dropout for regularization
- Data augmentation

### 3.3 VGGNet (2014)

Developed by Oxford's Visual Geometry Group, known for simplicity and depth.

**Variants:**
- VGG-16: 16 weight layers
- VGG-19: 19 weight layers

**Key Features:**
- Small 3×3 convolutional filters throughout
- Stacked convolutional layers instead of large receptive fields
- Consistent spatial resolution through padding

```python
# VGG-16 Architecture Representation
VGG16 Architecture:
Conv3-64 → Conv3-64 → Pool → Conv3-128 → Conv3-128 → Pool 
→ Conv3-256 → Conv3-256 → Conv3-256 → Pool 
→ Conv3-512 → Conv3-512 → Conv3-512 → Pool 
→ Conv3-512 → Conv3-512 → Conv3-512 → Pool 
→ FC-4096 → FC-4096 → FC-1000
```

### 3.4 ResNet (2015)

Microsoft Research Asia's breakthrough architecture that won ILSVRC 2015.

**Key Innovation**: Skip Connections (Identity Mapping)

```
Output = F(x) + x  # Residual block
```

Where F(x) is the learned residual. This enables training of very deep networks (50, 101, 152 layers) by solving the vanishing gradient problem.

**ResNet-50 Architecture:**
- 49 convolutional layers
- 1 fully connected layer
- Bottleneck design (1×1, 3×3, 1×1 convolutions)

### 3.5 EfficientNet (2019)

Google's family of models optimizing accuracy and efficiency through **compound scaling**.

**Key Innovation**: Balanced scaling of depth, width, and resolution

```python
# EfficientNet Compound Scaling Formula
# depth: d = α^φ
# width: w = β^φ
# resolution: r = γ^φ
# subject to: α × β² × γ² ≈ 2
# α ≥ 1, β ≥ 1, γ ≥ 1
```

**EfficientNet-B0 to B7** achieve state-of-the-art accuracy with significantly fewer parameters than ResNet.

---

## 4. Object Detection

Object detection combines localization and classification, identifying where objects are and what they are.

### 4.1 Two-Stage Detectors

#### R-CNN Family

- **R-CNN**: Selective search + CNN features + SVM classifier
- **Fast R-CNN**: RoI pooling + shared convolutional features
- **Faster R-CNN**: Region Proposal Network (RPN) for end-to-end training

```python
# Faster R-CNN Architecture Overview
Faster R-CNN Components:
1. Backbone (ResNet/VGG) → Feature Maps
2. Region Proposal Network (RPN)
   - Anchor boxes
   - Classification (object/no object)
   - Bounding box regression
3. RoI Pooling → Fixed-size features
4. Classifier
   - Object classification
   - Bounding box refinement
```

### 4.2 Single-Stage Detectors

#### YOLO (You Only Look Once)

YOLO revolutionized real-time object detection by treating detection as a regression problem.

**YOLO Architecture:**
- Divides image into S×S grid
- Each grid cell predicts B bounding boxes and class probabilities
- Single forward pass through the network

**YOLO Versions:**
- YOLOv1 (2015): 45 fps
- YOLOv3 (2018): Multi-scale detection
- YOLOv4/v5 (2020): Improved accuracy and speed
- YOLOv8 (2023): State-of-the-art performance

#### SSD (Single Shot MultiBox Detector)

- Uses feature maps at multiple scales
- Default anchor boxes for various aspect ratios
- Balances speed and accuracy

### 4.3 Performance Metrics

| Metric | Description |
|--------|-------------|
| mAP (mean Average Precision) | Average precision across all classes |
| IoU (Intersection over Union) | Overlap between predicted and ground truth boxes |
| FPS | Frames per second (speed metric) |

---

## 5. Image Segmentation

Segmentation assigns a class label to every pixel in an image.

### 5.1 Semantic Segmentation

Classifies each pixel into a category (e.g., "road", "car", "sky").

**Key Architectures:**

- **FCN (Fully Convolutional Networks)**: Replace FC layers with convolutions
- **U-Net**: Encoder-decoder with skip connections (popular for medical imaging)
- **DeepLab**: Uses atrous (dilated) convolutions and ASPP (Atrous Spatial Pyramid Pooling)

```python
# U-Net Architecture (Medical Image Segmentation)
U-Net Structure:
- Encoder (Contracting Path):
  64 filters → 128 → 256 → 512
  
- Bottleneck:
  1024 filters
  
- Decoder (Expanding Path):
  512 → 256 → 128 → 64
  
- Skip Connections: Connect encoder features to decoder
- Output: Segmentation mask (same size as input)
```

### 5.2 Instance Segmentation

Distinguishes separate instances of the same class (e.g., individual cars).

**Approaches:**
- Mask R-CNN: Extension of Faster R-CNN with mask prediction branch
- Panoptic Segmentation: Combines semantic and instance segmentation

### 5.3 Applications

- Autonomous driving (road, pedestrian, vehicle segmentation)
- Medical imaging (tumor segmentation, organ delineation)
- Satellite imagery analysis (land cover classification)

---

## 6. Face Recognition

### 6.1 Face Recognition Pipeline

```
Face Recognition Steps:
1. Face Detection → Locate faces in image
2. Face Alignment → Normalize facial landmarks
3. Feature Extraction → Generate face embedding
4. Face Matching → Compare embeddings
```

### 6.2 DeepFace (Facebook, 2014)

- 9-layer deep CNN
- 3D face alignment using landmark detection
- L2-similarity for face verification

### 6.3 FaceNet (Google, 2015)

**Key Innovation**: Triplet Loss

```
Loss = max(0, ||f(x_a) - f(x_p)||² - ||f(x_a) - f(x_n)||² + margin)
```

Where:
- x_a: Anchor image
- x_p: Positive image (same person)
- x_n: Negative image (different person)

**Output**: 128-dimensional embedding (FaceNet), 512-dimensional (FaceNet v2)

### 6.4 Modern Face Recognition Systems

- **ArcFace**: Additive Angular Margin Loss for enhanced discrimination
- **InsightFace**: Open-source face recognition framework
- **Dlib**: Face recognition using ResNet embeddings

### 6.5 Applications

- Mobile device unlocking
- Biometric authentication
- Surveillance systems
- Social media tagging

---

## 7. Neural Style Transfer

### 7.1 Concept

Neural Style Transfer separates and recombines the **content** and **style** of images:

- **Content**: High-level structural information
- **Style**: Textural patterns, colors, brush strokes

### 7.2 Gatys et al. (2015) Approach

**Optimization-based method:**

```python
# Neural Style Transfer Loss Function
Total Loss = α × Content_Loss + β × Style_Loss

# Content Loss: MSE between feature representations
Content_Loss = ||F_cl - F_c||²

# Style Loss: MSE between Gram matrices
Style_Loss = ||G_sl - G_s||²
Where Gram Matrix: G_ij = F_i × F_j (feature correlations)
```

### 7.3 Fast Style Transfer (Johnson et al., 2016)

- Training a feed-forward network
- Single forward pass for stylization
- Real-time performance (20-30 fps)

### 7.4 Applications

- Art generation and filters
- Photo enhancement
- Video stylization
- Interior design visualization

---

## 8. Practical Implementation Examples

### 8.1 Example 1: Image Classification with PyTorch and ResNet

```python
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# Load pre-trained ResNet-50
model = models.resnet50(pretrained=True)
model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                        std=[0.229, 0.224, 0.225])
])

def classify_image(image_path):
    # Load and preprocess image
    image = Image.open(image_path).convert('RGB')
    input_tensor = transform(image).unsqueeze(0)
    
    # Inference
    with torch.no_grad():
        output = model(input_tensor)
    
    # Get top 5 predictions
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    top5_prob, top5_indices = torch.topk(probabilities, 5)
    
    # ImageNet class labels (abbreviated)
    classes = [...]  # Load ImageNet class labels
    
    for prob, idx in zip(top5_prob, top5_indices):
        print(f"{classes[idx]}: {prob.item():.4f}")

# Example usage
classify_image('sample_image.jpg')
```

### 8.2 Example 2: Object Detection with YOLOv5

```python
import torch
from PIL import Image
import matplotlib.pyplot as plt

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_objects(image_path, save_path='result.jpg'):
    # Load image
    img = Image.open(image_path)
    
    # Inference
    results = model(img)
    
    # Display results
    results.show()
    
    # Get detection results as DataFrame
    df = results.pandas().xyxy[0]
    print(df)
    
    # Filter detections with confidence > 0.5
    high_conf = df[df['confidence'] > 0.5]
    print(f"\nDetected {len(high_conf)} objects with confidence > 0.5")
    
    return df

# Example usage
detect_objects('street_scene.jpg')
```

### 8.3 Example 3: Face Recognition withface_recognition Library

```python
import face_recognition
import numpy as np
from PIL import Image
import os

class FaceRecognitionSystem:
    def __init__(self):
        self.known_encodings = []
        self.known_names = []
    
    def load_known_faces(self, directory):
        """Load and encode known faces from directory"""
        for filename in os.listdir(directory):
            if filename.endswith(('.jpg', '.png', '.jpeg')):
                image_path = os.path.join(directory, filename)
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                
                if len(encodings) > 0:
                    self.known_encodings.append(encodings[0])
                    name = os.path.splitext(filename)[0]
                    self.known_names.append(name)
    
    def recognize_faces(self, image_path):
        """Recognize faces in an unknown image"""
        unknown_image = face_recognition.load_image_file(image_path)
        unknown_encodings = face_recognition.face_encodings(unknown_image)
        
        recognized = []
        
        for unknown_encoding in unknown_encodings:
            # Compare with known faces
            matches = face_recognition.compare_faces(
                self.known_encodings, 
                unknown_encoding,
                tolerance=0.6
            )
            
            face_distances = face_recognition.face_distance(
                self.known_encodings, 
                unknown_encoding
            )
            
            if True in matches:
                best_match_index = np.argmin(face_distances)
                name = self.known_names[best_match_index]
                recognized.append(name)
            else:
                recognized.append("Unknown")
        
        return recognized

# Example usage
system = FaceRecognitionSystem()
system.load_known_faces('known_faces/')
results = system.recognize_faces('test_image.jpg')
print(f"Recognized faces: {results}")
```

---

## 9. Key Takeaways

### Core Concepts Summary

1. **Computer Vision** enables machines to interpret visual data, with deep learning revolutionizing the field since 2012.

2. **Modern CNN Architectures** have evolved from simple LeNet-5 to complex networks like EfficientNet, with key innovations including:
   - Skip connections (ResNet)
   - Compound scaling (EfficientNet)
   - Attention mechanisms

3. **Object Detection** uses either two-stage (R-CNN family) or single-stage (YOLO, SSD) approaches, with trade-offs between speed and accuracy.

4. **Image Segmentation** (semantic, instance, panoptic) assigns pixel-level labels, critical for autonomous driving and medical imaging.

5. **Face Recognition** systems use deep embeddings (128-512 dimensions) and metric learning (triplet loss, ArcFace) for verification.

6. **Neural Style Transfer** separates content from style using feature representations and Gram matrices.

### Delhi University Examination Focus Areas

- Understand the evolution of CNN architectures
- Compare different object detection approaches
- Know the differences between segmentation types
- Be able to explain the mathematics behind key algorithms
- Implement basic computer vision pipelines

---

## 10. Assessment Items

### 10.1 Multiple Choice Questions (Application Level)

**Q1.** In ResNet, the "skip connection" primarily helps in:
- a) Increasing the receptive field
- b) Reducing computational cost
- c) Mitigating the vanishing gradient problem
- d) Decreasing model parameters

**Q2.** Which of the following is NOT a component of the YOLO object detection algorithm?
- a) Grid cell division
- b) Non-maximum suppression
- c) Region Proposal Network
- d) Bounding box regression

**Q3.** In Neural Style Transfer, the Gram matrix is used to capture:
- a) Spatial information of features
- b) Color distribution
- c) Texture and style patterns
- d) Object boundaries

**Q4.** Semantic segmentation differs from instance segmentation in that:
- a) It cannot distinguish between different object classes
- b) It assigns the same label to all objects of the same class
- c) It requires more computational resources
- d) It cannot process video data

**Q5.** EfficientNet achieves efficiency through:
- a) Reducing the number of convolutional layers
- b) Using depthwise separable convolutions
- c) Compound scaling of depth, width, and resolution
- d) Replacing ReLU with Swish activation

### 10.2 Short Answer Questions (Analysis Level)

**Q1.** Explain why VGGNet uses 3×3 convolutional filters instead of larger filters like 7×7. What is the computational advantage?

**Q2.** Compare Fast R-CNN and YOLO in terms of speed and accuracy. Under what circumstances would you choose one over the other?

**Q3.** Describe how triplet loss works in FaceNet. Why is it better than using a softmax classifier for face verification?

**Q4.** Explain the encoder-decoder architecture in U-Net. How do skip connections help in medical image segmentation?

**Q5.** How does the attention mechanism in Vision Transformers (ViT) differ from convolutional operations in CNNs?

### 10.3 Flashcards

| Term | Definition/Key Point |
|------|---------------------|
| **IoU (Intersection over Union)** | Metric measuring overlap between predicted and ground truth bounding boxes; IoU = Area of Intersection / Area of Union |
| **mAP (mean Average Precision)** | Mean of average precisions across all object classes; primary metric for object detection |
| **Skip Connection** | Direct connection from earlier layers to later layers in ResNet, allowing gradient flow in deep networks |
| **RoI Pooling** | Operation in R-CNN family that extracts fixed-size feature maps from region proposals |
| **Gram Matrix** | Matrix of inner products between feature maps, capturing style/texture information in neural style transfer |
| **Anchor Box** | Pre-defined bounding boxes of various sizes and aspect ratios used as priors in object detectors like SSD and YOLO |
| **Non-maximum Suppression** | Post-processing technique that removes duplicate detections by keeping only the highest confidence box per object |
| **Transfer Learning** | Using pre-trained model weights (trained on large datasets) to initialize training for a new task |

### 10.4 Programming Assignment

**Task:** Implement a complete computer vision pipeline for a traffic monitoring system.

**Requirements:**
1. Use YOLO for vehicle detection
2. Implement vehicle counting by tracking detections across frames
3. Classify vehicles into categories (car, truck, bus, motorcycle)
4. Calculate vehicle speed using frame timestamps and known distance
5. Generate a summary report with statistics

**Evaluation Criteria:**
- Code functionality and correctness (40%)
- Documentation and code quality (20%)
- Innovation in tracking algorithm (20%)
- Report presentation (20%)

---

## 11. References and Further Reading

1. Krizhevsky, A., et al. (2012). ImageNet Classification with Deep Convolutional Neural Networks. NIPS.
2. He, K., et al. (2016). Deep Residual Learning for Image Recognition. CVPR.
3. Redmon, J., & Farhadi, A. (2018). YOLOv3: An Incremental Improvement. arXiv.
4. Tan, M., & Le, Q. (2019). EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. ICML.
5. Gatys, L. A., et al. (2016). Image Style Transfer Using Convolutional Neural Networks. CVPR.
6. Ronneberger, O., et al. (2015). U-Net: Convolutional Networks for Biomedical Image Segmentation. MICCAI.
7. Schroff, F., et al. (2015). FaceNet: A Unified Embedding for Face Recognition and Clustering. CVPR.

---

*Study Material prepared for BSc (Hons) Computer Science, Delhi University — NEP 2024 UGCF Curriculum*