java
// Create a LinearLayout
LinearLayout layout = new LinearLayout(this);
layout.setOrientation(LinearLayout.VERTICAL);

// Create a TextView
TextView textView = new TextView(this);
textView.setText("Enter your name:");

// Create an EditText
EditText editText = new EditText(this);

// Create a Button
Button button = new Button(this);
button.setText("Submit");

// Add the components to the layout
layout.addView(textView);
layout.addView(editText);
layout.addView(button);

// Set the layout as the content view
setContentView(layout);