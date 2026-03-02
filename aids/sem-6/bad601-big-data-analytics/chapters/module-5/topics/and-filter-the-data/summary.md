# And Filter the Data

## BIG DATA ANALYTICS

### Spark and Big Data Analytics: Spark, Introduction to Data Analysis with Spark

#### Key Points

- **Filtering**: Removing unwanted data to reduce data size and improve analysis efficiency.
- **Filter Conditions**: Using conditions to select specific data based on criteria such as values, ranges, and logical operations.
- **Filter Functions**:
  - `filter()`: Applies a filter condition to each element of a dataset.
  - `filterNot()`: Applies a filter condition to each element of a dataset and returns the opposite result.
- **Filter Types**:
  - `==` (equal to)
  - `!=` (not equal to)
  - `>`, `<`, `>=` , `<=` (greater than, less than, greater than or equal to, less than or equal to)
  - `in` (in a list or array)
  - `like` (pattern matching)
- **Example**:

```scala
val data = Seq(1, 2, 3, 4, 5)
val filteredData = data.filter(_ % 2 == 0)
println(filteredData) // [2, 4]
```

#### Important Formulas, Definitions, Theorems

- **Set Theory**: A set is a collection of unique elements, denoted by curly brackets `{}`.
- **Intersection**: `A ∩ B` is the set of elements common to both sets A and B.
- **Union**: `A ∪ B` is the set of all elements in sets A and B.

#### Quick Revision

- Filtering is an essential step in Big Data Analytics to reduce data size and improve analysis efficiency.
- Use `filter()` and `filterNot()` functions to apply filter conditions to datasets.
- Understand the different filter types, such as `==`, `!=`, `>`, `<`, `>=` , `<=`, `in`, and `like`.
