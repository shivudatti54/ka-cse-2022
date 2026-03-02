# Layout Relative Layout – Table Layout - Summary

## Key Definitions and Concepts

- **RelativeLayout**: Positions child views relative to each other or parent container using alignment rules
- **TableLayout**: Organizes views into rows/columns using `<TableRow>` elements (subclass of LinearLayout)
- **Alignment Attributes**: `android:layout_alignParentTop`, `layout_toRightOf`, etc. (RelativeLayout)
- **Spanning Columns**: `android:layout_span` merges table cells horizontally (TableLayout)
- **WeightSum**: `android:weightSum` distributes space proportionally in layouts

## Important Formulas and Theorems

```xml
<!-- RelativeLayout Alignment -->
android:layout_centerInParent="true"
android:layout_below="@+id/element_id"

<!-- TableLayout Column Control -->
android:stretchColumns="*"  // Expands columns to fill width
android:shrinkColumns="1"   // Allows column 1 to shrink

<!-- Weight Distribution -->
android:layout_weight="1"   // Works with weightSum for proportional sizing
```

## Key Points

1. **RelativeLayout Advantages**:
   - Reduces nested views compared to LinearLayout
   - Enables complex positioning without fixed coordinates
   - Uses 20+ alignment attributes for precise control

2. **TableLayout Best Practices**:
   - Use `<TableRow>` for each row
   - Combine with `layout_span` for merged cells
   - Avoid deep nesting - limits to 10-12 rows for performance

3. **Common Use Cases**:
   - RelativeLayout: Forms, floating action buttons, overlay elements
   - TableLayout: Data grids, pricing tables, keyboard-like interfaces

4. **Performance Considerations**:
   - RelativeLayout requires 2 measurement passes
   - TableLayout becomes inefficient with >20 rows
   - Use ConstraintLayout for complex modern UIs

5. **XML Structure**:

   ```xml
   <RelativeLayout>
       <Button android:id="@+id/btn1"/>
       <Button android:layout_below="@id/btn1"/>
   </RelativeLayout>

   <TableLayout>
       <TableRow>
           <TextView android:text="Cell 1"/>
           <TextView android:text="Cell 2"/>
       </TableRow>
   </TableLayout>
   ```

## Common Mistakes to Avoid

1. Confusing TableLayout with GridLayout (TableLayout uses rows, GridLayout uses columns first)
2. Overusing alignment rules in RelativeLayout causing overlapping views
3. Forgetting to set `android:layout_width/height` in child elements
4. Using TableLayout for non-tabular data (prefer LinearLayout/ConstraintLayout)

## Revision Tips

1. **Practice XML Snippets**: Memorize 5 key RelativeLayout attributes and 3 TableLayout attributes
2. **Compare Layout Types**: Make a table comparing Linear/Relative/Table layouts
3. **Use Design Preview**: Test layouts in Android Studio's split view
4. **Exam Focus**: Expect questions on:
   - Choosing between Relative/Table layouts
   - Writing XML for specific UI patterns
   - Performance implications of nested layouts
