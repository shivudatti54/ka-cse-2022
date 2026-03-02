java
import javax.swing._;
import java.awt.event._;

public class SimpleSwingApp {
public static void main(String[] args) {
// 1. Create the frame (main window)
JFrame frame = new JFrame("My First Swing App");
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Exit on close
frame.setSize(300, 150); // Set window size

        // 2. Add a JPanel with a FlowLayout to the frame's content pane
        JPanel panel = new JPanel();
        frame.add(panel);

        // 3. Create components
        JLabel label = new JLabel("Enter your name:");
        JTextField textField = new JTextField(15); // 15 columns wide
        JButton button = new JButton("Submit");

        // 4. Add components to the panel
        panel.add(label);
        panel.add(textField);
        panel.add(button);

        // 5. Add event handling to the button
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String name = textField.getText();
                JOptionPane.showMessageDialog(frame, "Hello, " + name + "!");
            }
        });

        // 6. Make the frame visible (should be last)
        frame.setVisible(true);
    }

}
