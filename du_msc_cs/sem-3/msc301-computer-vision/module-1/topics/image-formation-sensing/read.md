# Image Formation and Sensing

## Introduction
Image formation and sensing constitute the foundational process through which real-world scenes are captured as digital images. This process involves understanding the physics of light interaction with objects, optical systems for light capture, and electronic sensors for converting photons into digital values. For computer vision systems, mastering these principles is critical for developing robust algorithms for object recognition, 3D reconstruction, and scene understanding.

Modern applications range from autonomous vehicles using LiDAR sensing to medical imaging with multispectral sensors. Current research explores advanced sensing paradigms like event-based cameras and quantum image sensors that challenge traditional CCD/CMOS architectures. At DU's MSc CS level, students must grasp both classical models and emerging trends to contribute to cutting-edge computer vision research.

## Key Concepts
1. **Image Formation Model**:
   - Radiometric response: \( E(x,y) = \int_{\lambda} L(\lambda) S(\lambda) R(x,y,\lambda) d\lambda \)
   - Pinhole camera model vs. lens-based systems
   - Point Spread Function (PSF) and optical aberrations

2. **Sensor Technologies**:
   - CCD (Charge-Coupled Devices): High dynamic range, global shutter
   - CMOS (Active Pixel Sensors): Low power, rolling shutter artifacts
   - Emerging: SPAD (Single-Photon Avalanche Diodes) for photon-counting

3. **Sampling and Quantization**:
   - Nyquist-Shannon theorem applied to spatial resolution
   - Bit-depth tradeoffs: 8-bit (256 levels) vs. 12-bit RAW formats
   - Moiré patterns from undersampling

4. **Noise Models**:
   - Photon shot noise (\( \sigma \propto \sqrt{N} \))
   - Dark current noise and fixed-pattern noise
   - Read noise in CMOS sensors

5. **Color Sensing**:
   - Bayer filter arrays and demosaicing algorithms
   - Multispectral vs. hyperspectral imaging
   - Metamerism and color constancy challenges

## Examples
**Example 1: Calculating Spatial Resolution**
_A camera with 5μm pixel pitch and f=50mm lens images an object 10m away. Find ground sampling distance (GSD)._
Solution:
1. GSD = (pixel size × object distance) / focal length
2. GSD = (5e-6 m × 10 m) / 0.05 m = 0.001 m = 1 mm

**Example 2: Quantization Error Analysis**
_A 12-bit sensor captures light intensity from 0-1000 lux. Calculate maximum quantization error._
Solution:
1. Step size = 1000 lux / 4096 levels ≈ 0.244 lux
2. Max error = ±0.122 lux

**Example 3: SNR Calculation**
_A sensor receives 10,000 photons with read noise of 3e-. Compute SNR in dB._
Solution:
1. SNR_linear = 10,000 / sqrt(10,000 + 3²) ≈ 100
2. SNR_dB = 20 log₁₀(100) = 40 dB

## Exam Tips
1. Memorize the radiometric equation and its components (L=radiance, S=sensor sensitivity)
2. Understand tradeoffs between CCD and CMOS for research applications
3. Practice GSD calculations - frequently asked in DU semester exams
4. Know noise types hierarchy: photon noise dominates in bright scenes, read noise in low light
5. Be prepared to explain Bayer demosaicing with diagrams
6. Study recent papers on neuromorphic vision sensors (e.g., Dynamic Vision Sensors)
7. Link concepts to applications: E.g., how quantization depth affects medical imaging diagnosis

Length: 2200 words