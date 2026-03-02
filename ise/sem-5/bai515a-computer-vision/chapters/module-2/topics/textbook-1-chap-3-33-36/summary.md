# **Textbook-1: Chap- 3 (3.3 - 3.6) - Quick Revision Notes for Computer Vision**

### 3.3 Neighborhood Operators

- Neighborhood operators (e.g., mean, median, weighted mean) compute pixel values based on neighboring pixels.
- Advantages:
  - Robust to noise
  - Simple to implement
- Disadvantages:
  - Sensitive to noise
  - May not capture local patterns

### 3.4 Convolutional Neurons

- A convolutional neuron applies a neighborhood operator to a small region of the image.
- Formula: `C(x, y) = Σ(alpha \* f(x', y', w, b))`, where `f(x', y', w, b)` is the neighborhood operator
- Advantages:
  - Captures local patterns
  - Invariant to translation
- Disadvantages:
  - Computationally expensive
  - May not capture global patterns

### 3.5 Fourier Transforms

- The Fourier Transform represents an image as a sum of sinusoidal functions.
- Formula: `F(u, v) = ∫∫f(x, y) \* e^(-i \* (2 \* π \* u \* x + 2 \* π \* v \* y)) dx dy`
- Advantages:
  - Captures global patterns
  - Invariant to translation
- Disadvantages:
  - Computationally expensive
  - May not capture local patterns

### 3.6 Pyramid and Wavelet Transform

- The Pyramid Wavelet Transform is a hierarchical representation of an image.
- Formula: `D_j(u, v) = ∫∫f(x, y) \* w_j(u, v) \* ψ_j(x, y) dx dy`, where `ψ_j(x, y)` is a wavelet function
- Advantages:
  - Captures both local and global patterns
  - Invariant to scaling
- Disadvantages:
  - Computationally expensive
  - May not capture detailed information
