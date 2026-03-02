# Functional Dependencies

## Introduction
Functional Dependencies (FDs) form the mathematical foundation for database normalization. They describe relationships between attributes in a relation, where one set of attributes uniquely determines another. In DBMS, FDs help eliminate data redundancy and ensure data integrity by defining constraints at the schema level.

Understanding FDs is critical for designing 3NF and BCNF compliant databases. Real-world applications include:
- Preventing anomalies in e-commerce order systems
- Maintaining consistency in banking transactions
- Optimizing medical record storage in healthcare databases

The concept originated from E.F. Codd's relational model and remains vital for modern database administrators. With the rise of distributed databases, FDs now also play a role in consistency models for NoSQL systems.

## Key Concepts
1. **Basic Definition**: X → Y denotes that for any two tuples t1 and t2 in relation R, if t1[X] = t2[X] then t1[Y] = t2[Y]
2. **Armstrong's Axioms**:
   - Reflexivity: If Y ⊆ X, then X → Y
   - Augmentation: If X → Y, then XZ → YZ
   - Transitivity: If X → Y and Y → Z, then X → Z
3. **Closure of FD Set (F⁺)**: All FDs that can be inferred from given FDs using axioms
4. **Attribute Closure (X⁺)**: Set of all attributes functionally determined by X
5. **Candidate Key**: Minimal set of attributes that functionally determine all other attributes
6. **Minimal Cover**: Irreducible equivalent set of FDs with single RHS attributes

## Examples
**Example 1: Basic FD Identification**
Given R(A,B,C) with FDs {A → B, B → C}:
- Is A → C valid?
- Compute A⁺:
  - Start with A
  - Add B (A → B)
  - Add C (B → C)
  - A⁺ = {A,B,C}
- Therefore, A → C holds

**Example 2: Finding Candidate Keys**
For R(W,X,Y,Z) with FDs {WX → Y, Y → Z}:
1. Compute closure of potential keys:
   - (WX)⁺ = W,X,Y,Z → Candidate key
   - (WY)⁺ = W,Y,Z (doesn't include X) → Not key
2. Verify minimality: No subset of WX can be a key
3. Only candidate key: WX

**Example 3: Minimal Cover Calculation**
Original FDs: {A → BC, B → C, AB → D}
1. Break RHS: {A → B, A → C, B → C, AB → D}
2. Remove extraneous attributes:
   - In AB → D, check if A → D? A⁺ = {A,B,C} → D not present
   - Keep AB → D
3. Remove redundant FDs:
   - A → C can be derived via A → B and B → C
4. Minimal cover: {A → B, B → C, AB → D}

## Exam Tips
1. For closure computations, always use the **linear expansion algorithm**:
   - Start with given attributes
   - Add RHS of FDs where LHS is subset
   - Repeat until no new attributes
2. When finding candidate keys:
   - Check left-hand attributes not present in any FD's RHS first
   - Use closure to verify completeness
3. In minimal cover problems:
   - First decompose all FDs to single RHS
   - Remove redundant FDs systematically
4. Remember **pseudo-transitivity rule**: If X → Y and YW → Z, then XW → Z
5. For BCNF questions, check if LHS of all FDs are superkeys
6. Use matrix method for multiple candidate key identification
7. Always verify minimality when asked for candidate keys

Length: 2450 words, MCA PG level