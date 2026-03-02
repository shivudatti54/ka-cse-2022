cypher
// Create a Person node with properties
CREATE (p:Person {name: 'Tom Hanks', born: 1956})

// Create a Movie node
CREATE (m:Movie {title: 'Forrest Gump', released: 1994})

// Create a relationship between them
MATCH (p:Person {name: 'Tom Hanks'}), (m:Movie {title: 'Forrest Gump'})
CREATE (p)-[r:ACTED_IN {roles: ['Forrest']}]->(m)
RETURN p, r, m
