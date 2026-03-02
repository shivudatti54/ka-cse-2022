java
import java.awt.\*;
public class AWTExample {
public static void main(String[] args) {
Frame f = new Frame("AWT Frame");
Button b = new Button("AWT Click Me");
f.add(b);
f.setSize(300, 200);
f.setVisible(true);
}
}
