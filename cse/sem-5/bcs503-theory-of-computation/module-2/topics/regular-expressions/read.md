# Regular Expressions

## Introduction

Regular expressions (regex or regexp) constitute a fundamental notation for describing regular languages within the formal framework of Theory of Computation. In the context of Formal Language and Automata Theory, regular expressions provide a declarative, algebraic mechanism for representing patterns that can be recognized by finite automata. This dual representation—state-based (automata) versus pattern-based (expressions)—offers complementary perspectives on regular languages and establishes the theoretical foundation for lexical analysis, text processing, and pattern matching applications in computer science.

The equivalence between regular expressions and finite automata represents one of the central results in automata theory. A language is regular if and only if it can be expressed by a regular expression, establishing the expressive completeness of both formalisms. This result enables practitioners to choose the most convenient representation—whether for theoretical analysis, practical implementation, or algorithmic manipulation—depending on the problem at hand.

## Formal Definition of Regular Expressions

### Recursive Definition

Let Σ denote an alphabet. The set of regular expressions over Σ is defined recursively as follows:

**Base Cases:**

1. **Empty String**: ε is a regular expression denoting the language {ε}
2. **Symbols**: For each a ∈ Σ, the symbol 'a' is a regular expression denoting the language {a}
3. **Empty Set**: ∅ (or φ) is a regular expression denoting the empty language

**Inductive Cases:** 4. **Union**: If r₁ and r₂ are regular expressions, then (r₁ + r₂) is a regular expression denoting L(r₁) ∪ L(r₂) 5. **Concatenation**: If r₁ and r₂ are regular expressions, then (r₁r₂) is a regular expression denoting L(r₁)L(r₂) = {xy | x ∈ L(r₁), y ∈ L(r₂)} 6. **Kleene Star**: If r is a regular expression, then (r)_ is a regular expression denoting L(r)_ = {ε} ∪ {x₁x₂...xₙ | n ≥ 1, xᵢ ∈ L(r)}

Parentheses may be omitted when precedence rules apply.

### Semantics: Language of a Regular Expression

The language L(r) denoted by a regular expression r is formally defined:

- L(ε) = {ε}
- L(a) = {a} for a ∈ Σ
- L(∅) = ∅
- L(r₁ + r₂) = L(r₁) ∪ L(r₂)
- L(r₁r₂) = L(r₁)L(r₂)
- L(r*) = L(r)*

## Operator Precedence and Algebraic Properties

### Precedence Hierarchy

From highest to lowest precedence:

1. Kleene Star (\*)
2. Concatenation (juxtaposition)
3. Union (+)

Parentheses override default precedence.

### Algebraic Laws

The following identities hold for all regular expressions r, r₁, r₂, r₃:

**Associativity:**

- (r₁ + r₂) + r₃ = r₁ + (r₂ + r₃)
- (r₁r₂)r₃ = r₁(r₂r₃)

**Commutativity:**

- r₁ + r₂ = r₂ + r₁

**Distributivity:**

- r₁(r₂ + r₃) = r₁r₂ + r₁r₃
- (r₁ + r₂)r₃ = r₁r₃ + r₂r₃

**Identity Elements:**

- εr = rε = r (concatenation identity)
- ∅ + r = r + ∅ = r (union identity)

**Annihilator:**

- ∅r = r∅ = ∅

**Idempotence:**

- r + r = r

**Star Properties:**

- r* = r*r* = (r*)\*
- ε + rr* = r* (proved by substitution)

## Arden's Theorem: Solving Regular Expression Equations

### Statement

Arden's Theorem provides a method for solving equations of the form X = AX ∪ B, where A and B are regular expressions and X is an unknown:

**Theorem:** If A does not contain ε, then the unique solution is X = A*B. If A contains ε, then the solutions are X = A*B ∪ C for any C ⊆ A\*.

### Formal Proof

Given X = AX ∪ B:

1. **Existence**: Let X = A\*B. Then:
   - AX ∪ B = A(A*B) ∪ B = (AA*)B ∪ B = A+B ∪ B = A\*B = X

2. **Uniqueness**: Assume X = X₁ is any solution:
   - X₁ = AX₁ ∪ B
   - Iterating: X₁ = AⁿX₁ ∪ (Aⁿ⁻¹B ∪ ... ∪ AB ∪ B)
   - As n → ∞ and A contains no ε: Aⁿ → ∅
   - Hence X₁ = A\*B

**Example:** Solve X = aX ∪ b:

- By Arden's Theorem: X = a*b = a*b
- Verification: a(a*b) ∪ b = a+b ∪ b = a*b ✓

## Equivalence: Regular Expressions and Finite Automata

### Theorem

A language L is regular if and only if ∃ a regular expression r such that L = L(r).

### Part I: Regular Expression → NFA (Thompson's Construction)

**Algorithm:** Given regex r, construct NFA N = (Q, Σ, δ, q₀, F) recursively:

**Base Cases:**

- For ε: Create N with two states, ε-transition from start to accept
- For a ∈ Σ: Create N with two states, transition on a from start to accept

**Inductive Construction:**

- **Union**: For r₁ + r₂, create new start and accept states; add ε-transitions to parallel NFAs
- **Concatenation**: Connect accept state of N₁ to start state of N₂ via ε; merge start/accept
- **Kleene Star**: Create new start/accept; connect in cycle via ε-transitions

**Complexity:** Resulting NFA has at most 2m states where m = |symbols| + |operators|

### Part II: NFA → Regular Expression (State Elimination)

**Algorithm:**

1. Add new start state s₀ with ε-transition to original start
2. Add new accept state f with ε-transitions from original accepts
3. Eliminate states one by one (except s₀ and f)
4. For each eliminated state, compute regex labels on incoming/outgoing arcs
5. When only s₀ and f remain, the label on (s₀, f) is the required expression

**Theorem Justification:** Elimination preserves the language accepted; final regex equals L(NFA).

## Extended Regular Expressions

Practical implementations include syntactic sugar:

- **Positive Closure**: r+ = rr\* (one or more occurrences)
- **Optional**: r? = ε + r (zero or one occurrence)
- **Character Classes**: [abc] = a + b + c
- **Negation**: [^abc] = Σ \ {a,b,c}
- **Ranges**: [a-z] = a + b + ... + z
- **Shorthands**: \d = [0-9], \w = [a-zA-Z0-9_], \s = whitespace
- **Quantifiers**: r{n,m} = repeated n to m times

Note: r+ = r\* - ε and r? = r + ε

## Worked Examples

### Example 1: Binary Strings with Even Number of 1s

**Problem:** Construct RE for strings over {0,1} with even number of 1s.

**Solution:**

- Strings with zero 1s: 0\*
- Each pair of 1s: 10*10*
- Complete expression: 0*(10*10*)*

**Verification:**

- ε: 0\* → ε ✓
- 0: 0\* → 0 ✓
- 11: 0* → ε, then 10*10\* → 11 ✓
- 101: 0* → ε, then 10*10\* → 101 ✓

### Example 2: Applying Arden's Theorem

**Problem:** Find regex for language (0+1)_01(0+1)_

**Solution:** Let X = (0+1)_01(0+1)_

- Rearranging: X = (0+1)\*01X ∪ ε (accounting for prefix/suffix)
- By Arden's: X = ((0+1)*01)*ε = ((0+1)_01)_

### Example 3: Thompson's Construction

**Problem:** Construct NFA for (a + b)\*ab

**Construction:**

- Build NFAs for 'a' and 'b' (base cases)
- Build NFA for (a + b) using union construction
- Build NFA for (a + b)\* using star construction
- Concatenate: (a + b)\* → a → b
- Result: ~10 states with appropriate transitions

---

## Assessment

### Multiple Choice Questions

**Question 1:** Given the regex r = (a + b)\*ab, which of the following strings is NOT in L(r)?

A) ab  
B) aab  
C) bab  
D) bba

**Answer:** D) bba  
**Explanation:** The regex requires any number of (a or b) followed by 'a' then 'b'. The string bba ends with 'ba', not 'ab'.

**Question 2:** Using Arden's Theorem, the solution to X = aX ∪ bX ∪ c is:

A) (a + b)_c  
B) c(a + b)_  
C) (a + b + c)*  
D) (a + b)*c(a + b)\*

**Answer:** A) (a + b)*c  
**Explanation:** X = (a + b)X ∪ c. By Arden's Theorem with A = (a + b), B = c: X = (a + b)*c.

**Question 3:** In Thompson's construction for regex (a + b)\*, the number of states in the resulting NFA is:

A) 2  
B) 4  
C) 6  
D) 8

**Answer:** B) 4  
**Explanation:** (a + b)\* requires: base a (2 states), base b (2 states), union (adds 2 states), star (adds 2 states) = 8 total, but final minimization yields 4 accessible states.

**Question 4:** Which algebraic law allows transformation of r₁(r₂ + r₃)?

A) Commutative  
B) Associative  
C) Distributive  
D) Idempotent

**Answer:** C) Distributive  
**Explanation:** r₁(r₂ + r₃) = r₁r₂ + r₁r₃ is the left distributive law.

### Flashcards

**Q1:** What is the language L(a*b*)?  
**A:** {aⁿbᵐ | n ≥ 0, m ≥ 0} - all strings of zero or more a's followed by zero or more b's

**Q2:** State Arden's Theorem.  
**A:** For equation X = AX ∪ B where ε ∉ L(A), the unique solution is X = A\*B
