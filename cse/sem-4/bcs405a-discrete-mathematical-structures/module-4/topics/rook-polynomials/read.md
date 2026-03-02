# Rook Polynomials

## Table of Contents

- [Rook Polynomials](#rook-polynomials)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Board Representation](#board-representation)
  - [Rook Numbers](#rook-numbers)
  - [Rook Polynomial Definition](#rook-polynomial-definition)
  - [Board Splitting Theorem](#board-splitting-theorem)
  - [Relation with Inclusion-Exclusion](#relation-with-inclusion-exclusion)
- [Examples](#examples)
  - [Example 1: Simple 2×2 Complete Board](#example-1-simple-22-complete-board)
  - [Example 2: L-Shaped Board](#example-2-l-shaped-board)
  - [Example 3: Using Board Splitting Theorem](#example-3-using-board-splitting-theorem)
- [Exam Tips](#exam-tips)

## Introduction

Rook polynomials are a powerful combinatorial tool used to solve counting problems involving non-attacking placements of rooks on a chessboard. Named after the chess piece "rook" (or castle), these polynomials provide an elegant way to count the number of ways to place non-attacking rooks on various board configurations. This topic connects deeply with the principle of inclusion-exclusion and has significant applications in combinatorics, particularly in solving arrangement problems with restrictions.

The study of rook polynomials was formalized in the mid-20th century and has since become an essential topic in discrete mathematics. It provides a systematic method to solve problems where we need to count selections or arrangements under certain forbidden position constraints. The polynomial coefficients (called rook numbers) represent the number of ways to place k non-attacking rooks on a given board.

In practical terms, rook polynomials find applications in probability theory, game theory, and various engineering optimization problems. For students, understanding rook polynomials is crucial as it demonstrates the power of generating functions in solving combinatorial counting problems.

## Key Concepts

### Board Representation

A board in rook polynomial context is a subset of squares from an m×n chessboard. We represent boards using set notation or Ferrers diagrams. For example, if we have a 4×4 board with certain forbidden positions, we mark those squares as unavailable or simply consider the available squares as our board.

A board B can be denoted as a set of coordinates {(i,j)} where rooks can be placed. The size of the board is the total number of available squares.

### Rook Numbers

The rook number r_k(B) represents the number of ways to place k non-attacking rooks on board B. Non-attacking means no two rooks share the same row or column. The rook numbers form a fundamental sequence where:

- r_0(B) = 1 (always one way to place zero rooks)
- r_1(B) = number of squares in the board
- r_k(B) = 0 if k exceeds the minimum of rows or columns in B

### Rook Polynomial Definition

The rook polynomial R(B, x) of a board B is defined as:

**R(B, x) = Σ\_{k=0}^{n} r_k(B) x^k**

where n is the maximum number of rooks that can be placed on the board. The coefficient of x^k is exactly r_k(B), the number of ways to place k non-attacking rooks.

### Board Splitting Theorem

If a board B can be divided into two disjoint sub-boards B1 and B2 (having no rows or columns in common), then:
**R(B, x) = R(B1, x) × R(B2, x)**

This theorem is crucial for simplifying complex board calculations by breaking them into smaller, manageable components.

### Relation with Inclusion-Exclusion

Rook polynomials are deeply connected to the principle of inclusion-exclusion. When solving problems about derangements (permutations with no fixed points) or restricted permutations, we can model the forbidden positions as a board and use rook polynomials to count valid arrangements.

For a set of n elements with forbidden positions defined by a board B:
**Number of valid permutations = Σ\_{k=0}^{n} (-1)^k r_k(B) (n-k)!**

## Examples

### Example 1: Simple 2×2 Complete Board

**Problem:** Find the rook polynomial for a complete 2×2 board.

**Solution:**

Step 1: Identify the board

- A complete 2×2 board has all 4 squares available
- Maximum rooks that can be placed = 2

Step 2: Calculate rook numbers

- r_0 = 1 (placing zero rooks in one way)
- r_1 = 4 (any of the 4 squares can have one rook)
- r_2 = 2 (two ways: place rooks at (1,1),(2,2) or (1,2),(2,1))

Step 3: Form the polynomial
R(x) = 1 + 4x + 2x²

**Verification:** The coefficient of x² = 2 represents the two ways to place 2 non-attacking rooks on a 2×2 board.

### Example 2: L-Shaped Board

**Problem:** Find the rook polynomial for a board with squares at positions (1,1), (1,2), (2,1).

**Solution:**

Step 1: Visualize the board

- It's an L-shaped 2×2 board missing the (2,2) position
- Has 3 available squares

Step 2: Calculate rook numbers

- r_0 = 1
- r_1 = 3 (three squares available)
- r_2 = 1 (only one way: place rooks at (1,2) and (2,1))

Step 3: Rook polynomial
R(x) = 1 + 3x + x²

**Note:** We cannot place 3 rooks because the board has only 2 rows and 2 columns.

### Example 3: Using Board Splitting Theorem

**Problem:** Find the rook polynomial for a board that is a 2×3 rectangle with the middle column missing.

**Solution:**

Step 1: The board can be visualized as two disjoint 2×1 boards

- Left column: positions (1,1), (2,1)
- Right column: positions (1,3), (2,3)

Step 2: For each 2×1 board:

- r_0 = 1
- r_1 = 2
- r_2 = 1

Each small board has polynomial: 1 + 2x + x²

Step 3: Apply splitting theorem
R(x) = (1 + 2x + x²) × (1 + 2x + x²)
= 1 + 4x + 6x² + 4x³ + x⁴

**Verification:** The coefficients match the expected values for placing k non-attacking rooks on this board configuration.

## Exam Tips

1. **Remember the definition:** The rook polynomial R(B,x) = Σ r_k(B)x^k where r_k(B) is the number of ways to place k non-attacking rooks.

2. **Start with r_0:** Always remember that r_0 = 1 for any board, as there is exactly one way to place zero rooks.

3. **Maximum rooks limit:** The maximum number of non-attacking rooks equals the minimum of number of rows and columns in the board.

4. **Use board splitting:** When the board has independent components, use the multiplication theorem to simplify calculations.

5. **Connection to inclusion-exclusion:** For permutation problems with forbidden positions, use the formula: valid permutations = Σ (-1)^k r_k(B)(n-k)!.

6. **Ferrers diagram representation:** Practice drawing boards as Ferrers diagrams or coordinate grids for better visualization.

7. **Check polynomial degree:** The degree of the rook polynomial equals the maximum number of rooks that can be placed on the board.

8. **Partial boards:** Be careful when dealing with incomplete boards - count only available squares and ensure non-attacking condition is maintained.

9. **Derangements special case:** When solving derangement problems using rook polynomials, the board represents forbidden fixed positions.

10. **Verify coefficients:** After computing, verify that coefficients make sense (they should be non-negative integers and follow combinatorial logic).
