# Computer Vision

## Introduction

Computer Vision is a multidisciplinary field that enables computers to extract meaningful information from digital images and videos, mimicking human visual perception. As one of the most rapidly advancing areas in artificial intelligence, computer vision bridges the gap between low-level image processing and high-level scene understanding. This topic forms a critical component of the Digital Image Processing curriculum, extending beyond traditional morphological operations to explore how machines can interpret visual data autonomously.

The significance of computer vision in contemporary technology cannot be overstated. From facial recognition systems in smartphones to autonomous vehicle navigation, from medical image analysis to industrial quality inspection, computer vision applications permeate virtually every sector of modern industry. The University of Delhi curriculum introduces this field to equip students with foundational knowledge that integrates seamlessly with preceding topics in morphological image processing and feature extraction, creating a comprehensive understanding of visual data analysis.

The evolution of computer vision traces back to the 1960s when early researchers attempted to reconstruct 3D structures from 2D images. Today, with advances in deep learning and increased computational power, systems can achieve superhuman performance in specific visual tasks. However, understanding the fundamental principles remains essential, as these concepts form the bedrock upon which advanced techniques are built.

## Key Concepts

### Relationship Between Image Processing and Computer Vision

Image processing and computer vision represent sequential stages in the visual information extraction pipeline. Image processing operations such as erosion, dilation, opening, and closing operate at the pixel level, transforming input images to produce enhanced or simplified outputs. These operations, covered extensively in preceding modules, serve as preprocessing steps for computer vision tasks. Computer vision builds upon these processed images to perform higher-level reasoning, including object detection, scene recognition, and spatial understanding.

### Levels of Vision

Computer vision operates across three distinct levels that progressively increase in complexity. Low-level vision involves image acquisition, preprocessing, and feature extraction tasks such as edge detection and corner detection. These operations transform raw pixel data into more abstract representations suitable for further analysis. Mid-level vision encompasses tasks like segmentation, where images are divided into meaningful regions, and representation, where structural descriptions are derived. High-level vision involves interpretation and understanding, including object recognition, scene classification, and cognitive decision-making based on visual input.

### Image Formation Fundamentals

Understanding how images are formed provides essential context for computer vision. The pinhole camera model describes the fundamental geometry of image formation, where 3D points in the world are projected onto a 2D image plane through a projection center. This model introduces critical concepts including camera calibration, perspective projection, and the transformation between world coordinates, camera coordinates, and image coordinates. The geometry of image formation establishes the mathematical foundation for tasks such as depth estimation and 3D reconstruction.

### Feature Representation

Features serve as intermediate representations that capture essential image characteristics while reducing data complexity. Common feature types include edges, which represent intensity discontinuities; corners, which indicate interest points with significant local variation; blobs, which denote regions with distinct properties; and textures, which describe repetitive patterns within image regions. The selection and extraction of appropriate features significantly impact the performance of subsequent computer vision algorithms.

### Object Recognition Approaches

Object recognition represents a fundamental computer vision task that involves identifying specific objects within images. Template matching provides a straightforward approach where objects are recognized by comparing image regions against predefined templates. Feature-based recognition identifies objects by matching extracted features against known feature collections. Modern approaches employ machine learning and deep neural networks to learn hierarchical feature representations directly from image data, achieving remarkable recognition accuracy across diverse object categories.

### Scene Understanding

Scene understanding extends beyond individual object recognition to comprehend the overall context and spatial relationships within images. This includes determining what objects are present, where they are located, and how they relate to each other. Semantic segmentation assigns class labels to each pixel, while instance segmentation distinguishes between individual object instances. Scene graphs represent objects and their relationships, enabling sophisticated reasoning about visual content.

## Examples

### Example 1: Edge-Based Object Detection

Consider detecting rectangular objects in an industrial quality control application. After applying morphological operations from previous modules to enhance object boundaries, the computer vision pipeline proceeds as follows:

Step 1: Apply Canny edge detector to obtain binary edge map
Step 2: Use Hough transform to detect straight line segments
Step 3: Identify line intersections that form right angles
Step 4: Group perpendicular lines that form closed quadrilaterals
Step 5: Validate rectangle properties (equal opposite sides, consistent dimensions)
Step 6: Classify as acceptable or defective based on geometric criteria

This approach demonstrates how low-level image processing operations combine with mid-level vision techniques to accomplish practical inspection tasks.

### Example 2: Simple Facial Recognition System

A basic facial recognition system illustrates computer vision at work. The system captures a facial image, detects the face region using Haar cascade classifiers, extracts facial landmarks (eyes, nose, mouth corners), computes a feature vector describing facial geometry, and compares this vector against enrolled face templates using distance metrics. If the computed distance falls below a threshold, identity is verified. This example shows the progression from image acquisition through feature extraction to recognition decision.

### Example 3: Motion Detection in Video Sequences

Computer vision extends to temporal image analysis. In a simple motion detection system, frame differencing compares consecutive video frames to identify moving regions. Background subtraction maintains a reference background model and identifies foreground objects by comparing current frames against this model. Morphological operations clean the resulting binary masks, while connected component analysis extracts individual moving objects. Tracking algorithms then follow these objects across frames, enabling applications from surveillance to traffic monitoring.

## Exam Tips

Understanding computer vision requires integrating knowledge from multiple domains. The following points address frequently tested concepts in DU semester examinations.

1. Clearly distinguish between image processing and computer vision, remembering that image processing transforms images while computer vision interprets their content.

2. Memorize the three levels of vision (low-level, mid-level, high-level) and provide appropriate examples for each when answering descriptive questions.

3. The pinhole camera model and perspective projection equations frequently appear in examination problems, requiring comfortable manipulation of coordinate transformations.

4. Feature types and their applications represent essential knowledge—be prepared to explain edge detection, corner detection, and blob detection in both theoretical and practical contexts.

5. Understand the complementarity between morphological operations (erosion, dilation, opening, closing) and computer vision tasks, as these topics connect across module boundaries.

6. Object recognition approaches ranging from template matching to modern deep learning methods may appear in examination questions requiring comparative analysis.

7. Practical applications of computer vision demonstrate understanding beyond theoretical knowledge—prepare examples from healthcare, automotive, security, and industrial domains.

8. Practice drawing and interpreting flow diagrams showing the computer vision pipeline from image acquisition to final interpretation.

9. Numerical problems may involve computing simple transformations, determining feature correspondences, or analyzing recognition decision thresholds.

10. Conceptual questions frequently test understanding of why computer vision remains challenging despite technological advances—consider illumination variation, viewpoint changes, occlusion, and computational complexity factors.