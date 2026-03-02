# **The Pumping Lemma for Context-Free Languages**

## **Overview**

The Pumping Lemma is a theoretical result used to prove that a language is not context-free. It was formulated by Stephen Cook in 1971.

## **Key Points**

- **Definition:** A language $L$ is context-free if and only if there exists an algorithm that can pump a string $w$ in $L$ to produce a new string $w' = w^i w^j$, where $i > 0$, $j > 0$, and $1 \leq i + j \leq k$ for some integer $k$, such that $w' \in L$.
- **Pumping Lemma:** If $L$ is context-free, then there exist integers $p$ and $k$ such that:
  - Any string $w$ in $L$ with length at least $p$ can be divided into three substrings $w = xyz$ such that:
    - $|y| \geq 1$
    - $|x| \geq 1$
    - $|z| \geq 1$
  - For all non-negative integers $i$ and $j$ such that $1 \leq i + j \leq k$, the string $w^i x z^j$ is in $L$.

## **Important Formulas and Definitions**

- **Context-free grammar:** A grammar $G = (V, \Sigma, P, S)$ is context-free if and only if for all $A \in V$ and all $w \in \Sigma^*$, $A \rightarrow w$ or $A \rightarrow \epsilon$ or $A \rightarrow A \cdot w$ for some $A' \in V$ and $w \in \Sigma^*$.
- **Chomsky normal form:** A grammar $G = (V, \Sigma, P, S)$ is in Chomsky normal form if and only if:
  - Every production is of the form $A \rightarrow aB$ for some $A, B \in V$ and $a \in \Sigma$.
  - $S$ is not associated with any production.

## **Theorems**

- **Pumping Lemma for context-free languages:** If $L$ is context-free, then the pumping lemma holds.
- **Undecidability of context-free languages:** If the pumping lemma holds for a language $L$, then $L$ is undecidable.

## **Revision Tips**

- Focus on understanding the definition of context-free languages and the pumping lemma.
- Practice solving problems that illustrate the pumping lemma.
- Review the key points and formulas to refresh your memory.
