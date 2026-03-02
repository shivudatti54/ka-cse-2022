# Construction of SLR Parsing Tables

## Overview

SLR parsing table construction involves building a canonical collection of LR(0) item sets, computing FOLLOW sets, and populating ACTION/GOTO tables. This systematic process creates a shift-reduce parser that can handle a broad class of context-free grammars.

## Key Points

- **Augmentation**: Add S' → S production to create unique start state and accept condition
- **Item Sets**: Each state is closure of LR(0) items; I₀ = closure({[S' → •S]})
- **Closure**: For [A → α•Bβ], add all B → •γ productions recursively
- **Goto**: goto(I,X) moves dot across X and computes closure of resulting items
- **ACTION Entries**: Shift if [A → α•aβ] in Iᵢ; reduce using FOLLOW(A) if [A → α•] in Iᵢ
- **GOTO Entries**: For non-terminals, GOTO[i,A] = j when goto(Iᵢ,A) = Iⱼ
- **Conflicts**: Shift-reduce or reduce-reduce conflicts indicate grammar unsuitable for SLR

## Important Concepts

- FOLLOW sets critical for determining reduce action lookahead
- Viable prefixes never extend beyond handle
- Systematic state construction through closure and goto
- Table size remains small compared to canonical LR

## Notes

- Memorize construction sequence: augment → collection → FOLLOW → table
- Practice multiple examples to build intuition
- Verify tables can parse simple inputs correctly
