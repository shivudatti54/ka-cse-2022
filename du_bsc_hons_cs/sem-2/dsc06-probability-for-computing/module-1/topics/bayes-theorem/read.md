# Bayes' Theorem

## Introduction

Bayes' Theorem is one of the most fundamental and powerful concepts in probability theory, serving as the backbone of modern artificial intelligence, machine learning, and statistical inference. Named after the Reverend Thomas Bayes, an 18th-century mathematician and Presbyterian minister, this theorem provides a mathematical framework for updating the probability of a hypothesis when new evidence is observed. In the context of computing, Bayes' Theorem forms the foundation of Bayesian networks, spam filtering algorithms, medical diagnosis systems, and numerous other applications that modern computer scientists encounter daily.

For students at the University of Delhi studying Computer Science under the NEP 2024 framework, understanding Bayes' Theorem is not merely an academic exercise but an essential skill for careers in data science, artificial intelligence, and software development. The theorem elegantly solves the problem of "inverse probability" - determining the probability of a cause given an observed effect. When you receive an email marked as "spam," behind that classification lies Bayes' Theorem working to calculate the probability that the email is spam given its content. When your phone's autocorrect predicts the word you're likely typing, Bayes' Theorem is operating in the background. This makes the topic both theoretically significant and practically indispensable.

## Key Concepts

### Understanding Conditional Probability

Before diving into Bayes' Theorem, it is crucial to master conditional probability, which represents the probability of an event occurring given that another event has already occurred. We denote P(A|B) as the probability of event A occurring given that event B has occurred. The fundamental relationship is expressed as:

**P(A|B) = P(A ∩ B) / P(B)**, provided P(B) > 0

This relationship tells us that the conditional probability of A given B equals the joint probability of A and B divided by the probability of B. Similarly, P(B|A) = P(A ∩ B) / P(A).

### The Chain Rule and Joint Probability

The joint probability of two events A and B can be expressed in two ways using the chain rule:

**P(A ∩ B) = P(A|B) × P(B) = P(B|A) × P(A)**

This simple yet powerful relationship is the key to deriving Bayes' Theorem.

### Statement of Bayes' Theorem

Bayes' Theorem states that for two events A and B, where P(B) > 0:

**P(A|B) = [P(B|A) × P(A)] / P(B)**

In more general terms, if we have a hypothesis H and evidence E:

**P(H|E) = [P(E|H) × P(H)] / P(E)**

Where:
- **P(H)** is the prior probability - our initial belief about the hypothesis before seeing evidence
- **P(E|H)** is the likelihood - probability of observing the evidence given the hypothesis is true
- **P(E)** is the marginal likelihood - total probability of observing the evidence under all possible hypotheses
- **P(H|E)** is the posterior probability - our updated belief about the hypothesis after considering the evidence

### The Law of Total Probability

To apply Bayes' Theorem effectively, we often need to calculate P(E), the marginal probability of the evidence. When the sample space can be partitioned into mutually exclusive and exhaustive events H₁, H₂, ..., Hₙ, the law of total probability states:

**P(E) = Σ P(E|Hᵢ) × P(Hᵢ)** for i = 1 to n

This allows us to compute the total probability of evidence by considering all possible ways the evidence could occur.

### Naive Bayes Classification

One of the most important applications of Bayes' Theorem in computing is the Naive Bayes classifier. Despite its "naive" assumption of feature independence (which is rarely true in real data), this algorithm performs remarkably well in many practical applications including text classification, spam filtering, and sentiment analysis. For a document classification problem with classes C and features F₁, F₂, ..., Fₙ:

**P(C|F₁, F₂, ..., Fₙ) ∝ P(C) × Πᵢ P(Fᵢ|C)**

The classifier calculates the posterior probability for each class and selects the class with the highest posterior probability.

## Examples

### Example 1: Medical Diagnosis (Classic Application)

**Problem:** A certain disease affects 1% of the population. A test for the disease is 95% accurate (meaning it correctly identifies diseased individuals 95% of the time and correctly identifies healthy individuals 95% of the time). If a person tests positive, what is the probability they actually have the disease?

**Solution:**

Let D = "has the disease"
Let T+ = "tests positive"

Given information:
- P(D) = 0.01 (prior probability of having the disease)
- P(T+|D) = 0.95 (sensitivity/true positive rate)
- P(T+|D̄) = 0.05 (false positive rate), therefore P(T-|D̄) = 0.95

We need to find: P(D|T+) = ?

Using Bayes' Theorem:
P(D|T+) = [P(T+|D) × P(D)] / P(T+)

First, calculate P(T+) using the law of total probability:
P(T+) = P(T+|D) × P(D) + P(T+|D̄) × P(D̄)
P(T+) = (0.95 × 0.01) + (0.05 × 0.99)
P(T+) = 0.0095 + 0.0495 = 0.059

Now apply Bayes' Theorem:
P(D|T+) = (0.95 × 0.01) / 0.059
P(D|T+) = 0.0095 / 0.059 ≈ 0.161

**Answer:** Despite testing positive, there is only approximately a 16.1% chance the person actually has the disease. This surprising result illustrates the importance of considering the base rate (prior probability).

### Example 2: Spam Email Classification

**Problem:** In an email system, 30% of emails are spam. The word "free" appears in 60% of spam emails and in 10% of legitimate emails. If an email contains the word "free", what is the probability it is spam?

**Solution:**

Let S = "email is spam"
Let F = "email contains the word 'free'"

Given:
- P(S) = 0.30 (prior probability of spam)
- P(F|S) = 0.60 (likelihood for spam)
- P(F|S̄) = 0.10 (false positive for non-spam)

We need: P(S|F) = ?

Using Bayes' Theorem:
P(S|F) = [P(F|S) × P(S)] / P(F)

Calculate P(F):
P(F) = P(F|S) × P(S) + P(F|S̄) × P(S̄)
P(F) = (0.60 × 0.30) + (0.10 × 0.70)
P(F) = 0.18 + 0.07 = 0.25

Now:
P(S|F) = (0.60 × 0.30) / 0.25
P(S|F) = 0.18 / 0.25 = 0.72

**Answer:** If an email contains "free", there is a 72% probability it is spam. This forms the basis of simple spam filters.

### Example 3: Algorithm Performance Analysis

**Problem:** Two algorithms A and B are used to solve a problem. Algorithm A succeeds 80% of the time, while Algorithm B succeeds 60% of the time. Algorithm A is used 40% of the time, and Algorithm B is used 60% of the time. If a run is successful, what is the probability that Algorithm A was used?

**Solution:**

Let A = "Algorithm A was used"
Let B = "Algorithm B was used" (note: A and B are complements)
Let S = "the run was successful"

Given:
- P(A) = 0.40, P(B) = 0.60
- P(S|A) = 0.80
- P(S|B) = 0.60

We need: P(A|S) = ?

Using Bayes' Theorem:
P(A|S) = [P(S|A) × P(A)] / P(S)

Calculate P(S):
P(S) = P(S|A) × P(A) + P(S|B) × P(B)
P(S) = (0.80 × 0.40) + (0.60 × 0.60)
P(S) = 0.32 + 0.36 = 0.68

Now:
P(A|S) = (0.80 × 0.40) / 0.68
P(A|S) = 0.32 / 0.68 ≈ 0.471

**Answer:** Given a successful run, there is approximately a 47.1% probability that Algorithm A was used.

## Exam Tips

1. **Identify Events Clearly:** In exam questions, carefully identify what represents the hypothesis (A) and what represents the evidence (B). The question typically asks for P(Hypothesis|Evidence).

2. **Calculate Marginal Probability Correctly:** The denominator P(B) is crucial. Use the law of total probability when the evidence can occur under multiple mutually exclusive scenarios.

3. **Remember the Meaning of Terms:** P(A) is the prior (before evidence), P(A|B) is the posterior (after evidence). Understand the flow of information updating.

4. **Watch for Base Rate Neglect:** In medical and security applications, always consider the base rate (prior probability). A highly accurate test can still produce many false positives if the condition is rare.

5. **Practice Reverse Calculation:** Questions often ask for the reverse probability. If given P(A|B), you may need to calculate P(B|A). Set up the Bayes' formula correctly.

6. **Use Tree Diagrams for Complex Problems:** For problems with multiple stages or conditions, drawing a probability tree can help organize information and avoid errors.

7. **Check Your Answers:** The posterior probability P(A|B) should always be between 0 and 1. Also, P(A|B) + P(Ā|B) should equal 1.

8. **Application-Based Questions are Frequent:** DU exams often include application-based questions in spam detection, medical diagnosis, or quality control. Focus on understanding how to translate word problems into probability notation.

9. **Understand the Naive Assumption:** For Naive Bayes classification, remember the independence assumption that allows multiplication of individual feature probabilities.

10. **Time Management:** Bayes' Theorem problems can become computationally intensive. Practice enough problems to become efficient at calculations, especially with decimals and percentages.