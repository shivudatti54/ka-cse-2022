# Painting in Swing - Summary

## Key Definitions and Concepts

- **Painting**: The process of rendering a component's visual representation using the `Graphics` object
- **paintComponent()**: Core method overridden for custom painting (invoked automatically by Swing)
- **Graphics Object**: Provides drawing methods (`drawRect()`, `fillOval()`) and graphics context (color, font)
- **Repaint Manager**: Swing's internal mechanism that triggers component repainting
- **Double Buffering**: Automatic flicker-reduction technique using off-screen buffer
- **JComponent**: Base class for all Swing components with built-in painting infrastructure

## Important Formulas and Theorems

```java
protected void paintComponent(Graphics g) // Override this for custom painting
public void repaint() // Request asynchronous repaint of component
public void paintImmediately() // Force immediate repaint
```

**Painting Process Order:**

1. `paint()` (Top-level, rarely overridden)
2. `paintComponent()` (Main custom painting)
3. `paintBorder()`
4. `paintChildren()`

## Key Points

- Always override `paintComponent()` not `paint()` for custom graphics
- Call `super.paintComponent(g)` first to clear background (critical for opaque components)
- Use `Graphics2D` (subclass of `Graphics`) for advanced features like anti-aliasing
- Swing uses **passive rendering** - components redraw when requested by RepaintManager
- Enable double buffering via `setDoubleBuffered(true)` for smooth animations
- Use `repaint(Rectangle)` for partial updates to optimize performance
- Set component opacity with `setOpaque(true/false)` to control background painting
- Coordinate system starts at (0,0) in component's top-left corner
- MVC architecture influences painting via separation of data (Model) and display (View)

## Common Mistakes to Avoid

1. **Overriding paint() instead of paintComponent()**  
   Leads to improper rendering of borders/children components

2. **Forgetting super.paintComponent(g)**  
   Causes ghosting artifacts and improper background clearing

3. **Modifying component state during painting**  
   Painting methods should be read-only operations

4. **Performing expensive operations in paintComponent()**  
   Slows down UI responsiveness (do preprocessing elsewhere)

## Revision Tips

1. **Memorize the painting sequence**  
   Practice writing skeleton code for `paintComponent()` with proper super call

2. **Experiment with coordinate transformations**  
   Create simple diagrams using different Graphics methods

3. **Trace the repaint process**  
   Understand how events trigger `repaint()` and the role of RepaintManager

4. **Compare AWT vs Swing painting**  
   Note how Swing's lightweight components enable transparent backgrounds
