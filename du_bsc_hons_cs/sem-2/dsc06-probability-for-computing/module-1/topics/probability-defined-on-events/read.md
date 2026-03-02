# Probability Defined on Events

## Introduction

Probability theory forms the mathematical foundation for numerous computing applications, from algorithm analysis to machine learning and cryptography. When we speak of probability in computing contexts, we are essentially quantifying uncertainty associated with events—be it the outcome of a randomized algorithm, the occurrence of a network failure, or the prediction of user behavior in data science applications.

In this topic, we formally define probability on events, establishing the axiomatic foundation that allows us to compute and reason about uncertain outcomes. The concept of a probability space, comprising the sample space, events, and a probability measure, is central to this formalization. Understanding how to define and manipulate events—the subsets of sample spaces—is crucial for solving real-world computing problems. For instance, when analyzing the performance of quicksort with random pivots, we model various scenarios as events and compute their probabilities to determine expected running time.

This topic builds the conceptual framework necessary for all subsequent probability studies, including conditional probability, Bayes' theorem, and random variables—tools every computer scientist must master.

## Key Concepts

### Sample Space and Outcomes

The **sample space (S or Ω)** is the set of all possible outcomes of a random experiment. In computing contexts, this might represent all possible inputs, all states a program can reach, or all possible results of a computation.

For example:
- Tossing a coin twice: S = {HH, HT, TH, TT}
- Rolling a die: S = {1, 2, 3, 4, 5, 6}
- A program executing: S = {program terminates successfully, program crashes, program enters infinite loop}

An **outcome (or elementary event)** is a single element of the sample space—the most granular result we consider.

### Events as Subsets

An **event** is a subset of the sample space. We say an event "occurs" if the outcome of the experiment is an element of that subset. Events allow us to group outcomes that share some property of interest.

Key types of events include:

**Simple (Elementary) Events**: Events containing exactly one outcome. In the coin toss example, {HH} is a simple event.

**Compound Events**: Events containing multiple outcomes. "Getting at least one head" in two coin tosses is {HH, HT, TH}.

**Impossible Event (∅)**: The empty set—an event that cannot occur.

**Certain Event (S)**: The sample space itself—an event that always occurs.

### Operations on Events

Given events A and B within sample space S:

**Complement (A')**: The set of outcomes in S that are not in A. A' occurs when A does not occur. Mathematically: A' = S - A

**Union (A ∪ B)**: The set of outcomes in either A or B (or both). A ∪ B occurs if at least one of A or B occurs.

**Intersection (A ∩ B)**: The set of outcomes in both A and B. A ∩ B occurs if both A and B occur simultaneously.

**Difference (A - B)**: Outcomes in A but not in B. Equivalent to A ∩ B'.

### Special Event Relationships

**Mutually Exclusive (Disjoint) Events**: Two events A and B are mutually exclusive if they cannot occur together, i.e., A ∩ B = ∅. When tossing a coin, getting "heads" and "tails" are mutually exclusive events.

**Exhaustive Events**: A set of events is exhaustive if their union equals the sample space S. Events A₁, A₂, ..., Aₙ are exhaustive if A₁ ∪ A₂ ∪ ... ∪ Aₙ = S.

**Complementary Events**: Two events A and A' are complements if they are mutually exclusive and exhaustive: A ∩ A' = ∅ and A ∪ A' = S.

### Probability Axioms and Measure

A **probability function** P assigns a number between 0 and 1 to each event, satisfying three axioms:

**Axiom 1 (Non-negativity)**: For any event A, P(A) ≥ 0

**Axiom 2 (Normalization)**: P(S) = 1, where S is the sample space

**Axiom 3 (Countable Additivity)**: If A₁, A₂, A₃, ... are pairwise mutually exclusive events (Aᵢ ∩ Aⱼ = ∅ for i ≠ j), then:
P(A₁ ∪ A₂ ∪ A₃ ∪ ...) = Σ P(Aᵢ)

These axioms, due to Andrey Kolmogorov (1933), form the foundation of modern probability theory.

### Probability Space

A **probability space** is a triple (S, ℱ, P) where:
- S is the sample space
- ℱ (sigma-algebra or event space) is the collection of all events (subsets of S) to which probabilities are assigned
- P is the probability function satisfying the axioms

For finite sample spaces, ℱ typically contains all subsets of S, giving us 2^|S| possible events.

### Fundamental Probability Rules

From the axioms, we derive essential rules:

**Complement Rule**: P(A') = 1 - P(A)

**Inclusion-Exclusion Principle**: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

**Boole's Inequality**: P(A ∪ B) ≤ P(A) + P(B)

**Monotonicity**: If A ⊆ B, then P(A) ≤ P(B)

## Examples

### Example 1: Programming Language Selection

A software company randomly selects a programming language for a new project from the set {Python, Java, C++, JavaScript, Ruby, Go}. What is the probability that the selected language begins with 'J'?

**Solution:**

Sample space S = {Python, Java, C++, JavaScript, Ruby, Go}, so |S| = 6

Event A = "Language begins with J" = {Java, JavaScript}, so |A| = 2

Since selection is random, each outcome is equally likely: P(A) = |A|/|S| = 2/6 = 1/3

This illustrates the classical (equiprobable) definition of probability: P(A) = number of favorable outcomes / total number of outcomes.

### Example 2: Network Server Failure Analysis

A server has three independent components: A, B, and C. The probabilities of components A, B, and C failing in a day are 0.1, 0.2, and 0.15 respectively. Calculate:
(a) Probability that at least one component fails
(b) Probability that exactly one component fails

**Solution:**

Let Fₐ = "A fails", Fʙ = "B fails", Fc = "C fails"
Given: P(Fₐ) = 0.1, P(Fʙ) = 0.2, P(Fc) = 0.15

(a) "At least one fails" = Fₐ ∪ Fʙ ∪ Fc

Using complement: "At least one fails" = 1 - "none fails" = 1 - P(Fₐ' ∩ Fʙ' ∩ Fc')

Since components fail independently:
P(none fails) = P(Fₐ') × P(Fʙ') × P(Fc') = (1-0.1) × (1-0.2) × (1-0.15) = 0.9 × 0.8 × 0.85 = 0.612

P(at least one fails) = 1 - 0.612 = 0.388

(b) "Exactly one fails" = (Fₐ ∩ Fʙ' ∩ Fc') ∪ (Fₐ' ∩ Fʙ ∩ Fc') ∪ (Fₐ' ∩ Fʙ' ∩ Fc)

These three events are mutually exclusive. Using independence:

P(exactly one fails) = P(Fₐ)P(Fʙ')P(Fc') + P(Fₐ')P(Fʙ)P(Fc') + P(Fₐ')P(Fʙ')P(Fc)
= (0.1 × 0.8 × 0.85) + (0.9 × 0.2 × 0.85) + (0.9 × 0.8 × 0.15)
= 0.068 + 0.153 + 0.108 = 0.329

### Example 3: Database Query Optimization

A database query can use either index scan (I) or sequential scan (S), chosen randomly with probabilities 0.7 and 0.3 respectively. The query succeeds with probability 0.95 using index scan and 0.8 using sequential scan. What is the overall probability of query success?

**Solution:**

Using the law of total probability:
P(Query Success) = P(Success | I) × P(I) + P(Success | S) × P(S)
= 0.95 × 0.7 + 0.8 × 0.3
= 0.665 + 0.24 = 0.905

This example demonstrates how to compute probability of compound events by considering all ways the event can occur—this principle is extensively used in probabilistic algorithms and system reliability analysis.

## Exam Tips

1. **Identify the sample space first**: Before solving any probability problem, clearly define the sample space and ensure it accounts for all possible outcomes.

2. **Use Venn diagrams for complex events**: For problems involving unions, intersections, and complements, drawing a Venn diagram helps visualize the relationships between events.

3. **Apply the complement rule strategically**: For "at least one" type problems, computing P(A') = 1 - P(A) is often simpler than directly computing P(A).

4. **Check for mutual exclusivity**: The addition rule P(A ∪ B) = P(A) + P(B) only applies when A and B are mutually exclusive. Otherwise, use inclusion-exclusion.

5. **Verify probability values**: Always ensure your computed probabilities lie between 0 and 1. Values outside this range indicate an error.

6. **Understand independence vs. mutual exclusivity**: These are distinct concepts—independent events can occur together, while mutually exclusive events cannot. Don't confuse them.

7. **For DU exams, show all working**: Even if you know the answer, display the formula and substitution. This earns partial credit if the final answer is wrong.

8. **Time management**: Allocation-exclusion questions are common in DU papers. Practice solving them within 5-7 minutes to manage exam time effectively.