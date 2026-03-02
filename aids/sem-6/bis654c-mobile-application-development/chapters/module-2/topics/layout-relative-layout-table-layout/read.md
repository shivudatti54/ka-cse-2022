# **Layout Relative Layout – Table Layout**

## **Introduction**

In Android, a `Layout` is used to arrange the user interface elements in a specific way. There are several types of layouts in Android, and `Layout Relative Layout` is one of them. In this topic, we will learn about `Layout Relative Layout` and `Table Layout`.

## **What is Layout Relative Layout?**

`Layout Relative Layout` is a type of layout where elements can be arranged relative to each other. It is a flexible layout that allows you to position elements relative to each other, as well as relative to the edges of the screen.

## **How Does it Work?**

In a `Layout Relative Layout`, elements are arranged relative to each other using the following attributes:

- `android:layout_width`
- `android:layout_height`
- `android:layout_toLeftOf`
- `android:layout_toRightOf`
- `android:layout_above`
- `android:layout_below`

These attributes are used to specify the position of elements relative to each other.

## **Example: Simple Layout Relative Layout**

Here is an example of a simple `Layout Relative Layout`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Hello World!"

    />

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Click me!"
        android:layout_toLeftOf="@id/textView"
    />

</LinearLayout>
```

In this example, the `TextView` is placed at the top of the screen, and the `Button` is placed to the left of the `TextView`.

## **Table Layout**

A `Table Layout` is a type of layout that consists of rows and columns. It is used to arrange elements in a table-like structure.

## **How Does it Work?**

In a `Table Layout`, elements are arranged in rows and columns. The following attributes are used to specify the position of elements:

- `android:layout_width`
- `android:layout_height`
- `android:layout_column`
- `android:layout_row`
- `android:layout_span`
- `android:layout_weight`

These attributes are used to specify the position of elements in the table.

## **Example: Table Layout**

Here is an example of a simple `Table Layout`:

```xml
<?xml version="1.0" encoding="utf-8"?>
."<table xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <tr>
        <td>
            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="Row 1, Column 1"
            />
        </td>
        <td>
            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="Row 1, Column 2"
            />
        </td>
    </tr>

    <tr>
        <td>
            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="Row 2, Column 1"
            />
        </td>
        <td>
            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="Row 2, Column 2"
            />
        </td>
    </tr>

</table>"
```

In this example, there are two rows and two columns. The elements are arranged in a table-like structure.

## **Key Concepts:**

- **Layout Relative Layout**: A type of layout where elements can be arranged relative to each other.
- **Table Layout**: A type of layout that consists of rows and columns.
- **android:layout_width**: Specifies the width of an element.
- **android:layout_height**: Specifies the height of an element.
- **android:layout_toLeftOf**: Specifies the position of an element relative to another element.
- **android:layout_toRightOf**: Specifies the position of an element relative to another element.
- **android:layout_above**: Specifies the position of an element relative to another element.
- **android:layout_below**: Specifies the position of an element relative to another element.

## **Conclusion**

In this topic, we learned about `Layout Relative Layout` and `Table Layout`. We saw how to use these layouts to arrange elements in a specific way. We also learned about the different attributes used to specify the position of elements. With this knowledge, you can create complex user interfaces using these layouts.
