# Asymptotic Notations Analysis - Summary (Ge4A Data Structures, Delhi University)

## Introduction
Asymptotic notations are mathematical tools used to describe the efficiency of algorithms in terms of input size (*n*). They express the growth rate of time or space complexity as *n* approaches infinity, enabling comparison of algorithms regardless of hardware. In Data Structures (Ge4A), this analysis is fundamental for selecting optimal algorithms and understanding algorithmic performance.

## Key Concepts
- **Time & Space Complexity**: Time complexity measures the number of operations; space complexity measures memory usage.
- **Big-O Notation (O)**: Represents the *upper bound* (worst-case growth rate). Example: O(*n*²) for bubble sort.
- **Big-Omega Notation (Ω)**: Represents the *lower bound* (best-case growth rate). Example: Ω(*n*) for linear search when the element is at the first position.
- **Theta Notation (Θ)**: Represents a *tight bound*, combining upper and lower bounds. Example: Θ(*n*) for traversing an array.
- **Little-o (o) & Little-omega (ω)**: Strict upper and lower bounds, respectively (less common in exam questions).
- **Case Analysis**:
  - **Best-case**: Minimum operations (e.g., sorted array for linear search).
  - **Average-case**: Expected operations (often assumed or computed probabilistically).
  - **Worst-case**: Maximum operations (most frequently analyzed for reliability).
- **Common Complexities** (in increasing order of growth):
  - O(1) – Constant (e.g., accessing an array element)
  - O(log *n*) – Logarithmic (e.g., binary search)
  - O(*n*) – Linear (e.g., linear search)
  - O(*n* log *n*) – Linearithmic (e.g., merge sort)
  - O(*n*²) – Quadratic (e.g., bubble sort)
  - O(2^*n*) – Exponential (e.g., recursive Fibonacci)
- **Master Theorem**: A formula to solve recurrence relations of divide-and-conquer algorithms (e.g., T(*n*) = aT(*n*/b) + f(*n*)).

## Conclusion
Asymptotic notations provide a standardized way to analyze and compare algorithm efficiency. Mastery of Big-O, Omega, and Theta is essential for exam success and practical algorithm design, aligning with the Delhi University BSc (H) Computer Science NEP 2024 syllabus for Data Structures (Ge4A).