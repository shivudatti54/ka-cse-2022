# Cartesian Products and Relations

### Revision Notes

#### Definitions and Notations

- Cartesian Product: The set of all ordered pairs $(a, b)$ where $a$ is an element of set $A$ and $b$ is an element of set $B$. Notation: $A \times B$
- Relation: A subset of the Cartesian product $A \times B$, denoted as $R \subseteq A \times B$

#### Formulas and Notations

- Cartesian Product: $(A \times B) \times C = A \times (B \times C)$
- Relation: $R \circ S = \{(a, c) | \exists b \in B, (a, b) \in S \text{ and } (b, c) \in R\}$

#### Important Theorems

- **Reflexivity**: A relation $R$ on a set $A$ is reflexive if $(a, a) \in R$ for all $a \in A$.
- **Symmetry**: A relation $R$ on a set $A$ is symmetric if $(a, b) \in R$ implies $(b, a) \in R$ for all $a, b \in A$.
- **Transitivity**: A relation $R$ on a set $A$ is transitive if $(a, b) \in R$ and $(b, c) \in R$ implies $(a, c) \in R$ for all $a, b, c \in A$.

#### Properties of Relations

- **Equivalence Relation**: A relation $R$ on a set $A$ is an equivalence relation if it is reflexive, symmetric, and transitive.
- **Partial Order**: A relation $R$ on a set $A$ is a partial order if it is reflexive, antisymmetric, and transitive.

#### Important Concepts

- **Ordering on a Set**: A relation $R$ on a set $A$ is an ordering if it is a partial order and any two elements of $A$ are comparable.
- **Order Type**: The order type of a set $A$ is a function from the natural numbers to the set of order types of the elements of $A$.
