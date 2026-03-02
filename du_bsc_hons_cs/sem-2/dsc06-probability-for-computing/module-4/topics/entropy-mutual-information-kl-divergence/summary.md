# Entropy, Mutual Information & KL Divergence

**Subject:** Probability For Computing | **Course:** BSc (Hons) Computer Science - Delhi University (NEP 2024 UGCF)

---

## Introduction

These are fundamental concepts from **Information Theory** (Shannon's theory), essential for understanding data compression, machine learning algorithms, and statistical inference. They quantify "information" or "uncertainty" in probability distributions.

---

## Key Concepts

### **1. Entropy (Shannon Entropy)**
- Measures the **uncertainty** or **randomness** in a probability distribution
- For a discrete random variable X with probability distribution P(x):
  
  **H(X) = -Σ P(x) log₂ P(x)**
  
  (using log base 2; units: bits)
- **Properties:**
  - H(X) ≥ 0 (zero when outcome is certain)
  - Maximum entropy when distribution is uniform
  - H(X, Y) = H(X) + H(Y) for independent variables

### **2. Joint Entropy & Conditional Entropy**
- **Joint Entropy:** H(X, Y) = -ΣΣ P(x,y) log P(x,y)
- **Conditional Entropy:** H(Y|X) = Σ P(x) H(Y|X=x)
- **Chain Rule:** H(X, Y) = H(X) + H(Y|X)

### **3. Mutual Information**
- Measures the **dependence** between two random variables
- Quantifies how much information one variable provides about another
- **Formula:** I(X; Y) = H(X) + H(Y) - H(X, Y)
- **Alternative:** I(X; Y) = H(Y) - H(Y|X) = H(X) - H(X|Y)
- **Properties:**
  - I(X; Y) ≥ 0
  - I(X; Y) = 0 if X and Y are independent
  - I(X; X) = H(X)

### **4. KL Divergence (Kullback-Leibler Divergence)**
- Measures how one probability distribution **P** differs from another **Q**
- Also called **relative entropy**
- **Formula:** DKL(P || Q) = Σ P(x) log [P(x)/Q(x)]
- **Properties:**
  - DKL(P || Q) ≥ 0 (Gibbs' inequality)
  - DKL(P || Q) ≠ DKL(Q || P) (asymmetric)
  - Zero only when P = Q
- **Interpretation:** Information lost when Q is used to approximate P

---

## Relationships Between Measures

```
H(X) ──────┐
           ├──→ I(X; Y) ──→ H(Y|X)
H(Y) ──────┘         │
                     ↓
              H(Y) ──┬──→ DKL(P||Q)
                     │
              H(X|Y)
```

---

## Applications in Computing

- **Data Compression:** Huffman coding, Shannon-Fano coding
- **Machine Learning:** Feature selection, classification, NLP
- **Pattern Recognition:** Information gain for decision trees
- **Communications:** Channel capacity, error detection

---

## Conclusion

Entropy, Mutual Information, and KL Divergence form the mathematical foundation of information theory. They provide essential tools for measuring uncertainty, dependence, and distribution differences—critical for data science, algorithms, and modern computing applications as per the Delhi University syllabus.