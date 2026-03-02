# Introducing Swing in Java

## What is Swing?

**Swing** is a GUI (Graphical User Interface) toolkit for Java that provides a rich set of lightweight components for building desktop applications. It is part of the Java Foundation Classes (JFC) and was introduced to replace the older AWT (Abstract Window Toolkit) with more sophisticated and flexible GUI components.

```java
import javax.swing.*;

public class SimpleSwingApp {
 public static void main(String[] args) {
 JFrame frame = new JFrame("My First Swing Application");
 frame.setSize(400, 300);
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 frame.setVisible(true);
 }
}
```

## Key Features of Swing

| Feature                     | Description                                               |
| --------------------------- | --------------------------------------------------------- |
| **Lightweight Components**  | Components written entirely in Java, platform-independent |
| **Pluggable Look and Feel** | Can change appearance without modifying code              |
| **Rich Component Set**      | Buttons, tables, trees, text fields, and more             |
| **MVC Architecture**        | Model-View-Controller design pattern                      |
| **Platform Independent**    | Same appearance across different operating systems        |

## Swing vs AWT

| Aspect            | AWT                             | Swing                             |
| ----------------- | ------------------------------- | --------------------------------- |
| **Weight**        | Heavyweight (native components) | Lightweight (pure Java)           |
| **Platform**      | Platform-dependent look         | Platform-independent              |
| **Components**    | Limited set                     | Rich set of components            |
| **Performance**   | Faster (native code)            | Slightly slower but more flexible |
| **Customization** | Limited                         | Highly customizable               |
| **Package**       | java.awt.\*                     | javax.swing.\*                    |

## Swing Architecture

### Model-View-Controller (MVC) Design

Swing follows the MVC architecture where:

- **Model**: Stores the component's data
- **View**: Displays the component
- **Controller**: Handles user interactions

```
┌─────────────────────┐
│ Controller │ ← User Input
│ (Event Handling) │
└─────────────────────┘
 ↓
┌─────────────────────┐
│ Model │ ← Data Storage
│ (Component State) │
└─────────────────────┘
 ↓
┌─────────────────────┐
│ View │ ← Visual Display
│ (Presentation) │
└─────────────────────┘
```

## Swing Class Hierarchy

```
java.lang.Object
 └── java.awt.Component
 └── java.awt.Container
 ├── java.awt.Window
 │ └── java.awt.Frame
 │ └── javax.swing.JFrame
 └── javax.swing.JComponent
 ├── javax.swing.JButton
 ├── javax.swing.JLabel
 ├── javax.swing.JTextField
 ├── javax.swing.JPanel
 └── ... (other components)
```

## Top-Level Containers

### JFrame - Main Application Window

```java
import javax.swing.*;

public class JFrameDemo {
 public static void main(String[] args) {
 // Create frame
 JFrame frame = new JFrame("JFrame Demo");

 // Set frame properties
 frame.setSize(400, 300);
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 frame.setLocationRelativeTo(null); // Center on screen

 // Make visible
 frame.setVisible(true);
 }
}
```

### JDialog - Dialog Window

```java
import javax.swing.*;

public class JDialogDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("Main Frame");
 frame.setSize(400, 300);
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

 // Create dialog
 JDialog dialog = new JDialog(frame, "My Dialog", true); // modal
 dialog.setSize(200, 150);
 dialog.setLocationRelativeTo(frame);

 JButton button = new JButton("Show Dialog");
 button.addActionListener(e -> dialog.setVisible(true));

 frame.add(button);
 frame.setVisible(true);
 }
}
```

### JApplet - Applet Container (Deprecated in Java 9+)

```java
import javax.swing.*;

public class SimpleApplet extends JApplet {
 public void init() {
 JLabel label = new JLabel("Hello from JApplet");
 add(label);
 }
}
```

## Common Swing Components

### JLabel - Display Text or Images

```java
import javax.swing.*;

public class JLabelDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("JLabel Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

 // Text label
 JLabel label1 = new JLabel("Welcome to Swing");

 // Label with HTML
 JLabel label2 = new JLabel("<html><b>Bold</b> and <i>Italic</i></html>");

 // Label with alignment
 JLabel label3 = new JLabel("Centered", SwingConstants.CENTER);

 frame.setLayout(new BoxLayout(frame.getContentPane(), BoxLayout.Y_AXIS));
 frame.add(label1);
 frame.add(label2);
 frame.add(label3);

 frame.setSize(300, 200);
 frame.setVisible(true);
 }
}
```

### JButton - Clickable Button

```java
import javax.swing.*;
import java.awt.event.*;

public class JButtonDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("JButton Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

 JLabel label = new JLabel("Click the button");
 JButton button = new JButton("Click Me");

 // Add action listener
 button.addActionListener(new ActionListener() {
 public void actionPerformed(ActionEvent e) {
 label.setText("Button Clicked!");
 }
 });

 frame.setLayout(new BoxLayout(frame.getContentPane(), BoxLayout.Y_AXIS));
 frame.add(label);
 frame.add(button);

 frame.setSize(300, 200);
 frame.setVisible(true);
 }
}
```

### JTextField - Single Line Text Input

```java
import javax.swing.*;
import java.awt.*;

public class JTextFieldDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("JTextField Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 frame.setLayout(new FlowLayout());

 JLabel label = new JLabel("Enter Name:");
 JTextField textField = new JTextField(20); // 20 columns wide
 JButton button = new JButton("Submit");
 JLabel output = new JLabel();

 button.addActionListener(e -> {
 String name = textField.getText();
 output.setText("Hello, " + name);
 });

 frame.add(label);
 frame.add(textField);
 frame.add(button);
 frame.add(output);

 frame.setSize(400, 150);
 frame.setVisible(true);
 }
}
```

### JTextArea - Multi-Line Text Input

```java
import javax.swing.*;
import java.awt.*;

public class JTextAreaDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("JTextArea Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

 JTextArea textArea = new JTextArea(10, 30); // rows, columns
 textArea.setLineWrap(true);
 textArea.setWrapStyleWord(true);

 // Add scroll pane
 JScrollPane scrollPane = new JScrollPane(textArea);

 frame.add(scrollPane);
 frame.setSize(400, 300);
 frame.setVisible(true);
 }
}
```

### JCheckBox - Multiple Selection

```java
import javax.swing.*;
import java.awt.*;

public class JCheckBoxDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("JCheckBox Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 frame.setLayout(new FlowLayout());

 JCheckBox cb1 = new JCheckBox("Java");
 JCheckBox cb2 = new JCheckBox("Python");
 JCheckBox cb3 = new JCheckBox("C++");

 JButton button = new JButton("Submit");
 JLabel output = new JLabel();

 button.addActionListener(e -> {
 String selected = "Selected: ";
 if (cb1.isSelected()) selected += "Java ";
 if (cb2.isSelected()) selected += "Python ";
 if (cb3.isSelected()) selected += "C++ ";
 output.setText(selected);
 });

 frame.add(cb1);
 frame.add(cb2);
 frame.add(cb3);
 frame.add(button);
 frame.add(output);

 frame.setSize(400, 200);
 frame.setVisible(true);
 }
}
```

### JRadioButton - Single Selection

```java
import javax.swing.*;
import java.awt.*;

public class JRadioButtonDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("JRadioButton Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 frame.setLayout(new FlowLayout());

 JRadioButton rb1 = new JRadioButton("Male");
 JRadioButton rb2 = new JRadioButton("Female");

 // Group radio buttons (only one can be selected)
 ButtonGroup group = new ButtonGroup();
 group.add(rb1);
 group.add(rb2);

 JButton button = new JButton("Submit");
 JLabel output = new JLabel();

 button.addActionListener(e -> {
 String gender = rb1.isSelected() ? "Male" : "Female";
 output.setText("Selected: " + gender);
 });

 frame.add(rb1);
 frame.add(rb2);
 frame.add(button);
 frame.add(output);

 frame.setSize(400, 150);
 frame.setVisible(true);
 }
}
```

### JComboBox - Dropdown List

```java
import javax.swing.*;
import java.awt.*;

public class JComboBoxDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("JComboBox Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 frame.setLayout(new FlowLayout());

 String[] countries = {"India", "USA", "UK", "Canada", "Australia"};
 JComboBox<String> comboBox = new JComboBox<>(countries);

 JLabel label = new JLabel("Select Country:");
 JLabel output = new JLabel();

 comboBox.addActionListener(e -> {
 String selected = (String) comboBox.getSelectedItem();
 output.setText("Selected: " + selected);
 });

 frame.add(label);
 frame.add(comboBox);
 frame.add(output);

 frame.setSize(400, 150);
 frame.setVisible(true);
 }
}
```

## Layout Managers

### FlowLayout - Left to Right Flow

```java
import javax.swing.*;
import java.awt.*;

public class FlowLayoutDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("FlowLayout Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 frame.setLayout(new FlowLayout());

 frame.add(new JButton("Button 1"));
 frame.add(new JButton("Button 2"));
 frame.add(new JButton("Button 3"));

 frame.setSize(300, 150);
 frame.setVisible(true);
 }
}
```

### BorderLayout - Five Regions

```java
import javax.swing.*;
import java.awt.*;

public class BorderLayoutDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("BorderLayout Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 frame.setLayout(new BorderLayout());

 frame.add(new JButton("North"), BorderLayout.NORTH);
 frame.add(new JButton("South"), BorderLayout.SOUTH);
 frame.add(new JButton("East"), BorderLayout.EAST);
 frame.add(new JButton("West"), BorderLayout.WEST);
 frame.add(new JButton("Center"), BorderLayout.CENTER);

 frame.setSize(400, 300);
 frame.setVisible(true);
 }
}
```

### GridLayout - Grid of Cells

```java
import javax.swing.*;
import java.awt.*;

public class GridLayoutDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("GridLayout Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 frame.setLayout(new GridLayout(3, 2)); // 3 rows, 2 columns

 for (int i = 1; i <= 6; i++) {
 frame.add(new JButton("Button " + i));
 }

 frame.setSize(300, 200);
 frame.setVisible(true);
 }
}
```

## Event Handling in Swing

### Action Event

```java
import javax.swing.*;
import java.awt.event.*;

public class ActionEventDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("Action Event Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

 JButton button = new JButton("Click Me");
 JLabel label = new JLabel("No clicks yet");

 // Using lambda expression (Java 8+)
 button.addActionListener(e -> label.setText("Button clicked!"));

 frame.setLayout(new java.awt.FlowLayout());
 frame.add(button);
 frame.add(label);

 frame.setSize(300, 150);
 frame.setVisible(true);
 }
}
```

### Mouse Event

```java
import javax.swing.*;
import java.awt.event.*;

public class MouseEventDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("Mouse Event Demo");
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

 JLabel label = new JLabel("Move mouse over the frame");

 frame.addMouseListener(new MouseAdapter() {
 public void mouseClicked(MouseEvent e) {
 label.setText("Mouse clicked at: " + e.getX() + ", " + e.getY());
 }
 });

 frame.add(label);
 frame.setSize(400, 300);
 frame.setVisible(true);
 }
}
```

## Complete Swing Application Example

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SimpleCalculator extends JFrame {
 private JTextField num1Field, num2Field, resultField;
 private JButton addButton, subtractButton, multiplyButton, divideButton;

 public SimpleCalculator() {
 setTitle("Simple Calculator");
 setSize(400, 200);
 setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 setLayout(new GridLayout(4, 2, 10, 10));

 // Create components
 num1Field = new JTextField();
 num2Field = new JTextField();
 resultField = new JTextField();
 resultField.setEditable(false);

 addButton = new JButton("Add");
 subtractButton = new JButton("Subtract");
 multiplyButton = new JButton("Multiply");
 divideButton = new JButton("Divide");

 // Add action listeners
 addButton.addActionListener(e -> calculate('+'));
 subtractButton.addActionListener(e -> calculate('-'));
 multiplyButton.addActionListener(e -> calculate('*'));
 divideButton.addActionListener(e -> calculate('/'));

 // Add components to frame
 add(new JLabel("Number 1:"));
 add(num1Field);
 add(new JLabel("Number 2:"));
 add(num2Field);
 add(addButton);
 add(subtractButton);
 add(multiplyButton);
 add(divideButton);

 // Create result panel
 JPanel resultPanel = new JPanel(new FlowLayout());
 resultPanel.add(new JLabel("Result:"));
 resultPanel.add(resultField);

 // Add result panel at bottom
 add(resultPanel);

 setVisible(true);
 }

 private void calculate(char operation) {
 try {
 double num1 = Double.parseDouble(num1Field.getText());
 double num2 = Double.parseDouble(num2Field.getText());
 double result = 0;

 switch (operation) {
 case '+': result = num1 + num2; break;
 case '-': result = num1 - num2; break;
 case '*': result = num1 * num2; break;
 case '/':
 if (num2 != 0) {
 result = num1 / num2;
 } else {
 resultField.setText("Error: Division by zero");
 return;
 }
 break;
 }

 resultField.setText(String.valueOf(result));
 } catch (NumberFormatException e) {
 resultField.setText("Error: Invalid input");
 }
 }

 public static void main(String[] args) {
 // Use Event Dispatch Thread for thread safety
 SwingUtilities.invokeLater(() -> new SimpleCalculator());
 }
}
```

## Best Practices

1. **Use SwingUtilities.invokeLater()**: Always create and modify Swing components on the Event Dispatch Thread (EDT)

```java
SwingUtilities.invokeLater(() -> {
 JFrame frame = new JFrame();
 // ... setup frame
 frame.setVisible(true);
});
```

2. **Separate GUI from Logic**: Keep business logic separate from UI code

3. **Handle Exceptions**: Always handle exceptions in event handlers

4. **Dispose Resources**: Properly dispose frames and dialogs when done

5. **Use Layout Managers**: Avoid absolute positioning; use layout managers for responsive designs

## Exam Tips

1. **Remember the Hierarchy**: JFrame → JPanel → Components
2. **Event Handling**: Know ActionListener, MouseListener, KeyListener
3. **Layout Managers**: FlowLayout, BorderLayout, GridLayout, BoxLayout
4. **Common Components**: JLabel, JButton, JTextField, JTextArea, JCheckBox, JRadioButton
5. **Thread Safety**: Swing is not thread-safe; use EDT for GUI updates
6. **Top-Level Containers**: JFrame, JDialog, JApplet (deprecated)
7. **setDefaultCloseOperation()**: Remember to set this for proper window closing

## Further Reading

For more information on Swing components, advanced layouts, custom painting, and Look and Feel customization, refer to the official Java Swing documentation and Oracle's Java Tutorials.
