# **AlexNet Text Book - 1 : Ch 3.2**

## **Convolutional Neural Networks (CNNs)**

### Introduction

Convolutional Neural Networks (CNNs) are a type of deep learning model particularly well-suited for image and video processing tasks. They were first introduced in the AlexNet paper in 2012 and have since become a standard component of many computer vision applications.

### Key Components of CNNs

- **Convolutional Layers**: These layers apply filters (kernels) to small regions of the input data, scanning the entire image, and generating feature maps.
- **Activation Functions**: These functions introduce non-linearity into the model, allowing it to learn more complex relationships between inputs and outputs.
- **Pooling Layers**: These layers downsample the feature maps, reducing the spatial dimensions of the data while retaining important information.
- **Flatten Layers**: These layers flatten the feature maps into a one-dimensional array, preparing the data for the fully connected layers.

### Convolutional Layers

Convolutional layers are the core of a CNN. They operate by scanning the input data with a filter (kernel), applying a dot product to each region of the data. This process generates feature maps that contain the key elements of the input data.

- **Filter (Kernel) Size**: The size of the filter determines the spatial resolution of the feature maps.
- **Stride Size**: The stride size determines the amount of spatial overlap between filters.
- **Padding**: Padding is used to ensure that the input data is the same size as the feature maps.

### Example of Convolutional Layer

Suppose we have an input image with 28x28 pixels and a filter size of 3x3 pixels. We apply the filter to each pixel in the image, scanning the entire image in 8x8 sub-regions.

| Pixel |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1    | P2  | P3  | P4  | P5  | P6  | P7  | P8  | P9  |
| ---   | --- | --- | --- | --- | --- | --- | --- | --- |
| P10   | P11 | P12 | P13 | P14 | P15 | P16 | P17 | P18 |
| ---   | --- | --- | --- | --- | --- | --- | --- | --- |
| P19   | P20 | P21 | P22 | P23 | P24 | P25 | P26 | P27 |
| ---   | --- | --- | --- | --- | --- | --- | --- | --- |
| P28   | P29 | P30 | P31 | P32 | P33 | P34 | P35 | P36 |
| ---   | --- | --- | --- | --- | --- | --- | --- | --- |
| P37   | P38 | P39 | P40 | P41 | P42 | P43 | P44 | P45 |
| ---   | --- | --- | --- | --- | --- | --- | --- | --- |
| P46   | P47 | P48 | P49 | P50 | P51 | P52 | P53 | P54 |
| ---   | --- | --- | --- | --- | --- | --- | --- | --- |

The output of the convolutional layer would be a feature map with 26x26 pixels, containing the key elements of the input image.

### Key Concepts

- **Convolutional Layers**: The core of a CNN, responsible for extracting features from the input data.
- **Filters (Kernels)**: Used to scan the input data and generate feature maps.
- **Stride Size**: Determines the amount of spatial overlap between filters.
- **Padding**: Used to ensure that the input data is the same size as the feature maps.
- **Activation Functions**: Introduced non-linearity into the model, allowing it to learn more complex relationships.
