# Photometric Image Formation

## Overview

Photometric image formation explains how light interacts with surfaces and is captured by cameras to create digital images. Understanding this process is crucial for developing CV algorithms that accurately interpret images, covering light sources, surface reflection models, and the camera's response to light.

## Key Points

- **Light Sources**: Point sources, directional sources (sun), area sources, ambient light with properties of intensity, color temperature, spectral distribution
- **Diffuse Reflection (Lambertian)**: Light scattered equally in all directions, appearance independent of viewing angle, I = kₐIₐ + kₑIₑmax(0, n·l)
- **Specular Reflection**: Light reflected in specific direction like a mirror, creates view-dependent highlights, I = kₛIₑmax(0, (r·v)^α)
- **Image Irradiance Equation**: E = L × (π/4) × (d/f)² × cos⁴θ relating scene radiance to image irradiance
- **Radiometry vs Photometry**: Radiometry measures physical light (Watts), photometry weights by human eye sensitivity (lumens, lux)
- **Camera Response Function**: Nonlinear mapping I = f(E × Δt) from irradiance to pixel values due to gamma correction and sensor characteristics
- **Bayer Pattern**: 50% green, 25% red, 25% blue pixels matching human eye sensitivity, requires demosaicing

## Important Concepts

- Pinhole camera model relates 3D point (X,Y,Z) to 2D projection: x = f×X/Z, y = f×Y/Z
- Real-world complications include interreflections, non-Lambertian surfaces, complex illumination, sensor noise
- Applications: photometric stereo, shape from shading, radiometric calibration, intrinsic image decomposition
- Digital camera pipeline: Lens → Aperture → Shutter → Sensor → ADC → Processing → Digital Image

## Notes

- Understand difference between radiometric (physical) and photometric (perceptual) quantities
- Memorize image irradiance equation components and how parameters affect the image
- Know both Lambertian (matte surfaces) and specular (shiny surfaces) reflection models
- Be able to trace the complete pipeline from scene radiance to digital pixel values
- Recognize that real surfaces don't follow ideal Lambertian or specular models perfectly
