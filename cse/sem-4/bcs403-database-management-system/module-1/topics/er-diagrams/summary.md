# ER Diagrams - Summary

## Key Definitions and Concepts

- **Entity**: A real-world object that can be uniquely identified and about which data is stored
- **Entity Set**: Collection of similar entities sharing common properties
- **Strong Entity**: Entity with its own primary key, independent existence
- **Weak Entity**: Entity dependent on strong entity for identification, has partial key
- **Attribute**: Property or characteristic of an entity
- **Primary Key**: Unique identifier for entity instances, underlined in ER diagrams
- **Foreign Key**: Attribute referencing primary key of another entity
- **Relationship**: Association between entities, represented as diamonds
- **Cardinality**: Number of entities associated in a relationship (1:1, 1:N, M:N)
- **Total Participation**: Mandatory relationship (double line), entity cannot exist without relationship
- **Partial Participation**: Optional relationship (single line), entity may or may not participate
- **Specialization**: Top-down process creating subcategories (IS-A relationship)
- **Generalization**: Bottom-up process combining similar entities into higher-level entity
- **Aggregation**: Treating relationships as entities for higher-level associations

## Important Concepts

- **Attribute Types**: Simple (atomic), Composite (divisible), Single-valued, Multi-valued (double oval), Derived (dashed)
- **Key Types**: Candidate key (minimal), Primary key (selected), Alternate key (unused candidate)
- **Relationship Attributes**: Descriptive properties of the relationship itself
- **Chen Notation**: Standard notation using rectangles for entities, ovals for attributes, diamonds for relationships

## Key Points

- ER diagrams provide abstract representation of real-world data requirements before implementation
- Attributes should be selected based on what data needs to be stored and retrieved
- Multi-valued attributes become separate entities in relational design
- M:N relationships require a separate relation/table in database implementation
- Weak entities are identified by both their own partial key and owner's primary key
- Specialization/generalization use triangles with "ISA" notation
- Cardinality is determined by analyzing business rules and requirements
- Total participation enforces referential integrity at the entity level
- ER diagrams serve as communication tool between designers and stakeholders

## Common Mistakes to Avoid

1. Confusing weak entities with strong entities - remember weak entities need owners
2. Incorrect cardinality determination - always read relationships in both directions
3. Forgetting to underline primary keys in ER diagrams
4. Missing participation constraints - double lines for total, single for partial
5. Treating multi-valued attributes as single-valued in basic ER design
6. Creating relationships between weak entities without including owner entity

## Revision Tips

1. Practice drawing ER diagrams for at least 5-6 different scenarios (University, Banking, Hospital, Library, E-commerce)
2. Memorize standard notation symbols: Rectangle = Entity, Oval = Attribute, Diamond = Relationship
3. Always identify primary keys first before drawing relationships
4. For weak entities, remember to show the identifying relationship (double diamond)
5. Review conversion rules: M:N becomes separate table, 1:N can be migrated, 1:1 can be merged
6. Understand that derived attributes should be shown with dashed lines as they can be computed
7. When answering exam questions, clearly label all components: entities, attributes, keys, relationships, cardinalities
