# Input Output Devices
## Comprehensive Study Material for BSc (Hons) Computer Science - Delhi University (NEP 2024 UGCF)
### Subject: DSE CG - Computer Graphics

---

## 1. Introduction

**Input Output (I/O) devices** form the critical bridge between humans and computer systems, enabling the seamless exchange of information. In the context of **Computer Graphics**, these devices play an especially vital role as they determine how visual data is captured, processed, and displayed to users.

Computer Graphics deals with the creation, manipulation, and rendering of visual content using computers. The effectiveness of any graphical application—from simple 2D drawings to complex 3D simulations—depends heavily on the quality and capabilities of the input and output devices used. Whether you're a graphic designer using a tablet to create digital art, a gamer experiencing immersive virtual reality, or an engineer viewing a CAD model on a high-resolution monitor, I/O devices make it possible.

For students at Delhi University studying under the NEP 2024 UGCF framework, understanding I/O devices is essential not only for theoretical examinations but also for practical applications in fields like game development, animation, scientific visualization, and user interface design.

---

## 2. Input Devices in Computer Graphics

Input devices allow users to provide data, commands, and spatial information to the computer. In computer graphics, the ability to capture precise spatial coordinates and convert them into digital form is fundamental.

### 2.1 Pointing Devices

#### 2.1.1 Mouse

The **mouse** is the most common pointing device used in computer graphics applications. It translates hand movements into cursor movements on the screen.

**Types:**
- **Mechanical Mouse**: Uses a rolling ball to detect movement
- **Optical Mouse**: Uses LED and sensor for movement detection (more precise)
- **Laser Mouse**: Uses laser for higher precision (DPI up to 16,000+)
- **Wireless Mouse**: Connects via Bluetooth or RF

**Technical Specifications:**
- **DPI (Dots Per Inch)**: Measures sensitivity. Gaming mice offer 800-16,000+ DPI
- **Polling Rate**: Measured in Hz (125Hz-8000Hz), determines how often the mouse reports position
- **Acceleration**: Measured in g, tracks rapid movements

```c
// Example: Simple mouse event handling in C (pseudo-code for graphics context)
#include <graphics.h>

void handleMouseInput() {
    // Initialize mouse
    initmouse();
    
    // Get mouse position
    int x, y, button;
    
    while (!kbhit()) {
        getmousepos(&x, &y, &button);
        
        if (button == LEFT_BUTTON) {
            // Draw point at clicked location
            putpixel(x, y, GREEN);
        }
        if (button == RIGHT_BUTTON) {
            // Clear screen region
            setcolor(BLACK);
            circle(x, y, 20);
            floodfill(x, y, BLACK);
        }
        delay(10);
    }
}
```

#### 2.1.2 Trackball

A **trackball** works like an inverted mouse where the ball is exposed on top. The user rotates the ball with fingers or palm to move the cursor. It offers high precision and is commonly used in CAD applications and robotics control.

**Advantages:**
- Precise control for graphic design
- Requires less desk space
- Reduced hand fatigue for extended use

#### 2.1.3 Light Pen

A **light pen** is a pointing device that uses a photocell to detect light from the screen. It can directly point to positions on the CRT display.

**Technical Details:**
- Response time: < 1ms
- Tip diameter: 1-3mm for precision
- Used in: CAD, medical imaging, interactive kiosks

```python
# Example: Light pen coordinate detection concept (Python pseudo-code)
class LightPen:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        self.photocell_threshold = 0.5  # Light sensitivity
    
    def detect_position(self, light_intensity):
        """Convert light intensity to screen coordinates"""
        if light_intensity > self.photocell_threshold:
            # In real implementation, this would read from hardware
            x_coord = self.read_x_position()
            y_coord = self.read_y_position()
            return (x_coord, y_coord)
        return None
    
    def draw_at_point(self, position, color):
        """Draw at detected light pen position"""
        if position:
            self.display_driver.draw_pixel(position[0], position[1], color)
```

#### 2.1.4 Joystick

Used primarily for gaming and flight simulation, a **joystick** provides directional input through handle movement. It captures X and Y coordinates along with button states.

**Applications in Computer Graphics:**
- Gaming and interactive simulations
- 3D navigation in virtual environments
- Robotic control interfaces

### 2.2 Digitizing Devices

#### 2.2.1 Graphics Tablet (Digitizer)

A **graphics tablet** uses a stylus or puck to capture precise X-Y coordinates. It converts hand-drawn images into digital form—essential for digital artwork and CAD.

**Technical Specifications:**
- Resolution: 2540-5080 LPI (Lines Per Inch)
- Accuracy: ±0.25mm to ±0.01mm
- Active Area: 4x5" to 12x12" or larger
- Pressure Sensitivity: 256-8192 levels

**Types:**
- **Passive Tablet**: Uses electromagnetic induction
- **Active Tablet**: Stylus has battery for better signal
- **Optical Tablet**: Uses optical sensors

#### 2.2.2 Touchscreen

A **touchscreen** allows direct interaction by touching the display surface. It has become ubiquitous in modern devices.

**Technologies:**
- **Resistive**: Two layers that touch when pressed
- **Capacitive**: Uses electrical properties of human body
- **Infrared**: Uses light beams interrupted by touch
- **SAW (Surface Acoustic Wave)**: Uses ultrasonic waves

**Technical Details:**
- Touch points: Single, Multi-touch (2-10+)
- Response time: <10ms
- Accuracy: ±1mm typical
- Durability: 50 million+ touches

### 2.3 Scanning Devices

#### 2.3.1 Image Scanner

Scanners convert physical documents and images into digital format for computer graphics processing.

**Types:**
- **Flatbed Scanner**: Document placed on glass surface
- **Sheet-fed Scanner**: Automatic document feeding
- **Handheld Scanner**: Manual sweeping motion
- **Drum Scanner**: High-quality cylindrical scanning

**Technical Specifications:**
- Resolution: 300-9600 DPI
- Color Depth: 24-bit to 48-bit
- Scan Area: A4, A3, A2, or larger
- Bit Depth: Determines color accuracy

#### 2.3.2 3D Scanner

3D scanners capture the three-dimensional shape of objects for use in computer graphics, animation, and reverse engineering.

**Technologies:**
- **Laser Triangulation**: Measures displacement of reflected laser
- **Structured Light**: Projects patterns and measures deformation
- **Photogrammetry**: Uses multiple photographs to reconstruct 3D geometry

### 2.4 Virtual Reality Input Devices

#### 2.4.1 Motion Controllers

VR controllers track hand movements in 3D space, enabling natural interaction in virtual environments.

**Features:**
- 6DOF (Degrees of Freedom) tracking
- Haptic feedback
- Thumbstick and trigger inputs

#### 2.4.2 Data Gloves

Gloves equipped with sensors track finger movements and hand position, enabling natural gesture-based input for VR applications.

#### 2.4.3 Eye Trackers

Used in VR headsets and eye-gaze applications, eye trackers monitor where the user is looking, enabling foveated rendering and eye-based interaction.

---

## 3. Output Devices in Computer Graphics

Output devices render processed graphical information for visual perception. The quality of output directly impacts the user's experience.

### 3.1 Display Devices

#### 3.1.1 Cathode Ray Tube (CRT)

Although largely obsolete, **CRT** monitors were the standard for decades and remain relevant for understanding display fundamentals.

**Components:**
- Electron gun
- Phosphor screen
- Deflection coils
- Control grid

**Technical Specifications:**
- Resolution: 640x480 to 2048x1536
- Refresh Rate: 60-200 Hz
- Dot Pitch: 0.20-0.30mm
- Color Depth: 24-bit (16.7 million colors)

#### 3.1.2 Liquid Crystal Display (LCD)

**LCD** technology uses liquid crystals between electrodes to control light passage. The standard for modern displays.

**Types:**
- **TN (Twisted Nematic)**: Fast response, limited viewing angles
- **IPS (In-Plane Switching)**: Excellent color accuracy, wide viewing angles
- **VA (Vertical Alignment)**: High contrast, good color reproduction

**Technical Specifications:**
- Resolution: 1920x1080 (Full HD) to 7680x4320 (8K)
- Response Time: 1-5ms
- Contrast Ratio: 1000:1 to 5000:1
- Brightness: 250-1000 nits
- Viewing Angles: 160°-178°

#### 3.1.3 Light Emitting Diode (LED) Display

**LED** displays use light-emitting diodes as pixels, offering better contrast and energy efficiency than LCD.

**Applications:**
- Large format displays
- Outdoor signage
- HDR televisions
- Desktop monitors (often marketing term for LCD with LED backlight)

#### 3.1.4 Plasma Display

Plasma displays use ionized gas cells that emit UV light to excite phosphors. Once common for large-screen TVs but largely discontinued.

**Characteristics:**
- Self-emissive (true blacks)
- Wide viewing angles
- Excellent color accuracy
- Higher power consumption than LCD/LED

#### 3.1.5 OLED (Organic LED)

**OLED** uses organic compounds that emit light when electrified. Each pixel is self-emitting, enabling perfect blacks and infinite contrast.

**Technical Specifications:**
- Resolution: Up to 8K
- Response Time: <0.1ms
- Contrast Ratio: Infinite (theoretical)
- Color Accuracy: >100% DCI-P3

```python
# Example: Display device capability detection
class DisplayCapabilities:
    def __init__(self):
        self.resolution = None
        self.color_depth = None
        self.refresh_rate = None
        self.panel_type = None
    
    def detect_display_info(self):
        """Query display capabilities"""
        # In real implementation, this would interface with OS APIs
        # (Windows: QueryDisplayConfig, macOS: CGDisplayIOServicePort)
        
        self.resolution = (3840, 2160)  # 4K example
        self.color_depth = 30  # bits per pixel
        self.refresh_rate = 144  # Hz
        self.panel_type = "IPS"
        
        return {
            "resolution": f"{self.resolution[0]}x{self.resolution[1]}",
            "pixels": self.resolution[0] * self.resolution[1],
            "color_depth": f"{self.color_depth}-bit ({2**self.color_depth:,} colors)",
            "refresh_rate": f"{self.refresh_rate} Hz",
            "panel_type": self.panel_type
        }
```

### 3.2 Hard Copy Output Devices

#### 3.2.1 Dot Matrix Printer

Uses pins striking an ink ribbon to create character patterns. Limited in graphical output quality but still used for multi-part forms.

**Specifications:**
- Resolution: 60-360 DPI
- Speed: 50-500 CPS (characters per second)
- Color: Monochrome (rarely 4-color ribbon)

#### 3.2.2 Inkjet Printer

Sprays microscopic ink droplets onto paper. The standard for photo and color graphic printing.

**Technical Specifications:**
- Resolution: 300-9600 DPI
- Color: 4-12 ink colors (CMYK + light variants)
- Print Speed: 10-100 PPM
- Droplet Size: 1-3 picoliters

#### 3.2.3 Laser Printer

Uses toner (dry ink) and electrostatic charges to create images. Excellent for text and high-quality graphics.

**Technical Specifications:**
- Resolution: 300-2400 DPI
- Speed: 20-100+ PPM
- Color: Monochrome or CMYK
- Memory: 64MB-2GB

#### 3.2.4 Plotter

Specialized output device for vector graphics, essential for CAD and architectural drawings.

**Types:**
- **Pen Plotter**: Uses pens for drawing
- **Electrostatic Plotter**: Uses toner like laser
- **Cutting Plotter**: Cuts vinyl/material
- **Large Format Printer**: For posters and banners

**Specifications:**
- Resolution: 300-2400 DPI
- Media Width: 24" to 60"+ (for large format)
- Speed: 100-1000+ mm/s

### 3.3 Virtual Reality Output Devices

#### 3.3.1 VR Head-Mounted Display (HMD)

Immersive displays worn on the head for virtual reality experiences.

**Technical Specifications:**
- Resolution: 1080x1200 per eye to 2160x2160 per eye
- Refresh Rate: 72-120 Hz
- Field of View: 90°-120°
- Panel Type: OLED or LCD

#### 3.3.2 Augmented Reality Glasses

Overlay digital information onto the real world.

**Applications:**
- Industrial maintenance
- Medical visualization
- Navigation
- Gaming

---

## 4. Technical Considerations for Computer Graphics

### 4.1 Resolution and Pixel Density

Understanding resolution is crucial for graphics professionals:

| Display Type | Typical Resolution | Pixel Density |
|--------------|-------------------|----------------|
| HD Monitor | 1920×1080 | 92 PPI |
| 2K Monitor | 2560×1440 | 109 PPI |
| 4K Monitor | 3840×2160 | 163 PPI |
| Retina Display | 4096×2304 | 218 PPI |

### 4.2 Color Models and Bit Depth

- **8-bit**: 256 colors (standard VGA)
- **24-bit**: 16.7 million colors (true color)
- **30-bit**: 1 billion colors (professional displays)
- **36-bit**: 68 billion colors (high-end graphics)

### 4.3 Refresh Rate and Response Time

- **Refresh Rate**: How often the display updates per second (Hz)
- **Response Time**: How quickly pixels change color (ms)
- **Importance for Graphics**: Higher values reduce motion blur and ghosting

---

## 5. Multiple Choice Questions

1. **Which input device is specifically designed for precision digital artwork creation?**
   - A) Mouse
   - B) Keyboard
   - C) Graphics Tablet
   - D) Joystick
   
   **Answer: C) Graphics Tablet** - Graphics tablets (digitizers) provide pressure sensitivity and precise coordinate input essential for digital art creation.

2. **What is the typical resolution range of a modern flatbed scanner for computer graphics work?**
   - A) 50-100 DPI
   - B) 300-9600 DPI
   - C) 10000-20000 DPI
   - D) 10-50 DPI
   
   **Answer: B) 300-9600 DPI** - Scanner resolution for graphics applications typically ranges from 300 DPI for basic documents to 9600 DPI for high-quality photo scanning.

3. **Which display technology provides "true black" through self-emissive pixels?**
   - A) LCD
   - B) LED-backlit LCD
   - C) OLED
   - D) CRT
   
   **Answer: C) OLED** - OLED pixels emit their own light and can be completely turned off, providing true blacks and infinite contrast ratios.

4. **What does DPI stand for in the context of input devices like mice and scanners?**
   - A) Data Per Input
   - B) Dots Per Inch
   - C) Digital Processing Index
   - D) Display Pixel Integration
   
   **Answer: B) Dots Per Inch** - DPI measures the sensitivity of pointing devices or the resolution of output/input devices, representing dots per linear inch.

5. **Which printer type uses dry toner and electrostatic charges for image creation?**
   - A) Inkjet Printer
   - B) Dot Matrix Printer
   - C) Laser Printer
   - D) Plotter
   
   **Answer: C) Laser Printer** - Laser printers use toner (powder) and electrostatic charges (via a laser) to fuse images onto paper.

6. **A light pen detects position on screen by sensing:**
   - A) Magnetic fields
   - B) Heat from the screen
   - C) Light emitted by phosphors
   - D) Electrical resistance
   
   **Answer: C) Light emitted by phosphors** - Light pens contain photocells that detect the light emitted when the electron beam strikes phosphor dots on CRT displays.

---

## 6. Flashcards

### Input Devices

| Device | Function | Key Specification |
|--------|----------|-------------------|
| **Mouse** | Translates hand movement to cursor position | DPI (800-16,000+) |
| **Graphics Tablet** | Captures precise X-Y coordinates with stylus | Resolution (2540-5080 LPI), Pressure levels (256-8192) |
| **Scanner** | Converts physical images to digital format | Resolution (300-9600 DPI), Bit depth (24-48 bit) |
| **Light Pen** | Directly points to screen positions | Response time <1ms |
| **Touchscreen** | Direct finger/stylus interaction | Multi-touch points (2-10+) |
| **VR Controller** | Tracks hand movement in 3D space | 6DOF tracking, Haptic feedback |
| **3D Scanner** | Captures object geometry | Accuracy (±0.01mm) |

### Output Devices

| Device | Technology | Primary Use |
|--------|------------|-------------|
| **CRT Monitor** | Electron beam & phosphors | Legacy systems, Testing |
| **LCD Monitor** | Liquid crystals & backlight | General computing |
| **LED Display** | Light-emitting diodes | Large format, HDR |
| **OLED Display** | Organic compounds | Premium displays, Mobile |
| **Inkjet Printer** | Microscopic ink droplets | Photo printing, Color graphics |
| **Laser Printer** | Toner & electrostatic | Text, High-volume |
| **Plotter** | Vector drawing | CAD, Architectural |
| **VR HMD** | Dual displays, Lenses | Virtual reality |

---

## 7. Key Takeaways

1. **I/O devices are fundamental to computer graphics** - They determine how users interact with graphical content and how that content is finally presented.

2. **Input devices in graphics are classified as:**
   - Pointing devices (mouse, trackball, light pen, joystick)
   - Digitizing devices (graphics tablets, touchscreens)
   - Scanning devices (2D scanners, 3D scanners)
   - VR/Specialized devices (motion controllers, data gloves, eye trackers)

3. **Output devices include:**
   - Display technologies (CRT, LCD, LED, OLED, Plasma)
   - Hard copy devices (printers: dot matrix, inkjet, laser; plotters)

4. **Technical specifications matter:**
   - DPI/LPI for input resolution
   - Refresh rate and response time for displays
   - Color depth and contrast ratios
   - Pressure sensitivity for tablets

5. **Modern trends:**
   - Touchscreen integration in all devices
   - VR/AR becoming mainstream
   - 4K/8K displays standard
   - HDR and wide color gamut displays

6. **For the Delhi University syllabus:** Focus on understanding the working principles, technical specifications, and practical applications of each device type, as this topic forms the foundation for advanced computer graphics concepts.

---

*Prepared for BSc (Hons) Computer Science, Delhi University - NEP 2024 UGCF*
*Subject: DSE CG - Computer Graphics*