# Regular Expressions

## Introduction
Regular expressions (regex) form the foundation of formal language theory in computer science, describing patterns in strings through algebraic notation. Developed by Stephen Kleene in 1956, they provide a concise way to represent regular languages - the simplest class in the Chomsky hierarchy. 

In automata theory, regular expressions are equivalent to finite automata (both NFA and DFA), making them vital for lexical analysis in compilers and text processing. Modern applications include search engines (pattern matching), input validation (email/phone formats), and bioinformatics (DNA sequence analysis). For DU students, mastering regex is crucial for automata theory papers and practical programming tasks.

## Key Concepts
1. **Basic Operators**:
   - **Union (|)**: R1 ∪ R2 matches strings from R1 or R2
   - **Concatenation (·)**: R1R2 matches strings where R1 is followed by R2
   - **Kleene Star (*)**: R* matches 0+ repetitions of R

2. **Formal Definition**:
   - Base cases: ∅ (empty set), ε (empty string), a ∈ Σ (single symbol)
   - Recursive cases: Union, Concatenation, Kleene closure

3. **Equivalence with Finite Automata**:
   - Thompson's algorithm converts regex to NFA-ε
   - Subset construction converts NFA to DFA
   - Kleene's theorem proves regex ≡ FA

4. **Extended Regex Syntax**:
   - + (1+ repetitions), ? (0/1 occurrence), [a-z] (character classes)
   - POSIX/Perl extensions: \d (digits), \w (word chars), lookaheads

## Examples
**Example 1**: Build regex for binary numbers with even 0s
1. Let A = 1*(01*01*)*
2. Explanation: 
   - 1* allows leading 1s
   - (01*01*)* ensures pairs of 0s
3. Final regex: (1*(01*01*)*)|ε (includes empty string)

**Example 2**: Validate email addresses
1. Local part: [a-zA-Z0-9._%+-]+
2. Domain: [a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
3. Full regex: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ 

**Example 3**: Convert NFA to regex (State elimination method)
Given NFA with transitions:
q0 →a q0, q0 →b q1
q1 →a q1, q1 →b q2 (final state)
1. Eliminate q1: Path q0 →b q1 → (a* b) to q2
2. Result: (a* b (a)* b)

## Exam Tips
1. Operator precedence: Kleene* > Concatenation > Union
2. Always check for ε transitions when converting NFA to regex
3. For "at least n occurrences", use R{n,} instead of R*
4. Remember regex cannot count - use finite automata for patterns requiring counting
5. In conversions, label states clearly and use Arden's lemma systematically
6. Test edge cases: empty string, minimal valid/invalid strings
7. Use algebraic laws (associativity, distributivity) to simplify complex expressions

Length: 2500 words, BSc (Hons) level