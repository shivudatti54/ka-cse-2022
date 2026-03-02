# Properties of Regular Languages

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

In the study of formal languages and automata theory, **regular languages** represent one of the most fundamental and practically significant classes of formal languages. A language is said to be regular if it can be recognized by a deterministic finite automaton (DFA), a nondeterministic finite automaton (NFA), or expressed using a regular expression.

Understanding the properties of regular languages is crucial for several reasons:

1. **Theoretical Foundation**: Regular languages form the backbone of language theory, serving as a stepping stone to more complex language classes (context-free, context-sensitive, and recursively enumerable languages).

2. **Practical Applications**: Regular expressions are extensively used in text processing, lexical analysis compilers, pattern matching, network protocols, and many software engineering tasks.

3. **Algorithm Design**: The decision properties and closure properties of regular languages enable us to construct algorithms for language processing tasks.

This study material covers all essential properties of regular languages as per the Delhi University BSc (Hons) Computer Science syllabus under NEP 2024 UGCF, including closure properties, the pumping lemma, Myhill-Nerode theorem, decision properties, and DFA minimization.

---

## 2. Real-World Relevance

Regular languages and their properties have numerous practical applications:

- **Text Editors and Search Engines**: Regular expressions power search functionalities in editors like VS Code, grep, and search engines.
- **Lexical Analysis**: Compilers use regular expressions to tokenize source code (identifiers, keywords, operators).
- **Network Security**: Firewalls and intrusion detection systems use regular patterns to identify malicious traffic.
- **Data Validation**: Form validation (emails, phone numbers, dates) relies on regular expressions.
- **Bioinformatics**: Pattern matching in DNA sequences uses regular language concepts.
- **Natural Language Processing**: Finite-state automata model morphological analysis and spell checking.

---

## 3. Closure Properties of Regular Languages

A class of languages is **closed** under an operation if, when we apply that operation to languages in the class, the result is always a language in the same class. Regular languages exhibit closure under numerous operations, making them particularly useful.

### 3.1 Union

**Theorem**: If L₁ and L₂ are regular languages, then L₁ ∪ L₂ (their union) is also regular.

**Proof**: Since L₁ and L₂ are regular, there exist DFAs M₁ = (Q₁, Σ, δ₁, q₁, F₁) and M₂ = (Q₂, Σ, δ₂, q₂, F₂) recognizing them. We construct a product DFA M = (Q, Σ, δ, q₀, F) where:
- Q = Q₁ × Q₂
- q₀ = (q₁, q₂)
- F = {(r₁, r₂) | r₁ ∈ F₁ or r₂ ∈ F₂}
- δ((p₁, p₂), a) = (δ₁(p₁, a), δ₂(p₂, a))

M accepts a string w if and only if either M₁ accepts w or M₂ accepts w, thus accepting L₁ ∪ L₂.

### 3.2 Intersection

**Theorem**: If L₁ and L₂ are regular languages, then L₁ ∩ L₂ (their intersection) is also regular.

**Proof**: Using the same product construction as above, but with F = {(r₁, r₂) | r₁ ∈ F₁ and r₂ ∈ F₂}. The product DFA accepts exactly those strings accepted by both automata.

### 3.3 Complementation

**Theorem**: If L is a regular language, then Σ* - L (its complement) is also regular.

**Proof**: Given a DFA M = (Q, Σ, δ, q₀, F) recognizing L, we construct M' = (Q, Σ, δ, q₀, Q-F) by making all accepting states non-accepting and vice versa. M' accepts exactly those strings not accepted by M.

### 3.4 Difference

**Theorem**: If L₁ and L₂ are regular languages, then L₁ - L₂ is also regular.

**Proof**: L₁ - L₂ = L₁ ∩ (Σ* - L₂). Since regular languages are closed under intersection and complement, the result is regular.

### 3.5 Concatenation

**Theorem**: If L₁ and L₂ are regular languages, then L₁L₂ (their concatenation) is also regular.

**Proof**: Given NFAs for L₁ and L₂, connect all accepting states of the NFA for L₁ to the start state of the NFA for L₂ using ε-transitions.

### 3.6 Kleene Star

**Theorem**: If L is a regular language, then L* (Kleene star of L) is also regular.

**Proof**: Add a new start state that is also accepting, and connect all original accepting states back to the start state with ε-transitions.

### 3.7 Reversal

**Theorem**: If L is a regular language, then Lᴿ (reversal of L) is also regular.

**Proof**: Reverse all transitions in the DFA, make the original start state the only accepting state, and create a new start state with ε-transitions to all original accepting states.

### 3.8 Homomorphism

A **homomorphism** is a function h: Σ → Δ* that maps each symbol to a string. For a homomorphism h and language L, h(L) = {h(w) | w ∈ L}.

**Theorem**: If L is a regular language and h is a homomorphism, then h(L) is regular.

**Proof**: Replace each symbol a in the regular expression for L with h(a).

### 3.9 Inverse Homomorphism

**Theorem**: If L is a regular language and h is a homomorphism, then h⁻¹(L) is regular.

**Proof**: Given a DFA for L, construct a new automaton that simulates the effect of applying h inversely.

---

## 4. The Pumping Lemma for Regular Languages

The **Pumping Lemma** is a fundamental tool for proving that certain languages are **not** regular. It provides a necessary (but not sufficient) condition for regularity.

### 4.1 Statement

**Pumping Lemma**: Let L be an infinite regular language. Then there exists a positive integer p (the pumping length) such that every string w ∈ L with |w| ≥ p can be decomposed as w = xyz such that:

1. |y| > 0 (y is non-empty)
2. |xy| ≤ p (the first part has length at most p)
3. For all i ≥ 0, the string xyⁱz ∈ L

### 4.2 Proof

Since L is regular, there exists a DFA M = (Q, Σ, δ, q₀, F) recognizing it. Let p = |Q| (the number of states in the DFA).

Consider any string w ∈ L with |w| ≥ p. As we process w through the DFA, we encounter |w| + 1 states (including the start state). Since |w| ≥ p = |Q|, by the pigeonhole principle, at least one state q must be visited twice during the first p+1 transitions.

Let:
- x = the prefix leading to the first occurrence of q
- y = the substring causing the transition from q back to q
- z = the remaining suffix

Since y is non-empty (we traversed at least one transition), condition 1 holds. The path from the start to the second occurrence of q has at most p transitions, so |xy| ≤ p, satisfying condition 2.

For any i ≥ 0, we can traverse the y-loop i times, thus xyⁱz is accepted by M, proving condition 3.

### 4.3 Using the Pumping Lemma to Prove Non-Regularity

To prove a language L is not regular using the pumping lemma:

1. **Assume** L is regular (for contradiction)
2. Let p be the pumping length
3. **Choose** a specific string w ∈ L with |w| ≥ p
4. **Consider** all possible decompositions w = xyz with |y| > 0 and |xy| ≤ p
5. **Show** that for each decomposition, there exists some i such that xyⁱz ∉ L
6. This contradicts the pumping lemma, proving L is not regular

### 4.4 Examples

**Example 1: Proving L = {0ⁿ1ⁿ | n ≥ 0} is not regular**

*Proof*: Assume L is regular with pumping length p. Consider w = 0ᵖ1ᵖ. Since |w| = 2p ≥ p, w must be pumpable.

The string begins with p zeros, and |xy| ≤ p means xy consists only of zeros. Since |y| > 0, y = 0ᵏ for some k ≥ 1.

Pump with i = 2: xy²z = 0ᵖ⁺ᵏ1ᵖ

This string has more 0s than 1s, so it is not in L. Contradiction! Therefore, L is not regular.

**Example 2: Proving L = {ww | w ∈ {0,1}*} is not regular**

*Proof*: Assume L is regular with pumping length p. Consider w = 0ᵖ1ⁿ... wait, we need a string that clearly violates the pumping condition.

Consider w = 0ᵖ10ᵖ1 (a string of the form ww where w = 0ᵖ1). Actually, let w = 0ᵖ10ᵖ1. With |w| = 2p+2 ≥ p, we decompose w = xyz.

Since |xy| ≤ p, xy consists only of zeros. Let y = 0ᵏ with k ≥ 1.

For i = 2: xy²z has zeros in the first part increased by k, while the second half remains 0ᵖ1. The string is no longer of the form ww. Hence, not in L.

Therefore, L is not regular.

---

## 5. Myhill-Nerode Theorem

The **Myhill-Nerode theorem** provides a necessary and sufficient condition for regularity in terms of equivalence classes, making it a powerful characterization of regular languages.

### 5.1 Distinguishability and Equivalence

Two strings x and y are **distinguishable** with respect to a language L if there exists a string z such that exactly one of xz and yz is in L. Otherwise, x and y are **indistinguishable** (denoted x ≡_L y).

### 5.2 Statement of the Theorem

**Myhill-Nerode Theorem**: A language L ⊆ Σ* is regular if and only if the number of equivalence classes in the relation ≡_L (called the **index** of L) is finite. Furthermore, the minimum number of states in any DFA recognizing L equals the number of equivalence classes.

### 5.3 Proof Sketch

**(⇒) Direction**: If L is regular, let M = (Q, Σ, δ, q₀, F) be a minimal DFA for L. For each state q ∈ Q, there exists at least one string w that leads from q₀ to q. Define equivalence classes based on the state reached: w₁ ≡_L w₂ iff δ(q₀, w₁) = δ(q₀, w₂). Since |Q| is finite, there are finitely many equivalence classes.

**(⇐) Direction**: If ≡_L has finitely many equivalence classes, construct a DFA with one state for each equivalence class. Define transitions based on suffix extension. This DFA recognizes L.

### 5.4 Applications

1. **Proving non-regularity**: If L has infinitely many equivalence classes, it is not regular.
2. **DFA minimization**: The Myhill-Nerode relation characterizes the smallest possible DFA for a regular language.
3. **Understanding language structure**: Equivalence classes reveal the "states of memory" needed to recognize the language.

**Example**: For L = {0ⁿ1ⁿ | n ≥ 0}, strings 0ⁱ and 0ʲ are distinguishable for i ≠ j because appending 1ⁱ makes one in L and the other not. Thus, there are infinitely many equivalence classes, proving non-regularity.

---

## 6. Decision Properties of Regular Languages

Decision properties are algorithms that answer questions about regular languages.

### 6.1 Emptiness Test

**Problem**: Is L = ∅?

**Algorithm**: Check if any accepting state is reachable from the start state in the DFA. Use BFS/DFS from the start state; if no accepting state is reachable, L is empty.

**Complexity**: O(|Q| + |E|) where E is the set of transitions.

### 6.2 Finiteness Test

**Problem**: Is L finite?

**Algorithm**: Find if there exists a reachable state that is part of a cycle. If yes, infinite language; otherwise, finite.

**Alternative**: Using pumping lemma: L is infinite iff there exists a string w ∈ L with |w| ≥ p that can be pumped.

### 6.3 Membership Test

**Problem**: Does a given string w belong to L?

**Algorithm**: Simulate the DFA on w. If we end in an accepting state, w ∈ L.

**Complexity**: O(|w|)

### 6.4 Equivalence Test

**Problem**: Are L(M₁) = L(M₂) for two DFAs M₁ and M₂?

**Algorithm**: Check if the symmetric difference L(M₁) Δ L(M₂) is empty. Construct a product automaton and check if any state (p,q) where p is accepting but q is not (or vice versa) is reachable.

### 6.5 Containment Test

**Problem**: Is L(M₁) ⊆ L(M₂)?

**Algorithm**: Check if L(M₁) ∩ L(M₂)' = ∅ (intersection with complement is empty).

---

## 7. Minimization of Deterministic Finite Automata

DFA minimization produces the **unique** smallest DFA (by number of states) equivalent to the given DFA.

### 7.1 Distinguishable and Indistinguishable States

Two states p and q are **distinguishable** if there exists a string w such that exactly one of δ(p,w) and δ(q,w) is accepting. Otherwise, they are **indistinguishable** (equivalent).

### 7.2 The Minimization Algorithm

**Step 1**: Remove unreachable states (states not reachable from the start state).

**Step 2**: Initialize partition Π with two blocks: accepting states (F) and non-accepting states (Q-F).

**Step 3**: Refine the partition: for each block B in Π, if there exist states p, q ∈ B and symbol a such that δ(p,a) and δ(q,a) are in different blocks of Π, split B into smaller blocks where states have different transition behavior.

**Step 4**: Repeat Step 3 until no more splitting occurs (fixed point).

**Step 5**: Construct the minimized DFA: each block becomes a state; transitions follow the original transitions.

### 7.3 Example: Minimizing a DFA

Consider a DFA that accepts strings ending in "ab":

Original DFA states: q₀ (start), q₁ (seen 'a'), q₂ (seen 'ab'), accepting = {q₂}

Transitions:
- q₀: a→q₁, b→q₀
- q₁: a→q₁, b→q₂
- q₂: a→q₁, b→q₀

**Step 1**: All states reachable.

**Step 2**: Initial partition: {q₂} and {q₀,q₁}

**Step 3**: Check distinguishability:
- On 'a': q₀→q₁, q₁→q₁ (both in {q₀,q₁}) — OK
- On 'b': q₀→q₀, q₁→q₂ (different blocks!) — Split!

Now partition: {q₂}, {q₁}, {q₀}

**Step 4**: No further splitting possible.

**Minimized DFA**: Three states, which is optimal for this language.

---

## 8. Concrete Examples with Code

### Example 1: Implementing a Regular Language Checker in Python

```python
import re

def accepts_language(automaton, string):
    """Simulate a DFA to check if it accepts a string."""
    state = automaton['start']
    transitions = automaton['transitions']
    accept_states = automaton['accept']
    
    for symbol in string:
        if (state, symbol) in transitions:
            state = transitions[(state, symbol)]
        else:
            return False
    
    return state in accept_states

# Example: Language L = {w | w ends with 'ab'}
dfa = {
    'states': {'q0', 'q1', 'q2'},
    'alphabet': {'a', 'b'},
    'start': 'q0',
    'accept': {'q2'},
    'transitions': {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q0',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q1',
        ('q2', 'b'): 'q0'
    }
}

# Test cases
test_strings = ['ab', 'aab', 'b', 'bab', 'abc']
for s in test_strings:
    result = accepts_language(dfa, s)
    print(f"'{s}' -> {'Accepted' if result else 'Rejected'}")

# Using Regular Expression for verification
pattern = r'.*ab$'
print("\n--- Using Regex ---")
for s in test_strings:
    result = bool(re.match(pattern, s))
    print(f"'{s}' -> {'Accepted' if result else 'Rejected'}")
```

**Output**:
```
'ab' -> Accepted
'aab' -> Accepted
'b' -> Rejected
'bab' -> Accepted
'abc' -> Rejected

--- Using Regex ---
'ab' -> Accepted
'aab' -> Accepted
'b' -> Rejected
'bab' -> Accepted
'abc' -> Rejected
```

### Example 2: Implementing DFA Minimization Algorithm

```python
from collections import deque

def minimize_dfa(dfa):
    """Minimize a DFA using the partition refinement algorithm."""
    states = dfa['states']
    alphabet = dfa['alphabet']
    start = dfa['start']
    accept = dfa['accept']
    transitions = dfa['transitions']
    
    # Step 1: Remove unreachable states (simplified)
    reachable = {start}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        for symbol in alphabet:
            next_state = transitions.get((state, symbol))
            if next_state and next_state not in reachable:
                reachable.add(next_state)
                queue.append(next_state)
    
    # Step 2: Initial partition
    non_accept = reachable - accept
    partition = []
    if accept & reachable:
        partition.append(frozenset(accept & reachable))
    if non_accept:
        partition.append(frozenset(non_accept))
    
    # Step 3: Refine partition
    changed = True
    while changed:
        changed = False
        new_partition = []
        
        for block in partition:
            if len(block) <= 1:
                new_partition.append(block)
                continue
            
            # Try to split block
            subblocks = {}
            for state in block:
                # Create signature for this state
                signature = []
                for symbol in alphabet:
                    next_state = transitions.get((state, symbol))
                    if next_state:
                        # Find which block contains next_state
                        for i, b in enumerate(partition):
                            if next_state in b:
                                signature.append(i)
                                break
                    else:
                        signature.append(-1)  # Dead state
                
                sig_tuple = tuple(signature)
                if sig_tuple not in subblocks:
                    subblocks[sig_tuple] = set()
                subblocks[sig_tuple].add(state)
            
            if len(subblocks) > 1:
                changed = True
                for subblock in subblocks.values():
                    new_partition.append(frozenset(subblock))
            else:
                new_partition.append(block)
        
        partition = new_partition
    
    # Step 4: Build minimized DFA
    new_states = [f's{i}' for i in range(len(partition))]
    state_mapping = {}
    for i, block in enumerate(partition):
        for state in block:
            state_mapping[state] = i
    
    new_start = state_mapping[start]
    new_accept = {state_mapping[s] for s in accept if s in state_mapping}
    
    new_transitions = {}
    for (state, symbol), next_state in transitions.items():
        if state in state_mapping and next_state in state_mapping:
            new_transitions[(state_mapping[state], symbol)] = state_mapping[next_state]
    
    return {
        'states': set(new_states),
        'alphabet': alphabet,
        'start': new_start,
        'accept': new_accept,
        'transitions': new_transitions
    }

# Example usage
dfa = {
    'states': {0, 1, 2},
    'alphabet': {'a', 'b'},
    'start': 0,
    'accept': {2},
    'transitions': {
        (0, 'a'): 1,
        (0, 'b'): 0,
        (1, 'a'): 1,
        (1, 'b'): 2,
        (2, 'a'): 1,
        (2, 'b'): 0
    }
}

minimized = minimize_dfa(dfa)
print("Minimized DFA states:", minimized['states'])
print("Start state:", minimized['start'])
print("Accept states:", minimized['accept'])
print("Transitions:", minimized['transitions'])
```

---

## 9. Boolean Operations on Regular Languages

Boolean operations combine multiple languages using logical operators:

| Operation | Definition | Closure |
|-----------|------------|---------|
| Union | L₁ ∪ L₂ = {w \| w ∈ L₁ or w ∈ L₂} | Yes |
| Intersection | L₁ ∩ L₂ = {w \| w ∈ L₁ and w ∈ L₂} | Yes |
| Difference | L₁ - L₂ = {w \| w ∈ L₁ and w ∉ L₂} | Yes |
| Symmetric Difference | L₁ △ L₂ = (L₁ - L₂) ∪ (L₂ - L₁) | Yes |
| Complement | Σ* - L | Yes |

All Boolean operations preserve regularity because regular languages form a **Boolean algebra** — they are closed under union, intersection, and complement, and hence under all Boolean operations.

---

## 10. Common Mistakes and Exam Tips

### Common Mistakes to Avoid

1. **Confusing necessary and sufficient conditions**: The pumping lemma provides a necessary condition for regularity. A language satisfying the pumping lemma may still be non-regular.
2. **Incorrect pumping lemma application**: Always ensure |xy| ≤ p and |y| > 0 when applying the lemma.
3. **Forgetting to handle empty strings**: When proving non-regularity, consider whether ε belongs to the language.
4. **Ignoring the alphabet**: Always specify the alphabet when describing languages.
5. **Mixing up closure directions**: Remember that while regular languages are closed under union, intersection, complement, they are also closed under difference, symmetric difference, etc.

### Exam Tips

1. **Time Management**: For proof questions, outline the approach first, then write the formal proof.
2. **Pumping Lemma Questions**: Always state the lemma clearly before applying it. Choose a string that clearly leads to a contradiction.
3. **Myhill-Nerode**: Understand how to count equivalence classes. For {0ⁿ1ⁿ}, there are infinitely many classes.
4. **Closure Properties**: Remember all closure proofs use constructions (product automata, complementation, etc.)
5. **Decision Properties**: Know the algorithms and their complexities.
6. **Minimization**: Practice with at least 2-3 examples to master the partition refinement algorithm.
7. **Definitions**: Know all key definitions: pumping length, distinguishable states, Myhill-Nerode equivalence relation.

---

## 11. Key Takeaways

1. **Regular languages are closed under**:
   - Union, Intersection, Complementation
   - Difference, Symmetric Difference
   - Concatenation, Kleene Star
   - Reversal, Homomorphism, Inverse Homomorphism

2. **Pumping Lemma**: Essential tool for proving non-regularity. Every sufficiently long string in a regular language can be "pumped" while remaining in the language.

3. **Myhill-Nerode Theorem**: Provides necessary and sufficient condition for regularity through equivalence classes. The number of equivalence classes equals the minimum number of states in any DFA for the language.

4. **Decision Properties**:
   - Emptiness, finiteness, and membership are decidable
   - Equivalence and containment are decidable
   - All can be computed in polynomial time

5. **DFA Minimization**: Produces the unique smallest DFA equivalent to the given automaton using partition refinement.

6. **Boolean Algebra**: Regular languages form a Boolean algebra — they are closed under all Boolean operations.

---

## 12. Multiple Choice Questions (MCQs)

### Section A: Closure Properties

1. **If L₁ and L₂ are regular languages, which of the following is NOT necessarily regular?**
   - (a) L₁ ∪ L₂
   - (b) L₁ ∩ L₂
   - (c) L₁ - L₂
   - (d) None of the above
   
   **Answer: (d)** All are regular due to closure properties.

2. **The complement of a regular language is:**
   - (a) Always regular
   - (b) Never regular
   - (c) Sometimes regular
   - (d) Cannot be determined
   
   **Answer: (a)** Regular languages are closed under complementation.

3. **Which operation does NOT preserve regularity?**
   - (a) Union
   - (b) Intersection
   - (c) Reversal
   - (d) All preserve regularity
   
   **Answer: (d)** All listed operations preserve regularity.

### Section B: Pumping Lemma

4. **The pumping length p in the Pumping Lemma is:**
   - (a) Always 1
   - (b) Equal to the alphabet size
   - (c) The number of states in the minimal DFA
   - (d) Unlimited
   
   **Answer: (c)** p can be chosen as the number of states in any DFA recognizing the language.

5. **To prove L = {0ⁿ1ⁿ | n ≥ 1} is not regular using pumping lemma, a suitable string is:**
   - (a) 01
   - (b) 0ᵖ1ᵖ
   - (c) 0ᵖ¹1ᵖ¹
   - (d) 1⁽ᵖ⁾
   
   **Answer: (b)** 0ᵖ1ᵖ is the standard choice.

6. **The pumping lemma gives a necessary condition for:**
   - (a) Regularity
   - (Context-freeness)
   - (Recursively enumerability)
   - (None of these)
   
   **Answer: (a)** It is a necessary condition for regularity.

### Section C: Myhill-Nerode and Minimization

7. **According to Myhill-Nerode theorem, a language is regular if and only if:**
   - (a) It has finite number of equivalence classes
   - (b) It has infinite equivalence classes
   - (c) It can be expressed as a union of singleton sets
   - (d) None of the above
   
   **Answer: (a)** Finite number of equivalence classes characterizes regular languages.

8. **The minimum number of states in a DFA recognizing a regular language equals:**
   - (a) The pumping length
   - (b) The number of equivalence classes
   - (c) The alphabet size
   - (d) Infinity
   
   **Answer: (b)** Myhill-Nerode theorem states this equality.

9. **In DFA minimization, states that are indistinguishable are:**
   - (a) Always merged
   - (b) Never merged
   - (c) Sometimes merged
   - (d) None of the above
   
   **Answer: (a)** Indistinguishable states are merged into single states.

### Section D: Decision Properties

10. **Which of the following is NOT a decidable property of regular languages?**
    - (a) Emptiness
    - (b) Finiteness
    - (c) Whether the language is infinite
    - (d) Whether a given string is in the language
   
    **Answer: (d)** Wait, all are decidable. Let me reconsider... Actually (d) is also decidable (membership test). All are decidable! So technically (d) is also correct. Let me provide another option: **(d) Emptiness is not decidable** is wrong. Let me correct: All are decidable, but if forced to choose one: (d) is actually decidable too. The answer should be that all are decidable, but if only one option: none of these.

    Let me provide a corrected version: **Which is NOT a decision property?** (d) None — all are decision properties.

    **Correct answer**: (d) — actually all are decidable, so (d) "None of the above" is correct.

---

## 13. Flashcards

| Term | Definition |
|------|------------|
| **Regular Language** | A language recognized by a finite automaton (DFA or NFA) or expressible by a regular expression |
| **Closure Property** | A property where applying an operation to languages in a class always yields a language in the same class |
| **Pumping Lemma** | A theorem stating that every sufficiently long string in a regular language can be split into three parts and pumped while remaining in the language |
| **Pumping Length (p)** | The minimum number such that all strings of length ≥ p can be pumped; typically the number of states in the minimal DFA |
| **Myhill-Nerode Theorem** | A language is regular iff it has finitely many equivalence classes under the indistinguishability relation |
| **Distinguishable Strings** | Two strings x and y are distinguishable w.r.t. L if there exists z such that exactly one of xz, yz is in L |
| **Indistinguishable Strings** | Two strings are indistinguishable if for every continuation z, xz and yz are either both in L or both not in L |
| **DFA Minimization** | The process of reducing the number of states in a DFA while preserving the recognized language |
| **Product Automaton** | A construction used to show closure under intersection and other operations |
| **Decision Property** | An algorithm that answers a yes/no question about a language |
| **Emptiness Problem** | Determining whether a regular language is empty (contains no strings) |
| **Finiteness Problem** | Determining whether a regular language contains infinitely many strings |
| **Membership Problem** | Determining whether a specific string belongs to a language |
| **Equivalence Problem** | Determining whether two regular languages are the same |
| **Homomorphism** | A mapping from symbols to strings that can be applied to entire languages |

---

## 14. Conclusion

This comprehensive study material covers all essential properties of regular languages as required for the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus. The properties discussed — closure under various operations, the pumping lemma, Myhill-Nerode theorem, decision properties, and DFA minimization — form the theoretical foundation for understanding and working with regular languages.

These concepts are not only theoretically important but also have significant practical applications in compiler design, text processing, pattern matching, and many other areas of computer science. Mastery of these topics will provide a strong foundation for further studies in automata theory and formal languages.

---

*Study Material prepared for Delhi University, BSc (Hons) Computer Science, NEP 2024 UGCF Curriculum*