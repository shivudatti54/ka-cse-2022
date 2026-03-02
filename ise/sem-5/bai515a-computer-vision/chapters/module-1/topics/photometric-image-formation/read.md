# Photometric Image Formation

## Introduction to Photometric Image Formation

Photometric image formation is the fundamental process by which light interacts with surfaces and is captured by imaging systems to create digital images. It forms the basis for understanding how computer vision systems perceive and interpret visual information from the world. This process involves understanding light sources, surface properties, and the camera's response to light.

At its core, photometric image formation answers the question: "How does light from the real world become pixel values in a digital image?" Understanding this process is crucial for developing computer vision algorithms that can accurately interpret images, estimate scene properties, and perform tasks like object recognition, 3D reconstruction, and scene understanding.

## The Physics of Light and Surfaces

### Light Sources and Illumination

Light sources can be categorized based on their properties:

**Types of Light Sources:**

- **Point sources**: Emit light from a single point in all directions
- **Directional sources**: Emit light from a specific direction (like the sun)
- **Area sources**: Emit light from an extended area
- **Ambient light**: General, non-directional illumination

**Light Properties:**

- **Intensity**: The amount of light energy emitted per unit time
- **Color temperature**: The color characteristics of the light source
- **Spectral distribution**: How light energy is distributed across wavelengths

### Surface Reflection Models

When light strikes a surface, it can be reflected, absorbed, or transmitted. The interaction depends on the surface properties:

**Diffuse Reflection (Lambertian Surfaces):**

- Light is scattered equally in all directions
- Appearance doesn't change with viewing angle
- Brightness depends on the angle between light source and surface normal
- Mathematically: I = kₐIₐ + kₑIₑ + kₑIₑmax(0, n·l)
  Where: I = observed intensity, kₐ = ambient coefficient, Iₐ = ambient light, kₑ = diffuse coefficient, Iₑ = light intensity, n = surface normal, l = light direction

```
Light Source
     |
     v
     *-----> Reflected Light (equal in all directions)
    / \
Surface Normal
```

**Specular Reflection:**

- Light is reflected in a specific direction (like a mirror)
- Creates highlights that move with viewing angle
- Mathematically: I = kₛIₑmax(0, (r·v)^α)
  Where: kₛ = specular coefficient, r = reflection direction, v = viewing direction, α = shininess exponent

```
Light Source
     |
     v
     *-----> Reflected Light (specific direction)
    / \
Surface Normal
```

**Comparison of Reflection Types:**

| Property           | Diffuse Reflection | Specular Reflection |
| ------------------ | ------------------ | ------------------- |
| Direction          | Scattered equally  | Specific direction  |
| View dependence    | No                 | Yes                 |
| Surface type       | Matte surfaces     | Shiny surfaces      |
| Mathematical model | Lambertian         | Phong, Blinn-Phong  |
| Appearance         | Uniform brightness | Highlights          |

## The Image Formation Process

### The Pinhole Camera Model

The simplest model of image formation is the pinhole camera:

```
Real World
   |
   |  Light rays
   v
  [ ] -> Pinhole
   |
   v
Image Plane (Upside down)
```

The relationship between a 3D point (X, Y, Z) and its 2D projection (x, y) is given by:
x = f _ X/Z
y = f _ Y/Z
Where f is the focal length.

### The Digital Camera Process

Modern digital cameras use a more complex process:

1. **Light enters** through the lens assembly
2. **Focusing** occurs as light passes through lenses
3. **Aperture control** regulates the amount of light
4. **Shutter control** determines exposure time
5. **Light strikes** the sensor (CCD or CMOS)
6. **Photons are converted** to electrical charge
7. **Analog-to-digital conversion** creates pixel values
8. **Image processing** (demosaicing, white balance, etc.)
9. **Compression and storage**

```
World -> Lens -> Aperture -> Shutter -> Sensor -> ADC -> Processor -> Digital Image
```

## Radiometry and Photometry

### Radiometric Quantities

Radiometry deals with the measurement of electromagnetic radiation:

- **Radiant flux (Φ)**: Total power emitted by a source (Watts)
- **Irradiance (E)**: Power incident on a surface per unit area (W/m²)
- **Radiance (L)**: Power emitted from a surface per unit solid angle per unit projected area (W/sr·m²)

### Photometric Quantities

Photometry measures light as perceived by the human eye:

- **Luminous flux**: Radiant flux weighted by human eye sensitivity (lumens)
- **Illuminance**: Luminous flux incident on a surface per unit area (lux)
- **Luminance**: Luminous intensity per unit area (cd/m² or nits)

**Conversion between radiometry and photometry:**
Photometric quantity = Radiometric quantity × Luminous efficacy
Where luminous efficacy represents the eye's sensitivity to different wavelengths.

## The Image Irradiance Equation

The fundamental equation relating scene radiance to image irradiance is:

E = L _ (π/4) _ (d/f)² \* cos⁴θ

Where:

- E = Image irradiance (power/area on sensor)
- L = Scene radiance (power/area/solid angle)
- d = Lens diameter
- f = Focal length
- θ = Angle between optical axis and ray direction

This equation shows that:

1. Image irradiance is proportional to scene radiance
2. The f-number (f/d) affects the amount of light
3. The cos⁴θ term causes vignetting (darker corners)

## The Digital Image Representation

### From Irradiance to Pixel Values

The process of converting light to digital values involves:

1. **Spatial sampling**: Continuous image → discrete grid
2. **Quantization**: Continuous intensity → discrete levels
3. **Color filtering**: Using Bayer pattern or other color filter arrays

**Bayer Pattern (most common):**

```
R G R G R G
G B G B G B
R G R G R G
G B G B G B
```

50% green, 25% red, 25% blue pixels, matching human eye sensitivity

### Camera Response Function

The camera response function (CRF) describes how incident light is mapped to pixel values:

I = f(E \* Δt)

Where:

- I = Pixel intensity
- E = Image irradiance
- Δt = Exposure time
- f = Nonlinear camera response function

The CRF is typically nonlinear due to:

- Gamma correction (approximately I ∝ E^γ)
- Sensor saturation
- Noise characteristics

## Applications in Computer Vision

Understanding photometric image formation enables several computer vision applications:

**Photometric Stereo:**
Recovering surface normals from multiple images under different lighting conditions.

**Shape from Shading:**
Estimating surface shape from intensity variations in a single image.

**Radiometric Calibration:**
Recovering the camera response function for high dynamic range imaging.

**Intrinsic Image Decomposition:**
Separating an image into illumination and reflectance components.

**Material Recognition:**
Identifying surface materials based on their reflective properties.

## Challenges and Limitations

**Real-world complications:**

- Non-Lambertian surfaces (specularities, translucency)
- Complex illumination (multiple light sources, interreflections)
- Sensor noise and limitations
- Lens distortions and aberrations
- Color inaccuracies and metamerism

**Interreflections:**
Light bounces between surfaces before reaching the camera, causing:

- Color bleeding
- Reduced contrast
- Incorrect brightness estimates

```
Surface A -> Reflects light -> Surface B -> Reflects light -> Camera
```

## Exam Tips

1. **Understand the difference** between radiometric and photometric quantities - radiometry deals with physical light measurements, while photometry weights these by human eye sensitivity.

2. **Memorize the image irradiance equation** and understand what each term represents. Be able to explain how changing parameters (like f-number) affects the image.

3. **Know the reflection models** - be able to distinguish between Lambertian (diffuse) and specular reflection, and describe the mathematical models for each.

4. **Understand the complete pipeline** from scene radiance to digital pixel values, including the role of the camera response function.

5. **Practice converting** between different representations of light and surface properties.

6. **Be familiar with applications** that rely on photometric principles, such as photometric stereo and shape from shading.

7. **Recognize the limitations** of simple models - real-world surfaces often don't follow ideal Lambertian or specular models perfectly.
