# Polygonal Shading

## Introduction

Polygonal shading is a fundamental technique in computer graphics that determines how light interacts with the surfaces of 3D polygonal objects to produce realistic visual images. In the context of 's Computer Graphics curriculum, understanding shading methods is essential for creating visually appealing 3D rendered scenes. Polygonal shading bridges the gap between geometric primitives (polygons) and the final displayed pixels by calculating color intensities across surface areas based on lighting conditions.

The importance of polygonal shading cannot be overstated in modern computer graphics applications. From video games to architectural visualizations, from animated films to scientific simulations, shading techniques determine how surfaces appear to the viewer. Different shading methods trade off computational complexity against visual quality, making the choice of shading technique a critical design decision in any graphics application. This module covers three primary shading methods: Flat Shading, Gouraud Shading, and Phong Shading, each with distinct characteristics and use cases.

## Key Concepts

### 1. Flat Shading (Constant Shading)

Flat shading is the simplest and fastest polygonal shading method. In this technique, a single normal vector is computed for each polygon (typically by taking the cross product of two edge vectors), and the entire polygon is filled with a single color based on the lighting calculation at that normal. The lighting intensity is constant across the entire face of the polygon.

**Mathematical Foundation:**
The basic lighting calculation uses the Lambertian diffuse reflection model:

I = Iₐ × kₐ + Iₗ × kd × (N · L)

Where:

- I = final intensity
- Iₐ = ambient light intensity
- kₐ = ambient reflection coefficient
- Iₗ = light source intensity
- kd = diffuse reflection coefficient
- N = surface normal vector (unit vector)
- L = direction to light source (unit vector)

Flat shading works best for objects with flat surfaces where the curvature is approximated by small polygons. It produces a "faceted" look, which can be desirable for low-poly aesthetics or stylized rendering.

### 2. Gouraud Shading (Vertex Shading)

Gouraud shading improves upon flat shading by interpolating vertex intensities across the polygon surface. The technique was introduced by Henri Gouraud in 1971 and was the first practical method for smooth-shaded surfaces. The process involves three main steps:

1. Calculate the surface normal at each vertex (typically by averaging normals of adjacent polygons)
2. Compute the intensity at each vertex using the lighting model
3. Interpolate the intensity across the polygon using bilinear interpolation

**Bilinear Interpolation Formula:**
For a point P with barycentric coordinates (α, β, γ) relative to vertices A, B, C:
I(P) = α × I(A) + β × I(B) + γ × I(C)

Gouraud shading produces smooth transitions between polygons but can miss specular highlights that fall between vertices, as the interpolation smooths out sharp intensity changes.

### 3. Phong Shading (Pixel/Fragment Shading)

Phong shading represents the highest quality among the three basic methods. Instead of interpolating intensities, Phong shading interpolates the surface normals across the polygon and performs the complete lighting calculation at each pixel. This allows for accurate rendering of specular highlights regardless of their position within the polygon.

**Phong Reflection Model:**
The complete Phong lighting model adds a specular component to the ambient and diffuse components:

I = Iₐ × kₐ + Iₗ × [kd × (N · L) + ks × (R · V)ⁿ]

Where:

- ks = specular reflection coefficient
- R = direction of reflected light vector
- V = direction to viewer (unit vector)
- n = shininess coefficient (specular exponent)

The shininess coefficient n controls the size and sharpness of the specular highlight. Higher values produce smaller, sharper highlights.

**Normal Interpolation:**
N(P) = α × N(A) + β × N(B) + γ × N(C)
Then normalize N(P) before use in lighting calculations.

### Comparative Analysis

| Aspect              | Flat Shading | Gouraud Shading    | Phong Shading |
| ------------------- | ------------ | ------------------ | ------------- |
| Computation         | Per polygon  | Per vertex         | Per pixel     |
| Speed               | Fastest      | Medium             | Slowest       |
| Quality             | Faceted look | Smooth but limited | High quality  |
| Specular Highlights | None         | May miss           | Accurate      |
| Memory              | Low          | Medium             | Higher        |

### Shading vs Rendering Pipeline

In modern graphics pipelines (OpenGL, DirectX), these shading methods correspond to different programmable shader stages:

- **Vertex Shader**: Performs operations at vertices (equivalent to Gouraud vertex intensity calculation)
- **Fragment/Pixel Shader**: Performs operations at each fragment (equivalent to Phong shading per-pixel calculation)

## Examples

### Example 1: Flat Shading Calculation

**Problem:** A triangular polygon has vertices at positions P1(0,0,0), P2(1,0,0), P3(0,1,0) in world coordinates. A point light source is at position L(0,0,1). Calculate the shade color using flat shading with ambient intensity 0.1, diffuse coefficient 0.7, light intensity 1.0.

**Solution:**

**Step 1: Calculate polygon normal**
Using vertices P1, P2, P3:
Vector P1P2 = (1, 0, 0)
Vector P1P3 = (0, 1, 0)
Normal N = P1P2 × P1P3 = (0, 0, 1)

**Step 2: Calculate light direction**
At polygon centroid C(1/3, 1/3, 0):
L = normalize(L - C) = normalize(0, 0, 1) = (0, 0, 1)

**Step 3: Apply Lambertian diffuse**
N · L = (0, 0, 1) · (0, 0, 1) = 1.0

**Step 4: Calculate final intensity**
I = 0.1 + 1.0 × 0.7 × 1.0 = 0.1 + 0.7 = 0.8

The polygon is rendered with intensity 0.8 (80% brightness).

### Example 2: Gouraud Shading Interpolation

**Problem:** A triangular polygon has vertex intensities calculated as I1 = 0.3, I2 = 0.7, I3 = 0.5. Using barycentric coordinates, find the intensity at point P that divides the triangle with weights α = 0.25, β = 0.25, γ = 0.5.

**Solution:**

**Step 1: Apply bilinear interpolation formula**
I(P) = α × I1 + β × I2 + γ × I3

**Step 2: Substitute values**
I(P) = 0.25 × 0.3 + 0.25 × 0.7 + 0.5 × 0.5
I(P) = 0.075 + 0.175 + 0.25
I(P) = 0.5

The interpolated intensity at point P is 0.5.

### Example 3: Phong Shading vs Gouraud Shading

**Problem:** A sphere is approximated by a triangle mesh. A specular highlight falls at the center of one triangle. With Gouraud shading (intensities at vertices: 0.4, 0.4, 0.4), where would the highlight appear? With Phong shading, how is it handled differently?

**Solution:**

**Gouraud Shading:**
Since all three vertices have the same intensity (0.4), the interpolated result across the entire triangle will be 0.4. Any specular highlight at the pixel level is lost because the calculation happens only at vertices. The smooth appearance fails to capture the sharp highlight.

**Phong Shading:**
The normal is interpolated at each pixel across the triangle. At the center where the highlight should be:

- The interpolated normal points directly toward the light and viewer
- N · L and R · V both approach maximum values
- The complete lighting calculation (with specular component) is performed
- The highlight is accurately rendered as a bright spot

This demonstrates why Phong shading produces superior specular highlights compared to Gouraud shading.

## Exam Tips

1. **Remember the shading order by quality/speed**: Flat (fastest, lowest quality) → Gouraud (medium) → Phong (slowest, highest quality)

2. **Key distinction**: Gouraud interpolates intensity values, while Phong interpolates normal vectors and computes lighting per pixel

3. **Flat shading formula**: Use I = Iₐ × kₐ + Iₗ × kd × (N · L) for diffuse reflection calculations

4. **Phong model components**: Know that I = Ambient + Diffuse + Specular, each with its own coefficient (ka, kd, ks)

5. **Specular exponent n**: Higher values produce smaller, sharper highlights (metallic appearance); lower values produce larger, softer highlights

6. **Vertex normals for Gouraud**: Remember to average normals of adjacent polygons to get smooth vertex normals

7. **Bilinear interpolation**: For Gouraud shading, intensity at any point = αI₁ + βI₂ + γI₃ using barycentric coordinates

8. **Practical applications**: Flat shading for low-poly/retro look, Gouraud for older games, Phong for modern applications requiring realistic highlights
