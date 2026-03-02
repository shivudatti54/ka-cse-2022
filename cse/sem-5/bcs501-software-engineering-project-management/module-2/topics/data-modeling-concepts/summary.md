# Data Modeling Concepts - Summary

## Key Definitions

- **Entity**: A distinguishable object in the application domain with independent existence and unique identification
- **Attribute**: A characteristic or property describing an entity or relationship
- **Key Attribute**: An attribute or combination of attributes that uniquely identifies each entity instance
- **Relationship**: An association connecting two or more entities representing meaningful business connections
- **Cardinality**: The numeric specification of how many instances of one entity associate with instances of another entity
- **Participation Constraint**: Specification determining whether entity existence requires relationship participation (total) or allows optional participation (partial)
- **Weak Entity**: An entity that depends on a strong entity for identification and lacks a complete primary key
- **Associative Entity**: An entity created to resolve many-to-many relationships, often carrying attributes of the relationship itself

## Important Formulas

- **Composite Key**: When a single attribute cannot uniquely identify entity instances, the combination of multiple attributes forms the key: Key = {attribute₁, attribute₂, ..., attributeₙ}
- **ER to UML Multiplicity Mapping**: 
  - Cardinality 1:1 → Multiplicity "1..1"
  - Cardinality 1:N → Multiplicity "0..*" or "1..*"
  - Cardinality M:N → Multiplicity represented through association class

## Key Points

1. Data modeling in requirements engineering focuses on capturing business meaning and relationships, not on database implementation efficiency
2. Three levels of data abstraction exist: conceptual (stakeholder communication), logical (detailed specification), and physical (implementation-ready)
3. ER modeling employs entities, attributes, and relationships as primary building blocks for representing data requirements
4. Cardinality specifies relationship numbers (1:1, 1:N, M:N) while participation specifies optionality (total or partial)
5. Weak entities require identification through owning strong entity plus their own partial identifier
6. Many-to-many relationships with attributes must transform into associative entities
7. Recursive relationships require role names to clarify participation directions
8. Data models provide essential foundation for class-based modeling and use case elaboration

## Common Mistakes

1. Confusing cardinality with participation—cardinality addresses "how many" while participation addresses "whether required"
2. Creating weak entities unnecessarily when the entity possesses sufficient attributes for unique identification
3. Failing to transform M:N relationships with attributes, instead attempting to attach attributes to either participating entity
4. Omitting role names in recursive relationships, causing ambiguity in self-referential associations
5. Conflating conceptual and logical models by including implementation-specific details too early in requirements analysis