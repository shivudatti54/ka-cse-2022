# Light Sources in Computer Graphics

## Introduction

Light sources are fundamental components in computer graphics that simulate illumination in virtual 3D environments. Without proper lighting, three-dimensional scenes appear flat and lack realism. The study of light sources is essential for understanding how rendering engines create visually appealing images by simulating how light interacts with surfaces in the real world. In the context of 's Computer Graphics curriculum, understanding light sources forms the foundation for advanced topics like shading models, ray tracing, and global illumination.

Light sources in computer graphics are mathematical models that approximate real-world lighting behavior. Different types of light sources are used to simulate various real-world lighting conditions, from the soft illumination of an overcast sky to the focused beam of a spotlight. The choice of light source and its parameters significantly impacts the mood, visibility, and visual quality of a rendered scene. Modern graphics applications use multiple light sources simultaneously to create complex lighting setups that enhance scene realism.

## Key Concepts

### Types of Light Sources

**1. Ambient Light**
Ambient light represents the simplest form of illumination in computer graphics. It is a uniform, non-directional light that illuminates all surfaces equally from all directions. Ambient light has no specific source or direction and provides base illumination to prevent objects from appearing completely black in shadowed areas. The intensity remains constant regardless of surface orientation or position. In mathematical terms, ambient lighting is calculated as:

```
I_ambient = k_a × I_a
```

where k_a is the ambient reflection coefficient and I_a is the ambient light intensity.

**2. Point Light Sources**
A point light source emits light equally in all directions from a single location in 3D space, similar to a light bulb. The intensity of illumination decreases with distance from the source following the inverse square law. Point lights have position coordinates (x, y, z) and parameters for color and intensity. They create realistic falloff effects and are commonly used for indoor lighting simulation. The intensity at a surface is calculated as:

```
I_point = I_l / (d² + 1)
```

where d is the distance from the light source to the surface.

**3. Directional Light Sources**
Directional lights simulate distant light sources like the sun, where light rays are parallel when they reach the scene. These lights have direction but no specific position in space. The intensity remains constant regardless of distance from the "source," making them computationally efficient for outdoor scenes. Directional lights are characterized by a direction vector and are particularly useful for creating consistent shadows across large areas. They are commonly used in game engines and real-time applications.

**4. Spot Light Sources**
Spot lights emit light within a specific cone-shaped region, similar to a flashlight or theatrical spotlight. They have position, direction, and two additional parameters: the angle of the cone (spread angle) and falloff rate. Light intensity decreases from the center of the cone toward the edges. Spot lights create focused illumination and dramatic shadow effects, making them essential for highlighting specific objects or creating mood in rendered scenes.

**5. Area Light Sources**
Area lights emit light from a finite surface area rather than a single point, producing soft shadows and more realistic illumination. Unlike point or directional lights, area lights create penumbras—soft shadow edges where light transitions from full illumination to complete shadow. These lights are computationally expensive but essential for photorealistic rendering.

### Light Attenuation

Attenuation describes how light intensity decreases with distance from the source. Real-world light follows the inverse square law, where intensity is inversely proportional to the square of the distance. In computer graphics, simplified attenuation models are often used:

```
I = 1 / (a₀ + a₁d + a₂d²)
```

where a₀, a₁, and a₂ are constant, linear, and quadratic attenuation coefficients respectively. This formula allows graphics programmers to control how quickly light fades with distance.

### Light Colors and RGB Model

Light sources in computer graphics typically use the RGB color model. Each light has red, green, and blue components that combine additively to produce the final illumination color. White light contains equal amounts of all three components. Color interactions with surface materials determine the final visible color—a red light illuminating a blue surface produces black (no reflection), while illuminating a white surface produces red.

## Examples

### Example 1: Calculating Diffuse Reflection from a Point Light

**Problem:** A point light source with intensity (1.0, 1.0, 1.0) is positioned at (2, 3, 4). A surface point has position (3, 3, 3), surface normal N = (0, 1, 0), and diffuse reflection coefficient k_d = 0.8. Calculate the diffuse illumination.

**Solution:**

Step 1: Calculate the light direction vector L

```
L = Light Position - Surface Point
L = (2-3, 3-3, 4-3) = (-1, 0, 1)
|L| = √(1 + 0 + 1) = √2 ≈ 1.414
L_normalized = (-0.707, 0, 0.707)
```

Step 2: Calculate the dot product N·L

```
N·L = (0, 1, 0) · (-0.707, 0, 0.707) = 0
```

Step 3: Since N·L ≤ 0, the surface is oriented away from the light

```
I_diffuse = 0
```

The surface receives no diffuse illumination because it faces away from the light source.

### Example 2: Spotlight Intensity Calculation

**Problem:** A spotlight positioned at (0, 5, 0) illuminates a point at (3, 0, 0). The spotlight direction is (0, -1, 0), with a cone angle of 30° and falloff exponent of 2. Calculate the spotlight intensity if the point light component intensity is 1.0.

**Solution:**

Step 1: Calculate light direction to point

```
L = (3-0, 0-5, 0-0) = (3, -5, 0)
|L| = √(9 + 25) = √34 ≈ 5.83
L_normalized = (0.514, -0.857, 0)
```

Step 2: Calculate angle between spotlight direction and L

```
cos(θ) = D · L = (0, -1, 0) · (0.514, -0.857, 0) = 0.857
θ = arccos(0.857) ≈ 31°
```

Step 3: Since θ > 30° (cone angle), intensity is 0

```
I_spot = 0
```

The point lies outside the spotlight's cone of illumination.

### Example 3: Three-Point Lighting Setup

**Problem:** Design a basic three-point lighting setup for product photography and calculate combined intensity at a point with normal (0, 1, 0).

**Solution:**

Three-point lighting consists of:

1. **Key Light:** Primary light source, typically a directional or spot light at 45° to the subject
2. **Fill Light:** Softer light on the opposite side to reduce harsh shadows
3. **Back Light (Rim Light):** Positioned behind the subject to separate it from the background

For a point at origin with normal (0, 1, 0):

- Key light at position (5, 5, 5) with intensity 1.0
- Fill light at position (-5, 3, 5) with intensity 0.5
- Back light at position (0, 5, -5) with intensity 0.3

The combined illumination is the sum of individual light contributions, allowing photographers and 3D artists to create balanced, professional-looking illumination.

## Exam Tips

1. **Remember the lighting equation:** The final surface color is typically computed as I = I_ambient × k_a + I_diffuse × k_d × (N·L) + I_specular × k_s × (N·H)^n. This is a frequently asked question in exams.

2. **Differentiate light types:** Be able to explain the differences between ambient, point, directional, and spot lights with practical examples for each.

3. **Understand attenuation:** Know the inverse square law and how it affects point light intensity over distance.

4. **Phong shading model:** Understand the three components—ambient, diffuse, and specular—and their respective coefficients.

5. **Vector mathematics:** Be comfortable calculating dot products between normal and light direction vectors for diffuse reflection.

6. **Real-world analogies:** Relate computer graphics lights to real-world sources: directional to sunlight, point to light bulbs, spot to flashlights.

7. **Spotlight cone:** Remember that spotlight intensity is highest at the center and decreases toward the cone edges using the falloff exponent.

8. **Color computation:** Understand how RGB values combine additively and how surface colors interact with light colors.
