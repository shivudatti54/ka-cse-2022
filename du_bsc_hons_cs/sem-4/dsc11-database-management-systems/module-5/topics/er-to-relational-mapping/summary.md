# ER to Relational Mapping

## Introduction

**Entity-Relationship (ER) to Relational Mapping** is the process of converting an ER diagram into a relational database schema. This transformation is fundamental to database design, as it bridges the conceptual design phase with the logical implementation phase. For the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus, this topic is essential under the Database Management Systems course, specifically targeting how abstract entity-relationship models are translated into concrete relational tables that can be implemented in RDBMS.

---

## Key Concepts

### 1. Mapping Entities

- **Regular Entities**: Each strong entity type becomes a relation (table). The primary key of the entity becomes the primary key of the relation.
- **Weak Entities**: A weak entity is mapped by creating a relation that includes the primary key of the owner entity as a foreign key. The composite key (owner's key + partial key) becomes the primary key.

### 2. Mapping Relationships

- **Binary 1:1 Relationships**: Can be mapped by including the primary key of one entity as a foreign key in the other, or by creating a separate relation containing both entities' primary keys.
- **Binary 1:N Relationships**: Mapped by including the primary key of the "one" side entity as a foreign key in the relation representing the "many" side entity.
- **Binary M:N Relationships**: Mapped by creating a new relation (association table) that includes the primary keys of both participating entities as foreign keys. The combination of these keys forms the primary key.

### 3. Mapping Attributes

- **Simple Attributes**: Directly become columns in the relation.
- **Composite Attributes**: Only the simple (leaf) attributes are included; the composite structure is flattened.
- **Multivalued Attributes**: These are mapped by creating a separate relation that includes the multivalued attribute along with the primary key of the original entity.

### 4. Mapping Specialization/Generalization

- **Option 1 (Single Relation)**: Create one relation with all attributes from superclass and subclasses, plus a type attribute to identify subclass membership.
- **Option 2 (Multiple Relations)**: Create separate relations for the superclass and each subclass. The superclass key serves as the primary key in subclass relations.

---

## Conclusion

ER to Relational Mapping is a systematic process that transforms conceptual database designs into implementable relational schemas. Mastery of mapping rules for entities, relationships, attributes, and specialization hierarchies is crucial for designing efficient databases. This topic forms the backbone of practical database development and is a frequently examined area in the Delhi University BSc Computer Science curriculum under the NEP 2024 UGCF framework. Students should practice converting various ER diagrams into relational schemas to gain proficiency in this essential database design technique.