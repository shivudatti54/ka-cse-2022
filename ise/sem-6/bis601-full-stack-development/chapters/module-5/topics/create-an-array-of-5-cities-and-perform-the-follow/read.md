# **Create an Array of 5 Cities and Perform Operations**

## **Introduction**

In this study material, we will learn how to create an array of 5 cities in MongoDB and perform various operations on it. We will cover the basics of arrays in MongoDB, how to create and manipulate them, and how to log the total number of cities.

## **What are Arrays in MongoDB?**

In MongoDB, an array is a data structure that stores a collection of values of the same data type. Arrays can contain different data types, including strings, integers, and objects.

## **Creating an Array of Cities**

To create an array of cities, we can use the `$set` operator in the MongoDB shell. Here's an example:

```markdown
// Create a new database called "cities"
use cities

// Create a new collection called "cities"
db.createCollection("cities", {
validator: {
$jsonSchema: {
required: ["name", "country"],
properties: {
name: {
type: "string"
},
country: {
type: "string"
}
}
}
}
})

// Create an array of 5 cities
db.cities.insertMany([
{
name: "New York",
country: "USA"
},
{
name: "London",
country: "UK"
},
{
name: "Paris",
country: "France"
},
{
name: "Tokyo",
country: "Japan"
},
{
name: "Sydney",
country: "Australia"
}
])

// Log the total number of cities
db.cities.countDocuments()
```

In this example, we create a new collection called "cities" and insert an array of 5 cities into it. We then log the total number of cities using the `countDocuments()` method.

## **Performing Operations on the Array**

Once we have created the array of cities, we can perform various operations on it. Here are a few examples:

### 1. Getting the First Element of the Array

To get the first element of the array, we can use the `$elementAt()` operator:

```markdown
// Get the first element of the array
db.cities.findOne({
\_id: 0
})
```

In this example, we use the `$elementAt()` operator to get the first element of the array. The `_id` field is used to specify the index of the element to retrieve.

### 2. Getting the Last Element of the Array

To get the last element of the array, we can use the `$elementAt()` operator with a negative index:

```markdown
// Get the last element of the array
db.cities.findOne({
\_id: -1
})
```

In this example, we use the `$elementAt()` operator with a negative index to get the last element of the array.

### 3. Updating the First Element of the Array

To update the first element of the array, we can use the `$set()` operator:

```markdown
// Update the first element of the array
db.cities.updateOne({
\_id: 0
}, {
$set: {
name: "New York City"
}
})
```

In this example, we use the `$set()` operator to update the first element of the array. We set the `name` field to "New York City".

### 4. Removing the First Element of the Array

To remove the first element of the array, we can use the `$pull()` operator:

```markdown
// Remove the first element of the array
db.cities.deleteOne({
\_id: 0
})
```

In this example, we use the `$pull()` operator to remove the first element of the array.

## **Conclusion**

In this study material, we learned how to create an array of 5 cities in MongoDB and perform various operations on it. We covered the basics of arrays in MongoDB, how to create and manipulate them, and how to log the total number of cities. We also covered some common operations that can be performed on arrays, including getting the first and last elements, updating and removing elements, and counting the number of elements.
