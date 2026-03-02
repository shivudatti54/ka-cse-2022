# JLabel and ImageIcon in Java Swing

## 1. Introduction

JLabel is a fundamental component in the Java Swing framework that displays non-editable text, images, or both. It is part of the `javax.swing` package and extends `JComponent`, inheriting its properties and behaviors. As a lightweight component, JLabel is primarily used for presenting information to users in a read-only format, making it essential for creating informative and visually appealing graphical user interfaces (GUIs).

Unlike interactive components such as buttons or text fields, JLabel does not respond to user input events directly. This passive nature makes it ideal for labeling form fields, displaying status messages, showing images, and creating splash screens. The component supports various alignment options and can render HTML-formatted text, providing developers with flexibility in presentation.

## 2. Class Hierarchy

```
java.lang.Object
 └── java.awt.Component
 └── java.awt.Container
 └── javax.swing.JComponent
 └── javax.swing.JLabel
```

The inheritance hierarchy reveals that JLabel inherits all capabilities from its parent classes, including painting, event handling (to some extent), and container management. The `JComponent` class provides look-and-feel support, while `Container` enables JLabel to potentially hold other components (though this is rarely used in practice).

## 3. ImageIcon Class

The `ImageIcon` class, also part of `javax.swing`, encapsulates an image and provides a convenient way to load and display graphical content. It implements the `Icon` interface and supports various image formats including GIF, JPEG, PNG, and BMP. ImageIcon can load images from files, URLs, byte arrays, and even from image objects.

### ImageIcon Constructors:

```java
// Load from file
ImageIcon icon1 = new ImageIcon("path/to/image.png");

// Load from URL
ImageIcon icon2 = new ImageIcon(new URL("https://example.com/image.gif"));

// Load from byte array
ImageIcon icon3 = new ImageIcon(byteArray);

// Load from Image object
ImageIcon icon4 = new ImageIcon(myImageObject);

// With description
ImageIcon icon5 = new ImageIcon("path/to/image.png", "Description text");
```

## 4. JLabel Constructors

JLabel provides multiple constructors to accommodate different initialization requirements:

```java
// Text-only label
JLabel label1 = new JLabel("Simple Text");

// Icon-only label
JLabel label2 = new JLabel(icon);

// Text with horizontal alignment
JLabel label3 = new JLabel("Text", SwingConstants.LEFT);

// Icon with horizontal alignment
JLabel label4 = new JLabel(icon, SwingConstants.CENTER);

// Text, Icon, and horizontal alignment
JLabel label5 = new JLabel("Text", icon, SwingConstants.RIGHT);

// All parameters: text, icon, horizontal alignment, vertical alignment
JLabel label6 = new JLabel("Text", icon, SwingConstants.LEADING);
```

## 5. Key Methods

### Text Manipulation:

- `setText(String text)`: Dynamically sets the label's text content
- `getText()`: Retrieves the current text
- `setDisplayedMnemonic(char mnemonic)`: Sets keyboard mnemonic for accessibility

### Icon Manipulation:

- `setIcon(Icon icon)`: Sets the icon to be displayed
- `getIcon()`: Returns the current icon
- `setDisabledIcon(Icon icon)`: Sets icon shown when component is disabled

### Alignment Control:

- `setHorizontalAlignment(int alignment)`: Sets horizontal alignment (LEFT, CENTER, RIGHT, LEADING, TRAILING)
- `setVerticalAlignment(int alignment)`: Sets vertical alignment (TOP, CENTER, BOTTOM)
- `setHorizontalTextPosition(int position)`: Position of text relative to icon
- `setVerticalTextPosition(int position)`: Vertical text position relative to icon

### Example demonstrating alignment:

```java
JLabel label = new JLabel("Text", icon, SwingConstants.CENTER);
label.setHorizontalTextPosition(SwingConstants.LEFT);
label.setVerticalTextPosition(SwingConstants.TOP);
```

## 6. HTML Formatting in JLabel

JLabel supports HTML rendering, enabling rich text formatting within labels. This feature significantly enhances the visual presentation of text in Swing applications.

```java
JLabel htmlLabel = new JLabel(
 "<html>" +
 "<font color='blue'><b>Bold Blue Text</b></font><br>" +
 "<font color='red'>Red Text</font><br>" +
 "<i>Italic Text</i>" +
 "</html>"
);
```

HTML support includes fonts, colors, lists, tables, and other HTML formatting. However, developers should note that extensive HTML in labels may impact performance.

## 7. Complete Example

The following comprehensive example demonstrates various JLabel and ImageIcon features:

```java
import javax.swing.*;
import java.awt.*;

public class LabelDemo {
 public static void main(String[] args) {
 // Create main frame
 JFrame frame = new JFrame("JLabel Comprehensive Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 frame.setSize(400, 300);
 frame.setLayout(new FlowLayout());

 // 1. Simple text label
 JLabel simpleLabel = new JLabel("Welcome to Advanced Java!");
 frame.add(simpleLabel);

 // 2. Label with center alignment
 JLabel centerLabel = new JLabel("Center Aligned", SwingConstants.CENTER);
 centerLabel.setPreferredSize(new Dimension(300, 30));
 frame.add(centerLabel);

 // 3. Label with icon (assuming image exists)
 // ImageIcon icon = new ImageIcon("path/to/image.png");
 // JLabel iconLabel = new JLabel(icon);
 // frame.add(iconLabel);

 // 4. Label with text and icon
 JLabel textIconLabel = new JLabel("Click Here", null, SwingConstants.LEFT);
 textIconLabel.setBorder(BorderFactory.createLineBorder(Color.GRAY));
 frame.add(textIconLabel);

 // 5. HTML formatted label
 JLabel htmlLabel = new JLabel(
 "<html><center>Multi-line<br>HTML Formatted<br>Label</center></html>"
 );
 frame.add(htmlLabel);

 // 6. Label with foreground color
 JLabel coloredLabel = new JLabel("Colored Text");
 coloredLabel.setForeground(Color.BLUE);
 coloredLabel.setFont(new Font("Arial", Font.BOLD, 16));
 frame.add(coloredLabel);

 frame.setVisible(true);
 }
}
```

## 8. Best Practices

1. **Use appropriate constructors**: Choose constructors that minimize subsequent method calls
2. **Set preferred sizes**: When precise sizing is needed, use `setPreferredSize()` or layout managers
3. **Combine with layout managers**: Let layout managers handle positioning rather than hardcoding coordinates
4. **Accessibility**: Set tooltips using `setToolTipText()` and displayed mnemonics for enhanced accessibility
5. **Non-editable content**: Remember that JLabel is display-only; use other components for user input

## 9. Common Pitfalls

- Attempting to make JLabel editable (it is not designed for this purpose)
- Forgetting to call `setVisible(true)` on the frame
- Not accounting for text size when setting label dimensions
- Using absolute positioning instead of layout managers
- Loading large images without proper scaling, affecting performance
