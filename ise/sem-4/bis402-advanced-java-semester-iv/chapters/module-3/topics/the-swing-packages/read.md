java
import javax.swing._;
import java.awt._;
import java.awt.event.\*;

public class SimpleSwingApp {

    public static void main(String[] args) {
        // 1. Create the frame (the main window)
        JFrame frame = new JFrame("My First Swing App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);
        frame.setLayout(new FlowLayout()); // Set a layout manager

        // 2. Create components
        JLabel label = new JLabel("Hello,  Students!");
        JButton button = new JButton("Click Me");

        // 3. Add an event listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // This code runs when the button is clicked
                label.setText("Button was clicked!");
            }
        });

        // 4. Add components to the frame's content pane
        frame.add(button);
        frame.add(label);

        // 5. Make the frame visible (should be last)
        frame.setVisible(true);
    }

}
