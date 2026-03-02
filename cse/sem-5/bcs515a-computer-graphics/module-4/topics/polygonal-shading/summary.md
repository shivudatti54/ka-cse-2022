# Polygonal Shading - Summary

## Key Definitions and Concepts

- **Polygonal Shading**: Technique for determining surface color based on lighting interactions across polygon surfaces
- **Flat Shading**: Computes lighting once per polygon using a single normal vector; produces faceted appearance
- **Gouraud Shading**: Interpolates vertex intensities across polygons using bilinear interpolation
- **Phong Shading**: Interpolates surface normals and computes complete lighting model at each pixel

## Important Formulas and Theorems

**Lambertian Diffuse Reflection:**
I = Iₐ × kₐ + Iₗ × kd × (N · L)

**Phong Reflection Model:**
I = Iₐ × kₐ + Iₗ × [kd × (N · L) + ks × (R · V)ⁿ]

**Bilinear Intensity Interpolation:**
I(P) = α × I(A) + β × I(B) + γ × I(C)

## Key Points

- Flat shading calculates intensity per polygon, Gouraud per vertex, Phong per pixel
- Gouraud shading may miss specular highlights that fall between vertices
- Phong shading provides accurate specular highlights regardless of position within polygon
- Vertex normals for smooth shading are computed by averaging adjacent face normals
- The shininess coefficient (n) in Phong model controls highlight sharpness
- Computational cost increases: Flat < Gouraud < Phong
- Modern GPUs implement these concepts through vertex and fragment shaders

## Common Mistakes to Avoid

- Confusing Gouraud and Phong shading; remember Gouraud interpolates intensity while Phong interpolates normals
- Forgetting to normalize vectors after interpolation in Phong shading
- Using the same normal for all pixels in flat shading instead of calculating per face
- Not understanding that specular highlights in Gouraud depend on vertex positions, not actual highlight location

## Revision Tips

1. Practice calculating surface normals from polygon vertices using cross products
2. Work through numerical examples of intensity interpolation with barycentric coordinates
3. Remember the quality-speed trade-off: Phong gives best results but requires most computation
4. Compare rendered images to identify which shading method was used (faceted = flat, smooth but dull highlights = Gouraud, sharp highlights = Phong)
5. Know the three components of Phong model: ambient, diffuse, and specular reflection
