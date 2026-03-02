# **Naive Bayes Classifier with Add-1 Smoothing**

### Definition and Assumptions

- **Naive Bayes Classifier**: A probabilistic classifier based on Bayes' theorem, assuming independence between features.
- **Add-1 Smoothing**: A technique to handle zero-probability events by adding 1 to the denominator of the Bayes' rule formula.

### Key Points

- **Bayes' Theorem**: P(A|B) = P(B|A) \* P(A) / P(B)
- **Naive Bayes Classifier**: P(A|B) = P(B|A) \* P(A) / Σ P(A|B) \* P(B)
- **Add-1 Smoothing**: P(A|B) = P(B|A) \* P(A) / (P(B|A) \* P(A) + 1)
- **Definition of Probability**: P(A) = K / N, where K is the number of occurrences of A and N is the total number of instances.

### Formulas and Theorems

- **Bayes' Rule**: P(A|B) = P(B|A) \* P(A) / P(B)
- **Naive Bayes Formula**: P(A|B) = P(B|A) \* P(A)
- **Add-1 Smoothing Formula**: P(A|B) = P(B|A) \* P(A) / (P(B|A) \* P(A) + 1)

### Important Concepts

- **Independence**: Features are independent of each other, P(A|B) = P(A) \* P(B|A)
- **Zero-Probability Event**: Handling events with zero probability using add-1 smoothing

### Revision Notes

- Understand the Naive Bayes classifier and its assumptions
- Familiarize yourself with Bayes' theorem and the add-1 smoothing technique
- Review the formulas and theorems related to the topic
- Practice applying the formulas to different scenarios

Note: This summary is a concise revision guide, focusing on the key points and formulas related to the topic. It is not intended to be a comprehensive overview of the subject.
