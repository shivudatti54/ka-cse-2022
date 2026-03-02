# Graph Analytics in Big Data

## Introduction
Graph analytics has emerged as a critical tool for analyzing complex relationships in big data. Unlike traditional tabular data analysis, graph-based approaches explicitly model entities (nodes) and their connections (edges), enabling insights into network structures, influence patterns, and connectivity dynamics. With the exponential growth of social networks, biological interactions, and IoT systems, graph analytics has become essential for applications ranging from fraud detection to epidemic modeling.

The importance of graph analytics in big data stems from its ability to handle scale and complexity. Modern graph frameworks like Apache Giraph and Spark GraphX can process billions of edges while supporting algorithms like community detection and centrality analysis. Recent research advances in graph neural networks (GNNs) and temporal graph analysis have further expanded its capabilities in dynamic network modeling.

For DU MSc CS students, mastering graph analytics provides a competitive edge in both industry and research. The university's focus on scalable computing aligns with India's Smart Cities Mission, where graph techniques analyze urban infrastructure networks. Current research at DU explores graph-based approaches for Aadhaar data analysis and disease spread modeling.

## Key Concepts
1. **Graph Representations**: 
   - Adjacency Matrix (O(n²) space) vs. Adjacency List (O(n+e))
   - Property Graphs (nodes/edges with attributes)
   - RDF Triples for semantic web data

2. **Centrality Measures**:
   - Betweenness Centrality: σ_st(v)/σ_st
   - PageRank: PR(u) = (1-d)/N + dΣ(PR(v)/L(v))
   - Eigenvector Centrality: Ax = λx

3. **Community Detection**:
   - Girvan-Newman Algorithm (edge betweenness)
   - Louvain Modularity: Q = 1/(2m)Σ[A_ij - (k_ik_j)/(2m)]δ(c_i,c_j)
   - Label Propagation Algorithm (LPA)

4. **Graph Query Languages**:
   - Cypher (Neo4j)
   - Gremlin (Apache TinkerPop)
   - SPARQL for RDF graphs

5. **Distributed Graph Processing**:
   - Bulk Synchronous Parallel (BSP) model
   - Vertex-centric programming (Think like a vertex)
   - Graph partitioning strategies (Edge-cut vs. Vertex-cut)

## Examples

**Example 1: Social Network Influence Analysis**
Problem: Identify top influencers in a 10M user network using PageRank.

Solution:
1. Represent users as nodes, follows as edges
2. Initialize all nodes with PR=1/N
3. Iterate: PR(u) = (1-d) + dΣ(PR(v)/out_degree(v))
4. Run for 20 iterations (convergence threshold 1e-6)
5. Top 10 nodes by PR score are influencers

**Example 2: Fraud Detection in Transaction Graphs**
Dataset: 5M transactions between 1M accounts

Steps:
1. Build bipartite graph: Accounts ↔ Transactions
2. Calculate weighted degree (number/frequency of transactions)
3. Apply Label Propagation to detect suspicious clusters
4. Validate using known fraud patterns (star structures, fast money movement)

**Example 3: COVID-19 Spread Modeling**
Use temporal graph with:
- Nodes: Individuals + Locations
- Edges: Contact duration + Mask status
- Apply SIR model with graph convolutional networks (GCNs) to predict infection spread

## Exam Tips
1. Focus on algorithm time complexity: BFS O(n+e) vs. Floyd-Warshall O(n³)
2. Memorize PageRank equation and damping factor implications (d=0.85 typical)
3. Understand tradeoffs: Adjacency matrix (fast edge lookup) vs. list (space efficiency)
4. Prepare real-world use cases: Recommendation systems (collaborative filtering as graph problem)
5. Know Hadoop ecosystem tools: Apache Giraph vs. GraphX (RDD vs. DataFrame API)
6. Practice drawing graph representations of sample problems
7. Revise recent DU research papers on graph neural networks for COVID modeling