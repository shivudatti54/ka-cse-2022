# Divergence and Curl - Summary

## Key Definitions and Concepts

- **Del Operator (∇)**: ∇ = î(∂/∂x) + ĵ(∂/∂y) + k̂(∂/∂z) — a vector differential operator

- **Divergence (∇·F)**: For F = (P, Q, R), div F = ∂P/∂x + ∂Q/∂y + ∂R/∂z — produces a scalar field

- **Curl (∇×F)**: For F = (P, Q, R), ∇×F = î(∂R/∂y - ∂Q/∂z) + ĵ(∂P/∂z - ∂R/∂x) + k̂(∂Q/∂x - ∂P/∂y) — produces a vector field

## Important Formulas and Theorems

1. **Divergence of F = (P, Q, R)**: ∇·F = ∂P/∂x + ∂Q/∂y + ∂R/∂z

2. **Curl of F**: Computable via determinant method with del operator

3. **Identity 1**: ∇·(∇×F) = 0 — divergence of curl is always zero

4. **Identity 2**: ∇×(∇φ) = 0 — curl of gradient is always zero

5. **Conservative field**: If ∇×F = 0, then F = ∇φ for some scalar potential φ

6. **Solenoidal field**: If ∇·F = 0, then F = ∇×A for some vector potential A

## Key Points

- Divergence measures outward flux per unit volume; positive values indicate sources, negative indicate sinks

- Curl measures angular rotation/vorticity; zero curl means the field is irrotational (conservative)

- Both divergence and curl are linear operations: ∇·(F+G) = ∇·F + ∇·G, ∇×(F+G) = ∇×F + ∇×G

- In simply-connected domains, ∇×F = 0 is necessary and sufficient for F to be conservative

- Divergence produces scalar quantities; curl produces vector quantities

## Common Mistakes to Avoid

- Forgetting the negative sign in the ĵ-component when computing curl using the determinant method

- Confusing which operation produces scalar vs. vector output

- Applying curl to scalar fields (only gradient operates on scalars)

- Neglecting to check domain connectivity when classifying conservative fields

- Computing partial derivatives incorrectly due to missing variables in chain rule

## Revision Tips

1. Practice 3-4 problems computing both divergence and curl from scratch each time you review

2. Memorize the two fundamental identities: ∇·(∇×F) = 0 and ∇×(∇φ) = 0

3. Associate divergence with "source/sink" and curl with "rotation/spin" for quick recall

4. Use the determinant mnemonic for curl — it prevents sign errors in calculations

5. Solve past DU exam questions to understand the typical problem patterns and marking schemes