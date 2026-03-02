# **Summary: 5 Implement Functions in MongoDB and Pig Latin Scripts**

- **Count Function**
  - Returns the number of documents in a collection
  - Formula: db.collection.count()
  - Theorem: The count function is used to determine the number of documents in a collection
- **Sort Function**
  - Sorts documents in a collection in ascending or descending order
  - Formula: db.collection.find().sort({field: 1}) or db.collection.find().sort({field: -1})
  - Definition: Sorting is the process of arranging data in a specific order
- **Limit Function**
  - Returns a specified number of documents from a collection
  - Formula: db.collection.find().limit(num)
  - Definition: Limiting is the process of selecting a subset of data from a larger dataset
- **Skip Function**
  - Returns a specified number of documents from a collection, skipping the first n documents
  - Formula: db.collection.find().skip(n)
  - Definition: Skipping is the process of skipping over certain data in a dataset
- **Aggregate Function**
  - Performs complex operations on data in a collection, such as grouping and sorting
  - Formula: db.collection.aggregate({$group: { \_id: "$field", count: { $sum: 1 } }})
  - Definition: Aggregation is the process of combining data from multiple sources into a single dataset

# **Pig Latin Scripts to Sort**

- **Sort by a Single Field**
  ```pig
  sort_field = 'name';
  sort_order = 1;
  sort_data = filter($sort($fields, $sort_field, $sort_order));

````
*   **Sort by Multiple Fields**
    ```pig
fields = ['name', 'age'];
sort_orders = [1, -1];
sort_data = filter($sort($fields, $sort_orders));
````

- **Sort in Descending Order**
  ```pig
  sort_order = -1;
  sort_data = filter($sort($fields, $sort_order));

```

```
