# Functions: Types and Compositions

## Introduction
Functions form the cornerstone of discrete mathematics with critical applications in computer science. A function f: A → B establishes a precise relationship between elements of domain A and codomain B, serving as fundamental building blocks for algorithms, database systems, and cryptographic protocols. In computer science, functions model real-world phenomena like hashing mechanisms, state transitions in finite automata, and memory address mappings.

The study of function types (injective, surjective, bijective) and compositions enables rigorous analysis of computational processes. For instance, bijective functions underpin reversible computations in quantum computing, while injective functions ensure unique identifiers in database systems. Composition operations are vital for function pipelining in functional programming and middleware architectures.

## Key Concepts
1. **Function Types**:
   - **Injective (One-to-One)**: ∀a₁,a₂ ∈ A, f(a₁)=f(a₂) ⇒ a₁=a₂
   - **Surjective (Onto)**: ∀b ∈ B, ∃a ∈ A such that f(a)=b
   - **Bijective**: Both injective and surjective
   - **Constant Function**: f(x) = c ∀x ∈ A
   - **Identity Function**: id_A(x) = x ∀x ∈ A

2. **Function Composition**:
   - For f: A → B and g: B → C, composition g∘f: A → C defined as (g∘f)(a) = g(f(a))
   - Properties:
     - Associativity: h∘(g∘f) = (h∘g)∘f
     - Identity: f∘id_A = f = id_B∘f

3. **Inverse Functions**:
   - For bijective f: A → B, ∃f⁻¹: B → A such that f∘f⁻¹ = id_B and f⁻¹∘f = id_A

4. **Characteristic Functions**:
   - Binary functions representing set membership: χ_S(x) = 1 if x ∈ S, 0 otherwise

## Examples
**Example 1: Proving Bijectivity**
Let f: ℝ → ℝ be defined as f(x) = 2x + 3
- **Injectivity**: Assume f(x₁)=f(x₂)
  ⇒ 2x₁+3 = 2x₂+3 ⇒ x₁=x₂
- **Surjectivity**: For any y ∈ ℝ, solve y=2x+3
  ⇒ x=(y-3)/2 ∈ ℝ
- **Conclusion**: Bijective. Inverse exists: f⁻¹(y) = (y-3)/2

**Example 2: Function Composition**
Given f(x) = x² and g(x) = x + 5:
- Compute (g∘f)(3):
  = g(f(3)) = g(9) = 14
- Compute (f∘g)(3):
  = f(g(3)) = f(8) = 64
- Demonstrates non-commutativity of composition

**Example 3: Inverse in Cryptography**
In AES encryption, the SubBytes step uses bijective S-box functions. For byte substitution:
- S: {0,1}⁸ → {0,1}⁸ is bijective
- Decryption requires S⁻¹ to reverse substitution

## Exam Tips
1. Always verify both injectivity and surjectivity when proving bijectivity
2. For composition f∘g, ensure codomain of g matches domain of f
3. Remember: All bijections on finite sets are permutations
4. In inverse problems, first confirm bijectivity before finding f⁻¹
5. Use counterexamples to disprove function properties
6. For characteristic functions, connect with bit vector representations
7. In algorithm analysis, identify function types in time/space complexity proofs