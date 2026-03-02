# **Naive Bayes Classifier**

**Definition**: A family of probabilistic classifiers based on Bayes' theorem, assuming independence between features.

**Key Points**:

- Naive Bayes is a supervised learning algorithm used for text classification tasks.
- It's based on Bayes' theorem and assumes conditional independence between features.
- The algorithm uses a prior probability distribution and conditional probability distributions to classify text.

## **Worked Example: Sentiment Analysis**

- **Formulas**:
  - Prior probability: P(class) = P(class) / P(total)
  - Conditional probability: P(feature|class) = P(feature, class) / P(class)
- **Steps**:
  1.  Preprocess text data: tokenize, remove stop words, lemmatize.
  2.  Calculate prior probability: P(class) = P(class) / P(total)
  3.  Calculate conditional probability: P(feature|class) = P(feature, class) / P(class)
  4.  Calculate posterior probability: P(class|feature) = P(feature|class) \* P(class) / P(feature)
  5.  Classify text: choose class with highest posterior probability

## **Optimizing for Sentiment Analysis**

- **Features**: use word embeddings (e.g. Word2Vec, GloVe) or TF-IDF.
- **Weights**: use Laplace smoothing or symmetric Laplace smoothing.
- **Regularization**: use L1 or L2 regularization for feature selection.

## **Naive Bayes for Other Text Classification Tasks**

- **Multi-class classification**: use multi-class Naive Bayes or one-vs-rest approach.
- **Multi-label classification**: use multi-label Naive Bayes or bagging.

## **Naive Bayes as a Language**

- **Language modeling**: use Naive Bayes to model language probability distributions.
- **Language generation**: use Naive Bayes to generate text based on language models.

**Important Formulas and Theorems**:

- Bayes' theorem: P(A|B) = P(B|A) \* P(A) / P(B)
- Conditional probability: P(A|B) = P(A, B) / P(B)
- Laplace smoothing: P(A) ≈ P(A) + k / N
