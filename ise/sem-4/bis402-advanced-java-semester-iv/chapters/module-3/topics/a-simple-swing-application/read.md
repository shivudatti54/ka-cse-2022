java
// 1. Import necessary Swing and AWT packages
import javax.swing._;
import java.awt._;
import java.awt.event.\*;

// 2. Define the class that builds the GUI
public class SimpleSwingApp {

    // Declare components as instance variables to access them in the listener
    private JTextField textField;
    private JLabel label;

    // 3. Method to set up the GUI components
    public void createGUI() {
        // Create the main frame and set its properties
        JFrame frame = new JFrame("My First Swing App"); // Set window title
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Close app on window close
        frame.setSize(400, 150); // Set window size (width, height in pixels)

        // Get the content pane and set a layout manager
        Container contentPane = frame.getContentPane();
        contentPane.setLayout(new FlowLayout());

        // 4. Create the components
        textField = new JTextField(15); // 15 is the preferred column width
        JButton button = new JButton("Click Me!");
        label = new JLabel("Your text will appear here");

        // 5. Register an Event Listener with the button
        button.addActionListener(new ActionListener() {
            // This method is called when the button is clicked
            @Override
            public void actionPerformed(ActionEvent e) {
                // Get text from the textField and set it to the label
                String text = textField.getText();
                label.setText("Hello: " + text);
            }
        });

        // 6. Add the components to the content pane
        contentPane.add(textField);
        contentPane.add(button);
        contentPane.add(label);

        // 7. Make the frame visible (do this last, after adding components)
        frame.setVisible(true);
    }

    // 8. Main method - the entry point of the application
    public static void main(String[] args) {
        // Use SwingUtilities.invokeLater for thread safety
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                SimpleSwingApp app = new SimpleSwingApp();
                app.createGUI();
            }
        });
    }

}
