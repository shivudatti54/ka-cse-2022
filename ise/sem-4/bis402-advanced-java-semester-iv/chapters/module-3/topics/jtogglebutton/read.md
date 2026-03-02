java
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class JToggleButtonExample {
    public static void main(String[] args) {
        JFrame frame = new JFrame("JToggleButton Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());

        JToggleButton toggleButton = new JToggleButton("Click me");
        toggleButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (toggleButton.isSelected()) {
                    System.out.println("Toggle button is selected");
                } else {
                    System.out.println("Toggle button is deselected");
                }
            }
        });

        frame.add(toggleButton);
        frame.pack();
        frame.setVisible(true);
    }
}