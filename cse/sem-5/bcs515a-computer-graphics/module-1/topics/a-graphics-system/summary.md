# Computer Graphics System - Summary

## Key Definitions and Concepts

- **Computer Graphics**: The creation, manipulation, and representation of visual information using computers
- **Display Device**: Output hardware that converts digital data into visual form
- **Refresh Rate**: Number of times per second a display redraws the screen (measured in Hz)
- **Resolution**: Number of pixels displayed horizontally and vertically (e.g., 1920 × 1080)
- **Color Depth**: Number of bits used to represent each pixel's color (e.g., 24-bit = 16.7 million colors)
- **DPI (Dots Per Inch)**: Printer resolution measurement
- **Hard Copy**: Permanent physical output (printed paper)
- **Soft Copy**: Temporary screen display output

## Important Formulas and Theorems

- **Time per scan line** (CRT) = (1/Refresh Rate) / Total Scan Lines
- **Frame memory requirement** = Horizontal Resolution × Vertical Resolution × Color Depth (in bits) / 8 = Result in bytes
- **Total dots for printing** = Horizontal DPI × Horizontal Size × Vertical DPI × Vertical Size
- **Color combinations** = 2^(bits per color channel × number of channels)

## Key Points

- A computer graphics system consists of display devices, input devices, hard copy devices, and graphics software
- CRT displays use electron beams to excite phosphors; LCD displays use liquid crystals with backlighting
- Raster scan displays the entire screen row by row; random scan draws vectors to specific points
- Common input devices include mouse, keyboard, digitizer (graphics tablet), light pen, and touch screen
- Impact printers (dot matrix) use mechanical striking; non-impact (inkjet, laser) use ink/toner without striking
- Plotters are specialized output devices for large-format technical drawings
- Graphics software includes system software (GDI, OpenGL, DirectX) and application software (CAD, paint programs)
- GKS is the ISO standard for 2D graphics; PHIGS supports 3D hierarchical graphics
- Higher refresh rate reduces flicker; minimum 60 Hz recommended for comfortable viewing

## Common Mistakes to Avoid

1. Confusing DPI with PPI - DPI is for printers, PPI is for digital images
2. Assuming LCD and LED are completely different technologies - LED displays are LCDs with LED backlights
3. Mixing up refresh rate and response time - Refresh rate is screen redraw frequency, response time is pixel change speed
4. Confusing vector and raster graphics storage - Vector stores mathematical descriptions, raster stores pixel values
5. Forgetting that color depth is per channel - 24-bit color means 8 bits each for R, G, and B

## Revision Tips

1. Create comparison tables for different display technologies (CRT, LCD, LED, Plasma) listing working principle, advantages, disadvantages
2. Memorize the formula for calculating frame buffer memory with the resolution and color depth
3. Practice calculating print resolution and total dots for different paper sizes
4. Remember that graphics standards (GKS, PHIGS) are device-independent interfaces
5. Focus on understanding why certain devices are used for specific applications (CAD uses digitizers, largeformat prints use plotters)
