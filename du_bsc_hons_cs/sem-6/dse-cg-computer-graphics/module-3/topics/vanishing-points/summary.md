# Vanishing Points — Quick Revision Summary

**Subject:** Dse Cg — Computer Graphics  
**Course:** BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)

---

## Introduction

Vanishing points are fundamental to perspective projection in computer graphics. They represent the point on the horizon where parallel lines appear to converge, creating the illusion of depth on a 2D surface. Understanding vanishing points is essential for realistic 3D rendering and scene representation.

---

## Key Concepts

### What is a Vanishing Point?
- A point on the horizon line where parallel lines seem to meet
- Creates the perception of depth and distance in 2D images
- Based on how human vision perceives parallel lines extending into the distance

### Types of Perspective Systems

**One-Point Perspective**
- Single vanishing point on the horizon
- Used when viewing a scene directly from the front
- Parallel lines converge to one point
- Common in railway tracks, corridors, architectural interiors

**Two-Point Perspective**
- Two vanishing points on the horizon line
- Used when viewing objects from a corner angle
- Vertical lines remain vertical; horizontal lines converge to two points
- Common in architectural exteriors, boxes, buildings

**Three-Point Perspective**
- Three vanishing points (two on horizon, one above or below)
- Used for dramatic viewpoints (looking up or down)
- No vertical parallel lines remain
- Common in tall buildings, aerial views, dramatic cinematography

### Mathematical Basis
- **Projection plane:** 2D surface where the 3D scene is rendered
- **Center of projection:** The viewer's eye position
- **Projection lines:** Rays from center of projection through 3D points to the projection plane
- Vanishing points occur where projection lines become parallel to principal axes

### Applications in Computer Graphics
- 3D rendering and scene composition
- Camera modeling and view transformation
- Drawing and design software
- Game environments and virtual reality
- Architectural visualization

---

## Delhi University Syllabus Coverage

This topic aligns with:
- **Unit III:** Viewing and Projection Transforms
- Perspective projections and vanishing point calculations
- Understanding how 3D-to-2D transformation works

---

## Conclusion

Vanishing points are essential for achieving realistic perspective in computer graphics. Mastery of one-point, two-point, and three-point perspective systems enables effective depth representation in 3D rendering. This concept forms the foundation for camera models, rendering pipelines, and architectural visualization in modern graphics applications.

**Quick Recall:** Vanishing Point = Point where parallel lines converge on the horizon → Creates depth illusion in 2D representation of 3D space.