Of course. Here is a comprehensive educational module on "Order Relation in Cardinal Numbers" for engineering students, formatted as requested.

***

### **Module 1: Theory of Sets | Order Relation in Cardinal Numbers**

**Subject:** METRIC SPACES
**Semester:** IV

---

#### **1. Introduction: Why Order Matters for Sizes of Infinity**

In set theory, after defining the cardinal number of a set (which represents its "size" or number of elements), a natural question arises: how do we *compare* the sizes of two sets, especially if they are infinite? The concepts of "less than," "equal to," and "greater than" for finite numbers need a rigorous mathematical definition for infinite cardinals. This is where **order relations in cardinal numbers** come into play. It allows us to formally state that, for instance, the cardinality of the natural numbers ($\aleph_0$) is "less than" the cardinality of the real numbers.

#### **2. Core Concepts: Defining Order Between Cardinals**

The order relation between two cardinal numbers, $\mathbf{|A|}$ and $\mathbf{|B|}$, is defined using the concept of **functions** between the sets they represent.

*   **Equality ($|A| = |B|$):** Two sets $A$ and $B$ have the same cardinality if there exists a **bijective function** (a one-to-one correspondence) from $A$ to $B$. This means every element of $A$ pairs uniquely with every element of $B$, and vice-versa.

*   **Inequality ($|A| \leq |B|$):** The cardinality of $A$ is less than or equal to the cardinality of $B$ if there exists an **injective function** (a one-to-one function) from $A$ *into* $B$. This means we can "embed" set $A$ inside set $B$ without any overlap, proving that $B$ is at least as large as $A$.

*   **Strict Inequality ($|A| < |B|$):** This is the crucial definition. We say $|A| < |B|$ if **both** of the following conditions hold:
    1.  $|A| \leq |B|$ (there exists an injection $f: A \rightarrow B$).
    2.  $|A| \neq |B|$ (there does **not** exist a bijection from $A$ to $B$).

This strict inequality captures the intuitive notion that $B$ is strictly larger than $A$.

#### **3. Examples: Applying the Definitions**

Let's apply these definitions to well-known sets.

*   **Example 1: Finite Sets**
    Let $A = \{1, 2, 3\}$ and $B = \{a, b, c, d\}$.
    *   An injection $f: A \rightarrow B$ exists (e.g., $f(1)=a, f(2)=b, f(3)=c$). So, $|A| \leq |B|$.
    *   A bijection *cannot* exist because $B$ has an element ($d$) with no partner in $A$. So, $|A| \neq |B|$.
    *   Therefore, $|A| = 3 < 4 = |B|$.

*   **Example 2: Infinite Sets (Countable vs. Uncountable)**
    Let $\mathbb{N}$ be the set of natural numbers ($|\mathbb{N}| = \aleph_0$) and $\mathbb{R}$ be the set of real numbers.
    *   **Injection:** The identity function $f(n) = n$ is an injection from $\mathbb{N}$ to $\mathbb{R}$, so $\aleph_0 \leq |\mathbb{R}|$.
    *   **No Bijection:** Georg Cantor's famous **diagonalization argument** proves that no function from $\mathbb{N}$ to $\mathbb{R}$ can be surjective (and hence not bijective). There will always be real numbers left out.
    *   Therefore, $\aleph_0 < |\mathbb{R}|$. The set of real numbers is a "larger" infinity than the set of natural numbers.

*   **A Subtle Point: The Schröder-Bernstein Theorem**
    Proving $|A| \neq |B|$ directly can be difficult. The Schröder-Bernstein Theorem is a powerful tool that states:
    > If $|A| \leq |B|$ *and* $|B| \leq |A|$, then $|A| = |B|$.
    This means if you can find an injection from $A$ to $B$ *and* an injection from $B$ to $A$, you have effectively proven a bijection exists without having to construct it explicitly.

#### **4. Key Points & Summary**

| Concept | Definition | Significance |
| :--- | :--- | :--- |
| **$|A| = |B|$** | ∃ a bijection $f: A \rightarrow B$. | Sets are of the same size. |
| **$|A| \leq |B|$** | ∃ an injection $f: A \rightarrow B$. | $B$ is at least as large as $A$. |
| **$|A| < |B|$** | $|A| \leq |B|$ **and** $|A| \neq |B|$. | $B$ is strictly larger than $A$. |
| **Schröder-Bernstein** | If $|A| \leq |B|$ and $|B| \leq |A|$, then $|A| = |B|$. | Powerful tool for proving cardinal equality. |

**Summary:**
The order relation for cardinal numbers provides a rigorous framework for comparing the sizes of sets, both finite and infinite. It is built entirely on the existence (or non-existence) of specific types of functions between sets—injections and bijections. This leads to a fascinating hierarchy of infinities, starting with $\aleph_0$ (the countable infinity) and moving to larger infinities like the cardinality of the continuum ($|\mathbb{R}|$). Understanding this ordering is fundamental to grasping the structure of different metric and topological spaces you will encounter.