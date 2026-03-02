# The Phong Lighting Model - Summary

## Key Definitions and Concepts

- **Phong Lighting Model**: A local illumination model that simulates light reflection from surfaces using three components: ambient, diffuse, and specular.

- **Ambient Reflection**: Background illumination that ensures surfaces in shadow are not completely dark; independent of surface orientation.

- **Diffuse Reflection**: Light that reflects equally in all directions; intensity depends on the angle between surface normal and light direction (Lambert's law).

- **Specular Reflection**: Creates shiny highlights on surfaces; depends on the angle between the reflection vector and view direction.

- **Shininess Exponent (n)**: Controls the size and sharpness of specular highlights; higher values produce smaller, sharper highlights.

## Important Formulas and Theorems

- **Ambient Component**: Iₐ = kₐ × Iₗ

- **Diffuse Component**: Iₐ = kₐ × Iₗ × max(0, n̂ · l̂)

- **Specular Component**: Iₛ = kₛ × Iₗ × max(0, r̂ · v̂)ⁿ

- **Reflection Vector**: r̂ = 2(n̂ · l̂)n̂ - l̂

- **Combined Phong Equation**: I_total = Iₐ + Iₐ + Iₛ

## Key Points

- The Phong model approximates realistic lighting through mathematical simplification of complex light-surface interactions.

- Ambient light provides base illumination, diffuse determines surface brightness based on orientation, and specular creates material-dependent highlights.

- The dot product n̂ · l̂ represents the cosine of the angle between surface normal and light direction.

- Shininess exponent typically ranges from 1 (matte) to 128+ (highly polished surfaces).

- The model is applied per-light and per-color-channel for colored materials.

- Works best for point light sources at moderate distances from surfaces.

## Common Mistakes to Avoid

- Forgetting to clamp negative dot product values to zero when calculating diffuse and specular components.

- Using non-unit vectors in dot product calculations, which produces incorrect results.

- Confusing the shininess exponent—higher values create smaller, not larger, specular highlights.

- Not normalizing vectors before calculating reflection or dot products.

## Revision Tips

- Practice vector calculations: normalization, dot products, and reflection vector computation.

- Work through at least three complete numerical problems covering all three components.

- Remember that surfaces facing away from light sources (negative dot products) receive zero diffuse and specular illumination.

- Create a cheat sheet with all formulas for quick review before exams.
