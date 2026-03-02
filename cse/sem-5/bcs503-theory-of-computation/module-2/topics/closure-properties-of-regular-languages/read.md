# Closure Properties of Regular Languages

## Introduction

Closure properties constitute one of the most elegant and theoretically significant characteristics of regular languages within the Chomsky hierarchy. A class of languages is said to be **closed** under a particular operation if, whenever we apply that operation to languages within the class, the resulting language also belongs to the same class. In other words, the operation does not take us outside the boundary of the language family.

For regular languages, this property manifests in remarkable breadth—we can demonstrate that regular languages remain regular under union, intersection, complement, concatenation, Kleene star, reversal, homomorphism, inverse homomorphism, and quotient operations. These closure properties serve dual purposes in the theoretical foundations of automata theory: they provide powerful analytical tools for understanding the structural limitations of regular languages, and they furnish rigorous techniques for proving that certain languages fall outside the regular family.

The practical implications of closure properties extend substantially into compiler design, where lexical analyzers employ regular expressions to define token patterns; in text processing applications requiring pattern matching; and in digital circuit design where regular languages model sequential behavior. Furthermore, closure properties under complement and intersection enable sophisticated non-regularity proofs that complement the pumping lemma methodology.

## 1. Closure Under Union

**Theorem:** If L₁ and L₂ are regular languages over alphabet Σ, then L₁ ∪ L₂ is also regular.

**Proof:** Since L₁ and L₂ are regular, there exist deterministic finite automata (DFAs) M₁ = (Q₁, Σ, δ₁, q₁, F₁) and M₂ = (Q₂, Σ, δ₂, q₂, F₂) recognizing them. We construct a product automaton M = (Q, Σ, δ, q₀, F) that simulates both machines simultaneously, using the Cartesian product of their state spaces.

The construction proceeds as follows:

- The set of states Q = Q₁ × Q₂ (all ordered pairs where the first component is a state of M₁ and the second is a state of M₂)
- The start state q₀ = (q₁, q₂)
- The transition function δ: Q × Σ → Q is defined by δ((p, a), a) = (δ₁(p, a), δ₂(q, a)) for all p ∈ Q₁, q ∈ Q₂, and a ∈ Σ
- The set of accepting states F = (F₁ × Q₂) ∪ (Q₁ × F₂)

This DFA accepts a string w if and only if after processing w, either the first component reaches an accepting state in M₁ or the second component reaches an accepting state in M₂ (or both). Therefore, L(M) = L₁ ∪ L₂. Since we have explicitly constructed a DFA recognizing the union, closure under union is established. ∎

## 2. Closure Under Intersection

**Theorem:** If L₁ and L₂ are regular languages over alphabet Σ, then L₁ ∩ L₂ is also regular.

**Proof:** We employ the same product automaton construction used for union, but with a fundamentally different accepting condition. Given DFAs M₁ = (Q₁, Σ, δ₁, q₁, F₁) and M₂ = (Q₂, Σ, δ₂, q₂, F₂) recognizing L₁ and L₂ respectively, we construct M = (Q, Σ, δ, q₀, F) where:

- Q = Q₁ × Q₂
- q₀ = (q₁, q₂)
- δ((p, q), a) = (δ₁(p, a), δ₂(q, a))
- F = F₁ × F₂ (the set of pairs where both components are accepting)

For a string w to be accepted by M, after processing w, the first component must be in an accepting state of M₁ AND the second component must be in an accepting state of M₂. This precisely corresponds to w ∈ L₁ ∩ L₂. Thus, L(M) = L₁ ∩ L₂, establishing closure under intersection. ∎

## 3. Closure Under Complement

**Theorem:** If L is a regular language over alphabet Σ, then its complement L̄ = Σ\* - L is also regular.

**Proof:** Let M = (Q, Σ, δ, q₀, F) be a DFA recognizing L. We construct a new DFA M' = (Q, Σ, δ, q₀, Q - F) that recognizes the complement. Critically, this construction requires M to be a deterministic complete automaton—every state must have defined transitions for all input symbols.

The key insight is that M' accepts exactly those strings that M rejects: for any string w ∈ Σ*, M accepts w if and only if the state reached after processing w belongs to F; conversely, M' accepts w if and only if the state reached belongs to Q - F. Therefore, L(M') = Σ* - L = L̄. Since we have constructed a DFA for the complement, regular languages are closed under complementation. ∎

## 4. Closure Under Set Difference

**Theorem:** If L₁ and L₂ are regular languages, then L₁ - L₂ is also regular.

**Proof:** The set difference operation can be expressed through combination of previously established closure properties. Observe that:

L₁ - L₂ = L₁ ∩ L̄₂

Since L₂ is regular, L̄₂ is regular by closure under complement. Both L₁ and L̄₂ are regular, so their₁ ∩ L intersection L̄₂ is regular by closure under intersection. Therefore, L₁ - L₂ is regular. ∎

## 5. Closure Under Concatenation

**Theorem:** If L₁ and L₂ are regular languages, then their concatenation L₁L₂ = {xy | x ∈ L₁, y ∈ L₂} is also regular.

**Proof:** Let M₁ = (Q₁, Σ, δ₁, q₁, F₁) and M₂ = (Q₂, Σ, δ₂, q₂, F₂) be NFAs (nondeterministic finite automata) recognizing L₁ and L₂ respectively. We construct an NFA M for L₁L₂ as follows:

- The states of M are Q₁ ∪ Q₂
- The start state is q₁ (the start state of M₁)
- The accepting states are F₂ (the accepting states of M₂)
- Add ε-transitions (empty string transitions) from every state in F₁ to the start state q₂ of M₂

The intuition is that to recognize a string in L₁L₂, the NFA first consumes a prefix that takes M₁ from its start state to some accepting state (thereby recognizing a string in L₁), then uses an ε-transition to move to the start state of M₂, and finally processes the remaining suffix to reach an accepting state of M₂ (recognizing a string in L₂). Since NFAs and DFAs are equivalent in expressive power, L₁L₂ is regular. ∎

## 6. Closure Under Kleene Star

**Theorem:** If L is a regular language, then L\* (Kleene star) is also regular.

**Proof:** Let M = (Q, Σ, δ, q₀, F) be an NFA recognizing L. We construct an NFA M' for L\* as follows:

- Add a new start state q_s that is also accepting (to handle the empty string, which belongs to L\*)
- Add ε-transitions from q_s to the original start state q₀
- Add ε-transitions from every accepting state in F back to q₀ (to allow repetition)

Now M' can accept: the empty string (directly, since q_s is accepting), or any finite concatenation of strings from L (by traversing through the original automaton repeatedly via ε-transitions). Thus, L(M') = L\*, establishing closure under Kleene star. ∎

## 7. Closure Under Reversal

**Theorem:** If L is a regular language, then Lᴿ = {wᴿ | w ∈ L} is also regular, where wᴿ denotes the reversal of string w.

**Proof:** Let M = (Q, Σ, δ, q₀, F) be an NFA recognizing L. We construct an NFA M' for Lᴿ through the following systematic reversal:

- Reverse all transition directions: for every transition δ(p, a) = q in M, create a transition δ'(q, a) = p in M'
- The start state of M' is a new state q_s
- The accepting states of M' are {q₀} (the original start state)
- Add ε-transitions from q_s to all states in F (the original accepting states)

To accept a string wᴿ, M' must process wᴿ from some original accepting state of M (via an ε-transition from q_s) and reach the original start state q₀. This precisely corresponds to M accepting w when processing w forward. Therefore, L(M') = Lᴿ. ∎

## 8. Closure Under Homomorphism

**Theorem:** If L is a regular language and h: Σ → Δ\* is a homomorphism, then h(L) = {h(w) | w ∈ L} is also regular.

**Proof:** Let M = (Q, Σ, δ, q₀, F) be a DFA recognizing L. We construct a new DFA M' = (Q, Δ, δ', q₀, F) recognizing h(L). The transition function δ' is modified to account for the fact that input symbols from Δ\* may map to strings of varying lengths under h:

For each state q ∈ Q and each input symbol a ∈ Δ, we define δ'(q, a) to be the state reached by simulating the processing of h(a) in M. Specifically, if h(a) = a₁a₂...aₖ (where each aᵢ ∈ Σ), then δ'(q, a) = δ(δ(...δ(q, a₁), a₂...), aₖ).

The constructed DFA M' processes an input string by reading one symbol at a time from Δ\*, but internally simulates the processing of the corresponding homomorphic image in the original automaton M. Therefore, M' accepts exactly those strings that are homomorphic images of strings in L, establishing closure under homomorphism. ∎

## 9. Closure Under Inverse Homomorphism

**Theorem:** If L is a regular language and h: Σ → Δ* is a homomorphism, then h⁻¹(L) = {w ∈ Σ* | h(w) ∈ L} is also regular.

**Proof:** Let M = (Q, Δ, δ, q₀, F) be a DFA recognizing L. We construct a DFA M' = (Q, Σ, δ', q₀, F) recognizing h⁻¹(L). The transition function δ' is defined as follows:

For each state q ∈ Q and input symbol a ∈ Σ, we compute δ'(q, a) by determining where M would be after processing the entire string h(a). If h(a) = a₁a₂...aₖ, then:

δ'(q, a) = δ(δ(...δ(q, a₁), a₂...), aₖ)

This construction ensures that after processing any string w ∈ Σ*, M' reaches exactly the state that M would reach after processing h(w) ∈ Δ*. Consequently, M' accepts w if and only if h(w) ∈ L, meaning L(M') = h⁻¹(L). Thus, regular languages are closed under inverse homomorphisms. ∎

## 10. Closure Under Quotient

**Theorem:** If L₁ and L₂ are regular languages, then L₁/L₂ = {x | ∃y ∈ L₂ such that xy ∈ L₁} is also regular.

**Proof:** Let M₁ = (Q₁, Σ, δ₁, q₀₁, F₁) be a DFA for L₁. We construct a DFA M for L₁/L₂ as follows:

- Use the same state space Q₁ and start state q₀₁
- Modify the accepting condition: a state q is accepting in M if there exists some string y ∈ L₂ such that δ₁(q, y) ∈ F₁

To determine which states are accepting, we compute for each state q ∈ Q₁ whether there exists a path (labeled by some string y ∈ L₂) from q to some state in F₁. This can be computed using standard graph algorithms since L₂ is regular and we can construct a DFA for it. The resulting automaton accepts exactly those strings that can be extended by some string in L₂ to form a string in L₁, which is precisely L₁/L₂. ∎

## Worked Examples

### Example 1: Proving Non-Regularity Using Closure Properties

**Problem:** Prove that L = {aⁿbⁿ | n ≥ 1} is not regular using closure properties.

**Solution:**

Assume, for contradiction, that L is regular. Consider the regular language A = a* b*, which is easily proven regular (construct a DFA that reads any number of a's, then any number of b's, accepting only if the transition from a's to b's occurs exactly once).

Since regular languages are closed under intersection, L ∩ A = L would be regular. However, L ∩ A = {aⁿbⁿ | n ≥ 1}, which is well-known to be non-regular (provable via pumping lemma).

This contradiction establishes that L is not regular. ∎

### Example 2: Constructing DFA for Union

**Problem:** Construct a DFA for L = {w ∈ {a, b}\* | w contains at least one 'a' or ends with 'b'}

**Solution:**

Let L₁ = {w | w contains at least one 'a'}, which is regular. A DFA for L₁: states {q₀, q₁} where q₀ is start (non-accepting), q₁ is accepting. On input 'a', transition from q₀ to q₁; on other inputs, stay in respective states.

Let L₂ = {w | w ends with 'b'}, which is regular. A DFA for L₂: states {p₀, p₁} where p₀ is start, p₁ accepts. On input 'b', transition from p₀ to p₁; otherwise stay in current state; from p₁, on 'b' stay in p₁, else go to p₀.

Using product construction for union: states are (q₀,p₀), (q₀,p₁), (q₁,p₀), (q₁,p₁). Start state is (q₀,p₀). Accepting states are {(q₁,p₀), (q₀,p₁), (q₁,p₁)} (union condition). Define transitions per the product rule. The resulting DFA accepts exactly L. ∎

### Example 3: Applying Homomorphism

**Problem:** Given L = {aⁿbⁿ | n ≥ 0} (non-regular), show that h⁻¹(L) is regular for some homomorphism h.

**Solution:**

Define h: {c, d}_ → {a, b}_ by h(c) = a and h(d) = b. Consider L' = h⁻¹(c* d*) = {w ∈ {c, d}_ | h(w) ∈ c_ d\*}.

For any w ∈ {c, d}_, h(w) is simply replacing c with a and d with b. Thus, h(w) ∈ c_ d* means h(w) has all c's before all d's. This means w itself must have all c's before all d's (since homomorphism preserves order). Therefore, h⁻¹(c* d*) = c* d\*, which is regular. This illustrates how inverse homomorphisms can transform non-regular languages into regular ones. ∎

## Summary

Regular languages exhibit closure under all major operations: union, intersection, complement, difference, concatenation, Kleene star, reversal, homomorphism, inverse homomorphism, and quotient. These properties follow from constructive proofs using DFA product constructions, NFA transformations, and algebraic combinations. The practical significance lies in their utility for proving non-regularity, constructing complex regular languages from simpler ones, and applications in lexical analysis and pattern matching.
