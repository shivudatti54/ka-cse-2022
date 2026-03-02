# Introduction to Graph Theory - Summary

## Key Definitions and Concepts

- **Graph:** An ordered pair G = (V, E) where V is a set of vertices and E is a set of edges connecting pairs of vertices
- **Simple Graph:** No loops or multiple edges
- **Directed Graph (Digraph):** Edges have a specific direction
- **Undirected Graph:** Edges have no direction; uv = vu
- **Weighted Graph:** Each edge has an associated weight/cost
- **Adjacent Vertices:** Two vertices connected by an edge
- **Degree of Vertex:** Number of edges incident to the vertex
- **In-degree/Out-degree:** In directed graphs, edges entering/leaving a vertex
- **Path:** Sequence of vertices where consecutive pairs are connected by edges
- **Cycle:** A path that returns to its starting vertex
- **Connected Graph:** A path exists between every pair of vertices

## Important Formulas and Theorems

- **Handshaking Lemma:** Σ deg(v) = 2|E| (sum of all vertex degrees equals twice the number of edges)
- **Complete Graph (Kn):** Maximum edges = n(n-1)/2, each vertex has degree (n-1)
- **k-regular Graph:** Total edges = (n × k)/2
- **Bipartite Check:** A graph is bipartite if and only if it contains no odd-length cycles

## Key Points

1. Graph theory originated from Euler's solution to the Königsberg bridge problem in 1736

2. The Handshaking Lemma is fundamental and always applies to undirected graphs

3. A complete graph Kn has the maximum number of edges possible for n vertices

4. Bipartite graphs can be 2-colored with no adjacent vertices sharing the same color

5. In a cycle graph Cn, each vertex has degree 2

6. A wheel graph Wn consists of a cycle Cn-1 plus one central vertex connected to all cycle vertices

7. An isolated vertex has degree 0; a pendant vertex has degree 1

8. The sum of degrees in any graph is always even (due to Handshaking Lemma)

## Common Mistakes to Avoid

1. Confusing directed and undirected graphs - remember direction matters in digraphs

2. Forgetting that the Handshaking Lemma applies only to undirected graphs

3. Not checking for odd cycles when determining if a graph is bipartite

4. Miscounting edges in complete graphs - remember the formula n(n-1)/2

5. Overlooking that loops contribute 2 to the degree of a vertex (enters and leaves)

## Revision Tips

1. Practice drawing different types of graphs from their descriptions

2. Always verify the Handshaking Lemma when given degree information

3. Memorize the properties of special graphs: complete, bipartite, regular, cycle

4. Work through previous year university exam questions on basic definitions

5. Create a table comparing different types of graphs and their properties
