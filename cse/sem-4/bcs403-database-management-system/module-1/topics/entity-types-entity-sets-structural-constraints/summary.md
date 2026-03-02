# Entity Types, Entity Sets, and Structural Constraints - Summary

## Key Definitions and Concepts

- **Entity**: A real-world object or concept that can be distinctly identified (e.g., a specific student, employee, product)

- **Entity Type**: A collection or schema of entities that share common characteristics, defining the structure and attributes (e.g., STUDENT, EMPLOYEE)

- **Entity Set**: The actual collection of entities of a particular type at a specific point in time (the population of entities)

- **Attributes**: Properties or characteristics of entity types - classified as simple (atomic), composite, single-valued, multi-valued, and derived

- **Key**: An attribute or set of attributes that uniquely identifies each entity (primary key, candidate key, superkey)

## Important Formulas and Theorems

- **Cardinality Ratios**: One-to-One (1:1), One-to-Many (1:N), Many-to-Many (M:N)
- **Participation Constraints**: Total participation (mandatory) and Partial participation (optional)
- **Key Hierarchy**: Superkey ⊇ Candidate Key ⊇ Primary Key

## Key Points

1. Entity type is the schema/structure, while entity set is the instance/data population

2. Primary key cannot have null values and must have unique values

3. Multi-valued attributes are represented by double ovals; derived attributes by dashed ovals in ER diagrams

4. In 1:N relationships, the primary key of the "one" side becomes a foreign key in the "many" side

5. Total participation is represented by double lines in ER diagrams

6. M:N relationships cannot be implemented directly and require a junction/bridge table

7. Weak entities have partial keys and depend on strong entities for identification

8. Composite attributes are broken down into simple components for storage

9. Candidate keys are minimal superkeys - no proper subset can be a superkey

10. The ER model provides a visual representation for database design before implementation

## Common Mistakes to Avoid

1. Confusing entity type with entity set - they are not interchangeable terms

2. Forgetting that multi-valued attributes cannot be decomposed further during normalization

3. Incorrectly identifying participation constraints from business scenarios

4. Selecting non-minimal attributes as candidate keys

5. Trying to implement M:N relationships directly without a junction table

## Revision Tips

1. Practice drawing ER diagrams for at least 5 different real-world scenarios

2. Memorize the Chen's notation symbols for all elements (rectangles, ovals, diamonds)

3. Focus on identifying keys from given business descriptions - this is frequently asked in exams

4. Review previous university question papers to understand the pattern of questions on this topic

5. Create flashcards for key definitions and draw quick ER diagrams to reinforce learning
