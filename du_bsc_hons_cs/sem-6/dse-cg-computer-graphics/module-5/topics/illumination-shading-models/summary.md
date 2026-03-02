# Illumination and Shading Models - Summary

## Key Definitions and Concepts

- **Illumination Model**: A mathematical model describing how light interacts with a surface, computing light intensity based on light sources, surface properties, and viewing direction.

- **Shading Model**: Determines how illumination calculations are applied across geometric primitives to produce pixel colors.

- **Phong Reflection Model**: The standard illumination model combining ambient, diffuse, and specular components.

- **Gouraud Shading**: Interpolates computed intensity values across polygon surfaces.

- **Phong Shading**: Interpolates surface normals and computes illumination at each pixel.

## Important Formulas and Theorems

**Combined Phong Illumination:**
$$I = k_a I_a + k_d I_l (\vec{N} \cdot \vec{L}) + k_s I_l (\vec{R} \cdot \vec{V})^n$$

**Lambert's Cosine Law (Diffuse):**
$$I_{diffuse} = k_d \times I_l \times \max(0, \vec{N} \cdot \vec{L})$$

**Light Attenuation:**
$$I_{attenuated} = \frac{I_{original}}{c_0 + c_1d + c_2d^2}$$

**Blinn-Phong Halfway Vector:**
$$\vec{H} = \frac{\vec{L} + \vec{V}}{|\vec{L} + \vec{V}|}$$

## Key Points

- Ambient illumination provides baseline brightness independent of geometry
- Diffuse reflection follows Lambert's cosine law—intensity proportional to cos(θ) = N·L
- Specular reflection creates shiny highlights; shininess coefficient n controls highlight size
- Flat shading computes once per polygon; fastest but produces faceted appearance
- Gouraud shading interpolates intensities; faster than Phong but may miss specular highlights
- Phong shading interpolates normals; highest quality but computationally expensive
- Blinn-Phong uses halfway vector instead of reflection vector for efficiency
- Color is computed component-wise (R, G, B) for colored lights and surfaces

## Common Mistakes to Avoid

1. Using raw (non-unit) vectors in dot product calculations—always normalize N and L
2. Forgetting the max(0, N·L) clamp—negative dot products mean light is behind the surface
3. Confusing Gouraud and Phong shading—Gouraud interpolates intensity, Phong interpolates normals
4. Applying specular formula when N·L ≤ 0 (light behind surface)—specular should be zero
5. Assuming shininess coefficient n can be any value—typical range is 1-100 in practice

## Revision Tips

1. Practice vector calculations: computing dot products, reflection vectors, and normalizing vectors
2. Draw the geometry: sketch surface normal, light direction, view direction, and reflection direction
3. Compare shading outputs: draw a simple polygon and compute colors under each shading method
4. Memorize the complete Phong formula and understand what each term represents visually
5. Remember that in real-time graphics, Phong shading is typically used due to GPU acceleration