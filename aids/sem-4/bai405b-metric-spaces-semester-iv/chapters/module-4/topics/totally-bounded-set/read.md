Of course. Here is a comprehensive educational note on "Totally Bounded Sets" for  Engineering students.

# Module 4: Compactness - Totally Bounded Sets

## 1. Introduction

In our exploration of compactness in metric spaces, we encounter a crucial concept that acts as a bridge between the intuitive idea of "finiteness" and the formal definition of compactness: the **totally bounded set**. While a compact set is both closed and "bounded" in a very strong sense, total boundedness provides a more precise and powerful notion of "finiteness" than simple boundedness. It essentially means that the set can be covered by a *finite* number of arbitrarily small "patches" (open balls).

## 2. Core Concepts

### Definition of Total Boundedness

Let $(X, d)$ be a metric space. A subset $A \subseteq X$ is said to be **totally bounded** if for every real number $\epsilon > 0$ (no matter how small), there exists a finite number of points $x_1, x_2, ..., x_n \in X$ such that:
$$ A \subseteq \bigcup_{i=1}^{n} B(x_i, \epsilon) $$
In other words, the entire set $A$ can be covered by a finite collection of open balls of radius $\epsilon$.

**Key Observations from the Definition:**
1.  **Finite Cover:** The emphasis is on a *finite* number of balls. The number $n$ will depend on $\epsilon$; as $\epsilon$ gets smaller, $n$ will generally need to get larger.
2.  **Centers can be anywhere:** The centers of the balls $x_i$ are required to be in the space $X$, but they do *not* necessarily have to be inside $A$. However, one can often prove that it's equivalent to require the centers to be in $A$.
3.  **Stronger than Boundedness:** Every totally bounded set is bounded, but the converse is not always true.

### Why is this a "Finite" Property?

Think of total boundedness as saying that the set $A$ has only a "finite" number of degrees of freedom at any scale $\epsilon$. For any desired level of precision ($\epsilon$), you only need a finite number of points to approximate every point in $A$. This is a much stronger condition than simple boundedness. A set can be bounded but still be "infinitely spread out" in a way that requires infinitely many small balls to cover it. A totally bounded set cannot be.

### Relationship with Compactness

This is the most important reason for studying total boundedness. We have the following fundamental theorem:

**Theorem:** *A metric space $(X, d)$ is **compact** if and only if it is **complete and totally bounded**.*

*   **Compact $\implies$ Totally Bounded:** This follows directly from the definition of compactness ("every open cover has a finite subcover"). For any $\epsilon > 0$, the collection of all $\epsilon$-balls is an open cover of $X$. By compactness, a finite subcover exists.
*   **Complete and Totally Bounded $\implies$ Compact:** This is the deeper part. Total boundedness ensures you can cover the space with finitely many $\epsilon$-balls. Completeness then guarantees that sequences don't "escape" or converge to a point outside the space.

This theorem is incredibly useful. Proving a set is compact directly from the open cover definition can be difficult. Instead, we can often prove it's complete and totally bounded.

## 3. Examples

**Example 1: A Totally Bounded Set**
Consider the set $A = \{1, 1/2, 1/3, ..., 1/n, ...\}$ in the metric space $(\mathbb{R}, d)$, with the standard Euclidean metric $d(x,y) = |x-y|$.
*   Is it bounded? Yes, it's contained in the ball $B(0, 2)$.
*   Is it totally bounded? Let $\epsilon > 0$ be given. Because the sequence converges to $0$, all but finitely many points lie inside the interval $(0, \epsilon)$. You can cover these with the ball $B(0, \epsilon)$. The finitely many points outside $(0, \epsilon)$ can each be covered by their own $\epsilon$-ball. Thus, a finite cover exists. Hence, $A$ is totally bounded.

**Example 2: A Bounded but NOT Totally Bounded Set**
Consider the closed unit ball $B[0,1]$ in the metric space $(\ell^\infty, d)$, where $\ell^\infty$ is the space of all bounded real sequences and the metric is the sup-norm: $d((x_n), (y_n)) = \sup_n |x_n - y_n|$.
*   This set is clearly bounded.
*   Now, consider the set of sequences $A = \{e_1, e_2, e_3, ...\}$ where $e_k$ is the sequence with a $1$ in the $k$-th position and $0$ everywhere else. Note that $A \subset B[0,1]$.
*   For any two distinct points $e_i$ and $e_j$ in $A$, $d(e_i, e_j) = \sup |e_i - e_j| = 1$.
*   Take $\epsilon = 1/2$. To cover these points, each open ball of radius $1/2$ can contain *at most one* point from $A$ (because the distance between any two is $1 > 1/2$). Since $A$ is infinite, you would need an *infinite* number of $\epsilon$-balls to cover it. Therefore, the entire unit ball $B[0,1]$ cannot be covered by a finite number of $\epsilon$-balls and is **not totally bounded**.

This shows that in infinite-dimensional spaces, boundedness does not imply total boundedness.

## 4. Key Points & Summary

*   **Definition:** A set $A$ in a metric space $(X,d)$ is **totally bounded** if for every $\epsilon > 0$, it can be covered by a finite number of open balls of radius $\epsilon$.
*   **Implies Boundedness:** Total boundedness is a stronger condition than boundedness. $Totally\ Bounded \implies Bounded$.
*   **Converse is False:** A set can be bounded but not totally bounded (as shown in the $\ell^\infty$ example).
*   **Link to Compactness:** A metric space is **compact if and only if it is complete and totally bounded**. This provides a powerful alternative method for proving compactness.
*   **Intuition:** Total boundedness means a set is "finite" at every scale $\epsilon$. You never need infinitely many points to approximate all other points to within $\epsilon$.