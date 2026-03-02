# **Linear Algebra Revision Notes**

## **Introduction**

- A vector space is a set of vectors that is closed under addition and scalar multiplication.
- A subset of a vector space is called a subspace if it is closed under addition and scalar multiplication.
- A dimension of a vector space is the number of vectors in a basis for the space.

## **Vector Spaces**

- Definition: A set of vectors that is closed under addition and scalar multiplication.
- Properties:
  - Commutative Property of Addition
  - Associative Property of Addition
  - Distributive Property of Scalar Multiplication over Vector Addition
  - Existence of Additive Identity (zero vector)
  - Existence of Additive Inverse (negative vector)

## **Subspaces**

- Definition: A subset of a vector space that is closed under addition and scalar multiplication.
- Properties:
  - Trivial Subspace: The set containing only the zero vector.
  - Span: The set of all linear combinations of vectors in the subspace.

## **Linear Combinations**

- A linear combination of vectors is a linear combination of scalar multiples of those vectors.
- Example: `a * v1 + b * v2`

## **Linear Span**

- The set of all linear combinations of vectors in a vector space.
- Example: The set of all linear combinations of the columns of a matrix.

## **Row Space and Column Space**

- Row Space: The span of the rows of a matrix.
- Column Space: The span of the columns of a matrix.

## **Linear Dependence and Independence**

- Linear dependence: A set of vectors is linearly dependent if one vector can be expressed as a linear combination of the others.
- Linear independence: A set of vectors is linearly independent if none of the vectors can be expressed as a linear combination of the others.

## **Key Formulas and Theorems**

- **Frobenius Formula**: `rank(A) = dim(R(A)) = dim(C(A))`
- **Row Echelon Form**: A matrix in row echelon form is a matrix where all rows consisting entirely of zeros are grouped at the bottom.
- **Column Echelon Form**: A matrix in column echelon form is a matrix where all columns consisting entirely of zeros are grouped at the left.
- **Gaussian Elimination**: A method for transforming a matrix into row echelon form.
