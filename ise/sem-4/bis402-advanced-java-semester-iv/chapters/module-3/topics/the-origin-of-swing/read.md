java
// AWT Example (Heavyweight)
import java.awt._;
import java.awt.event._;

public class AWTExample {
public static void main(String[] args) {
Frame frame = new Frame("AWT Frame");
Button button = new Button("Click Me (AWT)");
frame.add(button);
frame.setSize(300, 200);
frame.setVisible(true);
}
}
