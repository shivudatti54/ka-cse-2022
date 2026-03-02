java
import javax.swing._;
import java.awt._;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

public class JToggleButtonDemo {
public static void main(String[] args) {
JFrame frame = new JFrame("JToggleButton Example");
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
frame.setSize(300, 200);
frame.setLayout(new FlowLayout());

// Create a panel whose color we will change
JPanel colorPanel = new JPanel();
colorPanel.setPreferredSize(new Dimension(250, 100));
colorPanel.setBackground(Color.WHITE);
frame.add(colorPanel);

// 1. Create the toggle button with text and initial state
JToggleButton toggleBtn = new JToggleButton("Toggle Color (OFF)", false);

// 2. Add an ItemListener to handle state change events
toggleBtn.addItemListener(new ItemListener() {
@Override
public void itemStateChanged(ItemEvent e) {
if (e.getStateChange() == ItemEvent.SELECTED) {
colorPanel.setBackground(Color.GREEN);
toggleBtn.setText("Toggle Color (ON)");
} else {
colorPanel.setBackground(Color.WHITE);
toggleBtn.setText("Toggle Color (OFF)");
}
}
});

frame.add(toggleBtn);
frame.setVisible(true);
}

}
