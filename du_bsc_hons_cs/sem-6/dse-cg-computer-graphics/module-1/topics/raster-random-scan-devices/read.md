# Raster Random Scan Devices

## Comprehensive Study Material for DSE CG - Computer Graphics

---

## 📚 Learning Objectives

By the end of this chapter, you will be able to:

1. **Understand** the fundamental working principles of raster scan and random scan display devices
2. **Differentiate** between raster scan and random scan graphics systems
3. **Explain** the architecture and components of cathode ray tube (CRT) based display systems
4. **Analyze** modern display technologies and their relationship to raster principles
5. **Evaluate** the advantages and limitations of different scan methodologies
6. **Apply** knowledge of refresh rates and frame buffers in graphics programming
7. **Design** simple graphics applications using raster scan principles

---

## 1. Introduction and Real-World Relevance

### 1.1 What are Display Devices in Computer Graphics?

Display devices are the primary output hardware in computer graphics systems that render visual information from computational data. In the context of the Delhi University BSc (Hons) Computer Science syllabus (DSE CG - Computer Graphics), understanding display devices forms the foundation for comprehending how computers translate mathematical representations of objects into visible images on screens.

### 1.2 Real-World Relevance

Every digital image you see on a computer monitor, smartphone, or television relies on the fundamental principles of raster scanning. Consider these practical applications:

- **Medical Imaging**: MRI and CT scan displays use high-resolution raster systems
- **Gaming Industry**: Modern video games depend entirely on raster rendering pipelines
- **Digital Television**: All modern TVs use raster scan principles
- **Scientific Visualization**: Weather patterns, molecular structures, and simulation results are displayed using raster graphics
- **User Interfaces**: Every GUI application you've ever used employs raster techniques

The distinction between raster scan and random scan devices is not merely historical—understanding these fundamentals is essential for grasping modern GPU architectures, display technologies, and graphics programming concepts.

---

## 2. Overview of Display Technologies

### 2.1 Classification of Display Devices

Display devices in computer graphics can be broadly classified into:

```
Display Devices
├── Refresh Display Devices
│   ├── Cathode Ray Tube (CRT)
│   │   ├── Raster Scan CRT
│   │   └── Random Scan (Vector) CRT
│   ├── Liquid Crystal Display (LCD)
│   ├── Light Emitting Diode (LED) Display
│   ├── Organic LED (OLED)
│   └── Plasma Display Panels (PDP)
└── Hard Copy Devices
    ├── Plotters
    └── Printers
```

### 2.2 Historical Context

The evolution of display technology provides crucial context for understanding current systems:

1. **1950s**: First CRT-based vector displays (random scan)
2. **1970s**: Raster scan CRTs became dominant for television and computer monitors
3. **1990s**: Introduction of flat-panel displays (LCD, plasma)
4. **2010s onwards**: LED and OLED technologies revolutionized display quality
5. **Present**: Micro-LED and advanced HDR displays represent the cutting edge

---

## 3. Raster Scan Devices - Working Principle

### 3.1 Fundamental Concept

In a **raster scan system**, the electron beam scans the entire screen in a systematic pattern, typically from top-left to bottom-right, one row at a time. This creates a grid of picture elements (pixels) that can be individually addressed and illuminated.

### 3.2 How Raster Scan Works

The complete working principle involves several sequential steps:

#### Step 1: Frame Buffer Initialization
- A dedicated memory area called the **frame buffer** (or refresh buffer) stores the complete image
- Each pixel's color/intensity is represented by bits in this memory
- For a display resolution of 1920×1080 with 24-bit color, the frame buffer requires approximately 6.2 MB per frame

#### Step 2: Electron Beam Deflection
The electron gun generates a focused beam that:
- Horizontally scans from left to right (trace)
- Vertically moves down after each horizontal line (retrace)
- Returns to the top-left corner after completing one frame (vertical retrace)

#### Step 3: Intensity Modulation
- The beam's intensity is modulated based on the pixel values stored in the frame buffer
- High intensity creates bright pixels; low intensity creates darker areas
- Color displays use three electron guns (RGB) or a shadow mask with phosphors

#### Step 4: Continuous Refresh
- The entire screen is redrawn multiple times per second (typically 60-144 Hz)
- This rapid refresh creates the illusion of continuous display due to **persistence of vision**

### 3.3 Scan Pattern Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│ START → ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━→ │
│        │                                                        │ │
│        │  Horizontal Scan Lines (1, 2, 3, ... n)                │ │
│        │                                                        │ │
│        ▼                                                        │ │
│        ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━→ │
│        │                                                        │ │
│        ▼                                                        │ │
│        ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━→ │
│        │                                                        │ │
│        ▼                                                        │ │
│        ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━→ │
│                              ...                                   │
│        ▼                                                        │ │
│        ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━→ │
│                           END FRAME                               ▼
└─────────────────────────────────────────────────────────────────────┘
         ←──────────────── Horizontal Trace ───────────────→
              ↓
         Vertical Retrace
```

### 3.4 Key Components of a Raster Scan CRT

| Component | Function |
|-----------|----------|
| **Electron Gun** | Emits and focuses electron beam |
| **Phosphor Screen** | Emits light when struck by electrons |
| **Shadow Mask** | Controls beam landing for color accuracy |
| **Deflection Coils** | Electromagnetically steer the beam |
| **Video Amplifier** | Amplifies signal for intensity control |
| **Frame Buffer** | Stores pixel data for display |

---

## 4. Random Scan Devices (Vector Display)

### 4.1 Working Principle

In a **random scan system** (also known as vector display), the electron beam moves directly to specific points on the screen to draw lines and curves. Unlike raster scan, the beam only traces the paths necessary to display the image, not the entire screen area.

### 4.2 Characteristics

- **Line-drawing capability**: Directs beam from one point to another
- **No fixed resolution**: Lines can be drawn at any angle with equal clarity
- **Smooth curves**: Uses mathematical function generators (e.g., circle generators)
- **Limited color**: Typically single color or limited palette
- **No frame buffer**: Stores display list of line drawing commands

### 4.3 Display List Architecture

```
Display List (Example):
─────────────────────
MOVE TO (100, 100)
LINE TO (400, 100)
LINE TO (400, 300)
LINE TO (100, 300)
LINE TO (100, 100)
MOVE TO (150, 150)
LINE TO (350, 250)
MOVE TO (350, 150)
LINE TO (150, 250)
END
```

---

## 5. Comparison: Raster Scan vs Random Scan

### 5.1 Comprehensive Comparison Table

| Aspect | Raster Scan | Random Scan (Vector) |
|--------|-------------|---------------------|
| **Scan Pattern** | Systematic row-by-row | Direct point-to-point |
| **Frame Buffer** | Required (stores all pixels) | Not required (stores commands) |
| **Resolution** | Fixed (pixel grid) | Variable (continuous) |
| **Image Quality** | Pixelated at low resolution | Smooth lines at any resolution |
| **Color Capability** | Millions of colors (24-bit+) | Limited colors |
| **Fill Area** | Easy (solid fill) | Difficult (requires hatching) |
| **Refresh Rate** | Fixed (typically 60-144 Hz) | Variable (depends on complexity) |
| **Memory Requirement** | High (per-pixel storage) | Low (command storage) |
| **Applications** | TV, monitors, games | CAD systems, oscilloscopes |
| **Historical Era** | 1970s-present | 1950s-1980s |

### 5.2 When to Use Each Technology

**Use Raster Scan when:**
- Displaying photographic images or complex scenes
- Real-time animation is required
- Color depth and shading are important
- Working with standard video formats

**Use Random Scan when:**
- Precise line drawing is required (technical drawings)
- Resolution-independent display is needed
- Simple geometric shapes dominate the image
- Displaying waveforms or oscilloscope data

---

## 6. Modern Display Technologies

### 6.1 Evolution from CRT to Modern Displays

While the basic principle of raster scanning remains fundamental, modern displays have evolved significantly:

#### Liquid Crystal Display (LCD)
- Uses liquid crystal molecules that modulate light
- Requires backlight (CCFL or LED)
- Active matrix (TFT) or passive matrix construction
- **Raster principle**: Still scans rows and columns of pixels

#### Light Emitting Diode (LED) Display
- Uses LED backlights for improved brightness and contrast
- Can be edge-lit or direct-lit
- Energy efficient compared to CCFL LCD

#### Organic LED (OLED)
- Each pixel emits its own light
- True black (no backlight needed)
- Superior contrast ratios and color accuracy
- Flexible and foldable form factors possible

#### Quantum Dot Display
- Uses quantum dots for enhanced color accuracy
- Found in high-end TVs and monitors

### 6.2 Resolution Standards

| Standard | Resolution | Aspect Ratio | Common Use |
|----------|------------|--------------|------------|
| HD | 1280×720 | 16:9 | Entry-level displays |
| Full HD | 1920×1080 | 16:9 | Standard monitors |
| 2K/QHD | 2560×1440 | 16:9 | Gaming monitors |
| 4K/UHD | 3840×2160 | 16:9 | Premium displays |
| 8K UHD | 7680×4320 | 16:9 | Professional/future |

---

## 7. Refresh Rate and Frame Rate Details

### 7.1 Understanding Refresh Rate

**Refresh Rate** (measured in Hertz, Hz) refers to how many times per second the display hardware updates the entire screen. Common refresh rates include:

- **60 Hz**: Standard refresh (60 times per second)
- **75 Hz**: Slightly smoother than 60 Hz
- **120 Hz**: Common in gaming displays
- **144 Hz**: High-performance gaming
- **240 Hz**: Competitive gaming/ESports
- **360 Hz**: Cutting-edge gaming displays

### 7.2 Frame Rate vs Refresh Rate

| Term | Definition | Unit |
|------|------------|------|
| **Frame Rate** | Number of frames rendered by GPU per second | FPS (frames per second) |
| **Refresh Rate** | Number of times display updates per second | Hz |
| **Response Time** | Time for pixel to change color | milliseconds (ms) |

### 7.3 Important Relationships

1. **Ideal Scenario**: Frame rate matches refresh rate (e.g., 60 FPS at 60 Hz)
2. **Frame Rate > Refresh Rate**: Causes screen tearing
3. **Frame Rate < Refresh Rate**: Causes stuttering
4. **VSync**: Synchronizes frame rate with refresh rate to prevent tearing

### 7.4 Persistence of Vision

The human eye integrates light over approximately 1/30th of a second. This phenomenon, combined with phosphor persistence in CRTs or pixel hold time in modern displays, creates the illusion of continuous imagery. Understanding this is crucial for:

- Determining minimum refresh rates (typically 30-60 Hz)
- Designing animations that appear smooth
- Understanding motion blur and ghosting artifacts

---

## 8. Real-World Examples

### Example 1: Television Broadcast System

The standard television broadcast system provides a classic example of raster scanning:

**Technical Specifications:**
- **Resolution**: 1920×1080 pixels (Full HD)
- **Refresh Rate**: 60 Hz (interlaced) or progressive
- **Aspect Ratio**: 16:9
- **Color Space**: Rec. 709

**Working Process:**
1. Camera captures scene and converts to electronic signals
2. Signals are encoded and transmitted
3. Receiver decodes and stores frame in video memory
4. Display scans through frame buffer row by row
5. Each pixel is illuminated based on stored values
6. Process repeats 60 times per second

### Example 2: Computer Monitor in Office Application

Consider a typical office workflow:

**Scenario**: User types a document in Microsoft Word

**Raster Scan Process:**
1. Application renders text as vector shapes
2. Shapes are rasterized into pixel data
3. Pixel data stored in frame buffer (resolution: 1920×1080)
4. Monitor scans frame buffer:
   - Horizontal scan: 1080 lines
   - Each line: 1920 pixels
   - Total pixels processed: ~2 million per frame
5. At 60 Hz, approximately 124 million pixels processed per second
6. User perceives smooth, flicker-free text

---

## 9. Code Examples

### Example 1: Simple Raster Line Drawing (Python-like Pseudocode)

```python
class RasterDisplay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Frame buffer: 2D array representing screen
        self.frame_buffer = [[(0, 0, 0) for _ in range(width)] 
                             for _ in range(height)]
    
    def set_pixel(self, x, y, color):
        """Set a single pixel in the frame buffer"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.frame_buffer[y][x] = color
    
    def draw_line_dda(self, x1, y1, x2, y2, color):
        """
        Digital Differential Analyzer (DDA) algorithm
        for raster line drawing
        """
        dx = x2 - x1
        dy = y2 - y1
        
        # Determine number of steps
        steps = max(abs(dx), abs(dy))
        
        # Calculate increments
        x_increment = dx / steps
        y_increment = dy / steps
        
        # Starting point
        x = x1
        y = y1
        
        # Draw each point
        for _ in range(int(steps) + 1):
            self.set_pixel(int(x), int(y), color)
            x += x_increment
            y += y_increment
    
    def refresh(self):
        """Simulate screen refresh - scan frame buffer"""
        print(f"Refreshing {self.width}x{self.height} display...")
        for row in self.frame_buffer:
            # In real hardware, this would send signals to display
            pass

# Usage Example
display = RasterDisplay(800, 600)
display.draw_line_dda(100, 100, 700, 500, (255, 255, 255))
display.refresh()
```

### Example 2: Understanding Frame Buffer Operations (C-style)

```c
#include <stdio.h>
#include <stdlib.h>

// Define display parameters
#define WIDTH  1920
#define HEIGHT 1080
#define BYTES_PER_PIXEL 3  // RGB

// Frame buffer structure
typedef struct {
    unsigned char *data;
    int width;
    int height;
} FrameBuffer;

// Initialize frame buffer
FrameBuffer* create_frame_buffer(int width, int height) {
    FrameBuffer *fb = malloc(sizeof(FrameBuffer));
    fb->width = width;
    fb->height = height;
    fb->data = calloc(width * height * BYTES_PER_PIXEL, 
                      sizeof(unsigned char));
    return fb;
}

// Set pixel color at (x, y)
void set_pixel(FrameBuffer *fb, int x, int y, 
               unsigned char r, unsigned char g, unsigned char b) {
    if (x < 0 || x >= fb->width || y < 0 || y >= fb->height) {
        return;  // Out of bounds
    }
    
    int index = (y * fb->width + x) * BYTES_PER_PIXEL;
    fb->data[index] = r;     // Red
    fb->data[index + 1] = g; // Green
    fb->data[index + 2] = b; // Blue
}

// Simulate raster scan refresh
void refresh_display(FrameBuffer *fb) {
    printf("Performing raster scan refresh at %d Hz\n", 60);
    printf("Total pixels to process: %d\n", fb->width * fb->height);
    printf("Data transfer rate: %.2f MB/s\n", 
           (fb->width * fb->height * BYTES_PER_PIXEL * 60.0) / (1024 * 1024));
}

int main() {
    FrameBuffer *fb = create_frame_buffer(WIDTH, HEIGHT);
    
    // Draw a white pixel at center
    set_pixel(fb, WIDTH/2, HEIGHT/2, 255, 255, 255);
    
    // Simulate refresh
    refresh_display(fb);
    
    free(fb->data);
    free(fb);
    
    return 0;
}
```

---

## 10. Advantages and Disadvantages

### 10.1 Raster Scan Advantages

✅ **Versatile**: Can display any type of image (photographs, text, graphics)
✅ **Color depth**: Supports millions of colors (8-bit, 16-bit, 24-bit, 32-bit)
✅ **Fill capability**: Solid fills and patterns are straightforward
✅ **Standard format**: Compatible with broadcast standards
✅ **Cost-effective**: Mature technology with established manufacturing processes

### 10.2 Raster Scan Disadvantages

❌ **Fixed resolution**: Image quality degrades when not at native resolution
❌ **Aliasing**: Diagonal lines appear jagged (rasterization artifacts)
❌ **Memory intensive**: Requires large frame buffer for high resolution
❌ **Bandwidth**: High data rates needed for high-resolution, high-refresh displays

### 10.3 Random Scan Advantages

✅ **Resolution independent**: Lines are smooth at any size
✅ **Precise drawing**: Ideal for technical and engineering applications
✅ **Lower memory**: Stores drawing commands, not pixel data
✅ **Natural line representation**: Mathematical curves render perfectly

### 10.4 Random Scan Disadvantages

❌ **Limited to line graphics**: Cannot handle complex scenes or photographs
❌ **Flicker at high complexity**: More lines = slower refresh
❌ **No solid fills**: Difficult to fill enclosed areas
❌ **Obsolete technology**: Replaced by raster systems for most applications

---

## 11. Multiple Choice Questions

### Level 1: Recall Questions

**Question 1:** In a raster scan display, the electron beam scans the screen:
- (a) Randomly to any point
- (b) Row by row, from top to bottom
- (c) Only on diagonal paths
- (d) From center to edges

**Answer:** (b) Row by row, from top to bottom

---

**Question 2:** Which component stores pixel data in a raster scan system?
- (a) Display list
- (b) Vector generator
- (c) Frame buffer
- (d) Deflection coil

**Answer:** (c) Frame buffer

---

**Question 3:** The process of returning the electron beam from right end to left end of the next line is called:
- (a) Vertical retrace
- (b) Horizontal retrace
- (c) Frame refresh
- (d) Pixel scanning

**Answer:** (b) Horizontal retrace

---

### Level 2: Understanding Concepts

**Question 4:** A display has a resolution of 1920×1080 and uses 24-bit color. How much memory is required to store ONE frame in the frame buffer?
- (a) 1920 × 1080 bits
- (b) 1920 × 1080 × 3 bytes
- (c) 1920 × 1080 × 24 bits
- (d) 1920 × 1080 × 3 bits

**Answer:** (b) 1920 × 1080 × 3 bytes (approximately 6.2 MB)

---

**Question 5:** Which scan system requires higher bandwidth for the same screen area?
- (a) Random scan with fewer lines
- (b) Raster scan with higher resolution
- (c) Both require equal bandwidth
- (d) Random scan always requires less

**Answer:** (b) Raster scan with higher resolution

---

**Question 6:** The phenomenon that allows our eyes to perceive a rapidly refreshed display as continuous is called:
- (a) Pixel persistence
- (b) Persistence of vision
- (c) Phosphor decay
- (d) Scan integration

**Answer:** (b) Persistence of vision

---

### Level 3: Application-Based Questions

**Question 7:** A gaming monitor operates at 144 Hz refresh rate. How many times per second does the display hardware update the screen?
- (a) 60 times
- (b) 144 times
- (c) 240 times
- (d) 360 times

**Answer:** (b) 144 times

---

**Question 8:** If a raster scan system displays 60 frames per second at 1920×1080 resolution with 24-bit color, what is the required memory bandwidth (in MB/s)?
- (a) ~124 MB/s
- (b) ~373 MB/s
- (c) ~1.49 GB/s
- (d) ~6.22 GB/s

**Answer:** (b) ~373 MB/s (1920 × 1080 × 3 bytes × 60 = 373 MB/s)

---

**Question 9:** Which display technology would be MOST appropriate for a computer-aided design (CAD) application requiring precise line rendering at multiple zoom levels?
- (a) Standard LCD monitor
- (b) Random scan vector display
- (c) High-resolution raster display with anti-aliasing
- (d) Plasma display

**Answer:** (c) High-resolution raster display with anti-aliasing (modern CAD uses high-res raster with software enhancements)

---

**Question 10:** Screen tearing in displays occurs when:
- (a) Refresh rate is too low
- (b) Frame rate exceeds refresh rate without synchronization
- (c) The frame buffer is too small
- (d) Horizontal retrace fails

**Answer:** (b) Frame rate exceeds refresh rate without synchronization

---

### Level 4: Analytical Questions

**Question 11:** Analyze why vector (random scan) displays were preferred for early CAD applications but have been completely replaced by raster displays in modern systems.

**Answer:** Random scan displays offered resolution-independent line drawing, which was crucial for technical drawings at varying zoom levels. However, modern CAD applications now use high-resolution raster displays (4K+) with advanced anti-aliasing algorithms that simulate smooth lines. The transition occurred because raster displays can handle complex 3D models, textures, shading, and photorealistic rendering—all impossible with vector displays. Additionally, the gaming industry drove mass production of high-resolution raster displays, making them cost-effective.

---

**Question 12:** Calculate the difference in frame buffer size (in MB) between a 4K display (3840×2160) and a Full HD display (1920×1080), both using 32-bit color (4 bytes per pixel).

**Answer:**
- Full HD: 1920 × 1080 × 4 = 8,294,400 bytes ≈ 7.91 MB
- 4K: 3840 × 2160 × 4 = 33,177,600 bytes ≈ 31.64 MB
- Difference: 31.64 - 7.91 = 23.73 MB

---

**Question 13:** A manufacturer claims their display has a "1ms response time" and "144Hz refresh rate." Explain what each specification means and why both are important for gaming applications.

**Answer:**
- **1ms response time**: The time taken for a pixel to change from one color to another (typically gray-to-gray). Lower is better as it reduces motion blur and ghosting.
- **144Hz refresh rate**: The display updates 144 times per second. Combined with high frame rate from GPU, this provides smoother motion.
- **Importance for gaming**: Both specifications work together. High refresh rate without low response time causes blur; low response time without high refresh rate feels choppy. Competitive gamers typically require both for optimal performance.

---

## 12. Chapter Summary

This chapter covered the fundamental concepts of display devices in computer graphics, with specific focus on raster scan and random scan systems:

1. **Raster Scan Systems**: The electron beam scans the entire screen row-by-row, storing complete image data in a frame buffer. This method dominates modern display technology.

2. **Random Scan Systems**: The electron beam moves directly to specific points, drawing only the required lines. Once common in CAD applications but now largely historical.

3. **Key Components**: Understanding electron guns, phosphor screens, shadow masks, deflection coils, and frame buffers provides insight into how displays function.

4. **Modern Evolution**: While the fundamental raster principle remains, LCD, LED, and OLED technologies have replaced CRT-based systems in most applications.

5. **Performance Metrics**: Refresh rates, frame rates, and response times are crucial specifications for evaluating display performance, especially in gaming and professional applications.

6. **Practical Applications**: From television broadcasts to computer monitors, raster scanning enables the visual computing experience we rely on daily.

---

## 13. Key Takeaways

✅ **Raster scan** is the dominant display technology where the beam systematically scans row-by-row

✅ **Frame buffer** is essential in raster systems—stores complete pixel data for every frame

✅ **Refresh rate** (Hz) determines how often the display updates; higher rates provide smoother visuals

✅ **Random scan** (vector) displays were ideal for CAD but have been replaced by high-resolution raster systems

✅ **Persistence of vision** allows us to perceive rapidly refreshed images as continuous

✅ **Modern displays** (LCD, LED, OLED) still operate on raster principles—the scanning methodology has evolved, not the fundamental approach

✅ **Memory bandwidth** requirements for frame buffers increase with resolution, color depth, and refresh rate

✅ **Anti-aliasing** techniques in modern graphics address the jagged line problem inherent to rasterization

---

## References for Further Study

1. **Textbook**: Computer Graphics, Donald Hearn and M. Pauline Baker (Pearson Education)
2. **Delhi University Syllabus**: DSE CG - Computer Graphics, NEP 2024 UGCF
3. **Online Resources**: National Programme on Technology Enhanced Learning (NPTEL) lectures on Computer Graphics

---

*This study material is specifically designed for BSc (Hons) Computer Science students at Delhi University, aligned with the NEP 2024 UGCF curriculum for the DSE CG - Computer Graphics course.*