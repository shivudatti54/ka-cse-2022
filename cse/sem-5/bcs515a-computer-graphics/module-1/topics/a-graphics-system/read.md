# Computer Graphics System

## Introduction

Computer Graphics is a fundamental branch of computer science that deals with the creation, manipulation, and representation of visual information using computers. It has revolutionized various fields including entertainment, engineering, scientific visualization, medical imaging, and user interface design. A computer graphics system comprises hardware and software components that work together to generate and display visual output on various output devices.

The importance of computer graphics cannot be overstated in today's digital world. From the graphical user interfaces (GUIs) we interact with daily to sophisticated computer-aided design (CAD) systems used in engineering, computer graphics plays a pivotal role. The evolution of graphics systems from simple line displays to today's photorealistic real-time rendering represents one of the most significant advancements in computing technology. Understanding the components of a graphics system is essential for any computer science student, as this knowledge forms the foundation for advanced topics in graphics programming, visualization, and multimedia applications.

This topic explores the fundamental components of a computer graphics system, including display technologies, input devices, hard copy devices, and graphics software. A thorough understanding of these components is crucial for designing efficient graphics applications and optimizing visual output for various purposes.

## Key Concepts

### 1. Video Display Devices

Video display devices are the primary output devices in a computer graphics system. They convert digital image data into visual information that users can perceive.

#### Cathode Ray Tube (CRT)

CRT is one of the oldest and most well-understood display technology. It works by exciting phosphors on a screen using electron beams. The key components of a CRT include:

- **Electron Gun**: Emits electron beams that are focused and directed towards the screen
- **Phosphor Screen**: Coated with phosphors that emit light when struck by electrons
- **Deflection System**: Controls the electron beam path to scan across the screen

CRT displays operate in two primary modes:

- **Random Scan (Vector Display)**: Draws lines by directing the beam to specific coordinates
- **Raster Scan**: Scans the entire screen row by row, similar to television systems

**Refresh Rate**: The number of times per second the screen is redrawn, typically 60-144 Hz for modern displays.

#### Liquid Crystal Display (LCD)

LCD technology uses liquid crystals sandwiched between two polarizers. Key characteristics include:

- **Backlight**: Provides illumination through the liquid crystal layer
- **Pixel Structure**: Each pixel consists of subpixels for red, green, and blue
- **Response Time**: Time taken for a pixel to change state (typically 1-8 ms)
- **Viewing Angle**: The angle at which display remains visible

#### Plasma Display Panel (PDP)

Plasma displays use tiny cells containing ionized gas (plasma) that emit ultraviolet light, which then causes phosphors to emit visible light. These displays offer:

- Wide viewing angles
- High contrast ratios
- Better color reproduction
- Larger screen sizes (typically 42 inches and above)

#### Light Emitting Diode (LED) Display

LED displays use an array of LEDs as pixels. They offer:

- High brightness and contrast
- Energy efficiency
- Long lifespan
- Flexible form factors

### 2. Input Devices

Input devices enable users to interact with graphics systems and provide data for visual representation.

#### Keyboard

- Alphanumeric input for text and commands
- Function keys for predefined operations
- Arrow keys for cursor movement

#### Mouse

- **Pointing Device**: Controls cursor position on screen
- **Click Operations**: Single click, double click, right click, drag operations
- **Types**: Mechanical (ball-based), Optical, Laser, Wireless

#### Trackball

- Inverted mouse design
- Ball rotated by palm or fingers
- Common in CAD and specialized applications

#### Joystick

- Used in gaming and simulation
- Provides directional control
- Can include buttons for additional input

#### Light Pen

- Photoelectric device detects screen content
- Used for direct screen pointing
- Limited in modern applications

#### Graphics Tablet (Digitizer)

- Uses electromagnetic resonance technology
- Provides precise coordinate input
- Used in CAD, graphic design, and handwriting recognition
- Typical accuracy: 0.01-0.05 mm

#### Touch Screen

- Direct finger or stylus input
- Types: Resistive, Capacitive, Infrared, Surface Acoustic Wave
- Widely used in mobile devices and kiosks

#### 3D Input Devices

- **Spaceball**: Provides six degrees of freedom input
- **Data Glove**: Tracks hand and finger movements
- **Motion Capture Systems**: Records human movement for animation

### 3. Hard Copy Devices

Hard copy devices produce permanent visual records of graphics output.

#### Printer Technologies

**Impact Printers**

- Dot Matrix: Uses pins striking ribbon against paper
- Character-based output
- Low cost, used for basic graphics

**Non-Impact Printers**

- **Inkjet**: Sprays tiny ink droplets onto paper
- Resolution: 300-2400 DPI
- Color capability through CMYK cartridges
- Types: Thermal, Piezoelectric, Continuous Inkjet
- **Laser**: Uses toner and electrostatic charges
- Resolution: 300-1200 DPI
- Fast printing speed
- High quality text and graphics
- Electrostatic Photographic (EP) process
- **Thermal Wax Transfer**: Uses wax-based ribbons
- High color saturation
- Used in specialized applications

**Plotter**

- Vector output device for large-format printing
- Types: Pen plotter, Electrostatic plotter, Inkjet plotter
- Used in CAD, architectural drawings, GIS applications
- Resolution: 300-2400 DPI
- Paper sizes: A0, A1, A2, and larger

#### Screen Capture

- Software-based hard copy
- Saves current screen as image file
- Formats: PNG, JPEG, BMP, TIFF

### 4. Graphics Software

Graphics software provides the interface between applications and hardware.

#### System Software

**Graphics Device Interface (GDI)**

- Windows-based graphics subsystem
- Device-independent drawing
- Manages device contexts

**OpenGL**

- Cross-platform graphics API
- Hardware-accelerated rendering
- Standard for 3D graphics

**DirectX**

- Microsoft's multimedia API
- Direct3D for 3D graphics
- DirectDraw for 2D graphics

#### Application Software

**Paint Programs**

- Bitmap-based editing
- Examples: Paint, Photoshop, GIMP
- Operations: Drawing, painting, image manipulation

**Illustration Programs**

- Vector-based graphics
- Examples: Adobe Illustrator, CorelDRAW
- Operations: Drawing, typography, layout

**3D Modeling Software**

- Creates 3D objects and scenes
- Examples: 3DS Max, Maya, Blender
- Capabilities: Modeling, texturing, animation

**CAD Software**

- Computer-Aided Design
- Examples: AutoCAD, SolidWorks
- Technical and engineering drawings

#### Graphics Standards

**GKS (Graphical Kernel System)**

- ISO standard (ISO 7942)
- 2D graphics standard
- Device-independent graphics

**PHIGS (Programmer's Hierarchical Interactive Graphics System)**

- 3D graphics capability
- Hierarchical object structure
- More complex than GKS

**CGI (Computer Graphics Interface)**

- Device-level interface standard
- Connects graphics systems with devices

## Examples

### Example 1: Understanding CRT Refresh Rate

**Problem**: A CRT monitor has a resolution of 1024 × 768 pixels and operates at a refresh rate of 60 Hz. Calculate the time available for drawing each scan line.

**Solution**:

**Step 1**: Understand the parameters

- Resolution: 1024 × 768 means 768 horizontal scan lines
- Refresh rate: 60 Hz means 60 frames per second
- Each frame consists of 768 scan lines

**Step 2**: Calculate time per frame

- Time per frame = 1/60 seconds = 0.0167 seconds = 16.7 ms

**Step 3**: Calculate time per scan line

- Time per scan line = 16.7 ms / 768 = 0.0217 ms = 21.7 μs

**Answer**: Approximately 21.7 microseconds are available for drawing each scan line.

### Example 2: LCD Pixel Configuration

**Problem**: An LCD display has a resolution of 1920 × 1080 (Full HD) and uses 8-bit color depth per color channel. Calculate the total memory required to store one frame.

**Solution**:

**Step 1**: Identify the parameters

- Horizontal resolution: 1920 pixels
- Vertical resolution: 1080 pixels
- Color depth: 8 bits per channel (RGB = 3 channels)
- Total bits per pixel: 8 × 3 = 24 bits

**Step 2**: Calculate total pixels

- Total pixels = 1920 × 1080 = 2,073,600 pixels

**Step 3**: Calculate memory requirement

- Total bits = 2,073,600 × 24 = 49,766,400 bits
- Convert to bytes: 49,766,400 / 8 = 6,220,800 bytes
- Convert to megabytes: 6,220,800 / 1,048,576 ≈ 5.93 MB

**Answer**: Approximately 5.93 MB of memory is required to store one frame.

### Example 3: Inkjet Printer Resolution

**Problem**: An inkjet printer has a resolution of 600 × 600 DPI (dots per inch). Calculate how many dots can be printed on a 4 × 6 inch photo paper.

**Solution**:

**Step 1**: Understand DPI

- DPI means dots per linear inch
- Horizontal DPI: 600 dots per inch
- Vertical DPI: 600 dots per inch

**Step 2**: Calculate total dots

- Total dots horizontally = 600 × 4 = 2,400 dots
- Total dots vertically = 600 × 6 = 3,600 dots

**Step 3**: Calculate total dots on paper

- Total dots = 2,400 × 3,600 = 8,640,000 dots

**Answer**: The printer can place approximately 8.64 million dots on a 4 × 6 inch photo paper.

## Exam Tips

1. **CRT vs LCD**: Remember that CRT uses electron beams and phosphors while LCD uses liquid crystals with backlighting. CRT has better color accuracy but larger size; LCD is thinner and more energy-efficient.

2. **Refresh Rate Importance**: Higher refresh rates reduce screen flicker and eye strain. Know that minimum 60 Hz is required for comfortable viewing.

3. **Pixel vs Dot**: In printing, DPI (dots per inch) refers to printer capability, while PPI (pixels per inch) refers to image resolution. They are not always equal.

4. **Color Depth**: 8-bit color means 256 colors, 24-bit color means approximately 16.7 million colors (2^8 × 2^8 × 2^8).

5. **Graphics Standards**: GKS is for 2D graphics, PHIGS is for 3D graphics with hierarchical structures. Know their basic purposes.

6. **Hard Copy vs Soft Copy**: Soft copy refers to screen display (temporary), while hard copy refers to printed output (permanent).

7. **Input Device Selection**: For precision work (CAD), use digitizing tablets; for general pointing, use mouse; for 3D modeling, use spaceballs or data gloves.

8. **Display Technologies**: LED displays are essentially LCDs with LED backlights, making them more energy-efficient than traditional CCFL-backlit LCDs.

9. **Plotter Types**: Pen plotters are vector-based, while inkjet plotters are raster-based. Choose based on output requirements.

10. **Graphics APIs**: OpenGL is cross-platform, DirectX is Windows-specific. Know their primary use cases in graphics programming.
