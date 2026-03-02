# **Chapters 3 & 4: Directory Structure and Android User Interface**

## **Introduction**

In the previous chapter, we set up the foundation for our Android application by creating a new project and setting up the necessary tools. In this chapter, we will delve into the world of directory structure and Android user interface.

## **Directory Structure**

A directory structure is a hierarchical organization of files and folders that are used to categorize, store, and manage data and other files in a project. In Android, the directory structure is used to organize the different components of an application, such as activities, services, and assets.

### Project Structure

Let's take a look at the default project structure for an Android application:

```markdown
MyApp/
|---- app/
| |---- java/
| | |---- com.example.myapp/
| | | |---- MainActivity.java
| | |---- res/
| | | |---- layout/
| | | | |---- activity_main.xml
| | | |---- values/
| | | | |---- strings.xml
| |---- src/
| | |---- main/
| | | |---- java/
| | | | |---- com.example.myapp/
| | | | | |---- MainActivity.java
| | |---- test/
| | | |---- java/
| | | | |---- com.example.myapp/
| | | | | |---- MainActivityTest.java
|---- build.gradle
|---- gradle.properties
|---- settings.gradle
```

### Directory Structure Components

Here are the main components of a directory structure in Android:

- **app**: This is the top-level directory for the application's source code.
- **java**: This directory contains the application's Java source code.
- **res**: This directory contains the application's resources, such as layout files and strings.
- **src**: This directory contains the application's source code, including Java classes and test classes.
- **test**: This directory contains the application's test classes.
- **build.gradle**: This file contains the build configuration for the application.
- **gradle.properties**: This file contains the Gradle properties for the application.
- **settings.gradle**: This file contains the settings for the build configuration.

### Directory Structure Best Practices

Here are some best practices for organizing your directory structure:

- Use meaningful and descriptive names for directories and files.
- Keep related files and directories together.
- Use subdirectories to organize large amounts of data.
- Keep the root directory of your project organized and consistent.

## **Android User Interface**

The Android user interface (UI) is used to interact with the user and display information to them. In this chapter, we will explore the different components of the Android UI and how to create them.

### Android UI Components

Here are the main components of the Android UI:

- **Activity**: This is the top-level component of the Android UI. It is responsible for displaying the user interface and handling user interactions.
- **View**: This is a graphical component that is used to display information to the user.
- **Button**: This is a type of view that is used to perform an action when clicked.
- **EditText**: This is a type of view that is used to input text.
- **TextView**: This is a type of view that is used to display text.
- **LinearLayout**: This is a type of layout manager that is used to arrange views horizontally or vertically.
- **RelativeLayout**: This is a type of layout manager that is used to arrange views relative to each other.

### Creating a Simple UI

Let's create a simple UI to demonstrate how to use these components. We will create a layout file called `activity_main.xml` and add a button, edit text, and text view to it.

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <EditText
        android:id="@+id/editText"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter your name" />

    <Button
        android:id="@+id/button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Click me" />

    <TextView
        android:id="@+id/textView"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Hello, world!" />

</LinearLayout>
```

### Handling User Interactions

To handle user interactions, we need to create a Java class that extends the `Activity` class. We will override the `onCreate` method to initialize the UI components.

```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Get the UI components
        EditText editText = findViewById(R.id.editText);
        Button button = findViewById(R.id.button);
        TextView textView = findViewById(R.id.textView);

        // Set a click listener for the button
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Get the text from the edit text
                String name = editText.getText().toString();

                // Display the text in the text view
                textView.setText("Hello, " + name + "!");

                // Close the activity
                finish();
            }
        });
    }
}
```

## **Case Study: Creating a Simple To-Do List App**

Let's create a simple to-do list app to demonstrate how to use the directory structure and Android UI.

### Directory Structure

We will create a new project and organize the files and directories as follows:

```markdown
ToDoList/
|---- app/
| |---- java/
| | |---- com.example.todolist/
| | | |---- MainActivity.java
| | |---- res/
| | | |---- layout/
| | | | |---- activity_main.xml
| | | |---- values/
| | | | |---- strings.xml
| |---- src/
| | |---- main/
| | | |---- java/
| | | | |---- com.example.todolist/
| | | | | |---- MainActivity.java
| | | |---- test/
| | | | |---- java/
| | | | | |---- com.example.todolist/
| | | | | |---- MainActivityTest.java
|---- build.gradle
|---- gradle.properties
|---- settings.gradle
```

### Android UI

We will create a layout file called `activity_main.xml` and add a list view and a button to it.

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <ListView
        android:id="@+id/listView"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

    <Button
        android:id="@+id/button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Add to do list" />

</LinearLayout>
```

### Handling User Interactions

We will create a Java class that extends the `Activity` class. We will override the `onCreate` method to initialize the UI components and add a click listener for the button.

```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Get the UI components
        ListView listView = findViewById(R.id.listView);
        Button button = findViewById(R.id.button);

        // Set a click listener for the button
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Add a new to-do item to the list
                AddToDoItem("Buy milk");
            }
        });
    }

    // Method to add a new to-do item to the list
    public void AddToDoItem(String item) {
        // Create a new to-do item
        ToDoItem toDoItem = new ToDoItem(item);

        // Add the to-do item to the list
        listView.addItem(toDoItem);
    }
}

// Class to represent a to-do item
public class ToDoItem {
    private String item;

    public ToDoItem(String item) {
        this.item = item;
    }

    public String getItem() {
        return item;
    }

    public void setItem(String item) {
        this.item = item;
    }
}
```

## **Conclusion**

In this chapter, we explored the directory structure and Android UI. We learned how to create a simple UI using the `LinearLayout` and `TextView` components. We also learned how to handle user interactions by adding a click listener to a button. We created a simple to-do list app to demonstrate how to use the directory structure and Android UI. In the next chapter, we will learn about databases and data storage in Android.

## **Further Reading**

- [Android Developers: Directory Structure](https://developer.android.com/studio/projects/android-directory-structure)
- [Android Developers: User Interface](https://developer.android.com/guide/topics/ui)
- [Android Developers: Database and Data Storage](https://developer.android.com/training/data-storage)
- [Android Authority: Android UI components](https://www.androidauthority.com/android-ui-components-271926/)

Note: The code snippets provided in this chapter are just examples and may not be complete or functional. You may need to modify them to suit your specific needs.
