# Revision Notes for Chap-2 (2.2) - Image Formation: Photometric Image

=============================================

## Introduction

---

- **Definition**: Photometric image is a representation of the intensity of light in a scene.
- **Key concept**: Image formation is a fundamental aspect of computer vision.

## Image Formation Process

---

- **Incident Radiance**: Radiance of light rays incident on a surface
- **Reflectance**: Interaction between incident radiance and surface properties
- **Viewing Condition**: Observer's position and orientation

## Key Formulas and Equations

---

- **Radiance**: $L(\lambda, \theta_s, \theta_r)$
- **Reflectance**: $R(\lambda, \theta_s, \theta_r)$
- **Viewing Condition**: $I(x, y, z) = L(\lambda, \theta_s, \theta_r) \cdot R(\lambda, \theta_s, \theta_r)$

## Important Theorems and Definitions

---

- **Lambert's Law**: $L(\lambda, \theta_s, \theta_r) = \frac{S}{A} \cdot \cos(\theta_r)$
- **Bidirectional Reflectance Distribution Function (BRDF)**: $R(\lambda, \theta_s, \theta_r)$

## Photometric Image Parameters

---

- **Illumination**: Total amount of light in a scene
- **Viewing Angle**: Angle between the observer's line of sight and the surface normal
- **Surface Reflectance**: Ratio of reflected light to incident light
