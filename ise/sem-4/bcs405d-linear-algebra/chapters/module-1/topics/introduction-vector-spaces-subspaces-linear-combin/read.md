# **Linear Algebra: Vector Spaces**

## **Introduction**

Linear algebra is a branch of mathematics that deals with the study of linear equations, linear transformations, and vector spaces. Vector spaces are the foundation of linear algebra, and understanding them is crucial for further study in this field.

## **Definition of a Vector Space**

A vector space is a set of vectors that satisfies certain properties:

- **Closure under addition**: For any two vectors `u` and `v` in the vector space, their sum `u + v` is also in the vector space.
- **Closure under scalar multiplication**: For any vector `u` in the vector space and any scalar `c`, the product `cu` is also in the vector space.
- **Commutativity of addition**: For any two vectors `u` and `v` in the vector space, `u + v = v + u`.
- **Associativity of addition**: For any three vectors `u`, `v`, and `w` in the vector space, `(u + v) + w = u + (v + w)`.
- **Existence of additive identity**: There exists a vector `0` in the vector space such that for any vector `u` in the vector space, `u + 0 = u`.
- **Existence of additive inverse**: For any vector `u` in the vector space, there exists a vector `-u` in the vector space such that `u + (-u) = 0`.

## **Key Concepts**

- **Vector**: A geometric object that has both magnitude and direction.
- **Scalar**: A number that can be multiplied with a vector to give another vector.
- **Addition**: The operation of combining two or more vectors to give another vector.
- **Scalar multiplication**: The operation of multiplying a vector with a scalar to give another vector.

## **Subspaces**

A subspace of a vector space `V` is a subset of `V` that is closed under addition and scalar multiplication.

- **Example**: The set of all vectors with zero coordinates is a subspace of `R^2`.
- **Properties of subspaces**:
  - The zero vector is a subspace of any vector space.
  - The set of all vectors in `V` is a subspace of `V`.
  - The sum of two subspaces is a subspace.
  - The product of a subspace and a scalar is a subspace.

## **Linear Combinations**

A linear combination of vectors is an expression of the form `a_1v_1 + a_2v_2 + ... + a_nv_n`, where `v_1`, `v_2`, ..., `v_n` are vectors in a vector space `V` and `a_1`, `a_2`, ..., `a_n` are scalars.

- **Example**: The expression `2v_1 + 3v_2` is a linear combination of `v_1` and `v_2`.

## **Linear Span**

The linear span of a set of vectors is the set of all linear combinations of those vectors.

- **Example**: The linear span of the vectors `v_1` and `v_2` is the set of all expressions of the form `a_1v_1 + a_2v_2`, where `a_1` and `a_2` are scalars.

## **Row Space and Column Space**

The row space and column space of a matrix `A` are the sets of all linear combinations of the rows and columns of `A`, respectively.

- **Row space**: The row space of `A` is the set of all linear combinations of the rows of `A`.
- **Column space**: The column space of `A` is the set of all linear combinations of the columns of `A`.
- **Example**: The row space of the matrix `A = [1 2; 3 4]` is the set of all linear combinations of the rows `[1 2]^T` and `[3 4]^T`.

## **Linear Dependence and Independence**

A set of vectors is said to be linearly dependent if there exists a non-trivial linear combination of the vectors that equals the zero vector. Otherwise, the set is linearly independent.

- **Example**: The set of vectors `[1 0]^T`, `[0 1]^T`, and `[1 1]^T` is linearly independent.
- **Properties of linear dependence and independence**:
  - A set of vectors is linearly dependent if and only if the vectors are not linearly independent.
  - The dimension of a vector space is equal to the maximum number of linearly independent vectors in the space.

## **Key Terms**

- **Linear transformation**: A function that takes a vector to another vector, while preserving the operations of vector addition and scalar multiplication.
- ** Basis**: A set of linearly independent vectors that span a vector space.
- ** Span**: The set of all linear combinations of a set of vectors.

## **Exercises**

1. Determine whether the following sets of vectors are linearly independent or dependent.

- `[1 0]^T`, `[0 1]^T`
- `[1 0 0]^T`, `[0 0 1]^T`, `[0 0 0]^T`

2. Find the linear span of the set of vectors `[1 2]^T`, `[3 4]^T`.
3. Determine the row space and column space of the matrix `A = [1 2; 3 4]`.
