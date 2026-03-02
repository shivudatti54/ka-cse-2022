# Light and Matter Interaction in Computer Graphics

## Introduction

In computer graphics, the interaction between light and surfaces is fundamental to creating realistic images. When we render a 3D scene, we must simulate how light behaves when it strikes surfaces—this is the domain of **illumination models** or **reflection models**. Unlike physical optics, which deals with the true behavior of light, computer graphics uses simplified mathematical models that produce visually convincing results in real-time.

**Light and matter interaction** in CG refers to how surfaces reflect, absorb, and transmit light. The key insight is that when light hits a surface, it can be reflected in different ways depending on the material properties. Understanding these interactions allows us to compute the color seen at each pixel on a surface.

---

## 1. The Nature of Light in Computer Graphics

In CG, we treat light as **rays** that travel from light sources to surfaces, then to the camera (eye). This simplification, though not physically perfect, works remarkably well for visual rendering.

### Types of Light-Surface Interaction

- **Reflection**: Light bounces off the surface
- **Absorption**: Light is absorbed by the material (converted to heat)
- **Transmission**: Light passes through transparent surfaces

For opaque surfaces (most common in CG), we focus primarily on reflection.

---

## 2. Reflection Models

A reflection model defines how light is reflected from a surface. Three fundamental types form the foundation:

### 2.1 Ambient Reflection

Ambient light represents the **minimum light** in a scene, simulating light that has bounced around so many times it seems to come from everywhere. It's a constant term added to every surface.

**Characteristics:**

- Independent of viewer position and light direction
- Represents indirect illumination
- Same intensity everywhere in the scene

**Formula:**

```
I_ambient = k_a × I_a
```

Where:

- `k_a` = ambient reflection coefficient (0 to 1)
- `I_a` = ambient light intensity

### 2.2 Diffuse Reflection

Diffuse reflection occurs on **matte or rough surfaces** (like clay, paper, unpolished wood). Light is scattered equally in all directions regardless of viewing angle.

**Characteristics:**

- Depends on the angle between light direction and surface normal
- Independent of viewer position
- Follows Lambert's Cosine Law

**Formula:**

```
I_diffuse = k_d × I_l × max(0, N · L)
```

Where:

- `k_d` = diffuse reflection coefficient
- `I_l` = light source intensity
- `N` = surface normal vector (unit vector)
- `L` = light direction vector (unit vector, pointing toward light)

**Example:** If sunlight hits a matte sphere directly (90° to surface), maximum light is reflected. If at an angle, less light is reflected proportionally.

### 2.3 Specular Reflection

Specular reflection creates **shiny highlights** on surfaces (like metal, plastic, wet surfaces). Light reflects in a concentrated direction, creating bright spots.

**Characteristics:**

- Depends on both light direction and viewer direction
- Produces the "shininess" effect
- Only visible when viewer is near the reflection angle

**Formula (Phong Model):**

```
I_specular = k_s × I_l × max(0, R · V)^n
```

Where:

- `k_s` = specular reflection coefficient
- `R` = reflection vector
- `V` = view direction vector (unit vector, pointing toward viewer)
- `n` = shininess exponent (higher = smaller highlight)

**The shininess exponent `n`:**

- Small `n` (e.g., 1-10): Broad, soft highlights (matte surfaces)
- Large `n` (e.g., 50-100): Sharp, small highlights (polished surfaces)
- Very large `n` (e.g., 500+): Mirror-like reflection

---

## 3. The Phong Reflection Model

The **Phong model** combines all three reflection types to create a complete illumination model:

### Complete Phong Equation

```
I_total = k_a × I_a
 + k_d × I_l × max(0, N · L)
 + k_s × I_l × max(0, R · V)^n
```

### Computing the Reflection Vector

The reflection vector **R** is computed from the light direction **L** and surface normal **N**:

```
R = 2 × (N · L) × N - L
```

### Practical Example

Consider a red plastic sphere under white light:

- `k_a = 0.1`, `k_d = 0.6`, `k_s = 0.4`
- `I_a = 0.2`, `I_l = 1.0`
- `n = 32` (plastic-like shininess)
- Surface color = red

The final color combines ambient (dark red), diffuse (bright red based on light angle), and specular (white highlight) components.

---

## 4. The Blinn-Phong Model

A popular variation, the **Blinn-Phong model**, replaces the reflection vector with a **halfway vector** for better visual results:

### Key Difference

Instead of `R · V`, use `N · H` where **H** is the halfway vector:

```
H = (L + V) / |L + V|
```

### Blinn-Phong Formula

```
I_specular = k_s × I_l × max(0, N · H)^n
```

**Advantages:**

- Faster to compute (no reflection vector needed)
- Produces more realistic highlights for grazing angles
- Used in early OpenGL and many games

---

## 5. Light Sources in Computer Graphics

Different light types simulate various real-world lighting scenarios:

### 5.1 Point Light

A light source that radiates in all directions from a single point.

**Characteristics:**

- Position matters; intensity decreases with distance
- Simulates: light bulbs, candles, flames
- **Attenuation**: Light intensity decreases with square of distance

**Attenuation Formula:**

```
I = I_0 / (1 + a₁d + a₂d²)
```

### 5.2 Directional Light

Light rays are parallel, coming from a single direction. No position—only direction matters.

**Characteristics:**

- No distance attenuation (infinite distance)
- Simulates: sunlight, moonlight
- Used for outdoor scenes

### 5.3 Spotlight

A focused beam of light that radiates within a cone.

**Characteristics:**

- Has position, direction, and cone angle
- Intensity decreases toward edges of cone
- Simulates: flashlights, stage lights, car headlights

**Spotlight Formula:**

```
if (angle > cutoff): I = 0
else: I = I_0 × (cos(θ) / cos(φ))^spotlight_exponent
```

Where:

- `θ` = angle between spotlight direction and point-to-light vector
- `φ` = spotlight cutoff angle
- `spotlight_exponent` = controls falloff rate

### Comparison Table

| Property    | Point Light    | Directional Light | Spotlight   |
| ----------- | -------------- | ----------------- | ----------- |
| Position    | Yes            | No                | Yes         |
| Direction   | N/A            | Yes               | Yes         |
| Attenuation | Yes (distance) | No                | Yes (angle) |
| Cone effect | No             | No                | Yes         |
| Real-world  | Light bulb     | Sun               | Flashlight  |

---

## 6. Material Properties

Materials are defined by their **coefficients** and **shininess**:

### Material Coefficients

| Coefficient | Symbol | Range | Effect                    |
| ----------- | ------ | ----- | ------------------------- |
| Ambient     | k_a    | 0-1   | Base brightness in shadow |
| Diffuse     | k_d    | 0-1   | Surface color intensity   |
| Specular    | k_s    | 0-1   | Highlight brightness      |
| Shininess   | n      | 1-∞   | Highlight size/sharpness  |

### Common Material Values

| Material      | k_a | k_d | k_s | n    |
| ------------- | --- | --- | --- | ---- |
| Black plastic | 0.0 | 0.0 | 0.5 | 32   |
| Red plastic   | 0.0 | 0.6 | 0.4 | 32   |
| Brass         | 0.1 | 0.6 | 0.8 | 64   |
| White cloth   | 0.4 | 0.4 | 0.0 | 1    |
| Glass         | 0.1 | 0.1 | 1.0 | 128+ |

---

## 7. Shading Models

Shading determines **how to apply the illumination model** across a surface:

### 7.1 Flat Shading

- One color per polygon
- Uses polygon normal
- Fast but produces faceted look

### 7.2 Gouraud Shading

- Interpolates vertex colors across polygon
- Creates smooth transitions
- May miss specular highlights if vertices don't capture them

### 7.3 Phong Shading

- Interpolates normals across polygon
- Computes lighting per pixel
- Highest quality, most computationally expensive

### Shading Comparison

| Method  | Quality | Speed   | Use Case           |
| ------- | ------- | ------- | ------------------ |
| Flat    | Low     | Fastest | Low-poly, stylized |
| Gouraud | Medium  | Fast    | Most games         |
| Phong   | High    | Slow    | Quality renders    |

---

## 8. The Rendering Equation Basics

The **rendering equation** is the fundamental equation that describes light transport:

```
L_o(x, ω_o) = L_e(x, ω_o) + ∫ f_r(x, ω_i, ω_o) L_i(x, ω_i) (ω_i · n) dω_i
```

In simpler terms:
**Outgoing Light = Emitted Light + Reflected Light**

### Simplified for Direct Illumination

```
I = k_a × I_a + Σ (illumination from each light source)
```

The Phong model is an **approximation** of the full rendering equation, considering only direct illumination and ignoring:

- Inter-object reflections
- Global illumination
- Subsurface scattering

---

## 9. Real-World Applications

### Video Games

- **Phong shading** used in most 3D games for characters and objects
- **Blinn-Phong** preferred for real-time rendering (faster)
- Material properties create distinct looks (metal, plastic, skin)

### Architectural Visualization

- Accurate material coefficients create realistic buildings
- Directional lights simulate sunlight at different times

### Film and Animation

- More complex models (PBR, ray tracing) build upon Phong fundamentals
- Understanding basics essential for advanced techniques

### Product Visualization

- High shininess values create realistic metal and glass
- Spotlight effects highlight products

---

## 10. Implementation Example

### Pseudocode: Phong Shading

```c
// Compute Phong illumination at a point
vec3 phongShading(vec3 normal, vec3 viewDir,
 vec3 lightDir, Material mat, Light light) {

 // Ambient component
 vec3 ambient = mat.k_a * light.I_a * mat.diffuseColor;

 // Diffuse component
 float NdotL = max(dot(normal, lightDir), 0.0);
 vec3 diffuse = mat.k_d * light.I_l * mat.diffuseColor * NdotL;

 // Specular component
 vec3 reflectDir = reflect(-lightDir, normal);
 float spec = pow(max(dot(viewDir, reflectDir), 0.0), mat.n);
 vec3 specular = mat.k_s * light.I_l * spec * vec3(1.0); // white highlight

 return ambient + diffuse + specular;
}
```

---

## Summary

**Key Takeaways:**

- **Ambient** = constant base lighting
- **Diffuse** = matte reflection, depends on N·L
- **Specular** = shiny highlights, depends on reflection angle
- **Phong model** = ambient + diffuse + specular combined
- Different **light types** simulate different real-world sources
- **Material properties** define how surfaces respond to light
- Understanding these foundations is essential for advanced rendering

---
