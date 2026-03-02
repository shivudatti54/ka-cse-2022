# Prim's Algorithm - Summary

## Key Definitions and Concepts

- MINIMUM SPANNING TREE (MST): A spanning tree with minimum total edge weight in a connected, weighted, undirected graph.
- SPANNING TREE: A subgraph containing all vertices without any cycles, having exactly (V-1) edges.
- CUT PROPERTY: For any cut in a graph, the minimum weight edge crossing the cut belongs to some MST.
- GREEDY CHOICE: At each step, select the minimum weight edge connecting the MST set to a vertex outside the set.

## Important Formulas and Theorems

- Number of edges in MST: |V| - 1
- Time complexity with array: O(V²)
- Time complexity with binary heap: O(E log V)
- Time complexity with Fibonacci heap: O(E + V log V)
- CUT PROPERTY: The minimum weight edge crossing any cut is guaranteed to be in some MST.

## Key Points

- Prim's Algorithm builds the MST by starting from an arbitrary vertex and growing one vertex at a time.
- The algorithm always selects the minimum weight edge connecting the MST to a new vertex.
- Any starting vertex produces an MST with the same total weight (though edges may differ with equal weights).
- The algorithm requires the graph to be connected; it cannot handle disconnected graphs.
- The data structure choice (array vs heap) significantly affects practical performance.
- Prim's Algorithm and Dijkstra's Algorithm have similar structures but different objective functions.
- The algorithm is optimal for dense graphs when implemented with arrays, and for sparse graphs when using heaps.

## Common Mistakes to Confusing Prim's with Dijkstra's

- Students often confuse Prim's with Dijkstra's because both use similar greedy approaches. Remember: Dijkstra minimizes PATH DISTANCE from source, while Prim minimizes EDGE WEIGHT connecting to the growing tree.
- Another mistake: forgetting to check graph connectivity before applying Prim's Algorithm.
- Using vertex distances instead of edge weights when updating keys is a common implementation error.

## Revision Tips

1. Practice tracing Prim's Algorithm manually for at least 5 different graphs of varying sizes.
2. Create a comparison table between Prim's, Kruskal's, and Dijkstra's algorithms covering approach, time complexity, and use cases.
3. Memorize the cut property statement as it frequently appears in proof questions.
4. Remember that Prim's is suitable when the graph is dense (using array implementation) or when a starting point is naturally defined in the problem.