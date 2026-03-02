# **Performance Pandas: eval and query Chapter 22 Summary**

## **Key Points**

- **eval function**:
  - Evaluates a string as a Python expression
  - Can be slow for complex expressions due to Python's interpretation overhead
  - Example: `df['column'] = df.eval('column * 2')`
- **query function**:
  - Filters a DataFrame based on a string query
  - Uses a more efficient algorithm than eval, especially for complex queries
  - Example: `df.query('column > 0')`
- **Benefits of query over eval**:
  - Faster execution times
  - More readable and maintainable code
  - Less prone to errors due to Python's interpretation overhead

## **Important Formulas and Definitions**

- **Numpy trick**: Use `np.where` or `np.select` for vectorized operations, which can be faster than using eval
- **Vectorized string operations**: Use `str` accessor methods (e.g., `str.contains`, `str.replace`) for faster string manipulation

## **Theorems and Concepts**

- **Data alignment**: Ensure that the input strings to eval or query are aligned with the DataFrame's columns
- **Caching**: Consider caching the results of expensive eval or query operations to avoid repeated computations

## **Revision Tips**

- Practice using eval and query functions with simple examples
- Familiarize yourself with numpy's vectorized string operations
- Optimize your code by using query instead of eval for complex queries
- Regularly test and benchmark your code to ensure optimal performance
