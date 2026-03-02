# AI Safety and Alignment - Summary

## Key Definitions and Concepts

- **Alignment Problem**: The challenge of ensuring AI systems pursue the objectives humans actually intend, rather than literally specified but unintended goals.
- **Value Learning**: Approaches that learn human values from observation rather than explicit programming, including inverse reinforcement learning and preference learning.
- **Specification Problem**: The difficulty of precisely specifying objectives that capture human values, leading to unintended optimization of literal but incorrect goals.
- **Orthogonality Thesis**: The claim that any level of intelligence can combine with any set of goals; intelligence and goal content are independent.
- **Control Problem**: Whether humans can maintain meaningful control over AI systems more capable than humans in relevant domains.
- **RLHF (Reinforcement Learning from Human Feedback)**: Fine-tuning language models using human preference feedback through reward model learning and RL optimization.
- **Mechanistic Interpretability**: Reverse-engineering neural networks to identify specific circuits and components performing computations.

## Important Formulas and Theorems

- **IRL Objective**: Maximize probability of demonstrations: P(D|R) ∝ exp(Σ_τ R(τ)) / Z(R), where Z(R) is the partition function
- **CIRL Utility**: U(h, π) = R(θ, oᵃ) where the AI learns the human's reward parameter θ from observations
- **RLHF Loss**: L = E[R(p, a)] - β·KL(π||π₀), combining reward maximization with divergence penalty

## Key Points

- AI capability and alignment are orthogonal—a system can be extremely capable yet catastrophically misaligned
- The specification problem implies we cannot simply write down what we want; value learning approaches address this by learning from observation
- RLHF represents the most practical alignment success but has limitations: reward model errors, distributional failures, and reliance on human feedback quality
- The orthogonality thesis means advanced AI could have arbitrary goals—safety requires alignment, not just capability limitation
- Interpretability provides a path to auditing AI systems but currently scales poorly to complex models
- Constitutional AI attempts to reduce dependence on human feedback through explicit principles but raises questions about principle selection
- Current AI systems like GPT-4 and Claude are aligned through RLHF but remain imperfect—edge cases and novel situations reveal residual misalignment

## Common Mistakes to Avoid

- Confusing capability with alignment: more capable AI is not automatically safer
- Assuming explicit specification works: the specification problem makes this approach fundamentally limited
- Overestimating current alignment: RLHF is progress but not a complete solution
- Ignoring the control problem: even with perfect alignment, control mechanisms matter

## Revision Tips

1. Focus on the core distinction between capability and alignment, as this frames all safety considerations
2. Be able to walk through the RLHF pipeline from preference data collection to policy optimization
3. Understand why the specification problem motivates learning-based approaches to values
4. Review recent papers from Anthropic and DeepMind on alignment research for current context
5. Practice explaining the paperclip maximizer and King Midas examples clearly