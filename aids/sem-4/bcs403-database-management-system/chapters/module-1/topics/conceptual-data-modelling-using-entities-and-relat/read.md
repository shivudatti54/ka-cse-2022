# **Conceptual Data Modelling using Entities and Relationships**

## **Entity Types and Entity Sets**

### Definition

- Entity types are the entities that have an identity of their own, meaning they do not rely on other entities for their existence.
- Entity sets are the instances of an entity type.

### Examples

- A company is an entity type (has an identity of its own) and "ABC Inc.", "XYZ Corp." are two entity sets (instances of the company entity type).

### Characteristics

- Entity types have:
  - A name
  - An identity (key)
  - Attributes (data) and/or relationships
- Entity sets have:
  - A unique identifier (instance of the entity type's identity)
  - Attributes (data) and/or relationships

### Structural Constraints

- Structural constraints are rules that define how entities and relationships interact with each other.
- Examples of structural constraints include:
  - Referential integrity (a relationship's left side must contain an entity that exists on the right side)
  - Data integrity (ensures data is accurate and consistent)

### Weak Entity Types

---

### Definition

- Weak entity types are entities that must be associated with a strong entity type.
- Strong entity types are entities that can exist independently.

### Examples

- A customer order is a weak entity type (must be associated with a strong entity type, "Customer") and has attributes "Order ID", "Order Date", etc.

### Characteristics

- Weak entity types have:
  - A dependent relationship with a strong entity type
  - An identifier that depends on the strong entity type's identifier
- Strong entity types have:
  - An independent existence
  - An identifier that can be used to uniquely identify the weak entity

### ER Diagrams

---

### Definition

- Entity-Relationship (ER) diagrams are visual representations of the relationships between entities and their attributes.
- ER diagrams consist of entities, attributes, and relationships.

### Components

- Entities: represented as rectangles
- Attributes: represented as columns within the rectangle
- Relationships: represented as lines connecting entities

### Examples

- A simple ER diagram for a company might include:
  - Entity: Company (rectangle)
  - Entity: Employee (rectangle)
  - Relationship: Employee works for Company (line connecting rectangles)
  - Attributes:
    - Company: Company Name, Company Address
    - Employee: Employee Name, Job Title

### Specificity

---

### Definition

- Specificity is the degree to which an entity is distinct from other entities.
- Specific entities have more distinct characteristics.

### Examples

- A specific employee might have:
  - A specific job title
  - A specific department
  - A specific manager
