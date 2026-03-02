# Illumination and Shading Models

## Introduction

Computer graphics aims to create realistic images that mimic the physical world. At the heart of this realism lies the accurate simulation of how light interacts with surfaces in a 3D scene. **Illumination models** (also called lighting models) describe the physics of light reflection from surfaces, while **shading models** determine how these illumination calculations are applied across geometric primitives to produce smooth, realistic images.

Understanding illumination and shading is crucial for the University of Delhi Computer Science curriculum, as it forms the foundation for rendering realistic 3D scenes. Whether you're developing games, simulations, or visualization tools, the choice of illumination and shading model directly impacts visual quality and computational performance. This topic covers the fundamental physics-based illumination models (ambient, diffuse, and specular reflection) and the three primary shading approaches (flat, Gouraud, and Phong shading) used in real-time graphics pipelines.

## Key Concepts

### 1. Illumination Models

An illumination model computes the light intensity at a point on a surface based on light sources, surface properties, and viewing direction. The most widely used model is the **Phong Reflection Model**, which separates light interaction into three components:

#### Ambient Illumination
Ambient light represents the minimum illumination present in a scene, simulating light that has bounced around the environment so many times it appears to come from everywhere. It is independent of surface orientation and viewing direction.

**Formula:**
$$I_{ambient} = k_a \times I_a$$

Where:
- $k_a$ = ambient reflectivity coefficient (0 ≤ $k_a$ ≤ 1)
- $I_a$ = intensity of ambient light

Ambient illumination alone produces flat, unrealistic images with no depth perception, which is why it is combined with other components.

#### Diffuse Reflection (Lambertian Reflection)
Diffuse reflection occurs on matte or rough surfaces where light scatters equally in all directions. The intensity depends on the angle between the surface normal and the light direction.

**Formula:**
$$I_{diffuse} = k_d \times I_l \times \max(0, \vec{N} \cdot \vec{L})$$

Where:
- $k_d$ = diffuse reflectivity coefficient (0 ≤ $k_d$ ≤ 1)
- $I_l$ = intensity of the light source
- $\vec{N}$ = surface unit normal vector
- $\vec{L}$ = unit vector pointing to the light source
- $\vec{N} \cdot \vec{L} = \cos\theta$ (angle between normal and light direction)

This is **Lambert's cosine law**, which states that the intensity of diffuse reflection is proportional to the cosine of the angle between the surface normal and the light direction.

#### Specular Reflection
Specular reflection creates the shiny highlights on surfaces like polished metal or wet roads. It depends on the viewing direction and produces the characteristic "shininess" effect.

**Formula:**
$$I_{specular} = k_s \times I_l \times \max(0, \vec{R} \cdot \vec{V})^n$$

Where:
- $k_s$ = specular reflectivity coefficient (0 ≤ $k_s$ ≤ 1)
- $\vec{R}$ = unit vector representing the direction of perfectly reflected light
- $\vec{V}$ = unit vector pointing toward the viewer
- $n$ = shininess coefficient (specular exponent)
- $\vec{R} \cdot \vec{V} = \cos\alpha$ where α is the angle between R and V

The shininess coefficient $n$ controls the size of the specular highlight. Higher values produce smaller, sharper highlights (glossy surfaces), while lower values produce larger, more spread-out highlights (matte surfaces).

#### Combined Phong Illumination Model
The complete Phong reflection model combines all three components:

$$I = k_a I_a + k_d I_l (\vec{N} \cdot \vec{L}) + k_s I_l (\vec{R} \cdot \vec{V})^n$$

For colored surfaces and lights, this computation is performed separately for each RGB component.

### 2. Shading Models

Shading models determine how illumination is applied across polygon surfaces to produce the final pixel colors.

#### Flat Shading (Constant Shading)
In flat shading, the illumination is computed once per polygon using the polygon's normal. All pixels of the polygon receive the same color value.

**Advantages:** Fastest computational method, minimal memory requirements
**Disadvantages:** Visible polygon edges, "low-poly" appearance

Flat shading is suitable for scenes with small polygons or when maximum performance is required.

#### Gouraud Shading
Gouraud shading computes illumination at each vertex of a polygon and interpolates the resulting colors across the surface using **bilinear interpolation**.

**Process:**
1. Calculate surface normal at each vertex
2. Compute illumination intensity at each vertex using the illumination model
3. Interpolate vertex intensities across the polygon to get pixel colors

**Advantages:** Smoother color transitions than flat shading, eliminates visible polygon edges in many cases
**Disadvantages:** May miss specular highlights if vertices are not sufficiently dense

#### Phong Shading
Phong shading interpolates the **surface normals** across the polygon (rather than intensities) and computes the illumination model at each pixel.

**Process:**
1. Interpolate normals across the polygon surface
2. At each pixel, compute the illumination using the interpolated normal
3. This allows specular highlights to appear correctly even between vertices

**Advantages:** Highest quality, accurate specular highlights, smooth surface appearance
**Disadvantages:** Most computationally expensive, requires more processing per pixel

### 3. Light Attenuation

Real light intensity decreases with distance from the source. This is modeled using attenuation factors:

$$I_{attenuated} = \frac{I_{original}}{c_0 + c_1d + c_2d^2}$$

Where:
- $d$ = distance from light source
- $c_0$, $c_1$, $c_2$ = constant, linear, and quadratic attenuation coefficients

### 4. Blinn-Phong Model (Modified Phong)

The Blinn-Phong model replaces the $\vec{R} \cdot \vec{V}$ calculation with $\vec{N} \cdot \vec{H}$, where $\vec{H}$ is the **halfway vector** (bisector of light and view directions):

$$\vec{H} = \frac{\vec{L} + \vec{V}}{|\vec{L} + \vec{V}|}$$

This simplifies calculations and produces slightly different highlight shapes that some artists prefer. It is the default shading model in many graphics APIs.

## Examples

### Example 1: Computing Diffuse Reflection

**Problem:** A point light source is positioned at (5, 3, 4) and a surface point has a normal vector pointing toward (1, 1, 1). The diffuse coefficient $k_d$ = 0.7 and light intensity $I_l$ = 1.0. Calculate the diffuse component of illumination.

**Solution:**

**Step 1:** Compute unit vectors
$$\vec{L} = \frac{(5, 3, 4)}{\sqrt{25 + 9 + 16}} = \frac{(5, 3, 4)}{\sqrt{50}} = \frac{(5, 3, 4)}{7.071} = (0.707, 0.424, 0.566)$$

$$\vec{N} = \frac{(1, 1, 1)}{\sqrt{1 + 1 + 1}} = \frac{(1, 1, 1)}{\sqrt{3}} = \frac{(1, 1, 1)}{1.732} = (0.577, 0.577, 0.577)$$

**Step 2:** Compute dot product
$$\vec{N} \cdot \vec{L} = (0.577)(0.707) + (0.577)(0.424) + (0.577)(0.566)$$
$$= 0.408 + 0.245 + 0.327 = 0.980$$

**Step 3:** Apply Lambert's law
$$I_{diffuse} = k_d \times I_l \times (\vec{N} \cdot \vec{L})$$
$$= 0.7 \times 1.0 \times 0.980 = 0.686$$

The diffuse component intensity is 0.686 (or 68.6% of maximum).

### Example 2: Comparing Shading Methods

**Problem:** A square quad has vertices with computed illumination intensities of 0.2, 0.4, 0.6, and 0.8 at its four corners (starting top-left and going clockwise). Show how the intensity at pixel position (3, 3) would be computed using Gouraud shading.

**Solution:**

**Step 1:** Assume the quad spans from (0,0) to (6,6), so pixel (3,3) is at the center (50% horizontally, 50% vertically).

**Step 2:** Gouraud shading uses bilinear interpolation.

First, interpolate along the top edge (intensities 0.2 to 0.4):
$$I_{top} = 0.2 + (0.4 - 0.2) \times \frac{3}{6} = 0.2 + 0.2 \times 0.5 = 0.3$$

Interpolate along the bottom edge (intensities 0.8 to 0.6):
$$I_{bottom} = 0.8 + (0.6 - 0.8) \times \frac{3}{6} = 0.8 + (-0.2) \times 0.5 = 0.7$$

**Step 3:** Interpolate vertically between top and bottom:
$$I_{pixel} = 0.3 + (0.7 - 0.3) \times \frac{3}{6} = 0.3 + 0.4 \times 0.5 = 0.5$$

The pixel intensity is 0.5 using Gouraud shading.

### Example 3: Specular Highlight with Shininess

**Problem:** A surface has specular coefficient $k_s$ = 0.5, shininess exponent $n$ = 32, light intensity $I_l$ = 1.0. If $\vec{R} \cdot \vec{V}$ = 0.9, calculate the specular component and explain the visual effect.

**Solution:**

$$I_{specular} = k_s \times I_l \times (\vec{R} \cdot \vec{V})^n$$
$$= 0.5 \times 1.0 \times (0.9)^{32}$$
$$= 0.5 \times 0.036$$
$$= 0.018$$

With $n$ = 32 (high shininess), even though $\vec{R} \cdot \vec{V}$ = 0.9 (close to perfect reflection), the result is only 0.018. This creates a small, concentrated specular highlight typical of polished surfaces like mirrors or wet paint. If $n$ were 8 (lower shininess), the result would be:
$$I_{specular} = 0.5 \times (0.9)^8 = 0.5 \times 0.43 = 0.215$$
This produces a larger, more diffuse highlight typical of less polished materials.

## Exam Tips

1. **Remember the three components of Phong model**: Ambient ($k_a I_a$), Diffuse ($k_d I_l (\vec{N} \cdot \vec{L})$), and Specular ($k_s I_l (\vec{R} \cdot \vec{V})^n$). Questions often ask you to write the complete formula.

2. **Diffuse reflection follows Lambert's cosine law**: The intensity is maximum when light is perpendicular to the surface (N·L = 1) and zero when light is parallel or behind the surface.

3. **Gouraud vs Phong shading**: Remember that Gouraud interpolates **intensity values** while Phong interpolates **normals**. Phong produces better specular highlights because it computes illumination at each pixel.

4. **Shininess coefficient effect**: Higher $n$ values produce smaller, sharper highlights (glossy surfaces); lower $n$ values produce larger, diffuse highlights (matte surfaces).

5. **Flat shading is fastest**: For exam questions comparing shading methods, flat shading requires only one illumination calculation per polygon, making it the most efficient.

6. **Blinn-Phong optimization**: The Blinn-Phong model uses halfway vector H = (L+V)/|L+V| and computes N·H instead of R·V, avoiding the reflection vector calculation.

7. **Color computation**: When dealing with colored lights and surfaces, compute illumination separately for R, G, and B components using respective reflectivity coefficients.

8. **Attenuation formula**: Remember the quadratic attenuation model I = I₀/(c₀ + c₁d + c₂d²), which realistically models light falloff with distance.