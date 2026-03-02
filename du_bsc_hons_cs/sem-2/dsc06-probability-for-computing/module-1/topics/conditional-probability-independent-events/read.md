# Conditional Probability and Independent Events

## Introduction

Conditional probability is one of the most fundamental concepts in probability theory and serves as the backbone for understanding advanced topics in data science, machine learning, and artificial intelligence. In real-world scenarios, we rarely deal with isolated events; instead, the occurrence of one event often provides valuable information about the likelihood of another event happening. For instance, knowing that a patient tests positive for a disease changes the probability that they actually have the disease—a classic application of Bayes' theorem built upon conditional probability.

The concept of independence, on the other hand, captures the intuitive notion of events that do not influence each other. In computing applications, understanding whether events are independent is crucial for designing efficient algorithms, analyzing network reliability, and building probabilistic models. From spam email classification using Naive Bayes classifiers to recommendation systems, conditional probability and independence form the mathematical foundation upon which modern intelligent systems operate.

This topic becomes particularly important in the context of University of Delhi's Data Science curriculum, where students must master these concepts to excel in courses on statistical learning, data mining, and artificial intelligence. The internal assessment and end semester examinations frequently test students' ability to compute conditional probabilities, identify independent events, and apply these concepts to solve real-world problems.

## Key Concepts

### Conditional Probability

The conditional probability of an event A given that event B has occurred is denoted by P(A|B) and is defined as:

**P(A|B) = P(A ∩ B) / P(B)**, provided that P(B) > 0

This definition arises naturally from the concept of restricting our sample space to the outcomes where event B occurs. When we condition on B, we are essentially asking: "Among all the outcomes where B occurs, what fraction also has A occurring?" The intersection A ∩ B represents the favorable outcomes where both events occur.

**Properties of Conditional Probability:**

1. **P(A|B) ≥ 0** for any event A
2. **P(S|B) = 1** where S is the sample space
3. **P(A ∪ C|B) = P(A|B) + P(C|B) - P(A ∩ C|B)** for any two events A and C
4. **P(∅|B) = 0** where ∅ is the empty set

**Multiplication Rule:** From the definition of conditional probability, we derive the multiplication rule:
**P(A ∩ B) = P(B) × P(A|B) = P(A) × P(B|A)**

This rule extends to multiple events: P(A ∩ B ∩ C) = P(A) × P(B|A) × P(C|A ∩ B)

### Independent Events

Two events A and B are said to be independent if and only if:

**P(A ∩ B) = P(A) × P(B)**

Equivalently, independence can be expressed as:
- **P(A|B) = P(A)** when P(B) > 0
- **P(B|A) = P(B)** when P(A) > 0

The intuition behind independence is that knowing one event has occurred does not change the probability of the other event occurring. The occurrence of B provides no information about A.

**Mutual Independence:** Events A, B, and C are mutually independent if:
- P(A ∩ B) = P(A) × P(B)
- P(A ∩ C) = P(A) × P(C)
- P(B ∩ C) = P(B) × P(C)
- P(A ∩ B ∩ C) = P(A) × P(B) × P(C)

The last condition is crucial—it is possible for events to be pairwise independent but not mutually independent, a distinction that students must understand clearly.

### Law of Total Probability

If events B₁, B₂, ..., Bₙ form a partition of the sample space S (i.e., they are mutually exclusive and exhaustive), then for any event A:

**P(A) = Σ P(A|Bᵢ) × P(Bᵢ)** for i = 1 to n

This law is particularly useful when we know the conditional probabilities of A given each partition event but not directly P(A).

### Bayes' Theorem

One of the most powerful results in probability theory, Bayes' theorem allows us to "invert" conditional probabilities:

**P(Bᵢ|A) = P(A|Bᵢ) × P(Bᵢ) / Σ P(A|Bⱼ) × P(Bⱼ)** for all j

Here, P(Bᵢ) are called prior probabilities (before observing A), and P(Bᵢ|A) are called posterior probabilities (after observing A). This theorem has profound applications in medical diagnosis, spam filtering, and machine learning classification.

## Examples

### Example 1: Computing Conditional Probability

**Problem:** In a class of 60 students, 25 study Python, 30 study R, and 10 study both Python and R. A student is selected at random. If the selected student studies Python, what is the probability that they also study R?

**Solution:**

Given:
- Total students = 60
- P(Python) = 25/60
- P(R) = 30/60
- P(Python ∩ R) = 10/60

We need to find P(R|Python) = P(Python ∩ R) / P(Python)

P(R|Python) = (10/60) / (25/60) = 10/25 = 2/5 = 0.4

Therefore, the probability that a student studies R given that they study Python is 0.4 or 40%.

### Example 2: Testing Independence

**Problem:** A fair die is rolled. Let A be the event "roll is even" and B be the event "roll is greater than 3". Determine whether A and B are independent.

**Solution:**

Sample space S = {1, 2, 3, 4, 5, 6}

Event A (even): {2, 4, 6}, so P(A) = 3/6 = 1/2

Event B (>3): {4, 5, 6}, so P(B) = 3/6 = 1/2

Intersection A ∩ B = {4, 6}, so P(A ∩ B) = 2/6 = 1/3

Check independence: P(A) × P(B) = (1/2) × (1/2) = 1/4 = 0.25

Since P(A ∩ B) = 1/3 ≈ 0.333 ≠ 0.25, events A and B are NOT independent.

Alternatively, check: P(B|A) = P(A ∩ B)/P(A) = (1/3)/(1/2) = 2/3

Since P(B|A) = 2/3 ≠ P(B) = 1/2, the events are not independent.

### Example 3: Application of Bayes' Theorem

**Problem:** A diagnostic test for a disease has a 95% accuracy rate for sick patients (sensitivity) and a 90% accuracy rate for healthy patients (specificity). If 2% of the population has the disease, what is the probability that a person who tests positive actually has the disease?

**Solution:**

Let D = "has disease", D' = "does not have disease"
Let T+ = "tests positive"

Given:
- P(D) = 0.02 (prior probability of disease)
- P(D') = 0.98
- P(T+|D) = 0.95 (sensitivity)
- P(T+|D') = 1 - 0.90 = 0.10 (false positive rate)

Using Bayes' theorem:
P(D|T+) = P(T+|D) × P(D) / [P(T+|D) × P(D) + P(T+|D') × P(D')]

P(D|T+) = (0.95 × 0.02) / [(0.95 × 0.02) + (0.10 × 0.98)]
= 0.019 / (0.019 + 0.098)
= 0.019 / 0.117
≈ 0.1624 or 16.24%

This surprising result (only 16% chance despite 95% accuracy) demonstrates the importance of considering base rates—the low prevalence of the disease means many false positives occur. This principle is crucial in medical diagnosis and is a common question in DU examinations.

## Exam Tips

1. **Always verify the denominator is non-zero** when computing conditional probabilities. The formula P(A|B) = P(A ∩ B)/P(B) requires P(B) > 0.

2. **Distinguish between "and" and "or"**: P(A ∩ B) requires both events to occur, while P(A ∪ B) requires at least one to occur. Use the addition rule: P(A ∪ B) = P(A) + P(B) - P(A ∩ B).

3. **Check independence using the correct criterion**: Many students mistakenly use P(A|B) = P(B|A) for independence. The correct conditions are P(A ∩ B) = P(A) × P(B) or equivalently P(A|B) = P(A).

4. **Draw Venn diagrams** for visual understanding of intersections and unions. This is particularly helpful in problems involving "at least one" type questions.

5. **For Bayes' theorem problems**, clearly identify: what is the evidence (event A), what are the hypotheses (events Bᵢ), what are the prior probabilities P(Bᵢ), and what are the likelihoods P(A|Bᵢ).

6. **Remember that "mutual independence" is stronger than "pairwise independence"**: Three events can be pairwise independent (each pair satisfies independence) but not mutually independent.

7. **The complement rule is your friend**: Often it's easier to compute P(A') and then use P(A) = 1 - P(A'). This is especially useful in "at least one" problems.

8. **Practice problems from previous years**: DU exam questions frequently involve card problems, dice problems, and real-world scenarios like medical testing or quality control.

9. **Understand the multiplication rule extension**: For n independent events, P(A₁ ∩ A₂ ∩ ... ∩ Aₙ) = P(A₁) × P(A₂) × ... × P(Aₙ).

10. **Pay attention to wording**: "Given that" indicates conditional probability, while "and" indicates intersection.