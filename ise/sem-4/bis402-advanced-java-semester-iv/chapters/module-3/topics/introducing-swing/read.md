java
import javax.swing.\*;

public class SimpleSwingApp {
public static void main(String[] args) {
// 1. Create the frame on the Event Dispatch Thread (EDT)
SwingUtilities.invokeLater(() -> {
JFrame frame = new JFrame("My First Swing App"); // Create frame
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Ensure app closes
frame.setSize(400, 300); // Set size

            // 2. Create a panel and a component
            JPanel panel = new JPanel();
            JButton button = new JButton("Click Me!");

            // 3. Add an ActionListener to the button
            button.addActionListener(e ->
                JOptionPane.showMessageDialog(frame, "Hello, Swing!")
            );

            // 4. Add the button to the panel, and the panel to the frame's content pane
            panel.add(button);
            frame.add(panel);

            // 5. Make the frame visible
            frame.setVisible(true);
        });
    }

}
