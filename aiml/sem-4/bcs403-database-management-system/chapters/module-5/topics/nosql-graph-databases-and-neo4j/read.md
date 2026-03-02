cypher
// Create Person nodes with properties
CREATE (alice:Person {name: 'Alice', age: 30})
CREATE (bob:Person {name: 'Bob', age: 32})

// Create a directed FRIENDS_WITH relationship from Alice to Bob
CREATE (alice)-[:FRIENDS_WITH {since: '2022-01-01'}]->(bob)