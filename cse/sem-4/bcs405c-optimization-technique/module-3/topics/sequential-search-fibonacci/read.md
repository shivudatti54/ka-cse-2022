# Sequential Search and Fibonacci Search

## Table of Contents

- [Sequential Search and Fibonacci Search](#sequential-search-and-fibonacci-search)
- [Introduction](#introduction)
- [Sequential Search (Linear Search)](#sequential-search-linear-search)
- [Fibonacci Search Method](#fibonacci-search-method)
  - [Fibonacci Numbers](#fibonacci-numbers)
  - [Algorithm](#algorithm)
  - [Properties](#properties)
- [Comparison](#comparison)
- [Important Points](#important-points)

## Introduction

Fibonacci search is a unimodal optimization method using Fibonacci numbers to divide the search interval.

## Sequential Search (Linear Search)

Simple but inefficient:

- Check points one by one
- O(n) comparisons
- No assumption about function

## Fibonacci Search Method

### Fibonacci Numbers

F₀ = 0, F₁ = 1
Fₙ = Fₙ₋₁ + Fₙ₋₂

### Algorithm

1. Initialize interval [a, b]
2. Choose n such that Fₙ > (b-a)/ε
3. Evaluate at Fibonacci points
4. Reduce interval using Fibonacci properties
5. Repeat until convergence

### Properties

- Guaranteed convergence
- Evaluates one point per iteration
- No derivative needed
- Good for unimodal functions

## Comparison

| Method         | Evaluations | Derivative |
| -------------- | ----------- | ---------- |
| Binary Search  | O(log n)    | No         |
| Fibonacci      | O(log n)    | No         |
| Golden Section | O(log n)    | No         |

## Important Points

1. Fibonacci search optimal for unimodal functions
2. No derivative information needed
3. Number of iterations depends on Fibonacci sequence
4. More efficient than sequential search
