# Graphics Architectures - Summary

## Key Definitions and Concepts

- **Raster Scan Display:** A display system where the electron beam (or pixel array) scans across the screen row by row, from left to right and top to bottom.
- **Frame Buffer:** Dedicated video memory that stores the complete image to be displayed, with each pixel location corresponding to a screen pixel.
- **Video Controller:** Hardware component that manages timing and data flow between frame buffer and display, generating synchronization signals.
- **GPU (Graphics Processing Unit):** Specialized processor optimized for parallel graphics operations and rendering tasks.
- **Double Buffering:** Technique using two frame buffers (front and back) to eliminate screen flicker during animation.
- **Refresh Rate:** Number of times per second the display is redrawn, typically measured in Hertz (Hz).
- **Color Depth:** Number of bits used to represent the color of each pixel, determining the total number of possible colors.

## Important Formulas and Theorems

- **Frame Buffer Size (bytes):** Resolution (H × V) × Bytes per pixel
- **Memory Bandwidth (bytes/sec):** Resolution × Bytes per pixel × Refresh Rate
- **Color Depth to Colors:** 2^n colors where n is the number of bits per pixel

## Key Points

1. CRT displays use electron beams to excite phosphors, while LCD displays use liquid crystals controlled by electric fields to modulate light.

2. OLED displays have self-emitting pixels, enabling true blacks and superior contrast compared to LCDs which require backlights.

3. The frame buffer stores pixel data that the video controller continuously reads to generate the display signal.

4. Double buffering eliminates flicker by ensuring complete frames are displayed, never partially drawn ones.

5. The GPU operates in parallel with the CPU, offloading graphics computations from the main processor.

6. Raster scan systems dominate modern displays because they can render filled areas and complex images, unlike vector systems.

7. The video controller operates independently of the CPU, providing autonomous display refreshing.

8. Vertical blanking interval is the optimal time for swapping front and back buffers in double buffering.

9. Color depth of 24 bits provides over 16 million colors (16.7 million to be precise: 256 × 256 × 256).

10. Modern GPUs contain thousands of processing cores for parallel execution of shader programs.

## Common Mistakes to Avoid

1. Confusing raster scan with vector scan systems—raster is row-by-row scanning, vector is point-to-point drawing.

2. Forgetting that color depth is in bits, not bytes—24-bit color equals 3 bytes per pixel, not 24 bytes.

3. Not accounting for all components of the graphics system when calculating memory requirements.

4. Assuming the video controller and GPU are the same—they have distinct roles in the graphics pipeline.

5. Overlooking the importance of refresh rate in preventing display flicker and eye strain.

## Revision Tips

1. Draw a block diagram of the complete graphics architecture and label all components and data flows.

2. Practice frame buffer size calculations for various common resolutions (720p, 1080p, 4K) and color depths.

3. Memorize the sequence of operations in the graphics pipeline from application to display.

4. Review the advantages and disadvantages of each display technology (CRT, LCD, LED, OLED).

5. Understand the concept of vertical blanking interval and why it matters for buffer swapping in animation.
