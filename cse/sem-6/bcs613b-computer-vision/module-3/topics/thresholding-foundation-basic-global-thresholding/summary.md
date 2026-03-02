# Thresholding Foundation - Basic Global Thresholding

## Overview

Thresholding is the simplest segmentation technique converting grayscale images to binary by comparing pixel intensities to threshold value. Global thresholding uses single threshold for entire image, effective when objects and background have distinct intensity distributions.

## Key Points

- **Basic Thresholding**: g(x,y) = 1 if f(x,y) > T, else 0, where T is threshold value
- **Bimodal Histogram**: Ideal case with two distinct peaks (object and background), valley indicates good threshold
- **Otsu's Method**: Automatically finds optimal T by maximizing between-class variance σ²B = ω0×ω1×(μ0-μ1)²
- **Iterative Threshold Selection**: Start with initial T, compute means of regions above/below T, update T=(μ1+μ2)/2, repeat
- **Multi-level Thresholding**: Multiple thresholds for images with more than two distinct regions

## Important Concepts

- Global thresholding effective when uniform illumination creates bimodal intensity histogram
- Otsu's method equivalent to minimizing within-class variance or maximizing between-class variance
- Poor results when illumination non-uniform or object/background intensities overlap
- Applications include document binarization, quality inspection, simple object detection

## Notes

- Histogram shape indicates threshold selection difficulty: bimodal easy, unimodal hard
- Otsu's method optimal for images with Gaussian intensity distributions per class
- Try all possible thresholds (0-255) for Otsu, select T maximizing σ²B
- Limitations: single threshold fails with varying illumination, requires adaptive thresholding
