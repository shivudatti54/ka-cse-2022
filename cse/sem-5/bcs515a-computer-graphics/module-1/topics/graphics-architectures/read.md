# Graphics Architectures

## Introduction

Computer graphics has revolutionized the way we interact with computers, enabling visual communication, simulation, gaming, and scientific visualization. At the heart of every graphics system lies its architecture—the complex arrangement of hardware components that work together to transform digital data into visual representations on a display. Understanding graphics architectures is fundamental for any computer science engineer, as it forms the backbone of modern computing applications ranging from simple GUI interfaces to sophisticated virtual reality systems.

The evolution of graphics architectures spans several decades, from simple vector displays to today's highly sophisticated graphics processing units (GPUs) capable of rendering photorealistic images in real-time. For students, grasping these architectures is essential not only for theoretical understanding but also for practical applications in software development, game design, and multimedia applications. The architecture determines the performance, capabilities, and limitations of any graphics system, making it a critical area of study in computer graphics.

Modern graphics architectures must handle multiple complex tasks simultaneously: receiving graphics commands from the CPU, managing geometry data, performing transformations, handling textures, and outputting pixel data to the display. This requires careful coordination between various hardware components, each specialized for specific aspects of the rendering pipeline. Understanding how these components interact provides the foundation for optimizing graphics performance and developing efficient graphical applications.

## Key Concepts

### Display Devices

**Cathode Ray Tube (CRT):** The CRT was the dominant display technology for several decades. It works by firing electron beams at a phosphorescent screen, causing pixels to light up. The electron beam scans across the screen in a pattern (raster), illuminating phosphors that glow briefly before fading. CRTs offer excellent color reproduction and fast response times but are bulky, consume significant power, and suffer from screen flicker at lower refresh rates.

**Liquid Crystal Display (LCD):** LCDs use liquid crystal molecules that align to either block or allow light to pass through pixel cells. Each pixel consists of sub-pixels for red, green, and blue channels. LCDs require a backlight (typically CCFL or LED) to illuminate the display. They offer thin profiles, low power consumption, and are the standard for modern displays. However, they have limited viewing angles and potential backlight bleeding issues.

**Light Emitting Diode (LED) and Organic LED (OLED):** LED displays use an array of LEDs as the light source for LCD panels, offering improved brightness and energy efficiency. OLED displays use organic compounds that emit light when electric current is applied, eliminating the need for backlighting. This enables true blacks (since pixels can be completely turned off), superior contrast ratios, and flexible form factors. OLED is increasingly common in smartphones and high-end televisions.

### Raster Scan Display Systems

In a raster scan system, the electron beam (or pixel array) moves across the screen from left to right, completing one row at a time, from top to bottom. This creates a grid of pixels called a raster. The complete image is refreshed multiple times per second (refresh rate, typically 60Hz or higher) to create the illusion of a steady image.

The horizontal blanking interval occurs when the beam returns from the right edge to the left edge of the next line, and the vertical blanking interval occurs during the return from the bottom to the top of the screen. These blanking periods are essential for timing and synchronization in the display system.

The resolution of a raster display is determined by the number of pixels in the horizontal and vertical directions (e.g., 1920×1080). The aspect ratio describes the proportional relationship between width and height. Color depth (bit depth) determines how many distinct colors can be displayed, with 24-bit color allowing for over 16 million colors.

### Frame Buffer and Video RAM

The frame buffer (or refresh buffer) is a dedicated memory area that stores the complete image to be displayed. Each pixel location in the frame buffer corresponds to a pixel on the screen. The video controller continuously reads from the frame buffer and converts the digital data into analog signals (or digital signals for digital displays) to drive the display.

The size of the frame buffer depends on the display resolution and color depth. For a 1920×1080 display with 24-bit color (8 bits per channel), the frame buffer requires 1920 × 1080 × 3 bytes ≈ 6.2 MB. Modern systems use dedicated Video RAM (VRAM) or Graphics RAM (GRAM) that provides high-bandwidth access for both the graphics processor and the video controller.

Multiple buffers are often used to improve performance. A double buffer scheme uses two frame buffers: one being displayed while the other is being written to. When the new frame is complete, the buffers are swapped. Triple buffering extends this concept to eliminate frame rate limitations during buffer swaps.

### Graphics Display Processor

The Graphics Display Processor (GDP) or Graphics Processing Unit (GPU) is a specialized processor designed to handle graphics operations efficiently. Unlike the central processing unit (CPU), which handles general-purpose computations, the GPU is optimized for parallel processing of graphics primitives.

The GPU typically implements a graphics pipeline that includes stages such as:

- **Vertex Processing:** Transforming 3D coordinates to 2D screen positions
- **Primitive Assembly:** Grouping vertices into geometric primitives (points, lines, triangles)
- **Rasterization:** Converting primitives into fragments (potential pixels)
- **Fragment Processing:** Applying colors, textures, and lighting to fragments
- **Pixel Operations:** Testing fragments against existing depth values, blending colors

Modern GPUs contain thousands of processing cores capable of executing shader programs, enabling programmable graphics pipelines and highly realistic rendering effects.

### Video Controller

The video controller manages the timing and data flow between the frame buffer and the display device. It generates the horizontal and vertical synchronization signals required to properly scan the image onto the screen. The controller operates independently of the CPU, continuously refreshing the display from the frame buffer.

Modern video controllers support various display modes and can handle different resolutions and refresh rates. They often include hardware acceleration for common graphics operations like line drawing, polygon filling, and bit block transfers (BITBLT), reducing the computational burden on the CPU.

### Input Devices for Graphics

Graphics systems require specialized input devices beyond standard keyboards:

**Mouse:** The most common 2D pointing device, translating hand movements into cursor movement on screen. Optical mice use LEDs and sensors to track movement across surfaces.

**Graphics Tablet (Digitizer):** Uses electromagnetic resonance technology to precisely track stylus position, commonly used for digital artwork and CAD applications.

**Touch Screens:** Detect touch input directly on the display surface, supporting gestures and multi-touch interaction.

**Trackballs and Joysticks:** Provide alternative pointing and navigation methods, particularly useful in specialized applications.

**3D Input Devices:** Space mice, data gloves, and motion controllers enable 3D navigation and manipulation in virtual environments.

### Random Scan (Vector) Display Systems

Unlike raster scan systems, vector displays draw lines directly by steering the electron beam between specified endpoints. They can produce smooth, high-resolution lines and were commonly used in early computer graphics and specialized applications like CAD. Vector displays excel at wireframe representations but cannot easily fill areas or render complex shaded surfaces. They have largely been replaced by raster systems in mainstream applications.

## Examples

### Example 1: Calculating Frame Buffer Size

**Problem:** Calculate the minimum VRAM required for a display with resolution 2560×1440 pixels and 32-bit color depth.

**Solution:**

Step 1: Understand the parameters

- Resolution: 2560 × 1440 pixels
- Color depth: 32 bits = 4 bytes per pixel

Step 2: Calculate total pixels
Total pixels = 2560 × 1440 = 3,686,400 pixels

Step 3: Calculate frame buffer size
Frame buffer size = 3,686,400 × 4 bytes = 14,745,600 bytes

Step 4: Convert to appropriate units
14,745,600 bytes ÷ 1,048,576 = 14.06 MB

**Answer:** Minimum VRAM required is approximately 14.06 MB. In practice, graphics cards would have more memory for double/triple buffering and texture storage.

### Example 2: Understanding Refresh Rate and Bandwidth

**Problem:** A display has a resolution of 1920×1080 at 60Hz refresh rate with 24-bit color. Calculate the minimum memory bandwidth required for the video controller to continuously read the frame buffer.

**Solution:**

Step 1: Calculate data per frame
Pixels per frame = 1920 × 1080 = 2,073,600 pixels
Bytes per frame = 2,073,600 × 3 bytes = 6,220,800 bytes (24-bit = 3 bytes)

Step 2: Calculate data per second
Data per second = 6,220,800 × 60 = 373,248,000 bytes/second

Step 3: Convert to appropriate units
373,248,000 ÷ 1,000,000 = 373.25 MB/s

**Answer:** Minimum bandwidth required is approximately 373.25 MB/s. Modern GPUs provide tens of GB/s bandwidth to handle not just frame buffer reads but also texture lookups and shader operations.

### Example 3: Double Buffering Operation

**Problem:** Explain how double buffering solves the screen flicker problem in raster displays.

**Solution:**

**Without Double Buffering:**

- The CPU writes directly to the single frame buffer
- While drawing, the video controller reads from the same buffer being modified
- This causes visible tearing and flicker as partially drawn frames are displayed

**With Double Buffering:**

- Two frame buffers are used: front buffer and back buffer
- The video controller continuously reads from the front buffer for display
- The CPU/GPU writes complete frames to the back buffer
- Once a complete frame is drawn, the buffers are swapped (typically during vertical blanking interval)
- The viewer sees only complete, fully rendered frames

**Example Timeline:**

- Time 0-16ms: Draw frame 1 to back buffer
- Time 16ms: Swap buffers (frame 1 now displayed)
- Time 16-32ms: Draw frame 2 to back buffer
- Time 32ms: Swap buffers (frame 2 now displayed)

This eliminates flicker because the display always shows a complete frame, never a partially drawn one.

## Exam Tips

1. **Remember the difference between raster and vector scan systems:** Raster scans line by line (like TV), while vector draws between endpoints. Raster is dominant in modern systems.

2. **Know the components of the graphics pipeline:** Understand the sequence from application → geometry processing → rasterization → fragment processing → display.

3. **Frame buffer calculations are common exam problems:** Practice calculating memory requirements for different resolutions and color depths. Remember: Resolution × Bytes per pixel = Frame buffer size.

4. **Understand why CRT displays flicker at low refresh rates:** The phosphor glow fades between refresh cycles. Modern displays use higher refresh rates (60Hz+) and hold the image until the next refresh.

5. **Double buffering is fundamental:** Be able to explain how it eliminates flicker and the role of vertical blanking interval in buffer swapping.

6. **Know the advantages of OLED over LCD:** Self-emitting pixels (true blacks), no backlight required, better contrast ratios, thinner panels, flexible displays.

7. **GPU vs CPU architecture:** GPUs are designed for parallel processing of many pixels/vertices simultaneously, while CPUs handle sequential general-purpose computations.

8. **Video controller functions:** Remember it generates timing signals, reads frame buffer continuously, and handles display synchronization independently of the CPU.

9. **Color depth and color representation:** 24-bit color provides 8 bits (256 levels) each for red, green, and blue, totaling 16.7 million colors.

10. **Input devices:** Know the common graphics input devices and their primary uses—mouse for general pointing, tablets for precision drawing, touch screens for direct interaction.
