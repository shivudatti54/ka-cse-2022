# **5 Implement Functions: Count – Sort – Limit – Skip – Aggregate using MongoDB**

## **Introduction**

In this section, we will explore five essential functions in MongoDB for analyzing and manipulating data: Count, Sort, Limit, Skip, and Aggregate. These functions enable us to perform various tasks such as data summarization, data sorting, data pagination, and data transformation.

## **Count Function**

The Count function is used to count the number of documents that match a specific condition.

### Syntax:

```sql
db.collection.countDocuments({ query })
```

### Example:

```sql
db.customers.countDocuments({ country: "USA" })
```

This will return the number of customers from the "USA".

### Key Concepts:

- `db.collection`: specifies the collection to query
- `countDocuments()`: counts the number of documents in the collection or the matching subset of documents
- `{ query }`: specifies the query for the Count function

## **Sort Function**

The Sort function is used to sort the documents in a collection based on specific fields.

### Syntax:

```sql
db.collection.sort({ field: 1 })
```

### Example:

```sql
db.customers.sort({ name: 1 })
```

This will sort the customers collection by the "name" field in ascending order.

### Key Concepts:

- `db.collection`: specifies the collection to query
- `sort()`: sorts the documents in the collection or the matching subset of documents
- `{ field }`: specifies the field to sort by
- `1` (or `-1`): specifies the sort order (ascending or descending)

## **Limit Function**

The Limit function is used to limit the number of documents returned.

### Syntax:

```sql
db.collection.limit(n)
```

### Example:

```sql
db.customers.limit(10)
```

This will return the first 10 customers from the collection.

### Key Concepts:

- `db.collection`: specifies the collection to query
- `limit(n)`: returns a subset of the documents in the collection or the matching subset of documents
- `n`: specifies the number of documents to return

## **Skip Function**

The Skip function is used to skip a specified number of documents before returning the remaining documents.

### Syntax:

```sql
db.collection.skip(n)
```

### Example:

```sql
db.customers.skip(5)
```

This will return the remaining 5 customers from the collection, starting from the 6th customer.

### Key Concepts:

- `db.collection`: specifies the collection to query
- `skip(n)`: skips the first `n` documents in the collection or the matching subset of documents
- `n`: specifies the number of documents to skip

## **Aggregate Function**

The Aggregate function is used to perform complex operations on the documents in a collection.

### Syntax:

```sql
db.collection.aggregate([
  {
    $match: { query }
  },
  {
    $sort: { field: 1 }
  },
  {
    $limit: n
  }
])
```

### Example:

```sql
db.customers.aggregate([
  {
    $match: { country: "USA" }
  },
  {
    $sort: { name: 1 }
  },
  {
    $limit: 10
  }
])
```

This will return the first 10 customers from the USA, sorted by name in ascending order.

### Key Concepts:

- `db.collection`: specifies the collection to query
- `aggregate()`: performs a pipeline of operations on the documents in the collection or the matching subset of documents
- `$match()`: matches the documents based on a query
- `$sort()`: sorts the documents based on a field
- `$limit()`: limits the number of documents to return

## **Developing Pig Latin Scripts to Sort**

In Pig Latin, we can develop scripts to sort data using the following basic structure:

```pig
sort_data = foreach (A as item) {
    item_name = item.name;
    item_name_sort = item_name | sort;
    output = (item_name_sort, item);
}
```

Here's an example of how to sort a list of customers by name in Pig Latin:

```pig
data = (
    "John", "USA", "New York"
    "Alice", "Canada", "Toronto"
    "Bob", "USA", "Los Angeles"
);

sort_data = foreach (data) {
    item_name = $0;
    item_country = $1;
    item_city = $2;
    item_name_sort = $0 | sort;
    output = (item_name_sort, item_country, item_city);
}

result = group sort_data {
    $key = $0;
} by ($1);
```

This will output the sorted list of customers:

```
("Alice", "Canada", "Toronto")
("Bob", "USA", "Los Angeles")
("John", "USA", "New York")
```

## **Conclusion**

In this section, we explored five essential functions in MongoDB for analyzing and manipulating data: Count, Sort, Limit, Skip, and Aggregate. We also developed Pig Latin scripts to sort data. By mastering these functions and scripts, you can efficiently analyze and manipulate large datasets in MongoDB.
