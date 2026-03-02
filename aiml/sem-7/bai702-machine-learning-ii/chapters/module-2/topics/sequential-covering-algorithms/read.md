# Sequential Covering Algorithms for Rule-Based Classification

## Introduction

In Machine Learning, classification is a fundamental task. While algorithms like Decision Trees and SVMs create complex, monolithic models, **Sequential Covering Algorithms** take a different, more human-interpretable approach. They belong to the family of **Rule-Based Classifiers** and are designed to learn a set of `IF-THEN` rules that collectively represent the target concept.

These algorithms are particularly important for their high interpretability, making them invaluable in domains like medical diagnosis and fault analysis where understanding the *reason* behind a prediction is as crucial as the prediction itself. The core idea is "sequential" and "covering"—they learn one rule at a time, sequentially, and remove (or "cover") the data points classified by that rule before learning the next one.

## Core Concepts

### 1. The IF-THEN Rule Structure
A rule `R` is a logical expression of the form:
`IF (Condition1) AND (Condition2) AND ... THEN (Class = C_j)`

*   **Antecedent (LHS):** The `IF` part, consisting of a conjunction of attribute-value tests (e.g., `(BloodPressure = High) AND (Age > 60)`).
*   **Consequent (RHS):** The `THEN` part, which specifies the class label predicted for any record satisfying the antecedent.

### 2. The Sequential Covering Strategy
This is a greedy, general-to-specific search strategy. The goal is to create a set of rules `Rule_Set` that together cover all (or most) examples in the training data.

The generic pseudocode is:
1.  `Rule_Set = {}` // Start with an empty set of rules.
2.  `E = Training_Data` // Start with all training examples.
3.  **while** stopping condition not met (e.g., `E` is not empty, or accuracy is sufficient):
    a.  Learn a single rule `R` that performs well on the *current* set of examples `E`. This rule is typically learned to cover as many positive examples of a single class as possible while minimizing errors.
    b.  Add the learned rule `R` to `Rule_Set`.
    c.  **Remove all training examples** from `E` that are correctly classified by `R` (i.e., that are "covered" by the rule). This focuses the algorithm on the remaining, uncovered examples.
4.  **end while**
5.  Return `Rule_Set`.

This strategy is also known as **Separate-and-Conquer**.

### 3. Learning a Single Rule (The `LEARN-ONE-RULE` Function)

The key step is how to learn one high-quality rule in step 3a. This is usually done using a **general-to-specific beam search**:

*   **Start:** Begin with a very general, empty rule with no conditions: `IF {} THEN (Class = C_j)`.
*   **Specialize:** Iteratively add new attribute-value conditions to the antecedent to make the rule more specific. This improves the rule's accuracy by excluding negative examples.
*   **Beam Search:** Instead of keeping only the best candidate (like hill-climbing), a beam search keeps the top `k` best candidate rules at each step (`k` is the beam width). This helps avoid getting stuck in local optima.
*   **Evaluation:** Candidate rules are evaluated and selected based on a **heuristic function** that balances completeness and purity. Common functions include:
    *   **Accuracy:** `(p + n') / (P + N')` where `p` is positive examples covered, `n'` is negative examples *not* covered, `P` and `N'` are totals.
    *   **Information Gain / FOIL Gain:** Favors rules that provide the most information about the class.
    *   **Laplace Accuracy:** `(p + 1) / (p + n + c)` (where `c` is the number of classes), which provides a more pessimistic and stable estimate for small rules.

### Example: Classifying "Safe to Launch a Spacecraft?"

Imagine a simplified dataset with attributes `WindSpeed`, `CloudCover`, and class `Launch`.

| WindSpeed | CloudCover | Launch |
| :--- | :--- | :--- |
| Low | Clear | Yes |
| Low | Cloudy | No |
| High | Clear | No |
| High | Cloudy | No |

**Step 1:** The algorithm decides to first learn rules for the majority class, `Launch=No`.
**Step 2: Learn-ONE-RULE for class "No":**
*   Start with rule: `IF {} THEN (Launch=No)`. This covers all 4 examples (3 correct, 1 wrong). Accuracy = 3/4.
*   Specialize by adding conditions. Top candidates might be:
    *   `IF (WindSpeed=High) THEN (No)` -> Covers ex. 3 & 4. Both correct. Accuracy=2/2=1.0.
    *   `IF (CloudCover=Cloudy) THEN (No)` -> Covers ex. 2 & 4. Both correct. Accuracy=2/2=1.0.
*   Let's choose `IF (WindSpeed=High) THEN (Launch=No)`. Add it to `Rule_Set`.
*   **Remove covered examples:** Examples 3 and 4 are removed from the training set `E`. Now `E` contains only examples 1 and 2.

**Step 3:** Learn the next rule from the remaining data `E`.
**Step 4: Learn-ONE-RULE for class "No" again (from only ex. 1 & 2):**
*   `IF {} THEN (No)` has accuracy 1/2 (covers ex.2 correctly, ex.1 wrongly).
*   Specialize:
    *   `IF (CloudCover=Cloudy) THEN (No)` -> Covers ex.2. Correct. A perfect rule.
*   Add `IF (CloudCover=Cloudy) THEN (Launch=No)` to `Rule_Set`.
*   Remove covered example (ex.2). The only remaining example is ex.1 (`Launch=Yes`), which isn't covered by any `No` rule. A default rule (`IF (no other rule applies) THEN (Yes)`) would be used for it.

Our final `Rule_Set` is:
1.  `IF (WindSpeed=High) THEN (Launch=No)`
2.  `IF (CloudCover=Cloudy) THEN (Launch=No)`
3.  **Default Rule:** `ELSE (Launch=Yes)`

## Key Points & Summary

*   **Interpretability is Key:** The primary advantage is the production of simple, human-readable `IF-THEN` rules.
*   **Greedy Strategy:** The sequential covering algorithm is a greedy heuristic. It finds good local rules but does not guarantee a globally optimal rule set.
*   **Separate-and-Conquer:** The strategy involves learning one rule, removing the data it explains, and then concentrating on the rest.
*   **Rule Learning:** The `Learn-One-Rule` function typically uses a general-to-specific beam search, evaluated by a heuristic function like FOIL Gain or Laplace Accuracy.
*   **Order Matters:** Rules are learned in a specific sequence, and this order is important for prediction. The first rule that fires is used ("decision list").
*   **Handling Uncovered Data:** A default rule (usually the majority class) is often used to classify any instance not covered by any learned rule.

Famous algorithms based on this principle include **CN2** and **RIPPER** (Repeated Incremental Pruning to Produce Error Reduction).