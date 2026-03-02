java
import javax.swing.*;
import java.awt.*;

public class LabelImageDemo extends JFrame {

    public LabelImageDemo() {
        // Set up the JFrame
        setTitle(" - JLabel & ImageIcon Demo");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout()); // Simple layout manager

        // 1. Create a JLabel with only text
        JLabel textLabel = new JLabel("Welcome to Advanced Java Programming");
        add(textLabel);

        // 2. Create an ImageIcon from a file
        // Ensure the path is correct. The image file 'vtu_logo.png' should be in your project root.
        ImageIcon icon = new ImageIcon("vtu_logo.png"); 

        // 3. Create a JLabel with the ImageIcon
        JLabel imageLabel = new JLabel(icon);
        add(imageLabel);

        // 4. Create a JLabel with both text AND an image
        // The text will be placed to the right of the image by default.
        JLabel combinedLabel = new JLabel(" University", icon, SwingConstants.CENTER);
        combinedLabel.setHorizontalTextPosition(SwingConstants.CENTER); // Text centered over icon
        combinedLabel.setVerticalTextPosition(SwingConstants.BOTTOM); // Text at bottom of icon
        add(combinedLabel);

        setVisible(true); // Make the frame visible
    }

    public static void main(String[] args) {
        // Use the Event Dispatch Thread for thread safety
        SwingUtilities.invokeLater(() -> new LabelImageDemo());
    }
}