# Probabilistic Models for Link Prediction

## Introduction to Probabilistic Link Prediction

Link prediction is a fundamental task in social network analysis that aims to predict the existence of future or missing links between nodes in a network. While heuristic methods rely on similarity scores between nodes, probabilistic models take a more rigorous statistical approach by modeling the network generation process and calculating the probability that a link exists between two nodes.

Probabilistic models frame link prediction as a statistical inference problem: given an observed network G, what is the probability that a particular unobserved link (u,v) exists? These models can be broadly categorized into two types: **graph-based probabilistic models** that use the structure of the network, and **feature-based probabilistic models** that incorporate node attributes and other features.

## Key Concepts in Probabilistic Approaches

### Maximum Likelihood Estimation (MLE)

At the core of probabilistic link prediction is the principle of maximum likelihood estimation. Given a probabilistic model with parameters θ, we seek to find the parameter values that maximize the likelihood of observing the network data:

L(θ|G) = P(G|θ)

For link prediction, we're particularly interested in the probability that a specific edge exists:

P(Aₑ = 1|G, θ)

where Aₑ is the adjacency matrix entry for edge e.

### Bayesian Framework

Many probabilistic models employ a Bayesian approach that incorporates prior knowledge:

P(θ|G) ∝ P(G|θ) × P(θ)

This allows us to incorporate domain knowledge through the prior distribution P(θ) and update our beliefs as we observe more network data.

## Common Probabilistic Models

### Stochastic Block Models (SBM)

Stochastic Block Models assume that nodes belong to latent groups or communities, and the probability of a link between two nodes depends solely on their group memberships.

Let's define:

- K: number of groups
- zᵢ: group membership of node i
- Ω: K×K matrix where Ωₐₑ is the probability of link between group a and group b

The probability of an edge between i and j is:
P(Aᵢⱼ = 1) = Ω\_{zᵢzⱼ}

```
Example Network with 2 Groups:

Group 1: Nodes A, B, C
Group 2: Nodes D, E, F

Ω = [0.8  0.1]
    [0.1  0.7]

So:
- P(link within Group 1) = 0.8
- P(link within Group 2) = 0.7
- P(link between groups) = 0.1
```

### Latent Feature Models

These models assume that each node has latent features that determine connection probabilities. The most common approach is using Euclidean distance in a latent space:

P(Aᵢⱼ = 1) = logistic(β - d(zᵢ, zⱼ))

where zᵢ and zⱼ are the latent positions of nodes i and j, d() is a distance function, and β is a parameter.

### Probabilistic Matrix Factorization

This approach factorizes the adjacency matrix into low-rank matrices representing latent node features:

A ≈ U×Vᵀ

where U and V are n×k matrices (n = number of nodes, k = latent dimension), and the probability of a link is modeled as:

P(Aᵢⱼ = 1) = σ(uᵢᵀvⱼ)

where σ is the logistic function.

## Implementation Workflow

The typical workflow for probabilistic link prediction involves:

1. **Model Selection**: Choose an appropriate probabilistic model
2. **Parameter Estimation**: Estimate model parameters using observed data
3. **Probability Calculation**: Compute link probabilities for all node pairs
4. **Prediction**: Rank node pairs by their predicted probabilities

```
Data Flow Diagram:

Observed Network → Model Fitting → Parameter Estimates → Probability Calculation → Ranked Predictions
         ↓               ↓                 ↓                     ↓
     Training Data   MLE/Bayesian   P(link|model, params)   Top-K predictions
```

## Comparison of Probabilistic Models

| Model                          | Strengths                                              | Weaknesses                                            | Best For                                       |
| ------------------------------ | ------------------------------------------------------ | ----------------------------------------------------- | ---------------------------------------------- |
| Stochastic Block Model         | Captures community structure, interpretable            | Assumes discrete communities, may oversimplify        | Networks with clear community structure        |
| Latent Distance Model          | Captures homophily, intuitive geometric interpretation | Struggles with structural equivalence                 | Social networks with spatial organization      |
| Matrix Factorization           | Scalable, handles sparse data                          | Less interpretable, black-box nature                  | Large networks with many nodes                 |
| Exponential Random Graph Model | Flexible, incorporates various network features        | Computationally intensive, may have degeneracy issues | Networks where specific features are important |

## Practical Example: Predicting Co-authorship

Let's consider a co-authorship network where we want to predict future collaborations. Using a Stochastic Block Model:

1. We might discover that researchers naturally cluster into subfields
2. Within-subfield collaboration probability might be high (e.g., 0.7)
3. Cross-subfield collaboration probability might be lower (e.g., 0.2)
4. For any two researchers, we can calculate P(collaboration) based on their inferred subfields

## Advanced Topics

### Temporal Probabilistic Models

For dynamic networks, we can extend probabilistic models to incorporate temporal evolution:

P(Aᵢⱼ(t) = 1) = f(θ(t), historical patterns)

where θ(t) are time-varying parameters.

### Incorporating Node Attributes

Many probabilistic models can be extended to include node features:

P(Aᵢⱼ = 1) = f(zᵢ, zⱼ, xᵢ, xⱼ)

where xᵢ and xⱼ are attribute vectors for nodes i and j.

## Evaluation Metrics

Probabilistic models are typically evaluated using:

1. **Area Under ROC Curve (AUC)**: Measures ranking quality
2. **Precision@k**: Proportion of correct predictions in top-k
3. **Log-likelihood**: Measures how well the model explains the data
4. **Brier Score**: Measures calibration of probability forecasts

## Exam Tips

1. **Understand the assumptions**: Each probabilistic model makes specific assumptions about network formation - be prepared to explain these.

2. **Compare and contrast**: Be able to discuss when to use probabilistic vs. heuristic approaches and different probabilistic models.

3. **Interpret parameters**: For models like SBM, understand what the block matrix Ω represents.

4. **Calculation practice**: Be comfortable with basic probability calculations involving these models.

5. **Real-world applications**: Think about how these models would apply to specific network types (social, biological, information).

6. **Focus on trade-offs**: Understand the computational vs. accuracy trade-offs in different models.

7. **Bayesian thinking**: Remember that Bayesian approaches incorporate prior knowledge and update beliefs with evidence.
