# Syntax Directed Definitions

## Overview

Syntax Directed Definitions (SDDs) associate semantic rules with grammar productions to specify translations systematically. They use synthesized and inherited attributes to compute values during parsing, enabling type checking, code generation, and symbol table management.

## Key Points

- **Synthesized Attributes**: Computed bottom-up from children to parent; suitable for LR parsing
- **Inherited Attributes**: Computed top-down from parent/siblings; suitable for LL parsing
- **S-Attributed SDDs**: Use only synthesized attributes; evaluated during reductions in LR parsers
- **L-Attributed SDDs**: Use both types with left-to-right evaluation restrictions; work with LL parsers
- **Dependency Graphs**: Show attribute computation order based on data flow
- **Applications**: AST construction, type checking, intermediate code generation, symbol table management

## Important Concepts

- Semantic rules define attribute computation
- Evaluation order determined by dependencies
- Integration with LR parsing through semantic actions during reductions
- Circular dependencies must be avoided through careful design

## Notes

- Remember SUID principle: Synthesized goes Up, Inherited goes Down
- S-attributed works with bottom-up (LR), L-attributed with top-down (LL)
- Practice drawing dependency graphs for attribute computation
