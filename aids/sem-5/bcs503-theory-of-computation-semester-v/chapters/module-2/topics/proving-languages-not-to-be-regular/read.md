# Proving Languages Not to be Regular
## Introduction
In the theory of computation, regular languages are a fundamental concept. They are languages that can be recognized by a finite automaton, which is a simple computational model. However, not all languages are regular. In this chapter, we will learn how to prove that a language is not regular.

## The Pumping Lemma
The pumping lemma is a powerful tool for proving that a language is not regular. It states that if a language is regular, then there exists a pumping length $p$ such that any string $w$ in the language with length at least $p$ can be divided into three parts $w = xyz$ such that:

* $|y| > 0$
* $|xy| \leq p$
* For all $i \geq 0$, $xy^iz$ is in the language

If a language does not satisfy the pumping lemma, then it is not regular.

## Example 1: The Language $L = \{a^nb^n | n \geq 0\}$
This language is not regular. To prove it, we can use the pumping lemma. Assume that $L$ is regular, and let $p$ be the pumping length. Consider the string $w = a^pb^p$. Since $|w| \geq p$, we can divide $w$ into three parts $w = xyz$ such that $|y| > 0$ and $|xy| \leq p$.

Since $|y| > 0$, $y$ must contain at least one $a$. Let $y = a^k$ for some $k > 0$. Then $xy^2z = a^{p+k}b^p$, which is not in $L$. This contradicts the pumping lemma, so $L$ is not regular.

## Example 2: The Language $L = \{ww | w \in \{a, b\}^*\}$
This language is also not regular. To prove it, we can use the pumping lemma again. Assume that $L$ is regular, and let $p$ be the pumping length. Consider the string $w = (ab)^p(ab)^p$. Since $|w| \geq p$, we can divide $w$ into three parts $w = xyz$ such that $|y| > 0$ and $|xy| \leq p$.

Since $|y| > 0$, $y$ must contain at least one $a$ or $b$. Let $y = a^kb^l$ for some $k, l \geq 0$. Then $xy^2z = (ab)^p(ab)^{k+l}(ab)^p$, which is not in $L$. This contradicts the pumping lemma, so $L$ is not regular.

## Comparison of Regular and Non-Regular Languages
| Language | Regular | Non-Regular |
| --- | --- | --- |
| $L = \{a^n | n \geq 0\}$ | Yes | No |
| $L = \{a^nb^n | n \geq 0\}$ | No | Yes |
| $L = \{ww | w \in \{a, b\}^*\}$ | No | Yes |

## Exam Tips
* To prove that a language is not regular, use the pumping lemma.
* Choose a string $w$ in the language with length at least $p$.
* Divide $w$ into three parts $w = xyz$ such that $|y| > 0$ and $|xy| \leq p$.
* Show that $xy^iz$ is not in the language for some $i \geq 0$.