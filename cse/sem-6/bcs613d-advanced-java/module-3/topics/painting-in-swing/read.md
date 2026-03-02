# Painting in Swing

## Introduction

Painting in Swing refers to the mechanism by which graphical components are drawn on the screen. Unlike standard UI components that come with predefined appearances, custom painting allows developers to create unique visual elements through direct control over the rendering process. This capability is fundamental for building data visualization tools, custom controls, animations, and other graphically intensive applications.

The Swing framework handles painting through a well-defined process involving the `paintComponent()`, `paintBorder()`, and `paintChildren()` methods. At its core, painting relies on the **Graphics** class (from AWT) and its extended **Graphics2D** class, which provide methods for drawing shapes, text, and images. Understanding this process is critical because improper handling can lead to rendering artifacts, performance issues, or unresponsive UIs.

Key reasons to master Swing painting:

1. Enables creation of custom charts, graphs, and diagrams
2. Essential for game development and animations
3. Allows for platform-independent rendering
4. Forms the basis for implementing custom look-and-feel themes

## Key Concepts

### 1. The Painting Process

Swing components automatically repaint themselves when:

- The window is resized
- The component is shown for the first time
- A portion of the window becomes visible again
- Programmatically triggered via `repaint()`

**Painting sequence:**

```java
1. paintComponent(Graphics g) // Main custom drawing method
2. paintBorder(Graphics g)
3. paintChildren(Graphics g)
```

### 2. The paintComponent() Method

Override this method in `JComponent` subclasses (like `JPanel`) to implement custom painting:

```java
@Override
protected void paintComponent(Graphics g) {
 super.paintComponent(g); // Essential for proper rendering
 // Custom drawing code here
}
```

### 3. Graphics Object

The `Graphics` parameter provides drawing context with methods:

| Method                  | Description                        |
| ----------------------- | ---------------------------------- |
| `drawLine(x1,y1,x2,y2)` | Draws a straight line              |
| `fillRect(x,y,w,h)`     | Draws filled rectangle             |
| `drawOval(x,y,w,h)`     | Draws oval outline                 |
| `setColor(Color c)`     | Sets current drawing color         |
| `drawString(text,x,y)`  | Renders text at specified position |

### 4. Double Buffering

Swing uses automatic double buffering to prevent flickering. The rendering happens in an off-screen buffer before being copied to the screen.

### 5. Coordinate System

- Origin (0,0) at component's top-left corner
- X increases to the right
- Y increases downward

## Examples

### Example 1: Basic Shape Drawing

```java
class DrawingPanel extends JPanel {
 @Override
 protected void paintComponent(Graphics g) {
 super.paintComponent(g);

 // Set background
 setBackground(Color.WHITE);

 // Draw red rectangle
 g.setColor(Color.RED);
 g.fillRect(50, 50, 100, 80);

 // Draw blue circle
 g.setColor(Color.BLUE);
 g.fillOval(200, 100, 80, 80);

 // Draw text
 g.setColor(Color.BLACK);
 g.drawString(" Painting Demo", 100, 250);
 }
}

// Usage:
JFrame frame = new JFrame();
frame.add(new DrawingPanel());
frame.setSize(400, 400);
frame.setVisible(true);
```

**Output Diagram Description:**

- White background panel
- Red rectangle positioned at (50,50) with 100px width and 80px height
- Blue perfect circle at (200,100) with 80px diameter
- Black text " Painting Demo" centered near bottom

### Example 2: Custom Button with Gradient

```java
class GradientButton extends JButton {
 public GradientButton(String text) {
 super(text);
 setContentAreaFilled(false); // Disable default painting
 }

 @Override
 protected void paintComponent(Graphics g) {
 Graphics2D g2d = (Graphics2D)g;

 // Create gradient
 GradientPaint gradient = new GradientPaint(
 0, 0, Color.BLUE,
 getWidth(), getHeight(), Color.CYAN
 );

 g2d.setPaint(gradient);
 g2d.fillRoundRect(0, 0, getWidth(), getHeight(), 15, 15);

 super.paintComponent(g); // Paint text on top
 }
}
```

**Key Features:**

- Rounded corners with 15px radius
- Diagonal gradient from blue to cyan
- Inherited text rendering from JButton

### Example 3: Animation with repaint()

```java
class BouncingBall extends JPanel implements ActionListener {
 private int x = 0, y = 0;
 private int dx = 3, dy = 2;

 public BouncingBall() {
 Timer timer = new Timer(10, this);
 timer.start();
 }

 @Override
 protected void paintComponent(Graphics g) {
 super.paintComponent(g);
 g.setColor(Color.GREEN);
 g.fillOval(x, y, 30, 30);
 }

 @Override
 public void actionPerformed(ActionEvent e) {
 x += dx;
 y += dy;

 // Collision detection
 if(x < 0 || x > getWidth()-30) dx = -dx;
 if(y < 0 || y > getHeight()-30) dy = -dy;

 repaint();
 }
}
```

**Animation Process:**

1. Timer fires events every 10ms
2. Update ball position in actionPerformed()
3. repaint() triggers paintComponent()
4. Graphics context redraws ball at new position

## Exam Tips

1. **Painting Method Sequence:** Always remember the order - `paintComponent()` → `paintBorder()` → `paintChildren()`

2. **super.paintComponent(g):** Never forget to call this in overridden methods to clear background and maintain proper rendering

3. **Double Buffering:** Mention this feature when asked about flicker prevention

4. **Graphics vs Graphics2D:**

- Use `Graphics` for basic shapes
- Cast to `Graphics2D` for advanced features (gradients, anti-aliasing)

5. **repaint() vs paintImmediately():**

- `repaint()` queues a paint request
- `paintImmediately()` forces immediate update

6. **Coordinate System:** Remember Y-axis increases downward, unlike mathematical coordinates

7. **Performance Tip:** Minimize object creation in paint methods (create reusable objects in constructor)

8. **Common Mistake:** Never call paintComponent() directly - use repaint() instead
