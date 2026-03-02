json
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "name": "Alice",
  "department": "CSE",
  "address": {  // This is an embedded document
    "street": "123 Main St",
    "city": "Bengaluru"
  },
  "courses": ["Big Data", "Machine Learning"] // An array of values
}