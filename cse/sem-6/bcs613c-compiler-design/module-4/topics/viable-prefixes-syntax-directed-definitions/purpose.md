### Learning Purpose: Viable Prefixes and Syntax-Directed Definitions

**1. Why is this topic important?**
Viable prefixes provide the theoretical foundation for understanding why LR parsing works -- they characterize exactly which stack contents are valid during a shift-reduce parse. Syntax-Directed Definitions (SDDs) extend parsing by attaching semantic rules to grammar productions, enabling the compiler to compute meaning (types, values, intermediate code) during parsing.

**2. Real-world applications:**
SDDs with synthesized and inherited attributes are used in production compilers to perform type checking, constant folding, and intermediate code generation. Tools like Yacc/Bison allow developers to embed semantic actions directly in grammar rules, implementing SDDs that generate abstract syntax trees, symbol tables, and three-address code.

**3. Connection to other topics:**
Viable prefixes connect to LR parsing theory by explaining the valid stack configurations during bottom-up parsing. SDDs bridge the gap between syntax analysis (Modules 3-4) and semantic analysis/code generation (Module 5), as they provide the mechanism for translating parse trees into intermediate representations and ultimately into target code.
