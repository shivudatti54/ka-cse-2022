java
JFrame frame = new JFrame("JButton Example");
JPanel panel = new JPanel();
JButton button = new JButton("Click Me!");

panel.add(button); // Add button to the panel
frame.add(panel);  // Add panel to the frame
frame.pack();      // Sizes the window to fit its components
frame.setVisible(true);