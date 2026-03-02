# Video Understanding & Tracking - Summary

## Key Definitions and Concepts
- **Optical Flow**: Dense motion field estimation between frames
- **Data Association**: Matching detections across frames (e.g., Hungarian algorithm)
- **Tracklet**: Short trajectory fragment before full association
- **Occlusion Handling**: Re-identification after temporary object disappearance

## Important Formulas and Theorems
- Kalman Predictor: x̂ₖ⁻ = Fxₖ₋₁ + Buₖ₋₁
- Optical Flow Constraint: I_xu + I_yv + I_t = 0
- MOTA: 1 - (FN + FP + IDSW)/GT
- Bhattacharyya Coefficient: Σ√(p(i)q(i)) for histogram comparison

## Key Points
- Tracking requires both motion modeling and appearance features
- DeepSORT combines Kalman filter with deep appearance metrics
- Transformers enable global context modeling in video sequences
- Evaluation must consider accuracy and computational efficiency
- Occlusion handling is critical for Indian crowded scenarios
- Multi-modal fusion (RGB+thermal) improves night tracking
- Ethical considerations in surveillance applications

## Common Mistakes to Avoid
- Confusing detection score with tracking confidence
- Ignoring frame rate vs processing speed mismatch
- Misapplying linear models to non-linear motion
- Overlooking memory management in long videos

## Revision Tips
- Practice deriving Kalman filter equations from Bayes' rule
- Memorize MOT metrics calculation with sample data
- Review transformer architecture variants for video
- Study ablation studies from recent CVPR papers
- Implement simple tracker using OpenCV Python

Length: 650 words