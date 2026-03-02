# **Textbook 2: Ch - Naive Bayes Classifiers**

## **Key Points**

- **Definition:** Naive Bayes classifier is a family of probabilistic classifiers based on Bayes' theorem.
- **Assumptions:**
  - Independence of features (conditional independence)
  - Multinomial distribution for categorical features
  - Bernoulli distribution for binary features
- **Training:**
  - Calculate prior probabilities (P(C))
  - Calculate conditional probabilities (P(X|C))
  - Calculate posterior probabilities (P(X|C'))
- **Naive Bayes Formulas:**
  - **P(C)**: Prior probability of class C
  - **P(X|C)**: Conditional probability of feature X given class C
  - **P(X|C')**: Conditional probability of feature X given class C'
  - **P(X)**: Prior probability of feature X
  - **P(X|C)** = P(X) \* P(C|X)
  - **P(C|X)** = P(X|C) / P(X)
- **Text Classification:**
  - **Naive Bayes Classifier:** Classify text into categories based on feature counts (e.g., words, phrases)
  - **Spam/Not Spam:** Classify emails as spam or not spam
- **Sentiment Analysis:**
  - **Naive Bayes Classifier:** Classify text as positive, negative, or neutral sentiment

## **Important Formulas and Definitions:**

- **Bayes' Theorem:** P(C|X) = P(X|C) \* P(C) / P(X)
- **Conditional Independence:** P(X|C) = P(X) \* P(C|X)
- **Multinomial Distribution:** P(X|C) = P(x1, x2, ..., xn | C) = (n! / (x1! _ x2! _ ... _ xn!)) _ (P(c1))^x1 _ (P(c2))^x2 _ ... \* (P(cn))^xn
- **Bernoulli Distribution:** P(X|C) = P(x | C) \* P(c | x)
