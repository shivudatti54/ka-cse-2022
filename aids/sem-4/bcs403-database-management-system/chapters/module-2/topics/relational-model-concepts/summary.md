# Relational Model Concepts - Summary

## Key Definitions and Concepts

- **Relation**: A two-dimensional table with rows (tuples) and columns (attributes), representing a mathematical set of tuples.
- **Tuple**: A single row in a relation, representing one record of data.
- **Attribute**: A column in a relation, representing a specific characteristic or property.
- **Domain**: The set of all possible values that an attribute can take.
- **Relational Schema**: The logical structure of a relation defining its name and attributes with their domains.
- **Relation Instance**: The actual data (set of tuples) stored in a relation at a given point in time.
- **NULL**: A special marker representing missing or unknown information, distinct from zero or empty string.

## Important Formulas and Theorems

- **Degree of a Relation**: Number of attributes (columns) in a relation.
- **Cardinality of a Relation**: Number of tuples (rows) in a relation at a specific time.
- **Three-valued Logic**: Operations with NULL yield TRUE, FALSE, or UNKNOWN as results.

## Key Points

- The Relational Model was introduced by Edgar F. Codd in 1970 and is based on set theory and predicate logic.
- Five properties of a valid relation: atomic values, unique attribute names, unordered attributes, no duplicate tuples, and homogeneous domains.
- A super key is any attribute set that uniquely identifies tuples; a candidate key is a minimal super key.
- Primary key uniquely identifies tuples within a relation and cannot contain NULL values.
- Foreign key establishes relationships between tables and must satisfy referential integrity constraints.
- Entity integrity ensures primary key uniqueness; referential integrity ensures foreign key validity.
- The relational model serves as the foundation for SQL and all modern RDBMS systems.

## Common Mistakes to Avoid

- Confusing tuple with attribute: tuples are rows, attributes are columns.
- Treating NULL as zero or empty string—NULL represents unknown/missing value.
- Forgetting that primary key cannot be NULL (entity integrity constraint).
- Overlooking minimality when identifying candidate keys—a key must not have redundant attributes.
- Believing attribute order matters in relations—the relational model treats attributes as unordered.

## Revision Tips

- Create a table comparing all key types (super, candidate, primary, foreign) with definitions and examples.
- Practice identifying whether given tables satisfy relation properties, especially atomicity.
- Memorize the integrity constraints and be able to give real-world examples of each.
- Solve previous year DU examination questions on relational model fundamentals.
- Remember: degree = columns (stable), cardinality = rows (changes with insert/delete operations).