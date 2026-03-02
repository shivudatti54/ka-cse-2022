javascript
// Insert a single document into a 'users' collection
db.users.insertOne({
    name: "Alice",
    age: 27,
    email: "alice@example.com",
    address: {
        city: "Bengaluru",
        state: "KA"
    },
    hobbies: ["coding", "music"]
});