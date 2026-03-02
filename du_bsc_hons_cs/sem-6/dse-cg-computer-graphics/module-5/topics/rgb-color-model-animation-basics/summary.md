# RGB Color Model and Animation Basics - Summary

## Key Definitions and Concepts

- **RGB Color Model:** Additive color model using Red, Green, and Blue light to create colors. RGB(0, 0, 0) = black, RGB(255, 255, 255) = white.
- **Color Depth:** Number of bits used to represent color (e.g., 24-bit = 16.7 million colors).
- **Keyframe:** A specific frame defining a major position/state in animation.
- **Interpolation:** Computing intermediate frames between keyframes.
- **Alpha Channel:** Additional channel storing transparency information (0 = transparent, 255 = opaque).
- **Frame Rate:** Number of frames displayed per second (fps); determines animation smoothness.

## Important Formulas and Theorems

- **Linear Interpolation:** P(t) = P₁ + (P₂ - P₁) × t, where t ranges from 0 to 1
- **Normalized RGB:** Divide integer value by 255 to get value in range [0, 1]
- **Ease-out Formula:** ease(t) = 1 - (1 - t)² for natural deceleration

## Key Points

- RGB is additive—combining all primary colors creates white (opposite of paint/pigment)
- Secondary colors: Cyan = Green + Blue, Magenta = Red + Blue, Yellow = Red + Green
- 24 fps is cinema standard, 60 fps is smooth for games, 120+ fps for VR
- Keyframes define major animation states; computer calculates in-between frames
- Easing functions create natural motion by varying speed throughout animation
- Alpha channel enables layering and transparency effects in graphics applications

## Common Mistakes to Avoid

- Confusing RGB (additive, for light/display) with CMYK (subtractive, for printing)
- Treating interpolation as always linear—easing creates more realistic motion
- Forgetting that alpha values normalize differently (sometimes 0-1, sometimes 0-255)
- Assuming higher fps always looks better—beyond certain thresholds, returns diminish

## Revision Tips

1. Practice converting between RGB integer and normalized representations
2. Work through interpolation problems with different t values to solidify understanding
3. Compare linear vs. eased animations mentally—visualize how easing affects perceived motion
4. Remember that color depth directly affects file sizes and display capabilities