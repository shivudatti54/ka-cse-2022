# Light and Matter - Quick Reference

## Key Definitions

- **Illumination Model**: Mathematical model describing how light interacts with surfaces in computer graphics
- **Phong Reflection Model**: Combined ambient + diffuse + specular lighting model
- **Material Coefficients**: Properties (k_a, k_d, k_s, n) defining how surfaces respond to light

## Essential Formulas

### Phong Equation
```
I = k_a × I_a + k_d × I_l × max(0, N·L) + k_s × I_l × max(0, R·V)^n
```

### Reflection Vector
```
R = 2×(N·L)×N - L
```

### Blinn-Phong (specular term only)
```
I_spec = k_s × I_l × max(0, N·H)^n
H = (L + V) / |L + V|
```

## Light Source Types

| Type | Position | Direction | Attenuation |
|------|----------|-----------|-------------|
| Point | ✓ | - | Distance-based |
| Directional | ✗ | ✓ | None |
| Spotlight | ✓ | ✓ | Angle-based |

## Material Coefficients Reference

| Property | Symbol | Effect |
|----------|--------|--------|
| Ambient | k_a | Base brightness (0-1) |
| Diffuse | k_d | Matte color intensity (0-1) |
| Specular | k_s | Highlight brightness (0-1) |
| Shininess | n | Highlight sharpness (1-∞) |

## Must-Remember Points

- **N·L < 0** = surface in shadow (light behind) → no diffuse/specular contribution
- **Higher n** = smaller, sharper specular highlight (shinier surface)
- **R·V** = angle between reflection and view; maximum when viewing at reflection angle
- **Ambient** is view-independent; **diffuse** is view-independent; **specular** is view-dependent
- **Blinn-Phong** uses halfway vector, faster and better for grazing angles
- Flat → Gouraud → Phong: increasing quality and computation cost