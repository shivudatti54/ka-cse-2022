# Coding Standards and Reviews - Summary

## Key Definitions and Concepts
- **Coding Standard**: Organizational rules for code structure/naming/documentation
- **Code Review**: Systematic examination of source code to find defects
- **Static Analysis**: Automated checking without code execution
- **Technical Debt**: Future costs from current code quality compromises

## Important Formulas and Theorems
- **Cyclomatic Complexity**: M = E - N + 2P (E=edges, N=nodes, P=connected components)
- **Halstead Volume**: V = N * log2(n) (N=total operators/operands, n=unique operators/operands)
- **Fagan's Yield**: Defects Found / (Defects Found + Defects Missed)

## Key Points
- Standards reduce cognitive load during maintenance
- Reviews catch 60-80% of defects before testing phase
- NASA's 10:1 ROI on formal inspections
- ISO/IEC 5055 defines maintainability indexes
- Shift-Left Testing integrates reviews early in SDLC
- GDPR/PCI-DSS compliance requires security-focused standards
- AI pair programmers (GitHub Copilot) require updated review practices

## Common Mistakes to Avoid
- Inconsistent naming (temp1 vs userInputBuffer)
- Missing null checks in reviewed code
- Treating code formatting as "just style"
- Approving PRs without understanding business context
- Ignoring static analysis tool warnings

## Revision Tips
1. Practice with OWASP Secure Coding Quick Reference Guide
2. Use CodeClimate CLI to analyze personal projects
3. Memorize CERT C++ Secure Coding Rules
4. Watch Google's "Code Review Best Practices" tech talk

Length: 650 words