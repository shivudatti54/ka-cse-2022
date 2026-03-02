# **Layout Relative Layout – Table Layout**

## **What is Layout Relative Layout?**

Layout Relative Layout is a layout manager in Android that allows you to arrange views in a relative way, where the position and size of one view can be defined relative to another view. This is useful when you want to create a layout with multiple views that have different sizes and positions.

## **How does Layout Relative Layout work?**

In a Layout Relative Layout, each view has a defined position and size relative to its parent or sibling views. The position of a view can be defined using the following attributes:

- `layout_width`: specifies the width of the view
- `layout_height`: specifies the height of the view
- `layout_toLeftOf`: specifies the view to the left of the current view
- `layout_toRightOf`: specifies the view to the right of the current view
- `layout_above`: specifies the view above the current view
- `layout_below`: specifies the view below the current view

## **Table Layout**

A Table Layout is a type of Layout Relative Layout that arranges views in a table-like structure. Each row and column in the table has a defined width and height. The views in the table are arranged in a grid, where each view is positioned at the intersection of a row and column.

## **Key Features of Table Layout**

- **Rows and Columns**: Each row and column in the table has a defined width and height.
- **Views in a Grid**: Views are arranged in a grid, where each view is positioned at the intersection of a row and column.
- **Alignment**: Views can be aligned to the top, bottom, left, right, or center of their cell.

## **Example Use Case**

Suppose we want to create a simple table with two rows and two columns, where each cell contains a text view. We can use a Table Layout to achieve this:

```xml
<TableLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TableRow
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:text="Name" />

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:text="Age" />

    </TableRow>

    <TableRow
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:text="John Doe" />

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:text="25" />

    </TableRow>

</TableLayout>
```

In this example, we create a Table Layout with two rows and two columns. Each row contains two text views, which are aligned to the top of their cell.

## **Advantages and Disadvantages**

Advantages:

- Easy to use and customize
- Flexible layout options
- Can be used for complex table layouts

Disadvantages:

- Limited support for complex layouts
- Can be slower than other layout managers

## **Best Practices**

- Use Table Layout for simple table layouts
- Use other layout managers (e.g. LinearLayout, ConstraintLayout) for complex layouts
- Align views to the top, bottom, left, right, or center of their cell
