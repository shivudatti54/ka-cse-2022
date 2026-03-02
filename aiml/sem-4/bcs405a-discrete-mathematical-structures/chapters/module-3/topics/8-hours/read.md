# **Discrete Mathematical Structures**

## **Module: Relations and Functions**

### Topic: Functions

**Definition:** A function is a relation between a set of inputs, called the domain, and a set of possible outputs, called the range. It assigns to each element in the domain exactly one element in the range.

**Notation:** f: A → B, where A is the domain and B is the range.

**Properties of Functions:**

- **Domain:** The set of all possible input values.
- **Range:** The set of all possible output values.
- **Codomain:** The set of all possible output values, including those not in the range.

**Types of Functions:**

- **Constant Function:** f(x) = c, where c is a constant.
- **Identity Function:** f(x) = x.
- **One-to-One Function:** Each element in the range is assigned to by at most one element in the domain.
- **Onto Function:** Each element in the range is assigned to by at least one element in the domain.

**Examples:**

- Define a function f: R → R that maps each real number to its square.
- Define a function f: Z → Z that maps each integer to its double.
- Define a function f: A → B that maps each element in A to a unique element in B, where A and B are sets.

**Key Concepts:**

- **Domain and Range:** The sets of input and output values.
- **Codomain:** The set of all possible output values.
- **One-to-One and Onto Functions:** Functions that assign each element in the range to at most one element in the domain and vice versa.

### Topic: Relations

**Definition:** A relation between two sets is a subset of their Cartesian product. It assigns to each ordered pair (a, b) in the relation either true or false, indicating whether the pair is in the relation or not.

**Notation:** R ⊆ A × B, where A and B are the sets.

**Types of Relations:**

- **Equivalence Relation:** Reflexive, Symmetric, and Transitive.
- **Partial Order:** Reflexive, Anti-Symmetric, and Transitive.
- **Function:** A special type of relation that satisfies the property: for all a and b in the domain, exactly one of the following holds: aRb, bRa, neither.

**Examples:**

- Define a relation R between the set of integers and the set of real numbers that states that two numbers are related if their product is even.
- Define a relation R between the set of integers and the set of integers that states that two numbers are related if their sum is even.

**Key Concepts:**

- **Cartesian Product:** The set of all ordered pairs (a, b), where a is in A and b is in B.
- **Equivalence Relation:** A relation that satisfies the properties: Reflexive, Symmetric, and Transitive.
- **Partial Order:** A relation that satisfies the properties: Reflexive, Anti-Symmetric, and Transitive.

### Topic: Composition of Relations

**Definition:** The composition of two relations R1 and R2 is a relation R1 ∘ R2 between the domains of R1 and R2.

**Notation:** R1 ∘ R2: A × C → B × D, where A is the domain of R1, C is the domain of R2, B is the codomain of R1, and D is the codomain of R2.

**Properties of Composition:**

- **Associative:** (R1 ∘ R2) ∘ R3 = R1 ∘ (R2 ∘ R3).
- **Identity:** The identity relation on a set is the relation that assigns each element to itself.

**Examples:**

- Define two relations R1 and R2 between the set of integers and the set of real numbers.
- Calculate the composition of R1 and R2.

**Key Concepts:**

- **Composition of Relations:** A relation that assigns to each ordered pair (a, c) in the domain of R1 and the codomain of R2, exactly one ordered pair (b, d) in the range of R2 and the domain of R3.
- **Associativity:** The property that (R1 ∘ R2) ∘ R3 = R1 ∘ (R2 ∘ R3).

### Topic: Functions as Relations

**Definition:** A function can be viewed as a relation between the domain and range, where each element in the range is assigned to by at most one element in the domain.

**Notation:** f: A → B, where f is a function and A and B are sets.

**Properties of Functions as Relations:**

- **Injective:** Each element in the range is assigned to by at most one element in the domain.
- **Surjective:** Each element in the range is assigned to by at least one element in the domain.

**Examples:**

- Define a function f: R → R that maps each real number to its square.
- Define a function f: Z → Z that maps each integer to its double.

**Key Concepts:**

- **Function as a Relation:** A relation between the domain and range, where each element in the range is assigned to by at most one element in the domain.
- **Injective and Surjective Functions:** Functions that assign each element in the range to at most one element in the domain and vice versa.

### Topic: Injections and Surjections

**Definition:**

- **Injective Function:** A function that assigns each element in the range to by at most one element in the domain.
- **Surjective Function:** A function that assigns each element in the range to by at least one element in the domain.

**Properties of Injective and Surjective Functions:**

- **Injective Function:** At most one element in the range is assigned to by one element in the domain.
- **Surjective Function:** At least one element in the range is assigned to by one element in the domain.

**Examples:**

- Define a function f: R → R that maps each real number to its square.
- Define a function f: Z → Z that maps each integer to its double.

**Key Concepts:**

- **Injective and Surjective Functions:** Functions that assign each element in the range to by at most one element in the domain and vice versa.
- **One-to-One and Onto Functions:** Functions that satisfy the properties: Injective and Surjective.

### Topic: Equivalence Relations

**Definition:** An equivalence relation on a set A is a relation that satisfies the properties: Reflexive, Symmetric, and Transitive.

**Notation:** R: A → A, where R is an equivalence relation and A is a set.

**Properties of Equivalence Relations:**

- **Reflexive:** For all a in A, aRa.
- **Symmetric:** For all a and b in A, if aRb then bRa.
- **Transitive:** For all a, b, and c in A, if aRb and bRc then aRc.

**Examples:**

- Define an equivalence relation R on the set of integers that states that two numbers are related if they have the same remainder when divided by 4.
- Calculate the equivalence relation on the set of integers that states that two numbers are related if they are congruent modulo 5.

**Key Concepts:**

- **Equivalence Relation:** A relation that satisfies the properties: Reflexive, Symmetric, and Transitive.
- **Congruent Modulo:** Two numbers are congruent modulo n if they have the same remainder when divided by n.

### Topic: Partial Orders

**Definition:** A partial order on a set A is a relation that satisfies the properties: Reflexive, Anti-Symmetric, and Transitive.

**Notation:** R: A → A, where R is a partial order and A is a set.

**Properties of Partial Orders:**

- **Reflexive:** For all a in A, aRa.
- **Anti-Symmetric:** For all a and b in A, if aRb and bRa then a = b.
- **Transitive:** For all a, b, and c in A, if aRb and bRc then aRc.

**Examples:**

- Define a partial order R on the set of integers that states that two numbers are related if one is less than or equal to the other.
- Calculate the partial order on the set of integers that states that two numbers are related if one is a multiple of the other.

**Key Concepts:**

- **Partial Order:** A relation that satisfies the properties: Reflexive, Anti-Symmetric, and Transitive.
- **Less Than or Equal To:** Two numbers are related if one is less than or equal to the other.

### Topic: Linear Orders

**Definition:** A linear order on a set A is a relation that satisfies the properties: Reflexive, Anti-Symmetric, Transitive, and Total.

**Notation:** R: A → A, where R is a linear order and A is a set.

**Properties of Linear Orders:**

- **Reflexive:** For all a in A, aRa.
- **Anti-Symmetric:** For all a and b in A, if aRb and bRa then a = b.
- **Transitive:** For all a, b, and c in A, if aRb and bRc then aRc.
- **Total:** For all a and b in A, either aRb or bRa.

**Examples:**

- Define a linear order R on the set of integers that states that two numbers are related if one is less than the other.
- Calculate the linear order on the set of integers that states that two numbers are related if one is a multiple of the other.

**Key Concepts:**

- **Linear Order:** A relation that satisfies the properties: Reflexive, Anti-Symmetric, Transitive, and Total.
- **Total:** A linear order that is total means that for all a and b in A, either aRb or bRa.
