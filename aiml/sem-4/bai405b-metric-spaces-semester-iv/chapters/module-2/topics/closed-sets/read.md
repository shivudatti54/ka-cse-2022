Of course. Here is a comprehensive educational note on **Closed Sets** for  Engineering students, structured as requested.

# Module 2: Concepts in Metric Spaces - Closed Sets

## 1. Introduction

In the previous modules, you learned about open sets, which form the foundation for concepts like convergence and continuity in metric spaces. **Closed sets** are their natural counterpart and are equally crucial. Understanding what it means for a set to be "closed" allows us to formally characterize the limits of sequences, the boundaries of sets, and the idea of "containing all your limit points." This concept is vital for advanced topics in analysis, optimization, and numerical methods that you will encounter in your engineering curriculum.

## 2. Core Concepts

### Definition of a Closed Set

A subset \( F \) of a metric space \((X, d)\) is said to be **closed** if its complement, \( F^c = X \setminus F \), is an open set in \( X \).

This definition is elegant because it directly relates the new concept (closed sets) to a known one (open sets). However, an equivalent and often more intuitive definition exists.

### Limit Points and Closure

*   **Limit Point (or Accumulation Point):** A point \( x \in X \) is a limit point of a set \( A \subseteq X \) if every open ball \( B(x, r) \) (for any \( r > 0 \)) contains **at least one point of \( A \) different from \( x \) itself**. In other words, you can get arbitrarily close to \( x \) using points from \( A \).

*   **Closed Set (Alternative Definition):** A set \( F \) is closed **if and only if it contains all of its limit points**. This means there are no points "missing" from \( F \) that are arbitrarily close to it.

The set of all limit points of \( A \) is called the **derived set**, denoted by \( A' \). The **closure** of \( A \), denoted by \( \overline{A} \), is the union of the set and its derived set: \( \overline{A} = A \cup A' \). Therefore, a set is closed if and only if \( A = \overline{A} \).

## 3. Examples

Let's consider the metric space \( (\mathbb{R}, d) \), where \( d \) is the standard Euclidean distance \( d(x, y) = |x - y| \).

**1. Closed Intervals:** The interval \( A = [2, 5] \) is closed.
    *   Its complement is \( (-\infty, 2) \cup (5, \infty) \), which is a union of open sets and hence open.
    *   The limit points of \( A \) are all points in \([2, 5]\). For example, 2 is a limit point because any open ball \( B(2, r) = (2-r, 2+r) \) will contain points from \( A \) (like \( 2 + r/2 \)). Since \( A \) contains all these points, it is closed.

**2. Open Intervals are NOT Closed:** The set \( B = (2, 5) \) is not closed.
    *   Its complement is \( (-\infty, 2] \cup [5, \infty) \), which is not open because you cannot have an open ball around the point 2 that stays entirely within the complement (it will always include points just greater than 2, which are in \( B \)).
    *   The point 2 is a limit point of \( B \) (any ball around 2 contains points from \( B \)), but 2 is not itself an element of \( B \). Therefore, \( B \) does *not* contain all its limit points and is not closed.

**3. Finite Sets:** Any finite set of points, e.g., \( C = \{-1, 0, 5\} \), is closed.
    *   Consider a point not in \( C \), say \( x = 1 \). Let \( r = \min(d(1, -1), d(1, 0), d(1, 5)) = \min(2, 1, 4) = 1 \). The open ball \( B(1, 0.5) \) contains no points of \( C \), meaning 1 is not a limit point. In fact, no point outside \( C \) can be a limit point because the distances to the points in \( C \) are finite and positive. Therefore, \( C \) has no limit points outside itself. Since it contains all (zero) of its external limit points, it is closed. Its complement is a union of open intervals and is open.

**4. The Entire Space and the Empty Set:** In any metric space \((X, d)\):
    *   \( X \) is closed (its complement is the empty set, which is open).
    *   The empty set \( \emptyset \) is closed (its complement is \( X \), which is open).
These are both simultaneously open *and* closed sets.

## 4. Key Theorems and Properties

1.  **Arbitrary Intersection, Finite Union:** The intersection of any collection (finite or infinite) of closed sets is closed. The union of a *finite* number of closed sets is closed. (This is the dual of the properties for open sets).

2.  **Sequential Characterization:** A subset \( F \) of a metric space is closed **if and only if** for every sequence \( \{x_n\} \) in \( F \) that converges to a limit \( x \in X \), the limit \( x \) also belongs to \( F \). This is a very powerful and practical way to test if a set is closed, especially in \( \mathbb{R}^n \).

3.  **Relationship with Open Sets:** A set can be open, closed, both, or neither.
    *   \( (0, 1) \) is open but not closed.
    *   \( [0, 1] \) is closed but not open.
    *   \( \mathbb{R} \) and \( \emptyset \) are both open and closed.
    *   \( [0, 1) \) is neither open nor closed.

## 5. Summary & Key Points

*   **Definition:** A set \( F \) is **closed** if its complement \( F^c \) is open.
*   **Intuition:** A closed set **contains all its limit points**. There are no points "missing" from its boundary.
*   **Examples:** Closed intervals ([a, b]), finite sets, the whole space, and the empty set are all closed.
*   **Testing Closure:** Use the sequential characterization: if a sequence within the set converges, its limit must also be in the set.
*   **Set Operations:** Arbitrary intersections and finite unions of closed sets remain closed.
*   **Not Mutually Exclusive:** A set can be both open and closed (clopen) or neither.