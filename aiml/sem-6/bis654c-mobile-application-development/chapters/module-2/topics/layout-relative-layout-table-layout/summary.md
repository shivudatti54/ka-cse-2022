# **Layout Relative Layout – Table Layout**

## **Overview**

- A Layout Relative Layout is a layout manager that allows you to define the position of views relative to other views.
- It is a powerful tool for complex layouts.

## **Key Points**

- **Table Layout**: A table layout is a type of layout manager that uses a table to arrange views.
- **Table Layout Specifications**: Each view is specified by its row and column.
- **Table Layout Properties**:
  - `layout_width`: The width of the view in pixels.
  - `layout_height`: The height of the view in pixels.
  - `layout_row`: The row of the view in the table.
  - `layout_column`: The column of the view in the table.
- **Table Layout Example**:
  ```xml
  <TableLayout
      xmlns:android="http://schemas.android.com/apk/res/android"
      android:layout_width="match_parent"
      android:layout_height="match_parent">

      <TableRow
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:orientation="vertical">

          <EditText
              android:layout_width="0dp"
              android:layout_height="wrap_content"
              android:layout_column="0"
              android:layout_row="0"
              android:layout_weight="1" />

          <EditText
              android:layout_width="0dp"
              android:layout_height="wrap_content"
              android:layout_column="1"
              android:layout_row="0"
              android:layout_weight="1" />

      </TableRow>

      <TableRow
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:orientation="vertical">

          <EditText
              android:layout_width="0dp"
              android:layout_height="wrap_content"
              android:layout_column="0"
              android:layout_row="1"
              android:layout_weight="1" />

          <EditText
              android:layout_width="0dp"
              android:layout_height="wrap_content"
              android:layout_column="1"
              android:layout_row="1"
              android:layout_weight="1" />

      </TableRow>

</TableLayout>
```
**Important Formulas and Definitions**
-------------------------------------

- **Table Layout Formula**: `layout_width = layout_column * width + layout_row * width`
- **Table Layout Definition**: A table layout is a type of layout manager that uses a table to arrange views.

## **Theorems**

- **Table Layout Theorem**: The total width of a row is equal to the sum of the widths of all views in the row.

Note: This is a concise summary and revision notes for the topic "Layout Relative Layout – Table Layout". It is not a comprehensive guide.
