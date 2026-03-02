Of course. Here is a comprehensive educational module on "Combinations with Repetition" for  Engineering students, structured as requested.

---

### **Module 2: Properties of the Integers**

### **Topic: Combinations with Repetition**

#### **1. Introduction**

In Discrete Mathematical Structures, we often count the number of ways to choose items from a set. A standard combination, denoted as **C(n, r)** or **<sub>n</sub>C<sub>r</sub>**, counts the number of ways to choose `r` distinct items from `n` distinct objects **without repetition** and where **order does not matter**.

But what if repetition _is_ allowed? For instance, how many ways can you choose 3 scoops of ice cream from 5 flavors if you can choose the same flavor more than once? This scenario, where items can be selected repeatedly and order is irrelevant, is solved using **Combinations with Repetition**.

---

#### **2. Core Concepts & Derivation**

The number of **combinations with repetition** (or **multisubsets**) of `r` items chosen from `n` distinct types is denoted as **<sub>n</sub>H<sub>r</sub>** (often read as "`n` multichoose `r`").

**The Formula:**
<sub>n</sub>H<sub>r</sub> = C(n + r - 1, r) = <sub>n+r-1</sub>C<sub>r</sub>

**Why does this work? The "Stars and Bars" Method:**
This is a brilliant combinatorial proof. Imagine we want to count the number of ways to choose `r` items from `n` types with repetition allowed.

1.  Represent each selection as a sequence of `stars` (\*) and `bars` (|).
    - Let each star (`*`) represent one item being chosen.
    - Let the bars (`|`) act as _dividers_ between the different types of items.

2.  If we have `n` types of items, we need `n - 1` bars to create `n` compartments (one for each type).

3.  Therefore, any combination with repetition can be represented by a sequence of `r` stars and `n - 1` bars.

**Example:** Suppose we want to choose `r = 3` scoops from `n = 5` flavors (Chocolate, Vanilla, Strawberry, Mint, Berry). The sequence `* * | | * | |` means:

- 2 scoops of Flavor 1 (Chocolate)
- 0 scoops of Flavor 2 (Vanilla)
- 1 scoop of Flavor 3 (Strawberry)
- 0 scoops of Flavor 4 (Mint)
- 0 scoops of Flavor 5 (Berry)
  This represents the selection: {Chocolate, Chocolate, Strawberry}.

**The Key Insight:**
Every possible combination is uniquely represented by a distinct arrangement of `r` stars and `n-1` bars. Conversely, every arrangement of these `r + n - 1` symbols corresponds to a unique selection.

**The Final Count:**
We have `r + n - 1` positions in our sequence. We need to choose `r` of these positions to place the stars (the remaining `n-1` positions will automatically be bars). The number of ways to do this is **C(r + n - 1, r)**.

Alternatively, we could choose the positions for the `n-1` bars, which would be **C(r + n - 1, n - 1)**. These are equal due to the symmetry of combinations: C(a, b) = C(a, a-b).

---

#### **3. Worked Example**

**Problem:** A bakery has 4 types of donuts (Glazed, Chocolate, Jelly, Boston Cream). How many ways can a customer buy a box of 6 donuts? (Repetition is allowed, and order in the box doesn't matter).

**Solution:**
This is a classic combination with repetition problem.

- `n` (number of types) = 4
- `r` (number of items to choose) = 6

Apply the formula:
<sub>n</sub>H<sub>r</sub> = C(n + r - 1, r) = C(4 + 6 - 1, 6) = C(9, 6)

Now, calculate C(9, 6):
C(9, 6) = 9! / (6! _ (9-6)!) = 9! / (6! _ 3!) = (9×8×7) / (3×2×1) = 84

**∴ There are 84 distinct ways to choose a box of 6 donuts.**

---

#### **4. Key Points & Summary**

| Aspect            | Standard Combination (Without Repetition) | Combination with Repetition                        |
| :---------------- | :---------------------------------------- | :------------------------------------------------- |
| **Notation**      | <sub>n</sub>C<sub>r</sub>                 | <sub>n</sub>H<sub>r</sub>                          |
| **Formula**       | n! / (r! (n-r)!)                          | C(n + r - 1, r)                                    |
| **Repetition?**   | Not allowed                               | Allowed                                            |
| **Order?**        | Does not matter                           | Does not matter                                    |
| **Analogous To**  | Choosing a committee                      | Choosing a multiset                                |
| ** Relevance** | Used in probability, cryptography.        | Essential in counting problems, integer solutions. |

**Summary:**

- Use **Combinations with Repetition (<sub>n</sub>H<sub>r</sub>)** when the order of selection is unimportant, but you can select the same item multiple times.
- The fundamental formula is **<sub>n</sub>H<sub>r</sub> = C(n + r - 1, r)**.
- This concept is equivalent to finding the number of non-negative integer solutions to equations like x₁ + x₂ + ... + xₙ = r, which has immense applications in computer science algorithms, partitioning problems, and more.
