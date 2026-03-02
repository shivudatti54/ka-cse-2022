# Introduction to LR Parsing (Simple LR)

## Overview

SLR (Simple LR) parsing is a bottom-up technique that scans left-to-right, producing rightmost derivations in reverse. It uses LR(0) items with FOLLOW sets for lookahead, providing more power than LR(0) with manageable table sizes.

## Key Points

- **LR(0) Items**: Productions with dot (•) showing recognition progress (e.g., A → α•Xβ)
- **Closure Operation**: Expands item sets by adding B → •γ when [A → α•Bβ] exists
- **Goto Operation**: goto(I,X) moves dot across symbol X and computes closure
- **ACTION Table**: Specifies shift, reduce, accept, or error actions based on state and lookahead
- **GOTO Table**: Determines state transitions after reductions to non-terminals
- **SLR Lookahead**: Uses FOLLOW(A) for reduce actions [A → α•], simpler than canonical LR

## Important Concepts

- Canonical collection of LR(0) items forms parser states
- Shift-reduce and reduce-reduce conflicts indicate grammar limitations
- Augmented grammar adds S' → S for unique accept state
- Table construction: shift on terminals, reduce using FOLLOW sets

## Notes

- Always augment grammar first by adding S' → S
- Master closure operation - most common error source
- Practice building complete SLR tables from scratch
- Understand SLR's FOLLOW-based lookahead is sometimes too weak
