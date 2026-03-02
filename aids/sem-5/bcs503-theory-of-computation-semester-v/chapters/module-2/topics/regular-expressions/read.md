# Regular Expressions

## What are Regular Expressions?

A declarative way to describe patterns (regular languages).

## Basic Syntax

| Symbol | Meaning | Example |
|--------|---------|---------|
| a | Literal character | a matches "a" |
| ε | Empty string | ε matches "" |
| ∅ | Empty language | Nothing matches |
| R₁R₂ | Concatenation | ab matches "ab" |
| R₁\|R₂ | Union (OR) | a\|b matches "a" or "b" |
| R* | Kleene star (0+) | a* matches "", "a", "aa"... |

## Operator Precedence

**Highest to Lowest:**
1. Parentheses ()
2. Kleene star *
3. Concatenation (implicit)
4. Union |

```
ab*|c = (a(b*))|c
NOT: (ab)*|c or a(b*|c)
```

## Extended Operators (Not in formal definition)

| Symbol | Meaning | Equivalent |
|--------|---------|------------|
| R+ | One or more | RR* |
| R? | Zero or one | R\|ε |
| [abc] | Character class | a\|b\|c |
| . | Any character | a\|b\|c\|... |
| R{n} | Exactly n times | RRR... (n times) |
| R{n,m} | n to m times | R^n \| R^(n+1) \| ... \| R^m |

## Examples

| Regex | Language |
|-------|----------|
| a* | {ε, a, aa, aaa, ...} |
| (ab)* | {ε, ab, abab, ...} |
| a*b* | {ε, a, b, aa, ab, bb, ...} |
| (a\|b)* | All strings over {a,b} |
| a(a\|b)*b | Starts with a, ends with b |
| (a\|b)*ab | Strings ending in "ab" |
| a*ba* | Exactly one b |

## Regex to NFA Conversion (Thompson's Construction)

### Base Cases
```
Regex: a            Regex: ε
──►(q0)──a──►((q1))   ──►((q0))

Regex: ∅
──►(q0)   (no accept state)
```

### Union: R₁|R₂
```
        ┌──ε──►[NFA for R₁]──ε──┐
──►(q0)─┤                        ├──►((qf))
        └──ε──►[NFA for R₂]──ε──┘
```

### Concatenation: R₁R₂
```
──►[NFA for R₁]──ε──►[NFA for R₂]──►
```

### Kleene Star: R*
```
            ε
        ┌───────────────┐
──►(q0)─┴──ε──►[NFA]──ε─┴──►((qf))
                │      ↑
                └──ε───┘
```

## NFA/DFA to Regex (State Elimination)

1. Add new start (connect to old start via ε)
2. Add new accept (connect from old accepts via ε)
3. Eliminate states one by one
4. Combine parallel edges with |
5. Combine sequential edges with concatenation

## Algebraic Laws

| Law | Expression |
|-----|------------|
| Union commutative | R\|S = S\|R |
| Union associative | (R\|S)\|T = R\|(S\|T) |
| Concat associative | (RS)T = R(ST) |
| Distributive | R(S\|T) = RS\|RT |
| Identity | Rε = εR = R |
| Annihilator | R∅ = ∅R = ∅ |
| Idempotent | R\|R = R |
| Star idempotent | (R*)* = R* |

## Equivalence Theorem

**Regular Expression ↔ NFA ↔ DFA ↔ Regular Language**

All four describe exactly the same class: Regular Languages.

## Common Patterns

```
Pattern                 | Regex
------------------------|------------------
Starts with 'a'         | a(a|b)*
Ends with 'b'           | (a|b)*b
Contains 'ab'           | (a|b)*ab(a|b)*
Even length             | ((a|b)(a|b))*
Odd number of a's       | b*(ab*ab*)*ab*
At least one a          | (a|b)*a(a|b)*
```

## Exam Tips

1. **Precedence**: * > concatenation > |
2. **ε vs ∅**: ε is empty string, ∅ is nothing
3. **a* includes ε** (zero or more)
4. **a+ = aa*** (one or more)
5. **(a|b)* = Σ*** for Σ = {a, b}
