# Layout Relative Layout – Table Layout

=====================================

## Introduction

---

In Android application development, a Layout is a structural representation of the user interface. Android provides various layout types to support different design requirements. This topic will delve into the `Layout Relative Layout` and its variations, specifically focusing on `Table Layout`.

## Historical Context

---

The concept of `Layout Relative Layout` dates back to Android 1.0. It was designed to provide a flexible way to arrange views in a layout, allowing developers to create complex user interfaces.

## Modern Developments

---

Over the years, Android has introduced several new layout types, including:

- `Linear Layout`: A linear layout is a one-dimensional layout where all views are arranged in a row or column.
- `Relative Layout`: A relative layout is a layout where views are arranged relative to each other.
- `Constraint Layout`: A constraint layout is a layout where views are arranged based on constraints, providing a more efficient way to design and implement complex user interfaces.

## Layout Relative Layout

---

A `Layout Relative Layout` is a layout where views can be arranged relative to each other. It is based on a concept called "anchored" views, which are views that have a defined position relative to other views or the layout's edges.

### Layout Relative Layout Components

The following components are used in a `Layout Relative Layout`:

- `ViewGroup`: The root view of the layout.
- `View`: A view that can be added to the layout.
- `AnchorView`: A view that has a defined position relative to other views or the layout's edges.

### Layout Relative Layout Attributes

The following attributes are used in a `Layout Relative Layout`:

- `layout_width`: The width of the view.
- `layout_height`: The height of the view.
- `layout_x`: The x-coordinate of the view relative to its parent.
- `layout_y`: The y-coordinate of the view relative to its parent.
- `layout_alignParentX`: The x-coordinate of the view relative to its parent.
- `layout_alignParentY`: The y-coordinate of the view relative to its parent.

### Example Use Case

The following example demonstrates how to use a `Layout Relative Layout` to arrange two views:

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <GridLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_margin="16dp"
        android:columnCount="2">

        <Button
            android:id="@+id/btn1"
            android:layout_columnWeight="1"
            android:layout_rowWeight="1"
            android:text="Button 1" />

        <Button
            android:id="@+id/btn2"
            android:layout_columnWeight="1"
            android:layout_rowWeight="1"
            android:text="Button 2" />

    </GridLayout>

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Button 3" />

</LinearLayout>
```

### Table Layout

A `Table Layout` is a layout where views are arranged in a table-like structure. It is used to create complex layouts with multiple rows and columns.

### Table Layout Components

The following components are used in a `Table Layout`:

- `TableRow`: A row in the table.
- `TableLayout`: The root view of the layout.
- `TextView`: A view that can be added to the table.
- `Button`: A view that can be added to the table.

### Table Layout Attributes

The following attributes are used in a `Table Layout`:

- `layout_width`: The width of the view.
- `layout_height`: The height of the view.
- `tableLayout_width`: The width of the table layout.
- `tableLayout_height`: The height of the table layout.

### Example Use Case

The following example demonstrates how to use a `Table Layout` to arrange three views:

```xml
<?xml version="1.0" encoding="utf-8"?>
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
            android:text="Column 1"
            android:layout_columnWeight="1" />

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:text="Column 2"
            android:layout_columnWeight="1" />

    </TableRow>

    <TableRow
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:text="Row 1 Column 1"
            android:layout_columnWeight="1" />

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:text="Row 1 Column 2"
            android:layout_columnWeight="1" />

    </TableRow>

    <TableRow
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:text="Row 2 Column 1"
            android:layout_columnWeight="1" />

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:text="Row 2 Column 2"
            android:layout_columnWeight="1" />

    </TableRow>

</TableLayout>
```

## Constraint Layout

---

A `Constraint Layout` is a layout where views are arranged based on constraints. It is used to create complex layouts with multiple constraints and is the recommended layout type for Android versions 21 and later.

### Constraint Layout Components

The following components are used in a `Constraint Layout`:

- `ConstraintLayout`: The root view of the layout.
- `View`: A view that can be added to the layout.
- `Constraint`: A constraint that defines the relationship between a view and its parent or other views.

### Constraint Layout Attributes

The following attributes are used in a `Constraint Layout`:

- `layout_width`: The width of the view.
- `layout_height`: The height of the view.
- `constraintLayout_anchorsToParent`: The anchor point of the view relative to its parent.
- `constraintLayout_anchorsToPrevious`: The anchor point of the view relative to its previous sibling.
- `constraintLayout_anchorsToNext`: The anchor point of the view relative to its next sibling.

### Example Use Case

The following example demonstrates how to use a `Constraint Layout` to arrange two views:

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <Button
        android:id="@+id/btn1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Button
        android:id="@+id/btn2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:layout_constraintBottom_toBottomOf="@id/btn1"
        app:layout_constraintLeft_toRightOf="@id/btn1"
        app:layout_constraintRight_toRightOf="@id/btn1" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

## Conclusion

---

In this topic, we have covered the `Layout Relative Layout` and its variations, including `Table Layout` and `Constraint Layout`. We have discussed the historical context, modern developments, and covered the components, attributes, and example use cases for each layout type.

## Further Reading

---

- [Android Developer Documentation: Layouts](https://developer.android.com/guide/topics/ui/layout)
- [Android Developer Documentation: Constraint Layout](https://developer.android.com/guide/topics/ui/ui-layout)
- [Android Developer Documentation: Table Layout](https://developer.android.com/guide/topics/ui/table-layout)
- [Android Developer Documentation: GridLayout](https://developer.android.com/guide/topics/ui/layout/grid)

Note: The above content is a detailed and comprehensive guide to the `Layout Relative Layout` and its variations. It is intended to provide a thorough understanding of the topic and is not limited to a specific version of the Android operating system.
