# Feature Extraction: Background

### Overview

Feature extraction is a crucial step in computer vision that involves transforming an image into a representation that can be understood by a machine. Background subtraction is a type of feature extraction technique used to separate an object of interest from the background.

### Key Points

- **Definition:** Feature extraction is the process of transforming an image into a representation that can be understood by a machine.
- **Purpose:** To extract relevant information from an image, such as edges, textures, and shapes.
- **Types:**
  - Geometric features (e.g., corners, edges)
  - Texture features (e.g., pixel values, color histograms)
  - Shape features (e.g., contours, shapes)
- **Background Subtraction:**
  - A type of feature extraction that separates an object of interest from the background.
  - Can be achieved through various techniques, including:
    - Color histogram subtraction
    - Gradient morphological operations
    - Background/foreground modeling

### Mathematical Formulas and Definitions

- **Mean Squared Error (MSE):** A measure of the difference between predicted and actual values: MSE = (1/n) \* ∑(y_i - y_pred)^2
- **Mean Absolute Error (MAE):** A measure of the average difference between predicted and actual values: MAE = (1/n) \* ∑|y_i - y_pred|
- **Zero-Crossing Rate:** A measure of the number of zero crossings in a signal: ZCR = (1/n) \* ∑(sign(y_i+1) - sign(y_i))^2

### Important Theorems

- **Fourier Transform:** A mathematical tool used to analyze and transform signals into the frequency domain.
- **Hough Transform:** A mathematical tool used to detect and describe lines and curves in an image.

### Quick Revision Tips

- Understand the concept of feature extraction and its importance in computer vision.
- Familiarize yourself with background subtraction techniques and their applications.
- Practice applying mathematical formulas and theorems to solve problems related to feature extraction.
