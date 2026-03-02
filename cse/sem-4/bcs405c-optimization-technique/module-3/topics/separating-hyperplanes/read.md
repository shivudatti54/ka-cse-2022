# Separating Hyperplanes

## Table of Contents

- [Separating Hyperplanes](#separating-hyperplanes)
- [Introduction](#introduction)
- [Definition](#definition)
- [Types of Separation](#types-of-separation)
  - [Strict Separation](#strict-separation)
  - [Strong Separation](#strong-separation)
- [Support Vector Machine Context](#support-vector-machine-context)
- [Theorems](#theorems)
  - [Separating Hyperplane Theorem](#separating-hyperplane-theorem)
- [Applications](#applications)
- [Important Points](#important-points)

## Introduction

A separating hyperplane divides space into two half-spaces, with different sets on each side. Fundamental in classification and convex optimization.

## Definition

A hyperplane in ℝⁿ:
wᵀx + b = 0

Where w is normal vector, b is bias

## Types of Separation

### Strict Separation

All points of one set on one side, all points of other set on other side:
wᵀxᵢ + b > 0 for all i in class A
wᵀxⱼ + b < 0 for all j in class B

### Strong Separation

Points are strictly separated with margin

## Support Vector Machine Context

- Hyperplane maximizes margin between classes
- Support vectors lie on margin boundaries
- Optimal hyperplane found by solving convex problem

## Theorems

### Separating Hyperplane Theorem

If two convex sets are disjoint, there exists a hyperplane separating them.

## Applications

1. Support Vector Machines
2. Linear classification
3. Convex optimization
4. Decision boundary visualization

## Important Points

1. Normal vector defines hyperplane orientation
2. Distance from point to hyperplane: |wᵀx + b| / ||w||
3. Maximum margin hyperplane is unique
4. Required for linear classifiers
