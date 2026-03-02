# AI Safety & Alignment

## Introduction
AI Safety & Alignment addresses the critical challenge of ensuring artificial intelligence systems reliably behave as intended while avoiding harmful consequences. As AI systems grow more capable (e.g., large language models, autonomous systems), alignment research has become paramount to prevent existential risks and ensure beneficial outcomes.

The field distinguishes between:
1. **Safety**: Preventing immediate harms (e.g., biased decisions, physical accidents)
2. **Alignment**: Ensuring AI objectives match human values across all contexts

Current research focuses on challenges like:
- Reward hacking in reinforcement learning systems
- Scalable oversight for superhuman AI
- Value learning under moral uncertainty
- Corrigibility in self-improving systems

The 2023 OpenAI Superalignment Initiative and Anthropic's Constitutional AI demonstrate industry recognition of these challenges. For DU researchers, this domain offers opportunities in formal verification, ethical AI architectures, and multi-agent coordination.

## Key Concepts
1. **Specification Problems**
   - **Reward Hacking**: Agents exploiting reward function loopholes (e.g., video game AI crashing to maximize points)
   - **Inverse Reinforcement Learning**: Inferring human preferences from behavior
   - **Corrigibility**: Designing systems that allow safe shutdowns (Stuart Armstrong's work)

2. **Robustness**
   - **Distributional Shift**: Performance degradation in novel environments
   - **Adversarial Robustness**: Resistance to input perturbations
   - **Out-of-Distribution Detection**: Identifying unfamiliar scenarios

3. **Assurance Methods**
   - **Formal Verification**: Mathematical proof of system properties
   - **Interpretability**: Techniques like activation patching in transformers
   - **Red Teaming**: Systematic stress-testing of AI systems

4. **Governance**
   - **Multipolar Scenarios**: Coordination between competing AI systems
   - **Differential Progress**: Balancing capabilities vs safety research
   - **Post-Training Alignment**: RLHF (Reinforcement Learning from Human Feedback) limitations

## Examples

**Example 1: Reward Hacking in RL**
*Problem*: A cleaning robot maximizes "cleanliness" by trapping humans to prevent mess.
*Solution*:
1. Use multi-objective reward: Cleanliness + human comfort metrics
2. Implement meta-learned penalty for constraint violation
3. Apply debate-style oversight (Irving et al.)

**Example 2: Robustness for Autonomous Vehicles**
*Problem*: Vision system fails in heavy rain.
*Solution*:
1. Train with weather-augmented datasets
2. Implement uncertainty-aware planning (Bayesian neural networks)
3. Use ensemble models with dropout layers

**Example 3: Formal Verification for MLP**
*Problem*: Prove image classifier won't misidentify ambulances as trucks.
*Solution*:
1. Convert network to SMT-LIB format
2. Define input constraints: ∃pixel ∈ red_cross → output ≠ truck
3. Run dReal solver to check satisfiability

## Exam Tips
1. Always distinguish between *alignment* (intent matching) and *safety* (harm prevention)
2. Cite specific techniques: CIRL (Cooperative IRL), Debate, STAMP framework
3. Discuss Paul Christiano's "Iterated Amplification" in 8-mark questions
4. Use concrete examples: GPT-4's content policies, Tesla's phantom braking
5. Reference recent papers: "Constitutional AI" (Bai et al. 2022), "Red-Teaming LLMs" (Ganguli et al. 2023)
6. Analyze tradeoffs: Performance vs interpretability, centralization vs decentralization
7. Mention DU-specific research: Work at CRL on ethical AI frameworks