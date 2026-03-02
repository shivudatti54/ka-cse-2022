# Raster Random Scan Devices

## Introduction

Raster Random Scan Devices are fundamental display technologies in computer graphics, representing two distinct approaches to rendering images on cathode ray tube (CRT) displays. Understanding these devices is essential for the DSE CG (Computer Graphics) paper under the Delhi University BSc (H) Computer Science NEP 2024 UGCF syllabus. These devices differ primarily in their electron beam scanning methods and image construction techniques.

---

## Key Concepts

### **Definition & Working Principle**
- **Raster Scan**: Electron beam scans the entire screen row by row (horizontal lines), from top to bottom. Uses a *frame buffer* (refresh buffer) to store complete image data
- **Random Scan (Vector Scan)**: Electron beam directly draws vectors/lines to specific screen points only where needed, like an oscilloscope

### **Architecture & Components**
- **Frame Buffer**: Dedicated memory storing pixel values (intensity, color) for each screen location
- **CRT (Cathode Ray Tube)**: Primary display device with electron gun, focusing system, and phosphor screen
- **Refresh Circuitry**: Continuously redraws the image (typically 60-80 times/second) to maintain display
- **Display Controller**: Interfaces between CPU frame buffer and display hardware

### **Critical Differences**

| Feature | Raster Scan | Random Scan |
|---------|-------------|-------------|
| Scanning Method | Sequential (line-by-line) | Directed (point-to-point) |
| Image Storage | Full frame buffer required | Command/vector list only |
| Solid Fill | Easy (bitmap-based) | Difficult |
| Resolution | Limited by frame buffer size | Higher for line drawings |
| Applications | TV, monitors, games | CAD, animation |

### **Advantages & Disadvantages**

**Raster Scan Advantages:**
- Supports color and complex shading
- Suitable for realistic/raster images
- Cost-effective for mass production

**Random Scan Advantages:**
- Higher line drawing quality
- Faster for wireframe/vector graphics
- Better resolution control

### **Exam-Relevant Points (DU Syllabus)**
- Resolution calculation: Horizontal pixels × Vertical pixels
- Refresh rate impact on flicker (minimum 60 Hz recommended)
- Color depth: Number of bits per pixel determines colors (e.g., 8-bit = 256 colors)
- Interlacing vs. non-interlaced displays

---

## Conclusion

Raster and Random scan devices form the foundation of display technology in computer graphics. For Delhi University exams, focus on comparing these devices, understanding frame buffer concepts, and knowing when each type is preferred. Questions often test the distinction between these scanning methods and their practical applications in graphics systems.