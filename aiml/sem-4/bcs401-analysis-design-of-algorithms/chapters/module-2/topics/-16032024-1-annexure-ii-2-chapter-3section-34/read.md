# Exhaustive Search (Travelling Salesman Problem)

=====================================================

## 3.4 Exhaustive Search Approach

---

### Introduction

---

The exhaustive search approach is a brute force method used to solve the Travelling Salesman Problem (TSP). In this approach, every possible solution is generated and evaluated. This method is guaranteed to find the optimal solution but is computationally expensive due to its high time complexity.

### Definition

---

Exhaustive search is a problem-solving strategy where every possible solution is considered and evaluated until the optimal solution is found.

### Time Complexity

---

The time complexity of exhaustive search is O(n!), where n is the number of cities. This is because there are n! possible permutations of cities, and each permutation needs to be evaluated.

### Space Complexity

---

The space complexity of exhaustive search is also O(n!), as we need to store all possible permutations of cities.

### Example

---

Suppose we have 4 cities: A, B, C, and D. The exhaustive search approach would generate the following permutations:

- ABCD
- ABDC
- ACBD
- ACDB
- ADBC
- ADCB
- BCAD
- BCDA
- BDCB
- BDAC
- CDAB
- CDBA

Each permutation would be evaluated to determine the shortest tour.

### Key Concepts

---

- **Permutation**: An arrangement of objects in a specific order.
- **TSP**: Travelling Salesman Problem, a classic problem in combinatorial optimization.
- **Exhaustive search**: A problem-solving strategy that considers every possible solution until the optimal solution is found.

### Advantages

---

- **Guaranteed optimal solution**: Exhaustive search is guaranteed to find the optimal solution, if it exists.
- **Simple to implement**: The basic idea of exhaustive search is straightforward, making it easy to implement.

### Disadvantages

---

- **Computational expensive**: Exhaustive search is computationally expensive due to its high time complexity.
- **Not practical for large problems**: Exhaustive search is not practical for large problems, as it requires an enormous amount of time and memory.

### Conclusion

---

Exhaustive search is a brute force approach used to solve the Travelling Salesman Problem. While it guarantees an optimal solution, its high time and space complexity make it impractical for large problems. Other approaches, such as heuristics and approximation algorithms, are often preferred for solving TSP due to their faster computational time.
