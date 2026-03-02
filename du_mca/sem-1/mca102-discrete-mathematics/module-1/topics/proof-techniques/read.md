# Proof Techniques

## Introduction
Proof techniques form the backbone of discrete mathematics and are essential for establishing the validity of mathematical statements in computer science. In algorithm design, cryptography, and formal verification, rigorous proofs ensure correctness and security. This topic introduces formal methods to demonstrate why a particular statement must be true under given conditions.

Modern computing relies on proof methods like mathematical induction for recursive algorithms, contradiction for security protocol validation, and contrapositive for optimizing logical circuits. For example, induction proofs verify loop invariants in sorting algorithms, while contradiction proofs expose vulnerabilities in cryptographic systems. Mastering these techniques enables MCA students to design error-resistant systems and communicate technical arguments effectively.

## Key Concepts

1. **Direct Proof**  
   - Constructed by assuming the hypothesis and logically deducing the conclusion.  
   - Example: Prove "If n is even, then n² is even" by writing n=2k ⇒ n²=4k²=2(2k²).

2. **Contrapositive Proof**  
   - Proves "If P then Q" by showing "¬Q ⇒ ¬P" using logical equivalence (P → Q ≡ ¬Q → ¬P).  
   - Example: Prove "If 3n+2 is odd, then n is odd" by contrapositive: If n is even, 3n+2 is even.

3. **Proof by Contradiction**  
   - Assume the negation of the statement and derive a contradiction.  
   - Example: Prove √2 is irrational by assuming √2 = a/b (reduced fraction) ⇒ 2b² = a² ⇒ both a,b even (contradiction).

4. **Mathematical Induction**  
   - **Base Case**: Verify statement for initial value (n=1).  
   - **Inductive Step**: Assume true for n=k (inductive hypothesis), prove for n=k+1.  
   - Example: Prove 1 + 2 + ... + n = n(n+1)/2.

5. **Constructive vs Non-Constructive Proofs**  
   - Constructive: Explicitly finds a solution (e.g., finding an algorithm).  
   - Non-Constructive: Proves existence without providing an example (e.g., probabilistic methods).

## Examples

**Example 1: Induction for Summation Formula**  
*Prove 1³ + 2³ + ... + n³ = (n(n+1)/2)²*  
**Base Case**: n=1 ⇒ 1³ = 1 = (1×2/2)² ✔️  
**Inductive Step**:  
Assume true for n=k: S(k) = (k(k+1)/2)²  
For n=k+1:  
S(k+1) = S(k) + (k+1)³  
= (k²(k+1)²)/4 + (k+1)³  
= (k+1)²[k²/4 + (k+1)]  
= (k+1)²(k² + 4k + 4)/4  
= ((k+1)(k+2)/2)² ✔️

**Example 2: Contradiction in Cryptography**  
*Prove: No prime p > 2 divides both n and n+1*  
Assume ∃ prime p>2 dividing n and n+1.  
Then p | (n+1 - n) ⇒ p | 1 ⇒ Contradiction (primes >1 cannot divide 1).

**Example 3: Contrapositive in Algorithms**  
*Prove: If a graph has no cycles, then adding an edge creates exactly one cycle.*  
Contrapositive: If adding an edge creates ≥2 cycles, original graph had a cycle.  
Proof: Two new cycles ⇒ common edge e. Removing e leaves a cycle in original graph. Contradiction.

## Exam Tips
1. **Identify proof type early**: Check if statement is universal ("for all") or existential ("there exists").
2. **Induction pitfalls**: Always state inductive hypothesis clearly; verify base case for n=0 if required.
3. **Contrapositive vs. Contradiction**: Contrapositive retains original statement's quantifiers; contradiction introduces absurdity.
4. **Quantifier errors**: For "∀x∃y" statements, y can depend on x; reverse quantifiers change meaning.
5. **Counterexamples**: To disprove ∀x P(x), find one x where P(x) fails.
6. **Algorithmic proofs**: Use loop invariants (induction on iterations) for correctness proofs.
7. **Write clearly**: Use phrases like "Assume for contradiction..." or "By induction hypothesis..." for structure.