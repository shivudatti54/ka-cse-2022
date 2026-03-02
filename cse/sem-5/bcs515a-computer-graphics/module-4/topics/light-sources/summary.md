# Light Sources in Computer Graphics - Summary

## Key Definitions and Concepts

- **Light Source:** A mathematical model that simulates illumination in virtual 3D environments, fundamental to rendering realistic images.
- **Ambient Light:** Uniform, non-directional illumination from all directions that provides base lighting.
- **Point Light:** Emits light equally in all directions from a single position, following inverse square law for attenuation.
- **Directional Light:** Simulates distant light sources (like sun) with parallel rays and constant intensity regardless of distance.
- **Spot Light:** Cone-shaped illumination with focused direction and falloff from center to edges.
- **Attenuation:** The decrease in light intensity with distance from the source.

## Important Formulas and Theorems

- **Ambient Reflection:** I_ambient = k_a × I_a
- **Diffuse Reflection (Lambert's Law):** I_diffuse = k_d × I_l × (N·L)
- **Phong Illumination Model:** I = I_a×k_a + I_d×k_d×(N·L) + I_s×k_s×(N·H)^n
- **Attenuation:** I = 1 / (a₀ + a₁d + a₂d²)
- **Spotlight Intensity:** I = I_l × cosⁿ(θ) for points within cone angle

## Key Points

- Light sources are essential for converting 3D geometry into visually perceivable images.
- Different light types simulate various real-world illumination scenarios.
- The Phong model combines ambient, diffuse, and specular components for realistic shading.
- Surface normals and light direction vectors determine illumination intensity via dot product.
- Color in computer graphics uses additive RGB model where light colors combine.
- Spotlight falloff creates realistic cone-shaped illumination patterns.
- Multiple lights can be combined to create sophisticated lighting setups.

## Common Mistakes to Avoid

- Forgetting to normalize vectors when calculating dot products for illumination.
- Applying negative dot product values (surface facing away from light) as positive illumination.
- Confusing directional lights (no position) with point lights (have position).
- Using the wrong attenuation formula or forgetting attenuation entirely for point lights.
- Overlooking that specular reflection depends on view direction, not just surface and light orientation.

## Revision Tips

- Practice calculating dot products between surface normals and light direction vectors for various configurations.
- Memorize the complete Phong illumination equation and understand each term's purpose.
- Sketch light source arrangements and visualize how each type illuminates surfaces differently.
- Solve previous exam questions on lighting calculations to familiarise with problem patterns.
- Use graphics software or online simulators to experiment with different light setups and observe results.
