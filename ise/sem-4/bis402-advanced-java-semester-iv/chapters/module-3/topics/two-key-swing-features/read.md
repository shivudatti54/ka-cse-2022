java
import javax.swing._;
import java.awt._;
import java.awt.event.\*;

public class LookAndFeelDemo extends JFrame {
public LookAndFeelDemo() {
super("PL&F Demo");
setLayout(new FlowLayout());

        // Create buttons for different LAFs
        JButton metalBtn = new JButton("Metal LAF");
        JButton nimbusBtn = new JButton("Nimbus LAF");
        JButton windowsBtn = new JButton("Windows LAF");

        // Add action listeners to change LAF on button click
        metalBtn.addActionListener(e -> setLAF("javax.swing.plaf.metal.MetalLookAndFeel"));
        nimbusBtn.addActionListener(e -> setLAF("javax.swing.plaf.nimbus.NimbusLookAndFeel"));
        windowsBtn.addActionListener(e -> setLAF("com.sun.java.swing.plaf.windows.WindowsLookAndFeel"));

        add(metalBtn);
        add(nimbusBtn);
        add(windowsBtn);

        setSize(400, 100);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    // Helper method to change the Look and Feel
    private void setLAF(String lafClassName) {
        try {
            UIManager.setLookAndFeel(lafClassName);
            SwingUtilities.updateComponentTreeUI(this); // Refresh the current frame
            pack(); // Adjust window size to new component sizes
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(LookAndFeelDemo::new);
    }

}
