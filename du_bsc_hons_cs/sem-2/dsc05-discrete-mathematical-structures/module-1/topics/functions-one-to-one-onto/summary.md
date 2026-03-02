# Functions: One-to-One and Onto - Summary

## Key Definitions and Concepts

- **Function**: A relation f: A → B where every element of A maps to exactly one element in B. A is the domain, B is the codomain.
- **One-to-One (Injective)**: f(a₁) = f(a₂) ⇒ a₁ = a₂. Different domain elements have different images.
- **Onto (Surjective)**: For every b ∈ B, ∃a ∈ A such that f(a) = b. The range equals the codomain.
- **Bijective**: A function that is both one-to-one and onto. Has an inverse.
- **Inverse Function**: f⁻¹(b) = a if and only if f(a) = b. Exists only for bijections.

## Important Formulas and Theorems

- f is one-to-one: f(a₁) = f(a₂) ⇒ a₁ = a₂
- f is onto: f(A) = B (range equals codomain)
- Linear function f(x) = ax + b is injective if a ≠ 0
- Composition: (g ∘ f)(a) = g(f(a))
- If f and g are one-to-one, then g ∘ f is one-to-one
- If f and g are onto, then g ∘ f is onto
- Pigeonhole Principle: If |A| > |B|, no injection exists. If |A| < |B|, no surjection exists.

## Key Points

- A function requires every domain element to have exactly one image
- One-to-one ensures distinct inputs produce distinct outputs
- Onto ensures all codomain elements are "covered" by the mapping
- Bijections establish perfect one-to-one correspondence between sets
- Inverse functions reverse the mapping—only exist for bijections
- Hash functions typically cannot be injective when domain > codomain (collisions are inevitable)
- Composition of functions preserves injectivity and surjectivity

## Common Mistakes to Avoid

- Confusing domain with codomain—they are different sets
- Forgetting that a function must map EVERY element of the domain
- Claiming an inverse exists without first proving bijectivity
- Assuming "one-to-one" implies "onto" (or vice versa)—they are independent properties
- Using the wrong test: confusing the conditions for injectivity and surjectivity

## Revision Tips

1. Practice the formal proofs: always start with "Assume f(a₁) = f(a₂)" for injectivity
2. For onto proofs, solve f(x) = y for x and verify x is in the domain
3. Draw mapping diagrams for finite sets to visualize injectivity/surjectivity
4. Memorize that bijective functions have inverses; all other functions do not
5. Remember the cardinality constraints from the pigeonhole principle